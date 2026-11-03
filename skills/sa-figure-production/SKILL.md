---
name: sa-figure-production
description: Design, create or repair publication figures for computer-science research, including motivation examples, method diagrams and data plots. Deliver editable sources and verified exports. Use for figure layout and visual audits; numerical claim analysis and manuscript-only edits belong to other skills.
---

# Figure production

Make the requested research figure and verify what the rendered artifact communicates. Follow the [shared contract](../../shared/CONTRACT.md). Use the [production guide](references/production-guide.md) for tool choice and visual checks.

## Work

1. Identify the figure's question, target dimensions, medium and actual inputs. Inspect an existing figure before judging or editing its appearance. Distinguish a conceptual illustration from a measured result; label synthetic demonstrations explicitly.
2. Bind data to source versions, units, metric direction, comparison population and uncertainty definitions. Check figure numbers against the supplied table. If a conflict or missing result changes the claim, ask [experiment analysis](../sa-experiment-analysis/SKILL.md) to resolve it. Never fill missing cells, fabricate error bars or choose an axis to hide an unfavorable result.
3. Select the smallest design that answers the question. Use a concrete example for motivation, explicit components and labeled connections for architecture, and a suitable chart for the measurement type.
4. Produce editable source with an appropriate available tool. Data plots normally use a short reproducible plotting script; diagrams may use SVG, TikZ, Mermaid or available drawing tools. Prefer existing project conventions. For requested raster generation/editing, follow the host's image-generation policy and preserve editable layout/source for the larger figure. Do not treat a generated scientific chart as measured evidence.
5. Export suitable vector files for text/lines and a preview image; use adequate raster resolution for raster content. Preserve data references, generation command and relevant tool versions so the result can be regenerated.
6. Render and inspect at intended publication size. Check clipping, fonts, line weights, labels, legends, reading order, panel agreement and accessibility. Fix visible issues, then check the revised rendering. If rendering is unavailable, use the bounded recovery in the production guide and deliver source with visual checks explicitly unverified. A separately AI-generated image is not a render of the editable source.

## Finish

Return source, exports, preview and a brief figure specification with data provenance, transformations, draft caption and verified/unverified checks. The draft caption is figure metadata; [paper writing](../sa-paper-writing/SKILL.md) owns manuscript integration and prose revision. Design-only requests may stop at a concrete layout and caption with production still pending. Use [figure record](templates/figure-record.md) for multi-stage work.
