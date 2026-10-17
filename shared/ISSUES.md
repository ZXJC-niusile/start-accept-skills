# Review issue records

Load when producing a structured issue ledger or verifying previous issues. A one-off prose comment needs no ledger.

Each issue has a stable `id`, `summary`, `severity` (critical/major/minor), `status`, `anchor`, `close_criterion`, and chronological `history`. Keep confidence separate from severity. Critical/major findings without sufficient anchors remain questions or unverified findings, not established defects.

For a structured revision update, `python scripts/validate_artifacts.py ledger NEW.json --previous OLD.json` checks preservation of IDs, earlier history and close criteria. If the user changes a criterion, withdraw the old issue with that decision recorded and create a linked replacement rather than silently weaken the old criterion.

Before replacing/removing `resolution_evidence`, archive it in append-only `resolution_history` entries with `at`, `reason`, and `evidence`. For real closure, add `--verify-files --root PROJECT` and a source registry when needed; structural validity alone is insufficient. The [local operations](LOCAL_OPERATIONS.md) helper handles transitions and archival without rewriting previous events.

Statuses: open, verified, contested, deferred, resolved, withdrawn. Resolution requires version-specific `resolution_evidence` satisfying the close criterion; `unknown` versions cannot establish closure. Each history event has `at` (ISO date or timestamp, nondecreasing), `status`, and `reason`; date-only or timezone-free times are interpreted as UTC for ordering. Deferred and withdrawn issues require reasons. Preserve dissent. Reopen an issue with a new history event if new versions invalidate its resolution; do not silently discard earlier evidence. Only the coordinator or assigned synthesis owner writes the canonical ledger; review workers do not overwrite each other.
