# Cross-stage handoffs

Load only when passing work between stages or resuming a project.

Use these fields in prose or JSON: `goal`, `inputs` (source and version), `evidence`, `conclusions`, `unknowns`, `outputs`, `next_step`. See [handoff example](handoff.example.json). A structured multi-stage workspace may keep project state and source registries directly under `.start-accept/` and stage artifacts under `.start-accept/<run-id>/`; choose the user's established output directory first. Preserve previous artifacts with distinct run IDs rather than overwrite evidence.

The coordinator alone updates shared workflow state; workers return proposals and artifacts. Recheck affected outputs when upstream versions change. A successful process exit does not establish scientific correctness.

For durable state, use the [state contract](../skills/sa-workflow/references/state.md).
