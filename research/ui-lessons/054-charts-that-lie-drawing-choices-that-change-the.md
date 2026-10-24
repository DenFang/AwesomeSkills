---
lesson: 054
kind: video
duration_s: 55
type: ui
category: visual
topic: honest data visualization (baseline, chart type, colour encoding, data-ink, aspect ratio)
sources: frames, voice-over, lesson notes
---

# Charts that lie: drawing choices that change the story

**Hook:** A revenue chart badged "+400%" is really a +4% change; the y-axis simply did not start at zero.

## Main rule
Draw charts so the visual magnitude matches the data magnitude: bar axes start at zero, the chart
type follows the question, colour encodes meaning (one accent for the point, everything else muted),
non-data ink is removed, and line charts are proportioned so the average slope is near 45 degrees.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| Q1 = 104, Q2 = 108 | example revenue bars | 0:00-0:02 on-screen |
| y-axis 100 to 109 (truncated) | the lying version of the revenue chart | 0:00 on-screen |
| y-axis 0 to 110, ticks every 22 | honest version of the same chart | 0:01-0:02 on-screen |
| "+400%" vs "+4%" | badge on the truncated vs zero-based chart (real change 104 to 108 = +3.8%) | 0:00-0:02 on-screen + voice |
| 47% vs 48% | approval rating, Candidate A vs B | 0:03-0:10 on-screen |
| baseline 46% (axis 46-49) | truncated version of the approval chart | 0:03-0:06 on-screen badge |
| baseline 0 (axis 0-60, ticks every 12) | honest version of the approval chart | 0:08-0:10 on-screen badge |
| "2% gap looks like a cliff" | voice example; on screen the gap is 1 point (47 vs 48) | 0:04 voice |
| 0 | bar chart baseline, "no exceptions" | 0:09 on-screen + voice, lesson notes |
| 5 slices | pie charts break past this count | 0:12-0:19 on-screen + voice; page says "~5" |
| 3 roles | colour scale types: categorical, sequential, diverging | 0:23-0:29 on-screen + voice |
| 5 swatches per row | example palette rows | 0:23-0:29 on-screen |
| 1 accent | highlight colour for the one series/bar that matters; rest neutral | 0:22 on-screen + voice |
| 28% to 94% | data-ink meter as chartjunk is removed (28, 28, 30, 40, 50, 60, 69, 79, 89, 94 per second) | 0:30-0:39 on-screen |
| 45 degrees | target average slope of a line chart ("banking to 45°") | 0:46-0:50 on-screen + voice, lesson notes |
| 0 to 80 axis, 6 months | end-card bar chart titled with its takeaway | 0:51-0:54 on-screen |

## Before / after
1. **Truncated baseline.** Bad: revenue bars on an axis starting at 100, so 104 vs 108 is drawn as 4
   vs 8 units and the second bar looks twice as tall. Good: axis starts at 0, both bars look almost
   equal and the badge reads +4%. Why: a bar encodes value by its length; cutting the axis cuts the
   lengths unequally, so the perceived ratio is no longer the data ratio (here the visual change is
   about 26 times the real one).
2. **Truncated baseline, second example.** Bad: approval 47% vs 48% on an axis from 46, reads as a
   landslide. Good: axis from 0 (dashed zero line, "baseline 0" badge), reads as a tie.
3. **Chart type.** Bar = compare values (check), line = change over time (check), pie = fails past 5
   slices (cross). The bad pie has roughly 7-8 slices; a ranking line drawn across it shows that the
   slices cannot be ordered by eye. Why: people judge length and position accurately but angles and
   areas poorly, so small differences between many slices are invisible.
4. **Colour as decoration vs encoding.** Bad: 8 monthly bars each in a different hue, nothing stands
   out and the hues imply categories that do not exist. Good: all bars in one neutral, only the
   month that matters in the accent colour. Why: a single pre-attentive difference (one accent)
   directs attention instantly; many hues compete and suggest false grouping.
5. **Chartjunk.** Bad: line chart tilted in 3D perspective, heavy grid, boxed legend (data-ink 28%).
   Good: flat chart, no grid, legend removed and the series labelled directly at the line end
   (data-ink 94%). Why: every non-data mark costs attention; a direct label removes the eye trip
   between line and legend.
6. **Aspect ratio.** Bad: the same rising series squished wide ("Flat?") or stretched tall
   ("Spike?"). Good: proportions chosen so the line runs near a 45° dashed reference ("Banking to
   45°"). Why: slope perception is most accurate around 45°; extreme ratios exaggerate or hide the
   trend.

## Do
- Start every bar chart's value axis at zero; mark the zero line.
- Pick the chart from the question: compare categories with bars, show change over time with lines.
- Keep pie/donut charts to about 5 slices or fewer; otherwise use a sorted bar chart.
- Choose the colour scale from the data type: categorical for distinct groups, sequential for
  ordered magnitude, diverging for above/below a meaningful midpoint.
- Highlight the one value or series that carries the message with a single accent; render the rest
  in a muted neutral.
- Remove 3D, drop shadows and heavy gridlines; label series directly instead of using a legend.
- Size line charts so the overall slope sits near 45°.
- Title the chart with the takeaway ("Revenue flat since March"), not the metric name.

## Don't
- Don't truncate or crop a bar axis to make small differences look large.
- Don't give every bar its own hue when the bars are the same kind of thing.
- Don't use a pie chart for more than about 5 parts or for precise comparison.
- Don't add 3D tilt, shadows or boxed legends that encode no data.
- Don't stretch or squash a line chart to dramatise or flatten a trend.

## Scene by scene
- 0:00 Bar chart "Quarterly revenue", Q1 104 (neutral) vs Q2 108 (danger colour), axis 100-109, badge "+400% vs last quarter".
- 0:01 Axis animates to 0-110, Q2 turns success/accent colour, badge becomes "+4% vs last quarter".
- 0:02 Headline below: "This chart is lying."
- 0:03 Section "The truncated axis / Landslide? Or a tie.": "Approval rating" 47% vs 48%, axis 46-49, badge "baseline 46%".
- 0:07 Axis rescales to 0-60; dashed zero line; badge switches to "baseline 0"; bars become nearly equal.
- 0:09 Callout card "Bar charts start at zero. No exceptions." with caption "Start every bar axis at zero."
- 0:11 Section "Match the form to the question / Pick the chart for the job."; three cards appear.
- 0:12 Cards: bar "Compare values" (check), line "Change over time" (check), pie "Breaks past 5 slices" (cross, danger colour). Caption "The question picks the chart, not your taste."
- 0:13 Pie fills in slice by slice to roughly 7-8 slices.
- 0:15 A ranking line is drawn across the pie and the slices dim, showing they cannot be ordered.
- 0:20 Section "Color encodes meaning / Color is encoding, not decoration.": 8 bars Jan-Aug, each a different hue.
- 0:22 All bars go neutral except Jul in the accent colour (its axis label also in accent).
- 0:23 Palette rows appear: "Categorical" (accent + neutrals), "Sequential" (one hue, dark to light).
- 0:24 Third row "Diverging" (two opposing hues meeting at a neutral middle); held to 0:29.
- 0:30 Section "Strip everything that isn't data / Kill the chartjunk.", "Data-ink" meter at 28%.
- 0:31 3D-tilted line chart with heavy grid and boxed legend "Revenue" draws in.
- 0:32 Perspective flattens and grid fades as the meter climbs 30, 40, 50, 60, 69%.
- 0:37 Boxed legend fades (79%); 0:38 the label "Revenue" moves to the line end (89%), callout "Data-ink ratio: every pixel is data."; 0:39 94%.
- 0:40 Section "The aspect ratio / Same data. The ratio changes the story.": wide short area chart, badge "Flat?"; 3-step pager dots.
- 0:43 Same data in a tall narrow chart, badge "Spike?".
- 0:46 Chart morphs to balanced proportions in accent colour, badge "Banking to 45°".
- 0:48 Dashed 45° reference line with "45°" label appears next to the series; held to 0:50.
- 0:51 End card: bar chart titled "Revenue flat since March" (Jan-Jun, axis 0-80, March in accent), "Follow for more UI design", "Save this for your next dashboard."

## Voice-over summary
- The opening chart claims a 400% jump but the change is 4%, because the axis did not start at zero; a truncated baseline turns a tiny gap into a cliff.
- Bars start at zero with no exceptions; bars compare values, lines show change over time, pies fail beyond five slices because the eye cannot rank angles.
- Colour is encoding: categorical for groups, sequential for scale, diverging for above/below, one accent for the point and the rest neutral.
- Heavy grids, 3D bars and drop shadows are noise; cites Tufte's data-ink ratio ("Every pixel should be data"); label the line directly and drop the legend.
- Squashing a chart kills the trend, stretching it creates a spike; aim for slopes near 45°, where change reads best.

## Notes for the skill
- Implementation: set the value-axis domain to include 0 for bar/column/area charts (e.g. `domain([0, max])`, `beginAtZero: true`); render a distinct zero line. A line chart (position encoding) may use a non-zero baseline when the variation is the message, but say so with visible tick labels; the video's "no exceptions" rule is correct for bars only.
- The video's numbers are rhetorical: with a 100 baseline the Q2 bar is twice the Q1 bar (+100% visual), not +400%; the voice says "2% gap" while the screen shows a 1-point gap. The principle (visual change must equal data change) is right; Tufte's "lie factor" = visual effect size / data effect size, ideally 1.
- Pie limit "5 slices" is a heuristic (page says ~5). Also sort slices, start at 12 o'clock, and prefer a sorted bar chart for precise comparison. The angle claim is consistent with Cleveland and McGill's ranking of perceptual tasks (position and length beat angle and area).
- Banking to 45° (Cleveland) targets the average absolute slope of line segments; it is a starting point, not a hard rule (multi-scale banking exists for series with mixed frequencies).
- Colour accessibility: never rely on colour alone to carry meaning (WCAG 1.4.1); pair the accent with a direct label or value. Graphical objects needed to read the chart need at least 3:1 contrast against adjacent colours (WCAG 1.4.11); muted bars must still pass that if they carry data. Diverging scales should stay distinguishable for colour-vision deficiencies (avoid a pure red/green pair; vary lightness too).
- Removing the legend works only when every series can be labelled at its end without collisions; with many series, keep a legend or use small multiples.
- Provide a text alternative: an accessible name/description stating the takeaway (`role="img"` + `aria-label`, or `<figure>` + `<figcaption>`) and a data table for exact values.
- Animated axis transitions (as in the video) should respect `prefers-reduced-motion`.
