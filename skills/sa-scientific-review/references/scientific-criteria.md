# Applicable scientific criteria

Use the claim type to choose checks. The paper need not solve a larger or different problem to count as a contribution.

| Criterion | Questions and evidence |
|---|---|
| Contribution | What changes relative to the closest demonstrated prior work? Distinguish new capability, improved tradeoff, new measurement, and useful negative evidence. Do not call a citation missing without verifying its relevance. |
| Soundness | Do definitions, assumptions, algorithm, derivation, threat model, or implementation support the stated claim? Cite the precise dependency or counterexample. |
| Evaluation | Are tasks, populations, budgets, selection rules, metrics, baselines, uncertainty, and failure cases appropriate to the claim? Report protocol mismatches explicitly. |
| Reproducibility | Can a reader reconstruct the method and evidence provenance? Code availability, static inspection, tests, and reproduced results are distinct levels of evidence. |
| Scope | Do conclusions match the tested distribution or theorem assumptions? Are limitations and alternative explanations acknowledged? |
| Responsible research | Assess applicable data permissions, privacy, potential misuse, attribution, and human-study requirements from evidence. Do not infer misconduct. |

Methods papers: connect each claimed mechanism to an ablation or justified alternative evidence; avoid interpreting pooled improvements as causal proof.

Systems papers: inspect workload representativeness, hardware/software settings, throughput-latency/resource tradeoffs, scaling, and failures. A higher throughput at a different latency or cost is not a matched win.

Benchmarks: inspect construction provenance, licensing, leakage and contamination, split unit, labels and adjudication, metric validity, coverage, and evaluation reproducibility. Separate machine checks, human review, and gold labels.

Theory: evaluate definitions, quantified claims, assumptions, proof steps, edge cases, and relation to prior bounds. Experiments may be not applicable. Missing proof access limits confidence; it does not establish a false theorem.

For each finding provide an anchored observation, affected claim, criterion, impact, minimum remedy, close criterion, and confidence. Critical means a demonstrated threat to a central claim; major materially weakens its support; minor has limited consequence. Unanchored suspicions are questions. A negative claim has the same evidence burden as a positive one.

Requested new work must identify which claim needs it and why available evidence is insufficient. Consider clarification, narrowed claims, or limitations when adequate. Cosmetic preferences belong to submission checking and cannot automatically lower scientific merit.
