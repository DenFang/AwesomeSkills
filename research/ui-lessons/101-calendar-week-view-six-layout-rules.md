---
lesson: 101
kind: video
duration_s: 76
type: ui
category: content
topic: Calendar week view layout: grid, now line, colour stripe, overlap columns, height = duration, drag-to-create, pinned all-day row
sources: frames, voice-over
---

# Calendar week view: six layout rules

**Hook:** One week, 40 events, zero overlap, six layout rules.

## Main rule
Build a week view as a strict time grid (7 day columns, 24 one-hour rows, hour labels on the lines, a "now" line, opened scrolled to the current time), mark each calendar with a thin colour stripe and a faint tint instead of a solid fill, place concurrent events side by side at equal widths, make height proportional to duration with a one-line minimum, snap drag-create, move and resize to 15 minutes, and keep all-day events in a pinned row above the scrolling grid.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 40 events, 0 overlap (5 events, 0 overlap at start) | hook demo week | 0:00-0:03 on-screen + voice |
| Work 15, Personal 15, Team 10 | events per calendar in the legend | 0:01-0:03 on-screen |
| columns 7, rows 24 | week grid: one column per day, one row per hour | 0:04-0:13 on-screen + voice |
| scroll 8:00 | initial scroll position, with now at 10:40 visible | 0:04-0:10 on-screen |
| `scrollTop = 0 // 00:00` (struck out) | anti-pattern: opening at midnight | 0:12-0:13 on-screen |
| 10:40 | "now" line label (red line across the grid) | 0:02-0:13, 0:54-0:60 on-screen |
| 3 px stripe, fill at 10% | event chip styling per calendar colour | 0:14-0:23 on-screen + voice |
| 1.9 : 1 | white title on a solid warm fill (fails) | 0:15-0:23 on-screen |
| 11.4 : 1 | title on stripe + 10% tint (passes) | 0:17-0:23 on-screen |
| 1/2 width each | two events in the same hour (Design sync 2:00-3:00, 1:1 Maya 2:00-3:00) | 0:24-0:28 on-screen |
| 1/3 width each, 33% | three overlapping events (adds Sprint review 2:30-3:30) | 0:28-0:32 on-screen |
| "1 hidden", "+1 more" (struck out) | anti-pattern: hiding overlaps behind a counter | 0:24-0:31 on-screen |
| 2 h -> 120 px | height = duration | 0:33-0:42 on-screen |
| 1 h -> 60 px | one row, one hour | 0:34-0:42 on-screen + voice |
| 15 min -> 30 px | minimum height: one line, title clipped | 0:37-0:42 on-screen |
| 5 min -> 6 px | below the minimum: a bar, title on hover ("Ping 9:00-9:05") | 0:40-0:42 on-screen |
| snap 15 min | drag-create, move and resize step | 0:43-0:53 on-screen + voice |
| start 3:00, end 3:15 -> 3:45, dur 15 -> 45 min | live drag-state readout while drawing | 0:44-0:47 on-screen |
| 3:45-4:30, then 4:00-4:45 | event moved by its body, duration kept at 45 min | 0:48-0:50 on-screen |
| 4:00-5:00, dur 1 h | resize from bottom edge | 0:51-0:53 on-screen |
| "resize: top edge" (struck out) | top-edge resize not allowed | 0:51-0:53 on-screen |
| "00:00-24:00 block" (struck out) | anti-pattern: all-day event drawn as a full-height block ("eats the day") | 0:54-0:60 on-screen |
| scroll 8:00 -> 10:00 -> 11:00, "row stays" | pinned all-day row while hours scroll | 0:56-0:61 on-screen |
Note: 15 min -> 30 px is not proportional to 60 px/h (that would be 15 px); the 30 px is the one-line minimum height, and 6 px for 5 min is a minimum bar height.

## Before / after
1. **Grid and now (0:04-0:13).** Bad: the view opens at `scrollTop = 0` (midnight), showing empty night hours. Good: 7 columns x 24 one-hour rows, hour labels sitting on the grid lines (not centred in cells), a red line at the current time, and the view opens scrolled to now (8:00 at top with 10:40 visible). Why: labels on lines mark exact boundaries so start times read precisely; opening at now puts the relevant part of the day in view without a scroll.
2. **Stripe, not fill (0:14-0:23).** Bad, "Full fills, rainbow": each event solid-filled in its calendar colour; white title on a warm fill measures 1.9:1. Good, "Stripes, reads": a 3 px left stripe in the calendar colour and the body tinted at 10%; title contrast 11.4:1. Why: solid fills turn a busy week into a patchwork of strong colours that competes with the text; a thin stripe still identifies the calendar while the low-opacity body keeps one readable text colour on every calendar.
3. **Same hour, side by side (0:24-0:32).** Bad: a second event at the same time is stacked underneath, with "1 hidden" or "+1 more". Good: two concurrent events get 1/2 width each, three get 1/3 each ("3 visible, 0 hidden"). Why: every event remains visible and clickable; the shared time is visible as shared width instead of a hidden count.
4. **Height is duration (0:33-0:42).** 60 px per hour: 2 h = 120 px, 1 h = 60 px. 15 min still gets a 30 px chip with a one-line clipped title; anything shorter (a 5-minute "Ping") becomes a 6 px bar whose title shows on hover. Why: vertical size encodes length directly, so the day's load is visible at a glance; the minimum height keeps short events legible.
5. **Drag draws, snap holds (0:43-0:53).** Dragging on empty space draws a new event, snapping to 15-minute steps; the time label and a start/end/duration readout update live during the drag. The event moves by its body (duration preserved) and resizes only from the bottom edge; top-edge resize is struck out. Why: snapping removes off-by-a-few-minutes errors; live labels give feedback before release; one resize handle avoids accidental resizes when the user meant to move.
6. **All-day in a pinned row (0:54-0:61).** Bad: "Offsite" and "Leo OOO" drawn as 00:00-24:00 blocks covering whole day columns ("eats the day"). Good: an "All day" row pinned under the day headers holds them as short bars; the hour grid scrolls beneath while the row stays. Why: all-day items are attributes of the date, not time blocks; pinning keeps them visible without hiding the timed events.

## Do
- Use a fixed time scale (here 60 px per hour) and derive event height from duration, with a one-line minimum and a thin bar below that.
- Put hour labels on the horizontal lines, draw a now line, and open the view scrolled to the current time.
- Identify calendars by a thin colour stripe plus a light tint, keeping the title in the normal text colour.
- Split width equally between concurrent events (1/2, 1/3).
- Snap create, move and resize to 15 minutes; update the time label continuously during the drag.
- Keep all-day events in a sticky row above the hour grid.

## Don't
- Don't open a day or week view at midnight.
- Don't use solid saturated fills with white text for every calendar colour.
- Don't hide concurrent events behind "+1 more" in a time-grid view.
- Don't draw all-day events as full-height blocks.
- Don't offer resize handles on both edges if moving by the body is the main action (the video allows bottom-edge resize only).

## Scene by scene
- 0:00 "Calendar is a system 01, One week. Forty events.": app "Halo", week of Sep 14 (Mon 14 to Sun 20, today Tue 15); grid fills from 5 to 40 events, "40 events, 0 overlap"; legend Work 15, Personal 15, Team 10; all-day row with Offsite and Leo OOO; now line 10:40.
- 0:04 "02, Seven columns. One hour a row.": chips columns 7, rows 24, scroll 8:00; day headers highlight; hour rows highlight; "Opens at now".
- 0:11 Grid scrolls to midnight (scroll 12:00) with a struck-out "scrollTop = 0 // 00:00", then back up through 4:00 and 6:00 toward now.
- 0:14 "03, A stripe, not a fill.": zoomed Mon to Wed with Calendars legend; panel "Title on the fill": white on a warm fill 1.9:1 vs stripe + 10% 11.4:1; mini-weeks "Full fills, rainbow" vs "Stripes, reads"; "3 px stripe, fill at 10%".
- 0:24 "04, Same hour, side by side.": Tuesday 1-5 PM; 1:1 Maya covers Design sync with "1 hidden"; they split to 1/2 width each; Sprint review 2:30-3:30 joins and all three become 1/3 (33%); "+1 more" struck out; "3 visible, 0 hidden".
- 0:33 "05, Height is duration.": Monday with Deep work 10-12 (120 px, 2 h), Lunch w/ Leo 1-2 (60 px, 1 h), Standup 15 min (30 px, min 1 line); a 9:00 bar with tooltip "Ping 9:00-9:05" (5 min -> 6 px); "60 px an hour, min 1 line".
- 0:43 "06, Drag draws. Snap holds.": Thursday; drag state panel start 3:00, dur 0 min, snap 15 min; drawing 3:00-3:15 then 3:00-3:45 (45 min); "New event"; moved to 3:45-4:30 then 4:00-4:45; resized from the bottom to 4:00-5:00 (1 h); "resize: top edge" struck out; "Snap 15 min, resize bottom only".
- 0:54 "07, All day lives in a pinned row.": Offsite and Leo OOO as tall dashed blocks labelled "eats the day"; they collapse into an "All day" row; chips all day pinned, scroll 8:00 -> 10:00 -> 11:00, row stays; "00:00-24:00 block" struck out; "Pinned row, the grid scrolls".
- 1:01 "08, Six rules. One week that reads.": recap chips Grid + now, Overlap columns, Snap 15 min, Color stripe, Height = duration, Pinned all-day, over a mini week.

## Voice-over summary
- A week with 40 events and zero overlap comes from six layout rules.
- Seven columns, 24 one-hour rows, hour labels on the line not in the cell, a red line for now, and the view opens scrolled to now rather than midnight.
- Colour per calendar as a 3 px left stripe with the fill at 10%, so the title stays readable on every colour; full fills make a busy week a rainbow.
- Two events in the same hour sit side by side at half width, three at a third, never stacked or hidden behind "+1".
- Height is duration (one hour = 60 px); 15 minutes still gets a clipped one-line title, shorter events become a hoverable bar.
- Drag on empty space to draw an event, snapping to 15 minutes; move by the body, resize by the bottom edge only; the time label updates while dragging; all-day events live in a pinned row that stays while hours scroll.

## Notes for the skill
- Implementation: CSS grid with `grid-template-columns: <gutter> repeat(7, 1fr)` and absolutely positioned events at `top = minutes * (60px / 60)`, `height = max(duration * 1px/min, 1 line)`. Overlap layout: group events into collision clusters and assign columns (greedy interval partitioning); width = 1/columns. The all-day row uses `position: sticky; top: <header height>`.
- The minimum-height rule breaks strict proportionality (15 min drawn at 30 px overlaps the next 15-minute slot). Account for it in collision detection (use the rendered height, not the raw duration) or short back-to-back events will overlap visually.
- Equal-width splitting degrades with many concurrent events (5-6 columns become unreadable on narrow screens). A fallback is needed: a cascade/offset layout, or a capped column count with an explicit overflow affordance. The "never +1 more" rule is right for 2-3 overlaps, not for unlimited ones; month views legitimately use "+N more".
- Contrast numbers are the video's own measurements; the rule behind them: event titles at least 4.5:1 against their actual background (WCAG 1.4.3). The stripe colour, as the only calendar identifier, is a non-text cue: keep calendar names available (tooltip, legend, accessible name) since colour alone cannot convey it (WCAG 1.4.1).
- Drag-only interactions fail WCAG 2.5.7 (Dragging Movements): provide a click or keyboard path to create, move and resize (for example, click a slot to create, edit start/end in a form, arrow keys to move in 15-minute steps). Give events a focusable element with an accessible name containing title, day and time range.
- The "hover for the title" bar for very short events needs a focus and tap equivalent (touch has no hover).
- The now line must update (at least every minute) and the "open at now" scroll should only run on first render, not after the user has scrolled.
- Use the user's locale and time zone for labels (the grid shows "CET"); daylight-saving days have 23 or 25 hours, so "24 rows" is a simplification.
