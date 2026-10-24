---
lesson: 094
kind: video
duration_s: 77
type: ui
category: content
topic: data table UX in six decisions (alignment and tabular figures, row separators, density modes, sticky column and header, empty and long cells, row actions and sort indicators)
sources: frames, voice-over
---

# Data table: six decisions that stop it looking like a spreadsheet

**Hook:** Your table is a spreadsheet in disguise, and six decisions fix that.

## Main rule
Right-align numbers with tabular figures and left-align text; separate rows with one hairline plus a hover highlight (stripes only for very wide tables); offer three density modes (40 / 48 / 56px rows); pin the identity column and the header; show a dash for missing values, truncate long text to one line with the full value available, never truncate numbers; reveal row actions on hover or focus (a kebab on touch) and show the sort arrow only on the active column.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 6 | decisions: Align, Rows, Density, Sticky, Cells, Actions (numbered 01-06 on the intro grid; section tags run "02 ALIGN" to "07 ACTIONS" because 01 is the intro) | 0:00-0:04 on-screen + voice; 0:73-0:76 checklist |
| `text-align: center` + `normal figures` | bad amount column ("Centered · proportional") | 0:05-0:08 on-screen tags |
| `text-align: right` + `tabular-nums` | good amount column ("Right · tabular") | 0:08-0:14 on-screen tags + voice |
| $1,204.00 / $89.50 / $12,480.75 | sample amounts used in the alignment comparison | 0:05-0:14 on-screen |
| 12 columns | width at which zebra stripes "earn it" | 0:13-0:25 mini card "12 columns wide · stripes earn it" |
| 1 hairline | row separator in the good version | 0:19-0:25 title + voice |
| 40px | Compact rows ("Ops" preset) | 0:26-0:37 segmented control + row bracket + voice |
| 48px | Default rows ("Everyday" preset) | 0:26-0:37 on-screen + voice |
| 56px | Comfortable rows ("Review" preset) | 0:33-0:37 on-screen + voice |
| 42px | transient bracket value while the row animates from 48 to 40 (animation frame, not a design value) | 0:28 on-screen |
| 12 columns, 6 on screen | horizontal overflow scenario | 0:38-0:48 on-screen + voice |
| `position: sticky · left: 0` / `top: 0` | pinned identity columns / pinned header | 0:38-0:48 on-screen tags |
| 5 of 128 / 6 of 128 / 1 to 5 of 128 invoices | result count and pagination text in the mock | throughout |
| "$12,48..." vs "$12,480.75" | a truncated number (struck out) vs the full number | 0:58-0:60 on-screen |
| 7 rows · 14 icons | always-visible actions: edit + delete on every row | 0:61-0:64 on-screen tag |
| 50 rows, 50 pencils | voice / caption "Fifty rows, fifty pencils" for action-column noise | 0:61-0:64 on-screen + voice |

No durations or easing values are shown.

## Before / after
- **Align (0:05-0:14):** Before: amounts centred with proportional digits; decimal points scatter (a dashed guide shows misaligned endings), "The eye cannot compare scattered digits". After: amounts right-aligned with `tabular-nums`, decimals and digit places line up, "A column that reads like a receipt"; text columns stay left; the Amount header is right-aligned with its column. Why: magnitude comparison works by scanning digit places; equal-width figures in a right-aligned column put ones, tens and decimals in vertical lines, so length equals size. Also visible but not narrated: headers change from uppercase with sort icons on every column to sentence case.
- **Rows (0:15-0:25):** Before: zebra stripes on a 5-column table, "Every other row screams for nothing". After: no stripes, one hairline between rows, the hovered row lights up with a leading-edge marker, "Stripes only earn very wide rows" (checked on a 12-column mini table). Why: on a narrow table the eye does not lose its row, so alternating fills add visual noise that competes with content; hover gives a row guide only where the pointer is. On very wide rows stripes help the eye track horizontally.
- **Density (0:26-0:37):** one table, three presets: Ops / Compact 40px, Everyday / Default 48px, Review / Comfortable 56px, switched by a single segmented control; a bracket on one row shows the height. Why: the right height depends on the task (scanning many records vs reading carefully), so it is a deliberate setting, not leftover padding.
- **Sticky (0:38-0:48):** Before: 12 columns, 6 on screen; scrolling right hides Invoice and Customer, "No name, no context"; scrolling down hides column names, "No header, no column names". After: identity columns pinned with `position: sticky; left: 0` (a shadow edge marks the pinned boundary) and header pinned with `top: 0`, "Context never leaves the screen". Why: every cell is only interpretable with its row identity and column label; pinning keeps both in view during 2D scrolling.
- **Cells, empty (0:49-0:51):** Before: blank cells marked with "?" ("Missing, zero, or loading?"). After: an en dash in missing Due date cells, "Missing gets a dash, not a blank". Why: a blank is ambiguous (no data, zero, not loaded yet, or a rendering bug); an explicit placeholder states "no value".
- **Cells, long text (0:52-0:60):** Before: "Priya Natarajan Consulting Group" wraps to three lines and the row grows ("the row explodes"). After: one line, truncated with an ellipsis, full text in a tooltip on hover, "One line per row, always". Numbers are never truncated ("$12,48..." struck out, "$12,480.75" kept). Why: uniform row height keeps the rhythm scannable; a truncated number is a wrong number.
- **Actions and sort (0:61-0:72):** Before: edit and delete icons on every row ("7 rows · 14 icons", "Fifty rows, fifty pencils") and sort icons on every header. After: icons appear only on the hovered or focused row; on a phone mock each row has a kebab menu; after clicking "Due date" only that header shows a sort arrow, "One row, one set of actions". Why: repeating identical controls on every row multiplies noise without adding information; showing one set at the point of attention keeps the table calm, and a single sort arrow tells you the current sort state.

## Do
- Right-align numeric columns (and their headers) and enable `font-variant-numeric: tabular-nums`; left-align text.
- Separate rows with one hairline; add a row hover highlight; use zebra stripes only on very wide tables (around 12 columns).
- Provide three row densities: 40px compact, 48px default, 56px comfortable, behind one toggle, defaulting by context (dense for operations, airy for review).
- Pin the identity column(s) on horizontal scroll and the header on vertical scroll.
- Render missing values as a dash with an accessible "no value" label; show zero as 0 and loading as a skeleton, not a dash.
- Keep every row to one line: truncate long text with an ellipsis and expose the full value; never truncate numbers (widen the column or abbreviate with a clear unit instead).
- Reveal row actions on row hover and keyboard focus; use a kebab menu on touch; show the sort arrow on the active column.

## Don't
- Don't centre amounts or use proportional figures in numeric columns.
- Don't use zebra stripes by default on narrow tables.
- Don't let rows wrap and change height.
- Don't leave cells blank.
- Don't put an always-visible action column of identical icons on every row.
- Don't show sort arrows on every header at once.

## Scene by scene
- 0:00 "DATA TABLE · 01 / Your table is a spreadsheet." Mock "Lumen Billing" (tabs Invoices, Customers, Reports; "New invoice" primary button; search; Status filter; columns Invoice, Customer, Amount, Status, Due date; edit / delete icons). 0:01-0:03 numbered pins 01-06 land on the table; "Six decisions fix that."; grid 01 Align, 02 Rows, 03 Density, 04 Sticky, 05 Cells, 06 Actions.
- 0:05 "02 ALIGN · Digits that never line up." Centred amounts with a dashed guide; tags `text-align: center`, `normal figures`; panels "Centered · proportional" vs "Right · tabular"; "The eye cannot compare scattered digits".
- 0:07 "Numbers right. Text left." Tag switches to `text-align: right`, then `normal figures` → `tabular-nums` (0:09); "A column that reads like a receipt"; 0:11 headers change to sentence case.
- 0:15 "03 ROWS · Stripes fight the content." Striped table; mini card "12 columns wide · stripes earn it"; "Every other row screams for nothing".
- 0:18 "One hairline. Hover does the rest." Stripes removed; the cursor moves over rows, each hovered row highlights with a leading-edge marker; 0:24 the 12-column card gets a check; "Stripes only earn very wide rows".
- 0:26 "04 DENSITY · Row height is a decision." Presets Ops / Everyday / Review and control Compact 40px / Default 48px / Comfortable 56px; bracket shows 48; 0:28 Compact clicked, bracket 42 → 40; 0:32 Default 48; 0:35 Comfortable 56.
- 0:38 "05 STICKY · Scroll right, lose the row." Wide table with Plan, Seats, Method, Issued, Terms, Owner; "12 columns, 6 on screen"; 0:41 "No name, no context"; 0:43 "Context stays on screen." identity columns pinned (`position: sticky · left: 0` highlighted); 0:46 "No header, no column names"; 0:47 header pinned (`top: 0`), "Context never leaves the screen".
- 0:49 "06 CELLS · An empty cell is a question." "?" markers in empty Due date cells; 0:51 replaced with dashes.
- 0:52 "Truncate. Never wrap." A customer name wraps to three lines and the row grows (0:53); 0:54 truncated to one line; 0:56 tooltip with the full name; 0:58 "Numbers never truncate" with "$12,48..." struck and "$12,480.75"; "One line per row, always".
- 0:61 "07 ACTIONS · An action column is noise." "7 rows · 14 icons"; "Fifty rows, fifty pencils".
- 0:65 "Reveal on hover or focus." Icons appear only on the hovered row; 0:68 phone mock with a kebab on every row ("Touch keeps a kebab"); 0:71 "Due date" header clicked, only it shows a sort arrow; "One row, one set of actions".
- 0:73 "SYSTEM · A table is six decisions." Checklist Align, Rows, Density, Sticky, Cells, Actions; follow / save buttons until 0:76.

## Voice-over summary
- A table is a spreadsheet in disguise; six decisions fix that.
- Centred amounts never line up; numbers right with tabular figures, text left, so amounts read like a receipt.
- Zebra stripes fight the content; use one hairline and a hover highlight, stripes only on wide rows.
- Row height is a decision: compact 40, default 48, comfortable 56, three modes, one toggle (dense for ops, airy for review).
- With 12 columns and 6 visible, pin the first column and the header so context never leaves the screen.
- Empty cells get a dash; long text truncates with a tooltip, numbers never truncate; reveal actions on hover or focus, a kebab on touch, sort arrows only on the active column.

## Notes for the skill
- CSS: `td.num, th.num { text-align: right; font-variant-numeric: tabular-nums; }` (also `lining-nums` if the font defaults to old-style figures). Keep currency symbol and decimals consistent per column so digits align; consider aligning on the decimal by fixing decimal places.
- Density tokens: `--row-h-compact: 40px`, `--row-h-default: 48px`, `--row-h-comfortable: 56px`; persist the user's choice. On touch devices do not go below the platform target size for interactive rows (44pt / 48dp); 40px compact is a pointer-only mode.
- Sticky: `thead th { position: sticky; top: 0; z-index: 2 }`, first column `position: sticky; left: 0; z-index: 1`, the corner header cell above both (`z-index: 3`); sticky cells need an opaque background, and a shadow or border on the pinned edge only while scrolled. Sticky fails if an ancestor between the cell and the scroll container has `overflow: hidden`.
- Semantics: use a real `<table>` with `<th scope="col">` / `scope="row"` for the identity cell; set `aria-sort="ascending|descending"` on the active sortable header and make headers `<button>`s so sortability is announced even when arrows are hidden. Hiding the sort affordance on inactive columns hurts discoverability: show a faint arrow on header hover / focus.
- Empty values: render `<span aria-label="No value">–</span>` (or visually hidden text) so screen readers don't announce "dash" without context. The video's "missing, zero, or loading? use a dash" is oversimplified: a dash should mean missing only; zero is a real value (show 0 / $0.00) and loading should show a skeleton or spinner.
- Truncation: `white-space: nowrap; overflow: hidden; text-overflow: ellipsis; max-width` on text cells. A hover-only tooltip is not accessible to keyboard and touch users: also show the full value on focus, expose it via `title` / `aria-describedby`, or allow column resize / row detail view (WCAG 1.4.13 for hover / focus content: dismissible, hoverable, persistent).
- Hover-revealed actions: reveal with `tr:hover .actions, tr:focus-within .actions { opacity: 1 }`; keep them in the tab order (do not use `display: none`), so keyboard users reach them (WCAG 2.1.1). Under `@media (hover: none)` show a kebab button per row with an accessible name such as "Actions for INV-2043". Destructive actions (delete) still need confirmation or undo.
- Row hover highlight is pointer-only feedback; selected and focused rows need their own visible state with at least 3:1 contrast (WCAG 1.4.11 / 2.4.7).
- Status pills in the mock carry colour plus text labels (Paid, Open, Overdue, Draft), which is correct; never rely on colour alone (WCAG 1.4.1).
- Zebra stripes: evidence is mixed (some studies show small accuracy gains); the video's "only for very wide tables" is a reasonable default, and stripes remain useful when rows are wide or the user must track across many columns.
