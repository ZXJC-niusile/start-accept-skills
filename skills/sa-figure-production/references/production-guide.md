# Figure production guide

## Choose by evidence and output

| Need | Useful approach | Required source |
|---|---|---|
| Magnitude across categories | Dot plot or bars; intervals if defined | Tidy input data plus plotting script |
| Ordered trend | Lines or points with explicit sampling | Input series and transformation code |
| Trade-off / association | Scatter, units and relevant reference | Paired measurements and plot source |
| Matrix or distribution | Heatmap, histogram, ECDF or suitable distribution plot | Cell/bin definitions and underlying observations |
| Architecture / algorithm | Vector diagram with named states and edges | SVG/TikZ/diagram source or editable drawing file |
| Motivation example | Small labeled example with observed failure or clearly hypothetical behavior | Example provenance and editable composition |
| Theory | Geometric sketch, dependency diagram or boundary plot | Definitions; schematic status if not exact |

Select what exposes the comparison clearly; these are options, not mandatory chart rules. Interactive exploratory charts are acceptable when requested, but publication deliverables still need a stable export. Use existing installed tools first. Name unavailable dependencies rather than claiming the output exists.

## Honest encodings

Show units, populations, sample counts and uncertainty definitions where relevant. Bar length ordinarily needs a zero baseline; disclose justified breaks or use points for narrow comparisons. Log axes must be visibly labeled and cannot silently drop nonpositive values. Disclose smoothing, binning, normalization, clipping and omitted data. Keep color mappings consistent across panels, and add shape/line/pattern cues so color is not the only distinction.

Do not hard-code guessed paper numbers or draw significance markers without statistical evidence. A schematic arrow means an explicit conceptual relationship, not a verified causal effect. Qualitative visual improvement does not prove better measured performance.

## Export and visual QA

Set the canvas for its final column or page width, then choose readable text at that size. Use an available font with fallbacks and check its actual rendered glyphs. Vector output should preserve editable geometry/text where practical; embedded raster panels remain raster even inside a PDF. Use the venue's verified resolution requirement or a declared practical default such as a 300-DPI preview.

Inspect the actual exported file or its rendered preview: no cut-off labels, illegible text, overlapping legends, misleading scales, unexplained abbreviations or swapped panels. Check grayscale or alternate encodings where meaningful. Compare plotted coordinates and labels to the source values independently of visual style. Record which checks were numeric, visual or not run.

Track editable source, exports, AI-generated images and rendered previews separately, with the exact file/version inspected. A valid SVG or an HTML wrapper does not prove rendering; inspecting an independently generated PNG does not validate the SVG. Report actual pixel dimensions and intended placement size rather than copying requested dimensions as achieved.

If rendering fails, diagnose the concrete error. Make a focused retry when it addresses that error, or use a known available compatible renderer; do not keep trying unavailable libraries or repeat an unchanged failing command. If no viable renderer is available, stop rendering attempts, retain the source and error, and identify the remaining visual check. Installing dependencies or switching external generation services requires the applicable project authorization. Resume when new evidence makes rendering feasible.
