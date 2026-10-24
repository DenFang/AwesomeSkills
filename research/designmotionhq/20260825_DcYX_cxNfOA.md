---
id: DcYX_cxNfOA
reel_url: https://www.instagram.com/reel/DcYX_cxNfOA/
pattern_page: none
date: 2026-08-25
duration_s: 50
type: ui
category: content
topic: Number formatting in UI: tabular figures, right alignment, compact values, relative time, currency column
sources: frames, voice-over, caption
---

# Numbers that line up: five formatting rules

**Caption:** Number formatting like a pro.
**Hook:** "Pro numbers line up. Amateur numbers dance": watch the right edge of a revenue column snap straight when tabular figures are switched on.

## Main rule
Render numeric data with tabular (fixed-width) figures and right-alignment so digits and decimals form straight columns; abbreviate large values with the exact value available on demand, show relative time only for the last 24 hours, and keep the currency symbol in its own pinned position so decimals align.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| `font-variant-numeric: tabular-nums;` | the one-line fix, "one width per digit" | 0:10-0:16 on-screen code |
| 4,208.50 / 72.00 / 18,940.25 / 1,006.75 / 340.00 | Q3 revenue column, proportional vs tabular | 0:00-0:02 on-screen |
| 1,111 / 8,888 / 1,010 / 9,090 | same digit count, different pixel width ("edge wobbles") | 0:05-0:09 on-screen |
| 1,204.50 / 8,840.00 / 1,010.25 / 9,090.90 | "decimals on one line" demo | 0:10-0:16 on-screen |
| `text-align: left` -> `text-align: right` | price column in a product table ($1,299, $980, $2,450, $89, $1,150) | 0:17-0:23 on-screen |
| 3,400,000 -> 3.4M | compact notation | 0:24-0:28 on-screen |
| 1K = 1,000; 1M = 1,000,000; 1B = 1,000,000,000 | abbreviation legend | 0:25-0:28 on-screen |
| 1M -> tooltip "Exact value 1,000,000" | full precision on hover | 0:26-0:28 on-screen |
| 14:32, 12:05, 08:40 -> 2h ago, 5h ago, 9h ago | activity feed timestamps, relative under the boundary | 0:29-0:36 on-screen |
| 24h boundary | switch from relative to absolute ("Mar 3", "Feb 27") | 0:31-0:36 on-screen |
| $1,000.00 / $9.99 / $250.00 / $42.50 | currency column, symbol glued vs pinned | 0:37-0:42 on-screen |
| 5 | rules in the summary list | 0:44-0:49 on-screen |

## Before / after
1. **Proportional vs tabular figures (0:00-0:16).** Bad: default proportional digits, where "1" is a narrow glyph and "0" a wide one, so numbers with the same digit count (1,111 vs 8,888) have different pixel widths and a right-aligned column has a ragged edge ("dances", "edge wobbles"). Good: `font-variant-numeric: tabular-nums` gives every digit the same advance width, so the decimal points and last digits form a straight vertical line ("decimals aligned"). Why: equal-width digits make place values line up, so the eye can compare magnitudes by column position instead of reading each number.
2. **Right-align numbers, left-align text (0:17-0:23).** Bad: prices left-aligned next to left-aligned product names, so $89 and $2,450 start at the same x and their units do not line up. Good: price column `text-align: right`, product names stay left. Why: with right alignment, ones sit under ones and thousands under thousands; a longer number visibly sticks out further left, so magnitude is readable at a glance ("the eye compares straight down the last digit").
3. **Abbreviate big values (0:24-0:28).** Bad: "3,400,000" in a KPI tile, wider than its neighbours. Good: 1K, 1M, 3.4M tiles; hovering 1M shows "Exact value 1,000,000". Why: a dashboard tile needs order of magnitude, not full precision; compact values keep tiles uniform and scannable while precision stays one interaction away.
4. **Relative time for recent events (0:29-0:36).** Bad: activity feed shows 14:32, 12:05, 08:40, which forces the user to compute elapsed time. Good: "2h ago", "5h ago", "9h ago" for events under 24 hours, then a "24h boundary" divider, then absolute dates "Mar 3", "Feb 27". Why: for recent items the question is "how long ago", for old ones "when"; a relative label for an old event ("41 days ago") is harder to place than a date.
5. **Pin the currency symbol (0:37-0:42).** Bad: "$" glued to each number in a right-aligned column, so the symbols land at different x positions and form a ragged left edge. Good: "$" pinned at a fixed position on the left of the cell, digits right-aligned, decimals in one vertical line. Why: the symbol is the same on every row and carries no comparison value; aligning decimals is what makes values comparable.

## Do
- Apply `font-variant-numeric: tabular-nums` to tables, KPI tiles, prices, timers, counters and any number that changes or is stacked.
- Right-align numeric columns (and their headers); left-align text columns.
- Keep the same number of decimal places within a column so decimals align.
- Abbreviate large values in summaries (K, M, B) and expose the exact value on demand.
- Use relative time for events under 24 hours and absolute dates beyond that.
- Put the currency symbol in a fixed slot (or in the column header) instead of attaching it to each value.

## Don't
- Don't leave numeric columns in proportional figures.
- Don't left-align or centre numbers you expect users to compare.
- Don't show raw clock times for recent activity, or "N days ago" for old items.
- Don't let a currency symbol glued to the value push the column out of alignment.

## Scene by scene
- 0:00 "UI Numbers 01, Watch the right edge.": Q3 Revenue column labelled "proportional", right edge ragged; switches to "tabular-nums", edge becomes a straight line; chips "dances -> lines up".
- 0:03 "The problem, proportional: Every digit picks its own width.": "1" labelled narrow glyph vs "0" wide glyph; "Same length, ragged edge" list 1,111 / 8,888 / 1,010 / 9,090 with "edge wobbles"; banner "Same digit count, different pixel width."
- 0:10 "The fix, tabular: One line locks every width.": styles.css types `font-variant-numeric: tabular-nums;`; column badge changes from pnum to tnum; "decimals aligned"; banner "One width per digit, decimals in a straight line."
- 0:17 "Alignment, right-align: Numbers right, text left.": product table (Nordic Chair, Oak Desk, Linen Sofa, Brass Lamp, Wool Rug) with prices flipping from `text-align: left` to `text-align: right`; rows highlight; "The eye compares straight down the last digit."
- 0:24 "Abbreviation, compact: Big numbers, small footprint.": "3,400,000 -> 3.4M"; tiles Monthly Views 1K, Total Users 1M, Revenue 3.4M; legend 1K/1M/1B; hover tooltip on 1M shows exact value; "Compact by default, exact on hover."
- 0:29 "Relative time, recency: 14:32 or 2h ago?": activity feed flips 14:32/12:05/08:40 to 2h/5h/9h ago; "24h boundary" divider; older rows Mar 3, Feb 27; "Relative under a day, absolute for everything older."
- 0:37 "Currency, decimals: Pin the symbol, align the decimal.": left panel "$ glued to the number" vs right panel "$ pinned, decimals aligned" with a vertical guide through the decimals; "Decimals line up. Dollar signs don't have to."
- 0:43 "Numbers, formatted like a system.": summary list 01 Tabular figures, 02 Right-align numbers, 03 Abbreviate big values, 04 Relative recent time, 05 Pin the currency; site plug and "save this".

## Voice-over summary
- Default fonts give each digit its own width ("1" thin, "0" wide), so columns wobble; tabular figures lock digits to one width and decimals snap into a column.
- Right-align numbers and left-align text, because magnitude is compared by the last digit.
- Show 1K or 1M instead of a thousand or a million, with full precision on hover.
- A clock time like 14:32 means little; "two hours ago" means a lot: relative for recent, absolute for old.
- Keep the currency symbol out of the number column; align decimals, not dollar signs.

## Notes for the skill
- Check that the font actually has tabular figures (`tnum` OpenType feature); many UI fonts default to proportional. Fallback: `font-feature-settings: "tnum" 1`. A monospace font also works but changes the look; the demo's "after" currency column uses a monospace face.
- Use `Intl.NumberFormat` for locale-correct separators and compact notation (`notation: "compact"`), and `Intl.RelativeTimeFormat` for "2h ago". Decimal and thousands separators, symbol position (before or after) and abbreviation suffixes differ by locale, so do not hard-code "$" left or "K/M/B".
- "Exact on hover" excludes touch and keyboard users: expose the full value via a tooltip that also opens on focus and tap, `title`/`<abbr title>` as a minimum, or `aria-label` with the full number so screen readers do not read "1M" ambiguously. Do the same for relative times: `<time datetime="2026-08-25T14:32">2h ago</time>` with the absolute time in a tooltip.
- Relative labels must update (or be re-rendered) as time passes, otherwise "2h ago" goes stale on a long-open page.
- Right-align the numeric column header as well, and keep a consistent number of decimals per column; mixed precision breaks decimal alignment even with tabular figures.
- Tabular figures also stop layout jitter in animated counters, timers and live prices (digits changing width shift neighbouring content).
