---
lesson: 047
kind: video
duration_s: 47
type: ui
category: forms
topic: date and date-range pickers
sources: frames, voice-over, lesson notes
---

# Date pickers: presets, range highlight, two months, keyboard, mobile sheet

**Hook:** The same date costs six clicks with a month-by-month calendar or one click with a preset.

## Main rule
Lead a date-range picker with one-click presets and keep a custom range for the rest; make the custom range legible (hover preview, click start, click end, draggable edges), show two months side by side (three on wide screens), support the full keyboard including typing, and on mobile replace the popover with a full-screen, vertically scrolling sheet with a large confirm button.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 6 clicks vs 1 click | reaching a date by paging months ("Click 1/6" … "Click 6/6", Feb to Sep 2026) vs a preset ("Click 1/1") | 0:00-0:01 on-screen + voice |
| 90% | share of cases covered by presets | 0:02-0:11 headline + voice; page says "~90%" |
| Today 14%, Yesterday 9%, Last 7d 31%, Last 30d 22%, Last quarter 14%, Custom 10% | illustrative usage split per option (presets sum to 90%, custom 10%) | 0:11 chips under the picker (on-screen only) |
| 5 presets + 1 custom | Today, Yesterday, Last 7 days, Last 30 days, Last quarter, Custom range | 0:03-0:11 + voice |
| Apr 14 / Apr 13 / Apr 7 → Apr 14 / Mar 15 → Apr 14 / Q1 2026 / Mar 20 → Apr 8 | selection pill per preset when today is April 14, 2026 | 0:05-0:11 |
| 3 steps | hover = preview, click = lock (start then end), drag = refine | 0:12-0:19 chips + voice |
| May 5 → May 18 · 14 days | range summary pill, day count inclusive | 0:17-0:19 |
| 4 "next" clicks | single-month calendar forced to page ("Click 1/4", "Click 3/4") | 0:20-0:21 on-screen; voice "don't make users click next four times" |
| 2 months | side-by-side calendar so ranges cross month boundary (Mar 20 → Apr 12 example) | 0:22-0:26 |
| 3 months | on wide screens | 0:22-0:26 caption "WIDE SCREENS · 3 MONTHS" + voice |
| ← → ↑ ↓, Home, End, Enter, Esc, PgUp, PgDn | keys shown on the keyboard strip ("EVERY KEYSTROKE MATTERS") | 0:27-0:35 |
| MM/DD/YYYY | typed date mask in the input; segments fill progressively (03/DD/YYYY → 03/12/YYYY → 03/12/2026) | 0:27-0:31 |
| PgUp = 1 month, Shift+PgUp = 1 year | month and year jumps (March 2026 → February 2026 → February 2025) | 0:32-0:35 + voice |
| ≥ 44px | touch target size in the mobile sheet | 0:37-0:43 chip "Touch target ≥ 44px" |

## Before / after
1. **Paging months vs presets.** Bad: a single calendar where reaching a date means clicking the month arrow repeatedly (6 clicks). Good: a preset list (Today, Yesterday, Last 7 days, Last 30 days, Last quarter, Custom range) next to the calendar; one click selects and paints the range and updates a selection pill. Why: most real queries are relative ranges; presets turn several precise pointer actions into a single recognition choice and show the resulting dates as confirmation.
2. **Opaque range selection vs hover, click, drag.** Bad (implied): clicking dates with no preview of what range will result. Good: hovering after the first click paints a live preview of the range; the first click locks the start, the second the end; then the start and end cells show drag handles to adjust without restarting; a pill shows "May 5 → May 18 · 14 days". Why: the preview gives feedback before commitment, and editable edges make correction cheap instead of forcing a full redo.
3. **Single month vs two months.** Bad: a one-month view (April 2026) requiring "next" clicks to reach June (Click 1/4 … 3/4); ranges across a month boundary are awkward. Good: March and April side by side with a range Mar 20 → Apr 12 flowing across; three months on wide screens. Why: cross-month ranges are common, and seeing both ends at once removes navigation and keeps context.
4. **Mouse-only vs full keyboard.** Good: typing into the masked input (MM/DD/YYYY) fills segments and moves focus in the grid; arrows move the focused day; Enter confirms; Esc closes; PgUp/PgDn jump a month; Shift+PgUp a year. Why: typing is fastest for known dates, and grid keyboard support is required for accessibility and power users.
5. **Tiny popover vs full-screen sheet on mobile.** Bad: the desktop popover shrunk onto a phone ("Too tiny to tap"). Good: a full-screen "Select dates" sheet with months stacked vertically and scrolling, a "Today" chip at the top, and a range pill plus a large "Confirm dates" button at the bottom. Why: vertical scroll matches the touch gesture, cells reach the 44px touch size, and the confirm sits within thumb reach.

## Do
- Put presets (Today, Yesterday, Last 7 days, Last 30 days, Last quarter) first and "Custom range" last.
- Show the resolved dates of the current choice in a visible summary pill (e.g. "Mar 15 → Apr 14").
- Paint a hover preview between the locked start and the pointer during range selection.
- Keep range edges draggable after both ends are set.
- Show the day count of a range in the summary ("14 days").
- Render two months side by side on desktop, three on wide screens.
- Accept typed dates with a format mask and sync them to the grid.
- Support arrows, Home/End, Enter, Esc, PgUp/PgDn and Shift+PgUp/PgDn.
- On mobile, use a full-screen sheet, vertical scrolling months, a "Today" jump, touch targets of at least 44px and a large confirm button at the bottom.

## Don't
- Force repeated "next month" clicks to reach a date a few weeks away.
- Ship a single-month calendar for range selection.
- Shrink the desktop popover onto mobile.
- Make the calendar mouse-only or block typing into the field.

## Scene by scene
- 0:00 Headline "Same date. Different time." Left card "The old way": single month calendar, counter "Click 1/6" as the month pages from February to September 2026 ("Click 6/6"). Right card "The right way": presets list plus calendar, "Last 30 days" picked, counter "Click 1/1".
- 0:02 Section "01 · PRESETS": "Presets cover 90% of cases." A panel with a preset column and a two-month calendar (March, April 2026), selection pill "April 14". Presets appear one by one, then each is clicked in turn: Today (April 14), Yesterday (April 13), Last 7 days (Apr 7 → Apr 14), Last 30 days (Mar 15 → Apr 14), Last quarter (Q1 2026, February/March grid), Custom range (Mar 20 → Apr 8). The active preset uses the accent fill; the range is filled with a tinted accent, ends solid.
- 0:11 Usage chips under the picker: Today 14%, Yesterday 9%, Last 7d 31%, Last 30d 22%, Last quarter 14%, Custom 10% (custom highlighted).
- 0:12 Section "02 · RANGE HIGHLIGHT": "Hover. Click. Drag." Single May 2026 calendar, chips "Hover = preview", "Click = lock", "Drag = refine" highlight in sequence; hover outlines days, click sets May 5, second click sets May 18, the range fills, pill "May 5 → May 18 · 14 days". Drag handles appear on the 5 and the 18.
- 0:20 Section "03 · TWO MONTHS": "Cross-month is normal." Bad: single month "April 2026" with "× Single month" and counter "Click 1/4" → June 2026 "Click 3/4".
- 0:22 Good: "✓ 2 months side by side", March + April 2026 with range Mar 20 → Apr 12; below a small preview "WIDE SCREENS · 3 MONTHS" (April, May, June), which then expands into a full three-month panel.
- 0:27 Section "04 · KEYBOARD": "Type. Arrow. Validate." Input "DATE MM/DD/YYYY" over a March 2026 grid; key strip ← → ↑ ↓ Home End Enter Esc Pg↑ Pg↓ "EVERY KEYSTROKE MATTERS". Pressed keys light up; focus ring moves across days (6 → 21 → 20); typing fills 03/DD/YYYY → 03/12/YYYY → 03/12/2026.
- 0:31 Enter highlights: day 12 becomes selected. Esc highlights next.
- 0:33 PgUp: grid shows February 2026 with 12 still marked; Shift+PgUp: February 2025.
- 0:36 Section "05 · MOBILE": "Mobile is a sheet." Three phones: "× Tiny popover" (small calendar floating over a Bookings form, footer "Too tiny to tap"), "✓ Full-screen sheet" ("Select dates" with a "Today" chip, months stacked and scrolling vertically), "✓ Confirm button" (range Mar 12 → Mar 18, pill and a wide "Confirm dates" button, "Done" in the header). Chips "Touch target ≥ 44px", "Confirm action visible".
- 0:44 Outro: calendar with a range, "Follow for more UI systems", "Save this for your next form", handle badge.

## Voice-over summary
- The same date takes six clicks or one; presets cover about 90% of cases (today, yesterday, last 7 days, last 30 days, last quarter), and custom range handles the rest.
- Highlight the range: hover paints a preview, the first click sets the start, the second sets the end, and edges can be dragged to refine.
- Show two months side by side because ranges cross months; widen to three months on widescreens instead of making people click next four times.
- Keyboard: arrows move the cursor, typing enters the date directly, Enter validates, Escape closes, Page Up jumps a month and Shift+Page Up a year.
- On mobile it should not be a popover but a full-screen sheet scrolling vertically, today at the top and a big confirm button at the bottom.

## Notes for the skill
- Follow the WAI-ARIA APG "Date Picker Dialog" pattern: grid with `role="grid"`, roving `tabindex`, arrows by day/week, Home/End to start/end of week, PgUp/PgDn by month, Shift+PgUp/PgDn by year, Enter/Space select, Esc closes and returns focus to the trigger. The video's key mapping matches APG.
- Always keep a text input as an alternative to the grid; parse typed dates leniently and validate on blur/Enter with an inline error, not a silent reset. Respect locale order (MM/DD vs DD/MM) and first day of week rather than hardcoding the US format shown.
- Define preset semantics precisely and show resolved dates. In the demo, "Last 7 days" resolves to Apr 7 → Apr 14 (8 inclusive days) and "Last 30 days" to Mar 15 → Apr 14 (31 inclusive days): an off-by-one; decide whether "last N days" includes today and keep N days exactly. "Last quarter" is shown as "Q1 2026" in a February/March two-month view, so January is not visible; for ranges longer than the visible months, rely on the summary pill.
- Hover preview is pointer-only; on touch, show the preview after the first tap and provide the same feedback through the summary pill. Drag handles need a keyboard alternative (e.g. Shift+arrows extend the range end).
- Announce selected range changes via a polite live region; give each day cell an accessible name with full date and state ("Monday, May 5, 2026, range start").
- On mobile, a full-screen sheet needs a clear close/Done, focus trapping, and the confirm button placed above the safe-area inset; 44px matches Apple HIG (44pt), Material recommends 48dp, WCAG 2.5.8 minimum is 24px.
- Disable or visibly mark out-of-range dates (min/max) and never hide them, so the grid layout stays stable.
