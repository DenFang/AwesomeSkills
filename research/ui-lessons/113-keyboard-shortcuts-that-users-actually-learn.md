---
lesson: 113
kind: carousel
type: ui
category: interaction
topic: teaching keyboard shortcuts (keys in menus, same key in tooltip, post-action tip after 3 mouse uses)
sources: image slides 1-3 and 5-6, video slide (slide 4 of 6)
---

# Keyboard shortcuts that users actually learn

**Hook (slide 1):** "Nobody learns shortcuts you never show", over an action menu with no key hints at all.

## Slide by slide
- **Slide 1 (cover, bad example).** Sample app window titled Orbit, breadcrumb Invoices / INV-2041, page title INV-2041. An action menu lists Duplicate, Rename, Move to, Archive, Delete, each with an icon and a label only. A dashed outline in the danger colour wraps the whole menu, with a danger tag reading No key anywhere. Table headers Qty and Total peek out below.
- **Slide 2 (Save this: three values).** Headline: three values that make shortcuts stick. Left, a mock panel (Orbit) with three stacked examples, each connected by a leader line to a number:
  - A menu: Duplicate `Cmd D`, Rename `R`, Archive `E`. Keys are right-aligned in muted text; the Archive row is the selected one (accent bar on the left edge, raised row background, accent icon). Callout: **1** key per action, in the menu.
  - A toolbar button Archive (icon plus label). Callout: **500 ms** hover delay before the hint.
  - A toast with a keyboard icon in the accent colour, title Archived, second line Next time, press E in muted text. Callout: **3** mouse uses before one tip, never on the first click.
- **Slide 3 (five checks before you ship shortcuts).** Three passes (check marks in the accent colour) and two fails (cross marks in the danger colour):
  - Pass: every menu row shows its keys.
  - Pass: menu and tooltip name the same keys.
  - Pass: single keys stay off while typing.
  - Fail: shortcuts listed only on a help page.
  - Fail: a tip popping up on every click.
- **Slide 4 (video, about 4.5 s loop).** Headline: teach the key right after the click. See Video slide.
- **Slide 5 (Save this: three numbers for hints).** **500 ms** hover delay, then the tooltip shows. **3** mouse uses before a single tip. **1** key per action, the same in menu and tooltip.

## Main rule
Show each action's shortcut where the mouse user already looks: right-aligned in the menu row and, after a 500 ms hover, in the tooltip of the same control, with the identical key in both places. After a user has done the same action with the mouse 3 times, show one short, non-blocking tip naming the key right after the action completes, then never again. Single-key shortcuts must not fire while the user is typing in a field.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 1 key per action | same binding in the menu row and in the tooltip | slides 2, 5 |
| right-aligned, muted | key hint position and style inside a menu row | slide 2 |
| `Cmd D`, `R`, `E` | sample bindings: Duplicate, Rename, Archive | slide 2 |
| 500 ms | hover delay before the tooltip (with the key) shows | slides 2, 5; caption |
| 3 mouse uses | threshold before the shortcut tip; never on the first click | slides 2, 5; caption |
| 1 tip | shown a single time per action | slide 5 |
| single keys off while typing | single-letter shortcuts disabled when focus is in a text field | slide 3 |
| 2 lines | tip content: result line (Archived INV-2039) and key line (Next time, press E) | slides 2, 4 |
| about 2.5 to 3 s | tip visible on the video slide (present in frames 0:00.5 to 0:03, gone at 0:03.5) | slide 4 (measured at 2 fps, approximate) |

## Before / after
- **No keys vs keys in every row (slides 1 and 2).** Bad: the action menu shows labels only, so the shortcut exists nowhere the user looks. Good: each row ends with its key, right-aligned and muted. Why: the user reads the menu every time they use the mouse, so the key is seen at the exact moment of the action, many times, at no cost to the task; muting it keeps the label as the primary read.
- **Help page vs in place (slide 3).** Bad: shortcuts documented only on a help page. Good: in menu rows and tooltips. Why: people rarely open help for speed-ups; learning happens through passive repetition in context, not a separate lookup.
- **Different hints vs one key everywhere (slides 3, 5).** Good: the menu row and the toolbar tooltip for Archive both say `E`. Why: one action, one binding, so every exposure reinforces the same mapping; two different keys for one action cancel each other out.
- **Tip on every click vs one tip after 3 uses (slides 2, 3, 5).** Bad: a tip on each click, or on the first one. Good: one tip after the third mouse use. Why: three repetitions prove the action is frequent enough for a shortcut to pay off; a single tip respects the user and does not train them to dismiss tips.
- **Tip before vs after the action (slide 4).** Good: the toast appears once the archive has happened, leads with the result (Archived INV-2039) and adds the single key. Why: the action is fresh and its result is visible, so the key is attached to an outcome the user just wanted; nothing interrupts the task, because the work is already done.
- **Single keys while typing (slide 3).** Good: `R` or `E` do nothing when focus is in a text input. Why: otherwise typing a word containing those letters renames or archives items by accident.

## Do
- Put the key hint at the right edge of each menu row, in muted text, using the platform modifier (Cmd on macOS, Ctrl elsewhere).
- Show the same key in the tooltip of the matching toolbar control, after about 500 ms of hover.
- Count mouse uses per action and per user; on the third, show one brief tip after the action succeeds, then set a shown flag.
- Lead the tip with the result, then the key: two short lines, one key.
- Disable single-key shortcuts whenever focus is in an input, textarea or contenteditable region.
- Keep one binding per action across menus, tooltips, command palette and docs; a shortcut sheet is fine as an extra, not as the only place.

## Don't
- Don't ship a menu with no key hints for actions that have shortcuts.
- Don't list shortcuts only on a help page.
- Don't show the tip on the first click, or on every click.
- Don't use modal dialogs or blocking coachmarks for shortcut tips.
- Don't give the same action different keys in different places, or reuse a key for different actions.
- Don't let single-letter shortcuts fire while the user types.

## Video slide
Slide 4, about 4.5 s loop. Sub-headline: the action is done, the tip is short, and it names one key. Panel titled Orbit with invoice rows INV-2041 $1,240, INV-2040 $860, INV-2039 $415 (selected: accent bar on the left edge, accent document icon, raised row background), INV-2038 $2,100.
- 0:00 List only, empty space under the rows.
- 0:00.5 A toast appears under the list inside the panel: keyboard icon in the accent colour, Archived INV-2039, second line Next time, press E in muted text.
- 0:01 to 0:03 The toast stays still.
- 0:03.5 to 0:04 The toast is gone; the list is back to its initial state (loop). The entry and exit transitions fall between frames and are not visible at 2 fps.
The archived row stays in the list in the demo; the loop only illustrates the timing of the tip.

## Notes for the skill
- WCAG 2.1.4 Character Key Shortcuts (A): the slide's check (single keys off while typing) is necessary but not enough. A single-character shortcut like `E` or `R` must also be possible to turn off or remap, or be active only while the relevant component (here the invoice list) has focus. Scoping to the focused list is the simplest compliant option.
- Key conflicts: `Cmd D` / `Ctrl D` is the bookmark shortcut in common desktop browsers, so a web app either cannot use it or overrides a familiar browser action. Avoid keys that browsers or screen readers already own (Ctrl/Cmd plus L, T, W, D; single letters in screen reader browse mode).
- Tooltips: WCAG 1.4.13 Content on Hover or Focus requires the tooltip to be dismissible (Esc) without moving focus, hoverable, and persistent until dismissed. The WAI-ARIA APG tooltip pattern also requires showing it on keyboard focus, not only on hover; the 500 ms delay is for hover, focus can show it sooner. Tooltip text like Archive (E), linked with `aria-describedby` from the control.
- Expose bindings to assistive tech with `aria-keyshortcuts` on the control or menu item, e.g. `aria-keyshortcuts="E"` or `aria-keyshortcuts="Meta+D"`; keep the visible hint text too.
- The tip is a status message (WCAG 4.1.3): put it in a polite live region (`role="status"`), never move focus to it. About 3 s on screen, as in the demo, is short for two lines; consider 5 s or more and pause the timer on hover or focus.
- Persist the per-action counter and the shown-once flag per user (not per session), or the single tip repeats on every visit.
- If archiving removes the item from view, the same toast should offer Undo; the shortcut line is secondary to that.
