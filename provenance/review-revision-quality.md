# Review, revision, and submission sources

Created 2026-10-06. Source paths below are relative to the original collection root, not runtime dependencies. SKILL bodies were read; selected resources informed the rewrite. review-engine-v3.md was read only through its opening 100 lines; its full-file hash identifies that snapshot.

All new skill prose and templates in this group were rewritten for the approved package. No original script, template, or diagram was copied. This record preserves intellectual provenance and does not assert a license grant for unlicensed source material.

| Source read | SHA-256 |
|---|---|
| skills/academic-paper-reviewer/SKILL.md | f006520307ce207c656d75fb7cadc37c6344d4bbee8e9af48d3115554010f4da |
| skills/ccf-paper-reviewer/SKILL.md | ba9e673a90ae2111a9441910cea8582859db624a218cb84a1d1853d3405a1c3b |
| skills/let-accept-review/SKILL.md | 9b5759178d755e0f7eba6fc1272ada4482782e8c3368d909b45b2573eb8ce957 |
| skills/peer-review/SKILL.md | 4591645c59b057d0d12875134ab02560ca15fc073c9a47a6d21ff74ab0fb2c73 |
| skills/pre-submission-reviewer/SKILL.md | c4ee9268905dbc6b1200606c459bb262fec10a5991eaa8115c14cd86da142fcb |
| skills/paperjury/SKILL.md | 3b05ddbb4448850ac8eeff66351c8794deea8034bdfeb78fcc215b73076707e6 |
| skills/ccf-paper-reviewer/references/version-comparison.md | f0381f9f10e7f29bc58bf4835b256029978d567382d7698641fce2912ce0e3a3 |
| skills/ccf-paper-reviewer/references/universal-review-rubric.md | b0aa8358093c4c0913e08ef069670d5d06a272b2e5fe4ad842e427088e6e55a1 |
| skills/let-accept-review/references/issue-ledger.md | da230f4cc2d01d1ae45f30360bbf11d8825b02fe3e49beab17fc1949aab5ac38 |
| skills/let-accept-review/references/evidence-contract.md | ea6da018fc204a8719fdbfc66aa25bb8631d3435fe0b671b0dc87ea3dff50f53 |
| skills/let-accept-review/references/rubrics/core-scientific-review.md | 411929a9aacaed1fcde555315d53a1298fdf1cdc8e62abd22a7292a3c503dba8 |
| skills/peer-review/references/statistical_reproducibility.md | c0ae6ad51095e8271c6abd0dff54926f04514139f6d82bd4b725ce6f5efe51d3 |
| skills/pre-submission-reviewer/references/latex-rules.md | a9aff5c2fc256eb0b7a3294cb4d97616684c91b778ea8f9652944fd2db2ecc16 |
| skills/paperjury/references/ledger-schema.md | c0fcf0e432d7f1d90edf866439789272374794bc48cf2bbfc3f6e75edb330a51 |
| skills/paperjury/references/review-engine-v3.md | 18e2e93712534466734e9e71360b8eae53acbd2ff6201eb96748578bd6fbdb6b |
| skills/paperjury/LICENSE | ed49ce3abb5312534a3f24ce7ccab211856332685862c73b1712e69db1c6bae9 |

## Migration decisions

| Original skill | Destination | Retained / rewritten | Excluded |
|---|---|---|---|
| academic-paper-reviewer | sa-scientific-review; sa-revision-check | Anchored criticism, explicit dissent, optional differentiated perspectives, evidence before response claims | Fixed five-seat protocol, mandatory persona confirmation, cross-model calibration claims, old ecosystem contracts |
| ccf-paper-reviewer | sa-scientific-review; sa-revision-check; sa-submission-check | CS claim/evidence evaluation; frozen comparison criteria; distinct progress, readiness and confidence | Missing ccf-common/writer/rebuttal dependencies; universal numeric scoring; unconditional report overwrite |
| let-accept-review | all three | Typed evidence, single ledger owner, close criteria and resolution evidence, unknown checks | Mandatory intake form for ordinary author-owned material; terminal resolutions that cannot reopen after source changes |
| peer-review | sa-scientific-review; sa-submission-check | Reporting versus validity distinction; statistical denominators; confidential review restrictions; citation-support limits | Biomedical guideline machinery and local CLI suite; mandatory author-owned-work forms |
| pre-submission-reviewer | sa-submission-check | Language, cross-references, visual inspection, format, anchored repair guidance | Vocabulary-count scoring; automatic em-dash/raster penalties; incorrect blanket prohibition on hyphenated labels; required six-part structures |
| paperjury | sa-scientific-review; sa-revision-check | Strongest defense of findings; stable issues; concrete closure criteria; preserved contested findings | Fixed jury/quorum engine, model pinning, automatic updater, forced edit approvals, edit loops inside assessment skill |

## License observations

- academic-paper-reviewer and ccf-paper-reviewer: no license declaration in the inspected SKILL frontmatter. No copying of their implementation or substantial wording.
- let-accept-review: SKILL declares MIT. No separate license text was inspected.
- peer-review: SKILL declares MIT and names K-Dense Inc. No separate license text was inspected.
- pre-submission-reviewer: SKILL declares CC-BY-4.0. Attribution is provided by its named source and hash above; its checklist was critically redesigned, with rigid or incorrect rules excluded.
- paperjury: SKILL declares MIT; LICENSE was read and identifies Copyright (c) 2026 Yiran Wang. No source implementation copied.

The new group does not assign a license to the whole package. Source-derived ideas and actual code copying remain distinct; any later copying must carry the original notices and compatible terms.
