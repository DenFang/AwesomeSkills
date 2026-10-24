---
id: DUQqwPBDLhL
reel_url: https://www.instagram.com/reel/DUQqwPBDLhL/
pattern_page: none
date: 2026-02-02
duration_s: 52
type: ui
category: visual
topic: building a primary checkout button property by property (fill, padding, radius, type, shadow, hover)
sources: frames, voice-over, caption
---

# Primary CTA button, rebuilt one CSS property at a time

**Caption:** Simple CSS can be very powerful.
**Hook:** A polished checkout "Buy Now" button is stripped back to a raw unstyled HTML button, then rebuilt to show what each CSS line contributes.

## Main rule
A primary call-to-action gets its weight from a small, deliberate stack of properties: a solid accent fill with high-contrast label, generous horizontal padding, a moderate corner radius, a semibold label, a soft shadow tinted with the fill colour, and a small hover scale. Each property has one job; add them deliberately rather than by default.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| `padding: 20px 64px` | button padding (vertical / horizontal, ratio about 1:3) | 0:16 onward, code panel |
| `border-radius: 14px` | button corners | 0:20 onward, code panel |
| `font-weight: 600` | label weight (semibold) | 0:23 onward, code panel |
| `font-size: 28px` | label size in the demo (large because the demo button is shown huge; not a production size) | 0:25 onward, code panel |
| `box-shadow: 0 4px 20px` + fill colour at alpha 0.4 | tinted "glow" shadow under the button | 0:30-0:35, code panel (written as rgba of the fill colour, 0.4) |
| `transform: scale(1.05)` | `:hover` state | 0:37-0:42, code panel |
| `color: white` on accent fill | label contrast | 0:14, code panel + voice |

No transition duration or easing is shown for the hover scale.

## Before / after
- **Raw button vs styled button.** Bad: the browser default (grey bevelled box, thin border, default font) reads as a form control, not as the main action. Good: solid accent fill with white label; it immediately becomes the focal point. Why: a saturated fill against a dark, low-chroma surface creates the strongest figure-ground contrast on the screen, so the eye lands there first.
- **Tight vs generous padding.** Bad: label hugging the edges. Good: 20px / 64px. Why: a wider hit area and visual mass make it read as the primary action and easier to hit; the narrator says it gives the label "room to breathe".
- **Square vs rounded corners.** Sharp default corners vs 14px radius; the narrator ties rounding to a friendlier feel ("Shape = Friendly").
- **Default font vs semibold sans.** Switching to a clean sans and weight 600 makes the label read as confident ("bump up the weight").
- **Flat vs tinted shadow.** Adding a soft shadow in the button's own hue (0 4px 20px, 40% alpha) lifts it off the page ("Depth = Premium"). Why: a coloured, blurred shadow reads as emitted light/elevation rather than a dirty grey drop shadow.
- **Static vs hover scale.** On hover the button grows to 1.05; the narrator frames it as a signal that the element is alive and clickable ("Motion = Action"). On screen the hover state also shifts the fill to a gradient toward a second hue, which the code panel does not show.

## Do
- Give the single primary CTA a solid fill in the brand accent and a label that passes 4.5:1 contrast against it.
- Use horizontal padding roughly 3x the vertical padding for a wide, confident primary button.
- Pick one moderate radius for the button and keep it consistent with the rest of the system.
- Use a semibold (600) label weight for the CTA.
- If you add a shadow, tint it with the button's own fill at low alpha and keep a small y-offset with a wide blur.
- Give hover a small, perceptible response (around 1.05 scale) paired with a short transition.

## Don't
- Don't ship browser-default button styling for a primary action.
- Don't rely on the hover scale as the only interactive cue (touch devices have no hover; keyboard users need a focus style).
- Don't treat "purple means trust" as a rule; the colour should come from the product's theme.

## Scene by scene
- 0:00 Title "How Stripe designed a button that converts" over a small dark "Pay with Stripe" card (email, card number, expiry, CVC fields, "Buy Now" button).
- 0:03 Camera zooms into the button; a code panel shows the full final CSS.
- 0:04 "What if we remove all CSS?": lines delete from the bottom, the button loses shadow, radius and font, then turns into the grey default HTML button.
- 0:07 Empty code panel; raw "Buy Now" default button.
- 0:12 Typing `background:` then fill colour; label "Color = Trust"; then `color: white`.
- 0:15 `padding: 20px 64px` typed; button widens.
- 0:20 "Shape = Friendly": `border-radius: 14px`, `font-family: Inter`, `font-weight: 600`, `font-size: 28px`; corners round and label turns bold.
- 0:29 "Depth = Premium": `box-shadow: 0 4px 20px` with the fill colour at 0.4 alpha; a soft halo appears under the button.
- 0:37 "Motion = Action": `&:hover { transform: scale(1.05); }`; cursor hovers, button grows and shows a two-hue gradient.
- 0:43 Zoom out to the full card; caption "Every CSS choice is a psychological decision."
- 0:48 End card: "What UI element should I decode next?", "Drop it in the comments", follow prompt.

## Voice-over summary
- Opens on a famous payment provider's checkout button and asks what happens if all CSS is removed.
- Walks through each property: background sets the mood, white text gives contrast, padding gives room, radius makes it friendly.
- A clean modern font at heavier weight signals confidence.
- The tinted box shadow makes the button float and feel premium.
- A slight scale on hover tells users the button is alive and clickable.
- Closes with the claim that every CSS property was a psychological decision and asks for the next element to decode.

## Notes for the skill
- Colour-to-emotion mapping ("purple signals trust") and "rounded = friendly" are folk claims, not established rules; in the skill keep the mechanism (one accent reserved for the primary CTA, strong contrast with the surface) and take the actual hue from the project theme.
- The hover is shown without a transition; implement `transition: transform 150-200ms ease-out` (and the same for shadow if it changes) or the scale snaps. Wrap the scale in `@media (hover: hover)` and disable or reduce it under `prefers-reduced-motion: reduce`.
- Add `:focus-visible` (outline or ring offset from the button) and `:active` (e.g. scale 0.98) states; the reel only shows hover. Disabled and loading states for a checkout button are also missing.
- `scale(1.05)` on a wide button (e.g. 300px) moves edges by about 7-8px per side, which is noticeable; on full-width mobile buttons prefer a fill/brightness change instead.
- The 28px label is demo scale only; real primary buttons usually sit at 15-18px label with a 44-48px min height (touch target at least 44x44 pt / 48x48 dp).
- The on-screen hover state shows a gradient fill that the code never declares: treat this as a demo artefact, not part of the recipe.
- A coloured shadow at 0.4 alpha can look muddy on light backgrounds; tune alpha per theme and keep text contrast checks on the fill, not on the glow.
- The "Stripe" framing is the reel's attribution; the CSS is a recreation, not verified as the provider's actual code.
