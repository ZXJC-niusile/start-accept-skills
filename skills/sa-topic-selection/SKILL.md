---
name: sa-topic-selection
description: Generate and compare computer-science research directions, assessing novelty evidence, value, feasibility, and decisive risks. Use for choosing or narrowing a topic; study protocols and manuscript review belong to other skills.
---

# Select a research direction

Return a decision-ready comparison grounded in available evidence, following the [shared contract](../../shared/CONTRACT.md). The user owns the final topic choice unless already delegated.

## Work

- Establish the scientific question, intended contribution, relevant setting, and stated resources. Use known budget, compute, data access, skills, and deadline; leave absent constraints unknown rather than inventing capacity or project lifetime.
- For an existing idea, locate its closest conceptual alternatives, including a straightforward adaptation of the strongest relevant existing approach. State what remains scientifically unresolved after that adaptation; a new setting alone does not establish a method contribution. For brainstorming, derive candidate questions from evidenced limitations or unexplained behavior, not arbitrary combinations of fashionable methods.
- Compare each candidate's potential value (effectiveness, efficiency, reliability, access cost, transfer, or theoretical understanding as relevant), distinct contribution, accessible evidence, execution burden, and failure risk. Explain tradeoffs instead of producing unsupported numeric scores.
- Bound novelty by the actual literature examined and search date. Use [paper reading](../sa-paper-reading/SKILL.md) for targeted literature work when needed. A new task name, absence of a search hit, or model size change alone does not establish novelty.
- Test decisive risks: a prior result already answers the question; required data is inaccessible; the proposed measurement cannot distinguish the claim; the work cannot fit stated resources. Distinguish confirmed blockers from unresolved feasibility questions. Offer a narrower viable variant when supported.
- Specify the cheapest informative pilot or proof obligation, what outcomes would favor or weaken the direction, and what decision it would unlock. This is a selection probe, not a complete experiment protocol or permission to run it.

## Deliver

Use [the decision table](references/decision-table.md) for multiple candidates. Recommend pursue, refine, investigate first, or deprioritize with rationale and confidence; these are research-planning judgments, not predicted venue acceptance. State unresolved choices and the evidence needed to settle them. A theory direction may be valuable without experiments or immediate external deployment.

Send the selected question, assumptions, resource envelope, and decision history to [research design](../sa-research-design/SKILL.md). Route requests to evaluate a finished manuscript to [scientific review](../sa-scientific-review/SKILL.md), and requests for manuscript prose to [paper writing](../sa-paper-writing/SKILL.md).
