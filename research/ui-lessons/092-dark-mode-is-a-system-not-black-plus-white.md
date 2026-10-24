---
lesson: 092
kind: video
duration_s: 79
type: ui
category: visual
topic: dark mode as a system (near-black base, lightness elevation, text alpha tiers, calmer accent, alpha hairlines, dimmed images)
sources: frames, voice-over
---

# Dark mode is a system, not black plus white

**Hook:** A black background with white text is not dark mode; it is a terminal.

## Main rule
Build dark mode from six coordinated decisions: start from a near-black base (not pure black), express elevation by making higher surfaces lighter (not by shadows), set text as one light colour at three opacity tiers (87 / 60 / 38 %), lighten and desaturate the accent while keeping its hue, draw edges with a 1 px light hairline at about 8 % alpha, and dim photos to about 90 % brightness while giving illustrations a redrawn dark variant.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| L 0 % on all layers | "before": page, card and chip all pure black, so they merge | 0:05-0:12 on-screen |
| page L 5 %, card L 9 %, chip L 12 % | near-black base and stacked surfaces ("room for layers") | 0:13-0:16 on-screen |
| Levels 0 page, 1 card, 2 menu, 3 modal | elevation scale; each level a lighter surface | 0:18-0:27 on-screen |
| `box-shadow: 0 24px 64px` pure black (struck through) | shadow that does not read on a dark surface | 0:17-0:27 on-screen |
| 100 % / 100 % / 100 % | "before": primary, secondary and disabled text all pure white | 0:28-0:33 on-screen |
| 87 % primary, 60 % secondary, 38 % disabled | text opacity tiers of one light colour ("One color, three alphas"); code `rgb(255 255 255 / .87)` | 0:34-0:42 on-screen + voice |
| S 85 %, L 48 % → S 70 %, L 60 % → S 45 %, L 70 %, hue locked | accent adjusted for dark surfaces ("Same hue · lighter · softer") | 0:43-0:54 on-screen |
| 1px, light colour at 8 % alpha (`rgb(255 255 255 / .08)`) | hairline border on cards and inputs | 0:56-1:04 on-screen + voice |
| "fixed gray … Δ 9" vs "alpha 8% … Δ constant" | comparison: a fixed grey border changes its visible difference as the surface lightens, an alpha border keeps it constant (interpretation of the labels; the meaning of "Δ 9" is not explained) | 1:00-1:04 on-screen |
| `filter: brightness(.9)` | photos on dark pages (before: `filter: none · brightness 100%`) | 1:05-1:14 on-screen + voice |
| brightness(.9) on a light illustration: "still glare" | illustrations need a redrawn dark variant instead of a filter | 1:12-1:14 on-screen |
| 6 decisions | checklist: Surface, Elevation, Text, Accent, Hairline, Images | 1:15 on-screen |

Exact hex values shown in the video for the base, surfaces and accent are omitted (colour-independent skill).

## Before / after
- **Pure black vs near black.** Bad: page, card and chip are all L 0 %; the stack collapses into one plane ("saves OLED battery ✓, kills depth ✗"). Good: page L 5 %, card L 9 %, chip L 12 %. Why: nothing can sit below black, so with a black page there is no darker step for depth; starting slightly above black leaves room for layers.
- **Shadow vs lightness elevation.** Bad: a large black shadow under a card on a dark page is invisible ("no shadow" reads the same), so the card floats nowhere. Good: an export dropdown opening over the card uses a lighter surface (level 2) than the card (level 1), the modal is lighter still (level 3). Why: on dark backgrounds the perceptual cue for "closer" is lightness, not shadow.
- **Pure white text vs alpha tiers.** Bad: all text at 100 % white "vibrates" against the dark surface and every line has equal weight. Good: primary 87 %, secondary 60 %, disabled 38 % of one light colour, controlled by one variable. Why: full contrast on dark causes halation/glare during reading; opacity tiers create hierarchy without new colours and adapt to any surface.
- **Saturated accent vs calmed accent.** Bad: the brand accent at high saturation (S 85 %, L 48 %) glows past its edges and outshines content. Good: same hue, lighter and less saturated (S 45 %, L 70 %). Why: saturated colours on dark surfaces bloom and look heavier than on light; desaturating restores balance.
- **No border vs alpha hairline.** Bad: `border: none`; the search input and card edges disappear ("No edge, no shape"). Good: 1 px light hairline at 8 % alpha. Why: a translucent line keeps the same relative contrast on every surface level, while a fixed grey border becomes too strong or too weak as surfaces lighten.
- **Bright image vs dimmed image.** Bad: the hero photo at full brightness pulls every eye on a dim page ("Bright image, stolen attention"). Good: `filter: brightness(.9)`. Illustrations: a filtered light illustration still glares, so a redrawn dark variant is used. Why: the brightest area of a dark page captures attention; photos tolerate dimming, flat illustrations need new artwork.

## Do
- Use a near-black base and step surfaces up in lightness (e.g. L 5 / 9 / 12 %).
- Map elevation levels (page, card, menu, modal) to progressively lighter surfaces.
- Define text as one light colour with three opacity tokens: 87 % primary, 60 % secondary, 38 % disabled.
- Derive a dark-mode accent from the brand hue with higher lightness and lower saturation.
- Use 1 px hairlines in a light colour at about 8 % alpha for edges of cards and inputs.
- Dim photos slightly (about 90 % brightness) and ship dark variants for illustrations.

## Don't
- Don't use pure black for the base or pure white for body text.
- Don't rely on drop shadows for elevation in dark mode.
- Don't reuse the light-mode saturated accent unchanged.
- Don't use a fixed grey border value that must be retuned for every surface.
- Don't apply a brightness filter to illustrations and call it a dark variant.

## Scene by scene
- 0:00 "Dark mode · 01": analytics card (avatar "Maya Torres, Acme Analytics", $48,250, +12.4 % vs last month, bar chart, "Export report" button, mountain hero image) on pure black with pure white text; terminal line `dark-mode --invert`; tag "pure black + pure white = zero depth". Title "Black background. White text. Not dark mode. A terminal."
- 0:05 "01 Surface: Near black, not black.": three stacked planes (page, card, chip) all L 0 %; chips "saves OLED battery ✓", "kills depth ✗"; caption "OLED wins battery. You lose depth."
- 0:13 Planes switch to L 5 / 9 / 12 % and separate visibly; caption "room for layers".
- 0:17 "02 Elevation: Lightness is elevation.": card with a big black shadow labelled "no shadow" (it does not show); scale 0 page, 1 card, 2 menu, 3 modal.
- 0:21 The shadow declaration is struck through; the export menu (CSV, PDF) opens on a lighter surface; levels highlight; caption "Raise with lightness, not shadow".
- 0:28 "03 Text: Three tiers of white.": bars primary / secondary / disabled all at 100 %; caption "Never pure white".
- 0:34 Bars animate to 87 %, 60 %, 38 %; badges on the card mark the amount (primary), the description (secondary) and the "Forecast available on Pro" line (disabled). Code `color: rgb(255 255 255 / .87)`, caption "One color, three alphas".
- 0:43 "04 Accent: Calm the accent.": the Export button glows; HSL readout S 85 %, L 48 %; caption "Saturated glows past its edges".
- 0:50 Readout moves to S 70 %, L 60 %, then S 45 %, L 70 % with "H locked"; caption "Same hue · lighter · softer".
- 0:55 "05 Hairline: Alpha hairlines.": `border: none`, dashed outline around the borderless search field; caption "No edge, no shape".
- 0:56 A 1 px hairline traces the card and input; code `1px · rgb(255 255 255 / .08)`; rows "fixed gray … Δ 9" vs "alpha 8% … Δ constant"; caption "Alpha adapts. Hex doesn't."
- 1:05 "06 Images: Dim the photos.": hero photo at `filter: none · brightness 100%` with eye icons drawn to it; a white-background "light variant" illustration glares; caption "Bright image, stolen attention".
- 1:10 `filter: brightness(.9)` on the photo; the light illustration with the filter is marked "still glare"; a "redrawn dark variant" replaces it; caption "Photos: dim. Illustrations: redraw."
- 1:15 "Dark mode is a system.": final card plus checklist Surface, Elevation, Text, Accent, Hairline, Images; follow and save buttons.

## Voice-over summary
- Black background with white text is a terminal, not dark mode; pure black saves OLED battery but kills depth because nothing sits lower than black.
- Shadows disappear on dark; raise surfaces with lightness, the higher the lighter.
- Pure white text vibrates; drop to 87 %, secondary 60 %, disabled 38 %: "three tiers, one variable."
- A saturated brand colour bleeds and outshines content; lighten and desaturate it, same hue, less weight.
- Edges need a 1 px hairline of white at 8 % alpha; use alpha, not a fixed grey, so it adapts as surfaces lighten.
- Photos glare on dark: dim to 90 % brightness; illustrations get a dark variant, not a filter.

## Notes for the skill
- Tokens: `--surface-0..3` (page, card, menu, modal; increasing lightness), `--text-primary / --text-secondary / --text-disabled` as one foreground with alpha .87 / .60 / .38, `--accent-dark` (same hue, higher L, lower S), `--border-hairline: 1px solid rgb(from var(--fg) r g b / .08)`. The 87/60/38 tiers and lightness-as-elevation match Material Design's dark theme guidance.
- Contrast caution: when the accent is lightened to about L 70 %, white button text on it falls far below 4.5:1 (by calculation roughly 2.5:1 for the values shown; the video keeps a light label on the lightened button). Switch the label on a lightened accent to a dark foreground and verify 4.5:1 (WCAG 1.4.3). Also verify secondary text (60 %) on the lightest surface it appears on.
- Disabled text at 38 % is exempt from WCAG contrast only when it is really disabled; don't use the disabled tier for informational text such as "Forecast available on Pro", which the video does.
- An 8 % alpha hairline is decorative and will not meet the 3:1 non-text contrast (WCAG 1.4.11) needed for input boundaries; form fields need a stronger border or another visible boundary cue (fill difference, focus ring).
- Alpha text over images or varying backgrounds can drop in contrast; use solid computed colours where the background is not a known surface.
- Images: `filter: brightness(.9)` on `img` in dark mode only (e.g. under `prefers-color-scheme: dark` or a theme class); provide illustrations via `<picture>` with a `media="(prefers-color-scheme: dark)"` source or theme-specific assets.
- "Pure black saves OLED battery" is true but the saving from near-black (L 5 %) versus true black is small on most screens; true black can also cause smearing on OLED when scrolling, another reason to avoid it.
