---
id: DXEXGAwDAWQ
reel_url: https://www.instagram.com/p/DXEXGAwDAWQ/
pattern_page: none
kind: carousel
date: 2026-04-13
type: ui
category: css
topic: modern CSS features (container queries, :has, subgrid, view transitions, nesting, text-wrap balance, anchor positioning)
sources: caption, video slide (slide 1 of 9, cover)
---

# Seven modern CSS features that replace JS workarounds

**Caption:** Lists seven CSS features presented as game changers in 2026: container queries, the `:has()` parent selector, subgrid, view transitions, native nesting, `text-wrap: balance`, anchor positioning; claims most replace whole JS libraries.
**Hook:** The cover asks, in effect, whether CSS can really do that now, promising 7 features.

## Main rule
Before reaching for JavaScript or a library for component-responsive layout, parent-state styling, aligned nested grids, page/state transitions, selector nesting, balanced headings or tethered popovers, check whether the native CSS feature covers it (and check current browser support for the target audience).

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 7 features | list length | caption; cover subtitle on the video slide |
| 01-07 | feature numbering (container queries, :has, subgrid, view transitions, nesting, text-wrap balance, anchor positioning) | caption |
| 9 slides | carousel length (likely cover + 7 features + closing; assumed) | post metadata |
No other numbers. The image slides with the actual code examples were not available, so no syntax from the post can be quoted.

## Before / after
The caption only names features; the comparisons below are the standard JS-vs-CSS contrasts each feature addresses, not content seen on slides.
- Container queries: instead of resize observers or viewport media queries, a component adapts to its own container width.
- `:has()`: instead of toggling parent classes from JS, style a parent from a child's state (e.g. a field wrapper when its input is invalid, a card when it contains an image).
- Subgrid: instead of fixed heights or JS equalising, nested items (card titles, footers) align to the parent grid tracks.
- View transitions: instead of an animation library for state or page changes, the browser cross-fades or morphs between DOM snapshots.
- Nesting: instead of a preprocessor, nest selectors with `&` in plain CSS.
- `text-wrap: balance`: instead of manual line breaks or JS balancers, headings get evenly long lines.
- Anchor positioning: instead of a positioning library, tooltips and popovers attach to an anchor element and can flip on overflow.

## Do
- Use container queries for reusable components (`container-type: inline-size` on the wrapper, `@container (width > 30rem)` in the component).
- Use `:has()` for parent and sibling state (`.field:has(input:user-invalid)`), keeping selectors scoped.
- Use subgrid for card rows that must align internal parts (`grid-template-rows: subgrid` with `grid-row: span N`).
- Use view transitions for meaningful state changes, with a reduced-motion fallback.
- Use `text-wrap: balance` on short headings; `text-wrap: pretty` for paragraphs to avoid orphans.
- Use anchor positioning (with the Popover API) for tethered overlays, with fallback positions.

## Don't
- Don't ship any of these without checking current support and providing a working fallback (progressive enhancement, `@supports`).
- Don't apply `text-wrap: balance` to long body text.
- Don't use view transitions for every click or ignore `prefers-reduced-motion`.
- Don't nest selectors deeply just because nesting is available; it raises specificity and couples styles to markup.

## Slide by slide
The carousel has 9 slides. Only slide 1 (the animated cover) was available; slides 2 to 9 were not downloaded, so this list is reconstructed from the caption.
- Slide 1 (seen, animated): title card asking whether CSS can do that now, subtitle 7 features that changed everything with a swipe arrow.
- Slides 2 to 8 (not seen): presumably one feature each, in caption order 01 to 07.
- Slide 9 (not seen): likely a closing/save slide.

## Video slide
Slide 1 (cover), about 4 s, centred text on a dark background with a soft radial glow in the accent colour.
- 0:00 Empty dark frame.
- 0:00.5 First line appears (CSS can do).
- 0:01 Second line appears with the key word in the accent colour; the glow fades in behind it.
- 0:01.5-0:02 Glow grows; a muted subtitle appears (7 features, with an arrow).
- 0:02.5-0:03.5 The account handle fades in bottom right; the composition holds.

## Notes for the skill
- Browser support: all seven are recent features with uneven support history; check current support for each before relying on it, and gate with `@supports` (e.g. `@supports (anchor-name: --a)`, `@supports selector(:has(*))`).
- The claim that these replace entire JS libraries is oversimplified. Anchor positioning covers placement and fallback flipping, but focus management, dismissal and ARIA still need the Popover API, `<dialog>` or script. View transitions replace visual animation only; routing and state stay in JS.
- View transitions: wrap animations in `@media (prefers-reduced-motion: no-preference)` or shorten them to a fade; do not move focus unexpectedly during the transition, and make sure the new content is announced if it replaces the page.
- Container queries: a container with `container-type: size` needs an explicit height; prefer `inline-size`. Container query units (`cqi`) help fluid type inside components.
- `:has()` can be costly on very broad selectors (e.g. `body:has(...)` reacting to anything); keep the subject element specific.
- `text-wrap: balance` is limited by browsers to a small number of lines, so it is intended for headings, captions and short blocks.
- Nesting: `&` is required in some positions; nested rules add the parent's specificity.
- Accessibility: none of these features change semantics; overlays positioned with CSS still need correct roles, labels and keyboard behaviour (APG dialog, menu, tooltip patterns).
