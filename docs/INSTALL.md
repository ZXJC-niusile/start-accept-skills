# Installation

English · [中文](INSTALL.zh-CN.md)

Clone and keep the complete repository; individual skills use shared resources. Use an authenticated Codex CLI with plugin support.

## Install

From the cloned repository root:

```sh
codex plugin marketplace add .
codex plugin add start-accept-skills@start-accept-research
codex plugin list --marketplace start-accept-research --json
```

Verify installation in a fresh session. Existing skills remain enabled; select this package explicitly if responsibilities overlap. Historical host checks are recorded in [host acceptance](HOST_ACCEPTANCE.md).

## Update

```sh
git pull --ff-only
codex plugin add start-accept-skills@start-accept-research
codex plugin list --marketplace start-accept-research --json
```

Run from the repository root. Source edits do not automatically refresh the installed cache; verify the installed version and files.

If the marketplace points to an old checkout or archive directory, run `codex plugin marketplace remove start-accept-research`, then repeat installation from this repository. See the [CLI 0.166.0 check](validation/2026-11-02-host.md).

## Remove

```sh
codex plugin remove start-accept-skills@start-accept-research
codex plugin marketplace remove start-accept-research
```

Remove the marketplace only if no longer needed. Research outputs and other skills are unaffected.

## Requirements and direct use

Instruction-only tasks need an agent that can read local files. State scripts require Python 3.10+; developer checks also need `requirements-dev.txt`. Search, rendering and compilation use available host tools.

Without installation, ask the agent to read `<repository>/skills/<skill-name>/SKILL.md`; keep the full repository layout.
