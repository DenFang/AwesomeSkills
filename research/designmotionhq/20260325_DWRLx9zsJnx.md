---
id: DWRLx9zsJnx
reel_url: https://www.instagram.com/reel/DWRLx9zsJnx/
pattern_page: https://designmotionhq.com/patterns/shadow-elevation
date: 2026-03-25
duration_s: 33
type: ui
category: visual
topic: layered shadows, accent-tinted glow and 3D lift as an elevation signal
sources: frames, voice-over, pattern page
---

# Shadow elevation: layered shadows, tinted glow, slight 3D lift

**Caption:** Shadow glow can really elevate an UI
**Hook:** The same card can sit flat or float; the difference is three layers of depth.

## Main rule
Build elevation from stacked shadows (a tight contact shadow that anchors the element, a mid-distance shadow, and a wide soft glow tinted with the product's accent colour at low opacity), optionally add a very small 3D lift, and reserve the strongest elevation for the most important element (e.g. the recommended pricing tier).

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| `0 1px 3px rgba(0,0,0,0.4)` | contact shadow ("Tight shadow anchors it") | 0:05-0:15 on-screen; page "~0 1px 3px" |
| `0 8px 24px rgba(0,0,0,0.3)` | mid-distance shadow (appears only in the combined CSS) | 0:11-0:15 on-screen |
| `0 0 60px` accent colour at alpha 0.15 | soft glow behind the card ("Colored glow adds brand") | 0:07-0:15 on-screen |
| `perspective(1000px) rotateX(2deg) translateZ(20px)` | 3D lift ("3D lift creates depth") | 0:09-0:15 on-screen; page "perspective + a small rotateX + translateZ" |
| accent colour at alpha 0.35 | glow on the three tinted dashboard cards (creative app, fintech, health app) | 0:16-0:27 on-screen `box-shadow` labels (blur radius not shown) |
| 3 layers | contact + glow + elevation (video); contact + mid + wide spread (page) | 0:03-0:15 voice/on-screen; page |
| "Impact +40%" | decorative stat on the demo card; no source or meaning given | 0:04-0:15 on-screen |
| $9/mo vs $29/mo | pricing cards: Basic (flat) vs Pro (floats) | 0:00-0:03 on-screen |

Discrepancy: the voice and on-screen labels define the three layers as contact shadow, glow and 3D perspective; the page and the combined CSS block define three box-shadows (contact, mid-distance, wide soft). Both agree on the contact shadow and a soft accent glow.

## Before / after
- **Flat vs floating pricing card.** Bad/neutral: the Basic $9 card has no shadow, muted text, a grey "Get Started" button, labelled "Flat". Good: the Pro $29 card has layered shadows and an accent-tinted glow, an accent "Upgrade Now" button, labelled "Floats". Why: elevation reads as importance, so the tier the business wants chosen visually comes forward.
- **Single blur vs stacked layers.** Bad: one generic drop shadow. Good: a tight, darker contact shadow right under the edge (makes the card feel placed on the surface), a softer mid shadow for distance, and a wide, faint glow; optionally a 2° tilt and 20px Z translation in 1000px perspective. Why: real objects cast a sharp shadow where they touch and a diffuse one further away; combining both makes the depth believable.
- **Neutral vs tinted glow.** Good: the glow uses the product's accent colour (shown on a creative app, a fintech dashboard and a health app, each with its own accent at alpha 0.35). Why: the shadow becomes part of the visual identity rather than a generic grey effect.

## Do
- Stack at least two shadows: a small, tight, darker contact shadow plus one or two larger, softer, lighter ones.
- Tint the soft glow with the product's accent colour at low opacity (0.15-0.35 in the video).
- Use elevation as a hierarchy signal: strongest elevation on the single most important element (recommended plan, active card, modal).
- Keep 3D lift subtle (rotateX about 2deg) if used.
- Define elevation as a small token scale (e.g. levels 0-4) and reuse it.

## Don't
- Don't use one identical flat drop shadow for every surface.
- Don't treat shadows as decoration; they tell the user what is above what.
- Don't elevate everything equally; equal elevation removes the hierarchy.

## Scene by scene
- 0:00 Title "Shadow Layers": two pricing cards, Basic $9/mo (features partly struck/muted, "Get Started") labelled "Flat", and Pro $29/mo (all features checked, accent "Upgrade Now") labelled "Floats", with a faint accent glow around it.
- 0:04 Title "3 Layers of Depth: add them one by one". A "Premium Card" (text "Shadows aren't decoration. They communicate hierarchy and depth.", stats "Depth 3 layers", "Impact +40%") appears flat.
- 0:05 Chip "Contact" with `0 1px 3px rgba(0,0,0,0.4)`, "Tight shadow anchors it".
- 0:07 Chip "Glow" with `0 0 60px` accent at 0.15, "Colored glow adds brand"; glow appears behind the card.
- 0:09 Chip "Elevation" with `perspective(1000px) rotateX(2deg) translateZ(20px)`, "3D lift creates depth"; card lifts and moves.
- 0:11 "Combined CSS" panel: three box-shadows (contact, `0 8px 24px rgba(0,0,0,0.3)`, accent glow) plus the transform.
- 0:16 Title "Tint Your Glow": "Creative App" dashboard card with accent glow and label "box-shadow: accent at 0.35".
- 0:18 "Fintech" dashboard card (balance chart) with its own accent glow, same 0.35 alpha.
- 0:19 "Health App" card (steps ring) with its own accent glow; all three held until 0:27.
- 0:29 End card "@designmotionhq, Follow + Save for more" with a glowing follow button.

## Voice-over summary
- The same card can sit flat or float; three layers make the difference.
- A tight contact shadow at the base, a soft elevation glow behind it, and a subtle perspective shift that makes the brain see real depth.
- To make it feel premium, tint the glow with the brand colour (the narrator's examples: a creative app in its accent, a fintech dashboard in its accent).
- The shadow then becomes part of the design rather than an afterthought.

## Notes for the skill
- Token example (colour-agnostic): `--shadow-contact: 0 1px 3px rgb(0 0 0 / .4); --shadow-mid: 0 8px 24px rgb(0 0 0 / .3); --shadow-glow: 0 0 60px color-mix(in srgb, var(--accent) 15%, transparent);` combine as `box-shadow: var(--shadow-contact), var(--shadow-mid), var(--shadow-glow);`. Derive the glow from the theme accent token, never hard-code a hue.
- Dark vs light themes: black shadows are almost invisible on dark backgrounds, which is why the glow carries the effect in this dark-themed reel. On dark UIs also signal elevation with a slightly lighter surface colour for higher layers (Material's approach). On light backgrounds keep coloured glows very faint or they look like a rendering error.
- 3D lift: `translateZ` inside a perspective scales the element slightly and can blur text on some browsers; keep the tilt tiny, prefer applying it on hover/active only, and wrap motion in `@media (prefers-reduced-motion: no-preference)`.
- Performance: animating `box-shadow` repaints every frame; to animate elevation, put the larger shadow on a pseudo-element and animate its `opacity` instead.
- Elevation is not an accessibility signal on its own: elements whose meaning depends on being "on top" (selected plan, modal) also need text/ARIA cues (e.g. a "Recommended" label, `aria-modal`). Card borders/edges should still meet 3:1 non-text contrast if they are the only boundary of an interactive control (WCAG 1.4.11).
- "Impact +40%" on the demo card is decorative filler, not a measured result; do not cite it.
