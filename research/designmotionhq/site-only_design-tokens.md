---
id: unknown
reel_url: unknown
pattern_page: https://designmotionhq.com/patterns/design-tokens
date: unknown
duration_s: 46
type: ui
category: visual
topic: design tokens: semantic naming, spacing scale, theme swap, three layers
sources: frames, voice-over, pattern page
---

# Design tokens: name by role, snap to a scale, layer primitives -> semantic -> component

**Caption:** none (this video is published on the pattern page only; no matching reel on the Instagram profile as of 2026-10-24)
**Hook:** A rebrand can mean 47 hand-edited values or one edit; tokens decide which.

## Main rule
Components reference role-named (semantic or component) tokens, never raw values or value-named primitives; all spacing/size/radius values come from one fixed scale; dark mode is a second set of values for the same semantic tokens; primitives -> semantic -> component layering lets one primitive change cascade everywhere.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 47 changes vs 1 | hard-coded values to hunt vs one token edit | 0:00 voice, page |
| 5 manual updates vs 0 changes needed | rebrand cost: value-named vs role-named token list (5 tokens) | 0:07-0:11 badges |
| `spacing-16` -> `spacing-md` (16px); `font-14` -> `font-body` (14px) | value-named vs role-named examples | 0:05-0:11 |
| Scale 4, 8, 12, 16, 24, 32, 48 (px) | spacing / size / radius scale ("4-point scale") | 0:12-0:21 on-screen; voice misheard as "30, 248" |
| padding 13 -> 12px, gap 17 -> 16px, border-radius 22 -> 24px, font-size 15 -> 16px | card component values snapped to nearest scale step | 0:14-0:19 |
| Modal: padding 24px, gap 16px, border-radius 16px, font-size 16px | second component using the same scale ("Same scale, same rhythm") | 0:19-0:21 |
| `--surface`, `--on-surface`, `--primary` | alias tokens whose values swap between light and dark | 0:22-0:30 |
| 3 layers: Primitives (raw values), Semantic (meaning), Component (usage) | token architecture | 0:31-0:40 |
| `space-4` = 16px -> `spacing-md` -> `card-padding` | example chain (primitive step 4 of a 4px base = 16px) | 0:31-0:40 |

## Before / after
- **Value-named vs role-named tokens.** Bad ("Fragile"): `color-<hue>-500`, `color-<neutral>-200`, `color-<hue>-500` for errors, `spacing-16`, `font-14`; a rebrand needs 5 manual updates because each name now describes a value it no longer holds. Good ("Resilient"): `color-primary`, `color-surface`, `color-error`, `spacing-md`, `font-body` with the same values; rebrand = 0 renames. Why: the name encodes intent, which survives value changes; a value-based name becomes a lie after the first change.
- **Arbitrary values vs a scale.** Bad: card with 13px padding, 17px gap, 22px radius, 15px font. Good: each snaps to the nearest scale step (12, 16, 24, 16), and a modal built from the same steps shares the rhythm. Why: a constrained set removes per-instance guessing and makes neighbouring components visually consistent.
- **Inverting vs swapping token sets.** Bad (implied): dark mode by inverting colours. Good: the same components read `--surface`, `--on-surface`, `--primary`; the dark set gives a dark surface, light on-surface text and a lighter primary. Why: each theme is designed, not computed; accent and contrast are tuned per theme.
- **Flat vs layered.** Good: primitive -> semantic -> component. Changing one primitive's value recolours `primary` and then `btn-bg` automatically ("Change one. Cascade everywhere."). Why: references, not copies, propagate changes.

## Do
- Name semantic tokens by role: primary, surface, on-surface, error, spacing-md, font-body.
- Keep one spacing scale (4px base: 4, 8, 12, 16, 24, 32, 48) and snap off-scale values to the nearest step.
- Implement themes as alternate values of the same semantic tokens.
- Layer: primitives hold raw values, semantic tokens reference primitives, component tokens reference semantic tokens.

## Don't
- Don't reference value-named primitives (hue + step, `spacing-16`) directly from components.
- Don't scatter raw hex/px values in components.
- Don't derive dark mode by inverting colours.

## Scene by scene
- 0:00 Raw values (hex codes, px sizes, a font weight, opacity 0.5) scattered, then lined up under "Design tokens".
- 0:02 "Naming matters": two columns, "Fragile" (value-named tokens) vs "Resilient" (role-named tokens), same values; at 0:07 badges "Rebrand: 5 manual updates" vs "Rebrand: 0 changes needed"; fragile column dims.
- 0:11 "4-point scale": scale ruler 4 / 8 / 12 / 16 / 24 / 32 / 48; "Card component" lists off-scale values (13, 17, 22, 15 px); they animate to 12 / 16 / 24 / 16 with a "Snapped" label; a "Modal component" appears using 24 / 16 / 16 / 16, "Same scale, same rhythm".
- 0:22 "Alias tokens": a small app mock (header, two cards, Continue button) with `--surface`, `--on-surface`, `--primary` listed below; a toggle sweeps it to dark, values swap; "Same tokens. Different values." then light and dark side by side, "Same components. Different feel."
- 0:31 "Token architecture": three rows, Primitives (raw values: a hue-500 colour, a neutral-100 colour, space-4 = 16px), Semantic (primary, surface, spacing-md), Component (btn-bg, card-bg, card-padding), with connecting lines; the first primitive's value changes and the highlight runs down to primary and btn-bg. "Change one. Cascade everywhere."
- 0:41 Outro: "Your design system is only as strong as its tokens", follow button.

## Voice-over summary
- Most teams name colours wrong: a hue-and-step name says nothing, "primary action" says everything.
- Semantic names survive redesigns, hex codes do not.
- Random values create random designs; a 4-point scale forces consistency for every spacing, size and radius.
- Dark mode is swapping one token set for another, not inverting colours.
- Three layers: primitives define raw values, semantic tokens give meaning, component tokens lock usage; one primitive change cascades.

## Notes for the skill
- CSS: primitives as custom properties (`--palette-<hue>-500`), semantic aliases (`--color-primary: var(--palette-<hue>-500)`), component tokens (`--btn-bg: var(--color-primary)`); theme via `[data-theme="dark"] { --color-surface: ...; }` or `prefers-color-scheme`. Components read only semantic/component tokens.
- The video's own architecture names primitives by hue and step and then changes a hue-named primitive to a different hue, which is exactly the "lie" it warns about. Correct practice: value-named names are fine for primitives as long as you add a new primitive rather than mutate one into another hue; rebrands repoint semantic tokens to new primitives.
- The scale includes 12 even though the main steps are 8-multiples; it is a 4px-base scale with selected steps, not "every multiple of 4".
- Snapping font-size to the spacing scale is a simplification; typography usually has its own type scale and line-height tokens. Snapping 15px body text up to 16px is fine; do not force all text sizes onto spacing steps.
- Theme swaps must re-verify contrast per theme (4.5:1 body text, 3:1 large text and UI parts). In the dark set the primary is lightened, which is the right move for contrast on dark surfaces.
- Also tokenise motion (durations, easings), radius, elevation and z-index, not only colour and spacing.
