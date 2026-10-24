---
lesson: 128
kind: video
duration_s: 50
type: ui
category: motion
topic: product card hover state (lift, edge glow, staggered actions, image scale)
sources: frames, voice-over, lesson notes
---

# Card hover anatomy

**Hook:** In a grid of identical product cards only one responds to hover convincingly; the other three feel dead. Four hover rules plus one trap make the difference.

## Main rule
On hover, move the card's content, not its footprint: lift the card about 8px with a growing shadow over 200 ms ease-out, add an edge highlight, fade in bottom-anchored actions with a 60 ms stagger, and scale only the image (about 1.05) inside an `overflow: hidden` frame. Never scale the whole card.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| `translateY(-8px)` | card lift on hover ("REST · 0px" vs "HOVER · -8px", measured from a baseline line) | 0:05-0:09 on-screen + voice |
| shadow `0 24px 40px` at 60% alpha | hover shadow: 0 x offset, 24px y offset, 40px blur, shadow colour at 60% opacity | 0:07-0:09 on-screen code strip |
| 200 ms ease-out | lift + shadow transition | 0:07 on-screen + voice; page says ~200ms |
| 100 ms | labelled "twitchy" (too fast) | 0:09-0:11 on-screen comparison |
| 400 ms | labelled "stuck" (too slow) | 0:09-0:11 on-screen comparison |
| `border-color · Math.sin(frame)` | border pulse: border colour oscillates on a sine wave | 0:13-0:18 on-screen caption |
| `conic-gradient · rotate(360deg)` | gradient sweep: a conic gradient rotating a full turn around the edge | 0:13-0:18 on-screen caption |
| 3 | hidden actions revealed (heart / favourite, cart, share) | 0:19-0:22 voice + on-screen |
| `stagger(60ms)` | delay between successive action buttons | 0:19-0:25 on-screen + voice; page says ~60ms |
| `scale(1.000)` to `scale(1.050)` | image scale inside a static container (readout animates between 1.000 and 1.050) | 0:32-0:39 on-screen + voice ("1.05") |
| `overflow: hidden` | image frame clipping the scaled image | 0:33-0:39 on-screen label |
| `container: static` | card container does not move during image scale | 0:32-0:39 on-screen label |

## Before / after
- **Timing (100 / 200 / 400 ms):** the same 8px lift at 100 ms reads as a twitch, at 400 ms it lags behind the cursor and feels stuck, at 200 ms ease-out it reads as a physical object rising. Mechanism: 200 ms is long enough for the eye to track the motion but short enough to feel like a direct response to the pointer; ease-out front-loads the movement so the response starts immediately.
- **Lift without vs with shadow:** the shadow grows together with the lift (larger y offset and blur), so the card appears to leave the surface. Mechanism: depth is read from shadow offset and softness; translate alone looks like a slide.
- **Flat card vs edge glow:** a static card looks the same as its neighbours; a pulsing border or a rotating conic-gradient edge marks the hovered card as the one that "owns" the cursor. Mechanism: a moving or brightened edge separates figure from ground and signals interactivity.
- **Actions, three anti-patterns vs correct:**
  - "On top of title": buttons overlap the product name, hiding the content the user is reading.
  - "All at once": buttons appear simultaneously, with no cascade rhythm, so they arrive as one block.
  - "Outside the card": buttons spill over the card boundary into the gap / neighbour.
  - Correct: heart, cart, share fade in one after another (60 ms apart) in a row anchored at the bottom of the image area, above the title, entirely inside the card. Mechanism: the stagger lets the eye register each new control in order; placing them in reserved space adds affordance without changing layout.
- **Image scale:** the image grows to 1.05 while the container and its clip stay fixed, so the product appears to press outward against the frame. Mechanism: motion is contained, the card's bounds and the grid stay stable.
- **Trap, wrong vs right grid (2x2):** "scale(card) · LAYOUT BREAKS": the hovered card grows and the neighbouring cards visibly shift / are crowded. "lift(content) · GEOMETRY HELD": the hovered card lifts with a highlighted edge and the grid stays aligned.

## Do
- Lift about 8px with `transform: translateY(-8px)` and grow the shadow in the same transition, 200 ms ease-out.
- Give the hovered card a distinct edge treatment (brighter border, pulse, or sweeping gradient) using the theme's accent colour.
- Reveal secondary actions with a 60 ms stagger, anchored to a bottom edge, fully inside the card.
- Scale only the media (about 1.05) inside a clipping frame (`overflow: hidden`) on a static container.
- Keep the card's outer box (width, height, position in the grid) identical in rest and hover states.

## Don't
- Don't scale the whole card.
- Don't place revealed buttons over the title or let them extend past the card edge.
- Don't reveal all actions at the same instant.
- Don't use 100 ms (twitchy) or 400 ms (stuck) for the lift.
- Don't animate the lift without the shadow; it reads as sliding, not rising.

## Scene by scene
- 0:00 Label "Card hover anatomy". 2x2 grid of product cards (image, "NEW" badge, name, rating, price, stock label). Cursor hovers top-left card: it lifts, its border highlights and small action icons appear. Overlay: "Same card. One feels alive." with small "three stay dead".
- 0:03 Section "01 · Lift / Rise with weight." A single card fades in above a "BASELINE" line, tag "REST · 0px".
- 0:06 Card rises, tag changes to "HOVER · -8px", a -8px measurement marker on the left; code strip: `translateY(-8px)`, shadow `0 24px 40px` at 60% alpha, `200ms ease-out`.
- 0:09 Three small cards side by side with chips "100ms · twitchy", "200ms · right", "400ms · stuck"; caption "Same lift. Different feel."
- 0:12 Section "02 · Glow / Claim the cursor." Two cards: "Border pulse" (`border-color · Math.sin(frame)`) and "Gradient sweep" (`conic-gradient · rotate(360deg)`), both animating their edges. Overlay at 0:17: "The card claims the cursor."
- 0:19 Section "03 · Actions / Cascade. 60ms apart." Card marked "Correct": cursor on the image, heart, cart, share appear one by one in a row at the bottom of the image area; caption `heart · cart · share · stagger(60ms)`.
- 0:25 "Anti-patterns" set: three cards with error badges labelled "On top of title / overlaps the name", "All at once / no cascade rhythm", "Outside the card / breaks the boundary". Overlay at 0:29: "Reveal means new affordance, not new layout."
- 0:32 Section "04 · Image scale / Push against the glass." Card with labels "container: static", "image: scale(1.0xx)" (readout cycles 1.000 to 1.050), dashed outline around the image frame, label "overflow: hidden". Overlay at 0:38: "The product pushes against the glass."
- 0:40 Section "05 · Trap / Keep the geometry." Two 2x2 grids: "Wrong" (`scale(card) · LAYOUT BREAKS`, neighbours shift) and "Right" (`lift(content) · GEOMETRY HELD`). Overlay: "Never scale the whole card." then "Lift the content. Keep the geometry."
- 0:46 Outro: three cards, "Follow for more UI patterns", account handle, "Save for your next card grid."

## Voice-over summary
- Opens with the contrast: one identical card feels alive, three feel dead.
- Lift: the card rises 8px and the shadow stretches with it, 200 ms ease-out; faster is twitchy, slower is stuck.
- Glow: a pulsing border or sweeping gradient mask makes the card stop looking flat; it "claims the cursor".
- Actions: three hidden buttons (heart, cart, share) fade in 60 ms apart, stacked at the bottom, never over the title; "Reveal means new affordance, not new layout."
- Image: scale to 1.05 inside an overflow-hidden frame while the container stays still.
- Trap: never scale the whole card, neighbours shift and the layout breaks; lift the content, keep the geometry.

## Notes for the skill
- Implementation: `.card { transition: transform 200ms ease-out, box-shadow 200ms ease-out; }` `.card:hover { transform: translateY(-8px); }`. Animating `box-shadow` repaints every frame; a cheaper equivalent is a pseudo-element carrying the large shadow with `opacity` transitioned from 0 to 1.
- Image: `.media { overflow: hidden; } .media img { transition: transform 200ms ease-out; } .card:hover .media img { transform: scale(1.05); }`.
- Stagger: `transition-delay: calc(var(--i) * 60ms)` on each action; consider removing the delay on hover-out so actions leave together and faster.
- Precision on the trap: a CSS `transform: scale()` on the card does not reflow neighbours (transforms do not affect layout); it overlaps the gap and neighbouring cards, which reads as broken. Neighbours actually shift only if hover changes width, height, padding, margin or border width. Both are wrong; the rule is "hover must not change the layout box and should not paint outside it".
- Gate hover effects with `@media (hover: hover) and (pointer: fine)`. On touch there is no hover, so the heart / cart / share actions must be visible by default or reachable another way; never make hover the only path to an action.
- Keyboard: apply the same state on `:focus-visible` / `:focus-within` so revealed actions are reachable and visible when tabbing; hidden actions must not be focusable while invisible, or must become visible on focus.
- Reduced motion: under `prefers-reduced-motion: reduce` drop the translate and image scale, keep the shadow / border change as the state signal.
- An infinitely pulsing border or perpetually rotating gradient is auto-playing motion; limit it to the hover duration. WCAG 2.2.2 requires a pause mechanism for motion lasting more than 5 s that starts automatically.
- The glow / border must use the theme's accent or focus colour; ensure the hovered edge is distinguishable (non-text contrast at least 3:1 if it is the only hover indicator).
- Actions icon-only: give each an accessible name (`aria-label="Add to favourites"` etc.) and a touch target of at least 24x24 CSS px (WCAG 2.5.8), 44x44 recommended on touch.
