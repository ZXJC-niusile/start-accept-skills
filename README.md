# start-accept-skills

中文 · [English](README.en.md)

面向计算机科研的 Codex 技能插件：1 个流程协调技能加 10 个专项技能，覆盖从读文献、选题、设计实验，到写作、绘图、审稿、修订核验和投稿检查的全过程。适用于方法、系统、Benchmark 和理论类研究，可以从任意阶段开始，也可以只用其中一个技能。

## 技能一览

| 阶段 | 技能 | 做什么 |
|---|---|---|
| 协调 | `sa-workflow` | 规划跨阶段工作、恢复已有项目、在技能之间交接产物 |
| 文献 | `sa-paper-reading` | 检索、精读、比较论文，所有结论可追溯到原文位置 |
| 选题 | `sa-topic-selection` | 比较候选方向的新颖性证据、价值、可行性和关键风险 |
| 设计 | `sa-research-design` | 设计基线、指标、数据划分、消融和成败判据 |
| 代码 | `sa-code-audit` | 核对代码实现是否符合论文或实验方案 |
| 分析 | `sa-experiment-analysis` | 审查实验记录、公平比较结果、界定结论能说到哪一步 |
| 写作 | `sa-paper-writing` | 起草、修改、翻译、润色 Markdown/LaTeX 稿件 |
| 绘图 | `sa-figure-production` | 制作动机图、方法图、数据图，交付可编辑图源 |
| 审稿 | `sa-scientific-review` | 评估贡献、方法和证据，给出有定位的意见 |
| 复审 | `sa-revision-check` | 核对既有意见是否解决，或在固定标准下比较版本 |
| 投稿 | `sa-submission-check` | 检查语言、格式、引用、图表和会议/期刊要求 |

## 安装

需要已登录、且支持插件命令的 Codex CLI：

```sh
git clone https://github.com/ZXJC-niusile/start-accept-skills.git
cd start-accept-skills
codex plugin marketplace add .
codex plugin add start-accept-skills@start-accept-research
codex plugin list --marketplace start-accept-research --json
```

请保留完整仓库：技能依赖 `shared/` 和 `scripts/` 中的共享资源，单独复制某个技能目录无法正常工作。安装后在新会话中确认 11 个技能可见。已安装的其他技能不会被停用，职责重叠时请在请求中写明本包的技能名。

**更新**：在仓库根目录执行 `git pull --ff-only`，再重新执行上面的 `codex plugin add` 和 `codex plugin list` 两条命令，核对版本。修改源码不会自动刷新已安装的缓存。如果 marketplace 仍指向旧目录，先执行 `codex plugin marketplace remove start-accept-research`，再从当前仓库重新安装。

**卸载**：

```sh
codex plugin remove start-accept-skills@start-accept-research
codex plugin marketplace remove start-accept-research   # 不再需要该 marketplace 时才执行
```

卸载不会删除研究产物或其他技能。

**不安装直接使用**：让代理读取 `<仓库目录>/skills/<技能名>/SKILL.md` 即可。

**环境要求**：纯指令任务只需要能读取本地文件的代理；状态脚本需要 Python 3.10+（仅用标准库）；检索、绘图渲染和 LaTeX 编译使用宿主已有工具。本包不含 MCP 服务、后台进程或任何凭据。

## 使用

在请求中写明技能名，并附上材料和目标：

- `用 sa-paper-reading 精读这篇论文，解释方法和证据。`
- `用 sa-paper-writing 压缩这一段，保留数字、引用和必要限定。`
- `用 sa-experiment-analysis 检查这张结果表能否支持“显著优于基线”。`
- `用 sa-revision-check 核对这些审稿意见是否已解决。`
- `用 sa-workflow 根据现有材料继续这个研究项目。`

使用约定：

- 默认用中文沟通，稿件语言跟随原稿或你的要求。
- 单项任务直接用对应技能，不强制生成计划或台账；需要追踪的审稿问题才建立台账，跨阶段工作才使用 `sa-workflow` 和状态记录。
- 选题、核心主张变更、超出预算的实验由你决定，已经给出的决定和授权不会被反复确认。
- 论文报告、代码观察、实际测量和推断会分开标注；缺失的证据明确写成未知，不会补编。
- 私有代码和原始数据默认留在本地。
- 本包不保证论文被录用；文件哈希只证明内容没有变化，不证明科学结论正确。

跨阶段项目可以用脚本登记文件版本、恢复进度和维护审稿问题台账，用法见 [shared/LOCAL_OPERATIONS.md](shared/LOCAL_OPERATIONS.md)。

## 开发

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate_package.py
python -B -m unittest discover -s tests -v
git diff --check
```

本仓库通过 Git 分发。反馈问题时请附上技能名、脱敏后的最小输入、期望行为和实际输出。

## 许可与致谢

本项目新编写的内容采用 [MIT 许可](LICENSE)。

本包的能力设计参考了 17 个已有的社区科研技能，全部指令都为本包重新编写，没有复制原项目的代码、文本、图像、字体或模板资源。MIT 许可不覆盖这些第三方作品，原作者保留其各自的权利。已知来源如下：

- **MIT**：humanizer（Siqi Chen，[blader/humanizer](https://github.com/blader/humanizer)）、paperjury（Yiran Wang）、peer-review（K-Dense Inc.）、let-accept-review。
- **CC BY 4.0**：idea-evaluator、intro-drafter、figure-designer、tech-paper-template、benchmark-paper-template、pre-submission-reviewer、vibe-research-workflow。
- **CC BY-NC 4.0**：scientific-figure-making / figures4papers（[ChenLiu-1996/figures4papers](https://github.com/ChenLiu-1996/figures4papers)）。本包仅参考其设计理念，未打包其中任何内容。
- **未声明许可**：academic-paper-review（目录名 deerflow-paper-review）、academic-paper-reviewer、ccf-paper-reviewer、experiment-data-analysis、investigate-codebase。

未能确认的上游作者信息保持空缺，没有补编。如需向本包加入第三方资源，请同时记录来源并保留原许可声明。
