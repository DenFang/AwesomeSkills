---
id: DY9avLYtAri
reel_url: https://www.instagram.com/reel/DY9avLYtAri/
pattern_page: https://designmotionhq.com/patterns/toggle-anatomy
date: 2026-05-30
duration_s: 41
type: ui
category: forms
topic: toggle switch anatomy (proportions, 4-property morph, keyboard/ARIA, optimistic async state)
sources: frames, voice-over, pattern page
---

# Toggle anatomy: proportions, morph, accessibility, async state

**Caption:** Toggles UX deserve all those rules
**Hook:** Two toggles side by side: one snaps between states, the other morphs, and the morphing one feels like a real control.

## Main rule
Build a switch with stable proportions (track about twice as wide as it is tall, knob inset evenly), animate the state change by morphing track colour, knob position, knob shadow and label together over about 250 ms with ease-out, make it a real switch for keyboard and screen readers (Space toggles, visible focus ring, `role="switch"` + `aria-checked`), and for server-backed settings flip immediately, show a spinner inside the knob while pending, and roll back with an error message if the request fails.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| Rail width 600px | demo track width | 0:04-0:09 on-screen |
| Knob 260px | demo knob diameter (dimension line drawn along the full track height) | 0:05-0:09 on-screen |
| Padding 20px | inset between knob and track edge | 0:06-0:09 on-screen |
| "Width = 2x knob", "Padding = knob radius" | stated proportion rules (`rail = 2x knob · pad = knob radius`) | 0:03-0:09 on-screen + voice + page |
| 4 properties | rail colour (neutral -> accent), knob slide (translateX), knob shadow (soft -> glow), label (OFF -> ON) | 0:10-0:19 on-screen + voice + page |
| 250ms, ease-out | duration and easing of the morph | 0:10-0:19 on-screen + voice; page says "~250ms" |
| Space | key that toggles a focused switch | 0:20-0:27 on-screen + voice |
| `aria-checked` | attribute announced by the screen reader | 0:23-0:27 on-screen + voice |
| POST /api/settings `{ notifications: true }` | demo request; fails with "500 Internal Server Error" | 0:30-0:35 on-screen |
| "Couldn't save, try again" | rollback toast text | 0:33-0:36 on-screen |

Proportion check: the on-screen numbers do not satisfy the on-screen rules. 2 x 260 = 520, not 600, and the knob radius is 130px, not 20px. What the numbers do satisfy: track height = knob + 2 x padding = 260 + 40 = 300px, and track width = 2 x track height (600 = 2 x 300). So the usable rules are "track width = 2 x track height" and "equal inset on all sides", with the knob travel = width - height = 300px. Treat the slogans "2x knob" and "padding = knob radius" as wrong as stated.

## Before / after
1. **Snap vs morph (0:00-0:03).** Left switch ("Snap") jumps between off and on instantly; right switch ("Morph") slides the knob and blends the track to the accent colour. Why: continuous motion shows where the state came from and where it went, so the change is legible and feels physical; an instant jump can be missed or read as a glitch.
2. **Proportions (0:03-0:09).** A large on-state switch with dimension lines: rail width 600px, knob 260px, padding 20px, caption "rail = 2x knob · pad = knob radius". Why (claimed): fixed ratios keep the knob visually anchored and centred in both states. See the proportion check above for the corrected rule.
3. **Four-property morph (0:10-0:19).** A "Notifications" switch toggles repeatedly; four chips light up as each property animates: Rail color (neutral -> accent), Knob slide (translateX), Knob shadow (soft -> glow), Label (OFF -> ON), with a "250ms · ease-out" tag. Why: all channels change together, so the state reads as one coherent event; ease-out gives an immediate start (responsive) and a soft landing.
4. **Accessibility (0:20-0:27).** A "Space" key cap triggers the switch, then a focus ring appears around the track, then a screen-reader callout shows `aria-checked=` being read. Chips: Space, Focus ring, aria-checked. Voice: skip these and it is a fake button; real switches work without a mouse.
5. **Optimistic async (0:28-0:36).** Client switch flips to on immediately and its knob shows a spinner; a server panel shows `POST /api/settings`, "pending...", "awaiting response...". The server returns 500; the switch slides back to off and a toast "Couldn't save, try again" appears. Why: the user gets instant feedback, the spinner says the change is not yet saved, and the rollback keeps the UI truthful.

## Do
- Keep the track a stadium shape with width about 2 x height and the same inset around the knob in both states.
- Animate track colour, knob translateX, knob shadow and the on/off label together, about 250 ms, ease-out.
- Use a native checkbox styled as a switch or an element with `role="switch"` and `aria-checked="true|false"`, focusable, toggled by Space (Enter optional), with a visible focus ring.
- Pair the switch with a visible label ("Notifications") that is programmatically associated.
- For server-backed toggles: flip on click, show a pending indicator inside the knob, disable repeat input or queue it, roll back and show an actionable error on failure.

## Don't
- Don't snap the knob instantly between positions (unless the user prefers reduced motion).
- Don't animate the four properties in sequence or with different durations so they drift apart.
- Don't build the switch from a non-focusable `div` that only reacts to mouse clicks.
- Don't leave a pending server toggle looking finished; and don't leave a failed one showing the new state.
- Don't rely on track colour alone to show on/off.

## Scene by scene
- 0:00 "Hook": two switches labelled Snap and Morph toggle side by side; caption "Two toggles. One snaps. One morphs."
- 0:03 "Anatomy / Width = 2x knob. Padding = knob radius.": a large on-state switch; dimension lines appear one by one: rail width 600px, knob 260px, padding 20px; code-style caption `rail = 2x knob · pad = knob radius`.
- 0:10 "The transition / Don't snap. Morph 4 properties.": a "Notifications" switch toggles off/on several times; chips Rail color (neutral -> accent), Knob slide (translateX), Knob shadow (soft -> glow), Label (OFF -> ON) highlight in turn; tag "250ms · ease-out". Mid-transition frames show the track colour partly blended and the label crossfading.
- 0:20 "Accessibility / Space toggles. Focus rings. ARIA reads.": a "Space" key cap fires and the switch turns on; a focus ring outlines the track; a "Screen reader: aria-checked=..." callout slides in; chips Space, Focus ring, aria-checked light up.
- 0:28 "Loading state / Flip first. Spinner in the knob. Roll back if it fails.": client switch flips on with a spinner in the knob; server card `POST /api/settings {notifications: true}` "pending... awaiting response...".
- 0:32 Server card turns to error "500 Internal Server Error"; the switch slides back to off; toast "Couldn't save, try again".
- 0:37 End card with small background toggles: follow / save call to action.

## Voice-over summary
- Two toggles: one snaps, one morphs.
- Rail width should be twice the knob diameter and the padding equal to the knob radius, so the knob feels anchored (the on-screen numbers contradict this; see Notes).
- Do not snap: morph rail colour, knob slide, knob shadow and label crossfade together in 250 ms with ease-out.
- Space toggles, a focus ring is visible, and ARIA announces the state change; without these it is a fake button, and real switches work without a mouse.
- Flip first, spin in the knob, and if the server says no, roll back, so the user never waits for the network.

## Notes for the skill
- Markup: `<button role="switch" aria-checked="false" aria-labelledby="lbl">` or `<input type="checkbox" role="switch">` (native checkbox already toggles on Space and works with `<label>`). The WAI-ARIA APG switch pattern requires Space; Enter is optional. Update `aria-checked` immediately with the optimistic state; while pending, `aria-busy="true"` on the switch is acceptable, and announce the rollback via a polite live region (the toast should use `role="status"` or `role="alert"`).
- Do not change the label text meaning ("Notifications" stays; the state is in `aria-checked`). The ON/OFF text inside the track is a useful non-colour cue (WCAG 1.4.1); alternatively an I/O glyph or a check icon in the knob.
- Contrast: the track boundary in the off state and the knob against the track need at least 3:1 against adjacent colours (WCAG 1.4.11); dark-mode off tracks often fail this.
- Size: if the switch is the touch target, make the hit area at least 44x44 pt / 48x48 dp (WCAG 2.5.8 minimum 24x24 CSS px); the visual track can be smaller than the hit area.
- CSS: transition `background-color, transform, box-shadow, opacity` with one shared duration (250 ms) and `ease-out` (e.g. `cubic-bezier(0.2, 0, 0, 1)`); animate the knob with `transform: translateX(calc(var(--w) - var(--h)))`, never `left`. Under `prefers-reduced-motion: reduce`, set duration to 0 or a very short fade.
- Proportion slogans are wrong as stated (see the table): use width = 2 x height and knob diameter = height - 2 x inset. Platform switches differ (iOS UISwitch about 51x31 pt, Material 3 about 52x32 dp with a knob that grows when on), so follow the design system's token rather than a fixed ratio.
- The pattern page mentions a shake on rollback; frames at 1 fps do not show a shake clearly, only the knob sliding back and a toast. If a shake is used, keep it small and disable it under reduced motion.
- Optimistic toggles are appropriate for preferences; for consequential settings (billing, security, data deletion) confirm with the server first or ask for confirmation.
