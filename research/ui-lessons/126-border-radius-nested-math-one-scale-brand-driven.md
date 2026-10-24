---
lesson: 126
kind: video
duration_s: 35
type: ui
category: visual
topic: border radius (nested radius math, radius scale, radius as brand personality)
sources: frames, voice-over, lesson notes
---

# Border radius: nested math, one scale, brand-driven range

**Hook:** The same card can look "off" or "expensive", and the difference comes down to one CSS rule about corner radius.

## Main rule
When a rounded surface sits inside another rounded surface, set the inner radius to the outer radius minus the padding between them, so the curves stay concentric. Take every radius from a single fixed scale (4 / 8 / 12 / 16 / 24 px), grow radius with element size, and choose the overall range (sharp vs round) from brand tone.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| outer 16px, inner 8px, button 8px | "Edit Profile" modal (outer), nested inner section, footer buttons | 0:02-0:06 on-screen labels |
| padding 8px | gap between outer card edge and nested card | 0:08-0:15 on-screen diagram |
| 16 - 8 = 8 | worked example of inner = outer - padding | 0:10-0:13 on-screen formula |
| inner 16px = outer | wrong example, labelled "looks bloated" | 0:12-0:13 on-screen |
| 4 · 8 · 12 · 16 · 24 | the radius scale | 0:14-0:29 on-screen + voice |
| BEFORE: tooltip 12px, input 20px, card 6px, modal 30px, panel 10px | random per-component radii (no relation to size) | 0:16-0:17 on-screen |
| AFTER: tooltip 4px, input 8px, card 12px, modal 16px, panel 24px | radius mapped to scale, increasing with element size | 0:18-0:23 on-screen; same mapping on lesson notes ("~4 / ~8 / ~12 / ~16 / ~24") |
| Serious ↔ Playful slider | small radius = corporate, large radius = friendly | 0:25-0:30 on-screen; exact radii of the two cards not labelled |

## Before / after
1. **Nested corners (0:00-0:15).** Before: a modal with a nested inner section whose corners do not follow the outer curve; the result reads as "something's off" without the viewer knowing why. A second bad case: the inner radius is set equal to the outer radius (16px inside 16px), which makes the inner box look swollen ("looks bloated") because the gap between the curves widens at the corners. After: outer 16px, padding 8px, inner 8px. Why it works: with inner = outer - padding the two arcs share a centre point, so the gap between edges stays constant all the way around the corner; the eye reads constant spacing as deliberate.
2. **Radius values (0:16-0:23).** Before: each component got an arbitrary value (tooltip 12, input 20, card 6, modal 30, panel 10), so small elements are rounder than big ones and nothing relates. After: values come from one scale and step up with element size (tooltip 4 → panel 24). Why it works: a consistent, size-proportional rule produces a visible system; inconsistency is perceived as low quality even when no single value is "wrong".
3. **Personality (0:24-0:31).** Two identical profile cards: one with small radii labelled CORPORATE, one with large radii (rounded button, rounded avatar) labelled FRIENDLY; a Serious ↔ Playful slider with "Choose for your brand". Why: corner shape is a strong tone signal; sharp corners read formal, round corners read approachable.

## Do
- Compute nested radii: `inner = outer - padding` (e.g. 16px outer, 8px padding → 8px inner).
- Define a radius token scale (4, 8, 12, 16, 24 px) and use only those tokens.
- Increase radius with surface size: tooltip 4, input 8, card 12, modal 16, panel 24.
- Pick the overall radius range once, from brand tone (serious → smaller end, playful → larger end).

## Don't
- Don't give a nested element the same radius as its container.
- Don't pick radius values per component by eye.
- Don't let small elements (tooltips, inputs) be rounder than large surfaces (cards, modals, panels).
- Don't mix an oversized playful radius into a product meant to feel serious, or the reverse.

## Scene by scene
- 0:00 "Something's off..." over an Edit Profile modal (avatar row, Full name and Email inputs, Cancel / Save); corners subtly mismatched.
- 0:02 Title "One rule."; labels under the modal: Outer 16px, Inner 8px, Button 8px.
- 0:06 "The Rule": empty card outline, then label outer 16px appears.
- 0:08 Label "padding: 8px" on the top edge, then a nested card with label inner 8px.
- 0:10 Formula chip "16 - 8 = 8 ✓".
- 0:12 Counter-example thumbnail: "inner: 16px = outer", "✗ Looks bloated"; it fades out.
- 0:14 "Radius Scale" with "4 · 8 · 12 · 16 · 24".
- 0:15 BEFORE stack: Tooltip 12px, Input 20px, Card 6px, Modal 30px, Panel 10px (danger-coloured).
- 0:17 Morph to the AFTER stack: Tooltip 4px, Input 8px, Card 12px, Modal 16px, Panel 24px; a vertical ruler with 4/8/12/16/24px marks appears beside it.
- 0:23 "Radius = Personality": profile card (Alex Johnson, 24 Projects, 128 Reviews, View Profile) with small radii, then a twin with large radii.
- 0:25 Badges CORPORATE / FRIENDLY; then a Serious ↔ Playful slider and "Choose for your brand".
- 0:31 Summary list: "Inner = Outer - Padding / The math rule", "4 · 8 · 12 · 16 · 24 / The scale", "Match Your Brand / Perception".
- 0:32 Handle and follow button "Follow for more CSS secrets", "Save this".

## Voice-over summary
- Two copies of the same card: one looks wrong, one looks premium, and a single CSS rule is the difference.
- Inner radius equals outer radius minus padding; when a card sits inside a card, subtract the gap.
- Build a radius scale (4, 8, 12, 16, 24) and always pick from it: "Pick from the scale. Never guess."
- Small radius feels corporate, large radius feels friendly.
- Choose the radius by brand, not by mood.

## Notes for the skill
- CSS: `--radius-xs: 4px; --radius-sm: 8px; --radius-md: 12px; --radius-lg: 16px; --radius-xl: 24px;` and for nesting `border-radius: calc(var(--outer-radius) - var(--inner-padding));`. Clamp at zero: `max(0px, calc(...))`, because when padding ≥ outer radius the formula goes negative; in that case use 0 or the smallest scale step.
- The formula is an approximation that is exactly right only for uniform padding and for elements without visible borders; with a border, subtract the border width too (`outer - padding - border`).
- The size mapping (tooltip 4 → panel 24) is a convention, not a law. The rule underneath it is: radius should be monotonic with element size within one product.
- Pills (`border-radius: 9999px`) are a separate token outside the scale; they do not follow the size rule.
- The video does not label the exact radii of the CORPORATE vs FRIENDLY cards; only the direction (smaller vs larger) is shown.
- The frame-by-frame difference between the 0:00 "off" modal and the corrected modal is subtle at 540px; the precise wrong values in the opening are not labelled on screen.
- No accessibility impact from radius itself; keep focus rings following the element's radius (`outline` follows `border-radius` in modern browsers) and keep an offset ring concentric (`outline-offset` adds to the radius visually).
