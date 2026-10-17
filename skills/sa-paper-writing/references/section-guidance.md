# Drafting full sections

Load only for structural or full-section drafting. Start with the existing venue structure when available; verified current venue rules take precedence over a generic outline.

| Section | Content to establish | Avoid |
|---|---|---|
| Abstract | Problem, approach, main supported result and scope | Results absent from the body; uncited novelty superlatives |
| Introduction | Concrete problem, grounded gap, research goal, technical difficulty, solution and evidenced contributions | Forced six-paragraph molds or invented obstacles to match modules |
| Related work | Fair comparison of actual capabilities and assumptions, linked to verified sources | Treating a missing description as a proven inability |
| Method/system | Setting, notation, assumptions, inputs, outputs, algorithm or architecture, design reasons, costs and limits | Claiming planned components are implemented |
| Benchmark | Construct definition, source/collection pipeline, splits, deduplication, annotation/QC, metric protocol, coverage and release limits | Equating machine filtering with human validation; leakage-blind splits |
| Experiments | Questions, setup, baselines, metrics, budgets, measured comparisons, uncertainty and important exceptions | A number-by-number narration or unverified causal explanations |
| Theory | Definitions, assumptions, proposition scope, proof steps and relation to prior results | Unproved theorem claims or empirical requirements imposed by habit |
| Discussion/limitations | Interpretations separated from observations, limits and concrete implications | Scope expansion beyond available evidence |
| Conclusion | What was established and under which conditions | New evidence or generic promises |
| Appendix | Details needed to reproduce or check claims, full protocols and proofs | Hiding conditions that change the central claim |

## Argument continuity

For an Introduction, make the causal argument explicit: what the closest approaches already achieve, what remains unresolved under their actual assumptions, why that gap is difficult, and how the proposed mechanism addresses it. Do not infer a prior method's inability from missing documentation. When a concrete example motivates the problem, return to it when explaining the mechanism if that helps show what changes; no fixed paragraph sequence is required.

Place each material limitation where it bounds the corresponding claim. For example, identify a development pilot as such in the results paragraph and explain what it cannot establish there; avoid repeating the whole limitation list in the motivation, method and contributions. Keep conditions needed to interpret a standalone abstract, caption or claim even if they appear elsewhere. Author-side verification gaps stay in notes unless they affect the scientific meaning of the manuscript itself.

## Citation and markup integrity

Read the cited source or supplied evidence before using it to support a claim. Keep a known citation key unchanged. When citation verification is unavailable, record the missing source author-side instead of manufacturing a bibliography entry. Dates, venue requirements and novelty claims need current source checks.

Preserve math delimiters, labels, environments and reference keys. Escape characters for the actual target format, not by a blanket Markdown-to-LaTeX substitution. Do not convert a multi-file project into a standalone file without need. For Word or other formats, use an available appropriate document tool and report any conversion loss.

## Revision and style

Write the concrete operation, observation or limitation first. Keep one technical term for one concept. Remove exaggerated significance and empty connective phrases; preserve words with a precise technical meaning. A change in punctuation is not evidence of human authorship. Do not promise plagiarism or AI-detector evasion.

Captions are authored here when requested as prose: describe what is actually visible, define symbols and uncertainty, and state the allowed conclusion. Figure production supplies a draft caption with the graphic; writing integrates that caption into the manuscript without changing the evidence.
