---
name: sa-paper-reading
description: Find, explain, and compare computer-science literature with traceable sources. Use for paper summaries, method explanations, literature maps, and reading notes; formal merit judgments belong to sa-scientific-review.
---

# Read computer-science literature

Produce an accurate account of what the sources establish and what remains unclear. Follow the [shared contract](../../shared/CONTRACT.md), which links the evidence and handoff details.

## Work

- Identify the reading question and available source coverage. Record title, version/date, accessible sections, and source links or file anchors. An abstract supports an abstract-level summary, not a claim to have checked the full method or proof.
- For retrieval, search the task's terms and plausible alternative terminology; record the search date, scope, and inclusion rationale. Prefer original papers and official artifacts. A bounded search is not an exhaustive literature review. Verify bibliographic identity and the passage supporting each consequential claim.
- Explain the problem, assumptions, inputs/outputs, central mechanism, and reported evidence. Preserve benchmark version, comparison population, metric direction and denominator. Label numbers as paper reports unless independently measured.
- For comparisons, align task setting, data access, compute, evaluation protocol, and evidence type before comparing outcomes. Mark incompatible setups instead of constructing a false leaderboard.
- Distinguish author-stated limitations from reader inferences. For theory, explain theorem conditions and what was checked; reading a theorem statement is not proof verification. For systems, identify workload, hardware, and operational conditions.
- Missing access, unavailable retrieval, or unverified citations remain explicit unknowns; never complete citations from plausible guesses.

## Deliver

Scale the answer to the question. For sustained literature work, use [the literature card](references/literature-card.md), then synthesize agreements, disagreements, coverage gaps, and useful next questions. Cite source/version/locator for central claims. Do not require a fixed number of strengths, weaknesses, papers, or searches.

If the user asks which direction to pursue, hand off grounded gaps to [topic selection](../sa-topic-selection/SKILL.md). Acceptance recommendations, scores, and formal scientific defect assessment belong to [scientific review](../sa-scientific-review/SKILL.md). Writing related-work prose belongs to [paper writing](../sa-paper-writing/SKILL.md).
