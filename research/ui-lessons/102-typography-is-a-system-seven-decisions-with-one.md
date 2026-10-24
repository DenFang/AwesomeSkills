---
lesson: 102
kind: video
duration_s: 85
type: ui
category: visual
topic: typography system (scale, inks, weights, leading, tracking, measure, tabular figures)
sources: frames, voice-over
---

# Typography is a system: seven decisions with one font

**Hook:** Same font, two results: seven typographic decisions separate a product-looking screen from a form-looking one.

## Main rule
Make seven typography decisions explicitly and apply them as tokens: at most five sizes from one ratio (1.25), three text inks (primary, secondary, muted) instead of extra sizes, two weights (400 and 600), line height that falls as size rises (1.5 body, 1.1 headings), negative tracking on large type and positive tracking on small uppercase labels, a capped reading measure (45-75 characters), and tabular figures for any changing or aligned numbers.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 7 decisions | Sizes, Colors, Weights, Leading, Tracking, Measure, Tabular | 0:02 inspector "7 decisions", 1:08 summary + voice |
| 11 sizes → 5 · 1 grey → 3 · bold → 2 | before/after summary of the billing screen | 0:00-0:04 on-screen chip (counts down 11 → 10 → 6 → 5) |
| 11, 12, 13, 14, 15, 16, 18, 20, 22, 24, 28 px | the 11 hand-picked sizes before | 0:05-0:07 on-screen size list |
| 13, 16, 20, 25, 32 px with "× 1.25" between steps | the 5-size modular scale after; "1 ratio · 5 sizes · 0 hand-picked" | 0:08-0:12 on-screen + voice ("one ratio, 1.25") |
| 32/600/primary, 25/600/primary, 16/600/primary, 16/400/secondary, 13/400/secondary, 13/600/muted | inspector roles (size / weight / ink) on the billing screen | 0:02-0:04 on-screen |
| primary, secondary, muted | three text inks: amount ("the thing you scan for"), invoice id ("still readable"), date ("present but quiet") | 0:15-0:21 on-screen + voice |
| "Same size on all four cells. Only the ink changed." | invoice row ORB-2044 / Sep 12 / $712.00 / Paid | 0:17-0:21 on-screen |
| 700 → 400 · 600 | weights: stat cards drop from 700 to the 400/600 pair; "2 kept" of the family weights 300-800 | 0:22-0:30 on-screen + voice ("400 and 600") |
| line-height 1.4 → 1.10 (heading 32) and 1.4 → 1.50 (body 16) | leading; "1.4 everywhere" crossed out | 0:31-0:38 on-screen + voice |
| 13 → 1.50, 16 → 1.50, 20 → 1.35, 25 → 1.20, 32 → 1.10 | line height per scale step ("size up → leading down") | 0:36-0:38 on-screen bar chart |
| −0.02em above 24 px | letter-spacing on page title 32 px | 0:41-0:47 on-screen + voice ("minus 2%") |
| 0 for body 16 | body tracking "stays at 0"; "tracking is for the extremes, not for reading sizes" | 0:40-0:47 on-screen |
| +0.05em below 16 px, uppercase | letter-spacing on 13 px uppercase labels ("CURRENT PLAN"); "Caps have no ascenders to separate them. Tracking does it." | 0:45-0:47 on-screen + voice ("plus 5%") |
| 45 to 75 characters per line | comfort band for body text | 0:48-0:57 on-screen + voice |
| container 1400 px; 166 → 78 → 66 characters; measure 66ch; 3 lines | paragraph measure capped while the container stays 1400 px | 0:48-0:57 on-screen slider (scale ticks 30, 45, 66, 75, 150) |
| `font-variant-numeric: tabular-nums;` vs `proportional-nums` | invoice amounts and a ticking counter 1,284,905 → 1,285,220 | 0:58-1:07 on-screen + voice; "shifts on every tick" vs "0 wobble" |

## Before / after
- **11 hand-picked sizes → 5 from a ratio.** Bad: sizes like 11, 12, 14, 15, 18, 22, 24, 28 each chosen ad hoc; neighbouring steps are too close to read as different levels. Good: 13 / 16 / 20 / 25 / 32, each step ×1.25. Why: a consistent ratio makes each step visibly distinct, so size alone signals hierarchy, and fewer sizes means fewer decisions per component.
- **One grey + more sizes → three inks at one size.** Bad: hierarchy inside a row is created by changing size. Good: all four cells in an invoice row share one size; only the ink differs (amount primary, invoice id secondary, date muted). Rule shown: colour ranks inside a line, size ranks between blocks. Why: varying size within a row breaks the baseline and row rhythm; ink contrast ranks importance without layout cost.
- **700 everywhere → 400 and 600.** Bad: stat values and labels at 700, so nothing stands out ("when everything is bold, nothing is"). Good: Regular 400 for reading, Semibold 600 for scanning (numbers, headings). Why: emphasis only works relative to a calmer baseline; two weights also load fewer font files.
- **1.4 everywhere → leading against size.** Bad: one line-height for all sizes (called an AI tell); 1.4 is too loose on a 32 px heading and slightly tight on body. Good: 1.10 on the 32 px heading, 1.50 on 16 px body, graded steps between. Why: large type has big absolute gaps even at low ratios, so headings need tighter leading to read as one block; small text needs more to keep lines trackable.
- **Default tracking → extremes adjusted.** Good: −0.02em on the 32 px title, 0 on body, +0.05em on 13 px uppercase labels. Why: large glyphs look loosely spaced at default tracking; uppercase lacks ascenders and descenders, so letters crowd at small sizes unless opened up.
- **Full-width paragraph → capped measure.** Bad: a paragraph spanning the 1400 px container runs to about 166 characters per line, unreadable. Good: cap the paragraph at about 66ch (3 lines) while the container stays full width. Why: very long lines make the return sweep to the next line error-prone.
- **Proportional → tabular figures.** Bad: proportional digits make the amount column misalign and a live counter jitter "on every tick". Good: `tabular-nums` gives equal-width digits, columns align and updating numbers stay still ("0 wobble").

## Do
- Define a type scale from one ratio (1.25 shown) with five steps (13/16/20/25/32 px) and use only those.
- Define three text colour roles: primary, secondary, muted; vary ink, not size, inside a line.
- Use two weights: 400 for running text, 600 for headings, numbers and anything users scan.
- Set line height per size step: about 1.5 for 13-16 px, decreasing to about 1.1 at 32 px.
- Apply −0.02em letter-spacing to text above 24 px and +0.05em to uppercase labels below 16 px; leave body text at 0.
- Cap paragraph width with `max-width` in `ch` (about 66ch), not by shrinking the layout container.
- Use `font-variant-numeric: tabular-nums` on tables, prices, timers, counters and stats.

## Don't
- Don't hand-pick sizes per component or keep 10+ font sizes.
- Don't use one line-height value for every size.
- Don't bold everything; don't use 700 as the default emphasis next to 400 and 600.
- Don't track body text; tracking is for very large or very small uppercase text.
- Don't let body text run the full width of a wide container.
- Don't render aligned or live-updating numbers with proportional figures.

## Scene by scene
- 0:00 Tag "TYPOGRAPHY IS A SYSTEM · 01", "Typography is a system." A billing screen ("Orbit", "Usage & billing", current plan "Scale", stat cards API calls 1,284,905 / Spend $4,312.40 / Seats 24, an invoices table, a paragraph). An "INSPECTOR · 7 decisions" panel fills with size/weight/ink labels, family "Inter, one family, no swap" and a 5-step scale. Chip "11 sizes → 5 · 1 grey → 3 · bold → 2".
- 0:05 "02 Five sizes, one ratio.": a column of 11 size swatches (11-28) collapses to 13, 16, 20, 25, 32 joined by "× 1.25" markers; size bar "5 left"; chip "1 ratio · 5 sizes · 0 hand-picked".
- 0:13 "03 Three inks, not ten sizes.": zoomed invoice row ORB-2044, Sep 12, $712.00, Paid; three ink swatches primary / secondary / muted with their roles; "Same size on all four cells. Only the ink changed."; inspector "16 / 700 / primary", "16 / 700 / secondary"; chip "color ranks in a line · size ranks between blocks".
- 0:22 "04 Two weights, 400 and 600.": stat cards with "700 → 400 · 600"; specimen cards Aa 400 Regular ("reads") and Aa 600 Semibold ("scans"); family weights row 300-800 reduced to "2 kept"; chip "400 reads · 600 scans".
- 0:31 "05 Leading moves against size.": Heading 32 and Body 16 cards with line-height brackets animating 1.40 → 1.10 and 1.40 → 1.50; bar chart of the five sizes with leading 1.50 / 1.50 / 1.35 / 1.20 / 1.10; "1.4 everywhere" crossed out, "1.1 heading", "1.5 body"; chip "size up → leading down".
- 0:39 "06 Big tightens, small caps open.": page title 32 (above 24 px) tracking 0 → −0.02em; body 16 "stays at 0"; label 13 uppercase (below 16 px) 0 → +0.05em; chip "big → tight · small caps → open".
- 0:48 "07 Cap the measure, not the box.": browser 1400 × 900 with "container 1400 px"; a one-line paragraph at 166 characters; a slider drags from 150+ to 66, the paragraph wraps to 3 lines under "measure 66ch"; chips "container · 1400 px", "measure · 66ch", "comfort band · 45 to 75"; footer "45 to 75 chars per line".
- 0:58 "08 Tabular figures, one property.": `font-variant-numeric: proportional-nums;` (marked wrong) over a misaligned invoices table, then typed `tabular-nums;` (marked right) and the amount column aligns; two counters ticking (proportional "shifts on every tick" vs tabular "0 wobble"); chip "tabular-nums · 0 wobble".
- 1:08 "09 Seven decisions. One font.": list 01 Sizes, 02 Colors, 03 Weights, 04 Leading, 05 Tracking, 06 Measure, 07 Tabular above the finished billing header.

## Voice-over summary
- Typography is a system: same font, seven decisions separate a product from a form.
- Five sizes maximum from one ratio, 1.25, never hand-picked pixels; three text colours do more than ten sizes; colour ranks inside a line, size between blocks.
- Two weights, 400 and 600: "When everything is bold, nothing is."; regular for reading, semibold for scanning.
- Line height moves opposite to size, 1.1 on headings and 1.5 on body; one value everywhere is an AI tell. Tracking tightens 2% above 24 px and small uppercase labels open by 5%.
- Body text stays between 45 and 75 characters per line; cap the measure, not the container. Tabular figures for numbers in tables, prices and timers, otherwise columns wobble.

## Notes for the skill
- CSS sketch: `--text-xs:13px; --text-sm:16px; --text-md:20px; --text-lg:25px; --text-xl:32px;` (13 × 1.25ⁿ rounded); `--lh-13:1.5; --lh-16:1.5; --lh-20:1.35; --lh-25:1.2; --lh-32:1.1;`; `.display{letter-spacing:-0.02em}`; `.label{text-transform:uppercase;font-size:13px;letter-spacing:0.05em}`; `.prose{max-width:66ch}`; `.num, table td.amount{font-variant-numeric:tabular-nums}`.
- Use `rem` for the scale so user font-size preferences apply; px values here are at a 16 px root.
- Contrast: the muted ink shown in the video is a light grey on white at roughly 2.5:1, which fails WCAG 1.4.3 (4.5:1 for normal text). Muted text that carries information (dates, ids) must still meet 4.5:1; reserve lower contrast for purely decorative or disabled text. Secondary ink must meet 4.5:1 too.
- A 13 px minimum size is small for body copy on mobile; keep 13 px for labels and metadata, 16 px for reading text.
- WCAG 1.4.12 (text spacing): layouts must survive user overrides of line height 1.5, letter spacing 0.12em and word spacing 0.16em, so the 1.1 heading leading must not be enforced with fixed heights.
- 45-75 characters per line is the classic range (Bringhurst); 66 is the commonly cited ideal. The "ch" unit is based on the "0" glyph width, so 66ch is approximate for proportional text.
- `tabular-nums` only works if the font has the `tnum` OpenType feature; most UI fonts do. Right-align numeric columns as well.
- The video's claim that a single line-height everywhere is an "AI tell" is opinion, but the underlying rule (leading inversely related to size) is standard practice.
