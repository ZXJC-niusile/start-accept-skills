"""Validate research handoffs, issue ledgers and resumable state. Stdlib only.

This checks contracts, not scientific truth. All commands are read-only; stale
prints proposed updated state for the caller to review and persist.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import posixpath
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

KINDS = {"paper_report", "code_observation", "experiment_measurement", "inference"}
STATUSES = {"pending", "active", "needs_decision", "complete", "stale", "not_applicable"}
ISSUE_STATUSES = {"open", "verified", "contested", "deferred", "resolved", "withdrawn"}


def anchor_valid(anchor):
    return isinstance(anchor, dict) and all(
        isinstance(anchor.get(k), str) and anchor[k].strip()
        for k in ("source", "version", "locator")
    )


def known_version(anchor):
    return anchor_valid(anchor) and anchor["version"].strip().lower() not in {
        "unknown", "unverified", "n/a", "unspecified", "todo", "tbd", "latest",
        "current", "head", "pending", "待核实", "未知", "待定", "最新", "?", "-"}


def source_id(value):
    """Normalize relative file spelling; preserve URL and opaque ID case."""
    if not isinstance(value, str) or not value.strip():
        raise ValueError("source ID must be a nonempty string")
    value = value.strip().replace("\\", "/")
    return value if "://" in value else posixpath.normpath(value)


def source_map(mapping):
    if not isinstance(mapping, dict):
        raise ValueError("sources must be an object")
    result = {}
    for key, value in mapping.items():
        key = source_id(key)
        if key in result:
            raise ValueError(f"ambiguous normalized source ID: {key}")
        result[key] = value
    return result


def file_hash(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def local_path(root, value):
    if not isinstance(value, str) or "://" in value:
        raise ValueError("local file or a registered local source snapshot required")
    root = Path(root).resolve()
    path = (root / value).resolve()
    if not path.is_relative_to(root):
        raise ValueError(f"path outside project root: {value}")
    return path


def verify_source(source, version, root, sources=None, sha256=None):
    """Verify bytes/version binding, never whether a scientific claim is true."""
    try:
        if not known_version({"source": source, "version": version, "locator": "file"}):
            raise ValueError("unknown or mutable version")
        registry = source_map(sources or {})
        record = registry.get(source_id(source))
        if record is not None and not isinstance(record, dict):
            raise ValueError("source registry entry must be an object")
        record = record or {}
        path = local_path(root, record.get("path", source))
        if not path.is_file():
            raise ValueError(f"file missing: {path}")
        expected = sha256 or record.get("sha256")
        if sha256 and record.get("sha256") and sha256.lower().removeprefix("sha256:") != record["sha256"].lower().removeprefix("sha256:"):
            raise ValueError("anchor and registry hashes disagree")
        version_hash = version.removeprefix("sha256:")
        if re.fullmatch(r"[0-9a-fA-F]{64}", version_hash):
            if expected and expected.lower().removeprefix("sha256:") != version_hash.lower():
                raise ValueError("version and registered hash disagree")
            expected = version_hash
        elif record and record.get("version") != version:
            raise ValueError("anchor and registered versions disagree")
        elif not sha256 and record.get("version") != version:
            raise ValueError("opaque version needs a matching registered version and sha256")
        if not isinstance(expected, str) or not re.fullmatch(r"[0-9a-fA-F]{64}", expected.removeprefix("sha256:")):
            raise ValueError("immutable sha256 required")
        if file_hash(path) != expected.lower().removeprefix("sha256:"):
            raise ValueError(f"content changed: {source}")
        return []
    except (OSError, ValueError, TypeError, AttributeError) as exc:
        return [f"{source}: {exc}"]


def verify_files(kind, data, root, sources=None):
    errors = []
    if kind == "ledger":
        anchors = [a for issue in data["issues"] if issue["status"] == "resolved"
                   for a in issue["resolution_evidence"]]
    elif kind == "handoff":
        anchors = data["inputs"] + data["evidence"]
    else:
        anchors = []
        for name, stage in data["stages"].items():
            if stage["status"] != "complete":
                continue
            anchors.extend({"source": s, "version": v} for s, v in stage["inputs"].items())
            versions = stage.get("output_versions", {})
            if not isinstance(versions, dict):
                errors.append(f"stages.{name}.output_versions: object required")
                continue
            for output in stage["outputs"]:
                errors.extend(verify_source(output, versions.get(output, "unknown"), root))
    for anchor in anchors:
        errors.extend(verify_source(anchor["source"], anchor["version"], root, sources, anchor.get("sha256")))
    return errors


def event_time(value):
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        return parsed.replace(tzinfo=timezone.utc) if parsed.tzinfo is None else parsed.astimezone(timezone.utc)
    except ValueError:
        return None


def validate_handoff(data):
    if not isinstance(data, dict):
        return ["handoff: expected object"]
    errors = []
    for key in ("goal", "inputs", "evidence", "conclusions", "unknowns", "outputs", "next_step"):
        if key not in data:
            errors.append(f"handoff.{key}: missing")
    if not isinstance(data.get("goal"), str) or not data.get("goal", "").strip():
        errors.append("handoff.goal: nonempty string required")
    for key in ("inputs", "evidence", "conclusions", "unknowns", "outputs"):
        if not isinstance(data.get(key), list):
            errors.append(f"handoff.{key}: array required")
    for i, item in enumerate(data.get("inputs", []) if isinstance(data.get("inputs"), list) else []):
        if not isinstance(item, dict) or not all(isinstance(item.get(k), str) and item[k].strip() for k in ("source", "version")):
            errors.append(f"handoff.inputs[{i}]: source and version required")
    for i, item in enumerate(data.get("evidence", []) if isinstance(data.get("evidence"), list) else []):
        if not anchor_valid(item) or item.get("kind") not in KINDS:
            errors.append(f"handoff.evidence[{i}]: valid kind and anchor required")
    nxt = data.get("next_step")
    if not isinstance(nxt, dict) or not all(isinstance(nxt.get(k), str) and nxt[k].strip() for k in ("owner", "task")):
        errors.append("handoff.next_step: owner and task required")
    return errors


def validate_ledger(data):
    if not isinstance(data, dict) or not isinstance(data.get("issues"), list):
        return ["ledger.issues: array required"]
    errors, seen = [], set()
    for i, issue in enumerate(data["issues"]):
        loc = f"issues[{i}]"
        if not isinstance(issue, dict):
            errors.append(f"{loc}: object required")
            continue
        ident = issue.get("id")
        if not isinstance(ident, str) or not ident.strip():
            errors.append(f"{loc}.id: nonempty string required")
        elif ident in seen:
            errors.append(f"{loc}.id: duplicate")
        else:
            seen.add(ident)
        for key in ("summary", "close_criterion"):
            if not isinstance(issue.get(key), str) or not issue[key].strip():
                errors.append(f"{loc}.{key}: nonempty string required")
        status = issue.get("status")
        if status not in ISSUE_STATUSES:
            errors.append(f"{loc}.status: invalid")
        if issue.get("severity") not in {"critical", "major", "minor"}:
            errors.append(f"{loc}.severity: invalid")
        if "anchor" not in issue:
            errors.append(f"{loc}.anchor: missing (null permitted for an open question)")
        if status in {"verified", "resolved"} and not anchor_valid(issue.get("anchor")):
            errors.append(f"{loc}.anchor: verified finding needs versioned source")
        if status == "resolved":
            resolution = issue.get("resolution_evidence")
            if not isinstance(resolution, list) or not resolution or not all(known_version(a) for a in resolution):
                errors.append(f"{loc}.resolution_evidence: nonempty versioned anchors required")
        if status in {"deferred", "withdrawn"} and not issue.get("reason"):
            errors.append(f"{loc}.reason: required")
        archive = issue.get("resolution_history", [])
        if not isinstance(archive, list):
            errors.append(f"{loc}.resolution_history: array required")
        else:
            for j, record in enumerate(archive):
                if (not isinstance(record, dict) or event_time(record.get("at")) is None
                        or not record.get("reason") or not isinstance(record.get("evidence"), list)
                        or not record["evidence"] or not all(anchor_valid(a) for a in record["evidence"])):
                    errors.append(f"{loc}.resolution_history[{j}]: timestamp, reason and evidence anchors required")
        history = issue.get("history")
        if not isinstance(history, list) or not history:
            errors.append(f"{loc}.history: nonempty array required")
        else:
            previous_time = None
            for j, event in enumerate(history):
                if not isinstance(event, dict) or event.get("status") not in ISSUE_STATUSES or not event.get("reason") or not event.get("at"):
                    errors.append(f"{loc}.history[{j}]: at, valid status and reason required")
                timestamp = event_time(event.get("at")) if isinstance(event, dict) else None
                if timestamp is None:
                    errors.append(f"{loc}.history[{j}].at: ISO date or timestamp required")
                elif previous_time is not None and timestamp < previous_time:
                    errors.append(f"{loc}.history[{j}].at: chronological order required")
                if timestamp is not None:
                    previous_time = timestamp
            if not isinstance(history[-1], dict) or history[-1].get("status") != status:
                errors.append(f"{loc}.history: last status must match issue")
    return errors


def validate_ledger_update(previous, current):
    errors = validate_ledger(previous) + validate_ledger(current)
    if errors:
        return errors
    current_by_id = {i["id"]: i for i in current["issues"]}
    for old in previous["issues"]:
        new = current_by_id.get(old["id"])
        if new is None:
            errors.append(f"issues.{old['id']}: prior issue removed; withdraw with reason instead")
        elif new["history"][:len(old["history"])] != old["history"]:
            errors.append(f"issues.{old['id']}: prior history changed or truncated")
        elif new["close_criterion"] != old["close_criterion"]:
            errors.append(f"issues.{old['id']}: close criterion changed; withdraw and replace with a linked issue")
        if new is not None:
            old_archive = old.get("resolution_history", [])
            archive = new.get("resolution_history", [])
            if not isinstance(archive, list) or archive[:len(old_archive)] != old_archive:
                errors.append(f"issues.{old['id']}: prior resolution archive changed")
            old_evidence = old.get("resolution_evidence")
            if old_evidence and new.get("resolution_evidence") != old_evidence:
                appended = archive[len(old_archive):] if isinstance(archive, list) else []
                if not any(isinstance(a, dict) and a.get("evidence") == old_evidence for a in appended):
                    errors.append(f"issues.{old['id']}: archive previous resolution evidence before replacing/removing it")
    return errors


def validate_state(data):
    if not isinstance(data, dict) or not isinstance(data.get("stages"), dict):
        return ["state.stages: object required"]
    errors = []
    if data.get("schema_version") != 1:
        errors.append("state.schema_version: expected 1")
    for key in ("goal", "run_id"):
        if not isinstance(data.get(key), str) or not data[key].strip():
            errors.append(f"state.{key}: nonempty string required")
    stages = data["stages"]
    edges = {}
    for name, stage in stages.items():
        if not isinstance(stage, dict):
            errors.append(f"stages.{name}: object required")
            continue
        if stage.get("status") not in STATUSES:
            errors.append(f"stages.{name}.status: invalid")
        if not isinstance(stage.get("inputs"), dict) or not all(isinstance(v, str) and v for v in stage.get("inputs", {}).values()):
            errors.append(f"stages.{name}.inputs: source-to-version map required")
        else:
            try:
                source_map(stage["inputs"])
            except ValueError as exc:
                errors.append(f"stages.{name}.inputs: {exc}")
        deps = stage.get("depends_on")
        if not isinstance(deps, list) or not all(isinstance(d, str) for d in deps):
            errors.append(f"stages.{name}.depends_on: string array required")
            deps = []
        edges[name] = deps
        for dep in deps:
            if dep not in stages:
                errors.append(f"stages.{name}.depends_on: unknown stage {dep}")
        outputs = stage.get("outputs")
        if not isinstance(outputs, list) or not all(isinstance(v, str) and v for v in outputs):
            errors.append(f"stages.{name}.outputs: path array required")
        if "output_versions" in stage and (not isinstance(stage["output_versions"], dict)
                or not all(isinstance(k, str) and isinstance(v, str) and v for k, v in stage["output_versions"].items())):
            errors.append(f"stages.{name}.output_versions: path-to-version map required")
        if stage.get("status") == "complete" and not outputs:
            errors.append(f"stages.{name}: complete requires an output")
        if stage.get("status") == "not_applicable" and not stage.get("reason"):
            errors.append(f"stages.{name}: not_applicable requires reason")
    visiting, visited = set(), set()
    def visit(name):
        if name in visiting:
            errors.append(f"stages.{name}: dependency cycle")
            return
        if name in visited:
            return
        visiting.add(name)
        for dep in edges.get(name, []):
            if dep in stages:
                visit(dep)
        visiting.remove(name)
        visited.add(name)
    for name in stages:
        visit(name)
    for name, stage in stages.items():
        if isinstance(stage, dict) and stage.get("status") == "complete":
            for dep in edges.get(name, []):
                parent = stages.get(dep)
                if isinstance(parent, dict) and parent.get("status") not in {"complete", "not_applicable"}:
                    errors.append(f"stages.{name}: complete depends on unfinished/stale {dep}")
    return errors


def mark_stale(data, changes):
    errors = validate_state(data)
    if errors:
        raise ValueError("; ".join(errors))
    if not isinstance(changes, dict) or not all(isinstance(v, str) and v for v in changes.values()):
        raise ValueError("changes: source-to-version map required")
    result = copy.deepcopy(data)
    changes = source_map(changes)
    known_sources = {source_id(src) for stage in data["stages"].values() for src in stage["inputs"]}
    unmatched = set(changes) - known_sources
    if unmatched:
        raise ValueError(f"changes contain unregistered source IDs: {sorted(unmatched)}")
    stale = {name for name, s in result["stages"].items()
             if any(source_id(src) in changes and changes[source_id(src)] != ver for src, ver in s["inputs"].items())}
    while True:
        added = {name for name, s in result["stages"].items() if any(d in stale for d in s["depends_on"])} - stale
        if not added:
            break
        stale |= added
    for name in stale:
        result["stages"][name]["status"] = "stale"
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("kind", choices=["handoff", "ledger", "state", "stale"])
    parser.add_argument("path", type=Path)
    parser.add_argument("changes", type=Path, nargs="?")
    parser.add_argument("--previous", type=Path, help="For ledger updates, require prior IDs and history to be preserved")
    parser.add_argument("--verify-files", action="store_true", help="Also verify local bytes/version bindings, not scientific correctness")
    parser.add_argument("--root", type=Path, help="Explicit project root required for file verification")
    parser.add_argument("--sources", type=Path, help="Source ID to {path, version, sha256} registry")
    args = parser.parse_args()
    if args.verify_files and (args.root is None or args.kind == "stale"):
        parser.error("--verify-files requires --root and handoff, ledger or state")
    try:
        data = json.loads(args.path.read_text(encoding="utf-8"))
        if args.kind == "stale":
            if args.changes is None:
                parser.error("stale requires a changes JSON file")
            result = mark_stale(data, json.loads(args.changes.read_text(encoding="utf-8")))
            print(json.dumps(result, ensure_ascii=False, indent=2))
            return 0
        errors = {"handoff": validate_handoff, "ledger": validate_ledger, "state": validate_state}[args.kind](data)
        if args.previous:
            if args.kind != "ledger":
                parser.error("--previous applies only to ledger")
            errors = validate_ledger_update(json.loads(args.previous.read_text(encoding="utf-8")), data)
        if args.verify_files:
            if args.root is None or args.kind == "stale":
                parser.error("--verify-files requires --root and handoff, ledger or state")
            sources = json.loads(args.sources.read_text(encoding="utf-8-sig")) if args.sources else {}
            if not errors:
                errors.extend(verify_files(args.kind, data, args.root, sources))
        print(json.dumps({"valid": not errors, "scope": "structure_and_file_integrity" if args.verify_files else "structure_only", "scientific_correctness": "not_assessed", "errors": errors}, ensure_ascii=False))
        return int(bool(errors))
    except (OSError, ValueError, TypeError) as exc:
        print(json.dumps({"valid": False, "error": str(exc)}, ensure_ascii=False))
        return 1


if __name__ == "__main__":
    sys.exit(main())
