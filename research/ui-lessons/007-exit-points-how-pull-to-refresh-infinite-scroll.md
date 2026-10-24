---
lesson: 007
kind: video
duration_s: 78
type: ui
category: interaction
topic: engagement patterns that remove stopping cues (pull to refresh, infinite scroll, autoplay)
sources: frames, voice-over
---

# Exit points: how pull to refresh, infinite scroll and autoplay remove stopping cues

**Hook:** Apps are built so you never stop; three patterns remove every exit point.

## Main rule
A natural stopping cue (an end of list, a "next page" choice, a pause between videos) is a decision point where users can leave. Pull to refresh (variable reward), infinite scroll (no end) and autoplay (no gap) each remove one. Treat them as deliberate engagement levers, not neutral defaults: in products that should respect the user's time, keep or restore exit points (an end-of-feed marker, pagination or "load more", an autoplay countdown that can be cancelled or turned off).

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 3 tricks, 0 exit points | summary list: Pull to Refresh, Infinite Scroll, Autoplay | 1:04-1:13 on-screen |
| "3 second pause..." | gap after a video ends in the "With Pause" panel, with the thought "Should I keep watching?" | 0:47-1:03 on-screen (small text) |
| "0.5 seconds of silence = you leave." | headline claim about the gap after a video | 0:47-1:03 on-screen caption |
| Videos watched: 2 → 9 | counter in the "Autoplay" panel climbing while the "With Pause" panel stays on Replay | 0:50-1:03 on-screen |
| Pagination 1, 2, 3, ... | "With Exit" list ending in page buttons, labelled "Decision point" | 0:29-0:45 on-screen |

Note: the on-screen panel says "3 second pause" while the caption says "0.5 seconds of silence"; the video does not reconcile the two. Neither number is sourced.

## Before / after
The video frames each pair as "with exit" vs "no exit"; for a user-respecting product the "with exit" side is the recommendation.
- **Pull to refresh vs slot machine lever.** The phone panel shows a finger pulling down a feed, a spinner, then new rows; the slot machine panel spins on the same beat and lands on "New content!" (label "Variable Rewards"). Mechanism: the same physical pull, an uncertain result, and an occasional reward is a variable-ratio reinforcement loop, which drives repeated checking.
- **Pagination vs infinite scroll.** "With Exit": five items, then page buttons 1, 2, 3, ... marked "Decision point". "No Exit": items keep streaming in with a loading indicator at the bottom. Mechanism: reaching the end of a page forces a conscious "continue?" choice; an endless list removes that choice, so there is no moment to stop.
- **Pause vs autoplay.** "With Pause": the video ends on a Replay screen with a pause and the thought "Should I keep watching?", labelled "Exit point". "Autoplay": the next video (shown "Up next", "No gap") starts immediately and the watched counter keeps rising, labelled "No exit". Mechanism: the silence after content ends is when attention resurfaces; removing it skips the decision.

## Do
- Decide explicitly whether a feed needs an end; for task-oriented or finite content show an end state ("You're all caught up") or paginate/"load more".
- For autoplay, show a visible countdown to the next item with a Cancel control, and offer a setting to turn autoplay off.
- Keep pull to refresh for content that genuinely changes; pair it with a clear "updated" state and don't fake new content.
- Preserve scroll position and give a way back to a known point (e.g. "back to top", page anchors) in long lists.

## Don't
- Don't remove every stopping point by default in products where compulsive use harms the user (kids' apps, wellbeing, learning).
- Don't put essential content (footer links, contact, legal) below an infinite list where it can never be reached.
- Don't start the next video with zero gap and no way to stop it.

## Scene by scene
- 0:00 A phone mock-up with a feed of video cards and notification badges, glowing in an alarm-like colour. Text "Apps are designed so you never stop. 3 tricks that remove every exit point. Let me show you."
- 0:06 "Secret #1 Pull to Refresh": two panels, "Your Phone" (finger pulls down a list, spinner, rows) and "Slot Machine" (videos spin, lever drops, result "New content!", footer "Variable Rewards"), joined by an equals sign.
- 0:10 Caption "Same gesture. Same dopamine. You're playing a slot machine." The pull/spin loop repeats several times.
- 0:28 "Secret #2 Infinite Scroll": panels "With Exit" (five list items, page buttons 1 2 3 ..., label "Decision point") and "No Exit" (list scrolling continuously with a loading indicator).
- 0:30 Caption "No end = no decision point. No decision = no exit."
- 0:46 "Secret #3 Autoplay": panels "With Pause" and "Autoplay", both playing "Video 1".
- 0:49 Video ends: "With Pause" shows Replay, a pause icon, "3 second pause...", "Should I keep watching?", label "Exit point". "Autoplay" jumps to Video 2 with "Up next", "No gap", "Videos watched: 2", label "No exit".
- 0:50 Caption "0.5 seconds of silence = you leave. Autoplay removes the gap." Autoplay counter climbs to 9 while the paused panel stays put.
- 1:04 Summary "3 tricks. 0 exit points." with a numbered list (Pull to Refresh, Infinite Scroll, Autoplay), each marked with an X.
- 1:10 Prompt "Which one got you? Comment 1, 2 or 3".
- 1:15 Follow card "Want more design secrets? Follow for daily tips".

## Voice-over summary
- Apps are designed so you never stop; three tricks remove every exit point.
- Pull to refresh mirrors pulling a slot machine lever: same motion, same uncertainty, same dopamine hit.
- A "next" button forces a decision and is therefore an exit point; infinite scroll removes the decision and the end.
- When a video ends the silence wakes you up; autoplay removes that gap so the next video starts before you think of leaving.
- Closing line: every pixel is designed to remove your next reason to leave.

## Notes for the skill
- This video is an exposé of persuasive/engagement patterns, not a recommendation to use them. In the skill, list them under "engagement patterns: use consciously" and default to keeping stopping cues for finite or task-based content.
- Infinite scroll costs: no reachable footer, lost position after navigating away and back, hard to share a "page", poor keyboard and screen reader experience. If used, keep focus management sane (new items appended without stealing focus), announce loaded batches politely (`aria-live="polite"`), use `role="feed"` with `aria-setsize`/`aria-posinset` per WAI-ARIA APG, and provide a "load more" button as an accessible alternative.
- Autoplay: WCAG 2.2.2 (Pause, Stop, Hide) requires a way to pause moving content that starts automatically and lasts over 5 seconds; WCAG 1.4.2 requires control over auto-playing audio longer than 3 seconds. Respect `prefers-reduced-motion` and data-saver settings for autoplaying media. Browsers also block autoplay with sound by default.
- Pull to refresh: on the web, avoid fighting the browser's native overscroll refresh (`overscroll-behavior`), and always provide a visible refresh control as an alternative to the gesture (gesture-only actions fail for keyboard and switch users).
- The "slot machine" and "dopamine" framing is a popular simplification of variable-ratio reinforcement; the numbers 0.5 s and 3 s are illustrative, not research values.
