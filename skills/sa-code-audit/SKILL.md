---
name: sa-code-audit
description: Inspect research code architecture, behavior, changes, or consistency with a paper or protocol. Use for implementation audits, not ordinary feature implementation or manuscript-only review.
---

# Research code audit

Answer the implementation question with source or execution evidence. Use [evidence guidance](../../shared/EVIDENCE.md) for consequential findings and [shared principles](../../shared/CONTRACT.md) for project work.

## Investigate

- Scope the inspection to the supplied code or relevant repository path. For repository changes, identify the revision, dirty files and actual base/head. Use a file version when Git history is unavailable.
- Establish the expected behavior from the question, protocol, interface or an independent example. Trace the relevant inputs, decisions, state and outputs; follow dependencies only when they can change the answer.
- For research claims, check relevant split boundaries, preprocessing, denominators, cache identity and run provenance. Systems questions may instead require workload, resource or concurrency checks.
- Use a focused check or isolated reproducer when useful and authorized. Record commands and observations. A read-only audit does not authorize source edits, dependency installation, full experiments or external service changes.
- Distinguish inspected source, observed execution and inference. Source-derived reachability is not a runtime trace, and passing tests do not establish empirical paper claims.

## Deliver

For a narrow question, return the answer and its supporting code location or supplied snippet. Add a behavior map, severity-ranked findings or requirement-to-evidence table only when the requested investigation needs them. State material missing evidence and stop when the question is answered.

For an authorized fix, carry the evidence into the host's coding workflow. Use [handoffs](../../shared/HANDOFF.md) only when passing work onward; supported architecture can go to [figure production](../sa-figure-production/SKILL.md), and measured outcomes to [experiment analysis](../sa-experiment-analysis/SKILL.md).
