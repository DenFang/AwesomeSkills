---
lesson: 120
kind: video
duration_s: 57
type: ui
category: responsive
topic: five things that break when a desktop dashboard is viewed at 375 px (tables, big numbers, input zoom, touch targets, fixed bottom bar)
sources: frames, voice-over
---

# Dashboard on a 375 px phone: five spots that break

**Hook:** A desktop dashboard on a phone breaks in five specific places.

## Main rule
At phone width, turn data tables into cards below 640 px, keep big figures on one line with a capped size, give inputs a 16 px font and the right keyboard attributes, enlarge targets to 44 px only for coarse pointers, and pad fixed bottom bars with the safe-area inset while leaving room under the scrolling content.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 375 px | test viewport width (phone) | 0:00-0:49 on-screen labels |
| page 786 px vs screen 375 px | page wider than the viewport, content cut off | 0:01-0:03 on-screen |
| 5 spots / 5 fixes | table, big numbers, inputs, targets, bottom bar | 0:00 voice, 0:02-0:03 numbered markers 1-5, 0:41-0:49 "5 fixes at 375px" |
| 6 columns in 375 px | table that keeps every column on a phone | 0:04-0:09 on-screen |
| < 640 px : cards | breakpoint where table rows become cards | 0:09-0:12 on-screen + voice "under 640 pixels" |
| 48 px · wraps | KPI value too large: the "+" sign wraps onto its own line ("+ alone") | 0:13-0:18 on-screen |
| 30 px · one line; max ~30 px | capped KPI size on phones (slider scale 16 / 30 / 48 / 64) | 0:19-0:22 on-screen |
| `white-space: nowrap; font-variant-numeric: tabular-nums; font-size: 30px; /* max ~30px */` | KPI value CSS | 0:14-0:22 on-screen (kpi.css) |
| 14 px : iOS zoom | input font size that makes iOS Safari zoom on focus | 0:23-0:26 on-screen |
| 16 px : no zoom | input font size on phones | 0:26-0:31 on-screen + voice |
| `inputmode="numeric"`, `autocomplete="cc-number"`, `enterkeyhint="next"` | card-number field attributes for the right keyboard | 0:23-0:31 on-screen |
| 28 px : missed | button height a thumb misses | 0:32-0:35 on-screen |
| min 44 px | touch target height for touch | 0:32-0:40 on-screen + voice |
| `@media (pointer: coarse) { min-height: 44px }` | apply the larger target only on touch; mouse "stays dense" | 0:32-0:40 on-screen |
| `position: fixed; bottom: 0;` | bottom action bar that slides under the home indicator (bad) | 0:41-0:46 on-screen |
| `padding-bottom: env(safe-area-inset-bottom)` | fix for the bottom bar | 0:47-0:49 on-screen |

## Before / after
- **Fix 1, tables.** Bad: the "Change requests" table keeps 6 columns at 375 px; Status, Needed-by and Cost sit off-screen behind a horizontal swipe ("swipe to see status"). Good: under 640 px each row becomes a card with ID, programme, title, status badge and labelled fields (Needed by, Cost, Approver). Why: the decision-critical columns become visible without hidden horizontal scrolling; cards stack naturally in a narrow viewport.
- **Fix 2, big numbers.** Bad: KPI "+€5.3M" at 48 px wraps, so the plus sign lands alone on its own line ("+ alone"). Good: `white-space: nowrap`, tabular figures and a size capped around 30 px keep "+€5.3M" on one line. Why: a split sign changes how the figure reads (a lone "+" looks like a button or icon); one line keeps the value atomic.
- **Fix 3, inputs.** Bad: card-number input at 14 px; tapping it makes iOS Safari zoom the page ("14px : iOS zoom"). Good: 16 px input text ("16px : no zoom") plus `inputmode="numeric"`, `autocomplete="cc-number"`, `enterkeyhint="next"`, which brings up the numeric keypad. Why: iOS auto-zooms focused inputs smaller than 16 px, breaking layout; the attributes give the right keyboard, autofill and return-key label.
- **Fix 4, touch targets.** Bad: Approve / Reject / more buttons about 28 px tall; the thumb lands between them ("28px : missed"). Good: on `pointer: coarse` the buttons get `min-height: 44px` ("min 44px"); with a mouse (`pointer: fine`) they "stay dense". Why: fingertips are imprecise; mouse users keep the compact layout because the rule is scoped to touch.
- **Fix 5, fixed bottom bar.** Bad: a "2 selected · Approve selected" bar with `position: fixed; bottom: 0` sits under the home indicator and covers the last card (CR-0161). Good: the bar is padded with `env(safe-area-inset-bottom)` and the list gets room below so the last row (Rail possession rebooking) scrolls fully above the bar. Why: the system gesture area and the bar both occlude content unless space is reserved.

## Do
- Test every screen at 375 px; check that page width equals screen width.
- Switch tables to cards below about 640 px, keeping status and key fields visible.
- Keep KPI figures on one line (`white-space: nowrap`, `tabular-nums`) and cap their size on phones (about 30 px in the video).
- Use at least 16 px font in inputs on phones.
- Set `inputmode`, `autocomplete` and `enterkeyhint` per field.
- Give touch targets at least 44 px under `@media (pointer: coarse)`.
- Pad fixed bottom bars with `env(safe-area-inset-bottom)` and add bottom padding to the scroll container equal to the bar height.

## Don't
- Don't hide status or deadline columns behind a horizontal swipe on phones.
- Don't let large figures wrap so that a sign or unit sits alone.
- Don't use input text smaller than 16 px on iOS.
- Don't ship 28 px touch targets.
- Don't pin a bar with `bottom: 0` without the safe-area inset and content spacing.

## Scene by scene
- 0:00 "Responsive · 375px / Your dashboard, on a phone." A "Portfolio" dashboard (Off track 2 of 6 programmes, At risk 2, Forecast vs budget +€5.3M, Waiting on you 1) overflows: labels "page 786px, screen 375px", a "Needs your decision" column cut off on the right.
- 0:02 "Five spots break." Numbered markers 1-5 on the table header, the KPI plus sign, search field, export icon, and the "Approve selected" bar.
- 0:04 "Fix 1 · Tables / Columns hide behind a swipe." "Change requests" table, "6 columns in 375px"; a swipe reveals Waiting on, Needed by, Cost; tag "swipe to see status".
- 0:09 "Under 640px: cards." Rows turn into cards (CR-0142 Extra piling at Abbey Road bridge, "Waiting for decision", 5 Oct · overdue, +€18,000, approver). Tag "< 640px : cards".
- 0:13 "Fix 2 · Big numbers / The plus sign lands alone." Before card: "+" on its own line above "€5.3M", "48px · wraps", "+ alone"; kpi.css panel; size slider at 48.
- 0:19 "One line, capped size." After card "+€5.3M" on one line, "30px · one line"; CSS lines highlighted; slider at "max ~30px".
- 0:23 "Fix 3 · Inputs / Under 16px, iOS zooms in." Billing screen (Visa ending 4242 expired 09/26, Update card form); card number field tagged 14px; tapping zooms the page ("14px : iOS zoom").
- 0:26 "16px, and the right keyboard." Field tagged 16px, "16px : no zoom"; numeric keypad appears; attribute chips font-size 16px, inputmode="numeric", autocomplete="cc-number", enterkeyhint="next".
- 0:32 "Fix 4 · Touch targets / Thumbs miss 28px buttons." Card with small Approve, Reject, more buttons; a thumb misses, "28px : missed". Panels Touch (pointer: coarse, min 44px) vs Mouse (pointer: fine, stays dense).
- 0:36 "44px, on touch only." Buttons grow to 44px on the phone; the media query chip highlights.
- 0:41 "Fix 5 · Bottom bar / The bar hides your last row." Card list with a fixed "2 selected · Approve selected" bar covering the last card; `position: fixed; bottom: 0;`.
- 0:47 "Safe area, and room below." Hatched safe-area band under the bar, `padding-bottom: env(safe-area-inset-bottom)`; the list scrolls so the last card (CR-0161) sits fully above the bar. "5 fixes at 375px".

## Voice-over summary
- A dashboard breaks on a phone in five spots.
- Tables keep every column, so status and deadline hide behind a swipe; under 640 px each row becomes a card.
- In a narrow card a big figure wraps and its plus sign lands alone; keep amounts on one line and shrink big figures on phones.
- Input text under 16 px makes Safari zoom on tap; use 16 px on phones and the right keyboard per field.
- Thumbs miss small buttons, so touchscreens get 44 px targets while a mouse keeps the dense layout; a fixed bottom bar slides under the home indicator, so pad it with the safe area and leave room under the content.

## Notes for the skill
- Table-to-cards: implement with a container query or `@media (max-width: 639px)`; keep semantic table markup on wide screens and a list of `<article>`/`<li>` cards on narrow ones, or restyle the table with `display: block` while keeping header labels via `data-label`. Make sure status uses text plus colour, not colour alone.
- Big numbers: `white-space: nowrap` alone can overflow the card; combine with a fluid cap such as `font-size: clamp(1.25rem, 6vw, 1.875rem)` (30 px = 1.875rem) and `min-width: 0` on flex children. Keep the sign attached with a non-breaking construction if the value can wrap elsewhere.
- iOS input zoom: the 16 px threshold is accurate for iOS Safari. Do not "fix" it with `maximum-scale=1` or `user-scalable=no` in the viewport meta; that blocks user zoom and fails WCAG 1.4.4 Resize Text.
- Keyboard attributes: for card numbers prefer `inputmode="numeric"` with `autocomplete="cc-number"`; use `type="text"` not `type="number"` (spinners, leading zeros). `enterkeyhint="next"` should match real focus order.
- Touch targets: 44 px matches Apple HIG (44 pt); Material uses 48 dp. WCAG 2.2 AA (2.5.8) requires at least 24x24 CSS px or equivalent spacing for all pointers, so the dense mouse layout must still meet 24 px; 44 px is WCAG 2.5.5 (AAA). `pointer: coarse` reports the primary pointer only; for hybrid devices consider `any-pointer: coarse`.
- Safe area: `env(safe-area-inset-bottom)` only returns a non-zero value when the viewport meta includes `viewport-fit=cover`. Use `padding-bottom: calc(<bar padding> + env(safe-area-inset-bottom))`, and give the scroll container `padding-bottom` equal to the bar's full height (or `scroll-padding-bottom`) so focused elements and the last row are not hidden.
