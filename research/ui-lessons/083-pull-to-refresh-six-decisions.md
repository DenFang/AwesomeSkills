---
lesson: 083
kind: video
duration_s: 51
type: ui
category: interaction
topic: pull-to-refresh (threshold, resistance, indicator handoff, haptic, bounce, live list)
sources: frames, voice-over
---

# Pull-to-refresh: six decisions

**Hook:** Pull down, let go too early, and nothing loads: the gesture has a commit line, and everything else is built around it.

## Main rule
Pull-to-refresh fires only when the user releases past a visible threshold; the drag resists with diminishing travel (rubber band), the pull indicator morphs into the loading spinner, one haptic tick confirms the threshold before release, the list springs back with a slight overshoot, and the list stays scrollable and updates in place while the reload runs.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 85px, then 0px | "pull distance" meter for an early release: list snaps back, nothing loads | 0:00-0:02 on-screen |
| finger 220 → moved 106; 206 → 103; 191 → 100 | elastic pull: content travels about half the finger distance, ratio slightly falling as the pull grows (0.52 → 0.48) | 0:10-0:18 on-screen |
| finger 220 → moved 220 (also 206/206, 191/191) | 1:1 drag labelled "cheap" | 0:10-0:18 on-screen |
| 3 stages: stretch → full ring → spinner | indicator handoff at the threshold | 0:19-0:24 on-screen |
| 1 tick | haptic at the threshold, before release (timeline pull → tick → release → load) | 0:22-0:33 on-screen + voice |
| "1 new in place" | new row inserted at the top while the spinner runs | 0:43-0:47 on-screen |

The threshold distance itself is not given as a number (shown only as a dashed "threshold" line). No spring parameters or durations are shown.

## Before / after
- **Early release.** Releasing below the line: list snaps back, no reload ("snaps back · no reload"). Releasing past the line: "refresh fires". Why: a fixed commit point prevents accidental reloads from casual over-scroll and makes the gesture predictable.
- **Elastic vs 1:1 drag.** Side by side: elastic content moves about 50% of the finger distance with a flattening curve; 1:1 content tracks the finger exactly. Why: diminishing travel signals a boundary and "weight", and tells the user they are pulling against something; a 1:1 drag reads as ordinary scrolling and feels cheap.
- **Indicator handoff.** The arc that fills while stretching becomes a full ring at the threshold, then starts spinning as the loader. Why: one continuous object links the gesture to its result, so no second loader pops in; the gesture becomes the progress indicator.
- **Haptic before release.** An "armed" badge and a single tick fire when the threshold is crossed, while the finger is still down ("feedback before release"). Why: the user knows the action is committed before lifting the finger, so they do not keep pulling or release uncertainly.
- **Rubber band vs hard stop.** After release, the rubber-band list overshoots past rest and settles; the hard-stop list moves linearly and halts abruptly. Why: an overshoot-and-settle reads as physical; an abrupt stop reads as broken.
- **Frozen vs live list.** While "spinner running", the list remains scrollable and a new row slides in at the top ("1 new in place"). Why: locking scroll during a reload makes the content feel dead and blocks reading.

## Do
- Define a clear threshold; trigger refresh only on release beyond it.
- Snap back without reloading when released short of the threshold.
- Apply resistance: content travel well below finger travel (about 0.5x here) and decreasing as the pull lengthens.
- Grow the pull indicator with distance, complete it at the threshold, and turn the same element into the spinner.
- Fire one short haptic exactly once when the threshold is crossed (not again on release).
- Release with a spring that slightly overshoots and settles.
- Keep scrolling enabled during the reload and insert new items in place.

## Don't
- Don't fire the refresh mid-drag or on a short pull.
- Don't make the drag 1:1 with the finger.
- Don't swap the pull indicator for a separate loader at release.
- Don't end the release with a linear hard stop.
- Don't lock scroll or overlay the list while refreshing.

## Scene by scene
- 0:00 Phone "Inbox" list, a small pull arc above the rows; "pull distance 85px" meter drops to 0px after release. Caption "Let go early. Nothing loads."
- 0:03 "Threshold: Fires past the line." Dashed "threshold" line under the indicator; two rows: "release below → snaps back · no reload" (danger colour) and "release past → refresh fires" (success colour). Footer "Fires past the threshold, never before."
- 0:10 "Resistance: Make it carry weight." Two phones: "Elastic resists" vs "1:1 cheap"; readouts "finger 220 → moved 106" vs "finger 220 → moved 220"; a graph "finger drag → content move" with a flattening curve vs a straight dashed line. Footer "Resist like the content has weight."
- 0:19 "Handoff: The stretch becomes the spinner." Strip of three states: stretch → full ring → spinner, highlighted in turn.
- 0:25 "Haptic: It ticks before you let go." Timeline pull / tick / release / load with a marker; at the threshold the ring pulses, an "armed" badge appears and a label "feedback before release" marks the gap between tick and release. Footer "One tick at the threshold, before you let go."
- 0:34 "Bounce: Overshoot, then settle." Two phones "Rubber band" vs "Hard stop"; graph "position after release" shows a curve dipping past rest and settling vs a dashed linear drop.
- 0:41 "Scroll alive: Never freeze the list." Spinner running while the finger scrolls the list; chip "updates in place" turns into "1 new in place" as a new row (now) slides in at the top.
- 0:48 End card "Pull is a promise." with six tiles: Threshold, Resistance, Handoff, Haptic, Bounce, Scroll; site link.

## Voice-over summary
- Releasing too soon must load nothing; refresh fires only past the threshold, otherwise the list snaps back.
- Further pulling should resist as if the content has weight; a one-to-one drag feels cheap.
- At the threshold the stretch indicator becomes the spinner, so the gesture is the loader.
- One short haptic tick at the threshold arms the action before the finger lifts: feedback beats the release.
- Past the threshold the rubber band overshoots and settles; a hard stop feels broken.
- Do not lock scrolling during the reload; "Frozen content feels dead."

## Notes for the skill
- Resistance formula: a common rubber-band function is `offset = (1 - 1 / (d * c / dim + 1)) * dim` (iOS-style, c ≈ 0.55), or simply `offset = d * k` with k shrinking as d grows. The video's readouts (≈0.5x with slight decay) are consistent with this; exact coefficients are not given.
- Use the platform control where possible: `UIRefreshControl` on iOS and `SwipeRefreshLayout` / Compose `pullToRefresh` on Android already implement threshold, resistance and haptics. On the web, CSS `overscroll-behavior-y: contain` prevents the browser's native pull-to-refresh from competing with a custom one.
- Haptic: iOS `UIImpactFeedbackGenerator(.light)` or selection feedback; Android `HapticFeedbackConstants.GESTURE_THRESHOLD_ACTIVATE` (API 34+) or `CONFIRM`. Web `navigator.vibrate` is unsupported on iOS Safari, so never rely on haptics alone; the indicator completing to a full ring is the visual equivalent.
- Fire the haptic once per crossing; if the user drags back above the line, disarm (and optionally tick again on re-cross) so release then cancels.
- Accessibility: pull-to-refresh is a hidden gesture with no keyboard or switch-access equivalent. Always provide a visible or assistive alternative (refresh button, menu item, or `accessibilityCustomActions`), and announce "Refreshing" / "Updated, 1 new" via a live region.
- Inserting a new row at the top while the user is scrolled down shifts content; keep the scroll anchor stable (`overflow-anchor` on web, or insert above the viewport without moving visible rows) and show a "1 new" pill instead of jumping.
- Under reduced motion, keep the threshold logic but shorten or remove the overshoot bounce and use a non-rotating progress indicator.
