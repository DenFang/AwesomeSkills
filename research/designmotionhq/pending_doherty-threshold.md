---
id: unknown
reel_url: unknown
pattern_page: https://designmotionhq.com/patterns/doherty-threshold
date: unknown
duration_s: 30
type: ui
category: feedback
topic: Doherty Threshold (400 ms) and perceived-speed techniques
sources: frames, pattern page
---

# Doherty Threshold: respond within 400 ms, or fake it well

**Caption:** not captured yet
**Hook:** A Submit button press starts a counter that climbs through success, warning and danger-coloured zones until it hits 400 ms, where "your user disconnects".

## Main rule
Every interaction must produce visible feedback within 400 ms. When the real work takes longer, keep perceived response under the threshold with a skeleton (for loading screens), an optimistic update (for actions that almost always succeed) or determinate progress (for long tasks).

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 400 ms | Doherty Threshold: beyond it the user "disconnects" | 0:04-0:07 on-screen; page |
| 155 ms (success colour), 315 ms (warning colour), 400 ms (danger colour) | counter samples illustrating the three zones | 0:02-0:04 on-screen |
| < 200 ms instant · 200-400 ms tolerable · > 400 ms breaks engagement | response-time zones | page only (the video shows them as a three-segment success/warning/danger bar under "Doherty threshold", 0:06-0:07, without labels) |
| 0 ms → 240 → 540 → 800 ms, label "Feels ~200ms" | skeleton demo: same 800 ms load; the skeleton version is claimed to feel like about 200 ms | 0:08-0:12 on-screen |
| 40 → 340 → 640 → 800 ms vs "Response: 0ms", "Server confirmed in background" | optimistic like vs waiting for server | 0:13-0:16 on-screen |
| 350 → 1100 → 1850 → 2000 ms vs 22% → 73% → 94% → 100% | progress feedback demo (spinner vs determinate bar with steps Upload / Process / Done) | 0:18-0:21 on-screen |
| "< 400ms or the illusion of it" | closing rule | 0:26-0:29 on-screen |

No voice-over (music only), so all values come from on-screen text and the page.

## Before / after
1. **Skeleton loading (0:08-0:12).** Without: an empty card with a faint "..." until content arrives at 800 ms. With: placeholder shapes (avatar, title lines, image block, text lines) with a shimmer appear at 0 ms; label "Feels ~200ms". Why: the screen changes immediately, so the system is visibly responding; the layout shape also previews what is coming, which lowers uncertainty during the wait.
2. **Optimistic UI (0:13-0:16).** Without: tapping like shows a spinner ring for 800 ms before the heart fills. With: the heart fills at 0 ms, "Response: 0ms", and a muted note "Server confirmed in background". Why: the user's action gets an immediate acknowledgment; the network round trip still happens but is hidden because success is almost certain.
3. **Progress feedback (0:18-0:22).** Without: an indeterminate spinner for 2000 ms with nothing else. With: "Uploading..." with a percentage bar (22% → 100%), a step list (Upload ✓, Process ✓, Done) and "Complete!" at the end; tag "User stays engaged". Why: a determinate indicator shows that work is advancing and roughly how much remains, so an unavoidable wait does not look stalled.
4. **Wipe comparison (0:23-0:25).** A vertical divider sweeps across one card labelled Without / With: the "without" side is blank, the "with" side shows skeleton blocks, then content (unclear on screen whether it shows final content or the skeleton at full contrast).

## Do
- Acknowledge every click/tap/key within 400 ms (pressed state, skeleton, optimistic change or progress).
- Show a skeleton matching the final layout as soon as a screen opens.
- Apply optimistic updates to cheap, reversible, almost-always-successful actions (like, favourite, toggle).
- Use a determinate progress bar with named steps when the real work clearly exceeds the threshold (uploads, processing).

## Don't
- Don't leave the screen blank or frozen while data loads.
- Don't block the visual response on a server round trip.
- Don't rely on a bare indeterminate spinner for multi-second tasks.

## Scene by scene
- 0:00 A single Submit button on a dark background; it is pressed.
- 0:02 A millisecond counter replaces the button: 155 ms in a success-coloured glow, 315 ms in a warning-coloured glow, 400 ms in a danger-coloured glow.
- 0:05 "400 ms · After this, your user disconnects"; label "Doherty threshold" with a three-segment zone bar (success / warning / danger).
- 0:08 "Skeleton loading" split cards Without / With; both timers run to 800 ms; the With side shows shimmering placeholders and "Feels ~200ms".
- 0:13 "Optimistic UI": Without shows a spinner ring until the heart appears at 800 ms; With shows the filled heart at 0 ms with "Server confirmed in background".
- 0:17 "Progress feedback": Without spinner runs to 2000 ms; With shows an upload bar 22% → 73% → 94% → 100% "Complete!" with Upload / Process / Done steps and "User stays engaged".
- 0:22 Wipe transition on a single card: divider sweeps, blank side vs skeleton/content side.
- 0:26 Closing: "< 400 ms · or the illusion of it." with three chips appearing: Skeleton, Optimistic, Progress; handle shown.

## Voice-over summary
- No voice-over: the transcript contains only a filler line from the transcriber over music, so there is no narration to summarise.
- On-screen message: 400 ms is the attention limit; skeletons, optimistic UI and progress feedback keep perceived response under it.

## Notes for the skill
- Origin and accuracy: the Doherty Threshold comes from Doherty & Thadani (IBM, 1982), who found productivity rose sharply when system response was under about 400 ms. It is a guideline from terminal work, not a hard perceptual cliff. The page's zones (< 200 ms instant) differ from the more common Nielsen limits: about 100 ms feels instant, about 1 s keeps flow, about 10 s is the limit of attention. Use 100 ms as the target for direct-manipulation feedback (pressed state, toggle), 400 ms as the ceiling for any visible response.
- "Feels ~200ms" for an 800 ms skeleton load is an illustrative claim, not a measurement shown in the video.
- Skeleton: match final layout dimensions to avoid layout shift (CLS); set `aria-busy="true"` on the loading region and provide a text alternative ("Loading posts") for screen readers; stop shimmer under `prefers-reduced-motion: reduce` (keep a static placeholder).
- Avoid flashing loaders: if a response usually arrives fast, delay showing a spinner/skeleton by ~200-300 ms and, once shown, keep it a minimum time (~300-500 ms) so it does not flicker.
- Optimistic UI needs a rollback path: keep previous state, revert and show an error message if the server rejects; never use it for payments or irreversible actions (see behind-the-button).
- Progress: use a determinate bar when progress is measurable; expose it with `role="progressbar"` and `aria-valuenow`/`aria-valuemin`/`aria-valuemax`, and announce completion in a polite live region.
