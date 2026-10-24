---
id: unknown
reel_url: unknown
pattern_page: https://designmotionhq.com/patterns/data-table
date: unknown
duration_s: 53
type: ui
category: content
topic: data table system (sort, numerals, sticky header, density, row selection)
sources: frames, voice-over, pattern page
---

# Data tables: a table is a system

**Caption:** none (this video is published on the pattern page only; no matching reel on the Instagram profile as of 2026-10-24)
**Hook:** Your data table feels cheap (the page adds: because it is a grid of divs, not a system).

## Main rule
Build a table from a set of coordinated rules: tri-state sorting that can return to the original order, right-aligned tabular numerals, a sticky header and frozen first column with a scroll shadow, row height as a density token, and whole-row selection with an indeterminate select-all state.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 3 sort states: ascending, descending, original | column sort click cycle | 0:03-0:11 on-screen "asc -> desc -> original" + voice |
| 36 px | row height, Compact density | 0:33-0:38 on-screen "row-height: 36px · Compact"; page agrees |
| 48 px | row height, Comfortable density (default shown first) | 0:29-0:30 on-screen "row-height: 48px · Comfortable"; page agrees |
| 60 px | row height, Spacious density | 0:30-0:33 on-screen "row-height: 60px · Spacious"; page agrees |
| 3 density options | segmented control Compact / Comfortable / Spacious | 0:29 on-screen + voice |
| 1 hairline | row separator once rows are compact (instead of zebra stripes) | 0:35 voice; visible at 0:33-0:38 |
| "N of 6 selected" (1, 2, 3, 6) | selection counter chip | 0:40-0:46 on-screen |
| 3 select-all states: empty, dash (indeterminate), checked | header checkbox | 0:40-0:46 on-screen + voice |

No animation timings shown.

## Before / after
1. **Binary sort toggle vs tri-state sort (0:03-0:11).** Bad ("Binary toggle, original order lost forever"): each click flips asc/desc, so the natural order (e.g. by insertion or date) can never be restored. Good ("Tri-state, third click back to natural"): click 1 ascending (header arrow up, "Sorted ascending"), click 2 descending (arrow down), click 3 removes the arrow and restores the original order ("Natural order restored"). Why: the original order often carries meaning; a reversible cycle makes sorting exploratory without loss.
2. **Proportional left-aligned vs tabular right-aligned numbers (0:12-0:20).** Bad ("Proportional · left, digits jitter, can't compare"): $1,299.00, $84.50, $12,400.00 start at the same left edge, so magnitudes do not line up. Good ("Tabular · right, every digit on a grid"): same values right-aligned with equal-width digits; the largest ($12,400.00) and smallest ($96.00) are highlighted to show magnitude reads instantly. Why: aligned place values let the eye compare by column width, without reading each number.
3. **Header frozen vs not (0:21-0:28).** Good: header row stays while rows scroll under it, with a depth shadow ("Header stays · depth shadow"). Bad: header scrolls away ("Without freeze -> labels lost"). Then horizontal scroll: the Name column stays pinned with an edge shadow while Status scrolls under it ("First column frozen · edge shadow"). Why: the header and the row label are what users navigate by; the shadow signals that content continues underneath.
4. **Ad-hoc row height vs density token (0:29-0:38).** One segmented control switches all rows between 36/48/60 px. Spacious and comfortable rows use subtle zebra stripes; compact rows drop the stripes and use single hairline dividers. Why: one token gives a predictable rhythm; stripes at high density add visual noise, a hairline is enough to guide the eye.
5. **Checkbox-only vs whole-row selection (0:39-0:47).** Bad ("Checkbox only, tiny target, easy to miss"): only the checkbox toggles and the selected row looks almost the same. Good ("Whole-row target, tint + accent bar + checkbox"): clicking anywhere on the row selects it; the row gets a tinted background and an accent bar on its left edge; the counter reads "3 of 6 selected" and the header checkbox shows a dash; with all rows selected it becomes a tick ("6 of 6 selected"). Why: a larger hit area (Fitts's law) and multiple redundant selection cues; the indeterminate header state tells you the selection is partial before you act in bulk.

## Do
- Cycle sort through ascending, descending and back to the original order, and show the direction in the header.
- Right-align numeric columns and use tabular (monospaced) figures; keep the decimals consistent.
- Make the header sticky on vertical scroll and freeze the first column on horizontal scroll, each with a shadow that appears when content is under it.
- Expose density as a single token-driven control (e.g. 36 / 48 / 60 px).
- Use zebra stripes only at comfortable or spacious density; switch to one hairline divider when compact.
- Make the whole row clickable for selection; mark selected rows with a tint, a left accent bar and the checked box.
- Give select-all three states: empty, indeterminate dash, checked; show a "N of M selected" count.

## Don't
- Don't ship a two-state sort that throws away the natural order.
- Don't left-align numbers or use proportional digits in numeric columns.
- Don't let headers or the identifying column scroll out of view.
- Don't pick row heights per screen by eye.
- Don't make a tiny checkbox the only selection target.

## Scene by scene
- 0:00 A transactions table (Name, Status, Amount, Date) gets sorted and a row clicked; title "Why your data table feels cheap".
- 0:03 "Sort is a tri-state: asc -> desc -> original". Two cards: "Binary toggle, original order lost forever" vs "Tri-state, third click back to natural". Chip "Unsorted".
- 0:04 Click Amount: rows reorder, arrow up, "Sorted ascending".
- 0:07 Second click: arrow down, rows fly to new positions, "Sorted descending".
- 0:09 Third click: arrow disappears, only the tri-state card stays lit, "Natural order restored".
- 0:12 "Numbers need to line up: tabular figures + right align". Left column proportional/left, right column tabular/right; the top and bottom values get highlighted; caption "Right-aligned tabular digits are instantly scannable".
- 0:21 "Freeze what you navigate by". Rows scroll under a fixed header with a shadow ("Header stays · depth shadow").
- 0:23 Same scroll without a sticky header: labels scroll away ("Without freeze -> labels lost", danger colour).
- 0:25 Horizontal scroll: Name column pinned with an edge shadow, Status slides under it ("First column frozen · edge shadow").
- 0:29 "Density is a token: one control, predictable rhythm". Segmented control Compact / Comfortable / Spacious with a readout "row-height: 48px", then 60px, then 36px; stripes at larger heights, hairlines when compact.
- 0:39 "Make the whole row the target": checkbox-only table vs whole-row table; rows selected one by one, counter 1, 2, 3 of 6; header dash; then all 6 selected and header ticked.
- 0:48 Final assembled table (one row selected, Amount sorted, header dash) with "A table is a system."; "Save this before you build another table", @designmotionhq.

## Voice-over summary
- Clicking a column header once sorts ascending, twice descending, and a third time returns to the natural order; a binary toggle loses the original order.
- Right-align numbers and use tabular figures so every digit sits in the same column; proportional figures make a price list jagged.
- Freeze the header and the first column; a soft shadow shows when content scrolls under them, because without headers the table stops making sense.
- "Row height is a token, not a guess": compact, comfortable, spacious, chosen by the user; drop stripes for a single hairline when rows get dense.
- Select the whole row, show a tinted background and an accent bar; when only some rows are checked, the header shows a dash, not a tick.

## Notes for the skill
- Use a real `<table>` (or ARIA grid only if cells are interactive) so headers are announced. Put `aria-sort="ascending" | "descending" | "none"` on the sorted `<th>`, and make the header a `<button>` inside the `<th>`; only one column should carry a non-`none` value.
- Numerals: `font-variant-numeric: tabular-nums;` plus `text-align: right` on the numeric `<td>` and its `<th>` (header alignment should match the column).
- Sticky header: `position: sticky; top: 0` on `thead th` with a background; first column `position: sticky; left: 0`. Toggle the shadow only when scrolled (scroll listener or an IntersectionObserver sentinel), not permanently.
- Density: a CSS custom property such as `--row-h` set on the table root by a `data-density` attribute; persist the user's choice. 36 px rows are below the 44 px touch target guideline, so offer compact only for pointer devices or keep the interactive hit area larger than the visual row.
- Whole-row selection: keep the real checkbox as the accessible control (label it with the row name) and let row click toggle it; do not make the row itself the only focus target. Avoid conflicts if rows also open details on click (use the checkbox column or a modifier, or open details from a dedicated link).
- Header checkbox: set `input.indeterminate = true` for partial selection (it maps to `aria-checked="mixed"`); clicking it from indeterminate should select all (or clear, but be consistent).
- Do not convey selection by tint alone: the checkbox tick and the accent bar are the non-colour cues (WCAG 1.4.1). Ensure the tint keeps text contrast at least 4.5:1.
- Reduced motion: the rows animating to new positions on sort should become an instant reorder under `prefers-reduced-motion: reduce`.
