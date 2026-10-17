# Study-specific design decisions

## Methods and systems

Define the intervention and the baseline that isolates its claimed contribution. Choose ablations that distinguish competing explanations, not just component removal for its own sake. Include failure regimes and relevant transfer tests if transfer is claimed. In systems studies specify hardware/software, workload and load generation, warm-up, caching, concurrency, latency percentiles, throughput, and measurement boundaries as applicable. Match resource budgets or report the performance-cost frontier. A newer baseline is not automatically more relevant than an older one. Distinguish an adapted comparator from a faithful reproduction of the original system. If the strongest relevant comparator is infeasible, explain the missing comparison and narrow the claim rather than replacing it silently with an easy baseline. Predeclare what no incremental benefit would mean: a narrower mechanism or boundary study, a negative result, or stopping the direction; do not manufacture an algorithmic contribution.

## Benchmarks

Specify the capability to measure and why existing evaluations cannot answer the question. Define task inputs, allowed context/tools, output contract, scoring, invalid-output policy, units, subgroups, and aggregation. A parser failure is an operational outcome; distinguish it from incorrect task reasoning where evidence permits.

Map source selection, sample construction, annotation, validation, deduplication, splitting, and release to explicit inputs/outputs and responsible actors. Keep machine screening, independent human review, and final reference labels distinct. Synthetic generation or a second model's agreement does not by itself establish correct ground truth or freedom from contamination. Record disputed/ambiguous cases and adjudication policy.

Use source-level or other dependency-aware grouping before splits to prevent related items crossing boundaries. Keep tuning/calibration separate from final held-out evaluation. State unresolved training-data contamination and the limits of any provenance audit. Validate learned or model-based judges against appropriate independent reference judgments with subgroup/error checks.

Select model diversity, human comparisons, and difficulty ranges to answer the question within budget; no universal model count, target failure rate, expert-sample percentage, or required companion method applies. If adding a companion method, maintain training/evaluation separation. Difficulty alone is not construct validity.

## Theory

Specify definitions, assumptions, theorem/conjecture, comparison to known bounds, proof dependencies, and counterexample search. Distinguish a proof plan from a verified proof. Record whether empirical illustration contributes to the question; mark experiment-only fields not applicable when justified. Do not require an experimental win or deployment beneficiary for theoretical merit.

## Design matrix

| RQ/claim under test | Intervention or proof obligation | Comparator/control | Population and independent unit | Metric/criterion | Uncertainty/check | Cost and priority | Result that weakens the claim |
|---|---|---|---|---|---|---|---|

For empirical rows, include exact split/version and failure denominator in the surrounding specification. Plan confirmatory versus exploratory analyses explicitly; later changes require a recorded reason, not retroactive preregistration.
