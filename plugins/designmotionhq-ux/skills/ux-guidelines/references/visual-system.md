# Visual system

Tokens, type, colour roles, spacing, radius, elevation and hierarchy. These rules are palette-independent: they define relationships (how many colours, which role gets the accent, how surfaces step), never specific brand colours. Always use the project's own palette and tokens.

Severity: **P0** unreadable or inaccessible, **P1** inconsistent or confusing, **P2** polish.

---

### VIS-1 · Nothing is typed raw (P1)
**Applies to.** all styling (always check).
**Rule.** Every colour, size, space, radius, shadow, weight and duration comes from a named token on a fixed scale. Layer tokens: **primitives** (raw scale values) → **semantic** (`--color-bg`, `--color-text-muted`, `--color-accent`, `--color-danger`) → **component** (`--button-bg`). Name by role, not value (`--color-accent`, not `--blue-500`). Themes, including dark mode, swap the semantic layer; components never change.
**Detect.** Hex/rgb literals or px values inside components; near-duplicate values (13px next to 12px, 17px next to 16px); colour names in token names used for meaning.
**Fix.** Snap stray values to the nearest scale step and replace literals with tokens. If the project has no tokens, propose a minimal set before refactoring (see the "Missing design system" note in SKILL.md).

### VIS-2 · One spacing scale (P1)
**Applies to.** all spacing.
**Rule.** One base unit (4 px or 8 px) and a short scale (for example 4, 8, 12, 16, 24, 32, 48, 64). Random gaps (7, 11, 23) read as sloppy. A proportional scale (×1.5 or ×1.618) is fine if used consistently.
**Detect.** Many distinct spacing values; arbitrary Tailwind values (`p-[13px]`) for spacing.

### VIS-3 · Spacing does the grouping (P1)
**Applies to.** every layout.
**Rule.** The gap inside a group is clearly smaller than the gap between groups (proximity). Three kinds of white space: micro (padding inside elements), macro (between sections, often 40 px and more), active (deliberate emptiness around the one element that should pop). Cards and buttons that look cheap usually need more padding, more gap between their elements, and more line-height in body text, not a redesign.
**Detect.** Uniform gaps everywhere; borders and dividers doing work spacing could do; cramped padding (8 to 12 px on cards); body line-height near 1.1 to 1.2.

### VIS-4 · Type: seven decisions made once (P1)
**Applies to.** all text styling.
**Rule.**
1. **Sizes**: about five steps from one base and one ratio (for example 1.25: 13, 16, 20, 25, 31). Stop adding sizes.
2. **Inks**: three text roles (primary, secondary, muted) rank text within a line; size ranks between blocks.
3. **Weights**: two or three (for example 400 to read, 600 to scan). Avoid a pile of weights.
4. **Leading moves against size**: body about 1.5, large headings about 1.1 to 1.2. Not one line-height for everything.
5. **Tracking**: tighten large headings slightly (about -0.02em above 24 px); open small uppercase labels (about +0.05em).
6. **Measure**: cap paragraphs at about 45 to 75 characters (`max-width: 66ch`), whatever the container width.
7. **Figures**: tabular numbers wherever digits align or update (DAT-1).
Use one family (two at most).
**Detect.** More than about six font sizes; many weights; uniform line-height; full-width paragraphs; mixed families.

### VIS-5 · Colour roles: dominant, secondary, one accent (P1)
**Applies to.** every screen.
**Rule.** Distribute colour by role, roughly 60/30/10: a dominant neutral for backgrounds, a secondary step of the same family for surfaces (cards, nav, containers), and one accent spent only on primary actions and key states. Status colours (danger, success, warning) are semantic and used only for their meaning. When every element has its own colour, nothing stands out; mute everything else and the primary pops. The ground affects how a colour reads, so check the accent on the surfaces it actually sits on.
**Detect.** Many unrelated hues on one screen; accent colour on decorative elements; coloured status pills everywhere; a primary button that blends into its card.

### VIS-6 · The danger colour is a budget (P1)
**Applies to.** uses of the danger or error colour.
**Rule.** The danger colour appears only on destructive actions and real errors. A red logout button or red decorative badges make the real delete look routine.
**Detect.** Danger tokens on non-destructive controls.

### VIS-7 · Contrast is a ratio (P0)
**Applies to.** every text and essential UI element (always check).
**Rule.** Body text at least 4.5:1 against its actual background, large text (24 px, or about 19 px bold) and essential UI parts (borders of inputs, focus rings, icons that carry meaning) at least 3:1. Muted greys on labels, nav and placeholders are the usual failures. Check every text/background pair across light and dark themes.
**Detect.** Light grey text tokens; text on images without a scrim; disabled-looking labels used for real content.

### VIS-8 · Colour never carries meaning alone (P0)
**Applies to.** every status, state or series shown with colour (always check).
**Rule.** Every colour cue is paired with a second signal: an icon on errors, an arrow on trends, a label or pattern in charts, a check on active chips. Roughly 1 in 12 men cannot tell red and green apart.
**Detect.** Status shown only by text or dot colour; red borders as the only error signal; charts distinguishable only by hue.

### VIS-9 · Dark mode is its own system (P1)
**Applies to.** products with a dark theme.
**Rule.** Not an inversion. A near-black page (not pure black) leaves room for layers. Elevation is shown by lighter surfaces, not by shadows (shadows barely show on dark). Text is one light colour at a few opacities (about 87% primary, 60% secondary, 38% disabled), never pure white. The accent keeps its hue but is lighter and less saturated so it does not glow. Hairlines are white at a low alpha (about 6 to 10%) so they adapt to every surface. Photos are dimmed slightly; illustrations get dark variants. Text may need one weight step lighter. Implement as a semantic token swap, respecting `prefers-color-scheme` and any user choice.
**Detect.** `filter: invert()`; `#000` backgrounds with `#fff` text; the same saturated accent in both themes; fixed grey borders; shadows as the only elevation in dark.

### VIS-10 · Radius is a scale and a brand decision (P2)
**Applies to.** rounded elements, especially nested ones.
**Rule.** One scale (for example 4, 8, 12, 16, full) and radius grows with surface size: chips and badges small, inputs and buttons medium, cards larger, modals and sheets largest; full radius only for one-line elements (pills, avatars, toggles). Nested corners stay concentric: **inner radius = outer radius − padding**; a ring outside an element is outer = inner + gap. Edges that touch the screen get no corner (a bottom sheet is rounded only on top). Let the container clip images (`overflow: hidden`). Choose the scale for the brand: sharp reads authoritative, medium professional, round friendly, pill playful; rounded controls feel safer to touch.
**Detect.** The same radius on a card and the element nested inside it; many off-scale radii; full radius on multi-line cards.

### VIS-11 · Elevation encodes hierarchy (P1)
**Applies to.** shadows and elevated layers.
**Rule.** Elevation is a signal, so spend it only where something actually floats or matters most. Floating layers (menus, popovers, modals, dragged items) get layered shadows: a tight contact shadow plus a wide soft one. Page panels and rows do not; separate them with surface value steps and hairline borders. A shadow on every card means nothing floats. A soft tint of the brand colour in the shadow is an optional premium touch on the one hero element.
**Detect.** The same heavy drop shadow on every panel; single hard `box-shadow: 0 0 10px #000`; shadows used to separate table rows or sidebars.
**Example.**
```css
--shadow-float: 0 1px 2px rgb(0 0 0 / .08), 0 8px 24px rgb(0 0 0 / .12);
```

### VIS-12 · One focal point per view (P1)
**Applies to.** every screen.
**Rule.** Size, contrast, weight, colour and space stack to make one clear entry point: the primary element about twice body size, one accent, higher contrast for primary roles, and room around the hero. Primary action filled, secondary as outline or text link. When one item must be chosen (a pricing tier, a CTA), keep everything else calm and change it on several channels at once (scale, elevation, a badge), not colour alone.
**Detect.** Several equally loud buttons side by side; headings barely larger than body; everything bold.

### VIS-13 · Layout sits on a grid, then breaks it on purpose (P2)
**Applies to.** page and section layouts.
**Rule.** A 12-column grid (or the project's grid) with a consistent gutter; column ratios fit the content (4:8, 6:6, 3:9); columns collapse at breakpoints. Align to shared edges. Break the grid deliberately (a full-bleed hero, a pull quote) only once the order exists.
**Detect.** Elements that almost align; ad-hoc widths; centred everything.

### VIS-14 · Gestalt does free work (P2)
**Applies to.** every layout.
**Rule.** Similar things look similar (same component, same style); aligned things read as a path; a shared container groups distant items; a dimmed or blurred background pushes a dialog forward; closed shapes do not need every line drawn.

### VIS-15 · Icons are one set (P2)
**Applies to.** icon sets.
**Rule.** One family, one stroke weight, one fill style (outline or filled, not both), the same bounding box and grid (24 px, or 16 px for dense UI). Round shapes are drawn slightly larger than square ones to look the same size. Icons sit centred on the text line.
**Detect.** Mixed icon libraries; mixed stroke weights; icons misaligned with adjacent text.

### VIS-16 · Optical corrections beat maths (P2)
**Applies to.** play buttons, icon and shape pairs, text in buttons and badges.
**Rule.** When the correct value looks wrong, adjust for the eye: shift a play triangle right (about 8% of its box), make circles slightly larger than squares beside them, keep nested corners concentric, centre text on its cap height (labels in buttons often sit visually low), and reduce weight one step on light-on-dark text.

### VIS-17 · Gradients and glass are seasoning (P2)
**Applies to.** gradients and translucent "glass" surfaces.
**Rule.** Gradients stay between neighbouring hues (within about 60°), move lightness in one direction, and work as soft ambiance behind content rather than a wash over it; at most one gradient headline, body text stays solid. Add subtle grain if banding shows. Glass (translucent fill, `backdrop-filter: blur`, light hairline, soft shadow) only works over a busy backdrop and must keep text contrast.
**Detect.** Gradient text in body copy; gradients across opposite hues; glass panels over flat colour; translucent panels that fail contrast.

### VIS-18 · Layering without z-index wars (P1)
**Applies to.** overlapping layers: menus, modals, toasts, sticky headers.
**Rule.** `z-index` works only on positioned elements (or flex/grid children); a child can never escape its parent's stacking context, whatever its number. Give components their own context with `isolation: isolate`, and keep a small named z-index scale (base, dropdown, sticky, overlay, modal, toast). Huge numbers (9999, 99999) are a symptom; find the stacking context instead.
**Detect.** z-index values above about 100; `z-index` on static elements; overlays hidden behind content.

---
Sources: design-tokens, design-system-kit, design-system-build, atomic-design, proximity-rule, whitespace-types, card-spacing-fixes, perfect-card, typography-system, visual-hierarchy, golden-ratio, color-harmony, pop-out-effect, color-accessibility, dark-mode, dark-mode-surfaces, border-radius, border-radius-system, radius-spectrum, rounded-shapes, shadow-elevation, depth-layers, von-restorff, grid-system, gestalt-laws, icon-design-rules, optical-corrections, gradient-design, glassmorphism, z-index-mastery, buy-button-css, perfect-button. See `sources.md`.
