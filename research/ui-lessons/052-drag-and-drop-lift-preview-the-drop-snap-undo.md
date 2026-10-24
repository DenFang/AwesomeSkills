---
lesson: 052
kind: video
duration_s: 42
type: ui
category: interaction
topic: drag and drop (pickup signals, drop-zone preview, snap vs free, undo)
sources: frames, voice-over, lesson notes
---

# Drag and drop: lift, preview the drop, snap, undo

**Hook:** Grab a card and the board does the thinking: moving a card is moving state.

## Main rule
A drag needs four things: an unmistakable pickup state (cursor change + lift + visual separation), a drop target that is previewed before release (insertion line between items, fill highlight for a whole container), snapping on structured surfaces (free placement only on canvases), and an undo toast of about 5 seconds after every drop.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 3 signals | pickup feedback: cursor changes, card lifts, background fades | 0:03-0:10 on-screen chips + voice |
| 5 seconds | undo window after a drop | 0:30-0:36 on-screen title "Five seconds to undo" + voice; page says "~5 seconds" |
| 2 drop-zone cues | between items → line; whole column → fill | 0:11-0:18 on-screen chip |
| card tilt, scale | lifted card is rotated by a few degrees and slightly enlarged | 0:07-0:10 visual only; exact angle and scale not labelled (estimate about 2-3°) |

## Before / after
1. **Pickup (0:03-0:10).** Before: the card under an open-hand cursor stays flat; the voice-over says that with no signal the drag "feels stuck". After: three simultaneous cues: cursor switches from open hand to closed hand, the card tilts, scales up and gains a deeper shadow, and the rest of the scene fades back. Why it works: redundant cues confirm the state change instantly (the user knows the system has the object before moving), and the lift metaphor tells the user the item is detached from the layout and will follow the pointer. The page names the trio as scale, shadow and tilt.
2. **Drop preview (0:11-0:19).** Before (stated): no preview means a "blind drop": the user only learns where the item landed after letting go. After: while hovering, the target answers first. Between two cards an insertion line appears in the gap; over a whole column the column fills with a highlight and an empty dashed slot. Why it works: the user can correct the target before committing; the shape of the cue matches the scope of the result (line = exact position among siblings, fill = "into this container").
3. **Snap vs free (0:19-0:28).** Side by side: KANBAN (tag SNAP) shows dashed target slots during the drag and the card snaps into a slot; CANVAS (tag FREE) on a grid lets the card land at any coordinate. Why: on a structured list only some positions are valid, so snapping removes pixel-precision work and invalid states; on a canvas every coordinate is meaningful, so snapping would fight the user. "Pick the wrong one and users fight your UI."
4. **Undo (0:30-0:36).** A drop lands the card in Done; a toast appears: "Moved to Done / Tap Undo to send it back", with an UNDO button wrapped in a circular countdown ring. The user taps Undo and the card returns to In Progress. Why it works: drags are easy to fumble; a short, visible undo makes a mistake cost one click and removes the need for confirmation dialogs.

## Do
- Change the cursor on hover (open hand) and on press (closed hand).
- On pickup, apply scale-up, deeper shadow and a small tilt together, and dim or fade the surroundings.
- Show the landing spot during the drag: an insertion line between siblings, a filled highlight with a placeholder slot for a whole container.
- Snap to valid slots on lists, boards and grids; show those slots (dashed outlines) while dragging.
- After the drop, show a toast with a past-tense result ("Moved to Done") and an Undo action for about 5 seconds, with visible time remaining.

## Don't
- Don't move the item with no lift or shadow; it feels like nothing happened.
- Don't reveal the destination only after release.
- Don't require pixel-precise placement on a structured surface.
- Don't snap on a free canvas.
- Don't make a drop irreversible.

## Scene by scene
- 0:00 Kanban board (TODO / IN PROGRESS / DONE) with task cards; a card "Design review" is dragged into DONE, which fills with a highlight; it lands there. Title "The board does the thinking."
- 0:03 "PICK UP / Three signals. One grab.": a single enlarged card with an open-hand cursor, flat.
- 0:07 Pressed: closed-hand cursor, card tilts and lifts; chips appear one by one: Cursor changes, Card lifts, Background fades.
- 0:09 Caption chip: Three signals = "I'm holding this".
- 0:11 "DROP ZONES / Drop zones speak first."; chip "Between items → line • Whole column → fill". Dragged card hovers DONE (column fill); in TODO an insertion line shows between two cards.
- 0:18 Split view: COLUMN FILL (highlighted column with dashed empty slot) vs INSERTION LINE (line between two cards); footer "No preview = blind drop."
- 0:19 "SNAP OR FREE / Snap matches structure. Free matches canvas.": KANBAN (SNAP) panel shows dashed slots and the card snapping; CANVAS (FREE) panel on a grid where the card drops anywhere. Footer "Structured? Snap. | Canvas? Free." The demo loops twice.
- 0:29 Board alone.
- 0:30 "UNDO / Bad drop. Toast. Five seconds to undo.": the card has moved to Done; toast "Moved to Done / Tap Undo to send it back" with a ringed UNDO button.
- 0:35 Undo pressed; toast fades; the card is back in IN PROGRESS.
- 0:37 "Follow for more interaction patterns. / Save this for your next board." and a Follow button.

## Voice-over summary
- Picking up a card should produce three signals at once: cursor change, card lift, background fade; without them the drag feels stuck.
- "Drop zones speak first": hovering between items shows an insertion line, hovering a zone fills it; no preview means a blind drop.
- Kanban snaps to columns, Figma-style canvases drop anywhere: snap for structured lists, free for canvas, otherwise users fight the UI.
- Mistaken drops happen: show a toast with Undo, and give five seconds to take it back.

## Notes for the skill
- CSS states: `cursor: grab` on draggable handles, `cursor: grabbing` while dragging; lifted item e.g. `transform: scale(1.03) rotate(2deg)` plus a larger shadow token (exact values are not given in the video; these are typical). Animate pickup quickly (about 150-200 ms) and disable tilt/scale under `prefers-reduced-motion`, keeping the shadow/outline cue.
- Keep the original slot as a placeholder (ghost) so the layout does not jump, and animate siblings making room.
- Accessibility (missing from the video): drag and drop must have a non-pointer alternative. WCAG 2.2 SC 2.5.7 Dragging Movements (AA) requires a single-pointer way to do the same thing (e.g. a "Move to..." menu or up/down buttons). Provide keyboard support (Space/Enter to pick up, arrows to move, Space/Enter to drop, Escape to cancel) and announce pickup, position and drop through an `aria-live` region; `aria-grabbed`/`aria-dropeffect` are deprecated and should not be relied on.
- Escape during a drag should cancel and return the item to its origin.
- Touch: start a drag after a long press (to avoid conflicts with scrolling) and auto-scroll the container near edges.
- Undo toast: keep it on screen while hovered or focused (WCAG 2.2.1 Timing Adjustable applies to time limits), make the Undo button keyboard reachable, and announce the toast politely (`role="status"`). Five seconds is short for screen-reader users; consider a longer timeout or a persistent history.
- The "background fades" cue is not clearly isolated on screen at 540px; the lifted card itself also looks slightly translucent. Treat the third cue as "separate the dragged item from its surroundings" (dim the rest or make the item visually float).
