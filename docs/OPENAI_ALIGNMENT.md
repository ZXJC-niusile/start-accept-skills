# OpenAI 四篇文档核对

核对日期：2026-10-06；本地版本：0.1.2。以下是基于官方页面与包内文件的维护者评估，不是认证、兼容性承诺或无缺陷保证。

| 官方文档 | 本包对应实现 | 判断与边界 |
|---|---|---|
| [Testing Agent Skills Systematically with Evals](https://developers.openai.com/blog/eval-skills) | 有任务输入、真实轨迹/产物、独立分工评分与效率记录；结构检查、语义评分分别报告，保留失败 | 遵循评测方法。按用户要求减少运行规模不违背少量关键检查的建议；结果不足以证明广泛泛化或所有版本无回归 |
| [Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) | 聚焦描述；公共原则 228 个空白分词；详细证据/交接/台账按需加载；无固定审稿人数或段落数；短编辑直接完成；维护检查按变更选择 | 主要设计建议已落实。词数不是 token 节省证明，少量配对观察也不等于全流程更快 |
| [Skills — API guide](https://developers.openai.com/api/docs/guides/tools-skills) | 每个技能具有 name/description 与 SKILL.md，资源可追溯；默认无网络服务或外传动作 | 通用技能组织原则适用。Responses API 的单技能上传、skill_id 和版本管理没有实现，也未做 API 集成验证 |
| [Build skills — Plugins](https://developers.openai.com/plugins/build/skills) | 1 个协调入口与 10 个功能技能；各自有输入、产物、边界和按需资源；用户明确要求优先于技能默认流程 | 技能编写原则已落实。采用无 MCP 的文件插件；安装发现与旧技能共存仍待目标宿主检查 |

## 特别说明

- 第二篇建议减少不必要的指令，不能推导为删除证据真实性、权限或关键状态不变量。确定性校验放在脚本中，技能入口没有因此持续膨胀。
- 这些页面没有统一规定评测必须使用某一推理档位。历史 Astra High 是本项目明确选择并记录的配置。
- 便携根 `plugin.json` **不需要** `skills` 字段：官方[打包说明](https://developers.openai.com/plugins/build/plugins)明确从根 `skills/` 发现技能。技能页面中的 `skills: "./skills/"` 示例与兼容布局不能机械套用到便携清单。
- Responses API 的单技能 bundle 只允许一个 SKILL.md。本包包含 11 个，并使用共享资源和技能间交接，不能把整个插件 ZIP 当成单技能直接上传。迁移到该接口需要单独设计资源封装和交接，不在当前发布范围。

## 剩余问题并非都只能在使用中发现

安装与相对资源解析、许可和来源署名、发布内容泄露检查可在发布前完成。模型在真实长流程中的漂移、特殊论文/工具组合和跨模型表现，需要有范围的试用逐步验证。当前没有证据证明不存在未知缺陷。
