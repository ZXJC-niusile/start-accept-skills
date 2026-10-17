# 宿主验收 / Host acceptance

Date: 2026-10-17. Package: 0.1.3. Host: Windows, Codex CLI 0.162.1.

| 检查 / Check | 结果 / Result |
|---|---|
| Marketplace registration | Passed: start-accept-research |
| Plugin install and enabled state | Passed: start-accept-skills, version 0.1.3, installed and enabled |
| Installed runtime contents | Passed: 50 skill/shared/script files matched source SHA-256 |
| Fresh-session discovery | Passed: all 11 start-accept-skills names were visible |
| Installed skill invocation | Passed: sa-paper-writing read from installed cache |
| Shared resource resolution | Passed: ../../shared/EVIDENCE.md read from installed skill location |
| Short-edit behavior | Passed: preserved development-pilot uncertainty and held-out limitation |
| Adjacent responsibility boundary | Passed for this request: no scientific-review or revision-check panel invoked |
| Desktop picker refresh | Not directly verified; restart client if needed |
| Implicit selection across all legacy skills | Not assessed; this check explicitly selected the package |

Requested model/effort: gpt-6-astra / high. Server snapshot unavailable. The shell tool failed with `helper_unknown_error: setup refresh had errors`; the same authorized local read succeeded using Node file access. This was not a package-link failure. No research files were edited and no external research was sent.

Input: “Our development pilot suggests that the method may reduce unnecessary revalidation, but this has not been confirmed on held-out repositories.”

Output: “Our development pilot suggests the method may reduce unnecessary revalidation, but this remains unconfirmed on held-out repositories.”

这是一次范围有限的安装与调用检查，不是全部科研能力验收。原始轨迹与本机路径仅保留在开发评测目录，不纳入公开包。This scoped smoke check does not establish all scientific behaviors or desktop UI activation. Raw traces and local paths remain outside the public distribution.
