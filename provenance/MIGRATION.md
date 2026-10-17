# 原技能迁移对照

17 个独立技能均有归属。原目录保留；本表是能力迁移，不表示逐文件复制或替换安装。

| 原 skill | 主要去向 | 处理决定 |
|---|---|---|
| academic-paper-review（deerflow-paper-review） | sa-paper-reading、sa-scientific-review | 拆分理解与正式评审，重写入口 |
| academic-paper-reviewer | sa-scientific-review、sa-revision-check | 合并角色评审与版本核验；固定五人面板改为按需角色 |
| benchmark-paper-template | sa-research-design、sa-paper-writing | 保留构建与测量逻辑，按设计和正文分工 |
| ccf-paper-reviewer | sa-scientific-review、sa-revision-check、sa-submission-check | 拆分科学、版本和形式检查；移除缺失配套技能依赖 |
| experiment-data-analysis | sa-experiment-analysis | 保留比较单位、分母、公平性、统计和主张强度；正式正文交写作 |
| figure-designer | sa-figure-production | 合并设计和制作，按图的表达目标选择实现 |
| humanizer | sa-paper-writing | 吸收准确、简洁与保留作者风格的原则，避免全局机械禁词 |
| idea-evaluator | sa-topic-selection | 保留新颖性与可行性审视，不作无证据录用预测 |
| intro-drafter | sa-paper-writing | 保留论证链与贡献对应，段落数不硬编码 |
| investigate-codebase | sa-code-audit | 保留证据定位、薄路径追踪与验证边界，重写精简流程 |
| let-accept-review | sa-scientific-review、sa-revision-check、sa-submission-check | 保留证据/台账/版本；作者自有材料不强制额外 intake 表 |
| paperjury | sa-paper-writing、sa-scientific-review、sa-revision-check | 拆分编辑和对抗检查；不复制自动补丁、更新器及整套循环引擎 |
| peer-review | sa-scientific-review、sa-experiment-analysis、sa-submission-check | 保留方法统计与引用核查，首版不纳入医学报告规范 |
| pre-submission-reviewer | sa-submission-check | 保留投稿检查维度，形式偏好不升级为科学缺陷 |
| scientific-figure-making | sa-figure-production | 吸收导出与视觉核验目标；不复制非商业代码、字体和样例资产 |
| tech-paper-template | sa-research-design、sa-paper-writing | 分开研究结构与文章结构，适配方法/系统/理论 |
| vibe-research-workflow | sa-workflow | 保留阶段组织和人类关键决策；删除泛化拒绝起草、固定工具推荐和生产率承诺 |

科学审稿仅评价与提出问题；写作和绘图分别负责修改。实验执行与代码实现交宿主任务，不在此包增加同名近似技能。

`figures4papers` 指向 `scientific-figure-making`，只记录一个来源。分组记录保存实际读取的原文件哈希，用于区分历史能力和新实现。
