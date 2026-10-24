---
lesson: 027
kind: video
duration_s: 42
type: ui
category: feedback
topic: skeleton screens vs spinners: shimmer direction, content-aware shapes, optimistic UI
sources: frames, voice-over, lesson notes
---

# Skeleton loading instead of spinners

**Hook:** Same loading time, completely different feeling: a spinner versus a skeleton.

## Main rule
For content loads, replace the spinner with a skeleton that mirrors the real layout (avatar circle, short name line, long text lines, media block), animate it with a shimmer that sweeps in reading direction, and swap it for content without layout shift. For actions the user just performed (like, post), skip loading entirely and update optimistically with rollback on failure.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| Perceived 2.4 s (generic skeleton) vs 1.2 s (content-aware skeleton) | same 2-second load | 0:27-0:28 on-screen ("Same 2 seconds. Different perception.") |
| 2 seconds | actual load time in the comparison | 0:27-0:28 on-screen |
| 142 → 143 likes, "INSTANT" | optimistic like | 0:29-0:31 on-screen |
| User sees 0 ms vs server reality 200 ms | optimistic update vs real request/response | 0:35-0:36 on-screen ("The gap is invisible.") |
| Left → right ("Natural ✓") vs right → left ("Reversed ✗") | shimmer sweep direction | 0:12-0:17 on-screen + voice |
| ~2 s | maximum skeleton duration before showing partial content | page only |
| < 300 ms | loads too short for a skeleton (flash is noise) | page only |

The "perceived" seconds are illustrative labels, not measurements shown with a method.

## Before / after
1. **Spinner vs skeleton (0:00-0:02).** Spinner card: a ring spins above grey text bars; Skeleton card: placeholder shapes of the post. Both resolve to the same post at the same time: "Same time. Different feel." Why: the spinner says only "wait" (no information on what or how long), while the skeleton previews the structure, so the brain starts parsing the layout before data arrives; uncertainty, not duration, makes waits feel long.
2. **Waiting vs predicting (0:03-0:10).** A "Waiting" spinner ring raises a Stress meter; a "Predicting" skeleton ring raises an Engagement meter; "WAIT." vs "HERE'S WHAT'S COMING."; "Anxiety" turns into "Anticipation". Why: a preview lets users form expectations, which turns idle waiting into active anticipation.
3. **Shimmer direction (0:11-0:17).** Two identical skeleton cards: one shimmers left to right ("Natural ✓"), one right to left ("Reversed ✗", which then dims). Caption "Follow the reading flow". Why (as claimed): the sweep follows the eye's reading direction, so it reads as progress; reversed motion feels subtly wrong.
4. **Generic vs content-aware (0:18-0:28).** Generic ("Lazy"): three equal full-width bars and a block that do not match the post. Content-aware ("Smart"): avatar circle, short name line, small meta line, two long text lines, media block, row of action dots. When data arrives the content-aware skeleton maps 1:1 onto the post; perceived 2.4 s vs 1.2 s. Why: the closer the preview matches the real content, the less re-orientation and layout jump at swap time, so the load feels faster.
5. **Optimistic UI, "the beautiful lie" (0:29-0:36).** Tapping like fills the heart and increments 142 → 143 instantly. Success path: Click → Show result → Server confirms. Failure path: Click → Show result → Server fails → heart reverts to 142 and a "Something went wrong" message appears. Why: the user sees the result at 0 ms while the server takes 200 ms; rollback keeps the UI honest when the rare failure happens.

## Do
- Use skeletons for content areas whose structure is known (feeds, cards, lists, profiles).
- Shape skeleton elements like the real content: circle for avatars, short line for names, long lines for body text, block for media, same dimensions.
- Animate the skeleton with a subtle shimmer moving in reading direction.
- For user-initiated reversible actions, show the result immediately and reconcile in the background; roll back and show an error on failure.

## Don't
- Don't show a bare spinner for content loads where the layout is predictable.
- Don't use generic uniform bars that do not match the final layout.
- Don't run the shimmer against reading direction.
- Don't flash a skeleton for very short loads, or mix spinners and skeletons in one view (page).

## Scene by scene
- 0:00 Two small cards labelled "Spinner" and "Skeleton"; both resolve to the same post (author "Sarah Chen", two text lines, image). Caption "Same time. Different feel."
- 0:03 "Secret 01 · The brain · Prediction machine": a "Waiting" spinner ring with a filling Stress bar; a "Predicting" ring holding a mini skeleton with an Engagement bar.
- 0:07 Split screen "WAIT." vs "HERE'S WHAT'S COMING."; then "ANXIETY ↓ ANTICIPATION".
- 0:11 "Secret 02 · Shimmer direction · Reading flow matters": two skeleton posts, top tagged "→ Natural ✓", bottom "← Reversed ✗"; bottom card fades; caption "Follow the reading flow".
- 0:18 "Secret 03 · Content-aware · Match the shape to the content": "Generic / Lazy" skeleton (uniform bars) vs "Content-aware / Smart" skeleton (avatar, name, text, media, actions).
- 0:26 Both fill with the real post; progress bars "Perceived: 2.4s" vs "Perceived: 1.2s"; "Same 2 seconds. Different perception."
- 0:29 "Secret 04 · Optimistic UI · The beautiful lie": cursor taps the heart on a post; count 142 → 143 with an "INSTANT" tag.
- 0:32 Two timelines: Success (Click, Show result, Server confirms, 143) and Failure (Click, Show result, Server fails, back to 142, "Something went wrong").
- 0:35 "User sees: Click → Result, 0ms" vs "Server reality: Click → Request → Response, 200ms"; "The gap is invisible."
- 0:37 Summary chain: Waiting → Previewing → Anticipating.
- 0:40 Outro "Design Psychology", follow button.

## Voice-over summary
- The brain hates waiting but loves predicting: a spinner says wait, a skeleton says what is coming, turning anxiety into anticipation.
- Shimmer should run left to right, in reading direction, so the eye follows it; reversed, something feels off.
- Generic rectangles are lazy: match the skeleton to the real content (circle for avatars, short line for names, long lines for text); the closer the preview, the faster it feels.
- Next level is not waiting at all: show a like instantly and roll back if the server fails; "The UI lies, but it feels honest."

## Notes for the skill
- Reading direction depends on locale: in RTL interfaces (`dir="rtl"`) the shimmer should sweep right to left. Implement with logical direction (flip the gradient keyframes under `:dir(rtl)`). The claim that reversed shimmer "feels off" is plausible but not research-backed; treat direction as a consistency detail, not a core rule.
- Reduced motion: under `prefers-reduced-motion: reduce` replace the shimmer with a static placeholder or a very slow opacity pulse. The page's statement that a static skeleton reads as "broken" should not override this accessibility requirement.
- Accessibility: mark the loading region `aria-busy="true"`, hide decorative skeleton shapes from assistive tech (`aria-hidden="true"`), and provide one text status ("Loading posts..."). Remove `aria-busy` when content arrives.
- Avoid CLS: reserve the exact final dimensions (fixed image aspect-ratio boxes, line heights matching real text). A skeleton that jumps to a different layout on load is worse than a spinner (page).
- Timing (page): skip skeletons for loads under about 300 ms; if loading runs past about 2 s, show partial content progressively instead of holding the full skeleton. Skeleton tone should be a subtle surface step from the background, not high-contrast blocks.
- Spinners still fit unknown-shape or action-level waits (submitting a form, processing); use determinate progress for long tasks.
- Optimistic UI only for cheap, reversible actions that almost always succeed; never for payments or destructive actions. The failure message should say what failed ("Couldn't save your like. Try again") rather than a generic "Something went wrong".
