# start-accept-skills

中文 · [English](README.en.md)

**面向计算机科研的 11 个协作技能：一个流程入口，十个功能技能。**

覆盖阅读、选题、设计、代码审计、实验分析、写作、绘图、审稿、修订核验及投稿检查。适用于方法、系统、Benchmark 和适用的理论研究，可以从任意阶段开始。

[GitHub](https://github.com/ZXJC-niusile/start-accept-skills) · 版本 **0.1.3** · [MIT](LICENSE) · [来源与署名](NOTICE.md)

## 安装

下载完整发布包并解压，或克隆仓库。进入包含 `plugin.json` 的根目录，在已登录且支持插件的 Codex CLI 执行：

```sh
codex plugin marketplace add .
codex plugin add start-accept-skills@start-accept-research
codex plugin list --marketplace start-accept-research --json
```

包内已提供 `.agents/plugins/marketplace.json`。安装后在新一轮对话使用；桌面目录未刷新时重启客户端。以技能选择器显示的完整名称为准。保留下载目录，供本地 marketplace 更新使用。

不要只复制单个技能目录：技能依赖包内 `shared/`、`scripts/` 和相邻技能。安装不会停用旧技能，首次使用建议显式选择本包技能。不安装也可以直接请求代理读取 `<包目录>/skills/<技能名>/SKILL.md`。

详细更新、卸载与环境要求见[安装指南](docs/INSTALL.md)，实测范围见[宿主验收](docs/HOST_ACCEPTANCE.md)。没有 MCP 服务、后台程序或内置凭据。纯指令任务不需要 Python；状态脚本需 Python 3.10+。检索、图像、PDF 和 LaTeX 使用宿主已有工具。

## 使用

从技能选择器选择技能，或在请求中明确指定技能名，附实际材料、目标和约束。

| 任务 | 输入 | 请求示例 |
|---|---|---|
| 选题 | 想法、文献、时间和资源 | 用 sa-topic-selection 比较这三个方向，考虑最强已有方案的合理适配，提出最低成本试点，最终选题由我决定。 |
| 设计 | 已选问题、主张、预算 | 用 sa-research-design 设计基线、指标、划分与失败收缩方案；本次不运行实验。 |
| 完整起草 | 方法、结果、引用键、章节 | 用 sa-paper-writing 直接起草英文 Introduction，串联研究空缺与机制；缺少材料单列作者备注。 |
| 局部修改 | 原文、目标、保留项 | 用 sa-paper-writing 压缩这一段，保留数字、引用键和必要限定，直接给修改稿。 |
| 方法图 | 机制、条件、尺寸、图源 | 用 sa-figure-production 制作方法图，交付可编辑图源，分别说明导出图、AI 图与源文件渲染的检查状态。 |
| 继续项目 | 当前产物、目标 | 用 sa-workflow 识别当前阶段，继续本次已授权工作。 |

默认中文沟通，论文语言遵循目标稿件。模型和思考档位由宿主选择，历史 Astra High 评测不构成最低要求。模型、检索和图像调用可能产生宿主侧费用。

## 技能分工

| Skill | 职责 | 主要产物 |
|---|---|---|
| sa-workflow | 跨阶段协调 | 阶段计划、状态、交接 |
| sa-paper-reading | 检索、精读、比较 | 文献卡片、来源、研究脉络 |
| sa-topic-selection | 候选问题与可行性 | 方向比较、创新证据、风险 |
| sa-research-design | 可检验方案 | 基线、指标、划分、消融、证明义务 |
| sa-code-audit | 理解与审计实现 | 代码定位、实现与主张对应 |
| sa-experiment-analysis | 数据与结论边界 | 公平比较、分析表、可支持结论 |
| sa-paper-writing | 起草、修改、翻译、润色 | Markdown/LaTeX 正文 |
| sa-figure-production | 动机、方法与数据图 | 图源、导出、图注、视觉检查 |
| sa-scientific-review | 贡献与证据审稿 | 有定位的意见、问题台账 |
| sa-revision-check | 既有意见或版本复审 | 关闭证据、未解决项、回归 |
| sa-submission-check | 语言、格式、引用、投稿要求 | 质量检查报告 |

**阅读 → 选题 → 设计 → 审计/分析 → 写作/绘图 → 审稿 → 修改 → 修订核验 → 投稿检查**。

可跳过不适用阶段；简单编辑不建台账。代码实现和实验执行由宿主按项目任务完成。用户决定选题、核心主张变更与超出授权的昂贵实验，已有授权持续有效。

## 证据与限制

区分论文报告、代码观察、测量和推断；关闭问题需修订证据，上游版本变化触发下游复核。私有代码与原始数据默认留在本地，网页委托遵循项目配置。见[公共约定](shared/CONTRACT.md)和[本地操作](shared/LOCAL_OPERATIONS.md)。

完成结构检查及选定合成任务验证。配对样例显示规划、行文和 AI 方法图达到相近可用水平，未证明全面优于原技能。近期改进仅完成结构校验及实施代理自检，不能据此宣称效果提升。SVG 必须逐图渲染验收。没有录用保证或 OpenAI 官方认证。见[评测摘要](docs/EVALUATION.md)、[官方文档对齐](docs/OPENAI_ALIGNMENT.md)。

## 开发与开源

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate_package.py --runtime-only
python scripts/build_release.py
```

构建输出白名单 ZIP、SHA-256 和清单，不包含原始评测轨迹、开发快照、个人配置。请使用整理后的发布文件，不直接上传开发目录。见[发布说明](docs/RELEASE.md)。

欢迎报告技能名、期望行为、去除私人信息的最小输入及实际输出。维护优先解决真实问题，不要求每次全量评测。

新编写内容采用 MIT；原 17 个技能的能力参考与重写关系见[迁移表](provenance/MIGRATION.md)。第三方保留各自权利，未打包原绘图仓库的非商业脚本、图像或字体。请保留 LICENSE、NOTICE 和来源记录。
