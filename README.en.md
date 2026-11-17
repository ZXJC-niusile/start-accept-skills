# start-accept-skills

[中文](README.md) · English

A Codex skill plugin for computer-science research: one coordinator plus ten specialist skills, covering literature reading, topic selection, study design, writing, figures, scientific review, revision verification and submission checks. It supports methods, systems, benchmark and theory work. Start at any stage, or use a single skill on its own.

## Skills

| Stage | Skill | What it does |
|---|---|---|
| Coordination | `sa-workflow` | Plan multi-stage work, resume projects, hand off artifacts between skills |
| Literature | `sa-paper-reading` | Search, read and compare papers with traceable source locations |
| Topic | `sa-topic-selection` | Compare directions by novelty evidence, value, feasibility and decisive risks |
| Design | `sa-research-design` | Specify baselines, metrics, splits, ablations and success criteria |
| Code | `sa-code-audit` | Check an implementation against a paper or protocol |
| Analysis | `sa-experiment-analysis` | Audit runs, compare results fairly and bound what conclusions the data supports |
| Writing | `sa-paper-writing` | Draft, revise, translate and polish Markdown/LaTeX manuscripts |
| Figures | `sa-figure-production` | Produce motivation, method and data figures with editable sources |
| Review | `sa-scientific-review` | Assess contributions, methods and evidence with anchored findings |
| Re-review | `sa-revision-check` | Verify prior review issues or compare versions under fixed criteria |
| Submission | `sa-submission-check` | Check language, formatting, citations, figures and venue requirements |

## Install

Requires an authenticated Codex CLI with plugin support:

```sh
git clone https://github.com/ZXJC-niusile/start-accept-skills.git
cd start-accept-skills
codex plugin marketplace add .
codex plugin add start-accept-skills@start-accept-research
codex plugin list --marketplace start-accept-research --json
```

Keep the complete repository: skills depend on shared resources in `shared/` and `scripts/`, so copying a single skill folder will not work. After installing, confirm in a fresh session that all 11 skills are visible. Other installed skills stay enabled; name this package's skill in your request when responsibilities overlap.

**Update**: run `git pull --ff-only` from the repository root, then repeat the `codex plugin add` and `codex plugin list` commands above and check the version. Editing the source does not refresh the installed cache automatically. If the marketplace still points to an old directory, run `codex plugin marketplace remove start-accept-research` and install again from this repository.

**Remove**:

```sh
codex plugin remove start-accept-skills@start-accept-research
codex plugin marketplace remove start-accept-research   # only if the marketplace is no longer needed
```

Removing the plugin does not delete research outputs or other skills.

**Use without installing**: ask the agent to read `<repository>/skills/<skill-name>/SKILL.md`.

**Requirements**: instruction-only tasks need an agent that can read local files. State scripts need Python 3.10+ (standard library only). Search, rendering and LaTeX compilation use tools available on the host. No MCP server, background process or credentials are bundled.

## Use

Name the skill and supply your materials and objective:

- `Use sa-paper-reading to explain this paper's method and evidence.`
- `Use sa-paper-writing to shorten this paragraph, preserving numbers, citations and qualifications.`
- `Use sa-experiment-analysis to check whether this results table supports "significantly outperforms the baseline".`
- `Use sa-revision-check to verify whether these review issues are resolved.`
- `Use sa-workflow to continue this research project from the existing artifacts.`

Conventions:

- Communication defaults to Chinese; ask for another language as needed. Manuscript language follows the document or your instruction.
- A single task goes straight to its specialist; no plan or issue ledger is required. Ledgers are for review issues that need tracking, and `sa-workflow` with state records is for multi-stage work.
- You decide topics, changes to the central claim and experiments beyond budget. Decisions and authorization you have already given are not asked again.
- Paper reports, code observations, actual measurements and inference are labeled separately. Missing evidence stays explicitly unknown rather than being filled in.
- Private code and raw data stay local by default.
- This package does not guarantee acceptance. A file hash shows content is unchanged; it does not show that a scientific conclusion is correct.

For multi-stage projects, scripts can register file versions, resume progress and maintain a review-issue ledger; see [shared/LOCAL_OPERATIONS.md](shared/LOCAL_OPERATIONS.md).

## Develop

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate_package.py
python -B -m unittest discover -s tests -v
git diff --check
```

The repository is distributed via Git. When reporting an issue, include the skill name, a sanitized minimal input, the expected behavior and the actual output.

## License and acknowledgements

Newly authored material in this project is released under the [MIT License](LICENSE).

The capabilities were designed with reference to 17 existing community research skills. All instructions were rewritten for this package; no code, text, images, fonts or template assets were copied. The MIT License does not cover those third-party works, whose authors retain their rights. Known sources:

- **MIT**: humanizer (Siqi Chen, [blader/humanizer](https://github.com/blader/humanizer)), paperjury (Yiran Wang), peer-review (K-Dense Inc.), let-accept-review.
- **CC BY 4.0**: idea-evaluator, intro-drafter, figure-designer, tech-paper-template, benchmark-paper-template, pre-submission-reviewer, vibe-research-workflow.
- **CC BY-NC 4.0**: scientific-figure-making / figures4papers ([ChenLiu-1996/figures4papers](https://github.com/ChenLiu-1996/figures4papers)). Only its design ideas were consulted; none of its content is bundled.
- **No declared license**: academic-paper-review (directory deerflow-paper-review), academic-paper-reviewer, ccf-paper-reviewer, experiment-data-analysis, investigate-codebase.

Upstream author details that could not be confirmed are left blank rather than invented. If you add third-party resources, record their source and keep the original license notices.
