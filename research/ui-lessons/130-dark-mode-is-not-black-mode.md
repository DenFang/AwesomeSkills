---
lesson: 130
kind: video
duration_s: 35
type: ui
category: visual
topic: dark mode surfaces, accent saturation, text brightness
sources: frames, voice-over, lesson notes
---

# Dark mode is not black mode

**Hook:** Same app twice: one just inverts colours, the other feels premium.

## Main rule
Build dark UI on a near-black (not pure black) base and express elevation by making each higher surface slightly lighter; lower the saturation of accent colours (about 20%) and never set text to pure white: about 90% white for headings and 70% for body text.

## Numbers and values
Colour values are given as HSL lightness / saturation of neutral greys, converted from the on-screen swatches (no palette values per the colour rule).

| Value | Applies to | Where shown |
|---|---|---|
| base ≈ 7% lightness (neutral grey, near-black) | lowest surface / page background | 0:06-0:13 on-screen swatch; page names the same value |
| surface ≈ 12% lightness | first raised layer (cards) | 0:07-0:13 on-screen swatch |
| elevated ≈ 17% lightness | highest layer (popovers, raised cards) | 0:08-0:13 on-screen swatch |
| 3 layers: Base → Surface → Elevated, each ≈ 5 lightness points apart | elevation ladder, labelled "DEPTH" | 0:06-0:13 |
| 0% lightness (pure black) | the WRONG base | 0:00 WRONG card; page says avoid pure black |
| 100% → 80% saturation, "-20%" | accent buttons (primary CTA, success "Confirm") | 0:15-0:21 on-screen + voice ("desaturate by 20%") |
| 100% white | WRONG text colour, labelled HARSH | 0:23-0:29 |
| "90% white" (on-screen swatch is ≈ 88% lightness) | comfortable text, labelled COMFORTABLE; headlines | 0:24-0:30 on-screen + voice |
| 70% white | body text | 0:27-0:30 on-screen + voice |

Note: the "80% saturation" labels do not match the example colours shown: converted to HSL, the two desaturated buttons sit at about 57% and 64% saturation (and also shift lightness). Treat "-20%" as a direction, not a precise formula.

## Before / after
1. **Base and elevation (0:00, 0:05-0:13).** Before (WRONG card): pure black page with nearly black tiles; there is no visible separation between card, tiles and page, and shadows cannot show on black. After (RIGHT card): near-black base with tiles one step lighter. Why it works: in dark UI shadows are almost invisible, so lightness takes over the role of elevation; nearer surfaces are lighter, which matches how light falls on raised objects. Pure black also maximises contrast with white text, which increases glare and halation for many readers.
2. **Accent saturation (0:14-0:21).** Before: a fully saturated primary button and a fully saturated success button, both with a glow; they "vibrate" against the dark background. After: the same hues desaturated about 20%. Why it works: saturated colours on dark backgrounds create strong simultaneous contrast and visual vibration; reducing saturation keeps the accent recognisable while lowering eye strain and making it look deliberate.
3. **Text brightness (0:22-0:30).** Before: paragraph in pure white, labelled HARSH (eye strain, reduced comfort over time). After: paragraph at about 90% white, labelled COMFORTABLE. Then a hierarchy: headlines 90% white, body 70% white. Why it works: slightly dimmed text reduces glare and halation while still far exceeding 4.5:1 on a near-black base; opacity tiers create hierarchy without adding new colours.

## Do
- Use a near-black neutral base (around 7% lightness) instead of pure black.
- Define 3 or more surface tokens that get lighter as elevation increases (about +5 lightness points per step in the example).
- Desaturate accent colours for the dark theme (about 20% less saturation; verify contrast after the change).
- Set high-emphasis text to about 90% white and body text to about 70% white; use lower opacity tiers for secondary and disabled text.

## Don't
- Don't invert a light theme and call it dark mode.
- Don't use pure black as the page background.
- Don't reuse the light theme's fully saturated accents on dark surfaces, especially with glows.
- Don't set long-form text in pure white.

## Scene by scene
- 0:00 "Same app.": two dashboard cards side by side ("DarkApp", tiles Users 2.4k and Revenue $18k, a Get Started button). WRONG: pure black, saturated button. RIGHT: layered grey tiles, calmer accent.
- 0:01 The WRONG card leaves; RIGHT card centred, subtitle "One feels premium."
- 0:04 "Layered Surfaces / Dark mode is not black mode": a Base swatch appears.
- 0:06 Surface swatch slides in below, then Elevated; each gains its value label.
- 0:11 A vertical "DEPTH" arrow appears alongside the three swatches.
- 0:14 "Soften Your Colors / Desaturate accent colors for dark UI": two Subscribe buttons (100% saturation vs 80%), "-20%" chip with arrow.
- 0:17 Second pair: Confirm buttons (100% with glow vs 80%).
- 0:22 "Calibrate Your Text / Never use pure white on dark backgrounds": pure-white paragraph card tagged HARSH.
- 0:24 Second card with the dimmed white tagged COMFORTABLE.
- 0:27 Two tiles: Headlines "Aa" 90% white, Body Text "Aa" 70% white.
- 0:31 Summary: Layered Surfaces (not pure black), Soft Colors (desaturate 20%), Calibrated Text (never pure white).

## Voice-over summary
- An inverted-colour dark theme looks cheap; a crafted one looks premium.
- "Dark mode is not black mode": use layered surfaces, not pure black.
- Each layer gets slightly brighter, which creates depth without lighting.
- Desaturate accent colours by 20%; bright colours on dark backgrounds "burn", soft ones are easier on the eye.
- Never use pure white text: 90% white for headlines, 70% for body.

## Notes for the skill
- Tokens: `--surface-0` (base), `--surface-1`, `--surface-2` (lighter as they rise). Material Design's dark theme uses the same idea (white overlay of increasing opacity per elevation); an overlay approach keeps the ladder consistent if the base changes.
- Text tiers via opacity of the on-surface colour: about 0.90 high emphasis, 0.70 body/medium, and roughly 0.38-0.50 for disabled. Check that the lowest tier used for meaningful text still reaches 4.5:1 (3:1 for large text); disabled text is exempt from WCAG 1.4.3 but should still be legible.
- Contrast check on the example: 90% white on the 7% base is about 14:1 and 70% white is about 9:1, so both pass easily; the advice is about glare, not about passing WCAG.
- Contrast warning the video ignores: desaturating and lightening an accent can break the contrast of the label on top of it. In the example, light text on the softened success button is only about 1.7:1 (fails WCAG 1.4.3); on the saturated version it is also poor. When softening an accent, switch its label to dark text or darken the fill until the label reaches 4.5:1.
- Keep focus rings and borders visible: outline colours chosen for light mode often disappear on dark surfaces; non-text contrast needs 3:1 (WCAG 1.4.11).
- Shadows still help on the higher layers if made darker and larger, but lightness is the primary elevation cue in dark mode.
- Respect `prefers-color-scheme` and offer a manual toggle; dark theme should be designed as its own token set, not computed by inversion.
- "Pure white text causes eye strain" is a common recommendation (halation, especially for users with astigmatism), not a WCAG requirement.
