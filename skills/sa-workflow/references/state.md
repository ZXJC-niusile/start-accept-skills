# Minimal resumable state

State is optional for a one-stage answer. For a continuing project, store JSON with `schema_version: 1`, `goal`, `run_id`, and a `stages` object. Each stage has `status`, `inputs` (map of source ID to version string), `depends_on` (stage IDs), `outputs` (paths), and optionally `decision` or `reason`. Stages need not include every skill. Record missing versions explicitly as `unknown`; never invent hashes.

Use [example](state.example.json) as a shape, not as actual completion evidence. The coordinator writes state atomically and keeps distinct run directories. Before relying on completed work, resolve current versions from source artifacts. Run the package's `scripts/validate_artifacts.py state PATH` to check structural integrity. This validates state, not the underlying research.

For actual completion/resumption, use [local operations](../../../shared/LOCAL_OPERATIONS.md): register sources, record reviewed output hashes in `output_versions`, verify files, and save with a lock and expected prior hash. `resume` detects changed/missing inputs and outputs, marks transitive dependents stale, and reports next candidates. It never executes stages or certifies scientific correctness. Legacy states remain structurally readable; missing hashes require rechecking before file-verified completion.

`scripts/validate_artifacts.py stale STATE CHANGES` returns a revised JSON on stdout, without writing. CHANGES is a JSON map of source IDs to new versions. Any stage recording an older version and every transitive dependent becomes `stale`; the caller reviews and saves that result. Completed outputs remain on disk. Stale work must be rechecked against the changed source before completion is restored. A dependency's `not_applicable` status requires a reason and is acceptable only if the dependent stage actually has the inputs it needs.

Equivalent relative path spellings are normalized. Unknown source IDs or conflicting aliases are errors, not silent no-ops. Keep logical source IDs stable and case-sensitive.
