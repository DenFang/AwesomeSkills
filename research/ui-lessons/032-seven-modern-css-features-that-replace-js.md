---
lesson: 032
kind: carousel
type: ui
category: css
topic: modern CSS features (container queries, :has, subgrid, view transitions, nesting, text-wrap balance, anchor positioning)
sources: video slide (slide 1 of 9, cover), image slides 2-9
---

# Seven modern CSS features that replace JS workarounds

**Hook:** The cover asks whether CSS can really do that now, promising 7 features that changed everything.

## Main rule
Before reaching for JavaScript, a preprocessor or a library for component-responsive layout, parent-state styling, aligned card internals, page transitions, selector nesting, heading line balance or tethered overlays, check whether the native CSS feature covers it, check current browser support, and keep the parts CSS does not cover (accessibility, focus, state, fallbacks).

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 7 features, numbered 01/07 to 07/07 | list length | slide 1 subtitle; slides 2-8 counters |
| `container-type: inline-size`; `@container (min-width: 400px)`; `grid-template-columns: 1fr 1fr` | container queries example | slide 2 |
| `.card:has(img)` → `grid-template-rows: 200px 1fr` | `:has()` layout example | slide 3 |
| `form:has(:invalid) button` → `opacity: 0.5; pointer-events: none` | `:has()` form example | slide 3 |
| `repeat(3, 1fr)` columns; card `grid-template-rows: subgrid; grid-row: span 3` | subgrid example | slide 4 |
| 3 lines of CSS; `@view-transition { navigation: auto; }`; `view-transition-name: hero` | view transitions | slide 5 |
| `& h2 { font-size: 2rem }`, `&:hover { transform: scale(1.02) }`, nested `@media (width < 768px) { padding: 1rem }` | nesting example | slide 6 |
| `h1, h2, h3 { text-wrap: balance }`, `p { text-wrap: pretty }` | text wrapping | slide 7 |
| 3 lines unbalanced vs 2 lines balanced | demo headline | slide 7 |
| `anchor-name: --tooltip`; `position: fixed; position-anchor: --tooltip; top: anchor(bottom); left: anchor(center)` | anchor positioning | slide 8 |

## Before / after
Every feature slide has a small pill tag, a one-line promise, a code block, and a footer line naming what it replaces (struck through).
- **Container queries (slide 2, tag game changer).** Replaces media queries plus wrapper class hacks. Good: the wrapper gets `container-type: inline-size`; inside `@container (min-width: 400px)` the card switches to two columns. Why: the component responds to the space it is actually given, so the same card works in a sidebar and a main column without page-level breakpoints or modifier classes.
- **`:has()` (slide 3, tag parent selector).** Replaces JS DOM traversal plus `classList.toggle()`. Good: `.card:has(img)` gets an image row (`200px 1fr`) only when an image exists; `form:has(:invalid) button` dims and blocks the button. Why: the parent's style is derived from its content or state at render time, with no script to keep in sync. (The form example has accessibility problems; see Notes.)
- **Subgrid (slide 4, tag finally).** Replaces hacking equal-height cards with flexbox. Good: parent `display: grid; grid-template-columns: repeat(3, 1fr)`; each `.card` is `display: grid; grid-template-rows: subgrid; grid-row: span 3`. Why: each card spans three parent rows and its internal rows (for example image, body, footer) reuse the parent tracks, so the same part lines up across all cards whatever its content length.
- **View transitions (slide 5, tag 2025).** Replaces Framer Motion, GSAP or custom JS animations. Good: `@view-transition { navigation: auto; }` plus `view-transition-name: hero` on the hero image. Why: the browser snapshots the old and new page and animates between them; a shared name makes the hero morph between its two positions instead of cross-fading.
- **Nesting (slide 6, tag native).** Replaces Sass, LESS and PostCSS nesting. Good: inside `.card`, nest `& h2`, `&:hover` and an `@media (width < 768px)` block. Why: related rules stay together in plain CSS, and media queries can live inside the rule they modify.
- **`text-wrap: balance` (slide 7, tag typographers rejoice).** Replaces manual `<br>` tags and `&nbsp;` hacks. Demo: the same headline wraps as three lines with a single word on the last one without balance, and as two even lines with it. Good: `h1, h2, h3 { text-wrap: balance; }`, `p { text-wrap: pretty; }`. Why: balance equalises line lengths in short blocks; pretty avoids a lone last word in paragraphs without reflowing every line, and both adapt to any width, unlike hard-coded breaks.
- **Anchor positioning (slide 8, tag experimental, in a warning-coloured pill).** Replaces Popper.js, Floating UI and manual JS positioning. Good: trigger declares `anchor-name: --tooltip`; tooltip is `position: fixed; position-anchor: --tooltip; top: anchor(bottom); left: anchor(center)`. Why: the browser places the element relative to another element's box and keeps it attached on scroll and resize, without measuring in script.

## Do
- Put `container-type: inline-size` on a wrapper and query it from descendants; prefer `inline-size` over `size`.
- Use `:has()` for content-dependent layout (`.card:has(img)`) and parent state, keeping the subject selector specific.
- Use subgrid when parts of sibling cards must align; span as many parent rows as the card has parts.
- Use cross-document view transitions with a shared `view-transition-name` for the one element that should morph, and reduce or remove them under reduced motion.
- Nest shallowly, mainly for states (`&:hover`, `&:focus-visible`) and local media queries.
- Use `text-wrap: balance` on headings and `text-wrap: pretty` on paragraphs.
- Use anchor positioning together with the Popover API or `<dialog>`, with fallback positions for when the overlay would overflow.

## Don't
- Don't ship any of these without checking current support and a usable fallback (`@supports`, progressive enhancement).
- Don't disable a submit button with `opacity` and `pointer-events: none` as validation.
- Don't use `text-wrap: balance` on long body text.
- Don't use view transitions for every interaction or ignore `prefers-reduced-motion`.
- Don't nest selectors deeply; it raises specificity and couples styles to markup.
- Don't treat anchor positioning as a full tooltip or dropdown; it only places the box.

## Slide by slide
- **Slide 1 (video cover).** CSS can do THAT now?, with THAT in the accent colour; subtitle 7 features that changed everything. Details below.
- **Slide 2, 01/07 Container Queries.** Promise: style elements by their parent's size, not the viewport.
  ```css
  .card-container { container-type: inline-size; }
  @container (min-width: 400px) { .card { grid-template-columns: 1fr 1fr; } }
  ```
- **Slide 3, 02/07 The :has() Selector.** Promise: select parents based on their children.
  ```css
  .card:has(img) { grid-template-rows: 200px 1fr; }      /* only cards with an image */
  form:has(:invalid) button { opacity: 0.5; pointer-events: none; } /* "validation without JS" */
  ```
- **Slide 4, 03/07 Subgrid.** Promise: children align to the parent's grid tracks.
  ```css
  .grid { display: grid; grid-template-columns: repeat(3, 1fr); }
  .card { display: grid; grid-template-rows: subgrid; grid-row: span 3; }
  ```
- **Slide 5, 04/07 View Transitions.** Promise: smooth page transitions in 3 lines of CSS.
  ```css
  @view-transition { navigation: auto; }
  .hero-image { view-transition-name: hero; }
  ```
- **Slide 6, 05/07 CSS Nesting.** Promise: preprocessor-style nesting with no build step.
  ```css
  .card {
    background: var(--surface); /* a literal dark value on the slide */
    & h2 { font-size: 2rem; }
    &:hover { transform: scale(1.02); }
    @media (width < 768px) { padding: 1rem; }
  }
  ```
- **Slide 7, 06/07 text-wrap: balance.** Promise: no more single-word last lines. Side-by-side demo (without balance: 3 lines, last one a single word; with balance, label in the success colour: 2 even lines), then `h1, h2, h3 { text-wrap: balance; }` and `p { text-wrap: pretty; }`.
- **Slide 8, 07/07 Anchor Positioning.** Promise: position elements relative to any other element, for tooltips, popovers and dropdowns in pure CSS.
  ```css
  .trigger { anchor-name: --tooltip; }
  .tooltip { position: fixed; position-anchor: --tooltip;
             top: anchor(bottom); left: anchor(center); }
  ```
- **Slide 9 (closing).** Save this for your next project, a question asking which feature surprised you most, outlined follow button.

## Video slide
Slide 1 (cover), about 4 s (8 frames at 2 fps), centred text on a dark background with a soft radial glow in the accent colour.
- 0:00 Empty dark frame.
- 0:00.5 First line appears (CSS can do).
- 0:01 Second line appears with THAT in the accent colour; the glow fades in behind it.
- 0:01.5-0:02 The glow grows to full; a muted subtitle appears (7 features that changed everything, with an arrow).
- 0:02-0:02.5 The account handle with an accent arrow fades in bottom right.
- 0:03-0:03.5 The composition holds.

## Notes for the skill
- Browser support: these features arrived at different times and the slides themselves tag anchor positioning as experimental; check current support for each and gate with `@supports` (for example `@supports (anchor-name: --a)`, `@supports selector(:has(*))`).
- Container queries: an element cannot query its own container size; the query targets the nearest ancestor container, so `.card` must be inside `.card-container`, and the slide's two-column rule assumes `.card` is already `display: grid`. `container-type: size` would need an explicit height. Range syntax `@container (width >= 400px)` is equivalent; container units (`cqi`) help fluid type inside components.
- `:has()` form example, corrections: `:invalid` matches before the user types anything, so the button is dimmed on page load; `:user-invalid` waits for interaction (check current support). `pointer-events: none` blocks only the pointer: the button stays focusable and Enter or Space still submits, and pressing Enter in a field submits the form anyway. Opacity 0.5 drops text contrast below 4.5:1 in most themes (WCAG 1.4.3 exempts truly disabled controls, but this one is not disabled), and nothing tells the user why. The selector also hits every button in the form, including cancel. Prefer an enabled submit that, on activation, shows inline errors linked with `aria-describedby` and moves focus to the first invalid field (WCAG 3.3.1, 3.3.3); if the button must be disabled, use the `disabled` attribute plus a visible reason.
- `:has()` performance: very broad subjects such as `body:has(...)` re-evaluate often; keep the subject specific.
- Subgrid: the card's child count must match the spanned rows (three here); extra children create implicit rows that break alignment. The parent grid gets its rows implicitly from the spans; add `row-gap` on the parent and `gap: 0` or the desired gap on the card, since subgrid inherits the parent gaps unless overridden.
- View transitions: `@view-transition { navigation: auto; }` applies only to same-origin cross-document navigations (multi-page sites); same-document changes in a single-page app still need `document.startViewTransition()` in JS, and routing and state remain in JS. Each `view-transition-name` must be unique on the page at once. Wrap the opt-in in `@media (prefers-reduced-motion: no-preference)` or replace the morph with a short fade (WCAG 2.3.3); make sure focus and the page title update after navigation. Check current support.
- Nesting: early versions of the spec required `&` before a nested selector that starts with an element name, so `& h2` is the safe form (check current support); nested rules carry the parent's specificity. The hover scale should sit inside `@media (hover: hover)` so touch devices do not keep a stuck scaled state, should have a short transition, and should not be the only hover or focus cue; give keyboard users the same feedback with `&:focus-visible`.
- `text-wrap: balance` is limited by browsers to a small number of lines, so it is meant for headings, captions and short blocks; `pretty` may cost more layout time on long text. Check current support for both; without support text simply wraps normally, a safe fallback.
- Anchor positioning, corrections: `left: anchor(center)` puts the tooltip's left edge at the anchor's centre, so the tooltip is not centred; use `position-area: bottom` or `justify-self: anchor-center` (or a translate) for centring, and `position-try-fallbacks` (for example `flip-block`) so it flips when it would overflow. It handles placement only: showing, hiding, dismissal with Escape, focus and semantics still need the Popover API or `<dialog>` and the right ARIA (`role="tooltip"` with `aria-describedby` on the trigger, opening on hover and focus, dismissible and hoverable per WCAG 1.4.13; menu and dialog behaviour per WAI-ARIA APG).
- The claim that these replace whole libraries is oversimplified: CSS covers the visual part, while focus management, state and fallbacks remain the author's job.
