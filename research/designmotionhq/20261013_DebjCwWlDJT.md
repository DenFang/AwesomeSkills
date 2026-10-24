---
id: DebjCwWlDJT
reel_url: https://www.instagram.com/p/DebjCwWlDJT/
pattern_page: none
kind: carousel
date: 2026-10-13
type: ui
category: interaction
topic: teaching keyboard shortcuts (menus, tooltips, post-action tip, consistency)
sources: caption, video slide (slide 4 of 6)
---

# Keyboard shortcuts that users actually learn

**Caption:** Power users are trained by the interface, which teaches the keys it shows; four rules: menu rows show their shortcut right-aligned, tooltips appear after 500 ms and repeat the same key, after 3 mouse uses show one quiet tip (never the first time), and each action has one shortcut used everywhere.
**Hook:** Power users are made, not born: they learn the keys you put in front of them.

## Main rule
Expose shortcuts where the mouse user already looks (menu rows, tooltips) and, after someone has repeatedly done an action with the mouse, show one short non-blocking tip naming the key right after the action completes; keep a single, consistent shortcut per action across the product.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| right-aligned | shortcut label in each menu row | caption rule 1 |
| 500 ms | tooltip show delay; tooltip repeats the same key as the menu | caption rule 2 |
| 3 mouse uses | threshold before the shortcut tip is shown; never on the first use | caption rule 3 |
| 1 tip | shown once, quiet (non-blocking) | caption rule 3 |
| 1 shortcut per action | same binding everywhere | caption rule 4 |
| E | sample shortcut for Archive in the tip | video slide |
| about 3 s | tip visible time on the video slide (0:00.5 to about 0:03) | video slide (measured from frames, approximate) |
| 4 / 6 | slide position | video slide footer |

## Before / after
- **Tip before vs after the action (video slide).** Good: the user archives an invoice with the mouse; a small toast confirms Archived INV-2039 and adds Next time, press E, with a keyboard icon. Why: the tip arrives when the action is fresh and the result is visible, so the key is linked to the outcome; it does not interrupt the task in progress.
- **First-use tip vs after 3 uses (caption only).** Bad: a tip on the first click, before the user knows if they will repeat the action. Good: only after 3 mouse uses, once. Why: repetition shows the action is frequent enough to be worth a shortcut; a single tip avoids nagging.
- **Shortcuts hidden vs printed in menus (caption only).** Good: every menu item shows its key at the right edge, and the tooltip for the same toolbar button shows the same key after 500 ms. Why: repeated passive exposure in the exact place of the mouse action is how users learn bindings.

## Do
- Right-align shortcut hints in menu rows, in a muted style, using the platform's modifier symbols (Cmd on macOS, Ctrl elsewhere).
- Delay tooltips (about 500 ms) and show the same shortcut text as the menu.
- Count mouse uses per action; after the third, show one brief tip after the action succeeds, then stop.
- Keep one binding per action across views, menus, command palette and docs.
- Let users see all shortcuts in one place (a shortcut sheet, often on `?`).

## Don't
- Don't show the tip on first use or every time.
- Don't use modal dialogs or blocking coachmarks for shortcut tips.
- Don't assign different keys to the same action in different screens, or the same key to different actions.
- Don't advertise a shortcut that is not available in the current context.

## Slide by slide
The carousel has 6 slides. Only slide 4 (animated) was available; the other image slides were not downloaded, so the list is reconstructed from the caption with the order assumed.
- Slide 1 (not seen): cover/hook.
- Slides 2 and 3 (not seen): presumably right-aligned keys in menus; tooltips after 500 ms with the same keys.
- Slide 4 (seen, animated): headline about teaching the key right after the click; post-action tip. Matches caption rule 3.
- Slide 5 (not seen): presumably one shortcut per action, the same everywhere.
- Slide 6 (not seen): likely closing/save slide.

## Video slide
Slide 4, about 4.5 s loop. Sub-headline: the action is done, the tip is short, and it names one key. Panel titled Orbit with invoice rows INV-2041 $1,240, INV-2040 $860, INV-2039 $415 (selected: accent bar and icon), INV-2038 $2,100.
- 0:00 List only.
- 0:00.5 A toast appears under the list: Archived INV-2039, second line Next time, press E, keyboard icon in the accent colour.
- 0:01-0:03 The toast stays still.
- 0:03-0:03.5 The toast leaves; the list returns to its initial state (loop).

## Notes for the skill
- WCAG 2.1.4 Character Key Shortcuts: a single-letter shortcut like E must be possible to turn off or remap, or be active only when the relevant component has focus; otherwise speech-input and keyboard users trigger it by accident. Prefer scoping single keys to the focused list, or offer a setting.
- Tooltips: WCAG 1.4.13 requires hover/focus content to be dismissible (Esc), hoverable and persistent; tooltips must also appear on keyboard focus, not only on hover. The 500 ms delay applies to hover; on focus a shorter delay or none is fine.
- Expose shortcuts to assistive tech with `aria-keyshortcuts` on the control; in menus also keep the visible hint text.
- The tip is a status message: announce via `role="status"` (polite live region), never move focus to it. If it auto-dismisses, about 3 s as shown is short for reading two lines; consider 5 s or more and pause on hover/focus (WCAG 2.2.1 applies to time limits on interaction; a purely informational tip is lower risk but should still be readable).
- Persist the per-action counter and the shown-once flag (per user, not per session) so the tip truly appears once.
- Avoid binding keys that browsers or screen readers already use (e.g. single letters in browse mode, Ctrl+L, Ctrl+T).
- Archiving should offer Undo in the same toast if it removes the item from view; the sample keeps the row in the list.
