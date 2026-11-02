"""Check portable package structure, references, UI metadata and eval inventory.

Requires PyYAML; validates files, not model behavior. No network or mutations.
"""
import argparse
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote

import yaml

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {"sa-workflow", "sa-paper-reading", "sa-topic-selection", "sa-research-design", "sa-code-audit", "sa-experiment-analysis", "sa-paper-writing", "sa-figure-production", "sa-scientific-review", "sa-revision-check", "sa-submission-check"}


def check(root=ROOT, runtime_only=False):
    errors, statistics = [], {}
    manifest = json.loads((root / "plugin.json").read_text(encoding="utf-8"))
    if manifest.get("name") != "start-accept-skills" or manifest.get("$schema") != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
        errors.append("plugin.json: name/schema mismatch")
    paths = list((root / "skills").glob("*/SKILL.md"))
    names = []
    for path in paths:
        content = path.read_text(encoding="utf-8")
        match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", content, re.S)
        if not match:
            errors.append(f"{path.parent.name}: frontmatter missing")
            continue
        meta = yaml.safe_load(match.group(1))
        if not isinstance(meta, dict):
            errors.append(f"{path.parent.name}: invalid frontmatter")
            continue
        name, description = meta.get("name"), meta.get("description")
        names.append(name)
        if name != path.parent.name or not isinstance(name, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
            errors.append(f"{path}: invalid name/directory")
        if not isinstance(description, str) or not description.strip() or len(description) > 1024 or any(c in description for c in "<>"):
            errors.append(f"{path}: invalid description")
        if set(meta) - {"name", "description", "metadata", "license", "allowed-tools"}:
            errors.append(f"{path}: unsupported frontmatter field")
        ui_path = path.parent / "agents/openai.yaml"
        if not ui_path.is_file():
            errors.append(f"{name}: UI metadata missing")
        else:
            ui = yaml.safe_load(ui_path.read_text(encoding="utf-8"))
            interface = ui.get("interface") if isinstance(ui, dict) else None
            policy = ui.get("policy", {}) if isinstance(ui, dict) else {}
            if not isinstance(interface, dict):
                errors.append(f"{name}: UI metadata needs an interface mapping")
                interface = {}
            if not isinstance(policy, dict):
                errors.append(f"{name}: UI policy must be a mapping")
                policy = {}
            short = interface.get("short_description")
            if not isinstance(short, str) or not 25 <= len(short) <= 64:
                errors.append(f"{name}: short_description must be 25-64 characters")
            prompt = interface.get("default_prompt")
            if not isinstance(prompt, str) or f"${name}" not in prompt:
                errors.append(f"{name}: prompt missing explicit invocation")
            if policy.get("allow_implicit_invocation") is False:
                errors.append(f"{name}: automatic invocation unexpectedly disabled")
        statistics[name] = {"description_characters": len(description or ""), "body_words": len(content[match.end():].split())}
    if set(names) != EXPECTED or len(names) != len(EXPECTED):
        errors.append("skill inventory: expected exactly 11 unique names")
    # Package instruction links must remain inside the bundle and exist.
    for directory in (root / "skills", root / "shared"):
        for path in directory.rglob("*.md"):
            text = path.read_text(encoding="utf-8")
            for raw in re.findall(r"\]\(([^)]+)\)", text):
                target = raw.strip("<>").split("#", 1)[0]
                if not target or re.match(r"https?://", target):
                    continue
                resolved = (path.parent / unquote(target)).resolve()
                if not resolved.is_relative_to(root.resolve()) or not resolved.exists():
                    errors.append(f"{path.relative_to(root)}: broken/external package link {target}")
            if re.search(r"C:[\\/]|\.\./ccf-common|\.\./ccf-paper-writer|\.claude/CLAUDE", text):
                errors.append(f"{path.relative_to(root)}: nonportable legacy reference")
    eval_dir = root / "evals/cases"
    if runtime_only or not eval_dir.is_dir():
        # Development eval datasets are not distributed (see .gitignore); a
        # public checkout validates runtime structure and says so explicitly.
        return {"valid": not errors, "errors": errors, "skills": statistics,
                "scope": "runtime_structure", "routing_case_count": None,
                "eval_inventory": "skipped_by_request" if runtime_only else "not_present_in_checkout",
                "behavior_claim": "not assessed by this validator"}
    cases = []
    for path in sorted(eval_dir.glob("*.json")):
        cases.extend(json.loads(path.read_text(encoding="utf-8")))
    ids = [c.get("id") for c in cases]
    if len(ids) != 110 or len(set(ids)) != 110:
        errors.append("evals: expected 110 unique routing cases")
    for skill in EXPECTED:
        items = [c for c in cases if c.get("skill") == skill]
        if len(items) != 10 or not any(c.get("should_trigger") is False for c in items):
            errors.append(f"{skill}: expected 10 cases including negative controls")
    for case in cases:
        if not isinstance(case.get("should_trigger"), bool) or not isinstance(case.get("checks"), list) or not case["checks"]:
            errors.append(f"{case.get('id')}: checks and boolean expected trigger required")
    return {"valid": not errors, "errors": errors, "skills": statistics, "scope": "runtime_structure_and_eval_inventory",
            "routing_case_count": len(cases), "eval_inventory": "checked", "behavior_claim": "not assessed by this validator"}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--runtime-only", action="store_true", help="Validate a distribution without development eval datasets")
    args = parser.parse_args()
    try:
        result = check(runtime_only=args.runtime_only)
    except (OSError, ValueError, TypeError, yaml.YAMLError) as exc:
        result = {"valid": False, "errors": [str(exc)]}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(0 if result["valid"] else 1)
