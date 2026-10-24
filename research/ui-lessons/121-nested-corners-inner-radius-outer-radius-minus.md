---
lesson: 121
kind: carousel
type: ui
category: visual
topic: nested (concentric) border radius
sources: video slide 1 (frame sheet and final frame), image slides 2-8
---

# Nested corners: inner radius = outer radius minus padding (and border)

**Hook (slide 1):** A magnified card corner where the gap between the outer and inner curve is 8 px on the straight sides but 11.3 px at the corner.

## Slide by slide
The carousel has 8 slides styled as numbered technical drawing sheets (Sheet 01 / 08 to 08 / 08): 1 short video and 7 images. Four rules, each labelled Rule 0N / 04.
- **Slide 1 (video, 6 s, Fig. 01 card corner, scale 20:1).** Headline: this corner is why your card looks AI-made. Subtitle in the bad state: 8 px on the sides, 11.3 px in the corner. The top-left corner of a card: outer curve solid, inner curve dashed in the danger colour, a vertical dimension of 8 on the straight edge, a diagonal measure of 11.3 across the corner, two separate arc centres C1 (outer) and C2 (inner). The animation then shows the fixed state. See Video slide.
- **Slide 2 (Rule 01 / 04: nested corners share one centre).** Text: inner radius = outer radius minus padding; with the same centre the gap stays 8 all the way round. Drawing: outer arc R 24, padding p 8, inner arc r 16 in the accent colour, both arcs drawn from one centre C.
- **Slide 3 (Rule 01 in CSS, labelled copy / paste).** Headline: one line of CSS keeps it true. Code, with `--r` and `--p` marked as set once and the result annotated as 16 px that follows any change:
  ```css
  .card {
    --r: 24px;
    --p: 8px;
    border-radius: var(--r);
    padding: var(--p);
  }
  .card > * {
    border-radius: calc(var(--r) - var(--p));
  }
  ```
- **Slide 4 (Rule 02 / 04: a border is part of the gap).** Text: subtract the border too; a 2 px border inside a 24 px card leaves 14 for the child, not 16. Drawing: hatched border band b 2, then p 8, inner arc labelled r 24 - 2 - 8 = 14, one centre C.
- **Slide 5 (Rule 03 / 04: image on the edge gets the same radius as the card).** Text: no padding means nothing to subtract; round only the corners that touch, minus the border if there is one. Code line:
  ```css
  img { border-radius: 24px 24px 0 0; }
  ```
  Drawing: card corner R 24 with a flush image; a correct image arc labelled img r 24 = card coincides with the card curve; a danger-coloured dashed arc labelled img r 12: sticks out, with a hatched sliver of image poking outside the card curve.
- **Slide 6 (Rule 04 / 04: controls inside controls follow it too, scale 15:1).** Text: a segmented control's thumb sits 4 px inside a 12 px track; give it 8, not 12. Drawing: a Week / Month segmented control, track R 12, inset 4; the accent thumb outline labelled thumb 12 - 4 = 8 and a danger dashed outline labelled thumb 12: the corners swell, with the two arc centres shown offset.
- **Slide 7 (summary, save this sheet).** Four formulas:
  - 01 nested corners share one centre: `r = R - p`
  - 02 borders count: `r = R - b - p`
  - 03 image on the edge: `r = R`, touching corners only
  - 04 controls inside controls: `thumb = track - inset`

## Main rule
Nested rounded shapes must be concentric, so the band between them has the same width everywhere: inner radius = outer radius - border - padding (`r = R - b - p`). A flush element with no padding takes the outer radius (minus the border) on the corners that touch the edge only. The same subtraction applies to any control inset in another control (`thumb = track - inset`).

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 8 px | padding, gap on the straight sides | slides 1, 2 |
| 11.3 px | gap across the corner when inner radius = outer radius | slide 1 |
| 10.8, 8.6, 10.0 | intermediate gap readouts while the inner arc animates | slide 1 at 1.5 s, 2.0 s, 5.0 s |
| 8.0 px | gap at the corner after the fix (one centre) | slide 1, 2.5-4.5 s |
| R 24, p 8, r 16 | worked example of rule 1 | slides 2, 3 |
| `--r: 24px`, `--p: 8px`, `calc(var(--r) - var(--p))` = 16 px | CSS for rule 1 | slide 3 |
| R 24, b 2, p 8, r 14 | worked example of rule 2 (24 - 2 - 8 = 14, not 16) | slide 4 |
| `24px 24px 0 0` | flush top image: card radius on the two touching corners, square elsewhere | slide 5 |
| img r 12 | wrong flush image radius; the image corner sticks out past the card curve | slide 5 |
| track R 12, inset 4, thumb 8 | worked example of rule 4 (12 - 4 = 8) | slide 6 |
| thumb 12 | wrong thumb radius; corners swell | slide 6 |
| 20:1, 15:1 | drawing scales | slides 1-5, slide 6 |
| 6 s | video slide length | slide 1 |

The 11.3 figure is exact geometry: with equal radii the arc centres are offset by p on both axes, so the corner gap is p x sqrt(2) = 8 x 1.414 = 11.3, independent of the radius (as long as the radius is at least p).

## Before / after
- **Equal radii vs one centre (slides 1, 2).** Bad: inner radius equals outer radius; centres C1 and C2 sit 8 px apart on each axis, so the band is 8 px on the sides and 11.3 px across the corner. Good: inner radius 16 inside a 24 card with 8 padding; both arcs share centre C and the band is 8 px everywhere. Why: the eye reads a nested frame by the evenness of the band between two parallel lines. A band that fattens at each corner breaks that parallelism and reads as careless, which is the generated look the post names.
- **Ignoring the border (slide 4).** Bad: 24 - 8 = 16 for the child of a card with a 2 px border. Good: 24 - 2 - 8 = 14. Why: the inner edge of the border is already an offset curve with radius R - b; padding is measured from there, so both offsets must be subtracted to keep one centre.
- **Flush image with a smaller radius (slide 5).** Bad: image radius 12 in a 24 card corner; the image's corner lies outside the card curve and pokes out as a visible sliver (when the card does not clip). Good: image radius 24 = card, on the touching corners only (`24px 24px 0 0` for a top image). Why: with zero padding the image edge coincides with the card edge, so concentric means identical radius; corners not on the card edge face content and stay square.
- **Thumb with the track radius (slide 6).** Bad: thumb 12 inside a track 12 with 4 inset; the thumb's corners swell away from the track. Good: thumb 8. Why: identical geometry to cards; the inset plays the role of padding.

## Do
- Derive inner radii from tokens: set radius and padding once on the container and compute children with `calc()`.
- Subtract every offset between the two edges: border width, padding, inset (`r = R - b - p`), and apply it again at each nesting level.
- Clamp at zero when the offsets exceed the outer radius: `max(0px, calc(var(--r) - var(--b) - var(--p)))`.
- For flush media give the card radius (minus border) only to corners that touch the card edge, or clip with the parent.
- Apply the same subtraction to segmented control thumbs, buttons inside inputs, chips inside pills, tabs inside tab bars.

## Don't
- Don't reuse the outer radius token on inner elements.
- Don't forget the border in the subtraction.
- Don't give a flush image a smaller radius than the card; its corner will stick out unless clipped.
- Don't round an image's corners that sit against content inside the card.

## Video slide
Slide 1, 6 s, frames sampled at 2 per second; it starts and ends in the bad state, so it loops cleanly.
- 0.0-1.0 s: subtitle 8 px on the sides, 11.3 px in the corner (number in the danger colour). Inner arc dashed, danger colour, readout 11.3, centres C1 and C2 apart.
- 1.5 s: inner arc starts tightening, readout 10.8, subtitle fading.
- 2.0 s: readout 8.6, arc turns accent-coloured but still dashed, C2 sliding into C1; subtitle switches to one centre, 8 px all the way round.
- 2.5-4.5 s: inner arc solid in the accent colour, readout 8.0, single centre C1.
- 5.0 s: arc relaxes back, readout 10.0, dashed and neutral, C2 reappears.
- 5.5 s and final frame: back to 11.3, danger dashed arc, C1 and C2.
- The straight-side dimension stays 8 throughout; only the arc, its colour and style, the centres and the readout change. The fixed state is shown roughly twice as long as each transition.

## Notes for the skill
- The slide 3 snippet `.card > *` gives the inner radius to every direct child, including ones that never touch a corner, and it has no clamp or border term. Better: apply it only to children that sit in corners (or to the single inner surface), and write `border-radius: max(0px, calc(var(--r) - var(--b, 0px) - var(--p)))`.
- `r = R - p` holds only when padding is equal on both axes at that corner. With different horizontal and vertical padding, concentric arcs need elliptical radii: `border-radius: calc(R - p-x) / calc(R - p-y)`.
- When the result becomes tiny (1-3 px), consider a square inner corner or a larger outer radius; very small radii read as rendering errors. Some designers add a pixel back for optical balance at small sizes; treat that as taste, the concentric rule is the baseline.
- Clipping instead of rule 3: `overflow: clip` (or `hidden`) on a rounded parent clips flush children to the parent's curve. It also clips descendants' focus outlines, shadows and popovers, so avoid it on containers holding focusable controls whose rings extend outside.
- Focus rings: `outline` follows `border-radius` in current engines (check current support). With `outline-offset`, the ring is a further concentric offset, so its radius should be element radius + offset; a hand-drawn ring (box-shadow or pseudo-element) must compute that explicitly.
- The 4.5:1 and 3:1 contrast rules are unaffected; this is a purely visual rule with no accessibility conflict. The "looks AI-made" framing is the author's opinion; the testable rule is the formula.
