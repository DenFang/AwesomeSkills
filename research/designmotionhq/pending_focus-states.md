---
id: unknown
reel_url: unknown
pattern_page: https://designmotionhq.com/patterns/focus-states
date: unknown
duration_s: 57
type: ui
category: interaction
topic: keyboard focus: visible ring, :focus-visible, DOM tab order, modal focus trap, skip link
sources: frames, voice-over, pattern page
---

# Focus states: five keyboard-focus rules

**Caption:** not captured yet
**Hook:** Press Tab on a checkout form and you cannot tell where focus is; removing the outline is presented not as a style choice but as legal exposure.

## Main rule
Never remove the focus indicator without shipping a better one (about 2 px thick, offset from the element, at least 3:1 contrast on every background); show it via `:focus-visible` so keyboard users get it and mouse clicks do not; keep DOM order equal to visual order; trap focus inside modals and return it to the trigger on close; and put a skip link first on the page, hidden until focused.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 2px width | focus ring thickness | 0:08-0:12 on-screen annotation, 0:06 voice, page |
| 2px offset | gap between element and ring | 0:08-0:12 on-screen (voice says only "an offset"; page says 2px) |
| 3:1 contrast | minimum ring contrast against adjacent colours | 0:08-0:12 on-screen |
| 3.2:1 | measured ring contrast on a light card and on a dark card (both pass) | 0:03-0:12 on-screen badges |
| WCAG 2.4.7 | criterion failed by `outline: none` with no replacement | 0:05-0:07 on-screen |
| `outline: 2px solid <accent token>` on `button:focus-visible` | example rule | 0:13-0:22 on-screen code |
| tab sequence 1 -> 2 -> 3 -> 4 | 2x2 KPI grid: CSS-reordered sequence jumps top-left -> bottom-right -> top-right -> bottom-left; DOM-reordered goes in reading order | 0:24-0:32 on-screen |
| Cancel -> Delete -> Close (x) -> wraps to Cancel | Tab cycle inside the modal | 0:34-0:39 on-screen |
| 40 links | navigation links before main content, skipped by one skip link | 0:42 voice, 0:43-0:51 on-screen |

## Before / after
- **No focus indicator vs visible ring.** In the checkout form, Tab moves focus but nothing marks it ("your keyboard users see nothing"), so a keyboard user cannot know which field or button will receive input. A ring makes the current target explicit.
- **`outline: none` vs a designed replacement.** Typing `button:focus { outline: none; }` removes the ring from "Sign in" and triggers a "WCAG 2.4.7 fail" tag. The replacement ring on "Continue" is annotated 2px width, 2px offset, 3:1 contrast, and is shown passing (3.2:1) both on a light surface and on a dark surface. The offset separates the ring from the element's own border/fill so it reads as a distinct indicator; checking both backgrounds prevents a ring that disappears in one theme.
- **`:focus` vs `:focus-visible`.** Mouse panel: clicking "Subscribe" shows no ring ("click, no ring"). Keyboard panel: Tab to "Subscribe" shows the ring ("tab, ring"). `:focus-visible` uses the browser's input-modality heuristic, so designers stop removing focus styles to avoid "ugly rings on click", and keyboard users keep them.
- **CSS reorder vs DOM reorder.** A 2x2 dashboard (Revenue, Orders, Customers, Refunds) reordered visually with CSS makes Tab "teleport" diagonally across the grid (dashed path). Reordering the DOM itself makes Tab flow in reading order. Keyboard and screen-reader users follow DOM order, so any mismatch breaks their mental map of the page.
- **Modal focus trap.** "Delete account?" dialog opens over Account settings: Tab cycles Cancel, Delete, Close and then wraps back to Cancel ("wraps around") without escaping to the page behind. Esc closes the dialog and focus returns to the "Delete account" button that opened it. Without this, focus leaks behind the overlay or resets to the top of the page after closing.
- **Skip link.** A header with 40 links ("40 links before content"). The first Tab reveals a "Skip to main content" link; Enter moves focus to the "Latest releases" heading ("40 links skipped"). One keypress replaces 40.

## Do
- Keep a visible focus indicator on every interactive element; if you restyle it, use roughly a 2px outline with a 2px `outline-offset`.
- Check ring contrast (at least 3:1) against every surface it can appear on, light and dark.
- Use `:focus-visible` for the ring so pointer clicks stay clean.
- Change visual order by changing DOM order, not with CSS `order`, `flex-direction: row-reverse`, grid placement or absolute positioning.
- In modals: move focus inside on open, cycle Tab/Shift+Tab within, close on Esc, return focus to the trigger.
- Make a "Skip to main content" link the first focusable element, visually hidden until focused, targeting the main content.

## Don't
- Don't write `outline: none` (or `outline: 0`) without a replacement.
- Don't use a ring colour that passes on one theme and vanishes on the other.
- Don't let CSS layout reorder content so Tab jumps around.
- Don't let focus escape a modal to the page behind it, or get lost when the modal closes.
- Don't make keyboard users tab through dozens of nav links to reach content.

## Scene by scene
- 0:00 "Press Tab. Where's the focus?" Checkout card (Email, Card number, Pay button) with a Tab key cap; caption: your keyboard users see nothing. At 0:01 the card number field shows a glowing ring (unclear whether this is the corrected state or a transition).
- 0:02 A lone "Sign in" button with a focus ring.
- 0:03 "The focus ring: Don't kill the ring." A code panel types `button:focus { outline: none; }`; the ring disappears and a "WCAG 2.4.7 fail" tag appears. Below: "On light" and "On dark" sample cards, each with a focused Sign in button and a "3.2:1" pass badge. Caption: kill it? ship a better one.
- 0:08 "Continue" button with annotations: 2px width, 2px offset, 3:1 contrast.
- 0:13 ":focus-visible: Ring for those who need it." Mouse panel (cursor clicks Subscribe, no ring, "click, no ring") vs Keyboard panel (Tab, ring appears, "tab, ring"); code `button:focus-visible { outline: 2px solid <accent>; }`. Caption: click, no ring; Tab, ring.
- 0:24 "Tab order: Focus follows the DOM." 2x2 KPI cards with numbered badges; "CSS reorder, teleports" shows a diagonal dashed path 1 -> 2 -> 3 -> 4 jumping across; then "DOM reordered, flows" renumbers and the focus ring walks in reading order. Caption: visual order = DOM order.
- 0:33 "Focus trap: Lock focus inside." Account settings card with a danger-styled "Delete account" button focused; Tab and Esc key caps. The "Delete account?" dialog opens; ring moves Cancel -> Delete -> Close (x) -> back to Cancel with a "wraps around" tag.
- 0:40 Esc pressed; dialog closes and the ring is back on "Delete account". Caption: Escape hands focus back.
- 0:42 "Skip link: Jump the header in one press." Site header with many nav links and a "40 links before content" tag. Tab reveals "Skip to main content" at top-left; Enter draws a jump arrow to the "Latest releases" heading, which gets the ring; tag changes to "40 links skipped". Caption: invisible until focused.
- 0:52 "Focus is a feature." over the blurred checkout form with a focused field; follow and save prompts.

## Voice-over summary
- Press Tab and you cannot see focus: `outline: none` is described as "not a style choice. It's a lawsuit."
- A ring needs two pixels, an offset and contrast on every background; if you remove the default, ship a better one.
- Mouse users never asked for a ring, keyboard users cannot work without one; `:focus-visible` separates them.
- Focus follows the DOM, not the layout; reordering columns with CSS makes Tab teleport, so visual and DOM order must match.
- Modals must lock focus inside, wrap Tab, and on Escape close and return focus to the opener.
- A skip link jumps past 40 links in one press; it is invisible until focused and is the first element on the page.

## Notes for the skill
- CSS: `:focus-visible { outline: 2px solid var(--focus-ring); outline-offset: 2px; }`. Keep `outline` (not only `box-shadow`) because box-shadow is removed in Windows High Contrast / forced-colors mode; if you use a shadow ring, add `outline: 2px solid transparent` so forced-colors still draws one. Never pair `:focus { outline: none }` with no `:focus-visible` replacement.
- For two-tone safety on mixed backgrounds, a double ring (inner surface-coloured gap via offset or an inner shadow, outer contrasting ring) keeps 3:1 against both the element and the page.
- WCAG mapping: 2.4.7 Focus Visible (AA) requires an indicator; 2.4.11 Focus Not Obscured (Minimum, AA, WCAG 2.2) requires it not be fully hidden by sticky headers/overlays; 2.4.13 Focus Appearance (AAA) gives the 2px-perimeter and 3:1 change-of-contrast numbers the reel uses; 1.4.11 Non-text Contrast (AA) gives 3:1. 2.4.3 Focus Order covers the DOM-order rule, 2.4.1 Bypass Blocks covers skip links.
- "It's a lawsuit" is an oversimplification: missing focus indicators are a WCAG failure and do appear in accessibility complaints, but the reason to fix it is usability, and legal exposure depends on jurisdiction.
- `:focus-visible` on text inputs always matches on click too (browsers show focus for fields regardless of modality), which is correct behaviour; do not try to suppress it.
- Modal: prefer native `<dialog>` opened with `showModal()` (built-in inertness, Esc to close) or set `inert` on the page behind; label with `aria-labelledby`. Initial focus: the first focusable element or, for destructive confirmations, the least destructive action (APG). The reel lands initial focus on Cancel, which matches. Return focus to the trigger; if the trigger no longer exists (e.g. the deleted row), move focus to a logical nearby element.
- Skip link: `<a class="skip-link" href="#main">Skip to main content</a>` as the first element; hide with a visually-hidden technique that becomes visible on `:focus` (not `display: none`, which removes it from the tab order). Target `<main id="main" tabindex="-1">` so focus actually moves in all browsers.
- Avoid positive `tabindex` values; they create the same "teleporting" problem as CSS reordering.
- Respect reduced motion: the glow/pulse used on the ring in the reel is decoration; a static ring is sufficient.
