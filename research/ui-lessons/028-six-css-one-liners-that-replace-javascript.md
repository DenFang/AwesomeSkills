---
lesson: 028
kind: carousel
type: ui
category: css
topic: CSS one-liners replacing JS (smooth scroll, dark mode, truncation, sticky, scroll snap, system accent colour keywords)
sources: video slide (slide 1 of 8, cover), image slides 2-8
---

# Six CSS one-liners that replace JavaScript

**Hook:** The cover crosses out JavaScript and replaces it with CSS, promising 6 one-liners.

## Main rule
When JavaScript only listens to scroll, media or OS state to set a style, replace it with the declarative CSS feature that does the same thing (`scroll-behavior`, `prefers-color-scheme`, `text-overflow`, `position: sticky`, scroll snap, system colour keywords), then add the guard each one needs (reduced motion, access to the full text, contrast, a user override).

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 6 one-liners | list length, items numbered 01/06 to 06/06 | slide 1 subtitle; slides 2-7 counters |
| `top: 0`, `behavior: 'smooth'` | the JS being replaced (`window.scrollTo`) | slide 2 |
| `scroll-behavior: smooth` on `html` | smooth scroll fix | slide 2 |
| `--bg`, `--text` custom properties redefined in `@media (prefers-color-scheme: dark)` on `:root` | dark theme fix (values are a near-black background and near-white text) | slide 3 |
| 50 characters | JS truncation threshold (`text.length > 50`, `slice(0, 50) + '...'`) | slide 4 |
| `white-space: nowrap; overflow: hidden; text-overflow: ellipsis` | `.truncate` fix | slide 4 |
| `scrollY > 100` | JS sticky threshold that adds a `stuck` class | slide 5 |
| `position: sticky; top: 0` on `nav`, "2 lines" | sticky fix | slide 5 |
| `scroll-snap-type: x mandatory` / `scroll-snap-align: start` | container / item | slide 6 |
| `background: AccentColor; color: AccentColorText` on `button` | system accent fix | slide 7 |

## Before / after
Each content slide pairs a struck-through JS block (danger-coloured left edge) with a CSS block (success-coloured left edge).
- **Smooth scroll (slide 2).** Bad: `window.scrollTo({ top: 0, behavior: 'smooth' })` on each call site. Good: `html { scroll-behavior: smooth; }`. Why: the browser's own scroll machinery animates every programmatic and anchor-link scroll on that scroller, so no call site needs the option. Caveat: the CSS does not replace the scroll-to-top action itself; a `#top` link or a plain `scrollTo(0, 0)` still triggers it.
- **Dark mode (slide 3).** Bad: `matchMedia('(prefers-color-scheme: dark)')` plus a `change` listener calling `toggleTheme(e.matches)`. Good: redefine colour tokens inside `@media (prefers-color-scheme: dark) { :root { --bg: ...; --text: ...; } }`. Why: components read only tokens, the media query re-evaluates live when the OS theme changes, and there is no flash waiting for script. Caveat: the slide title says toggle, but the CSS only follows the OS; an in-page toggle still needs a stored preference and a class or attribute on the root.
- **Truncation (slide 4).** Bad: `if (text.length > 50) text = text.slice(0, 50) + '...'`. Good: `.truncate { white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }`. Why: it cuts at the real rendered width instead of a character count that ignores font, container size and glyph width, and the full string stays in the DOM for copy, search, translation and screen readers.
- **Sticky header (slide 5).** Bad: a `scroll` listener that adds `stuck` to `nav` once `scrollY > 100`. Good: `nav { position: sticky; top: 0; }`. Why: positioning is handled by layout with no per-frame script and no jump at the threshold. Caveat: the JS version also gave a stuck styling hook (e.g. a shadow); sticky alone does not, so that still needs a sentinel observer or a scroll-state query (check current support).
- **Scroll snap (slide 6).** Bad: an `IntersectionObserver` that calls `entry.target.scrollIntoView()` for intersecting entries. Good: `.container { scroll-snap-type: x mandatory; } .item { scroll-snap-align: start; }`. Why: snapping is applied by the scroller at the end of every gesture, wheel, keyboard or programmatic scroll, without fighting the user mid-scroll. The container still needs `overflow-x: auto`.
- **System accent colour (slide 7).** Bad: the JS block is only comments saying there is no clean way to detect the OS colour. Good: `button { background: AccentColor; color: AccentColorText; }`, with the note that it follows the OS theme colour. Why: these are CSS system colour keywords that resolve to the platform accent and its paired text colour. This is not the `accent-color` property (which tints native checkboxes, radios and ranges).

## Do
- Put `scroll-behavior: smooth` on the root scroller inside `@media (prefers-reduced-motion: no-preference)`.
- Keep theme colours as tokens on `:root` and swap only the tokens per scheme; also declare `color-scheme` so form controls and scrollbars follow.
- Truncate with CSS on an element that has a constrained width (block, or `min-width: 0` inside flex), and give a way to read the full text.
- Use `position: sticky; top: 0` with `scroll-padding-top` equal to the header height so anchor and focus targets are not hidden.
- Give the snap container an overflow axis and visible controls; snap is behaviour, not a carousel UI.
- When using `AccentColor`, pair it with `AccentColorText` (never your own text colour) and verify contrast.

## Don't
- Don't force smooth scrolling on users who asked for reduced motion.
- Don't truncate by character count in JS; don't truncate prices, errors or names needed to decide with no way to see the rest.
- Don't call a pure `prefers-color-scheme` rule a theme toggle; users need an override that persists.
- Don't put a sticky element inside an ancestor with `overflow: hidden` or with no room to scroll; it will not stick.
- Don't use `mandatory` snapping when items can be taller or wider than the viewport; content can become unreachable, use `proximity`.
- Don't confuse `AccentColor` (system colour keyword) with `accent-color` (form control tint).

## Slide by slide
- **Slide 1 (video cover).** Heading crossing out JavaScript and pointing to CSS, subtitle 6 CSS one-liners with an arrow. Details below.
- **Slide 2, 01/06 Smooth Scroll.**
  ```js
  window.scrollTo({ top: 0, behavior: 'smooth' }); // struck out
  ```
  ```css
  html { scroll-behavior: smooth; }
  ```
- **Slide 3, 02/06 Dark Mode Toggle.** Struck JS: `matchMedia('(prefers-color-scheme: dark)')`, `addEventListener('change', e => toggleTheme(e.matches))`.
  ```css
  @media (prefers-color-scheme: dark) {
    :root { --bg: /* near-black */; --text: /* near-white */; }
  }
  ```
- **Slide 4, 03/06 Truncate Text.** Struck JS labelled string manipulation: `if (text.length > 50) { text = text.slice(0, 50) + '...'; }`.
  ```css
  .truncate { white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  ```
- **Slide 5, 04/06 Sticky Header.** Struck JS labelled scroll listener: `if (scrollY > 100) nav.classList.add('stuck')`. CSS: `nav { position: sticky; top: 0; }`. Accent-coloured line below says it really is just 2 lines.
- **Slide 6, 05/06 Scroll Snap.** Struck JS: `new IntersectionObserver(entries => entries.forEach(entry => { if (entry.isIntersecting) entry.target.scrollIntoView(); }))`.
  ```css
  .container { scroll-snap-type: x mandatory; }
  .item { scroll-snap-align: start; }
  ```
- **Slide 7, 06/06 System Accent Color.** Struck block is three comments: OS colour detection has no clean JS solution. CSS: `button { background: AccentColor; color: AccentColorText; }`. Muted caption: matches the user's OS theme colour automatically.
- **Slide 8 (closing).** Save this for later, a question asking which one you will use first, outlined follow button.

## Video slide
Slide 1 (cover), about 3.5 s (7 frames at 2 fps), centred text on a dark background with a soft radial glow.
- 0:00 First line (stop writing) appears; the second line is still faint.
- 0:00.5 Second line visible with JavaScript in the accent colour.
- 0:01 A strike-through line crosses out JavaScript.
- 0:01.5 A small down arrow and the word CSS fade in below, in the success colour; the glow appears behind.
- 0:02-0:03 CSS brightens to full; a muted subtitle (6 CSS one-liners you need to know, with an arrow) fades in and holds.

## Notes for the skill
- Smooth scroll: WCAG 2.3.3 Animation from Interactions (AAA) and vestibular guidance mean `scroll-behavior: smooth` should sit inside `prefers-reduced-motion: no-preference`; scripted `scrollTo`/`scrollIntoView` with `behavior: 'smooth'` must follow the same preference. Smooth in-page jumps should also move focus to the target (or at least not leave it behind) so keyboard users continue from there.
- Dark mode: keep text at 4.5:1 and UI boundaries at 3:1 (WCAG 1.4.3, 1.4.11) in both schemes; check that token pairs hold in each. A user toggle overrides the OS value; store it and apply it before first paint to avoid a flash. `light-dark()` with `color-scheme` is an alternative token style; check current support.
- Truncation: the CSS needs a definite or constrained width; in a flex row the item needs `min-width: 0`. Multi-line clamping is a different technique (`line-clamp`; check current support). A `title` attribute alone is not keyboard or touch accessible; prefer a visible expand, a detail view, or a tooltip that also opens on focus. Truncated text that loses meaning when text is enlarged conflicts with WCAG 1.4.4 and 1.4.10.
- Sticky: sticks only within its containing block and fails under an ancestor with `overflow` other than visible on the wrong axis. Cap its height on small screens; a tall sticky header can hide the focused element (WCAG 2.4.11 Focus Not Obscured); `scroll-padding-top` helps.
- Scroll snap: the before/after are not equivalent; the observer version moved the page whenever an item entered view, the CSS snaps only where the user stops. Snap carousels still need keyboard reachable items, visible previous/next controls and, if they auto-advance, a pause (WAI-ARIA APG Carousel pattern).
- `AccentColor` and `AccentColorText`: system colour keywords from CSS Color 4; whether they reflect the real OS accent varies by browser and platform, so check current support and supply a fallback. The author does not control the resulting pair, so verify contrast; for native form controls the relevant feature is `accent-color`.
