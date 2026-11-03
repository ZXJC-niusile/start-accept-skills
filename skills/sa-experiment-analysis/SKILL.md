---
name: sa-experiment-analysis
description: Audit research runs, aggregate results, compare baselines and ablations, and determine which empirical claims the data supports. Use for logs, result tables, uncertainty, coverage or fairness analysis. Manuscript drafting belongs to sa-paper-writing; new experimental design belongs to sa-research-design.
---

# Experiment analysis

Determine what the available measurements support. Use [shared principles](../../shared/CONTRACT.md) and [evidence guidance](../../shared/EVIDENCE.md).

## Analyze

1. Identify the question, input versions, observation unit, metric direction, denominator and expected coverage. Use raw records when supplied; state what aggregates cannot reconstruct.
2. Check run identity, duplicates, missing/failed runs and aggregation rules before calculating. Repeated rows are not independent seeds. Conflicting records block the affected aggregate until reconciled, not unrelated analysis.
3. Compare compatible populations and protocols. Report coverage and exclusions, including any matched subset; do not silently discard failed runs or pool incompatible tasks.
4. Calculate effect magnitude and variation at the appropriate unit. Inferential procedures require a suitable design and justified assumptions. Otherwise report descriptive results. Read [analysis checks](references/analysis-checks.md) for multi-run or statistical work, including conditional analyses.
5. Bound each requested claim by its evidence: supported, overstated, unsupported or unresolved. Preserve contrary results and distinguish association, causal attribution and generalization.

## Deliver

Answer a narrow numerical question directly with the calculation, denominator and material limitation. For a reusable analysis report, use the [claim table](templates/claim-table.md). Record commands and outputs for calculations actually run.

If additional experiments are necessary, specify the missing evidence for [research design](../sa-research-design/SKILL.md); do not launch them from this skill. Use [writing](../sa-paper-writing/SKILL.md) or [figures](../sa-figure-production/SKILL.md) for requested manuscript or figure work, carrying over verified values and claim bounds.
