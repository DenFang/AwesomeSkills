---
id: unknown
reel_url: unknown
pattern_page: https://designmotionhq.com/patterns/depth-layers
date: unknown
duration_s: 43
type: ui
category: visual
topic: depth illusion with layered shadows, parallax and hover lift
sources: frames, voice-over, pattern page
---

# Depth layers: three properties that turn a flat list into depth

**Caption:** none (this video is published on the pattern page only; no matching reel on the Instagram profile as of 2026-10-24)
**Hook:** The same flat UI, with the same layout and colours, gains depth one property at a time.

## Main rule
Create depth without redesigning: stack several soft shadows of increasing size instead of one drop
shadow, move background layers slower than foreground on scroll, and lift the hovered element toward
the viewer with a small Z translation plus about 3% scale.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 3 | number of properties/techniques used (shadows, parallax, Z lift) | 0:03 on-screen "3 properties. That's it." + voice |
| 2px "tight" | first (contact) shadow layer | 0:07 on-screen label; page "~2px" |
| 12px "spread" | second (mid) shadow layer | 0:08 on-screen label; page "~12px" |
| 32px "ambient" | third (large, soft) shadow layer | 0:10 on-screen label; page "~32px" |
| decreasing opacity | each larger shadow layer is fainter | voice 0:05-0:12 (no opacity values shown) |
| 1x BG / 2.5x MID / 5x FG | relative scroll speed of background, midground, foreground layers | 0:17-0:22 on-screen; page "roughly 1x / 2.5x / 5x" |
| `translateZ(20px)` | hover lift distance | 0:25-0:31 on-screen code caption |
| `scale(1.03)` | hover scale (about 3%) | 0:25-0:31 on-screen code caption; page "~3% scale" |
| 4 | cards in the demo list (Dashboard, Messages, Settings, Profile) | throughout |

No durations or easing values are shown.

## Before / after
1. **Flat vs depth (side by side).** Bad: four nav cards as plain filled rectangles with muted labels,
   no shadow; they read as one painted surface. Good: the same cards with layered shadows and
   slightly brighter labels/borders; each card reads as an object sitting above the background. Why:
   the visual system infers height from shadow; separating card from background makes each item a
   distinct, tappable thing. (Note: the depth version also raises label brightness, so "same colours"
   is not strictly true.)
2. **One shadow vs layered shadows.** Bad (implied): a single drop shadow. Good: three shadows stacked
   on each card, tight 2px, mid 12px, ambient 32px, each larger one fainter (shown as 1, 2, 3 dots
   per card as layers are added). Why: real light gives a sharp dark contact shadow near the object
   and a wide faint penumbra further out; one shadow can only imitate one of these, so it looks
   pasted on.
3. **Static vs parallax scroll.** Good: background panels ("Hero Section", "Features") scroll at 1x,
   a middle layer at 2.5x and the foreground cards at 5x relative speed. Why: motion parallax is a
   strong depth cue; closer things move faster across the eye, so speed differences read as
   distance.
4. **No hover vs Z lift.** Good: the hovered card scales up slightly, its border and label brighten
   and a soft glow appears, with `transform: translateZ(20px) scale(1.03)`; the lift follows the
   pointer card by card. Why: the element reacts to the pointer like a physical object rising toward
   the hand, which confirms it is interactive and which item is targeted.

## Do
- Stack 2-3 shadows of increasing blur/offset and decreasing opacity (e.g. about 2px, 12px, 32px).
- Give parallax layers clearly different speeds (background slowest, foreground fastest).
- Keep the hover lift small: a few pixels of lift and about 3% scale.
- Reinforce the lifted state with a brighter border or stronger shadow, not only movement.
- Combine the three cues; together they read as dimensional while the layout stays clean.

## Don't
- Don't use a single hard drop shadow as the only depth cue.
- Don't redesign layout or palette to fake depth when shadows and motion already do it.
- Don't push parallax offsets or hover scale so far that the motion pulls attention from content.

## Scene by scene
- 0:00 Title "Same layout. Same colors." with two column labels "FLAT" and "DEPTH" and a divider.
- 0:01 Two copies of a 4-item nav list (Dashboard, Messages, Settings, Profile): flat on the left, shadowed with brighter labels on the right.
- 0:03 Caption "3 properties. That's it." under the comparison; held to 0:04.
- 0:05 Badge "LAYER 1 / Layered Shadows"; a single faint card fades in.
- 0:06 Four full-width flat cards.
- 0:07 First shadow added, one dot per card, label "2px tight".
- 0:08 Second shadow, two dots, label "12px spread".
- 0:10 Third shadow, three dots, label "32px ambient"; held to 0:14.
- 0:15 Badge "LAYER 2 / Parallax Scroll": background panels "Hero Section" and "Features" behind three foreground cards.
- 0:17 Speed legend "1x BG, 2.5x MID, 5x FG"; on scroll the foreground cards travel faster than the background panels; continues to 0:22.
- 0:23 Badge "LAYER 3 / Z-Translation on Hover" fades in, then four cards.
- 0:25 Cursor over Dashboard: card scales up, border and label brighten, soft glow; code caption "transform: translateZ(20px) scale(1.03)".
- 0:26 Lift moves to Messages, then Settings (0:28), then Profile (0:30); 0:31 pointer leaves, all cards rest.
- 0:33 Badges "Shadows + Parallax + Z-Translation" build up; cards gain subtitles (Analytics overview, 3 unread, Preferences, Edit account); full combined state held to 0:39.
- 0:40 End card "Save this." and "Follow for more motion design tricks."

## Voice-over summary
- Starts from a completely flat UI and adds one property at a time.
- Layer 1: layered box shadows with decreasing opacity, not a single drop shadow; claims this adds more depth than any gradient.
- Layer 2: parallax on scroll, background slower than foreground, which the brain reads as physical space.
- Layer 3: Z translation on hover so elements lift toward the viewer; with the shadows it feels like reaching into the screen.
- Three CSS properties, "No WebGL. No libraries.", just a depth illusion.

## Notes for the skill
- Layered shadow pattern: three comma-separated `box-shadow` layers using the theme's shadow colour token, e.g. blur 2px / 12px / 32px with growing Y offset and opacity falling from the first layer to the last. The reel labels only the sizes (2/12/32px); offsets and opacities are not shown, so treat them as a starting scale. Define them as elevation tokens (e.g. `--shadow-1..3`) rather than per-component values.
- Dark themes: shadows are barely visible on a dark background; pair them with a slightly lighter surface or a subtle border per elevation level (as the reel's depth column does).
- `translateZ(20px)` has no visible effect unless an ancestor sets `perspective` (or the transform includes `perspective()`); without it only `scale(1.03)` is doing the work. Add `perspective: 800-1200px` on the container if the Z lift is meant to read.
- Animate `transform` and `opacity`, not `box-shadow`, for smooth hover: put the stronger shadow on a pseudo-element and fade its opacity.
- Hover is pointer-only: gate with `@media (hover: hover)` and give keyboard users the same lift on `:focus-visible`; touch users need a pressed state instead.
- Parallax can trigger vestibular discomfort: disable or reduce it under `prefers-reduced-motion: reduce` (WCAG 2.3.3 Animation from Interactions). Prefer CSS scroll-driven animations or `transform` updated in `requestAnimationFrame`; never animate `top`/`background-position` on scroll.
- The 1x/2.5x/5x figures are relative speeds between layers, not absolute scroll multipliers; a foreground moving 5x faster than the page scroll would be disorienting. Usually the foreground moves with scroll (1x) and background layers move at a fraction of it.
- The claim "more depth than any gradient" is opinion, not a measured result.
