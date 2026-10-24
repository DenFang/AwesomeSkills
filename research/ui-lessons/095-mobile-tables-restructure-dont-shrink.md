---
lesson: 095
kind: video
duration_s: 84
type: ui
category: content
topic: Responsive data table on mobile: restructure into two-line rows / cards
sources: frames, voice-over
---

# Mobile tables: restructure, don't shrink

**Hook:** Your table on a phone: don't shrink it, restructure it.

## Main rule
Below the width the full table needs, turn each row into a two-line card that shows only the top-ranked columns (identity, value, state), keeps the amount in one fixed, right-aligned slot with tabular figures, labels ambiguous values, moves sorting into a control, reveals hidden fields on tap (in place or in a bottom sheet), and switches layout by a container query on the table, not the viewport.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 6 columns, 15px, scroll | full invoice table squeezed onto a phone ("Shrunk to fit - 15px"); whether 15px is text or row size is unclear on screen | 0:00-0:01 on-screen chip |
| 2 lines, 27px, no scroll | restructured rows; 27px unit target unclear on screen (it contrasts with the 15px above) | 0:02 on-screen chip |
| 6 columns, 3 fit on one line | how many columns fit a phone row | 0:05-0:07 chip + voice |
| P1 Customer, P1 Amount, P2 Status, P2 Due date, P3 Invoice ID, P3 actions | column priority ranking ("Identity, Value, State") | 0:10-0:14 |
| 2 lines per row | name left, amount right, status and due date underneath | 0:15-0:25 |
| 72 pt | height of one two-line row ("thumb-sized") | 0:24-0:25 on-screen chip |
| +3 fields | hidden fields revealed on tap (invoice ID, note, actions) | 0:51-0:52 chip |
| Invoice INV-2043, note "PO 4471, second reminder sent", buttons "Send reminder" / "Mark paid", link "Full record" | expanded row content (2 fields + actions in place) | 0:53-0:57 |
| 8 fields in sheet: Amount, Due, Issued, Plan, Seats, Method, Terms, Owner | full record in a bottom sheet ("Not a new page") | 0:58-0:62 |
| 700px | width at which six columns fit; below it, cards ("700 - 6 columns", "Under 700, cards") | 1:04-1:13 voice + on-screen |
| `@container (max-width: 700px)` | container query that switches table to cards | 1:03-1:14 code |
| 940 / 929 / 739 / 700 / 480 px | container widths in the resize demo | 1:03-1:12 |
| 375 / 768 / 1024 px | device breakpoints shown struck through (not used) | 1:03-1:14 |
| 400px panel | desktop side panel narrow enough to get cards | 1:12-1:14 |

## Before / after
- **Shrink vs restructure.** Before: all 6 columns scaled down to fit (tiny text) with horizontal scroll. After: two-line rows with larger text and no horizontal scroll. Why: shrinking kills legibility and tap accuracy; restructuring keeps readable sizes by dropping low-value columns.
- **Which columns stay.** Bad: cutting by position (keep the leftmost 3: Invoice, Customer, Amount, losing Status). Good: rank by use: identity (customer), value (amount), state (status), then due date; the invoice ID goes first because nobody reads it on a phone. Why: on small screens columns compete for attention; priority should follow the user's task, not source order.
- **Horizontal scroll vs stacking.** Bad: horizontal scroll hides half the row ("Half the row off-screen"). Good: stack into two lines, name left, amount right, status and due date below, one 72 pt row per record. Why: the row reads as a single unit and is a comfortable touch target.
- **Amount slot.** Bad: in cards the amount flows after the name / under it, so amounts drift and "nothing lines up". Good: amount always top-right in every card with `tabular-nums`, forming a right-aligned column. Why: aligned, equal-width digits keep a list of cards scannable and comparable like a numeric column.
- **Labels without a header.** Bad: "Mar 04" alone ("Mar 04 of what?"). Good: "Due Mar 04"; the dollar amount needs no label ("Dates get a label. Dollars don't."). Why: cards lose the header row, so only values whose meaning is not self-evident need inline labels.
- **Sorting.** The column-header sort becomes a toolbar control ("Sort: Due date"), re-ordering cards (overdue item moves to top).
- **Hidden fields.** Bad: dropping fields entirely or opening a new page. Good: tap a row to expand two fields plus actions in place; "Full record" opens a bottom sheet over the list ("Not a new page"). Why: preserves list context and scroll position for a quick glance.
- **Breakpoint.** Bad: switching at device widths (375/768/1024). Good: `@container (max-width: 700px)` on the table's container, so the same component shows cards in a 400px desktop side panel too. Why: the table's own available width, not the screen, decides whether 6 columns fit.

## Do
- Rank columns by user task (identity, value, state), drop IDs and secondary metadata first on small widths.
- Use two-line rows: primary label left, key number right, status and date on line two.
- Fix the number's position (top-right) in every card and use `font-variant-numeric: tabular-nums`.
- Add inline labels only to ambiguous values ("Due", "Issued"), not to self-evident ones (currency).
- Provide an explicit sort control when column headers disappear.
- Reveal hidden detail by expansion or a bottom sheet; keep the list underneath.
- Switch layouts with a container query on the table wrapper.

## Don't
- Don't scale the whole table down to fit a phone.
- Don't rely on horizontal scrolling for primary data.
- Don't choose visible columns by source order.
- Don't let amounts float with name length in card layouts.
- Don't navigate to a new page just to show a few more fields.

## Scene by scene
- 0:00 "Responsive table 01: Your table on a phone." Invoice app with a 6-column table shrunk to fit, chip "6 columns, 15px, scroll".
- 0:02 Table morphs into two-line rows, "Restructure it.", chip "2 lines, 27px, no scroll".
- 0:04 "02: Rank by use, not position." Chips "6 columns", "3 fit on one line"; first 3 columns outlined "Cut by position" (status cut off); then P1/P2/P3 badges over columns with legend Identity = Customer, Value = Amount, State = Status; Invoice and actions fade out.
- 0:15 "03: Two lines per row." Horizontal-scroll version, "Half the row off-screen"; morphs to stacked rows with callouts Name, Amount, State - Due; chip "72 pt" on one row; footer "Name left, Amount right, State below".
- 0:27 "04: One slot for the amount." Amounts placed under names with dates on the right; a zigzag line traces misaligned amounts, "Nothing lines up"; amounts snap to top-right, highlighted column, chip `tabular-nums`; "Still a column of numbers".
- 0:38 "05: Label the ambiguous." Header row struck out; date chips flagged "Mar 04 of what?"; dates become "Due Mar 04"; amount marked "No label needed"; sort control appears and switches to "Sort: Due date", overdue row moves to top.
- 0:50 "06: Hidden isn't deleted." "+3 fields" chip; tap expands the row in place (invoice ID, note, Send reminder / Mark paid, Full record), "In place"; tapping Full record raises a bottom sheet with 8 fields, "Not a new page"; footer "Expand, Sheet, Never a page".
- 1:03 "07: The table owns the breakpoint." Browser window resized 940 -> 929 -> 739 -> 700 -> 480 px; marker "700 - 6 columns"; device breakpoints 375/768/1024 struck out; under 700 it becomes cards ("Under 700, cards"); `@container (max-width: 700px)`.
- 1:12 Desktop overview dashboard: "Recent invoices" in a 400px side panel renders as cards.

## Voice-over summary
- On a phone, a six-column table should be restructured, not shrunk; only three columns fit on a line, chosen by use (identity, value, state), not by position; the ID goes first.
- Horizontal scroll hides half the row; stack each row into two lines, name left, amount right, status and due date underneath, so the row reads as one thumb-sized unit.
- Cards break comparison when amounts drift; give the amount one slot, top-right on every card, in tabular figures.
- Without a header row, label what is ambiguous ("Due March 4th"), not the dollar amount; sorting moves into a control.
- Hidden fields are revealed by tapping: two fields expand in place, the full record goes to a bottom sheet, never a new page.
- The breakpoint belongs to the table: six columns need 700px, below that cards, via one container query that also works in a desktop side panel. Ends with a product plug.

## Notes for the skill
- CSS: `.table-wrap { container-type: inline-size; } @container (max-width: 700px) { /* card layout */ }`. Pick the threshold from the table's real minimum width with all columns readable, not from device sizes.
- Semantics: if you restyle a `<table>` into cards with CSS `display: block/grid`, browsers (notably Safari) may drop table semantics; either keep `role="table"`/`row`/`cell` explicitly or render a list (`<ul>` of `<li>` with labelled fields) for the card view. Inline labels like "Due" also serve screen-reader users who lose the column header.
- Expand-in-place: use a button with `aria-expanded` and `aria-controls`; the bottom sheet needs dialog semantics (`role="dialog"`, `aria-modal`, focus trap, Escape / swipe-down to close, focus return to the row).
- Touch targets: the 72 pt row is well above the 44 pt (Apple) / 48 dp (Material) minimum; inline action buttons inside an expanded row must meet the minimum too.
- Status should not rely on colour alone (the video's chips also carry the text "Paid / Open / Overdue / Draft", which is correct).
- The 15px / 27px chips are not explained on screen; do not treat them as a rule.
- The final segment is a product advertisement; no UI rule there.
