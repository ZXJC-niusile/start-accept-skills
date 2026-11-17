---
name: sa-workflow
description: Coordinate multi-stage computer science research or resume a research project across stages. For one isolated deliverable, use its specialist skill directly.
---

# Research workflow

Turn the user's research goal into a sequence of evidence-bearing deliverables. Use [shared principles](../../shared/CONTRACT.md); load [handoffs](../../shared/HANDOFF.md) when coordinating stages or persisting state.

## Choose the entry

Inspect the supplied materials and existing project decisions before asking for missing information. Identify paper type, current stage, authorized actions, and the next unresolved research decision. A paper, repository, or results directory alone is not a request to execute every stage.

| Requested deliverable | Owner |
|---|---|
| Understand/search/compare literature | [sa-paper-reading](../sa-paper-reading/SKILL.md) |
| Compare possible research questions | [sa-topic-selection](../sa-topic-selection/SKILL.md) |
| Specify methods, benchmarks or experiments | [sa-research-design](../sa-research-design/SKILL.md) |
| Explain or audit implementation | [sa-code-audit](../sa-code-audit/SKILL.md) |
| Interpret experimental evidence | [sa-experiment-analysis](../sa-experiment-analysis/SKILL.md) |
| Draft or revise manuscript prose | [sa-paper-writing](../sa-paper-writing/SKILL.md) |
| Design or produce a figure | [sa-figure-production](../sa-figure-production/SKILL.md) |
| Assess scientific merit | [sa-scientific-review](../sa-scientific-review/SKILL.md) |
| Verify revisions or compare versions | [sa-revision-check](../sa-revision-check/SKILL.md) |
| Check presentation and submission readiness | [sa-submission-check](../sa-submission-check/SKILL.md) |

## Coordinate

Propose only the stages needed for the goal. A typical empirical study moves from reading and topic selection to design, then code audit/analysis, writing/figures, scientific review, revision and submission checks. Enter midway when appropriate. A theory paper can mark experiments not applicable with a reason; a systems paper needs workload and resource evidence, not an imposed ML benchmark.

Each stage has one primary owner, explicit inputs, output and completion condition. Parallelize independent reading or checks only when authorized; keep shared-state writes with the coordinator. Code implementation and experiment execution are ordinary project tasks outside the specialist skills' ownership: hand off a concrete spec and authorized budget, then resume from actual outputs.

For decisions requiring user input under the shared principles, present the concrete choice and supporting evidence. A review finding alone does not authorize editing the manuscript.

When persisting or resuming, follow the [state contract](references/state.md) for storage, versions and stale propagation. Update input and output versions along with stage status.

## Complete

Return the accomplished stages, artifact links, unresolved decisions and the next owner. A completed stage needs the actual deliverable and relevant checks; unavailable tools produce a named limitation. Do not promise acceptance or claim a full pipeline completed after a plan, mock review, or static validation alone.
