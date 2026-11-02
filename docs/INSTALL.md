# 安装 / Installation

安装完整插件，不能拆开安装单个技能。Install the complete plugin; individual skill folders depend on shared resources.

通过 Git 克隆仓库安装和更新。Clone the Git repository to install and update.

## Codex CLI

克隆后在仓库根目录执行 / Run from the cloned repository root:

```sh
codex plugin marketplace add .
codex plugin add start-accept-skills@start-accept-research
codex plugin list --marketplace start-accept-research --json
```

需要已登录且支持这些命令的 CLI。Requires an authenticated CLI supporting these commands. The bundled catalog uses source path `./`, relative to the marketplace root.

安装后下一轮可用；桌面未刷新时重新启动。Installed skills are available on the next turn; restart the desktop client if needed. Select the names shown by the skill picker. Existing legacy skills remain installed; explicit selection helps avoid overlap.

## 更新 / Update

在仓库根目录运行 `git pull --ff-only`，再重新执行安装命令并用 list 核对。更新源码不会自动更新安装缓存。Run `git pull --ff-only` from the repository root, repeat the install command and inspect the listed version. Updating source files does not automatically refresh the installed cache.

## 卸载 / Uninstall

```sh
codex plugin remove start-accept-skills@start-accept-research
codex plugin marketplace remove start-accept-research
```

第二条仅在不再需要此 marketplace 时运行。Run the second command only when the marketplace is no longer needed. This does not remove your research outputs or other installed skills.

## 直接读取 / Direct file use

不安装也可请求代理读取 `<package>/skills/sa-paper-writing/SKILL.md` 等入口，保留整个包。Without installation, ask the agent to read the desired SKILL.md and retain the complete package layout.

## 环境 / Requirements

Instruction-only work needs a local-file-capable agent. State scripts use Python 3.10+ and the standard library. Developer validation requires requirements-dev.txt. Rendering, search and image generation depend on available host tools. This is not a single-skill Responses API upload bundle.

流程依据 / Official reference: [Plugin packaging](https://developers.openai.com/plugins/build/plugins). Actual verification is recorded separately in [host acceptance](HOST_ACCEPTANCE.md); CLI checks do not prove desktop UI discovery.
