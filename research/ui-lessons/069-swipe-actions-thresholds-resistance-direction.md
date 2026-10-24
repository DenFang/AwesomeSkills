---
lesson: 069
kind: video
duration_s: 59
type: ui
category: interaction
topic: swipe actions on list rows
sources: frames, voice-over, lesson notes
---

# Swipe actions: thresholds, resistance, direction, discoverability, undo

**Hook:** Swipe right and the email is archived, swipe left and it is gone: one gesture, zero taps, but the gesture has a grammar.

## Main rule
Give every swipe two thresholds (a short pull reveals action buttons and fires nothing; pulling past a commit line fires the action on release), add rubber-band resistance that drops with a haptic tick at the commit point, keep direction semantics fixed app-wide (swipe right = safe/reversible, swipe left = destructive), teach the gesture once with a first-launch peek, and back a one-motion destructive swipe with an undo toast instead of a confirm dialog.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 2 thresholds | REVEAL (short pull: buttons out, nothing fires) and COMMIT (released past the line, action fires) | 0:03-0:12 diagram + voice "two thresholds" / "two trip-wires" |
| 2 actions | revealed on the trailing side on short pull (Archive + Delete) | 0:06-0:10 |
| 1 haptic tick | at the commit point, with the icon "pop" and resistance ending | 0:15-0:22 label "HAPTIC TICK" + voice |
| launch 1 / launch 2+ | first launch shows a peek hint; from the second launch nothing ("nothing, learned") | 0:35-0:45 |
| 1 row | only the first row peeks (buttons half revealed, then settle back) | 0:36-0:42 + voice |
| 5 s | undo window after a full-swipe delete; countdown ring 5 → 4 → 3 | 0:47-0:50 on-screen ring + voice "five seconds of grace" |
| ≤ 2 actions per side | page only: more than two per side prevents muscle memory | page (not in video) |

## Before / after
1. **One threshold vs two.** Implied bad: any swipe distance fires the action. Good: the "pull distance" track has two marks; between 0 and REVEAL the row slides and buttons (Archive, Delete) slide out ("short pull: buttons out, nothing fires"); past COMMIT the destructive button expands to fill the row and the action fires only on release ("released past the line, the action fires"). Why: the short pull acts as a menu and a pause to choose; the long pull is a deliberate decision, and firing on release (not on crossing) lets users back out by dragging back.
2. **Linear drag vs rubber-band resistance.** Good: a graph "ROW DISPLACEMENT VS FINGER TRAVEL" shows the row moving less than the finger in the "rubber-band zone" (curve below the 1:1 dashed line), then at COMMIT the curve kinks upward ("resistance dies"), the action panel expands with its icon, and a "HAPTIC TICK" fires. Why: increasing resistance communicates "you are approaching something"; the sudden release plus haptic marks the exact commit moment without the user looking ("Resistance is feedback.").
3. **Consistent vs swapped direction.** Good: "Right = safe: archive, mark as read, reversible in one tap" and "Left = destructive: delete, unsubscribe, the costly stuff". Bad ("SIDES SWAPPED"): Delete appears on the side where Archive usually is. Why: users swipe from muscle memory, so swapping sides between screens or apps turns a habitual archive into a delete ("Muscle memory has no undo.").
4. **Hidden gesture vs taught gesture.** Good: in a fresh Inbox ("NEW USER") the first row peeks, its delete button half revealed, then settles back ("buttons half-revealed... then settle back"); "Teach once, then never again": LAUNCH 1 peek hint → LAUNCH 2+ nothing, learned. Why: gestures have no visible affordance, so new users rarely discover them unaided; a single motion hint demonstrates the affordance without permanent clutter.
5. **Confirm dialog vs undo.** Good: a full left swipe on "Marcus Webb" deletes in one motion with no dialog; a toast "Conversation deleted" with a 5 s countdown ring and Undo appears; tapping Undo restores the row (briefly highlighted in place). Why: speed is preserved for the common case while a mistaken swipe stays recoverable ("Delete fast. Forgive faster.").

## Do
- Implement two thresholds: reveal (buttons, no action) and commit (fires on release).
- Let the user cancel by dragging back below the commit line before release.
- Add progressive resistance before commit, then release resistance with a visual pop and a haptic tick at commit.
- Keep swipe right for safe, reversible actions and swipe left for destructive ones, identically on every list.
- Show a one-time peek of the first row on first launch, then never again.
- After a full-swipe destructive action, show an undo toast with a visible countdown (5 s in the video).
- Colour-code by consequence: neutral/accent for safe actions, the danger colour for destructive ones.

## Don't
- Fire actions on a short swipe or the moment the threshold is crossed.
- Swap left/right semantics between screens or lists.
- Rely on users discovering swipe gestures without any hint.
- Put a confirm dialog after a swipe delete when undo is possible.
- Make swipe the only way to perform an action (page).

## Scene by scene
- 0:00 "One gesture. Zero taps." Mail list: the top row is swiped right into a full-width "ARCHIVE" panel; then a row is swiped left into a danger-coloured "DELETE" panel and disappears; caption "Swipe is a language. Here's its grammar."
- 0:03 "THRESHOLD DESIGN · One swipe, two trip-wires." A row above a "pull distance" track with marks REVEAL and COMMIT; caption "Reveal is a menu. Commit is a decision."
- 0:06 Short pull: Archive and Delete buttons slide out from the right; label "short pull: buttons out, nothing fires".
- 0:09 Pull continues past REVEAL toward COMMIT; the Delete button widens.
- 0:10 Past COMMIT: Delete fills the row (Archive squeezed to the edge); label "released past the line, the action fires".
- 0:13 "RUBBER-BAND PHYSICS · The row resists you." A row being dragged right; graph "ROW DISPLACEMENT VS FINGER TRAVEL" with a 1:1 dashed reference, "rubber-band zone", and a COMMIT line; the plotted curve grows sub-linearly as the safe-action panel (accent fill) reveals.
- 0:19 At COMMIT: "HAPTIC TICK" badge, the ARCHIVE label pops in, the curve kinks up ("resistance dies"); the row then completes into a full ARCHIVE panel; caption "Resistance is feedback."
- 0:24 "DIRECTION SEMANTICS · Direction is a language." Legend "Right = safe (archive, mark as read, reversible in one tap)", "Left = destructive (delete, unsubscribe, the costly stuff)"; top row swiped right shows "SAFE", second row swiped left shows "DESTRUCTIVE".
- 0:29 Badge "SIDES SWAPPED": the top row now reveals "DELETE" on the safe side; caption "Muscle memory has no undo."
- 0:34 "DISCOVERABILITY · Invisible until you teach it." Phone "Inbox" with a "NEW USER" badge; the first row peeks left showing a delete button, then settles back ("buttons half-revealed... then settle back"); strip "Teach once, then never again: LAUNCH 1 peek hint → LAUNCH 2+ nothing, learned"; at 0:42 the LAUNCH 2+ state activates and the hint text fades ("no hint needed anymore", faint).
- 0:46 "THE SAFETY NET · No dialog. Just a net." Three rows; "Marcus Webb" is fully swiped left into DELETE and removed; toast "Conversation deleted" with countdown 5 → 4 → 3 and Undo; Undo tapped, the row slides back with a brief highlight. Caption "Delete fast. Forgive faster."
- 0:55 Outro "MOBILE UX · GESTURES · The gesture is the UI." with a row half-swiped to Archive, "Follow for more mobile UX", "Save this for your next app".

## Voice-over summary
- Swipe right archives, swipe left deletes; every swipe hides two thresholds: a short pull reveals buttons (a pause, a choice), pulling further crosses the commit line, and the action fires on release.
- Under the finger the row resists like a rubber band; at the commit point the icon pops and resistance disappears, and that small haptic beat is the interaction communicating.
- Direction is a language: right for safe actions (archive, mark as read), left for destructive ones; swapping sides makes muscle memory delete the wrong email.
- Gestures are invisible, so peek the first row on first launch (buttons half revealed, then settle back); one hint teaches the pattern.
- A full swipe deletes in one motion without a dialog, which only works with a safety net: an undo toast with five seconds of grace.

## Notes for the skill
- Thresholds are usually proportional to row width (e.g. reveal ≈ width of the action buttons, commit ≈ 50-60% of row width) plus a velocity rule (a fast fling commits even before the distance threshold); the video gives no numbers, so these are implementation suggestions, not video values.
- Rubber band: map finger delta to row delta with a damping function before commit (e.g. `d * (1 - d / (d + k))` or iOS-style `(1 - 1/(d*c/w + 1)) * w`), then 1:1 after commit; trigger `navigator.vibrate(10)` on Android web or UIImpactFeedbackGenerator / HapticFeedback on native at the commit crossing, once per crossing (re-arm if the user drags back).
- Platform conventions: iOS uses leading (swipe right) for non-destructive actions like read/unread and trailing (swipe left) for delete/more, matching the video; Android Gmail defaults both directions to archive and makes them configurable. "Right = safe" is a convention, not a universal rule; the binding rule is consistency within the app.
- Accessibility: swipe must never be the only path. Provide the same actions via a visible button, long-press/context menu, or the detail view; expose them to screen readers as custom actions (iOS `accessibilityCustomActions`, Android `AccessibilityAction`, web: a "More actions" menu button per row). WCAG 2.5.1 Pointer Gestures requires a single-pointer, non-path alternative for path-based gestures; WCAG 2.5.2 Pointer Cancellation is satisfied by firing on release and allowing drag-back.
- Undo toast: 5 s is short for some users (WCAG 2.2.1 Timing Adjustable); pause the countdown while the toast is touched or focused, keep Undo keyboard/screen-reader reachable, and announce "Conversation deleted, Undo available" via a polite live region. Defer the real delete (or soft delete) until the window closes.
- The first-launch peek should run once per user per device, only when the list is visible and idle, and be skipped under `prefers-reduced-motion: reduce` (use a static hint or tooltip instead).
- Keep at most two actions per side (page) and the destructive action at the outer edge so the full swipe maps to it.
