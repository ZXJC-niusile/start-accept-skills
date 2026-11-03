# Local evidence and project operations

Use these helpers for durable multi-stage work or tracked review issues. Short answers need none of them. They use Python's standard library and do not call models, browse, install tools, or decide scientific correctness.

Run commands from the research project's directory. Below, `SA` stands for the package's absolute path; replace it in the command. File arguments and `--root .` refer to that project. Each `--output` must remain inside the project. Without it, commands print a proposal instead of writing files.

## Register source versions

`python "SA/scripts/project_state.py" snapshot data/results.csv paper.md --root . --output .start-accept/sources-v1.json`

The registry maps each source ID to `path`, `version: sha256:<digest>`, and `sha256`. Use these versions in stage inputs and evidence anchors. A logical ID or URL may instead map to a local archived source, with its original immutable version and snapshot hash; the script does not fetch URLs or verify bibliographic identity. Existing opaque versions such as `v2` require an explicit registry binding to that version and hash. A version alone, `latest`, or `TODO` cannot pass file verification.

Keep old registries. Creating a new snapshot records current bytes; it does not establish that a claim is supported or silently refresh existing conclusions.

## Close or reopen a tracked issue

After the reviewer has checked the unchanged close criterion, prepare an evidence JSON array with `source`, `version`, and `locator` per anchor. A local hash can be supplied as `sha256`, or bound through the registry.

`python "SA/scripts/project_state.py" ledger-transition issues-v1.json REV-001 resolved --reason "Checked the fixed table and matched run records" --evidence closure-evidence.json --root . --sources .start-accept/sources-v1.json --output issues-v2.json`

`python "SA/scripts/project_state.py" ledger-transition issues-v2.json REV-001 open --reason "New data invalidate the previous conclusion" --root . --output issues-v3.json`

Each transition appends history. Replacing/removing active closure evidence moves it into append-only `resolution_history`, retaining prior anchors. Reopening does not require old evidence files to remain available. Closing does require current evidence bytes to match; satisfying the scientific criterion remains the reviewer's responsibility. These commands preserve other issues, IDs, and close criteria.

## Finish, resume and save project state

After reviewing a stage's actual deliverables, record their bytes:

`python "SA/scripts/project_state.py" record-outputs state-draft.json --root . --output state-with-hashes.json`

This adds `output_versions` for stages already marked complete. It does not mark a stage complete or update input versions. If an output already has a recorded hash and its bytes have changed, the command refuses; re-review the changed output, then repeat with `--rerecord`. Then check or save with file verification:

`python "SA/scripts/validate_artifacts.py" state state-with-hashes.json --root . --sources .start-accept/sources-v1.json --verify-files`

`python "SA/scripts/project_state.py" save state state-with-hashes.json --root . --sources .start-accept/sources-v1.json --output .start-accept/state.json`

On resumption:

`python "SA/scripts/project_state.py" resume .start-accept/state.json --root . --sources .start-accept/sources-v1.json --output .start-accept/resume-proposal.json`

`resume` checks input/output versions and proposes affected work for rechecking under the [state rules](../skills/sa-workflow/references/state.md). It prints next candidates and notes for preserved statuses; it does not execute work or change source files. Review the proposal before saving it.

For canonical replacement, use `save` with `--expect-sha256` set to the current state/ledger file hash returned by a previous save (case-insensitive; only `save` accepts this option). The helper locks the destination, rejects stale writers, archives prior bytes under `.history/`, and atomically replaces the file. Omitting the expected hash permits only a new destination. Ledger replacements also check immutable prior history and closure criteria.

Locks coordinate writers using this helper, not arbitrary external editors. Hard process termination can leave a `.lock` file; inspect its PID and destination before manually recovering it. Locks are never stolen by age. Atomic replacement protects against partial JSON writes, but is not a cross-file transaction or a distributed filesystem guarantee.

## Lightweight structural checks

Without `--verify-files`, `validate_artifacts.py` reports `scope: structure_only`. Strict mode reports file integrity separately from scientific correctness. Ledger strict mode checks currently resolved evidence; state strict mode checks complete stages; handoff strict mode checks inputs and evidence anchors.

Manual `stale STATE CHANGES` accepts equivalent `./data.csv` and `data.csv` spellings, but rejects unregistered source IDs and conflicting aliases. Logical IDs remain case-sensitive. Prefer `resume` when actual files are available, since it also detects missing files and changed outputs.
