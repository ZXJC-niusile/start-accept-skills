# Reading, selection, and design provenance

Source snapshot: local collection inspected 2026-10-06. Paths below identify historical inputs relative to the original collection root; they are provenance, not runtime dependencies. All new skill prose and templates were rewritten for this package; no source scripts or assets were copied.

| Source read | SHA-256 | License observed |
|---|---|---|
| `skills/deerflow-paper-review/SKILL.md` | `a0285baaeacc916bf45751c06db37745b195ddd4ec30e271ec1472f6cd48e8aa` | No license declaration found in SKILL.md or accompanying files (directory contains only SKILL.md) |
| `skills/idea-evaluator/SKILL.md` | `9380170484f657f9177c2e3a1a2cb5950005338eb93b839c6eb08e5559c9cf3d` | Source skill frontmatter declares CC-BY-4.0; reference inherits no separately verified license |
| `skills/idea-evaluator/references/fatal-flaws.md` | `74e13022ff7d7b6c1b4a424aefd0acafe78448124a00c0000ce44c41a6a05801` | Source skill frontmatter declares CC-BY-4.0; reference inherits no separately verified license |
| `skills/tech-paper-template/SKILL.md` | `7e0746fc51a42b19e4934ec9d53ea7570c2f85d14e874bfa1497822e5da1a9c0` | Source skill frontmatter declares CC-BY-4.0; reference inherits no separately verified license |
| `skills/tech-paper-template/references/consistency-checks.md` | `3473e9784dda0a47434428846db5bef03dced311164231d0c55a347a4688031b` | Source skill frontmatter declares CC-BY-4.0; reference inherits no separately verified license |
| `skills/benchmark-paper-template/SKILL.md` | `ab40a1dfcbce2e7859df76795118d264afa5acbe788627a47f064736a777caf6` | Source skill frontmatter declares CC-BY-4.0; reference inherits no separately verified license |
| `skills/benchmark-paper-template/references/construction-pipeline.md` | `ffe08823cf17c0ee59ad648af4b5226dabbcf5e38929f9c88845b15f32997bec` | Source skill frontmatter declares CC-BY-4.0; reference inherits no separately verified license |
| `skills/benchmark-paper-template/references/benchmark-design.md` | `2e34ef26f7f3b07d151b41914252baf9639845c021aa482a7d5181ae9662abc4` | Source skill frontmatter declares CC-BY-4.0; reference inherits no separately verified license |
| `skills/benchmark-paper-template/references/experiments.md` | `e3384e6faf1d8a69850ca97b158b35a73d8cfb4d396a9afa615721ecb3c658e9` | Source skill frontmatter declares CC-BY-4.0; reference inherits no separately verified license |

## Attribution and transformation

The local `idea-evaluator`, `tech-paper-template`, and `benchmark-paper-template` sources declare [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). This record attributes those source names and exact local snapshots; upstream author and URL were not established by the files inspected. Preserve this notice when distributing derived guidance. No broader package license is inferred from these declarations.

| Source capability | Action | New owner / change |
|---|---|---|
| Paper metadata, mechanisms, claims and literature comparison | Retain concepts; rewrite | `sa-paper-reading`; bounded source access and version anchors |
| Formal scoring and accept/reject recommendations in reading | Exclude from reading | Owned by scientific review; no automatic invocation for every paper URL |
| Research value and resource feasibility | Merge and rewrite | `sa-topic-selection`; conditional comparisons without unsupported numeric scores |
| Fatal flaws and novelty checks | Rewrite | Confirmed blockers versus uncertainty; bounded literature evidence |
| Fixed flaw counts, calendar recency rules, lifecycle predictions and paradigm score thresholds | Exclude | No universal rejection rules or invented estimates |
| Limitation, idea, challenge, mechanism consistency | Retain concept; rewrite | `sa-research-design`; justified many-to-many connections allowed |
| Benchmark gap, construction, measurement and RQ-driven evaluation | Merge and rewrite | `sa-research-design`; source grouping, fixed failure policies, calibrated judges |
| Fixed hardest-subset accuracy targets, model counts, expert percentages, mandatory companion model | Exclude | Counts and difficulty determined by validity, precision and budget |
| Paper section skeleton and Introduction drafting | Handoff | `sa-paper-writing` owns manuscript organization and prose |
| Missing external skills and hardcoded output path | Exclude | Only package-relative links and user-selected outputs |

Authoring guidance read: system skill-creator/SKILL.md and references/openai_yaml.md; package shared/CONTRACT.md. These operational instructions are not source research content.
