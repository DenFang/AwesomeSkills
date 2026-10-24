---
id: unknown
reel_url: unknown
pattern_page: https://designmotionhq.com/patterns/accordion-disclosure
date: unknown
duration_s: 54
type: ui
category: interaction
topic: accordion / disclosure expand-collapse
sources: frames, voice-over, pattern page
---

# Accordion and disclosure: smooth height, synced chevron, real button

**Caption:** none (this video is published on the pattern page only; no matching reel on the Instagram profile as of 2026-10-24)
**Hook:** Two identical accordions side by side; one opens with a smooth height transition, the other snaps open. Four small rules make the difference.

## Main rule
Animate the panel through an animatable property (grid rows `0fr` to `1fr`, or a measured pixel height), drive the chevron from the exact same duration and easing as the panel, render the header as a real `<button>` with `aria-expanded` / `aria-controls`, and keep the clicked header anchored in place while content fades in.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| `height: auto` (struck out) | does not transition, snaps | 0:03-0:13 code card |
| `display: grid; grid-template-rows: 0fr` to `1fr` | collapsed / expanded panel | 0:03-0:13 code card, voice |
| `transition: 0.3s` | panel open/close duration in the demo code | 0:03-0:13 code card |
| scrollHeight measured, animate to px | fallback when grid is not used | 0:03-0:13 caption, voice |
| 0 frame lag | chevron vs panel, good version | 0:15-0:22 chart label |
| 10 frames late | chevron lagging the panel, reads as broken | 0:15-0:22 chart label; page says "~10 frames" and "even a few frames" |
| 1 open at a time | accordion (sequential steps) | 0:23-0:31 |
| many open | disclosure group (FAQ) | 0:23-0:31 |
| Tab = focus, Enter = toggle, Space = toggle | header keyboard contract | 0:32-0:41 key caps |

## Before / after
- **`height: auto` vs grid rows.** Bad: transitioning `height` from `0` to `auto`; the browser cannot interpolate to an intrinsic keyword, so the panel jumps open. Good: the panel is a grid whose single row animates `0fr` to `1fr` (child needs `min-height: 0` / `overflow: hidden`), or JS measures `scrollHeight` and animates to that pixel value. Why: both give the browser two numeric endpoints to interpolate, so the motion shows where the content came from.
- **Chevron in sync vs chevron lagging.** Bad: chevron rotation starts or settles about 10 frames after the panel (separate duration, delay or curve). Good: same duration, same easing, same start, so the curves overlap (0 frame lag). Why: the chevron is the state indicator; when it drifts from the panel the eye sees two unrelated motions and reads it as a glitch rather than one object changing state.
- **Accordion vs disclosure group.** Not good/bad but a choice by content: sequential steps (shipping, payment, review) keep one panel open; FAQ items let several stay open so users can compare answers.
- **Div vs button.** Bad: a clickable `div` header, unreachable by Tab, silent to screen readers. Good: `<button>` with `aria-expanded="true|false"` and `aria-controls="panel-1"` pointing at the panel id. Why: native focus, Enter/Space activation and announced state come for free.
- **No anchor vs anchored.** Bad: opening an item near the bottom of a scroll container shifts the list so the clicked header moves away and upper items scroll out of view. Good: the clicked header stays at the same screen position, the panel opens below it and its lines fade/stagger in. Why: the user's point of attention stays put; height growth alone with no content motion feels empty.

## Do
- Use `grid-template-rows: 0fr -> 1fr` (or measured px) for the panel transition.
- Share one duration and one easing token between panel height and chevron rotation; start them in the same frame.
- Choose single-open for ordered steps, multi-open for reference lists like FAQs.
- Use a `<button>` header with `aria-expanded` and `aria-controls`; keep a visible focus ring.
- Keep the activated header anchored when the list is scrollable; fade or stagger the revealed content after height starts.

## Don't
- Don't transition `height: auto` and expect motion.
- Don't give the chevron its own delay, duration or curve.
- Don't use a clickable `div` for the header.
- Don't let the list jump under the cursor when a lower item expands.

## Scene by scene
- 0:00 Two accordions side by side (refund, shipping, cancel questions); cursor clicks the first item on both; overlay "One glides. One jumps."
- 0:03 Label "The height trap", title says height auto cannot be animated; a single FAQ item opens and closes repeatedly above a code card: `.panel { height: auto (struck out); display: grid; grid-template-rows: 0fr/1fr; transition: 0.3s; }`; footer: no grid, measure scrollHeight and animate to px.
- 0:14 Title "Rotate the chevron WITH the panel." Two cards "In sync" vs "Chevron lags" with timing curves: panel and chevron overlapping (0 frame lag) vs chevron curve offset (10 frames late, feels broken); both cards open/close.
- 0:23 Title "One at a time, or many open?" Left: Accordion (one at a time) with numbered checkout steps, opening step 2 closes step 1. Right: Disclosure (many open) FAQ where all three answers end up open. Footer: steps stay single, FAQs let many breathe.
- 0:32 Label "Accessibility", title "It's a button, not a div." FAQ item showing `aria-expanded = false/true` under the header and `aria-controls = "panel-1"` linking to the panel; key caps Tab (focus), Enter (toggle), Space (toggle) highlight as the item toggles.
- 0:41 Title "Anchor the scroll. Stagger the content." Two "Help Center" lists: "No anchor" (opening "Update my payment method" scrolls the list so earlier rows go off the top) vs "Anchored" (rows above stay put, panel lines appear below the header).
- 0:50 Outro: follow / save call to action.

## Voice-over summary
- Height `auto` cannot be animated; the browser just snaps.
- Animate grid rows from zero to one fraction, or measure scrollHeight and animate to pixels.
- The chevron must rotate with the panel, same duration and same easing; when they drift, the whole component feels broken.
- One open at a time is an accordion, many open is a disclosure group; pick by content (steps single, FAQs many).
- Header is a button; `aria-expanded` announces state, `aria-controls` points to the panel, so keyboard and screen reader both work.
- Anchor scroll to the clicked header, then fade the content in: "Height alone feels hollow."

## Notes for the skill
- Grid technique: `.panel { display: grid; grid-template-rows: 0fr; transition: grid-template-rows var(--dur) var(--ease); } .panel[data-open] { grid-template-rows: 1fr; } .panel > .inner { min-height: 0; overflow: hidden; }`. Put the chevron `transform: rotate()` on the same `var(--dur) var(--ease)`.
- The claim "you can't animate height auto" is no longer universally true: Chromium supports `interpolate-size: allow-keywords` and `calc-size()`. Treat these as progressive enhancement; grid rows or measured px remain the cross-browser default.
- Collapsed content must not be focusable or read: use `hidden` / `inert` (or `visibility: hidden` after the transition ends), not only a zero row height.
- WAI-ARIA APG accordion: the button sits inside a heading element of appropriate level; panel may be `role="region"` with `aria-labelledby` pointing to the button (avoid region for many panels, >6). Enter/Space toggle; Up/Down/Home/End between headers are optional extras. Native `<details>/<summary>` is an acceptable disclosure alternative (multi-open; `name` attribute makes it exclusive in modern browsers).
- Anchoring: CSS `overflow-anchor` handles some cases; otherwise record the header's `getBoundingClientRect().top` before opening and correct `scrollTop` after layout. Do not auto-scroll the page away from the clicked control.
- Reduced motion: under `prefers-reduced-motion: reduce`, drop the height transition and stagger (instant or short opacity fade), keep the chevron state change.
- The 0.3s value is a demo value from the code card, not a stated rule.
