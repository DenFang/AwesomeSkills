---
id: unknown
reel_url: unknown
pattern_page: https://designmotionhq.com/patterns/icon-design-rules
date: unknown
duration_s: 55
type: ui
category: visual
topic: icon set consistency (optical sizing, pixel grid, stroke weight, bounding box, fill vs outline)
sources: frames, voice-over, pattern page
---

# Icon design rules: five ways an icon set stops looking cheap

**Caption:** none (this video is published on the pattern page only; no matching reel on the Instagram profile as of 2026-10-24)
**Hook:** Icons look cheap when they are sized by math and mixed by accident; five system rules give the same icons a different level of polish.

## Main rule
Treat icons as one system: size round and pointed shapes optically larger than squares, draw on a 24px grid (16px for dense UI) with whole-pixel coordinates, keep one stroke weight (2px) and one fixed container size for every icon, and use outline as the default style with fill reserved for the active/selected state.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 5 rules | optical sizing, grid alignment, stroke consistency, bounding box, fill vs outline | 0:01-0:03 on-screen "5 icon rules" + voice |
| 5-8% larger | circles vs squares to look the same size | 0:04-0:10 on-screen rule chip + voice + page |
| 64px / 64px / 64px | "Math" (bad) row: circle, square, triangle all at equal size | 0:03-0:10 on-screen |
| 70px / 64px / 72px | "Optical" (good) row: circle, square, triangle | 0:03-0:10 on-screen; subtitle "Math says 64. Eyes say 70." |
| 24px grid | default icon grid | 0:10-0:20 on-screen + voice + page |
| 16px grid | dense interfaces | 0:12-0:20 on-screen + voice + page |
| x = 12.5px (blur) vs x = 12px (crisp) | off-grid vs on-grid node position of a star icon | 0:11-0:20 on-screen |
| 2px | single stroke weight for the whole set | 0:20-0:29 on-screen + voice + page |
| 1px, 1.5px, 2px, 2.5px, 3px | mixed stroke weights in the bad row (heart, bell, search, mail, star) | 0:21-0:29 on-screen |
| "4 libraries" | what a set with mixed weights looks like | 0:23-0:29 on-screen |
| 16-30px (chaos) vs 28px (steady) | loose icon sizes vs one fixed bounding container | 0:30-0:39 on-screen |
| 5 icons: like, save, rate, home + active | fill vs outline demo; only the active one is filled | 0:40-0:48 on-screen |

Note on the optical-size numbers: 70 / 64 is about +9.4% and 72 / 64 is +12.5%, so the on-screen "good" example exceeds the 5-8% rule it illustrates. Treat 5-8% as the circle guideline and expect triangles/pointed shapes to need more.

## Before / after
1. **Optical sizing (0:02-0:10).** Bad ("DIY / Math"): circle, square and triangle all 64px; the circle and triangle look smaller and lighter. Good ("System / Optical"): circle 70px, square 64px, triangle 72px; all three read as the same size. Why: a circle or triangle covers less area of its bounding box than a square and its extremes are only points, so equal boxes produce unequal perceived mass. Compensate by overshooting the box.
2. **Grid alignment (0:10-0:20).** Bad ("Off-grid"): a star whose position is x = 12.5px, labelled "blur". Good ("24px grid"): same star at x = 12px with nodes on grid intersections, labelled "crisp". Why: half-pixel coordinates get anti-aliased across two device pixels, softening edges, especially at 1x density and small sizes.
3. **Stroke consistency (0:20-0:29).** Bad ("Mixed"): heart 1px, bell 1.5px, search 2px, mail 2.5px, star 3px. Good ("2px uniform"): all five at 2px. Why: stroke weight is the most visible stylistic parameter; mixed weights make a set look assembled from different libraries and break visual rhythm in a row.
4. **Bounding box (0:30-0:39).** Bad ("Loose"): toolbar icons rendered anywhere from 16 to 30px, uneven spacing ("chaos"). Good ("Bounded"): every icon sits in an identical 28px container ("steady"). Why: equal containers give equal hit areas and an even rhythm along toolbars and menus, regardless of the glyph's shape.
5. **Fill vs outline (0:40-0:48).** Bad ("Random"): like and rate filled, save and home outlined, with no meaning behind the difference. Good ("Strategy"): all outlined, and a separate "Active" heart shown filled in the accent colour. Why: when style changes carry meaning (outline = available, fill = selected/active), the user can read state from the icon; random mixing looks accidental and destroys that signal.

## Do
- Scale circular icons about 5-8% larger than square ones (pointed shapes like triangles often more) so they read equally large.
- Draw icons on a 24px grid (16px for dense UI) and snap every node and path to whole pixels.
- Use one stroke weight for the whole set (2px at 24px is the common default).
- Put every icon in the same fixed container/bounding box; let the glyph vary inside it.
- Use outline as the default and fill for active/selected state; apply that rule set-wide.
- Prefer an established library that enforces these constraints (the voice names Lucide and Phosphor).

## Don't
- Don't size icons by equal raw dimensions regardless of shape.
- Don't leave nodes at sub-pixel positions.
- Don't mix stroke weights or mix icons from several libraries.
- Don't let icons float at different sizes in a toolbar or menu.
- Don't mix filled and outlined icons without a rule behind it.

## Scene by scene
- 0:00 A "DIY" row (mismatched bell, mail, filled star, varied colours and weights) scrolls past a "System" row of clean uniform outline icons (heart, search, bell, mail, star).
- 0:02 Badge "5 icon rules"; caption "Five rules. Same icons. Different polish."
- 0:03 "01/05 Optical sizing / Math says 64. Eyes say 70.": DIY math row (64/64/64) vs System optical row (70/64/72); chips "Circles 5-8% larger than squares" and "Avoid: math equality makes round icons look small".
- 0:10 "02/05 Grid alignment / Snap to 24px, sub-pixel kills crispness": off-grid star at x = 12.5px (blur) vs 24px-grid star at x = 12px (crisp); chips "Snap to 24px grid (16 for dense UI)", "Avoid: sub-pixel drift kills crispness".
- 0:20 "03/05 Stroke consistency / 2px across the entire set": mixed row 1-3px vs uniform 2px row; chips "2px stroke across the entire set", "Avoid: mixed weights look like 4 libraries".
- 0:30 "04/05 Bounding box / Shape varies. Container never does.": loose toolbar (16-30px, chaos) vs bounded toolbar (28px, steady) with each icon in a square tile; chips "Same container, every icon", "Avoid: loose sizing makes toolbars unreadable".
- 0:40 "05/05 Fill vs outline / Pick one strategy. Commit to it.": random fill/outline row (like, save, rate, home) vs outline row plus a filled accent "Active" heart; chips "Pick fill or outline. Commit.", "Avoid: random mix has no visual rule".
- 0:49 Summary "5 rules, 1 system / Optical beats math. Grid beats eye." with chips Optical, Grid, Stroke, BBox, Fill; save/follow call to action.

## Voice-over summary
- Icons look cheap for fixable reasons; five rules fix them.
- A circle must be 5-8% larger than a square to look the same size; the eye wins over arithmetic.
- Use a 24px grid by default and 16px for dense UIs; sub-pixel positions destroy crispness, so snap every node.
- Keep a 2px weight across the set; mixing weights breaks harmony at once (Lucide and Phosphor enforce this by default).
- Every icon takes the same space so toolbars and menus keep a regular density; the shape varies, the container does not.
- Choose fill or outline and commit: outline for utility, fill for the active state; a random mix looks accidental. Closing line: optical beats math, grid beats eye, consistency beats novelty.

## Notes for the skill
- In code, render icons at their design size or integer multiples (16, 20, 24, 32) to keep strokes on the pixel grid; avoid CSS transforms or flex centring that put an SVG at a fractional position (e.g. odd container minus even icon divided by 2). `shape-rendering` tweaks are rarely needed if sizes are integer.
- Keep `stroke-width` constant across sizes when using `vector-effect: non-scaling-stroke` or a library's `absoluteStrokeWidth` option; otherwise a 24px 2px icon scaled to 16px becomes ~1.33px. Lucide's default stroke is 2 at 24px; Phosphor uses weights (regular, bold, fill...) rather than a numeric stroke, so "Phosphor enforces 2px" is loose.
- Bounding box: the fixed container is also the hit target. For tappable icon buttons the touch target should be at least 44x44 pt (iOS) / 48x48 dp (Android); WCAG 2.2 SC 2.5.8 asks for at least 24x24 CSS px. A 28px visual box may need extra padding to reach that.
- Fill-for-active: pair the fill change with `aria-pressed="true"` / `aria-current` and a text label or tooltip; fill alone is a visual-only state cue. Meaningful icons need 3:1 contrast against their background (SC 1.4.11), and icon-only buttons need an accessible name (`aria-label`); decorative icons get `aria-hidden="true"`.
- Optical overshoot: the on-screen example (+9.4% circle, +12.5% triangle) is larger than the stated 5-8%; adjust by eye at the actual rendering size rather than applying a fixed percentage. Established icon grids handle this with keyline shapes (circle, square, portrait and landscape rectangles of different sizes inside the same live area).
