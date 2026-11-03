---
name: sa-research-design
description: Turn a selected computer-science question into a testable method, systems, benchmark, or theory study. Use for hypotheses, baseline and metric choices, data construction, ablations, and success criteria; manuscript drafting and result interpretation have separate owners.
---

# Design a testable study

Develop the requested part of a study within its chosen question and resource envelope. Follow the [shared contract](../../shared/CONTRACT.md). Design work alone does not authorize experiments, data collection or a change to the central claim.

## Design

- Establish the question, contribution, target setting and available evidence. If the question is undecided, identify the choice for [topic selection](../sa-topic-selection/SKILL.md).
- Connect the motivating gap to the mechanism and an observation or counterexample that could test it. Preserve the selected construct: a system that meets the user's target must not fail the primary metric solely because an extra capability was added. Keep broader diagnostics optional.
- Specify the relevant comparison unit, intervention/control, metric direction, denominator, uncertainty and success/failure criteria. Derive thresholds and repetition counts from the question, variance and budget; leave unsupported choices explicit.
- Compare against the strongest relevant baseline, including plausible adaptations, with comparable resources and data access. Identify the comparison that isolates the proposed increment.
- Specify data versions, split/grouping units, leakage controls, failed-run handling and reproducibility records where applicable. Separate development from final evaluation and planned evidence from observations.
- Read [study modes](references/study-modes.md) for method/system, benchmark or theory details needed by this task.

## Deliver

For a local request such as one metric or ablation, return that design, its rationale and a minimal validation method. For a full study, provide a specification, experiment/proof matrix, execution priorities, resource assumptions and unresolved decisions. Include what would weaken the central claim; do not invent results.

Actual implementation and execution follow the authorized project task. Existing-code questions may use [code audit](../sa-code-audit/SKILL.md); measured results use [experiment analysis](../sa-experiment-analysis/SKILL.md); manuscript drafting uses [paper writing](../sa-paper-writing/SKILL.md).
