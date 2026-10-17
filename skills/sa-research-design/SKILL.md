---
name: sa-research-design
description: Turn a selected computer-science question into a testable method, systems, benchmark, or theory study. Use for hypotheses, baseline and metric choices, data construction, ablations, and success criteria; manuscript drafting and result interpretation have separate owners.
---

# Design a testable study

Build an executable research specification within the stated resource envelope. Apply the [shared contract](../../shared/CONTRACT.md). Drafting a design does not authorize experiments, data collection, or changing a chosen central claim.

## Core specification

- State the question, claimed contribution under investigation, prior-work evidence, target population/setting, and assumptions. If the question itself is undecided, offer bounded alternatives and hand selection to [topic selection](../sa-topic-selection/SKILL.md).
- Connect the motivating limitation to the proposed mechanism, actual implementation challenges, and observations that would test it. Allow many-to-many relationships where justified; do not invent modules to fill a fixed template.
- For each question, specify comparison units, interventions and controls, relevant baselines, metrics and direction, denominators, repeated-measure unit, uncertainty method, negative outcomes, and predeclared success/failure criteria. Missing thresholds remain explicit decisions; do not invent a scientifically justified threshold from convention alone.
- Preserve the selected construct in the primary metric: could a system fully meet the user's stated target yet fail your metric solely because you added another capability? If so, revise the metric. Put broader capabilities in optional diagnostics or a clearly pending scope-change proposal; protocol design does not authorize that expansion.
- Select strong and relevant baselines, including plausible adaptations of existing approaches, with comparable tuning, data access, tools, and compute; record justified deviations. Identify the proposed increment over the strongest relevant comparator and the comparison that isolates it. Choose sample/repetition counts from precision, variance, paired structure, and budget, not universal minimums. Specify development versus final evaluation and controls against test-set adaptation.
- Define data provenance and versioning, split/grouping unit, leakage checks, failure/exclusion policy, and reproducibility records (code/config/data/model versions and run IDs). Denominators must preserve declared failure handling rather than silently omit failed outputs.
- Read [study modes](references/study-modes.md) only for the relevant method/system, benchmark, or theory details. Separate planned evidence from already observed evidence.

## Deliver and hand off

Provide a research specification, experiment/proof-obligation matrix, prioritized execution order, resource estimate with assumptions, and unresolved decisions. Include the measurement or counterexample that could invalidate the central claim. No manuscript prose, simulated results, or invented expected findings.

Implementation questions pass to [code audit](../sa-code-audit/SKILL.md) if code exists; actual coding and execution follow the project task. Result records go to [experiment analysis](../sa-experiment-analysis/SKILL.md). Paper outlines and prose go to [paper writing](../sa-paper-writing/SKILL.md). A user asking only to analyze existing results should go directly to the analysis owner.
