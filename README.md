# start-accept-skills

中文 · [English](README.en.md)

面向计算机科研的 11 个技能，覆盖文献阅读、研究设计、写作、审稿和项目衔接。可以从任意阶段开始。

## 安装

使用已登录且支持插件的 Codex CLI：

```sh
git clone https://github.com/ZXJC-niusile/start-accept-skills.git
cd start-accept-skills
codex plugin marketplace add .
codex plugin add start-accept-skills@start-accept-research
```

保留完整仓库，技能依赖共享资源。更新和卸载见[安装指南](docs/INSTALL.md)。

## 使用

在请求中指定技能，附上材料和目标，例如：

- `用 sa-paper-reading 精读这篇论文，解释方法和证据。`
- `用 sa-paper-writing 压缩这一段，保留数字、引用和必要限定。`
- `用 sa-revision-check 核对这些审稿意见是否已解决。`
- `用 sa-workflow 根据现有材料继续这个研究项目。`

默认中文沟通，论文语言遵循稿件要求。单项任务直接使用对应技能；只有跨阶段工作才需要流程协调和状态记录。

| 技能 | 用途 |
|---|---|
| sa-workflow | 协调阶段、恢复项目、交接产物 |
| sa-paper-reading | 检索、精读和比较文献 |
| sa-topic-selection | 比较研究方向、新颖性和可行性 |
| sa-research-design | 设计基线、指标、数据划分和消融 |
| sa-code-audit | 检查代码实现与研究主张 |
| sa-experiment-analysis | 分析实验、比较结果、判断结论范围 |
| sa-paper-writing | 起草、修改、翻译和润色正文 |
| sa-figure-production | 制作科研图及可编辑图源 |
| sa-scientific-review | 评审贡献、方法和证据 |
| sa-revision-check | 核验修改、追踪问题和回归 |
| sa-submission-check | 检查语言、格式、引用和投稿要求 |

检索、绘图和编译使用宿主已有工具。状态脚本需要 Python 3.10+，操作见[本地操作](shared/LOCAL_OPERATIONS.md)。

## 开发

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate_package.py
```

通过 Git 仓库分发和更新，不再提供独立 ZIP 发布包。结构校验不代表科研结论正确或模型效果提升，已有验证范围见[评测记录](docs/EVALUATION.md)。

[维护记录](docs/RELEASE.md) · [MIT 许可](LICENSE) · [第三方来源](NOTICE.md)
