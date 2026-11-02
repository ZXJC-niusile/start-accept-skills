# Resumable state

Use state only for continuing multi-stage projects. Store `schema_version: 1`, `goal`, `run_id`, and a `stages` object. Each stage records `status`, `inputs` (source-to-version map), `depends_on`, `outputs`, and optional `decision` or `reason`. Completed output hashes use `output_versions`. Record unavailable versions as `unknown`; see the [shape example](state.example.json).

## Status rules

- `pending`: work has not started. Input gaps do not make it stale.
- `active`: interrupted work needs inspection before retrying.
- `complete`: a deliverable exists and its required checks are satisfied.
- `stale`: started/completed work needs rechecking against changed or missing evidence.
- `needs_decision`: an unresolved choice; preserve its recorded decision context.
- `not_applicable`: a justified omission with a reason; dependents must still have the inputs they need.

`resume` checks current files and propagates recheck requirements through dependencies. Only active, complete or already stale stages can become stale. Other statuses retain their meaning; `status_preserved_notes` reports their input/dependency gaps. Next candidates are proposals, not automatic execution or verified readiness.

Manual `stale` compares supplied versions for equality, not chronological order. It preserves the same protected statuses and returns proposed JSON without writing. Source IDs normalize equivalent relative paths; unknown IDs or conflicting aliases are errors. Logical IDs remain case-sensitive.

## Persistence

The coordinator writes canonical state; workers return proposals. Use the user's location or `.start-accept/state.json`, source registries under `.start-accept/`, and versioned stage artifacts under `.start-accept/<run-id>/`. Retain prior evidence.

From the research project directory, check structure with `python "SA/scripts/validate_artifacts.py" state PATH`, replacing `SA` with the package's absolute path. For source registration, reviewed-output recording, file verification and locked saves, use [local operations](../../../shared/LOCAL_OPERATIONS.md). Structural validity and byte identity do not establish scientific correctness. Legacy complete stages without hashes require rechecking before file-verified completion.
