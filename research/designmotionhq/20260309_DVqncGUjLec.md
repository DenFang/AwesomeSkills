---
id: DVqncGUjLec
reel_url: https://www.instagram.com/reel/DVqncGUjLec/
pattern_page: none
date: 2026-03-09
duration_s: 74
type: ui
category: visual
topic: Five optical corrections (play icon, shape size, nested radius, dark-mode weight, button text)
sources: frames, voice-over, caption
---

# Five optical corrections: math vs perception

**Caption:** "Pro design tips, save it for later."
**Hook:** Designers nudge things "by feel", and they are right to.

## Main rule
Align and size by perceived (optical) geometry, not by bounding boxes: offset asymmetric icons toward their visual centroid, enlarge round shapes next to square ones, make nested corner radii concentric (inner = outer minus gap), lighten text weight on dark backgrounds, and correct the vertical position of button labels.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| `shift += bbox_width × 0.08` | play triangle moved right by 8% of its bounding-box width to sit on its visual centroid | 0:10-0:18 on-screen code |
| 200px vs 200px | square vs circle at the same nominal size ("Circle looks smaller") | 0:19-0:23 on-screen |
| 221px (intermediate) then 226px | circle size animating up to optical equality with the 200px square | 0:24-0:25 on-screen |
| `circle_size = square × 1.13` | circle about 13% larger than a square to look equal (voice: "about 13% larger") | 0:24-0:30 on-screen + voice |
| outer 32px / inner 32px / gap 14px | same radius on nested element: "Pinched corners" | 0:32-0:35 on-screen |
| inner 21px (intermediate), then 18px | inner radius animating down to the corrected value | 0:36-0:37 on-screen |
| outer 32px / inner 18px / gap 14px | corrected nested radius, `inner = outer - padding` ("Smooth curves") | 0:37-0:42 on-screen |
| weight 600 light vs weight 600 dark | same weight looks heavier on dark ("Dark mode looks heavier") | 0:44-0:47 on-screen |
| weight 600 light vs weight 500 dark, `dark_mode: weight - 100` | one weight step lighter in dark mode ("Visually balanced") | 0:48-0:53 on-screen + voice |
| `padding-top: +2px` | button label vertical correction ("Cap-height aligned"); voice says "a two pixel nudge up" | 0:59-0:65 on-screen + voice |
| 5 | number of corrections in the recap | 0:66-0:70 |

## Before / after
- **Play button.** Before: triangle centred on its bounding box ("bbox center"), looks shifted left ("Looks lopsided"). After: triangle shifted right by about 8% of its box width, onto its visual centroid ("Optically centered"). Why: a triangle's mass sits toward its wide base; the eye centres the mass, not the box. The reel cites YouTube, Spotify and Apple doing this.
- **Shape sizing.** Before: square and circle both 200px; the circle reads smaller. After: circle 226px (x1.13) looks equal. Why: the eye compares area; a circle covers about 78.5% of its bounding square, and 2/sqrt(pi) ≈ 1.128 equalises the areas. "Icon grids use this."
- **Nested border radius.** Before: inner button radius 32px inside a 32px container with 14px gap: the gap band is thin at the corners and thick on the sides ("Pinched corners"). After: inner 18px = 32 - 14, curves run parallel ("Smooth curves"). Why: concentric arcs keep the gap constant around the corner. Shown with a 4x zoom inset of the corner.
- **Dark-mode weight.** Before: "The quick brown fox" at weight 600 in both light and dark cards; the light-on-dark one looks bolder. After: dark card at 500. Why: irradiation illusion, light glyphs appear to bleed into the dark surround and look thicker.
- **Button text centring.** Before: label in a pill button is mathematically centred but looks low ("Text sits too low"), annotated "descender space below baseline". After: corrected by 2px ("Cap-height aligned"). Why: CSS centres the whole line box including descender space, while the eye centres the cap height / x-height of the letters; buttons with no descenders look low.

## Do
- Offset play/arrow/chevron glyphs toward the point they indicate so their mass is centred (about 8% of glyph width for a play triangle, per the reel).
- In icon sets, draw circles and other round shapes about 10-13% larger than squares on the same grid.
- Compute nested radius: `inner-radius = outer-radius - padding` (clamp at 0).
- Consider one weight step lighter for light text on dark backgrounds, verified by eye at real sizes.
- Check button labels visually; trim or compensate for line-box space below the baseline.

## Don't
- Don't trust bounding-box centring for asymmetric icons.
- Don't reuse the same border radius for a container and the element inset inside it.
- Don't assume identical weight renders identically in light and dark themes.

## Scene by scene
- 0:00 Large play button in a ring with crosshair guides, then "Optically correct." badge.
- 0:04 "#1 Play Button": smaller button, triangle on "bbox center" guide; badge "Looks lopsided".
- 0:10 Triangle slides right onto a "visual centroid" guide; "Optically centered", code `shift += bbox_width × 0.08`; text: YouTube, Spotify, Apple all shift the triangle right.
- 0:19 "#2 Shape Sizing": filled square vs circle, both 200px, "Same size? Both set to 200px", badge "Circle looks smaller".
- 0:24 Circle grows (221px, then 226px); "Optically equal", `circle_size = square × 1.13`; text: icon grids use this, your brain reads area, not pixels.
- 0:31 "#3 Border Radius": zoomed corner inset (x4) above a "Get Started" button inside a container; readout outer 32px / inner 32px / gap 14px; "Pinched corners".
- 0:36 Inner radius animates 21px then 18px; "Smooth curves", `inner = outer - padding`; text: Apple added this to iOS guidelines, most devs still miss it.
- 0:43 "#4 Dark Mode Weight": light card and dark card with the same sentence, both weight 600; "Same weight, different feel", "Irradiation illusion: light bleeds into dark"; badge "Dark mode looks heavier".
- 0:48 Dark card switches to weight 500; "Visually balanced", `dark_mode: weight - 100`; text: Apple reduces font weight by one step in dark mode.
- 0:54 "#5 Text Centering": pill "Get Started" button with a red "descender space below baseline" annotation; badge "Text sits too low".
- 0:59 Label shifts; "Cap-height aligned", `padding-top: +2px`; text: CSS centers the line box, your eye centers the letters.
- 1:06 Recap list "5 optical corrections, Math is not always right": Play Button, Shape Sizing, Border Radius, Font Weight, Text Center; "Your eyes are the judge."
- 1:11 End card "More design secrets? @designmotionhq" with Follow button.

## Voice-over summary
- Centring a play triangle on its box looks off; designers move it slightly right to the visual centroid, as YouTube, Spotify and Apple do.
- A circle and a square of equal pixel size do not look equal; the circle needs about 13% more because perception follows area.
- Equal radii on nested elements pinch the corners; inner radius should be outer radius minus the gap, which the narrator says every iOS card follows.
- Light text on dark looks heavier (irradiation illusion); Apple is said to drop weight by one step in dark mode.
- CSS centres the full line box including space below the baseline, so button text looks low; a 2px nudge fixes it.
- Closing idea: five corrections that are mathematically unnecessary but visually essential.

## Notes for the skill
- Play icon in CSS: `transform: translateX(8%)` on the glyph (percent of its own width), or bake the offset into the SVG viewBox so every usage is correct.
- Concentric radius token: `--radius-inner: max(0px, calc(var(--radius-outer) - var(--pad)))`.
- Button text: the on-screen `padding-top: +2px` would push the label down, which contradicts the voice-over's "nudge up". To raise the label, use asymmetric padding (more at the bottom, e.g. `padding-block: calc(var(--py) - 1px) calc(var(--py) + 1px)`), a small `translateY(-1px)`, or the modern `text-box: trim-both cap alphabetic` (`text-box-trim` / `text-box-edge`) to centre on cap height. The correct offset depends on the font's metrics; do not hard-code 2px across fonts.
- Dark-mode weight: implement as a theme token (e.g. `--fw-body: 400` light, a lower step or variable-font axis value in dark). Keep contrast at least 4.5:1 for body text after thinning; very thin weights on dark backgrounds can hurt legibility. The claim that Apple systematically drops one weight step in dark mode is not stated in Apple's HIG as far as known; treat it as unverified, the optical principle itself (irradiation) is sound.
- Shape sizing: 1.13 is the pure area-equalisation factor; Material icon keylines use a slightly smaller ratio (circle 20 vs square 18 in a 24 grid, about 1.11). Either is a starting point; final check by eye.
- "Every iOS card follows this rule" is an overstatement, but concentric corners are recommended by Apple's guidance.
