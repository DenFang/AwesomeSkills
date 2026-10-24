---
id: DZUtKvIqrHo
reel_url: https://www.instagram.com/reel/DZUtKvIqrHo/
pattern_page: https://designmotionhq.com/patterns/range-sliders
date: 2026-06-08
duration_s: 48
type: ui
category: forms
topic: sliders and range sliders
sources: frames, voice-over, pattern page
---

# Range sliders: designing around imprecise dragging

**Caption:** Sliders should be done like this
**Hook:** Trying to drag to exactly 47 the readout jitters between 46, 47 and 49; a finger cannot tell 47 from 48.

## Main rule
Design sliders around imprecise pointer input: make the whole row the drag target, fill the track up to the thumb, snap to meaningful steps with visible ticks, float the exact value above the thumb while dragging, use two thumbs with a filled band for ranges, and support arrow keys (one step) and Home/End (extremes).

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 47% → 49% → 46% | jittering readout while trying to hit 47 | 0:00-0:02 on-screen; voice "47 or 48" |
| 4px | track (hairline) height that is a poor hit target ("4px track", "A 4px hairline is a moving target") | 0:03-0:09 on-screen + voice |
| full row | hit area of the good slider ("full-row hit area") | 0:03-0:09 |
| 90%, 66%, 13%, 27%, 83%, 78%, 22% | demo values on the filled slider; the unfilled twin shows only "?" | 0:10-0:16 |
| 47.3 vs 50 | continuous slider result vs stepped slider result ("Nobody wants 47.3.") | 0:17-0:21 |
| 0 / 25 / 50 / 75 / 100 | tick labels of the stepped slider (step 25 in the demo) | 0:17-0:21 |
| Volume 70, Rating 4 / 5, Price $50 | examples of discrete values; Rating track shows 6 ticks (0-5), Volume and Price show 5 ticks at quarters | 0:22-0:26 + voice "volume, ratings, price" |
| 25% → 32% → 50% → 72% → 84% → 85% | floating value bubble above the thumb during drag; disappears after release | 0:27-0:33 |
| $15 – $100, then $20 – $80 | two-thumb price range with values in chips above and labels under each thumb | 0:34-0:38 |
| 1 step per arrow key; Home = min, End = max | keyboard behaviour (keys shown: ←, →, Home, End) | 0:39-0:44 on-screen + voice |

## Before / after
1. **Hairline target vs full-row hit area.** Bad: "4px track" where the cursor repeatedly misses the line and thumb. Good: "full-row hit area" where pressing anywhere on the row starts the drag (shown as a tinted row background). Why: target acquisition time grows as targets shrink (Fitts's law); a 4px line is nearly impossible to hit by finger and frustrating by mouse.
2. **Bare track vs filled track.** Bad ("no fill"): only a thumb on a neutral track, captioned "hard to read at a glance", value shown as "?". Good ("filled"): the track left of the thumb is filled with the accent and a large value is shown ("value reads from the fill"). Why: the filled length encodes the value as a bar, so proportion is perceived pre-attentively without reading the number.
3. **Continuous vs stepped.** Bad: a continuous slider lands on 47.3 (track drawn in the danger colour). Good: a stepped slider snaps to 50 with ticks at 0, 25, 50, 75, 100. Why: most real values are discrete (volume, rating, price); snapping absorbs pointer imprecision and produces values people actually want.
4. **Blind drag vs floating value.** Good: a small bubble above the thumb shows the exact value (25%, 32%, 50% … 85%) while dragging and fades on release. Why: the value appears where the eye already is; above the thumb keeps it visible under a finger.
5. **One thumb vs two thumbs.** Good: "Price range" with two thumbs, a filled band between them, value chips "$20 – $80" and labels under each thumb. Why: a min/max filter is captured in one control instead of two separate sliders or fields.
6. **Pointer-only vs keyboard.** Good: focused slider gets a visible focus outline; → nudges one step, End jumps to the maximum, Home to the minimum. Why: keyboard and assistive-tech users need a non-drag way to set exact values; keys also give precise control to mouse users.

## Do
- Make the entire row (or at least a 44px-tall area) respond to pointer down and drag.
- Fill the track from the minimum to the thumb (between thumbs for a range).
- Snap to meaningful steps and show tick marks when values are discrete.
- Show the exact value above the thumb while dragging and also a persistent readout.
- Use two thumbs with a filled band for min/max filters.
- Support arrows (one step), Home/End (min/max) and a visible focus state.

## Don't
- Rely on a 4px hairline as the only hit target.
- Leave a slider continuous when users need round values.
- Hide the value so users drag blind.
- Ship a slider that cannot be operated with arrow keys, Home and End.

## Scene by scene
- 0:00 A large readout over a filled slider jitters 47% → 49% → 46% as the cursor drags; caption "Drag to 47. Or 48? Your finger can't tell."
- 0:03 "Make the whole row draggable. A 4px hairline is a moving target." Two cards: "4px track" (thin line, cursor misses) vs "full-row hit area" (tinted row, filled track, drag works from anywhere in the row); loops through several drags.
- 0:10 "Fill the track. The fill length is the value." Cards "no fill" (thumb only, "?", "hard to read at a glance") vs "filled" (accent fill, big value, "value reads from the fill"); both thumbs move together through 90%, 66%, 13%, 27%, 83%, 78%, 22%.
- 0:17 "Snap to steps. Nobody wants 47.3." "continuous" slider showing 47.3 vs "stepped" slider showing 50 with ticks 0/25/50/75/100.
- 0:22 Three stepped sliders with ticks: Volume 70, Rating 4 / 5, Price $50 (thumbs animate in).
- 0:27 "Float the value. Show it above the thumb while dragging." A single slider; a value bubble rides above the thumb (25% → 32% → 50% → 72% → 84% → 85%), then disappears when the drag ends at 0:30-0:33.
- 0:34 "One value? Or a range. Two thumbs, a filled band between." "Price range" $15 – $100, thumbs move to $20 – $80; value chips above, labels under thumbs.
- 0:39 "Make it keyboard-able. Arrows step. Home & End jump." Focused slider (outlined row) with key caps ←, →, Home, End; → highlights and the thumb steps; End sends it to the maximum; Home sends it to the minimum.
- 0:44 Outro: "SAVE THIS · Follow for more UI systems.", "Save this for your next form.", a small slider and a Follow button.

## Voice-over summary
- Dragging to an exact value (47 vs 48) is unreliable, and a four-pixel track is a coin toss, so extend the hit area far past the line so the whole row responds.
- A bare track gives no sense of progress; filling everything left of the thumb lets the value read at a glance.
- Continuous sliders never land on clean values; snap to steps because most values (volume, ratings, price) are discrete.
- Users drag blind without a number: float the exact value above the thumb while moving, then fade it.
- One thumb sets a point, two set a range; arrows nudge by one step and Home/End jump to the edges.

## Notes for the skill
- Prefer native `<input type="range">` with `min`, `max`, `step` and a visible `<label>`/`<output>`; for custom sliders follow the WAI-ARIA APG Slider pattern: `role="slider"`, `aria-valuemin`, `aria-valuemax`, `aria-valuenow`, `aria-valuetext` for formatted values ("$50", "4 of 5"), `aria-orientation`; keys: arrows ±1 step, PageUp/PageDown larger jump (often 10%), Home/End to min/max. The video omits PageUp/PageDown.
- Two-thumb range (APG "Multi-Thumb Slider"): each thumb is its own focusable slider with its own label ("Minimum price", "Maximum price"); constrain min ≤ max and update the other thumb's `aria-valuemin`/`aria-valuemax` dynamically; the filled band is decorative.
- Hit area: expand with padding or a pseudo-element; keep at least 44×44px around the thumb on touch (WCAG 2.5.8 minimum 24px; Apple 44pt, Material 48dp). Use pointer capture (`setPointerCapture`) so drags continue outside the row; `touch-action: pan-y` on horizontal sliders so vertical page scroll still works.
- Pressing the row away from the thumb should jump or move the nearest thumb to that position, then continue as a drag.
- Floating value bubble: render above the thumb (not under the finger), clamp it inside the container at the ends, keep a persistent readout as well since the bubble disappears; announce values through the slider's `aria-valuetext`, not a separate live region (avoid double announcements).
- Snap feedback: ticks should match the actual step. In the demo, Volume shows 70 on a track with ticks at quarters, so tick spacing and step disagree there; if ticks are coarser than the step, label that or align them.
- Sliders are poor for precise or wide-range values (e.g. exact prices over thousands); pair with numeric inputs for exact entry.
- Use the accent colour for the fill and focus ring with at least 3:1 contrast against the track and background (WCAG 1.4.11 non-text contrast).
