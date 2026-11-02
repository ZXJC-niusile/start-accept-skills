# Sources and license handling

This package was developed from the user's approved functional specification and
an audit of the local research skill collection. On 2026-10-07, the maintainer
selected the MIT License for this project's newly authored instructions,
documentation, fixtures and scripts. See [LICENSE](LICENSE). The copyright notice
uses the collective project attribution "start-accept-skills contributors".

This grant does not relicense third-party source material. Original rights and
any applicable attribution requirements remain. The source audits below predate
the MIT decision; statements that they do not grant a package-wide license
describe those historical audits, not the current license of our new work.

See provenance/sources.json and the group provenance records for source names,
paths, hashes, declared licenses and retained/reworked/excluded capabilities.
These records describe provenance, not a legal determination of license scope.

Here, "provenance" means which earlier skills informed which capabilities,
which parts were rewritten or excluded, and which source versions and license
declarations were observed. It does not refer to users' papers or research data.
Known upstream authors and links are retained; missing upstream identity remains
explicitly unknown rather than invented.

Known source declarations include CC-BY-4.0 on several research-planning skills,
MIT on paperjury, peer-review and let-accept-review, and CC-BY-NC-4.0 in the
scientific-figure-making LICENSE. humanizer includes a separate upstream MIT
notice. Some sources lack a package-level license. We did not vendor plotting
code, images, template assets, source validators or scripts from those packages.
New instructions, fixtures and scripts are written for this package. Do not copy
additional third-party resources into a distributable build without recording
their source and retaining the relevant notices.

Official design references consulted:
- https://developers.openai.com/blog/eval-skills
- https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra
- https://developers.openai.com/api/docs/guides/tools-skills
- https://developers.openai.com/plugins/build/skills
- https://developers.openai.com/plugins/build/plugins

The first four guided evaluation, description scope, progressive disclosure and
workflow/tool boundaries; the last specified the portable package layout. Their
examples are not vendored as implementation. Source availability and product
integration can change; validate installation against the target host.
