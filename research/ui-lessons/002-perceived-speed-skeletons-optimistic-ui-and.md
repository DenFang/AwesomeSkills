---
lesson: 002
kind: video
duration_s: 66
type: ui
category: feedback
topic: perceived performance (skeleton screens, optimistic UI, front-loaded progress bar)
sources: frames, voice-over
---

# Perceived speed: skeletons, optimistic UI and front-loaded progress

**Hook:** The same loading time can feel different; three techniques make an app feel fast without making it faster.

## Main rule
When the real wait cannot be shortened, shape how it is perceived: show the page layout as a skeleton instead of a blank area with a spinner, update the UI immediately on a user action instead of waiting for the server (optimistic UI), and let a determinate progress bar move fast early and slow near the end rather than advancing linearly.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 3 techniques | skeleton screens, optimistic UI, progress illusions | 0:05-0:14 on-screen cards ("Coming up") + voice |
| 142 → 143 | like counter on the heart button; optimistic version flips at about 0:29, server-wait version shows a spinner and flips at about 0:31 (roughly 2 s later in the demo) | 0:27-0:31 on-screen |
| Linear: 8, 24, 41, 58, 74, 91, 100 % | linear bar, sampled once per second | 0:40-0:46 on-screen |
| Psychological: 16, 49, 80, 80, 80, 97, 100 % | front-loaded bar at the same moments: jumps to 80 % in about 2 s, holds, then finishes | 0:40-0:46 on-screen |
| 3.7s → 3.0s → 2.4s → 1.7s → 1.0s → 0.4s remaining | shared countdown chip; both bars finish together ("Both finished!") | 0:40-0:46 on-screen |
| 0, 33, 75, 87, 93, 99 % → Done | combined demo upload of a 2.4 MB file (vacation_photo.jpg) | 0:51-0:59 on-screen |

No easing curves or millisecond values are given.

## Before / after
- **Blank screen vs skeleton preview.** Bad: an empty card with a small spinner until content arrives. Good: grey placeholder blocks in the exact shape of the coming post (avatar circle, name line, text lines, media block, action row) with a shimmer sweep. Both receive real content at the same moment (about 0:22). Why: the layout tells the user what is coming and where, so the brain starts processing the structure and the wait feels shorter; the shimmer signals ongoing activity.
- **Wait for server vs instant feedback (like button).** Bad: tapping the heart replaces it with a spinner and the count stays 142 until the response returns. Good: the heart fills and the count goes to 143 on tap. Why: the feedback lands at input latency instead of network latency, which the user reads as speed.
- **Linear vs psychological progress.** Bad: the bar advances evenly (8 → 24 → 41 → ...). Good: the bar jumps quickly to 80 % and then crawls; both end at the same time. Why (as claimed): people remember the quick start more than the slow end, so the same duration feels shorter.

## Do
- Render a skeleton that matches the final layout (same block sizes and positions) while data loads.
- Add a subtle shimmer to skeleton blocks to signal activity.
- Apply cheap, reversible actions (like, toggle, reorder) to the UI on tap and sync in the background.
- For determinate progress, give immediate visible movement at the start (the video's advice is fast start, slow end; see Notes for the caveat about late slowdowns) and finish at the true end.
- Combine the techniques: placeholder of the item, fast-start progress, immediate state update, then a clear "Done" state.

## Don't
- Don't show a blank area with only a spinner when the layout is known in advance.
- Don't block a simple toggle behind a spinner until the server answers.
- Don't advance a progress bar at a constant rate when you can front-load it.

## Scene by scene
- 0:00 Two progress bars side by side labelled "Same time" vs "Feels faster"; both fill. Headline "Same loading time. Different feeling. Here's how."
- 0:05 Section "Tricks your brain doesn't notice": three cards appear in turn with "Coming up": Skeleton Screens, Optimistic UI, Progress Illusions.
- 0:15 "Secret #1 Skeleton Screens": left card "Blank screen" (empty, small spinner), right card "Skeleton preview" (avatar, lines, media block with shimmer). Caption "Show the layout before the content. Your brain fills in the gaps."
- 0:22 Both cards load the same post (avatar "A", name "Alex Chen", short text, media block, like/comment/share counts) at the same moment.
- 0:27 "Secret #2 Optimistic UI": two like buttons showing 142, labelled "Wait for server" and "Instant feedback".
- 0:29 Instant button turns to a filled heart with 143; the server-wait button shows a spinner with 142.
- 0:31 Server-wait button also reaches 143. Caption "Don't wait for the server. Assume success. Update instantly."
- 0:38 "Secret #3 Progress Illusions": card with "Linear Progress" and "Psychological Progress", both "Uploading... 0%".
- 0:40 Both bars run with a "remaining" countdown chip (3.7 s down to 0.4 s); the psychological bar reaches 80 % by 0:42 and holds while the linear bar catches up. Caption "Same duration. Different curve. Fast start = perceived speed."
- 0:46 Both at 100 %, chip "Both finished!".
- 0:51 "All three techniques combined": upload card for vacation_photo.jpg (2.4 MB) with an image skeleton and three tags (Skeleton, Fast start, Instant UI); bar runs 0 → 33 → 75 → 87 → 93 → 99 %.
- 0:59 Card finishes: image appears, "Done!" with a check, full bar, success glow. Caption "Perception is reality. Make it feel fast."
- 1:03 Follow card "Want more UX tricks? Follow for daily tips".

## Voice-over summary
- Same loading time, different feeling: apps manipulate perceived speed with three tricks.
- Skeleton screens: show the layout instead of nothing; the shimmer makes you expect content, so the wait feels shorter.
- Optimistic UI: don't wait for the server after a tap, show success immediately; instant feedback registers as speed.
- Progress bar psychology: start fast and slow down at the end; the same total time feels faster because the quick start is remembered.
- Closes with all three together and "Perception is reality."

## Notes for the skill
- Skeletons: size the placeholder blocks to the real content to avoid layout shift (CLS) when content arrives. Mark the loading region `aria-busy="true"` and give screen readers a text status ("Loading posts"); hide the decorative skeleton blocks with `aria-hidden="true"`. Stop or replace the shimmer under `prefers-reduced-motion: reduce` (a static placeholder is fine). For very short loads (under roughly 300 ms) consider delaying the skeleton so it does not flash.
- Optimistic UI is only safe for actions that almost always succeed and are reversible. The video omits the failure path: on error, roll back the state (143 → 142, heart unfilled) and tell the user with a non-blocking message and a retry. Do not use optimistic success for payments, irreversible deletes or anything where a false "done" causes harm. Keep the button usable during sync and debounce repeated taps.
- Progress: the demo bar actually jumps to 80 % and stalls for about 3 s before finishing, which is a "fast start, stall, finish" curve rather than a smooth deceleration. A long stall near the end can read as "stuck"; prefer a smooth ease-out, keep moving slowly, and never show 100 % before the work is truly done. A fake curve should still track real progress when it is known; if progress is unknown, use an indeterminate indicator instead of an invented percentage. Expose progress with `role="progressbar"` and `aria-valuenow`.
- The "your brain remembers the quick start" claim is questionable: the best-known study on progress-bar perception (Harrison et al., "Rethinking the Progress Bar", 2007) found the opposite tendency, with bars that accelerate toward the end (and avoid late stalls) judged faster, consistent with the peak-end effect. Treat curve choice as something to test, avoid slowing or stalling near the end, and keep it honest.
- Use the success state colour for completion only together with a text/icon cue ("Done!" plus a check), not colour alone.
