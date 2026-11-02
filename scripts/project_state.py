"""Local evidence snapshots, ledger transitions and safe project resumption.

Stdlib only. No network or model calls. File verification proves byte identity,
not scientific correctness. Mutations require explicit output paths.
"""
import argparse
import copy
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import tempfile

import validate_artifacts as checks


def load(path):
    return checks.read_json(path)


def now():
    return datetime.now(timezone.utc).isoformat()


def atomic_save(path, data, expected="missing"):
    """Cooperating writers lock + compare-and-swap + immutable prior snapshot."""
    path = Path(path).resolve()
    path.parent.mkdir(parents=True, exist_ok=True)
    lock = path.with_name(path.name + ".lock")
    try:
        descriptor = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        raise ValueError(f"writer lock exists: {lock}; inspect owner before manual recovery")
    temporary = None
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
            json.dump({"pid": os.getpid(), "at": now(), "target": str(path)}, stream)
            stream.flush()
            os.fsync(stream.fileno())
        actual = checks.file_hash(path) if path.exists() else "missing"
        if actual != expected.strip().lower().removeprefix("sha256:"):
            raise ValueError(f"concurrent/stale write: expected {expected}, found {actual}")
        if actual != "missing":
            history = path.parent / ".history"
            history.mkdir(exist_ok=True)
            backup = history / f"{path.name}.{actual}.json"
            if backup.exists():
                if checks.file_hash(backup) != actual:
                    raise ValueError(f"history collision: {backup}")
            else:
                with backup.open("xb") as stream:
                    stream.write(path.read_bytes())
                    stream.flush()
                    os.fsync(stream.fileno())
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent,
                                         prefix=f".{path.name}.", suffix=".tmp", delete=False) as stream:
            temporary = Path(stream.name)
            json.dump(data, stream, ensure_ascii=False, indent=2)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
        temporary = None
        return checks.file_hash(path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
        lock.unlink(missing_ok=True)


def snapshot(root, files):
    records = {}
    for value in files:
        path = checks.local_path(root, value)
        relative = path.relative_to(Path(root).resolve()).as_posix()
        digest = checks.file_hash(path)
        records[relative] = {"path": relative, "version": "sha256:" + digest, "sha256": digest}
    return records


def transition(ledger, ident, status, reason, evidence, root, sources):
    errors = checks.validate_ledger(ledger)
    if errors:
        raise ValueError("; ".join(errors))
    result = copy.deepcopy(ledger)
    issue = next((i for i in result["issues"] if i["id"] == ident), None)
    if issue is None:
        raise ValueError(f"unknown issue: {ident}")
    if not reason.strip():
        raise ValueError("a reason based on the actual review is required")
    if evidence is not None and status != "resolved":
        raise ValueError("new resolution evidence applies only to resolved status")
    at = now()
    old_evidence = issue.pop("resolution_evidence", None)
    if old_evidence:
        issue.setdefault("resolution_history", []).append({
            "at": at, "reason": reason, "evidence": old_evidence})
    issue["status"] = status
    issue["history"].append({"at": at, "status": status, "reason": reason})
    if status in {"deferred", "withdrawn"}:
        issue["reason"] = reason
    else:
        # The status reason describes the current deferral/withdrawal only;
        # earlier reasons remain in history.
        issue.pop("reason", None)
    if status == "resolved":
        issue["resolution_evidence"] = evidence
    errors = checks.validate_ledger_update(ledger, result)
    if not errors and status == "resolved":
        errors += checks.verify_files("ledger", {"issues": [issue]}, root, sources)
    if errors:
        raise ValueError("; ".join(errors))
    return result


def resume(state, root, sources):
    errors = checks.validate_state(state)
    if errors:
        raise ValueError("; ".join(errors))
    result = copy.deepcopy(state)
    stages = result["stages"]
    reasons, notes = {}, {}
    for name, stage in stages.items():
        problems = []
        for source, version in stage["inputs"].items():
            problems += checks.verify_source(source, version, root, sources)
        if stage["status"] not in checks.STALEABLE:
            # Unstarted work, open decisions and justified non-applicability
            # keep their status; unverifiable inputs are reported, not "stale".
            if problems:
                notes[name] = [f"input not yet verifiable: {p}" for p in problems]
            continue
        if stage["status"] == "complete":
            for output in stage["outputs"]:
                problems += checks.verify_source(output, stage.get("output_versions", {}).get(output, "unknown"), root)
        if stage["status"] == "active":
            problems.append("previous active execution has no verified completion; inspect before retry")
        if problems:
            reasons[name] = problems
    affected = checks.dependents(stages, reasons)
    for name in affected - set(reasons):
        message = [f"dependency needs recheck: {dep}" for dep in sorted(affected & set(stages[name]["depends_on"]))]
        if stages[name]["status"] in checks.STALEABLE:
            reasons[name] = message
        else:
            notes.setdefault(name, []).extend(message)
    for name, problems in reasons.items():
        stages[name]["status"] = "stale"
        stages[name]["recheck_reasons"] = problems
    ready = [name for name, stage in stages.items()
             if stage["status"] in {"pending", "stale"}
             and all(stages[dep]["status"] in {"complete", "not_applicable"}
                     for dep in stage["depends_on"])]
    return result, {"recheck": reasons, "status_preserved_notes": notes, "next_candidates": ready,
                    "note": "Candidates need the recorded evidence gaps resolved; no work is auto-executed."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    snap = commands.add_parser("snapshot", help="Register current local bytes; not scientific endorsement")
    snap.add_argument("files", nargs="+")
    move = commands.add_parser("ledger-transition", help="Append a reviewed status change and archive old closure evidence")
    move.add_argument("path", type=Path)
    move.add_argument("issue")
    move.add_argument("status", choices=sorted(checks.ISSUE_STATUSES))
    move.add_argument("--reason", required=True)
    move.add_argument("--evidence", type=Path, help="JSON array of current closure anchors")
    restore = commands.add_parser("resume", help="Check current files and mark dependent work stale")
    restore.add_argument("path", type=Path)
    seal = commands.add_parser("record-outputs", help="Record current output hashes for already-reviewed complete stages")
    seal.add_argument("path", type=Path)
    seal.add_argument("--rerecord", action="store_true",
                      help="Allow replacing previously recorded output hashes whose files changed (re-review first)")
    save = commands.add_parser("save", help="Validate and atomically save a candidate state or ledger")
    save.add_argument("kind", choices=["state", "ledger"])
    save.add_argument("path", type=Path)
    save.add_argument("--expect-sha256", default="missing", help="Current destination hash for intentional replacement")
    for command in (snap, move, restore, seal, save):
        command.add_argument("--root", type=Path, required=True)
        command.add_argument("--output", help="Path inside root; omitted means print proposal only")
    for command in (move, restore, save):
        command.add_argument("--sources", type=Path, help="Source ID to {path, version, sha256} registry")
    args = parser.parse_args()
    try:
        sources = checks.source_map(load(args.sources)) if getattr(args, "sources", None) else {}
        report = {}
        if args.command == "snapshot":
            result = snapshot(args.root, args.files)
        elif args.command == "ledger-transition":
            result = transition(load(args.path), args.issue, args.status, args.reason,
                                load(args.evidence) if args.evidence else None, args.root, sources)
        elif args.command == "resume":
            result, report = resume(load(args.path), args.root, sources)
        elif args.command == "record-outputs":
            result = load(args.path)
            errors = checks.validate_state(result)
            if errors:
                raise ValueError("; ".join(errors))
            changed = {}
            for name, stage in result["stages"].items():
                if stage["status"] != "complete":
                    continue
                previous = stage.get("output_versions", {})
                current = {p: "sha256:" + checks.file_hash(checks.local_path(args.root, p)) for p in stage["outputs"]}
                differing = [p for p, v in current.items()
                             if p in previous and previous[p].lower() != v]
                if differing:
                    changed[name] = differing
                stage["output_versions"] = current
            if changed and not args.rerecord:
                raise ValueError(f"recorded outputs changed since last recording: {changed}; "
                                 "re-review them, then pass --rerecord")
            if changed:
                report["rerecorded_changed_outputs"] = changed
            report["note"] = "Recorded current bytes only; this does not approve the stage or refresh its input versions."
        else:
            result = load(args.path)
            errors = {"state": checks.validate_state, "ledger": checks.validate_ledger}[args.kind](result)
            if not errors:
                errors += checks.verify_files(args.kind, result, args.root, sources)
            if args.output and args.kind == "ledger":
                destination = checks.local_path(args.root, args.output)
                if destination.exists():
                    errors += checks.validate_ledger_update(load(destination), result)
            if errors:
                raise ValueError("; ".join(errors))
        if args.output:
            destination = checks.local_path(args.root, args.output)
            if args.command != "save" and destination.exists():
                raise ValueError("use a new output path; only save supports canonical replacement")
            expected = args.expect_sha256 if args.command == "save" else "missing"
            report.update(output=str(destination), sha256=atomic_save(destination, result, expected))
            print(json.dumps(report, ensure_ascii=False, indent=2))
        else:
            print(json.dumps({"data": result, **report}, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, TypeError, KeyError) as exc:
        print(json.dumps({"valid": False, "error": str(exc)}, ensure_ascii=False))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
