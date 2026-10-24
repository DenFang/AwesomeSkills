---
lesson: 017
kind: video
duration_s: 26
type: ui
category: visual
topic: border-radius as brand personality (0 / 8 / 20 px / pill spectrum)
sources: frames, voice-over
---

# Corner radius sets the tone of the whole UI

**Hook:** One CSS property, border-radius, is enough to change how a whole interface feels.

## Main rule
Choose a base corner radius deliberately to match the product's personality (square for institutional and authoritative, small for professional and B2B, larger for friendly consumer apps, full pill for playful/social) and apply it consistently, instead of picking a value per component by guesswork.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 0px | "Feels corporate" card at the sharp end of a radius slider | 0:00-0:01 on-screen slider |
| 36px, 40px | "Feels friendly" card at the rounded end of the slider | 0:01-0:03 on-screen slider |
| 90° | sharp corner annotated as the point where "the eye snags" | 0:06-0:08 on-screen |
| 32px | rounded corner annotated "Rounded = Eye flows" | 0:09-0:10 on-screen |
| 0px | Authority: banks, law firms (voice adds government, legal) | 0:11-0:13 on-screen + voice |
| 8px | Professional: SaaS, enterprise (voice: B2B) | 0:14-0:16 on-screen + voice |
| 20px | Friendly: consumer apps | 0:16-0:20 on-screen + voice |
| 50% (full pill) | Playful: social, Gen Z | 0:21 on-screen + voice |

## Before / after
- **Sharp vs rounded card.** A slider drags a sample card (icon, text lines, two chips, CTA) from 0px to 40px; the badge flips from "Feels corporate" to "Feels friendly". Why (as claimed): a 90° corner is a hard stop for the eye, while a curve lets the gaze continue along the edge. The perceptual effect is real in the sense that rounded shapes read as softer and more approachable; "friction" is the video's framing.
- **Spectrum of four presets.** The same card and "Get Started" button are shown at 0px, 8px, 20px and 50%, each labelled with a personality and a product category. Mechanism: radius is a strong, global stylistic signal; a uniform choice across components reads as an intentional brand voice.

## Do
- Decide one base radius for the product as a design token early, based on brand tone.
- Map tone to range: 0 for institutional/authoritative, about 8px for professional SaaS/B2B, about 20px for friendly consumer products, full pill for playful/social.
- Apply that choice consistently across cards, buttons and inputs (scaled by element size; see the later "radius is a system" video).

## Don't
- Don't pick radius values ad hoc per component ("stop guessing radius").
- Don't mix sharp and very round corners at random in one interface.

## Scene by scene
- 0:00 Title "One CSS property changes everything"; a sample card with a `border-radius:` slider at 0px (labels Sharp / Rounded), badge "Feels corporate".
- 0:01 Slider moves to 36px then 40px; the card, icon and CTA round off, palette shifts warmer, badge "Feels friendly"; caption "The psychology behind rounded corners".
- 0:04 Flat card corner on a grid; caption "Sharp corners create friction".
- 0:06 Zoom on a 90° corner highlighted in a danger colour with a target ring: "Sharp corner = Eye snags".
- 0:09 The corner morphs into a 32px curve drawn in a success colour: "Rounded = Eye flows".
- 0:11 "The spectrum: every pixel changes the vibe". 0px: "Authority, Banks • Law firms".
- 0:14 8px: "Professional, SaaS • Enterprise".
- 0:17 20px: "Friendly, Consumer apps".
- 0:21 50%: "Playful, Social • Gen Z".
- 0:22 End card "Stop guessing radius. Match it to your brand." with a follow pill button.

## Voice-over summary
- One CSS property changes how the UI feels.
- Sharp corners create friction: the eye catches on the edge; rounding lets it flow through.
- Zero pixels for authority (banks, government, legal), eight for professional B2B, twenty for friendly consumer apps, full pill for playful social and Gen Z.
- Match the radius to the brand: "One rule, infinite impact."

## Notes for the skill
- Treat the brand-tone mapping as a heuristic, not a law; plenty of products break it (e.g. professional tools with large radii). The durable rule is consistency through a radius token scale.
- The "eye snags on corners" explanation is simplified. Research on curvature preference (rounded shapes rated as more pleasant/safe) supports the general direction, but it is not about eye-tracking friction.
- One base value is not enough in practice: radius should scale with element size and nest correctly (inner = outer minus padding). See 20260902_Dcx__07t8e5 for the system version.
- `border-radius: 50%` makes a pill only on a square-ish or circular element; on a wide rectangle it produces an ellipse. For pill buttons use a large fixed value (e.g. `9999px`) instead of 50%.
- Radius changes nothing for accessibility directly, but very large radii on small or dense elements reduce usable content area; keep focus rings following the same radius (`outline` follows `border-radius` in modern browsers).
