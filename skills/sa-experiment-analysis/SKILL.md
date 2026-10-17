---
name: sa-experiment-analysis
description: Audit research runs, aggregate results, compare baselines and ablations, and determine which empirical claims the data supports. Use for logs, result tables, uncertainty, coverage or fairness analysis. Manuscript drafting belongs to sa-paper-writing; new experimental design belongs to sa-research-design.
---

# Experiment analysis

Establish what the available measurements support. Use [shared principles](../../shared/CONTRACT.md) and [evidence guidance](../../shared/EVIDENCE.md); do not infer experimental completion from a passing test or a paper's reported number.

## Work

1. Identify the research question, source versions, observation unit, metric definition/direction, denominator and expected coverage. Read raw records when provided. If only aggregates exist, state what cannot be reconstructed.
2. Audit run identity, split/checkpoint/configuration, duplicate keys, missing values, failed runs and aggregation rules before calculating. A repeated identical row is not another seed. Conflicting records for one run key block that aggregate pending reconciliation; do not pick the favorable row.
3. Compare compatible populations and protocols. Show full coverage and any matched subset separately, including exclusions and paired denominators. Never silently discard failed runs or pool unlike tasks to manufacture a ranking.
4. Calculate effect magnitude, variation and exceptions at the correct unit. Use inferential tests or intervals when the question calls for them and the design supports their assumptions. If independence, pairing or sampling design is unresolved, report descriptive results and the missing basis; do not add hypothetical tests merely to rebut an unsupported significance claim. When warranted or explicitly requested as a sensitivity analysis, label conditional inference and its assumptions. Distinguish standard deviation, standard error and confidence intervals; avoid pseudoreplication.
5. For each proposed claim, assign supported, overstated, unsupported or unresolved with evidence and scope. Controlled interventions may support attribution; a correlation or unmatched baseline gap alone does not. A single dataset cannot establish broad generalization.
6. Return the useful analysis and a compact claim table. Preserve contrary results. If new experiments are needed, return a request to [research design](../sa-research-design/SKILL.md); do not launch them from this skill. Pass verified values and claim bounds to [writing](../sa-paper-writing/SKILL.md) or [figures](../sa-figure-production/SKILL.md).

## Finish

Use [analysis checks](references/analysis-checks.md) for multi-run or statistical work and the [claim table](templates/claim-table.md) for a reusable report. Show commands and output locations for calculations actually run, with coverage and limitations. A source conflict may block one comparison without blocking unrelated analysis. For theory-only work, empirical analysis can be not applicable; route proof assessment to scientific review.
