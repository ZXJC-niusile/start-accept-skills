# Workflow and code audit provenance

The integrator read the full `vibe-research-workflow/SKILL.md` and
`investigate-codebase/SKILL.md`, plus the latter's four investigation guides.
Exact original source paths and SHA-256 values are recorded in sources.json.

`vibe-research-workflow` declares CC-BY-4.0 in frontmatter. Its phase organization
and human responsibility informed the coordinator. This implementation replaces
the original's blanket rejection of paper drafting, fixed six-rule recital,
fixed tool recommendations and unvalidated productivity multiplier with the
approved scope, existing authorization and explicit completion evidence.

No license field was observed in `investigate-codebase/SKILL.md`. Its ideas of
targeted inspection, source/runtime distinction and independent correctness
oracles inform a new concise instruction file. Original scripts and text blocks
are not copied. The new artifact validator and tests implement the user's shared
contract using Python's standard library; they are not adapted source validators.

The coordinator owns cross-stage handoffs; the code-audit skill owns inspection.
Neither implements or executes a research project by default. Useful constraints
were retained semantically and rewritten for a computer-science research context.
