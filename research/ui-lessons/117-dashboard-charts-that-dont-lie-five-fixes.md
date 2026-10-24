---
lesson: 117
kind: video
duration_s: 53
type: ui
category: visual
topic: Honest dashboard charts: zero baseline, one accent, direct labels, table past 5 series, annotations
sources: frames, voice-over
---

# Dashboard charts that don't lie: five fixes

**Hook:** This chart lies: bars starting at 90 make a small gain look several times bigger.

## Main rule
Start bar-chart axes at zero, reserve one accent colour for the series that matters and mute the rest, label lines directly at their ends instead of a legend, switch to a sortable table (or small multiples) once a chart has more than five series, and annotate outliers with their cause on the chart itself.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 925 vs 1,000 | last week vs this week signups (intro demo) | 0:00-0:02 |
| y from 900, "truncated axis", badge +300% | bars look 4x different (perceived +300%) | 0:00-0:01 |
| y from 17 (axis 17/263/509/754/1,000) | intermediate frame while the axis animates down | 0:01 |
| y from 0, "honest axis", badge +13% | corrected bars; note: 925 -> 1,000 is actually +8.1%, so the on-screen +13% is wrong (the dashboard KPI card in the same video shows "1,000 +8%") | 0:02 |
| axis 90 to 100, "starts at 90" | weekly signups bar chart W1-W8, truncated | 0:03-0:10 |
| W8 / W3 = 4x | apparent ratio with truncated axis | 0:05-0:10 |
| W8 / W3 = 1.08x | real ratio with zero baseline (axis 0/33/67/100, "starts at 0") | 0:11-0:12 |
| "line charts: may skip zero, label it" | exception for line charts | 0:04-0:12 |
| Signups 1,000 +8%, Activation 41% +2 pts, Trials 312 +5% | dashboard KPI cards (context) | 0:03-0:12 |
| 5 plans, 5 colours ("rainbow") | revenue by plan line chart: Free, Starter, Pro, Team, Enterprise; axis $0k-$40k, Nov-Oct | 0:13-0:17 |
| 1 accent + grey | Pro line in accent, other 4 muted | 0:18-0:20 |
| trips: 5 -> trips: 0 | legend look-ups needed vs direct labels at line ends | 0:22-0:27 |
| 12 series, "readable up to 5" | usage by customer spaghetti chart | 0:28-0:35 + voice ("passes five series") |
| sortable table columns Customer / Usage / Trend (sparkline) / Change (sorted desc, +41% ... -9%) | replacement for >5 series; "or small multiples" alternative | 0:35-0:36 |
| 409 / 412 on Tue, axis 0/160/320/480 | daily signups spike | 0:37-0:41 |
| Comments 3 open -> 0 open, "Answered on the chart, 0 questions" | effect of annotation "Launch day, Product Hunt" | 0:38-0:45 |

## Before / after
- **Baseline.** Before: bars start at 90 (or 900); W8 looks 4x W3 and the gain looks like +300%. After: axis from 0; W8/W3 is 1.08x. Why: bars encode value by length; a truncated axis cuts off a shared chunk of every bar, so length ratios no longer match value ratios. Line charts encode position/slope, so they may start above zero if the axis is clearly labelled.
- **Colour.** Before: five plans in five saturated colours ("rainbow"), nothing stands out. After: the Pro plan in the single accent colour, others muted grey, so the eye lands there. Why: pre-attentive pop-out works only when one element differs; equal salience across all series means no hierarchy.
- **Legend vs direct labels.** Before: legend box below the chart; identifying a line costs an eye trip down to the legend and back (trips: 5). After: each series name at the right end of its line (trips: 0). Why: removes colour-matching and back-and-forth eye movement (working memory load); also works without relying on colour.
- **Too many series.** Before: 12 customer lines overlaid ("12 lines, 0 answers"). After: a sortable table with usage, a sparkline trend and change %, sorted by change; or small multiples. Why: beyond about five series lines overlap and colours become indistinguishable; a table supports lookup and ranking, which is what the question actually is.
- **Outliers.** Before: Tuesday spike (412) with three open comments guessing why ("why the jump on Tuesday?", "bot traffic maybe?", "tracking bug again?"). After: an annotation on the peak "Launch day, Product Hunt" and the spike bar in the accent; comments 0 open. Why: context at the point of attention prevents misreading and repeated questions.

## Do
- Start bar and area chart value axes at 0.
- If a line chart's axis does not start at 0, label the axis range clearly.
- Use one accent colour for the focus series; render others in a muted neutral.
- Put series labels at the end of each line (direct labelling).
- Cap line charts at about 5 series; above that, use a sortable table with sparklines or small multiples.
- Annotate spikes, dips and discontinuities with a short cause label on the chart.

## Don't
- Don't truncate the bar-chart axis to make changes look dramatic.
- Don't give every series its own saturated colour by default.
- Don't rely on a separate legend box when direct labels fit.
- Don't overlay a dozen lines and expect a readable answer.
- Don't leave obvious outliers unexplained.

## Scene by scene
- 0:00 "Pulseboard weekly signups: This chart lies." Two bars 925 vs 1,000 with "y from 900, truncated axis" and a +300% badge in danger colour; axis animates to "y from 0, honest axis", badge changes to +13%. Progress stepper: 1 zero, 2 accent, 3 labels, 4 table, 5 notes.
- 0:03 "Fix 01, Baseline: Bars that start at 90." Dashboard with KPI cards and W1-W8 bars on a 90-100 axis, chip "starts at 90", ratio chip "W8 / W3 4x", note "line charts: may skip zero, label it".
- 0:11 "Bars start at zero": axis 0-100, chip "starts at 0", ratio "W8 / W3 1.08x", W8 bar in accent.
- 0:13 "Fix 02, One accent: Five plans, five colors." Revenue by plan, 5 coloured lines with legend, chip "rainbow".
- 0:18 "Pro teal, the rest grey": Pro line thickens in the accent, other lines turn grey; a highlight circle on the Pro line.
- 0:21 "Fix 03, Direct labels: Every line costs a trip." Legend moved below the chart, chip "trips: 5", a dotted path animates from a line end down to the legend item.
- 0:27 "Name the line where it ends": labels Pro, Enterprise, Team, Starter, Free at line ends, legend removed, "trips: 0".
- 0:28 "Fix 04, Past 5 series: 12 lines, 0 answers." Usage by customer, 12 grey lines drawn in; chips "12 series", "readable up to 5", "or small multiples" with four mini sparklines.
- 0:36 "Switch to a sortable table": Customer / Usage / Trend / Change table, cursor sorts by Change, rows reorder.
- 0:37 "Fix 05, Annotate: A spike nobody explains." Daily signups Mon-Sun, Tuesday spikes to 409 then 412; comment list "Comments 3 open" with three guesses.
- 0:42 "Put the reason on the peak": callout "Launch day, Product Hunt" connected to the Tuesday bar (now accent); "Comments 0 open", "Answered on the chart, 0 questions"; stepper shows "5 fixes".

## Voice-over summary
- Sign-up bars that start at 90 make a small gain look about three times bigger.
- Bars are compared by length, so the axis must go to zero, which shrinks the gap to its true size.
- Five plans in five bright colours means nothing stands out; colour only the Pro plan and grey the rest so the eye lands there.
- A legend box makes every line cost a trip down and back, so names move to the end of each line.
- Twelve customers on one chart become spaghetti; past five series, switch to a sortable table.
- A note on the Tuesday peak ("launch day") stops the team from guessing. Ends with a product plug.

## Notes for the skill
- On-screen error: the intro's "honest" badge says +13%, but 925 to 1,000 is +8.1% (the video's own KPI card shows +8%). Use the correct arithmetic in any example; the "+300%" is the perceived change from bar lengths (25 vs 100 units above 900), not a real figure.
- The voice says the gain "looks three times bigger" while the chip says 4x for W8/W3; both describe the distortion loosely. The rule (zero baseline for bars) holds regardless.
- Accent colour: the highlighted series must still meet non-text contrast of at least 3:1 against the chart background (WCAG 1.4.11), and muted series should remain distinguishable from the background. Do not encode the focus series by colour alone; also use thicker stroke (as shown) and a direct label.
- Direct labels: avoid label collisions at line ends (nudge vertically, or fall back to an interactive legend); keep labels in the series colour or neutral text with a colour swatch.
- Five-series limit is a guideline consistent with common data-viz practice (categorical palettes beyond about 5-7 hues become hard to distinguish), not a hard standard.
- Tables replacing charts: make columns sortable with `aria-sort` on the active header and keep the sparkline decorative (`aria-hidden`) with the numeric change as text.
- Annotations should be real text (not baked into an image) so screen readers and search pick them up; provide a text alternative or data table for the chart as a whole.
- Final segment is a product advertisement; no UI rule there.
