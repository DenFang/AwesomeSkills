# Always-on rules

Nine rules apply to any interactive UI, whatever elements it contains, so they live here and not in their topic files. Load this file for every task that touches UI beyond a one-line edit; load a topic file only when the inventory contains the elements it covers.

| Rule | Checks | Applies when |
|---|---|---|
| INT-1 | visible focus | anything is focusable |
| INT-2 | real elements, real keyboard | anything is clickable |
| INT-11 | target size | anything is clickable |
| INT-12 | nothing reachable by hover alone | anything reveals on hover |
| VIS-1 | values come from tokens | any style is written |
| VIS-7 | text and UI contrast | any text or control is drawn |
| VIS-8 | colour is never the only signal | colour carries meaning |
| MOT-13 | reduced motion | anything moves |
| CON-1 | interface copy | there is text |

## Interaction and input

### INT-1 · Focus is always visible (P0)
**Applies to.** every focusable element, the page's tab order and skip links (always check).
**Rule.** Never remove the focus outline without a better replacement: about 2 px, offset about 2 px, at least 3:1 contrast against the element and every surface it can sit on (check light and dark themes), shown via `:focus-visible` so keyboard users get it and mouse clicks do not (text inputs still show focus on click; leave that alone). Draw it with `outline`, not only `box-shadow`, which forced-colours mode removes; on mixed backgrounds a two-tone ring (a surface-coloured gap plus a contrasting ring) keeps 3:1 everywhere. Sticky headers and overlays must not cover the focused element. The focus style differs from the selected/active style. DOM order matches visual order: reorder the markup, not the layout. On content-heavy pages a "Skip to main content" link is the first focusable element, visually hidden until focused (never `display: none`), and targets `<main id="main" tabindex="-1">` so focus really moves.
**Detect.** `outline: none` / `outline: 0` without a `:focus-visible` replacement; rings drawn only with `box-shadow`; `tabindex` > 0; CSS reordering (`order`, `flex-direction: row-reverse`, grid placement, absolute positioning) that changes the visual sequence of interactive items; skip links hidden with `display: none`; sticky headers without `scroll-padding-top`.
**Fix.**
```css
:focus-visible { outline: 2px solid var(--color-focus); outline-offset: 2px; }
```

### INT-2 · Real elements, real keyboard (P0)
**Applies to.** every interactive element and custom widget (always check).
**Rule.** Clickable things are `<button>` or `<a href>`, not `<div onClick>`. Custom widgets carry the right roles and states (`aria-expanded`, `aria-controls`, `aria-selected`, `aria-checked`, `aria-haspopup`) and keys: Enter/Space activate, arrows move within composite widgets (menus, tabs, listboxes, radio groups, grids), Home/End jump, Escape closes one level.
**Detect.** `onClick` on non-interactive elements without role and key handlers; accordions with `<div>` headers; menus that ignore arrow keys.

### INT-11 · Targets are big enough and close (P0 below 24 × 24 px, P1 below 44 × 44 px on touch)
**Applies to.** every interactive target (the 44 px minimum on touch only).
**Rule.** Interactive targets at least 44 × 44 px on touch and never below 24 × 24 px (WCAG 2.5.8; inline links in text, and targets spaced so a 24 px circle around each does not overlap a neighbour, are exempt), even when the glyph is smaller; pad the hit area, keep the icon small (a 20 px icon in a 44 px box), preferably with `min-width`/`min-height` or a pseudo-element rather than padding that only works for one icon size, and without letting neighbouring hit areas overlap. Put frequent targets near where the pointer or thumb already is: primary mobile actions at the bottom, menus at the cursor, edit in place rather than in a far modal. Use `@media (pointer: coarse)` to grow controls for touch. Screen edges and corners are effectively infinite targets for a mouse. A floating action button is for the one main creation action per screen, with bottom padding on the content so it never covers the last row or its actions; bottom-docked CTAs clear `env(safe-area-inset-bottom)` (INT-27).
**Detect.** 16 to 32 px icon buttons without padding on mobile; tiny close buttons; primary mobile actions at the top of the screen.

### INT-12 · Hover is an extra, never the only path (P0)
**Applies to.** anything revealed or triggered on hover: card actions, row actions, hover menus.
**Rule.** Touch has no hover: mobile browsers (iOS Safari most of all, when hover reveals content) turn the first tap into a sticky `:hover` that can stay until the user taps elsewhere, so the tap is spent and the action never fires. Ask the input, not the device: gate hover-reveal styles with `@media (hover: hover) and (pointer: fine)` (consider `any-hover` for hybrids), never with user-agent or screen-width sniffing. Keep actions visible by default and hide them only inside that query, revealing on `:hover` and `:focus-within`; hide them with `opacity: 0` plus `pointer-events: none`, so they take no taps but stay in the tab order and `:focus-within` can reveal them; `visibility: hidden` removes them from the tab order, so use it only when another focusable element in the row or card reveals them first. Hover may reveal extras (compare, quick view), never the primary action, and every extra also has a touch home: in the card, behind a swipe that has a visible alternative, or in a sheet.
**Detect.** `opacity: 0` actions revealed only on `:hover`; `isMobile` or user-agent checks deciding what to show; `mouseenter` handlers with no touch or focus equivalent.

## Visual system

### VIS-1 · Nothing is typed raw (P1)
**Applies to.** all styling (always check).
**Rule.** Every colour, size, space, radius, shadow, weight, duration, easing and z-index comes from a named token on a fixed scale. Layer tokens: **primitives** (raw values; value names such as a numbered 100 to 900 shade ramp per hue are fine here) → **semantic** (`--color-bg`, `--color-surface`, `--color-text-muted`, `--color-accent`, `--color-danger`) → **component** (`--button-bg`, `--card-padding`). Components read only semantic or component tokens, never primitives, so one changed primitive or repointed alias cascades everywhere. Name by role, not value (`--color-accent`, `--space-md`, not `--blue-500`, `--spacing-16`); a rebrand repoints semantic tokens to new primitives rather than mutating a primitive into a value its name no longer describes. Themes, including dark mode, swap the semantic layer and are re-checked for contrast (VIS-7); components never change. A shared component ships with its variants, sizes and every state (STA-1, INT-10), not just the default, and new screens reuse those variants: a third button style or a one-off card beside the shared one is drift, not a new decision.
**Detect.** Hex/rgb literals or px values inside components; components referencing primitive ramps (`var(--gray-200)`) directly; near-duplicate values on one scale (a 13 px gap next to 12, a 15 or 17 px font size next to 16); value names (hue, px) on tokens used for meaning; one-off variants (another primary button style) next to the shared component.
**Fix.** Snap stray values to the nearest step of the project's scale for that property (spacing 13 → 12, 17 → 16, 22 → 24 on a 4 px grid; type sizes snap to the type scale, VIS-4) and replace literals with tokens; pick the nearest colour token by perceived difference (OKLCH), not hex distance, and report every substitution. Before inventing tokens, extract the ones the project already encodes, in this order: theme config, CSS custom properties, token files, then the most reused component (its padding and radius are the de facto scale); derive a missing value from the values already in use. Write the result in one file every screen reads from; a value outside it is either snapped to a token or added as a documented extension with its reason, never typed in silently. If the project has no tokens at all, propose a minimal set before refactoring (see the "Missing design system" note in SKILL.md).

### VIS-7 · Contrast is a ratio (P0)
**Applies to.** every text and essential UI element (always check).
**Rule.** Contrast belongs to a text/background pair, never to a colour token alone: the same text colour can pass on one surface and vanish on the next. Body text at least 4.5:1 against its actual background; large text (24 px, or about 18.7 px bold) and essential UI parts (input borders, focus rings, icons that carry meaning) at least 3:1; aim for 7:1 (AAA) on critical text such as errors, prices and terms where the palette allows. Muted greys on nav links, card labels, subtitles, stat labels and placeholders are the usual failures, often only 1.5 to 2:1. Text dimmed by opacity is measured as rendered on its surface, gradient text at its weakest point. Check every pair in light and dark themes. Disabled controls are exempt, but their label stays legible.
**Detect.** Light grey text tokens; `opacity` below about 0.6 on text; text on images or gradients without a scrim; disabled-looking labels used for real content.
**Fix.** Change the lightness of the failing token, keeping its hue and the layout; a redesign is rarely needed.

### VIS-8 · Colour never carries meaning alone (P0)
**Applies to.** every status, state, series or group shown with colour: error and success messages, trends, chart series, chips, active nav items, selected icons (always check).
**Rule.** Every colour cue is paired with a second signal: an icon on error and success messages, an arrow plus a signed number on trends ("+14%"), patterns, textures or direct labels on chart series with shapes in the legend, a check or fill change on active chips, an underline or filled shape plus `aria-current` on the active nav item, a heading or position for colour-coded groups. Red against green is exactly the difference red-green colour-blind users (about 1 in 12 men) lose, so error and success, pass and fail, up and down never differ by hue alone. Before release, view key screens through a protanopia, deuteranopia and tritanopia simulator.
**Detect.** Status shown only by text or dot colour; red borders as the only error signal; charts distinguishable only by hue; groups distinguished only by tint.
**Fix.** For form errors add the icon, `aria-invalid="true"` and `aria-describedby` pointing at the message, so the meaning is not visual at all.

## Motion

### MOT-13 · Respect reduced motion (P0 for parallax, large travel or motion over 5 s without a control; P1 otherwise)
**Applies to.** any project with motion (always check).
**Rule.** Every non-essential animation turns off or becomes a short fade under `prefers-reduced-motion: reduce`. Parallax, auto-playing motion and large movements are removed entirely; shake and bounce become a fade, staggered cascades one quick fade, celebration bursts a static success state, animated counters the final number. Smooth scrolling counts too: put `scroll-behavior: smooth` inside `@media (prefers-reduced-motion: no-preference)`, and let scripted `scrollTo` or `scrollIntoView` with `behavior: 'smooth'` check the same preference. Essential progress indicators (spinners, indeterminate bars) are exempt from a global reset, or get a slow non-spatial pulse, so they never look frozen. Whatever the setting, anything that moves on its own for more than 5 s (looping glows, marquees, auto-rotating carousels) needs a pause or stop control (WCAG 2.2.2).
**Detect.** No `prefers-reduced-motion` handling anywhere; JS animations (Web Animations API, motion libraries) that ignore the setting; `scroll-behavior: smooth` set outside a reduced-motion query.
**Fix.**
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: 1ms !important; animation-iteration-count: 1 !important; transition-duration: 1ms !important; scroll-behavior: auto !important; }
}
```
And check `matchMedia('(prefers-reduced-motion: reduce)')` before starting JS animations.

## Copy

### CON-1 · Microcopy is interface (P1)
**Applies to.** all interface copy: button labels, error messages, empty states, field labels and hints, confirmations.
**Rule.** The button label is the last thing read before committing, so it names the reward or result ("Create my free account", "Send 3 invoices"), never "Submit". Errors name the cause in plain words and hand over the fix as a link or action ("That email is already registered. Log in instead?"): a detour, not a dead end. Empty states give one action, the first step (STA-6), so they never look like a bug. Labels stay visible after typing; a placeholder is not a label (FRM-2). Write like a helpful colleague: plain words, "you", no system jargon ("operation failed", "invalid input", "null"), and stay specific: friendly but vague ("Hmm, that didn't go through") still needs the cause when it is known, and jokes stay out of serious failures (payments, data loss). Keep one voice across the product. Destructive confirmations repeat the verb and the object. On login and password reset, never reveal whether an account exists; use a neutral message there.
**Detect.** "Submit", "OK", "Click here", "Error occurred", "Invalid", "No data"; a `placeholder` with no `<label>`; mixed tone; shouting capitals in body copy.
