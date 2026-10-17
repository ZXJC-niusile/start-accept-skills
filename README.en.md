# start-accept-skills

[中文](README.md) · English

**11 collaborative skills for computer-science research: one workflow coordinator and ten functional skills.**

Work from literature and topic selection through study design, code auditing, experiment analysis, writing, figures, scientific review, revision verification and submission checks. Supports methods, systems, benchmarks and applicable theory work. Enter at any stage.

[GitHub](https://github.com/ZXJC-niusile/start-accept-skills) · Version **0.1.3** · [MIT](LICENSE) · [Sources and attribution](NOTICE.md)

## Install

Clone the repository for direct installation. With an authenticated Codex CLI supporting plugins, run:

```sh
git clone https://github.com/ZXJC-niusile/start-accept-skills.git
cd start-accept-skills
codex plugin marketplace add .
codex plugin add start-accept-skills@start-accept-research
codex plugin list --marketplace start-accept-research --json
```

The ZIP is an optional fixed-version download; SHA-256 checks download integrity. Neither is required for installation. See the installation guide below for activation, updates and removal.

Do not copy individual skill folders: they depend on bundled `shared/`, `scripts/` and sibling skills. Existing skills are not disabled. Select this package explicitly when overlapping skills are installed. Without installing, ask an agent to read `<package>/skills/<skill-name>/SKILL.md` directly.

See the bilingual [installation guide](docs/INSTALL.md) and [host acceptance record](docs/HOST_ACCEPTANCE.md). No MCP server, daemon or credentials are bundled. Instruction-only tasks need no Python; state scripts require Python 3.10+. Search, image generation, PDF and LaTeX use host-provided tools.

## Use

Select a skill or name it in your request. Supply the actual materials, objective and constraints.

| Task | Inputs | Example request |
|---|---|---|
| Topic selection | Ideas, literature, time and resources | Use sa-topic-selection to compare these directions, consider the strongest plausible adaptation of prior work and propose a cheap pilot. Leave the final topic decision to me. |
| Study design | Selected question, claim, budget | Use sa-research-design to specify baselines, metrics, splits and fallback scope. Do not run experiments. |
| Full drafting | Method, results, citation keys, section | Use sa-paper-writing to draft the Introduction, connect the research gap to the mechanism and keep missing-input notes separate. |
| Local editing | Original text, objective, invariants | Use sa-paper-writing to shorten this paragraph while preserving numbers, citation keys and necessary qualifications. Return the revision directly. |
| Method figure | Mechanism, conditions, size, existing source | Use sa-figure-production to create an editable method figure. Report export, AI image and source-render inspection statuses separately. |
| Resume a project | Existing artifacts and current objective | Use sa-workflow to identify the current stage and continue the authorized work. |

Communication defaults to Chinese; request another language as needed. Manuscript language follows the target document. Model and reasoning effort are host choices; historical Astra High evaluations do not establish a minimum requirement. Model, search and image calls may incur host-side costs.

## Skills

| Skill | Responsibility | Outputs |
|---|---|---|
| sa-workflow | Coordinate stages | Plan, state, handoffs |
| sa-paper-reading | Search, read and compare literature | Source-grounded reading cards and research context |
| sa-topic-selection | Compare questions and feasibility | Candidate directions, novelty evidence and risks |
| sa-research-design | Specify a testable study | Baselines, metrics, splits, ablations, proof obligations |
| sa-code-audit | Understand and audit implementation | Code locations and implementation–claim mapping |
| sa-experiment-analysis | Audit data and bound conclusions | Fair comparisons, analysis tables, supported claims |
| sa-paper-writing | Draft, revise, translate and polish | Markdown/LaTeX manuscript text |
| sa-figure-production | Produce motivation, method and data figures | Editable source, exports, captions, visual checks |
| sa-scientific-review | Assess contributions and evidence | Located findings and issue records |
| sa-revision-check | Verify existing findings or compare versions | Closure evidence, open issues and regressions |
| sa-submission-check | Check language, format, citations and requirements | Scoped quality report |

**Read → Select → Design → Audit/Analyze → Write/Draw → Review → Revise → Verify revisions → Check submission.**

Skip inapplicable stages. Small edits need no project ledger. The host implements code and runs experiments under the project task. Users retain decisions on topics, central-claim changes and expensive work beyond existing authorization.

## Evidence and limits

Distinguish paper reports, code observations, measurements and inference. Issue closure requires revision evidence; upstream version changes affect downstream findings. Private code and raw data stay local by default, and web delegation follows project configuration. See the [shared contract](shared/CONTRACT.md) and [local operations](shared/LOCAL_OPERATIONS.md).

Structural checks and selected synthetic scenarios have been exercised. Paired planning, prose and AI diagram samples showed comparable usability to corresponding legacy skills, not overall superiority. Recent refinements received structural checks and implementer self-checks, not proof of improved performance. SVGs require their own rendered inspection. This is neither an acceptance guarantee nor an OpenAI certification. See [evaluation scope](docs/EVALUATION.md) and [documentation alignment](docs/OPENAI_ALIGNMENT.md).

## Develop and share

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate_package.py --runtime-only
python scripts/build_release.py
```

The allowlisted build emits a ZIP, SHA-256 and manifest, excluding raw evaluation traces, development snapshots and personal configuration. Publish the prepared files rather than the entire development directory. See [release notes](docs/RELEASE.md).

For issues, include the skill name, expected behavior, sanitized minimal inputs and actual output. Maintenance prioritizes real failures over repeated full-suite testing.

Newly authored material is MIT licensed. The [migration table](provenance/MIGRATION.md) records capabilities adapted and rewritten from 17 legacy skills. Third-party rights remain intact; noncommercial plotting scripts, images and fonts are not bundled. Preserve LICENSE, NOTICE and provenance records.
