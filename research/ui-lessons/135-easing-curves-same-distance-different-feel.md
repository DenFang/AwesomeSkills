---
lesson: 135
kind: video
duration_s: 30
type: ui
category: motion
topic: easing curves (linear vs ease-out vs spring)
sources: frames, lesson notes
---

# Easing curves: same distance, different feel

**Hook:** Three dots travel the same distance in the same time with linear, ease-out and spring curves, and they feel completely different.

## Main rule
Choose the curve deliberately: ease-out (fast start, decelerating stop) as the default for UI that enters and settles, a subtle spring overshoot for presses, sheets/modals and confirmations, and linear only for continuous motion such as spinners or marquees; reuse the same small set of curves across the product and stagger list/card entrances.

## Numbers and values
No numeric values shown. The video shows no durations, cubic-bezier values or spring parameters, and the lesson notes gives none either ("a few frames apart" for stagger is the only quantity, without a number). No voice-over: the audio is music only (the transcript file contains only a speech-recognition artifact, no narration).

## Before / after
1. **Dot race (0:00-0:03).** Three dots on identical tracks, same start and end time. Linear: still around a quarter of the way at the moment ease-out is already past halfway, and it arrives at constant speed, then stops abruptly. Ease-out: covers most of the distance early and decelerates into the end. Spring: reaches the end first, slightly overshoots the track end, then settles (marked with a check). Why: the eye reads velocity profile, not duration; constant speed with an instant stop looks mechanical, deceleration looks like a physical object coming to rest.
2. **Button press (0:04-0:08).** Three "Submit" buttons labelled linear, ease-out and spring, each with its curve drawn below. The spring button scales with a small overshoot, called out as "the bounce". Why: a little overshoot gives tactile, responsive feedback for a press.
3. **Card entrance (0:09-0:12).** Three columns of five list cards slide in from the right with a stagger (rows arrive one after another) using linear, ease-out and spring. Why: staggered arrival creates a readable cascade instead of one rigid block; the curve changes whether the cascade feels mechanical or settled.
4. **Modal / bottom sheet open (0:13-0:17).** Three phones open the same bottom sheet with linear, ease-out and spring; the spring one is tagged "premium"; caption "same timing → different perception". Why: same duration, but the overshoot and deceleration change how polished the motion feels.
5. **Curves explained (0:18-0:23).** "The curve shapes the feel": plots of position over time (linear straight diagonal, ease-out steep then flattening, spring rising past the target with a small wave before settling), each with a dot moving on a vertical start → end track in sync with a marker on its curve.

## Do
- Use ease-out as the default for elements entering or moving into place.
- Use a subtle spring (small overshoot, quick settle) for button presses, sheets/modals and confirmations.
- Reserve linear for continuous or looping motion (spinners, progress shimmer, marquees).
- Keep one shared set of easing tokens and reuse it for press, cascade and sheet open.
- Stagger list and card entrances by a small, constant offset so they cascade.

## Don't
- Use linear easing for UI that starts and stops.
- Tune spring bounce/stiffness so high that the element visibly wobbles.
- Mix arbitrary curves per component; inconsistent easing makes the interface feel stitched together.

## Scene by scene
- 0:00 No title yet: three dots on horizontal tracks start moving together; mid-flight the linear dot lags, the ease-out dot is ahead, the spring dot is already at the end with a trail past the track end.
- 0:02 Dots at the end; labels appear: "linear", "ease-out", "spring ✓".
- 0:03 Headline "Same distance. Different feel." Small label "EASING CURVES".
- 0:04 "BUTTON PRESS": three "Submit" buttons (neutral, accent, success-styled) labelled linear / ease-out / spring with mini curve plots; buttons press and scale; at 0:06 a chip "↑ the bounce" points at the spring curve's overshoot.
- 0:09 "CARD ENTRANCE": three columns (linear, ease-out, spring) of five skeleton list cards slide in from the right row by row; by 0:11 all are in place.
- 0:13 "MODAL OPEN": three phone mockups; a bottom sheet with a handle, two text lines and a button rises in each; the spring column is tagged "premium"; caption "same timing → different perception".
- 0:18 "The curve shapes the feel": three plots (linear, ease-out, spring) drawn progressively, each paired with a dot moving down a vertical start → end track.

## Voice-over summary
- Voice-over not present: the video is music only (no narration to summarise). All content comes from on-screen labels and the lesson notes.

## Notes for the skill
- Concrete starting values (not from the video, standard practice): ease-out as `cubic-bezier(0.16, 1, 0.3, 1)` or `cubic-bezier(0.22, 1, 0.36, 1)` for entrances; ease-in for exits; ease-in-out for on-screen moves between two positions. Springs: a low bounce (for example Framer Motion `type: "spring", bounce: 0.15-0.25`, or stiffness about 300-500 with damping about 25-35); in CSS approximate with `linear()` easing or a cubic-bezier with y1/y2 slightly above 1.
- The closing claim "spring > ease > linear. Always." is an oversimplification. Linear is correct for continuous motion (spinners, indeterminate progress, marquees, opacity crossfades driven by scroll); exits generally use ease-in (accelerate away), not ease-out or spring; springs on large surfaces or frequent actions can feel slow or distracting. Rank by context, not universally.
- Springs also suit interruptible, gesture-driven motion because they preserve velocity; that is a stronger reason to use them than "premium".
- Overshoot on layout-affecting properties can cause content jumps; animate `transform` and `opacity` only.
- Respect `prefers-reduced-motion: reduce`: remove overshoot and travel, keep a short opacity fade; staggered cascades should collapse to a single quick fade.
- Stagger: keep the per-item offset small (commonly 30-60 ms) and cap the total cascade (for example, stagger only the first 5-8 items) so long lists do not delay content.
