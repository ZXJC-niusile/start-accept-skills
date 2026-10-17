# Cross-stage handoffs

Load only when passing work between stages or resuming a project.

Use these fields in prose or JSON: `goal`, `inputs` (source and version), `evidence`, `conclusions`, `unknowns`, `outputs`, `next_step`. See [handoff example](handoff.example.json). A structured multi-stage workspace may keep these under `.start-accept/`; choose the user's established output directory first. Preserve previous artifacts with distinct run IDs rather than overwrite evidence.

The coordinator alone updates shared workflow state; workers return proposals and artifacts. Record stage status as pending, active, needs_decision, complete, stale, or not_applicable. A changed upstream version makes dependent outputs stale, recursively, until checked against the new inputs. A successful process exit does not by itself establish scientific correctness.

For durable state, use the [state contract](../skills/sa-workflow/references/state.md).
