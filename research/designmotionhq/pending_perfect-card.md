---
id: unknown
reel_url: unknown
pattern_page: https://designmotionhq.com/patterns/perfect-card
date: unknown
duration_s: 59
type: ui
category: visual
topic: card polish (padding, type hierarchy, layered shadow + hairline border, hover lift)
sources: frames, voice-over, pattern page
---

# The premium card: four CSS changes

**Caption:** not captured yet
**Hook:** One card looks free, the other looks like it costs $1,000; the difference is four CSS changes.

## Main rule
A card reads as premium when it has generous inner padding and consistent gaps, a clear title/body hierarchy (heavier title, smaller and dimmer description), depth from two stacked shadows plus a hairline border, and, if it is interactive, a hover state that lifts it and strengthens shadow and border.

## Numbers and values
The video's voice-over, its on-screen code labels and the pattern page give different numbers. All are listed; see the notes for which to use.

| Value | Applies to | Where shown |
|---|---|---|
| padding 24px all sides, 16px between elements | card inner padding and vertical rhythm | 0:11-0:15 voice |
| padding: 40px | card inner padding | 0:10-0:16 on-screen code label |
| 12px → 40px padding, border-radius 24px | before → after padding; card radius | pattern page only |
| title semibold 18px | card title | 0:19-0:21 voice |
| font-weight: 600 | card title | 0:18-0:30 on-screen label |
| title 600 weight, ~38px | card title | pattern page only (likely the large demo render scale) |
| description regular 14px at 60% opacity | card description | 0:22-0:27 voice |
| opacity: 0.55 | card description | 0:18-0:30 on-screen label; page also says 55% |
| box-shadow: 0 2px 8px | tight shadow for crisp edge | 0:34-0:40 on-screen label (property name partly hidden) + voice "one tight shadow" |
| box-shadow: 0 20px 40px | large soft shadow for depth | 0:36-0:40 on-screen label + voice "one large soft shadow" |
| border: 1px solid, 10% white | hairline border | voice "one pixel border at 10% white"; on-screen "border: 1px solid" |
| border ~12% opacity | hairline border | pattern page |
| translateY(-4px), expand shadow spread, subtle primary-colour border glow | hover state | 0:43-0:49 voice |
| lift ~8px, scale 1.02, deeper shadow | hover state | pattern page only |
| 4 changes | padding, typography, shadows, hover | 0:03 on-screen "4 CSS changes" |

Shadow colours/opacities are not shown on screen.

## Before / after
1. **Padding (0:07-0:16).** Before (BASIC): the image runs almost to the card edge, text sits tight against the border, corners are nearly square. After: generous padding all round and even gaps between image, tag, title, description and meta. Why it works: white space separates the card's content from its edge and from neighbouring cards, so the boundary reads as intentional; cramped content looks like an unstyled default.
2. **Typography (0:17-0:30).** Before: title and description have the same weight and full brightness, and the description is even larger than the title, so nothing leads. After: title at weight 600 and larger; description smaller, regular weight, reduced opacity (0.55 on screen, "60%" in the voice). Why: contrast in size, weight and brightness gives one obvious entry point; the eye reads title first, then scans the body.
3. **Shadows and border (0:31-0:41).** Before: the card is a flat rectangle barely separated from the dark page. After: a tight small shadow (0 2px 8px) defines the edge, a large soft shadow (0 20px 40px) adds ambient elevation, and a 1px low-opacity light border outlines the card. Why: real objects cast a sharp contact shadow and a diffuse ambient one; combining both reads as believable depth. On dark backgrounds shadows are weak, so the hairline border carries the edge definition.
4. **Hover (0:41-0:51).** The cursor enters the card: it moves up, the shadow grows and the border picks up a faint accent glow; on leave it settles back. Why: the lift signals the whole card is clickable (affordance) and confirms the pointer is on it.

## Do
- Give cards generous, uniform inner padding (e.g. 24px) and a fixed gap between elements (e.g. 16px).
- Make the title clearly dominant: weight 600 and a larger size than the body (e.g. 18px vs 14px).
- Dim secondary text with opacity or a muted text token (about 0.55-0.6), not just a smaller size.
- Stack two shadows (tight + large soft) and add a 1px border at about 10-12% opacity of the text colour on dark surfaces.
- On interactive cards, lift on hover (translateY about -4px to -8px), deepen the shadow, and add a subtle accent border.

## Don't
- Don't push content to the card edge with tiny padding and near-zero radius.
- Don't give title and description the same weight, size and full opacity.
- Don't rely on a single hard shadow, or on shadows alone on a dark background.
- Don't add a hover lift to a card that is not clickable; it promises an action that does not exist.

## Scene by scene
- 0:00 Two versions of the same "Dashboard Redesign" card (tag UI Design, description, author Alex Chen, "2 days ago"): BASIC vs PREMIUM, with "vs".
- 0:02 Caption "The difference? 4 CSS changes."
- 0:07 "01 PADDING": the basic card is centred; padding grows, image shrinks inside the card, label "padding: 40px".
- 0:17 "02 TYPOGRAPHY": title grows and gets bolder, description shrinks and dims; labels "font-weight: 600" and "opacity: 0.55".
- 0:31 "03 SHADOWS": the card gains depth; labels "box-shadow: 0 2px 8px", "box-shadow: 0 20px 40px", "border: 1px solid".
- 0:41 "04 HOVER STATE": the card briefly dims and returns; cursor enters, card lifts with a stronger shadow and a faint accent border; cursor stays, then the card settles.
- 0:52 "Same content. Four changes. That's it." over the finished card; then a "Follow @designmotionhq" button.

## Voice-over summary
- Same card, one cheap and one premium; four CSS changes make the difference.
- Padding: developers cram content edge to edge; use 24px on all sides and 16px between elements.
- Typography: title semibold 18px, description regular 14px at 60% opacity; "This contrast tells the eye where to look first."
- Shadows: one tight shadow for crisp edges, one large soft shadow for depth, plus a 1px border at 10% white so the card floats.
- Hover: translate Y -4px, expand the shadow spread, add a subtle primary-colour border glow.

## Notes for the skill
- Which numbers to use: the voice-over values (24px padding, 16px gap, 18px / 14px, -4px lift) fit real product UI at 1x. The on-screen 40px padding and the page's ~38px title match the enlarged demo render and are too large for a typical card. The opacity values agree closely (0.55-0.6).
- Example CSS: `padding: 24px; display: grid; gap: 16px; border-radius: 16px; border: 1px solid color-mix(in srgb, var(--text) 10%, transparent); box-shadow: 0 2px 8px var(--shadow-tight), 0 20px 40px var(--shadow-soft);` hover: `transform: translateY(-4px); box-shadow: 0 4px 12px ..., 0 28px 56px ...; border-color: color-mix(in srgb, var(--accent) 40%, transparent);` with `transition: transform 200ms ease-out, box-shadow 200ms ease-out`. The radius (16px here) and the 200 ms transition are not given in the video; the page pairs its 40px padding with a 24px radius, and the reel never states a hover duration.
- Contrast: text at 55-60% opacity must still pass 4.5:1 against the card surface. On a very dark surface 0.6 white passes (about 7:1), but on lighter surfaces or for small text it may fail; prefer a muted text token checked for contrast over raw opacity.
- The 1px hairline border is decorative here; if it is the only thing showing a card's boundary for an interactive card, WCAG 1.4.11 (3:1 non-text contrast) is not strictly required for card edges, but focus indicators are: add a visible `:focus-visible` ring that mirrors the hover emphasis, since keyboard users never see hover.
- Make the whole card a single link/button target (one `<a>` with a stretched pseudo-element) rather than nesting several interactive elements.
- Hover lift should be disabled or reduced under `prefers-reduced-motion` (keep the shadow/border change) and should not be the only affordance on touch devices, which have no hover (`@media (hover: hover)` to scope it).
- Animate `transform` and `box-shadow` (or a pseudo-element's opacity holding the larger shadow) rather than `top`/`margin` to avoid layout work.
