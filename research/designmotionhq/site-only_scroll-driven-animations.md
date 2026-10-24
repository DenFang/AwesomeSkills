---
id: unknown
reel_url: unknown
pattern_page: https://designmotionhq.com/patterns/scroll-driven-animations
date: unknown
duration_s: 39
type: ui
category: motion
topic: CSS scroll-driven animations (scroll(), view(), animation-range, parallax, sticky combos)
sources: frames, voice-over, pattern page
---

# Scroll-driven animations in pure CSS

**Caption:** none (this video is published on the pattern page only; no matching reel on the Instagram profile as of 2026-10-24)
**Hook:** Two pages with the same scroll; only the one with scroll-linked motion feels alive.

## Main rule
Tie scroll-linked motion to native CSS timelines instead of scroll listeners: `animation-timeline:
scroll()` for page-level progress, `animation-timeline: view()` for per-element reveals,
`animation-range` to choose exactly where in the element's entry/exit the animation runs, and
combine with `position: sticky` for progress bars and transforming headers or sidebars.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 2 lines of CSS | `animation: fade-in;` + `animation-timeline: scroll();` | 0:06-0:09 on-screen chip + voice |
| "15 more lines" | elided remainder of the JS scroll-listener version | 0:05-0:09 on-screen code comment |
| ~30 lines of JS | old parallax implementation with a scroll listener | 0:21 voice, page "~30 lines" |
| `entry 0%` / `entry 100%` / `exit` | range markers: element touching the viewport bottom / element fully entered / leaving at the top | 0:10-0:15 on-screen diagram |
| `animation-range: entry 0% entry 100%;` | reveal runs only while the element enters | 0:13-0:15 on-screen code |
| `const speed = 0.5` | parallax factor in the JS version | 0:23-0:28 on-screen code |
| `animation-range: 0% 100%;` + `translate: 0 var(--offset);` | CSS-only parallax snippet | 0:23-0:28 on-screen code |
| 12.4k / 891 / 234 | example stats in the view() card list (content, not a rule) | 0:17-0:21 on-screen |
| 4 | numbered sections in the combined docs demo (Introduction, Core Concepts, Examples, Advanced) | 0:29-0:35 on-screen |

No durations or easing values are shown (scroll position drives progress).

## Before / after
1. **Static vs animated scroll.** Bad: a page whose cards just slide past. Good: the same page where
   cards fade/scale in as they arrive and a progress bar tracks position. Why: motion linked to the
   user's own scroll gives continuous feedback about position and makes new content noticeable at
   the moment it appears.
2. **Scroll listener vs scroll timeline.** Bad: `window.addEventListener("scroll", ...)` calling
   `el.getBoundingClientRect()` plus about 15 more lines (struck through). Good: `.element {
   animation: fade-in; animation-timeline: scroll(); }`. Why: the browser drives the animation from
   scroll position itself, off the main thread where possible, with no layout reads per scroll
   event and no JavaScript to maintain.
3. **When it starts.** `animation-range: entry 0% entry 100%` makes the animation run from the moment
   the element's top edge touches the bottom of the viewport until it is fully inside; it is finished
   before the element reaches the middle and does nothing in the exit zone. Why: the reveal completes
   while the user is still looking at the incoming area, instead of being spread across the whole page.
4. **Per element.** With `view()` each card (profile, stats, hero, feature, call to action) animates
   individually as it scrolls into view. Why: every element gets its own timeline, so no observer
   bookkeeping is needed.
5. **Parallax.** Bad: JS listener multiplying `window.scrollY` by `speed = 0.5` and writing
   `translateY` each event. Good: CSS-only layers with `animation-timeline: scroll()`,
   `animation-range: 0% 100%`, different translate offsets per layer (mountain layers in a landing
   hero move at different speeds). Why: different speeds per layer create depth, and the browser
   keeps it in sync with scroll without jank.
6. **Combine with sticky.** A docs page with a sticky header, a reading-progress line under the
   header, and a side indicator that highlights the current section (Introduction → Core Concepts →
   Examples → Advanced). Voice also mentions shrinking headers and transforming sidebars.

## Do
- Use `animation-timeline: scroll()` for page or container progress (reading bars, header changes).
- Use `animation-timeline: view()` for elements that should animate when they enter or leave the viewport.
- Set `animation-range` (e.g. `entry 0% entry 100%`) so reveals finish while the element enters.
- Build parallax with different translate distances per layer on a scroll timeline.
- Combine scroll timelines with `position: sticky` for progress bars, shrinking headers and section indicators.

## Don't
- Don't hand-roll reveals or parallax with a scroll listener and `getBoundingClientRect()` when CSS can drive them.
- Don't add a JS animation library for effects the browser handles in a couple of CSS lines.

## Scene by scene
- 0:00 Title "Same scroll. One feels alive."; two browser mocks scrolling side by side, labelled STATIC and ANIMATED.
- 0:02 Section "SCROLL-TIMELINE": one browser scrolls while a progress bar along its top fills.
- 0:05 Code card "JAVASCRIPT": scroll listener with `getBoundingClientRect()` and "// 15 more lines...".
- 0:06 Code card "CSS": `.element { animation: fade-in; animation-timeline: scroll(); }` with `scroll();` highlighted.
- 0:07 The JS card is struck through and dimmed.
- 0:08 Chip "2 lines of CSS".
- 0:10 Section "ANIMATION-RANGE": a VIEWPORT box with markers "entry 0%" (bottom edge), "entry 100%" (mid line) and "exit" (top band).
- 0:11 A small card enters from the bottom; the band between entry 0% and entry 100% lights up.
- 0:12 Card reaches the entry 100% line fully animated.
- 0:13 Code `animation-range: entry 0% entry 100%;` appears; card moves up toward the exit band.
- 0:14 Card leaves through the exit band; 0:15 empty viewport.
- 0:16 Section "VIEW()": a scrolling list of cards (profile, weekly stats, hero section, auto-animate, get started) each fading/sliding in as it enters; caption "Each element animates on scroll into view."; to 0:21.
- 0:22 Landing-page mock "Premium Landing Page / Scroll-driven parallax with zero JavaScript" with layered mountain shapes moving at different speeds.
- 0:23 Code cards: JAVASCRIPT (scroll listener, `speed = 0.5`, `translateY(${y * speed}px)`) vs CSS ONLY (`animation-timeline: scroll(); animation-range: 0% 100%; translate: 0 var(--offset);`).
- 0:25 JS card marked ✗ and dimmed, CSS card marked ✓; page keeps scrolling to 0:28.
- 0:29 Section "COMBINE EVERYTHING": docs app with a sticky top bar, progress line under it, numbered sections and a right-side dot indicator labelling the active section; scrolls through sections 1-4 to 0:35.
- 0:37 End card "CSS > JavaScript", "Follow @designmotionhq", Follow and "Save for later" buttons.

## Voice-over summary
- A scroll timeline turns the scrollbar into an animation controller, with no JavaScript and no Intersection Observer, in two lines of CSS.
- `animation-range` picks the exact trigger point: entry, exit, or anywhere in between.
- `view()` targets individual elements, so each card or image animates when it enters the viewport.
- Parallax that used to need about 30 lines of JS in a scroll listener is now pure CSS with different speeds and zero dependencies.
- Combining sticky positioning with scroll animations gives shrinking headers, reading-progress bars and sidebars that transform on scroll.

## Notes for the skill
- Minimal reveal: `@keyframes reveal { from { opacity: 0; translate: 0 24px; } }` then `.card { animation: reveal linear both; animation-timeline: view(); animation-range: entry 0% entry 100%; }`. Put `animation-timeline` after the `animation` shorthand, because the shorthand resets it.
- The reel's simplifications: the "scroll()" fade-in example maps the whole page scroll to one element's fade (usually you want `view()` for reveals); the parallax snippet `translate: 0 var(--offset)` does nothing by itself, a `@keyframes` rule must animate `translate` from 0 to the offset for each layer.
- Browser support is not universal: guard with `@supports (animation-timeline: view())` (or `scroll()`) and make sure content is fully visible without it (start from the final state, add the hidden "from" state only inside `@supports`). Check current Firefox support before relying on it.
- Respect `prefers-reduced-motion: reduce`: remove parallax and large translations, keep at most an opacity change. Parallax is a known vestibular trigger (WCAG 2.3.3).
- Never hide content until it scrolls in without a fallback: printing, find-in-page, screen readers and fast scrolling must still see it.
- Prefer animating `transform`/`translate`/`opacity` (compositor-friendly); avoid animating layout properties on a scroll timeline.
- Reading progress bar: `animation: grow linear; animation-timeline: scroll(root);` on a fixed/sticky bar scaling `scale: 0 1` → `1 1` with `transform-origin: left`. Expose it as decorative (`aria-hidden`) or give it `role="progressbar"` with values only if it carries information.
- Section indicator (scroll spy) needs the active section exposed to assistive tech (e.g. `aria-current` on the TOC link), which pure CSS timelines cannot set; that part still needs JS or an IntersectionObserver.
