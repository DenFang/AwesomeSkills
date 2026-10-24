---
lesson: 124
kind: carousel
type: ui
category: visual
topic: consistent shadow light source and two-layer elevation shadows
sources: video slide 1 (frame sheet and final frame), image slides 2-8
---

# Shadows: one light source, two layers, steady opacity

**Hook (slide 1):** Three cards whose shadows each point away from a different sun, so the shadows disagree about where the light is.

## Slide by slide
The carousel has 8 slides styled as technical drawing sheets (Sheet 01 / 08 to 08 / 08): 1 short video and 7 images. Four rules, each labelled Rule 0N / 04.
- **Slide 1 (video, 6 s, Fig. 01 light sources, top view).** Headline: your shadows disagree on where the light is. Bad state subtitle: three cards, three light directions. Three cards, each tied by a dotted line to its own sun (top-left, top-right, bottom-right), with hatched shadow outlines offset away from each sun in a different direction. Good state subtitle: one sun, every shadow falls the same way. See Video slide.
- **Slide 2 (Rule 01 / 04: one light source, one direction).** Text: every shadow falls the same way, x 0 and y down; focus rings and inset shadows are exempt. Drawing: one sun at top centre, dotted arrows straight down to three cards at different positions, each with an identical shadow band directly below, annotated x 0, y +4.
- **Slide 3 (Rule 02 / 04: higher means farther and softer, side view).** Text: offset and blur grow together with height; keep the opacity steady so modals still lift off the page. Drawing: light from the top of the screen at 24°, three slabs at increasing heights over the screen surface, their shadows landing farther down the screen with a wider soft penumbra:
  - level 1: y 2, blur 6
  - level 2: y 6, blur 16
  - level 3: y 16, blur 40
- **Slide 4 (Rule 03 / 04: stack two shadows, not one, scale 3:1).** Text: a tight, darker contact shadow under the edge plus a larger, softer, lighter one for height. Drawing: a card with a thin contact outline and a wider ambient outline. Code:
  ```css
  box-shadow:
    0 1px 2px rgb(0 0 0 / .12),      /* contact */
    0 6px 16px -4px rgb(0 0 0 / .08); /* ambient */
  ```
- **Slide 5 (Rule 04 / 04: negative spread tucks the shadow under the element, scale 4:1).** Text: a soft shadow also grows sideways; a negative spread shrinks that side halo, so the shadow reads as below the card, not around it. Dashed outlines mark the approximate visible extent (spread + blur).
  - Bad: `0 12px 24px`, halo on every side, about 24 px visible past the side edge.
  - Good: `0 12px 24px -12px`, mostly below, about 12 px past the side edge and none above.
  - Code line: `box-shadow: 0 12px 24px -12px rgb(0 0 0 / .08);`
- **Slide 6 (Copy this: three levels, ready to paste, tokens).**
  ```css
  :root {
    --shadow-1:
      0 1px 2px rgb(0 0 0 / .12),
      0 2px 6px -2px rgb(0 0 0 / .08);
    --shadow-2:
      0 1px 2px rgb(0 0 0 / .12),
      0 6px 16px -4px rgb(0 0 0 / .08);
    --shadow-3:
      0 1px 2px rgb(0 0 0 / .12),
      0 16px 40px -8px rgb(0 0 0 / .08);
  }
  ```
  Footnote: the contact layer is the same on every level; on the soft layer offset, blur and spread grow while opacity stays.
- **Slide 7 (summary, save this).** 01 one light, one direction: x 0, y down, everywhere. 02 higher: farther and softer, offset and blur grow together. 03 two layers per shadow: tight contact + soft ambient. 04 negative spread on soft layers: trims the halo on the sides.

## Main rule
Every elevation shadow in the interface comes from one light source above the screen: x offset 0, y offset positive. Height is expressed by growing the soft layer's y offset, blur and negative spread together while its opacity stays fixed. Each elevation token is two layers: an identical tight, darker contact layer (`0 1px 2px`, alpha .12) and a soft, lighter ambient layer (alpha .08) whose negative spread keeps it from haloing past the sides. Focus rings and inset shadows are outside this rule.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| x 0, y down | direction of every elevation shadow | slides 2, 7 |
| y +4 | example offset in the direction diagram | slide 2 |
| 24° | light angle from the top of the screen in the side-view diagram | slide 3 |
| y 2, blur 6 | level 1 | slide 3 |
| y 6, blur 16 | level 2 | slide 3 |
| y 16, blur 40 | level 3 | slide 3 |
| `0 1px 2px`, alpha .12 | contact layer, identical on every level | slides 4, 6 |
| `0 2px 6px -2px`, alpha .08 | soft layer of `--shadow-1` | slide 6 |
| `0 6px 16px -4px`, alpha .08 | soft layer of `--shadow-2` (also the slide 4 example) | slides 4, 6 |
| `0 16px 40px -8px`, alpha .08 | soft layer of `--shadow-3` | slide 6 |
| `0 12px 24px` vs `0 12px 24px -12px` | halo on every side vs mostly below; side extent about 24 vs 12 px | slide 5 |
| 3 levels | elevation token count | slides 3, 6 |
| 6 s | video slide length | slide 1 |

Derived from slide 6 (calculation, not on the slides): blur is about 2.5 to 3 times the y offset at every level; negative spread is a third, a quarter and a fifth of the blur (2/6, 4/16, 8/40), i.e. it equals y at level 1 and half of y at level 3. Visible extent past the top edge = blur - |spread| - y: 2, 6 and 16 px for levels 1 to 3, so the top stays light while the bottom carries the shadow.

## Before / after
- **Many suns vs one sun (slides 1, 2).** Bad: each card's shadow is offset in a different direction, as if lit by its own sun. Good: one sun above, every shadow straight down by the same rule. Why: the visual system reads shadow direction as the cue for where the light is and how objects sit in space; conflicting directions make the screen look composited from unrelated parts, a single direction makes all cards read as objects in one space.
- **Same shadow at every height vs farther and softer (slide 3).** Bad (implied): one shadow for card, menu and modal. Good: y and blur grow together (2/6, 6/16, 16/40). Why: a higher object casts a shadow that lands farther from it and has a wider penumbra, so offset and softness are the cues for height. Opacity stays fixed because a larger blur already spreads the same alpha over more area and makes it look lighter; fading opacity as well would make a high modal's shadow vanish instead of lifting it off the page.
- **One shadow vs two layers (slide 4).** Bad: a single shadow, which is either crisp (sticker-like, no lift) or soft (floating, no grounding). Good: a tight, darker contact layer that anchors the edge plus a larger, lighter ambient layer that gives height. Why: real objects show both a dark occlusion line where they meet the surface and a soft diffuse shadow; each layer supplies one of these cues.
- **No spread vs negative spread (slide 5).** Bad: `0 12px 24px` extends about 24 px past every side and 12 px above, so the element looks wrapped in a glow. Good: `0 12px 24px -12px` pulls the shadow in by 12 px on all sides, leaving about 12 px on the sides, nothing above and the bulk below. Why: a shadow that is mostly below the element is consistent with light from above; a symmetric halo has no direction and reads as a glow or a border.

## Do
- Light everything from above: x offset 0, y offset positive, for every elevation shadow.
- Build each elevation token from two layers: a shared contact layer (`0 1px 2px`, alpha .12) and a soft layer with growing y, blur and negative spread at fixed alpha (.08).
- Keep elevation as tokens (`--shadow-1` to `--shadow-3`) so components never hand-pick values.
- Map levels to roles: low for resting cards, middle for raised or hovered elements and menus, high for modals and dialogs.
- Give soft layers a negative spread so the shadow sits under the element.

## Don't
- Don't mix shadow directions or non-zero x offsets on one screen.
- Don't use the same single shadow for every elevation.
- Don't lower the opacity of the soft layer as it grows; and don't fake height by darkening only.
- Don't let the soft layer halo past the element's sides.
- Don't apply the direction rule to focus rings or inset shadows; the post exempts them.

## Video slide
Slide 1, 6 s, frames sampled at 2 per second; it starts and ends in the bad state, so it loops cleanly.
- 0.0-1.5 s: bad state. Subtitle three cards, three light directions (second phrase in the danger colour). Suns top-left, top-right, bottom-right in the danger colour, each linked by a dotted line to one card; the hatched shadows are offset away from their suns (down-right, down-left, up-left).
- 2.0 s: the three suns slide toward the top centre and bunch together; shadows and suns switch to the accent colour; the subtitle changes.
- 2.5-4.5 s: good state. Subtitle one sun, every shadow falls the same way. One sun at top centre, vertical dotted lines to each card, every card with the same shadow band directly beneath it.
- 5.0 s: the sun splits back into separate suns moving to the corners, shadows turn neutral, subtitle fades.
- 5.5 s and final frame: bad state again.
- The cards never move; only suns, connector lines, shadow offsets and colours change, so the shadow is the only variable.

## Notes for the skill
- Exact values from slides 4 to 6 are usable as defaults, but they are tuned for light surfaces. Black at alpha .08 is barely visible on dark surfaces (the slides themselves are dark): in dark themes express elevation mainly with a lighter surface tone or a subtle border, and keep the shadow as a secondary cue.
- Small inconsistency: slide 2 annotates y +4, which matches none of the token levels (2, 6, 16). Treat it as an illustration of direction only.
- The 24° light angle on slide 3 is a diagram detail; the code uses x 0, so the angle only shows up as y offset growing with height.
- Slide 5 matches the CSS Backgrounds spec: blur radius B approximates a Gaussian with standard deviation B/2, so the visible shadow extends about B past the spread edge; a negative spread shrinks the shadow box before blurring.
- Prefer a single shadow colour token with alpha (for example a dark tint of the surface hue) over hardcoded black, so shadows stay coherent across themes; keep the .12 / .08 alpha relationship.
- Accessibility: shadows on cards are decorative, but if a shadow is the only thing marking a control's boundary (button, input), that boundary needs 3:1 contrast against adjacent colours (WCAG 1.4.11); add a border or fill. In forced-colors mode `box-shadow` is removed, so a boundary must not depend on it.
- Animating elevation (hover lift): transition between two tokens, or fade the opacity of a pseudo-element carrying the higher shadow, which avoids repainting the blur each frame; respect `prefers-reduced-motion`.
- The claim that uniform shadows are a tell of generated UI is the author's opinion; the testable rules are the four on slide 7.
