---
id: DUDy5gNDBVM
reel_url: https://www.instagram.com/reel/DUDy5gNDBVM/
pattern_page: none
date: 2026-01-28
duration_s: 46
type: ui
category: motion
topic: three micro-interaction basics: easing, feedback, anticipation
sources: frames, voice-over, caption
---

# Easing, feedback and anticipation make a control feel good

**Caption:** Hashtags only (motion graphic, design studio, motion); no text caption.
**Hook:** A toggle that "feels good" is not luck: it is a set of small motion details you sense but do not consciously notice.

## Main rule
Every interactive control needs three things: non-linear easing (ease-out for motion that responds to the user), immediate visible feedback that the action registered, and a short anticipation beat (a small squash or wind-up) before a bigger move. Combine all three on the primary action of a flow.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 3 | number of "secrets" (easing, feedback, anticipation) | 0:12-0:37 on-screen labels "SECRET 1/2/3" + voice |
| 1937 | year cited for Disney's anticipation principle (illustrative, not a UI value) | 0:26 on-screen subtitle + voice |
| $249.00 | demo amount in the combined payment card (content, not a design value) | 0:37-0:40 on-screen |

No durations, easing curves or other numeric UI values are shown.

## Before / after
- **Linear vs ease-out (0:12-0:19).** Two squares slide along tracks; the top one (label "LINEAR", caption "Robotic") moves at constant speed, the bottom one ("EASE OUT", caption "Alive") pulls ahead early and settles into the end. A small progress-vs-time graph under each draws the curve. Why: real objects decelerate as they come to rest; constant velocity with abrupt start and stop reads as mechanical, while a fast start answers the input immediately and a soft landing reads as physical.
- **No response vs ripple (0:22-0:29).** Two "Submit" buttons side by side. Left ("NO RESPONSE"): nothing happens on tap, caption "...hello?". Right ("WITH RIPPLE"): the button shows a press effect and a confirmation line "Confirmed!" in the success colour appears below. Why: without a visible state change the user cannot tell whether the tap registered, so they wait, doubt, or tap again; immediate feedback closes the action-perception loop.
- **No prep vs squash (0:29-0:36).** Two character tiles. Left ("NO PREP", caption "Flat. Lifeless.") moves without preparation; right ("SQUASH", caption "Satisfying.") compresses before it moves. Why: a short preparatory squash tells the eye a motion is coming and gives it weight, so the following move reads as intentional rather than sudden. (The squash itself is not visible at 1 frame per second; inferred from labels and voice.)

## Do
- Use ease-out (fast start, slow end) for elements that respond to user input or enter the screen.
- Give every tap an immediate visible response: a pressed state, ripple or scale, then a clear result state (e.g. a check mark or "Confirmed").
- Add a brief anticipation beat (slight squash or pull-back) before larger or playful motions.
- Layer all three on the key action: in the demo, "Send Payment" uses easing, a press, then morphs into a full-width success-state button with a check mark.

## Don't
- Don't animate UI with linear timing for position or scale changes.
- Don't leave a button silent after a tap ("silence equals anxiety").
- Don't start a large movement from a dead stop with no preparation when the motion is meant to feel physical.

## Scene by scene
- 0:00 Dark screen; a toggle switch flips from off to on; small floating icon tiles (mini toggle, spinner, heart, check) drift around it. Text builds: "This button feels good." / "That's not an accident." / "It's design." (last line in the accent colour).
- 0:04 Header "The details you feel but never see". A card cycles through micro-interaction demos, each with a label: "Button Pulse" (Subscribe button pulses), "Notification" (a toast "Changes saved!" slides in and gains a check icon), "Toggle Switch" (off to on), "Instant Feedback" (heart grows, then a success check appears next to it).
- 0:12 "SECRET 1 / EASING / Why cheap apps feel... off". Two tracks with squares: "LINEAR" (muted) vs "EASE OUT" (accent). Graphs below labelled "Robotic" and "Alive" redraw on each loop.
- 0:20 "SECRET 2 / FEEDBACK / Silence = anxiety". Split view: "NO RESPONSE" grey Submit with "...hello?" vs "WITH RIPPLE" accent Submit with "Confirmed!" in the success colour.
- 0:28 "SECRET 3 / ANTICIPATION / Disney knew this in 1937". Split view: "NO PREP" grey face tile, caption "Flat. Lifeless." vs "SQUASH" accent face tile with glow, caption "Satisfying."
- 0:37 "Now watch them work together": a "Payment Details" card (Amount $249.00, To Alex Johnson). The "Send Payment" button is pressed (ripple), then turns into a success-coloured button with a check mark and glow. Tags light up one by one under the card: "Easing", "Anticipation", "Feedback".
- 0:41 "Without them, an app feels dead." then "With them, it breathes." (accent).
- 0:43 Outro "Want more UI secrets? Follow for daily tips" with a Follow button.

## Voice-over summary
- A pleasant-feeling button is the result of deliberate design details users feel but do not see.
- Tiny moments such as a pulse, slide or snap decide whether an app feels good.
- Linear motion feels robotic; ease-out feels alive, and its absence is why cheap apps feel off.
- Feedback: silence after a tap creates anxiety; the user must know the action worked.
- Anticipation, a Disney animation principle: squash before the bounce.
- Combined, the three make an app feel like it "breathes".

## Notes for the skill
- CSS: for responsive or entering motion use an ease-out curve such as `cubic-bezier(0.22, 1, 0.36, 1)` or `ease-out`; reserve `linear` for continuous loops (spinners, progress) and opacity cross-fades of very short length. The reel gives no durations; typical micro-interaction ranges are 100-200 ms for press feedback and 200-300 ms for small transitions.
- Visual inconsistency in the reel: the "Alive / EASE OUT" graph drawn at 0:13 is concave upward (slow start, fast finish), which is the shape of an ease-in progress curve. The moving square does behave like ease-out (it leads early). Trust the rule, not the drawn graph: an ease-out curve rises steeply at the start and flattens at the end.
- Feedback states: model the button as idle, pressed, pending, success, error. Show press feedback within about 100 ms of input; announce the result to assistive tech (e.g. `aria-live="polite"` region for "Confirmed" or the success label), because a colour/check morph alone is not perceivable by screen-reader users and a check icon replacing the label removes the accessible name unless `aria-label` is kept.
- Success-colour button with only an icon: keep text contrast and give the button an accessible label; do not rely on colour alone to say "done".
- Anticipation and bounce are decorative: wrap them in `@media (prefers-reduced-motion: reduce)` and drop squash/bounce or replace with a plain fade. Keep anticipation short so it never delays the response to input; for a tap, the wind-up must not postpone visible feedback.
- Ripple is a Material-style choice; any immediate state change (scale to ~0.97, background shift) satisfies the same rule.
