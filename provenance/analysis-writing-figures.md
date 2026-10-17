# Analysis, writing and figures provenance

These sources were inspected locally for capability mapping on 2026-10-06. Paths below are repository-relative source inventory, not runtime dependencies. New instructions, templates and routing cases were written for this package; no source scripts, plots, example data or image assets were copied.

| Source capability | Decision | New owner | Changes / excluded material |
|---|---|---|---|
| experiment-data-analysis | Retain concepts, rewrite | sa-experiment-analysis | Preserve integrity, fair comparison and claim bounds; manuscript prose ownership moves to writing |
| humanizer | Merge, rewrite | sa-paper-writing | Preserve plain language and author meaning; omit blanket vocabulary and punctuation bans and any detector-evasion promise |
| intro-drafter | Merge, rewrite | sa-paper-writing | Retain problem-to-contribution logic; remove six-paragraph and one-to-one module requirements |
| tech-paper-template writing guidance | Merge, rewrite | sa-paper-writing | Retain argument structure; remove fixed contribution/module counts |
| benchmark-paper-template writing guidance | Merge, rewrite | sa-paper-writing | Retain construction/evaluation rationale; omit mandated first claims, fixed figure placements and promotional patterns |
| paperjury edit layer | Merge, rewrite | sa-paper-writing | Preserve markup, evidence and edit scope; remove missing external writing dependency, blanket repeat approval, workflow runtime and update checks |
| figure-designer | Merge, rewrite | sa-figure-production | Preserve visual purpose, design and inspection; extend to production and theory diagrams; remove fixed taxonomy and unsupported universal figure-count claims |
| scientific-figure-making (figures4papers) | Concept review only; implementation excluded | sa-figure-production | Reproducible figures and editable exports implemented with new instructions; exclude repository scripts, palettes, presets, demo images and noncommercial assets |

## License observations

- intro-drafter and figure-designer declare CC-BY-4.0 in their SKILL.md frontmatter. Attribution: local skill titles and source paths listed below; author/upstream origin is not established by the inspected entrypoints. Changes are summarized above. License URL: https://creativecommons.org/licenses/by/4.0/ . No text blocks or assets were copied.
- humanizer attributes the upstream pattern taxonomy to Siqi Chen / github.com/blader/humanizer; LICENSE.blader-humanizer is MIT, copyright 2025 Siqi Chen. No taxonomy text was reproduced; new wording focuses on scientific meaning preservation.
- paperjury LICENSE is MIT, copyright 2026 Yiran Wang. No runtime scripts or prompt templates were copied. Its edit-safety concepts informed the new writing interface.
- figures4papers LICENSE is Creative Commons Attribution-NonCommercial 4.0. The inspected design reference attributes figures4papers to https://github.com/ChenLiu-1996/figures4papers . No code, palette, assets or copied instructions are distributed here. License URL: https://creativecommons.org/licenses/by-nc/4.0/ . This inspection does not establish a package-wide MIT grant.
- experiment-data-analysis entrypoint does not state a license. The tech-paper-template and benchmark-paper-template entrypoint frontmatter declares CC-BY-4.0; their first 15 lines were inspected to verify this. Their references informed requirements; no source paragraphs were copied. Distribution review should preserve uncertainty where upstream author attribution is absent.

## Exact inspected source snapshots

| Source path | SHA-256 |
|---|---|
| `skills/experiment-data-analysis/SKILL.md` | `60cfc91388add0a204781e4b2d386bff7500b8beb0f6df55b0d16a98be5ef5ad` |
| `skills/humanizer/SKILL.md` | `77071445054a3d8a26c3b665b5784204d34af1cadff9a00daa854b0623410042` |
| `skills/humanizer/LICENSE.blader-humanizer` | `caa1be9cba41c1afb88fe730ab1a4e04728295ea5b29ac2ee9f003a4ffbe3a77` |
| `skills/intro-drafter/SKILL.md` | `635c5254127dcc844c8c61b487ee2d7048dda05737def291a8ddd261ac699499` |
| `skills/figure-designer/SKILL.md` | `bb43872f2e77d570cbd160616066fab8fbc571205b5328c9c2967f93f920b38c` |
| `skills/figures4papers/SKILL.md` | `121cdc63bc6828e45f11332cb421641c81ab42bfdb149a3c2d0829daaa411b19` |
| `skills/figures4papers/references/design-theory.md` | `d5f6bfd03cdd34d8b4c2f345b4d630985a0a1e17dcd4dd6631d60b896386fcf8` |
| `skills/figures4papers/LICENSE` | `3003c8ec6028420f2e4029adfa5b90f120921dcdc9f3f4741897ad8296288a47` |
| `skills/paperjury/SKILL.md` | `3b05ddbb4448850ac8eeff66351c8794deea8034bdfeb78fcc215b73076707e6` |
| `skills/paperjury/references/writing-toolkit.md` | `755258fd7b925b9ecce0a65f931a96d2e0c143cfe96fc4c68743bb1aee94a951` |
| `skills/paperjury/LICENSE` | `ed49ce3abb5312534a3f24ce7ccab211856332685862c73b1712e69db1c6bae9` |
| `skills/tech-paper-template/references/thinking-template.md` | `3b7728a17d548558cb9c8cca2edf6c4a4d312ba688b0e24ca2be5ff8f77cff5e` |
| `skills/benchmark-paper-template/references/paper-structure.md` | `aba22cc31960292f5f2f8f93e5c15d190ce7ec1722e3765adf457ebca64eb61c` |

The `figures4papers` directory is a junction to `skills/scientific-figure-making`; both refer to one independent skill.

Additional metadata-only snapshots (first 15 lines inspected):

- `skills/tech-paper-template/SKILL.md` SHA-256 `7e0746fc51a42b19e4934ec9d53ea7570c2f85d14e874bfa1497822e5da1a9c0`
- `skills/benchmark-paper-template/SKILL.md` SHA-256 `ab40a1dfcbce2e7859df76795118d264afa5acbe788627a47f064736a777caf6`
