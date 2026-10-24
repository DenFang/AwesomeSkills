---
lesson: 057
kind: video
duration_s: 50
type: ui
category: interaction
topic: filter chips as a system
sources: frames, voice-over, lesson notes
---

# Filter chips: three states, OR/AND logic, live count, clear-all, one scrolling row

**Hook:** Three taps take a catalogue from about 200 results down to a dozen; every one of those taps has to be visible and reversible.

## Main rule
Each chip needs distinct idle / active / disabled states; combine OR within a group and AND across groups; update the result count in the same frame as the tap; always offer one clear-all; keep overflowing chips in one horizontally scrolling row with an edge fade; pin active filters above the results.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 200 results -> 12 left after 3 taps | hook | voice 0:00 |
| 172 -> 17 results with 3 active chips | hook (count mid-animation on screen) | 0:00-0:01 on-screen; differs from voice |
| 3 states: Idle, Active, Disabled | chip states | 0:02-0:09 |
| Color: 1 chip -> 58 "wider", 2 chips -> 98 "wider"; + Size (Medium) -> 31 "tighter" | OR within a group, AND across groups | 0:10-0:15 |
| 120 -> 48 -> 19 results, label "same frame" | count update per tap | 0:15-0:22 |
| "No count change = users tap twice" | bad example (tap on a chip, count does not move) | 0:21-0:22 |
| 2 -> 4 filters, then 0 after Clear all | clear-all with filter count | 0:23-0:30 |
| 10 chips | overflow case on a phone | 0:31-0:39 voice + title |
| wall: 4 rows of chips; 2 results visible vs single row: 6 results visible | wrap vs horizontal scroll | 0:32-0:39 frames |
| 3 results with 3 pinned active filters | sticky active-filter bar | 0:40-0:45 |

## Before / after
- **Active looks like idle vs three distinct states.** Bad: selected and unselected chips look nearly the same, so users cannot tell if the filter applied. Good: Idle = surface + border (tappable, not chosen); Active = accent fill + check icon; Disabled = dimmed, used when no results sit behind that option. Why: state must be readable at a glance and not only by colour (the check carries it too).
- **Unclear logic vs OR-within / AND-across.** Good: adding a second colour widens the set (58 -> 98, label "wider"); adding a size narrows it (98 -> 31, "tighter"). Why: matches user mental model of facets; the wider/tighter hint makes the logic visible.
- **Silent tap vs same-frame count.** Bad: tapping "Mesh back" leaves the count unchanged, so users think nothing happened and tap again (toggling it off). Good: count changes on the same frame as the chip state (120 -> 48 -> 19). Why: immediate feedback confirms the action; delay or silence triggers repeated taps.
- **Trapped in stacked filters vs one clear-all.** Good: header shows "N filters" plus a single "Clear all"; one tap returns to 0 filters and the button goes inactive. Why: a single escape hatch; the count tells users what will be wiped.
- **Wall of chips vs one scrolling row.** Bad: 10 chips wrap into 4 rows and push results down (2 visible). Good: one horizontal row, right edge fades (and a chip is cut off) to hint more; 6 results stay visible. Why: results are the goal; partial visibility affords scrolling.
- **Hidden active filters vs pinned summary.** Good: a sticky "Active filters" bar with removable chips and the result count sits above the grid, so users see why the list shrank; non-matching cards fade out.

## Do
- Design idle, active (fill + check) and disabled (dimmed, zero results) states.
- OR inside a facet group, AND across groups; show whether a tap widened or narrowed results.
- Update the result count synchronously with the chip toggle.
- Provide one Clear all next to an active-filter count.
- Use a single horizontal scroll row with an edge fade when chips overflow; pin active filters on top.

## Don't
- Don't let active and idle chips look alike.
- Don't leave the count unchanged after a tap.
- Don't wrap many chips into a multi-row wall above the results.
- Don't hide which filters are applied once the user scrolls.

## Scene by scene
- 0:00 Product grid (chairs) with count and three chips; tapping all three drops the count to 17 and dims non-matching cards.
- 0:02 "One chip, three states": Idle (surface + border, tappable, not chosen), Active (fill + check, clearly selected), Disabled (dimmed, no results behind it). Footer: if active looks like idle, the filter feels broken.
- 0:10 "How chips combine": Color group (OR within) and Size group (AND across); counts 58 wider, 98 wider, 31 tighter; chips "Or within a group", "And across groups"; footer: more chips in one group widen the net, a new group narrows it.
- 0:15 "Every tap needs an answer": two chips, count 120 -> 48 -> 19 with a "same frame" marker; at 0:21 a bad-example strip: tapping "Mesh back" with "No count change = users tap twice".
- 0:23 "One clear-all, always": header "2 filters" then "4 filters" with removable chips and "Clear all"; tap resets to "0 filters", chips go idle. "Stacked filters trap users." / "Reset in one tap."
- 0:31 "10 chips, one phone": two phones, "Wraps into a wall" (buries the results) vs "One scrolling row" (edge fade hints more), the row scrolls sideways.
- 0:40 "Pin active filters on top": sticky "Active filters" bar with 3 chips and "3 results", hint "why the list shrank", grid filters down.
- 0:46 Outro: chip row Idle / Active / Disabled / Clear all, "Filters are a system.", follow and save.

## Voice-over summary
- A chip lives in three states: idle, active, disabled; if active looks like idle the filter feels broken.
- Two colours grow results, adding a size shrinks them: OR inside a group, AND across groups.
- Update the result count the moment a chip flips; "Silence makes users tap twice."
- Stacked filters trap people; one clear-all resets, paired with a count so users know what it wipes.
- Ten chips never fit a phone: one sideways row with a faded edge; a wrapped wall buries results.
- Keep active filters pinned on top so users see why the list shrank.

## Notes for the skill
- ARIA: a toggle chip is a `<button aria-pressed="true|false">`; a group of mutually exclusive chips is a radio group; multi-select facets can be checkboxes styled as chips. Disabled options: prefer `aria-disabled="true"` with an explanation (e.g. "0 results") so they stay discoverable, or show the zero count in the label.
- State must not rely on colour alone (WCAG 1.4.1): the check icon or a weight/border change is required; active chip contrast against its fill 4.5:1 for text, chip boundary 3:1 against the background.
- Live count: announce changes via a polite live region (`aria-live="polite"`) with debounce so screen readers are not flooded on rapid taps. If results come from a server, update the chip immediately and show a pending state on the count rather than freezing the old number.
- Horizontal scroll row: `overflow-x: auto; scroll-snap-type: x proximity;` mask-image gradient for the fade; keep it keyboard reachable (chips are buttons in tab order) and ensure the last chip is not permanently under the fade (add end padding). Touch targets at least 44x44 pt (iOS) / 48dp (Android), WCAG 2.2 minimum 24x24 CSS px.
- Clear all should be disabled or hidden at 0 filters (shown in the video) and focus should move to a sensible place (the result count or first chip) after reset.
- The hook numbers differ between voice (200 -> 12) and screen (172 -> 17); the screen count is captured mid-animation.
