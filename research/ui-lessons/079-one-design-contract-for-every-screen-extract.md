---
lesson: 079
kind: video
duration_s: 71
type: ui
category: visual
topic: design-system consistency across generated screens (extract tokens first, enforce, then one decision per visual axis)
sources: frames, voice-over
---

# One design contract for every screen: extract, enforce, then decide per axis

**Hook:** Ten AI-built pricing pages from the same prompt; only one looks deliberate.

## Main rule
Before styling a new screen, derive the design tokens from what the project already encodes (theme config, CSS custom properties, token files, then the most reused component), write them down once with a one-line reason each, and make every screen read from that file. A value outside the system is either replaced by the closest token or added as an explicit, documented extension; never invented silently. Consistency is necessary but not sufficient: also make one explicit choice per visual axis (type contrast, colour signature, spacing rhythm, surface finish).

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 10 | pricing cards from the same prompt ("Same prompt · ten times") with prices $29, $24, $19, $29, $39, $29, $19, $34, $29 | 0:00 on-screen |
| 3 screens, 3 blues, 3 button styles | Pricing / Settings / Members generated separately: spacing 24 + solid button, 16 + outline button, 20 + pill button, each with a different blue | 0:04-0:13 on-screen + voice |
| Scan order | theme config (Tailwind) → `:root` custom properties → theme.ts / tokens.json (not found in demo) → most-reused component: Button | 0:17-0:22 on-screen |
| 11 tokens extracted, 0 invented | result of the scan | 0:23 on-screen + voice |
| space.tight 8px | spacing inside a group | 0:28 on-screen (DESIGN.md) |
| space.base 20px | "median of 16 / 20 / 24" (the three screens' values) | 0:29 on-screen |
| space.loose 40px | spacing between groups | 0:29 on-screen |
| radius.md 8px | "from Button, most reused" | 0:30 on-screen |
| border.hair 1px | "one separation language" | 0:30 on-screen |
| text.lo contrast 4.6:1 on surface.1 | muted/meta text | 0:27 on-screen |
| text.hi "never pure white" | primary text | 0:27 on-screen |
| Type axis: 15 / 42, weight 400 → 700 | body size / display size and weight range of the distinctive variant | 0:51 on-screen |
| Space axis: 8 inside, 40 between | spacing rhythm decision | 0:53 on-screen |
| Finish axis: border only | one surface treatment | 0:53 on-screen |
| Colour axis: one signature, on the action | single accent on the primary action | 0:52 on-screen |

The DESIGN.md shows hex values for brand, surfaces and text; they are omitted here (colour-independent skill). Token roles: `brand.500` (already the Button default), `surface.1` (app background, unchanged), `surface.2` (raised cards), `text.hi`, `text.lo`, three spacing steps, one radius, one UI font (the one already loaded), one border width.

## Before / after
- **Every screen decided alone vs one contract.** Bad: Pricing, Settings and Members were generated in separate sessions; each picked its own blue, its own padding (24 / 16 / 20) and its own button style (solid / outline / pill). Caption "generation 1 × generation 2 × generation 3 · context never carries". Good: after the token file exists, all three use the same brand colour, spacing and a solid button ("One contract. Every screen."). Why: nothing persists between generations, so without a shared written source each screen re-decides, and the product stops reading as one product.
- **Inventing tokens vs extracting them.** Bad: a fresh palette and scale are invented. Good: the skill reads existing config and the most reused component first and only fills gaps; e.g. base spacing is the median of the values already in use (16 / 20 / 24 → 20 px). Why: if decisions already exist in code, the system already exists; re-inventing creates a second, conflicting system.
- **Silent off-system value vs enforcement.** On a fourth screen a new blue is requested; it is flagged "off-system", replaced with the closest token (`brand.500`), and an approved extension would be written to DESIGN.md with its reason. Why: silent one-off values are how drift starts; writing extensions down keeps the system the single source of truth.
- **Coherent vs distinctive.** Bad: the unified screens are consistent but generic ("same system · still interchangeable"). Good: one decision per axis is recorded (type 15 / 42 with weight 400 → 700; one colour signature on the action; 8 inside / 40 between; border-only finish) and the pricing card is restyled with a high-contrast display price, a single accent on the CTA and dash bullets. Why: distinctiveness comes from committing to a contrast on each axis instead of taking defaults.

## Do
- Read existing tokens before creating any: theme config, CSS custom properties, token files, then the most reused component.
- Keep one root-level design file that lists each token with a one-line reason; make every new screen use it.
- Derive missing values from what is already used (e.g. the median of observed spacings) rather than guessing.
- Map off-system values to the nearest existing token; add a new token only as an explicit, documented extension.
- Use a small spacing scale with distinct jobs: tight inside a group, base, loose between groups.
- Make one explicit decision per axis: where type contrast lives, one colour signature on the action, a spacing rhythm, and one finish (borders or shadows or flat, not all three).

## Don't
- Don't let each screen pick its own primary colour, padding or button variant.
- Don't introduce a new hex value in a component without adding it to the system.
- Don't use pure white for primary text on dark surfaces.
- Don't mix several separation languages (borders plus shadows plus fills) on one surface.

## Scene by scene
- 0:00 Grid "Same prompt · ten times": nine near-identical pricing cards (blue price, check bullets, blue "Start trial") plus one different card with a serif price, dash bullets and a warm accent button. Caption "Ten AI-built pricing pages."
- 0:01 The odd card gets a highlight ring: "One of them follows a design contract."
- 0:04 "Where it comes from: Every screen decided alone": Pricing, Settings and Members panels with dashed outlines; chips under each show a different blue, spacing 24 / 16 / 20 and button style solid / outline / pill.
- 0:08 Red strip "generation 1 × generation 2 × generation 3 · context never carries"; "One product. Three answers."
- 0:14 Terminal: "use the design-system skill on this project" → "no DESIGN.md found – creating it first" → checks tailwind.config.ts, `:root` custom properties, theme.ts / tokens.json (dimmed), most-reused component: Button → "extracted 11 tokens · 0 invented".
- 0:24 DESIGN.md fills line by line: brand, two surfaces, text.hi ("never pure white"), text.lo ("meta, 4.6:1 on surface.1"), space 8 / 20 / 40 px, radius 8px, UI font ("already loaded"), border 1px.
- 0:33 The three panels unify: same blue, the outline "Save changes" becomes a solid button; badge "One contract. Every screen."
- 0:37 "Enforcement: The contract has teeth": a "Screen four" Settings panel requests a new blue; warning "off-system … using closest token brand.500 instead"; the token is applied; a green note "+ extension approved, written to DESIGN.md with its reason".
- 0:48 "The other new skill: Coherent isn't distinctive", subline "same system · still interchangeable".
- 0:51 Axis rows appear: TYPE "15 / 42, weight 400 → 700", COLOUR "one signature, on the action", SPACE "8 inside, 40 between", FINISH "border only"; the pricing card restyles (display serif price, warm accent CTA, dash bullets) while the other panels dim.

## Voice-over summary
- Ten AI pricing pages, one made with a design contract; separately generated screens end up with three blues and three button styles.
- Because nothing carries between generations, every screen decides alone and the product stops looking like one product.
- The design-system skill writes one root file that every other skill reads; "rule zero" is to read the existing config, CSS variables and most reused component first.
- Eleven tokens extracted, none invented, each with a one-line reason; later a new blue is stopped and replaced by the closest token, and extensions must be written down because silent invention causes drift.
- Coherent still isn't distinctive: a second skill forces one decision per axis (type, colour, space, finish) and refuses defaults.

## Notes for the skill
- Implementation: a single source of truth (DESIGN.md, a tokens JSON, or CSS custom properties) with semantic names (`--brand`, `--surface-1`, `--surface-2`, `--text-hi`, `--text-lo`, `--space-tight/base/loose`, `--radius-md`, `--border-hair`). Lint for raw colour literals and off-scale spacing in components (e.g. stylelint `declaration-strict-value`, Tailwind config restricting arbitrary values).
- "Closest token" replacement should be done in a perceptual colour space (OKLCH/ΔE), not by hex distance, and the substitution must be reported, not silent.
- Contrast: 4.6:1 for muted text clears WCAG 1.4.3 AA (4.5:1) with little margin; check it on every surface it is used on (surface.2 is lighter, so the same muted text may fall below 4.5:1 there).
- The median rule for spacing is a pragmatic heuristic; it fits when the existing values are close. If observed values are scattered, normalise to a scale (e.g. 4/8-based) instead.
- A 15 px body size is on the small side for long reading; it is shown as one example of a type decision, not a recommended default.
