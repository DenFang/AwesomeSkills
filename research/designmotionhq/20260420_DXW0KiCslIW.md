---
id: DXW0KiCslIW
reel_url: https://www.instagram.com/reel/DXW0KiCslIW/
pattern_page: https://designmotionhq.com/patterns/loading-states-system
date: 2026-04-20
duration_s: 51
type: ui
category: feedback
topic: choosing a loading pattern (skeleton, spinner, progress bar, optimistic UI, show nothing)
sources: frames, voice-over, pattern page
---

# Loading is a system, not a default skeleton

**Caption:** Loading is a system
**Hook:** Stop using skeletons for everything; there are five loading patterns and one right choice per context.

## Main rule
Pick the loading pattern from what you know about the wait: known content shape and wait over 300 ms → skeleton; unknown duration under 3 s → inline spinner; known percentage and over 3 s → progress bar with real meta; reversible high-success mutation → optimistic update with rollback; response under 300 ms → show no loading state at all.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 5 patterns | skeleton, spinner, progress bar, optimistic UI, show nothing | 0:02 on-screen "5 LOADING PATTERNS", "1 right choice per context." |
| > 300ms + known shape | skeleton threshold | 0:05-0:12 on-screen chips + voice |
| < 3s + unknown duration | spinner range | 0:14-0:20 on-screen chips + voice |
| > 3s + known % | progress bar range | 0:21-0:29 on-screen chips + voice |
| 0% → 23% → 51% → 78% → 100% of 14.2 MB; 1.5 / 2.1 / 1.9 / 1.4 MB/s; 8s / 6s / 4s / 2s remaining | example progress meta (file name, bytes done/total, speed, time remaining) | 0:21-0:29 on-screen |
| 99% | success rate of mutations suited to optimistic UI | 0:33-0:35 voice ("succeed 99% of the time") |
| 0 ms click → 300 ms synced | optimistic timeline: user sees result at 0 ms, server sync behind | 0:31-0:38 on-screen timeline "User sees the result in 0ms. Sync happens behind." |
| 12,423 → 12,424 likes | optimistic like counter increments instantly | 0:30-0:31 on-screen |
| < 300ms → show nothing | threshold below which no indicator is shown | 0:40-0:47 on-screen + voice |
| 200ms | example: a 200 ms skeleton flash "feels broken" | 0:41-0:47 on-screen |

The pattern page states the same thresholds with "~" (about 300 ms, about 3 s).

## Before / after
1. **Skeleton (0:03-0:12).** A blurred placeholder card resolves into an article card (author, title, text, image). Labels: KNOWN SHAPE, > 300ms. Why it works: the placeholder previews the final layout, so the brain matches content into a structure it already sees; perceived speed improves and there is no layout shift when content arrives. Wrong use (stated in the hook and on the page): skeleton for every fetch regardless of shape or duration.
2. **Spinner (0:13-0:20).** RIGHT: a "Save changes" button switches to an inline spinner + "Saving..." and then to "✓ Saved". WRONG: a large panel with a lone spinner and "Loading dashboard...", annotated "No context. No progress. No trust." Labels: UNKNOWN DURATION, < 3s. Why: a spinner says only "something is happening"; that is enough for a short, local action tied to the control the user just pressed, but on a full page or long wait it gives no sense of progress and reads as frozen.
3. **Progress bar (0:21-0:29).** Upload card "project-build.zip" with percentage, bytes done of total, speed and time remaining, ending at 100% "14.2 MB · Complete", "Done", "✓ Uploaded". Labels: KNOWN %, > 3s, BUILDS TRUST. Why: when the system knows progress, showing it (plus concrete meta) lets users predict the end and decide whether to wait, which builds trust on long operations.
4. **Optimistic UI (0:30-0:39).** Tapping the heart fills it and increments 12,423 → 12,424 likes immediately; a small "Synced" badge appears later; the timeline shows 0 ms click vs 300 ms synced. Labels: INSTANT FEEDBACK, ROLLBACK ON FAIL. Why: for reversible actions that almost always succeed, waiting for the server adds latency with no benefit; show the result now and revert only if the request fails.
5. **Show nothing (0:39-0:47).** Two identical cards load: WITH SKELETON FLASH (marked ✗) briefly blinks a placeholder; SHOW NOTHING (marked ✓) simply shows the content. "200ms of skeleton feels broken", labels < 300ms, SHOW NOTHING. Why: a loading state that appears and disappears in a fraction of a second is perceived as flicker, a glitch, not as feedback; a slight delay with no indicator feels smoother.

## Do
- Decide per request: known shape → skeleton; known percentage → progress bar; short unknown wait → inline spinner; reversible likely-success mutation → optimistic update.
- Put the spinner inside the control that triggered the action and finish with an explicit success state ("Saved").
- Show real meta on progress bars: bytes done of total, speed, time remaining, and a clear completion state.
- On optimistic updates, reconcile in the background and roll back visibly if the server fails.
- Delay any loading indicator until about 300 ms have passed.

## Don't
- Don't use a skeleton for every fetch.
- Don't cover a full page or a long, open-ended load with a lone spinner.
- Don't flash a loading state for responses under 300 ms.
- Don't use optimistic UI for actions that are irreversible or often fail.

## Scene by scene
- 0:00 Five floating thumbnails (skeleton card, spinner "LOADING", upload bar, heart with likes, "SHOW NOTHING") assemble into a grid under "5 LOADING PATTERNS": "1 right choice per context."
- 0:03 "01 · SKELETON": blurred placeholder card with a shimmer, resolves into an article card "The Loading State Hierarchy"; chips KNOWN SHAPE, > 300ms.
- 0:13 "02 · SPINNER": RIGHT "Save changes" button with inline spinner "Saving..." toggling to "✓ Saved" (success colour); WRONG panel "Loading dashboard..." with "No context. No progress. No trust."; chips UNKNOWN DURATION, < 3s.
- 0:21 "03 · PROGRESS BAR": upload card fills 0% → 23% → 51% → 78% with speed and time remaining; chips KNOWN %, > 3s, BUILDS TRUST.
- 0:26 100%: "14.2 MB · Complete", "Done", "✓ Uploaded".
- 0:30 "04 · OPTIMISTIC UI": post card, cursor taps the heart, count goes 12,423 → 12,424 instantly; "Synced" badge fades in; timeline 0MS CLICK → 300MS SYNCED; chips INSTANT FEEDBACK, ROLLBACK ON FAIL.
- 0:39 "05 · SHOW NOTHING": side-by-side cards WITH SKELETON FLASH (✗) vs SHOW NOTHING (✓); "200ms of skeleton feels broken"; chips < 300ms, SHOW NOTHING. The load replays once.
- 0:48 Recap grid labelled SKELETON, SPINNER, PROGRESS, OPTIMISTIC, NOTHING; "Save this for your next UI." and the handle.

## Voice-over summary
- Skeletons are overused; loading should be a system.
- Skeleton when the shape is known (cards, lists, articles) and the wait is over 300 ms; it makes the page feel already loaded.
- Spinner for short waits under three seconds of unknown length, never for full page loads.
- Progress bar when the percentage is known: uploads, installs, anything over three seconds; seeing progress builds trust.
- Optimistic UI for likes, saves, bookmarks (mutations that succeed about 99% of the time): show the result instantly, roll back on failure. Under 300 ms show nothing: "Your brain reads it as a bug."

## Notes for the skill
- Implement "show nothing" as a delayed indicator: start a ~300 ms timer when the request begins and only render the loading UI if it has not resolved; once shown, keep it for a minimum (commonly ~400-500 ms) so it does not flicker out. The video gives only the 300 ms threshold; the minimum display time is a common complement, not from the video.
- Thresholds vs NN/g: Nielsen's response-time limits (0.1 s instant, 1 s flow, 10 s attention) and NN/g's guidance (looped indicator for roughly 2-10 s, percent-done for longer) are slightly more conservative than the video's 3 s cut-off for progress bars. Use 3 s as a practical trigger, but always prefer determinate progress whenever percentage is known.
- Spinner in a button: keep the button width stable (no layout jump), set `aria-busy="true"` or `aria-disabled="true"` to prevent double submission, keep focus on the button, and announce "Saving" / "Saved" through a polite live region (`role="status"`).
- Progress bar semantics: native `<progress>` or `role="progressbar"` with `aria-valuenow`, `aria-valuemin`, `aria-valuemax` and an accessible name; announce completion. Time-remaining estimates should be smoothed, not jump around.
- Skeleton: mark placeholders `aria-hidden="true"`, set `aria-busy="true"` on the loading region, and stop or soften the shimmer under `prefers-reduced-motion`. Match placeholder dimensions to real content to avoid layout shift (CLS).
- Optimistic UI rollback must be visible: restore the previous state and show an error with Retry (a silent revert looks like a bug). Not for payments, deletes without undo, or actions with validation likely to fail.
- The "99%" figure is the narrator's rule of thumb, not a measured threshold.
