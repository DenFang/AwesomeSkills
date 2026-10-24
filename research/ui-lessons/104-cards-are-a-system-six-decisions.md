---
lesson: 104
kind: video
duration_s: 80
type: ui
category: visual
topic: cards as a system (one entity, background-driven treatment, whole-surface click, no nesting, one media ratio, dark mode)
sources: frames, voice-over
---

# Cards are a system: six decisions

**Hook:** A card is border, shadow or flat, and the background decides which.

## Main rule
Use a card only for one entity with one title, one subject and one destination; make the whole surface the single click target; choose the card's edge treatment from the background it sits on (border on white, shadow on a tinted background, flat inside a panel); never nest cards (group inside a card with dividers and section labels); keep one media aspect ratio across a card grid (e.g. 16:9, cropped); in dark mode replace shadows with a faint border and a lighter surface tint.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 3 backgrounds · 3 treatments · 1 component | white → border, tinted → shadow, panel → flat | 0:00-0:04, 0:17-0:27 on-screen + voice |
| Title, Subject, Destination | the three things that make one entity (example: "Atlas redesign", "Northwind Labs · 72 %", "Project page") | 0:07-0:12 on-screen |
| "3 cards, 0 entities" → "3 sections" | settings page wrapped in three cards, fixed by turning them into labelled sections | 0:11-0:16 on-screen |
| 1 surface · 1 action | clickable card; "2 actions in 1 card" (Archive + Open) flagged | 0:28-0:37 on-screen + voice |
| 24 + 24 + 24 → 24 | stacked padding of three nested boxes vs one padding after flattening | 0:38-0:45 on-screen |
| 16:9 | single media ratio for every card in a grid; "cropped, never stretched" | 0:47-0:56 on-screen + voice |
| 1 ratio · 0 broken rows | grid result after unifying ratios | 0:46-0:56 on-screen |
| border `rgba(255,255,255,.10)` | dark-mode card edge (light colour at 10 % alpha) | 0:58-1:01 on-screen |
| surface 0 / 1 / 2 | dark-mode elevation expressed as tint steps ("elevation → tint") | 1:02-1:04 on-screen |
| 6 decisions | Entity, Treatment, Clickable, No nesting, Media ratio, Dark mode | 1:05 on-screen + voice |

Hex values of the light background tints and dark surfaces are omitted (colour-independent skill); the light tints are a near-white grey for the "tinted" band and a slightly different near-white for the panel.

## Before / after
- **Card for everything vs one card, one entity.** Bad: a settings page with Profile, Notifications and Billing each boxed as a card ("3 cards, 0 entities"). Good: one surface with section labels (PROFILE, NOTIFICATIONS, BILLING) and dividers. Why: a card promises an object you can open; boxing form sections adds borders without adding meaning, and the voice notes this is a common AI-generated tell.
- **Treatment ignores background vs background picks it.** On white, a shadow-only card "barely reads"; on a tinted background, border plus shadow becomes a "double outline" (noise). Good: border on white, shadow on tinted, flat inside a panel. Why: each treatment works only by contrast with its surroundings; one combined style looks wrong in at least two places.
- **Partial click target vs whole surface.** Bad: a card with Archive and Open buttons ("2 actions in 1 card"). Good: the entire card is one link (hover lifts the whole card, click opens the Project details panel); secondary actions move to a "..." menu on a list row ("1 surface · menu for the rest"). Why: a card with two buttons is really a panel; one target per surface is predictable and large.
- **Nested cards vs dividers.** Bad: Project details panel containing a Team card containing a Milestones card ("box in a box in a box"), padding stacking 24 + 24 + 24. Good: flat sections with small-caps labels and divider lines, one 24 padding. Why: nested boxes waste width on repeated padding and borders and blur the hierarchy.
- **Mixed media ratios vs one ratio.** Bad: one tall image breaks the grid row, leaving an empty gap ("row breaks"), or an image is stretched to fit. Good: every card image at 16:9, cropped ("16:9 cropped"). Why: equal media heights keep rows aligned and scannable.
- **Shadows in dark mode vs border + tint.** Bad: shadows vanish on dark surfaces ("shadows gone"). Good: a light border at 10 % alpha and surfaces stepped 0 / 1 / 2 in lightness. Why: dark backgrounds cannot show darker shadows; lightness becomes the elevation cue.

## Do
- Reserve cards for repeatable entities that have a title, a subject and a destination.
- Pick the edge treatment from the background: border on white, shadow on a tinted surface, flat inside a panel or sheet.
- Make the whole card one link; apply hover feedback (lift) to the whole surface.
- Move secondary actions to an overflow menu or turn the layout into a list/panel.
- Inside a card or panel, group with dividers and section labels.
- Set one aspect ratio for card media in a grid (16:9 shown) and crop with `object-fit: cover`.
- In dark mode, use a faint light border and a lighter surface step instead of shadows.

## Don't
- Don't wrap form sections or settings groups in cards.
- Don't combine border and shadow on a tinted background.
- Don't place two buttons in a clickable card.
- Don't nest a card inside a card.
- Don't let one image's natural ratio set its card height; don't stretch images.

## Scene by scene
- 0:00 "Cards are a system · 01": a project list (Fathom / Projects) with the same card on three background bands labelled border, shadow, flat (with their background tints); badge "3 backgrounds · 3 treatments · 1 component".
- 0:05 "02 One card, one entity.": a card annotated 1 Title (Atlas redesign), 2 Subject (Northwind Labs · 72 %), 3 Destination (Project page); below, a Settings page split into three cards; badge "1 card = 1 thing".
- 0:11 Settings flagged "3 cards, 0 entities", then flattened to labelled sections with dividers: "3 sections".
- 0:17 "03 The background picks the treatment.": white band with bordered card, tinted band with shadowed card, "Project details" panel with a flat card; chain "white → border · tinted → shadow · panel → flat".
- 0:21 Counter-examples: shadow on white tagged "barely reads", border + shadow on tinted tagged "double outline"; both struck through.
- 0:28 "04 One surface, one action.": cursor hovers anywhere on the Atlas card; the whole card lifts with an outline; click opens a Project details side panel.
- 0:33 A "Billing v2" card with Archive and Open buttons, flagged "2 actions in 1 card"; it becomes a list of rows (Billing v2, Atlas redesign, Mobile onboarding) each with a "..." menu: "1 surface · menu for the rest". Badge "1 surface · 1 action".
- 0:38 "05 Never nest cards.": Project details panel with a Team card and a nested Milestones card; tags "box in a box in a box" and "24 + 24 + 24".
- 0:43 Inner boxes removed: section labels TEAM / MILESTONES with dividers, padding tag "24"; badge "0 nested · dividers inside".
- 0:46 "06 One ratio across the grid.": a 2-column card grid where Mobile onboarding has a taller image; tag "row breaks" and an "empty" gap under the neighbour.
- 0:50 Images labelled 16:9; a "stretched" image tagged "stretched, not cropped", then replaced by "16:9 cropped"; badge "1 ratio · 0 broken rows".
- 0:57 "07 Dark mode kills shadows.": the grid and panel switch to dark; "shadows gone" struck; "border + tint" with a hairline measure `rgba(255,255,255,.10)`; panel shows "elevation → tint" swatches surface 0, 1, 2. Badge "dark → border + tint, 0 shadow".
- 1:05 "08 Six decisions. One card that knows its background.": checklist Entity, Treatment, Clickable, No nesting, Media ratio, Dark mode.

## Voice-over summary
- Cards are a system: border, shadow or flat, and the background decides.
- A card is one entity: one title, one subject, one place to go; a form section is not a card, and "cards for everything" is an AI tell.
- Border on white, shadow on tinted, flat inside a panel; on white a shadow barely reads, on grey a border is noise.
- A clickable card is clickable everywhere; two buttons inside make it a panel; hover lifts the whole thing.
- Never nest cards: flatten the inner one and let dividers group.
- Media keeps one aspect ratio across the grid (16:9, cropped, never stretched); in dark mode shadows die, so borders come back one step lighter than the surface and elevation becomes tint.

## Notes for the skill
- Whole-card link: wrap the title in an `<a>` and stretch its hit area with a pseudo-element (`.card a::after { position:absolute; inset:0 }`) rather than wrapping the whole card in `<a>`, so screen readers announce a concise link name and text stays selectable. Hover lift should also apply on `:focus-visible` (visible focus ring on the card), and the lift motion should be removed under `prefers-reduced-motion`.
- If a card truly needs a secondary action, the overflow menu button must sit above the stretched link (`position:relative; z-index:1`) and have its own accessible name; avoid nested interactive elements inside an `<a>`.
- Media ratio: `aspect-ratio: 16 / 9; object-fit: cover;` on the image container; choose a focal point (`object-position`) so cropping does not cut faces or key content.
- "Shadow on white barely reads" is an aesthetic judgement of the video; many systems do use soft shadows on white. The useful rule is to pick one treatment per background and not stack border plus shadow.
- A 10 % alpha light border is decorative; it does not meet the 3:1 non-text contrast of WCAG 1.4.11. That is fine for a card whose boundary is not needed to identify the control, but if the card itself is the interactive target, keep its focus indicator strong.
- Using flat sections instead of cards in settings matches common platform guidance (grouped lists with section headers).
