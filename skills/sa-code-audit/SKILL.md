---
name: sa-code-audit
description: Inspect research code architecture, behavior, changes, or consistency with a paper or protocol. Use for implementation audits, not ordinary feature implementation or manuscript-only review.
---

# Research code audit

Answer the concrete implementation question with source or execution evidence. Use [shared principles](../../shared/CONTRACT.md) and [evidence guidance](../../shared/EVIDENCE.md) for consequential findings; [handoffs](../../shared/HANDOFF.md) apply only when passing work onward.

## Ground the investigation

Read applicable project instructions, inspect current revision and dirty changes, and identify the relevant entry point, configuration and tests. If there is no Git history, record that and use file hashes or an identified snapshot. Resolve actual base/head for change reviews. Read only documentation relevant to the question; treat documentation as intent to verify against code.

Choose the smallest useful investigation: architecture orientation, a runtime/data path, change impact, or implementation-versus-requirement verification. Establish the oracle: supplied protocol, public interface, expected examples or a test independent of the implementation. If code is missing, report that limitation; a paper's pseudocode is not evidence of the repository behavior.

Trace inputs through transformations, decisions, mutable state, side effects and outputs/failures. Expand into dependencies when they can change the answer. Check data split boundaries, preprocessing fit scope, evaluation denominators, cache identity, seeds and checkpoint provenance when those affect a research claim. For systems work inspect configuration, workload, concurrency or failure behavior as relevant; do not impose every possible check.

## Verify and report

Use existing safe focused checks or an isolated reproducer when useful and authorized. Record exact commands and observed outcomes. Do not edit source files, install dependencies, run full experiments or touch external services merely to complete a read-only audit. A request to fix an identified issue hands implementation back to the host's normal coding workflow with the audit evidence.

Distinguish `code_observation` with `source` basis from `runtime` basis; source-derived reachability is not an observed execution trace. Record inferred edges, missing specifications, skipped checks and environment failures explicitly. Passing tests establish only the tested properties, not the paper's empirical claims.

Deliver a direct answer, scope/revision, minimal behavior map, severity-ranked findings with file/symbol/line anchors, requirement-to-evidence table and the smallest useful next check. For figure-ready explanations hand off the supported architecture to [sa-figure-production](../sa-figure-production/SKILL.md); for measured outcomes use [sa-experiment-analysis](../sa-experiment-analysis/SKILL.md).

Stop when the requested behavior has a supported answer or a precise missing-evidence boundary. Do not expand a narrow audit into a full repository census.
