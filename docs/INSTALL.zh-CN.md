# 安装

[English](INSTALL.md) · 中文

保留完整仓库，单个技能依赖共享资源。使用已登录且支持插件的 Codex CLI。

## 安装

在克隆后的仓库根目录执行：

```sh
codex plugin marketplace add .
codex plugin add start-accept-skills@start-accept-research
codex plugin list --marketplace start-accept-research --json
```

在新会话中核对技能是否可用。已有技能不会停用，职责重叠时可显式选择本包技能。历史实测见[宿主验收](HOST_ACCEPTANCE.md)。

## 更新

```sh
git pull --ff-only
codex plugin add start-accept-skills@start-accept-research
codex plugin list --marketplace start-accept-research --json
```

从仓库根目录执行。源码更新不会自动刷新安装缓存，应核对已安装的版本和文件。

## 卸载

```sh
codex plugin remove start-accept-skills@start-accept-research
codex plugin marketplace remove start-accept-research
```

不再需要此 marketplace 时才执行第二条。卸载不删除研究产物或其他技能。

## 环境与直接读取

纯指令任务只需能读取本地文件的代理。状态脚本需要 Python 3.10+；开发检查还需安装 `requirements-dev.txt`。检索、渲染和编译使用宿主已有工具。

不安装也可请求代理读取 `<仓库目录>/skills/<技能名>/SKILL.md`，同时保留完整仓库布局。
