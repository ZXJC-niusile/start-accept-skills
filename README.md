# start-accept-skills

English · [中文](README.zh-CN.md)

11 skills for computer-science research, from literature and study design to writing, review and project coordination. Start at any stage.

## Install

With an authenticated Codex CLI supporting plugins:

```sh
git clone https://github.com/ZXJC-niusile/start-accept-skills.git
cd start-accept-skills
codex plugin marketplace add .
codex plugin add start-accept-skills@start-accept-research
```

Keep the complete repository: skills depend on shared resources. See the [installation guide](docs/INSTALL.md) for updates and removal.

## Use

Name the skill and provide your materials and objective. For example:

- `Use sa-paper-reading to explain this paper's method and evidence.`
- `Use sa-paper-writing to shorten this paragraph, preserving numbers, citations and qualifications.`
- `Use sa-revision-check to verify whether these review issues are resolved.`
- `Use sa-workflow to continue this research project from the existing artifacts.`

Communication defaults to Chinese; request another language as needed. Manuscript language follows the document. Use a specialist for a single task; coordination and state records are for multi-stage work.

| Skill | Purpose |
|---|---|
| sa-workflow | Coordinate stages, resume projects and hand off artifacts |
| sa-paper-reading | Search, read and compare literature |
| sa-topic-selection | Compare directions, novelty and feasibility |
| sa-research-design | Design baselines, metrics, splits and ablations |
| sa-code-audit | Check implementation against research claims |
| sa-experiment-analysis | Analyze experiments, compare results and bound conclusions |
| sa-paper-writing | Draft, revise, translate and polish manuscripts |
| sa-figure-production | Create research figures and editable sources |
| sa-scientific-review | Assess contributions, methods and evidence |
| sa-revision-check | Verify revisions, track issues and identify regressions |
| sa-submission-check | Check language, formatting, citations and submission requirements |

Search, figure production and compilation use host tools. State scripts require Python 3.10+; see [local operations](shared/LOCAL_OPERATIONS.md).

## Develop

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate_package.py
python -B -m unittest discover -s tests -v
```

Distribution and updates use Git; standalone ZIP releases are discontinued. Structural validation does not establish scientific correctness or improved model performance. See the [evaluation record](docs/EVALUATION.md).

[Maintenance history](docs/RELEASE.md) · [MIT license](LICENSE) · [Third-party sources](NOTICE.md)
