"""Build a portable preview ZIP from an explicit distribution allowlist.

No installation, publishing, network calls or deletion of development evidence.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import stat
from urllib.parse import unquote
import zipfile

import validate_package

ROOT = Path(__file__).resolve().parents[1]
FILES = (
    "README.md", "README.zh-CN.md", "NOTICE.md", "plugin.json", "requirements-dev.txt",
    ".agents/plugins/marketplace.json", ".gitignore",
    "scripts/validate_artifacts.py", "scripts/project_state.py",
    "scripts/validate_package.py", "scripts/build_release.py",
    "provenance/sources.json",
    "provenance/reading-design.md", "provenance/analysis-writing-figures.md",
    "provenance/review-revision-quality.md", "provenance/workflow-audit.md",
)
DIRECTORIES = ("skills", "shared", "docs")


def digest(data):
    return hashlib.sha256(data).hexdigest()


def check_path(path):
    info = path.lstat()
    if path.is_symlink() or getattr(info, "st_file_attributes", 0) & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 1024):
        raise ValueError(f"linked/reparse path excluded: {path.name}")
    if not path.resolve().is_relative_to(ROOT):
        raise ValueError("distribution path leaves package root")


def collect():
    paths = [ROOT / name for name in FILES]
    if (ROOT / "LICENSE").is_file():
        paths.append(ROOT / "LICENSE")
    for directory in DIRECTORIES:
        check_path(ROOT / directory)
        for current, dirs, names in os.walk(ROOT / directory, followlinks=False):
            dirs[:] = sorted(d for d in dirs if d != "__pycache__")
            for child in dirs:
                check_path(Path(current) / child)
            paths.extend(Path(current) / name for name in names if not name.endswith((".pyc", ".pyo")))
    payload = {}
    for path in sorted(paths):
        check_path(path)
        payload[path.relative_to(ROOT).as_posix()] = path.read_bytes()
    return payload


def inspect(payload):
    manifest = json.loads(payload["plugin.json"])
    if manifest.get("name") != "start-accept-skills" or not re.fullmatch(r"\d+\.\d+\.\d+", manifest.get("version", "")):
        raise ValueError("unexpected package identity/version")
    entries = [name for name in payload if re.fullmatch(r"skills/[^/]+/SKILL\.md", name)]
    if len(entries) != 11:
        raise ValueError("expected 11 skill entrypoints")
    directories = {p.as_posix() for name in payload for p in Path(name).parents if p.as_posix() != "."}
    for name, data in payload.items():
        if name.endswith((".md", ".py", ".json", ".yaml", ".txt")):
            text = data.decode("utf-8-sig")
            # Target known accidental host paths/key material, not a general DLP claim.
            if re.search(r"(?i)[a-z]:[/\\]Users[/\\][a-z0-9_.-]+|/Users/[a-z0-9_.-]+|/home/[a-z0-9_.-]+|-----BEGIN (?:RSA |OPENSSH )?PRIVATE KEY-----", text):
                raise ValueError(f"local user path or private-key marker in {name}")
            if name.endswith(".md"):
                for raw in re.findall(r"\]\(([^)]+)\)", text):
                    target = unquote(raw.strip("<>").split("#", 1)[0])
                    if not target or re.match(r"https?://", target):
                        continue
                    resolved = (ROOT / Path(name).parent / target).resolve()
                    if not resolved.is_relative_to(ROOT):
                        raise ValueError(f"external local link in {name}: {target}")
                    relative = resolved.relative_to(ROOT).as_posix()
                    if relative not in payload and relative not in directories:
                        raise ValueError(f"link missing from release in {name}: {target}")
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="New build directory; existing directories are never overwritten")
    args = parser.parse_args()
    try:
        structure = validate_package.check(ROOT, runtime_only=True)
        if not structure["valid"]:
            raise ValueError("package structure check failed: " + "; ".join(structure["errors"]))
        payload = collect()
        manifest = inspect(payload)
        prefix = manifest["name"]
        version = manifest["version"]
        output = args.output or ROOT / "dist" / f"{prefix}-{version}-preview"
        output.mkdir(parents=True, exist_ok=False)
        file_manifest = {name: digest(data) for name, data in sorted(payload.items())}
        payload["RELEASE-MANIFEST.json"] = json.dumps({
            "version": version, "status": "preview_not_published", "files": file_manifest,
            "excluded": ["evals", "tests", "cache", "personal configuration"],
            "license": manifest.get("license"),
            "open_release_items": ["third-party attribution review", "desktop UI refresh (CLI smoke check documented)"]
        }, ensure_ascii=False, indent=2).encode("utf-8")
        archive = output / f"{prefix}-{version}-preview.zip"
        with zipfile.ZipFile(archive, "x", compression=zipfile.ZIP_DEFLATED) as bundle:
            for name, data in sorted(payload.items()):
                entry = zipfile.ZipInfo(f"{prefix}/{name}", date_time=(1980, 1, 1, 0, 0, 0))
                entry.compress_type = zipfile.ZIP_DEFLATED
                entry.external_attr = 0o100644 << 16
                bundle.writestr(entry, data)
        with zipfile.ZipFile(archive) as bundle:
            if bundle.testzip() is not None:
                raise ValueError("ZIP CRC verification failed")
            for name, data in payload.items():
                if bundle.read(f"{prefix}/{name}") != data:
                    raise ValueError(f"ZIP content mismatch: {name}")
        archive_sha = digest(archive.read_bytes())
        (output / "SHA256SUMS.txt").write_text(f"{archive_sha}  {archive.name}\n", encoding="utf-8")
        report = {"version": version, "license": manifest.get("license"), "status": "preview_prepared_not_published", "archive": archive.name,
                  "sha256": archive_sha, "file_count": len(payload), "skill_count": 11,
                  "archive_bytes": archive.stat().st_size, "included_file_hashes": file_manifest,
                  "checks": ["runtime package structure (frontmatter, UI metadata, links)", "allowlist", "local markdown links", "known local paths", "11 skill entries", "archive round-trip"],
                  "not_checked": ["host activation", "scientific behavior", "third-party rights clearance", "general secret detection"]}
        (output / "build-report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
        print(json.dumps({k: v for k, v in report.items() if k != "included_file_hashes"}, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, UnicodeError, zipfile.BadZipFile, validate_package.yaml.YAMLError) as exc:
        print(json.dumps({"valid": False, "error": str(exc)}, ensure_ascii=False))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
