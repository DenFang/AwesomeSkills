---
id: DXCMEljsw3w
reel_url: https://www.instagram.com/reel/DXCMEljsw3w/
pattern_page: https://designmotionhq.com/patterns/design-system-kit
date: 2026-04-12
duration_s: 73
type: ui
category: visual
topic: five foundations of a design system (semantic colour tokens, type scale, 4px spacing, component states, motion scale)
sources: frames, voice-over, pattern page
---

# Design system foundations: tokens, type scale, spacing, states, motion

**Caption:** Atomic design system is the key 🔑
**Hook:** Most design systems fail because they skip five basics: semantic colour, a type scale, consistent spacing, components with every state, and purposeful motion.

## Main rule
Store every visual decision as a named token on a fixed scale (colour by purpose, numbered shade scale, type steps with size/weight/line-height, a 4px spacing scale, a duration/easing scale) and build every component with all of its states before it is reused.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 5 | number of foundations | 0:00-0:06 voice + title "5 things you need" |
| 9 shades, 900 -> 100 | primary colour scale (900, 800, 700, 600, 500, 400, 300, 200, 100) | 0:10-0:19 on-screen + voice ("nine shades") |
| 100-900 | numbered colour scale | pattern page |
| 4 semantic roles shown | bg-primary, brand, success, error (voice also names surface) | 0:13-0:19 on-screen + voice |
| 48px / 800 | type step `text-5xl` | 0:24-0:32 on-screen |
| 36px / 700 | type step `text-4xl` | 0:24-0:32 on-screen |
| 28px / 700 | type step `text-3xl` | 0:24-0:32 on-screen |
| 22px / 600 | type step `text-2xl` | 0:24-0:32 on-screen |
| 24px / 400 | type step `text-lg` | 0:25-0:32 on-screen |
| 20px / 400 | type step `text-base` | 0:25-0:32 on-screen |
| 400 / 500 / 700 / 800 | font weights Regular / Medium / Bold / Extrabold | 0:29-0:32 on-screen |
| 4px | spacing base unit; every margin, padding, gap is a multiple | 0:33-0:41 voice + on-screen "4px GRID" |
| 7px, 23px vs 16px, 16px | "Random" vs "System" gaps in the comparison | 0:33-0:37 on-screen |
| space-1 4px, space-2 8px, space-3 12px, space-4 16px, space-6 24px, space-8 32px, space-12 48px, space-16 64px | spacing tokens | 0:37-0:41 on-screen; page: space-1=4 ... space-16=64 |
| 7px, 23px, 11px | examples of random gaps that look sloppy | pattern page |
| 4 button variants | Primary, Secondary, Ghost, Destructive | 0:43-0:55 on-screen |
| 3 sizes | Small, Medium, Large | 0:44-0:55 on-screen |
| input states default / focus / error / disabled | input component | 0:46-0:49 on-screen |
| default, hover, active, focus, disabled | component states listed by voice | 0:45-0:50 voice |
| 4 badge states | New, Active, Pending, Error | 0:50-0:55 on-screen |
| ease-out = enter/appear; ease-in-out = move/resize; ease-in = exit/leave | easing by intent | 0:56-1:04 on-screen; voice mentions ease-out enters, ease-in exits |
| 100ms | Micro: hover, toggle | 0:60-1:04 on-screen |
| 200ms | Small: button press | 0:60-1:04 on-screen |
| 300ms, tagged MAX | Medium: modal, dropdown; voice: "300 milliseconds max for interactions" | 0:60-1:04 on-screen + voice |
| 400ms | Large: page transition | 0:60-1:04 on-screen |
| 500ms | XL: complex | 0:61-1:04 on-screen; page: scale runs 100 ms micro to 500 ms complex |
| fade-in, slide-up, scale-in, bounce | named animation presets | 1:03-1:05 on-screen |
| $14 | price of the advertised kit | 1:07-1:12 on-screen (ad, not a design value) |

## Before / after
1. **Colours: raw hex vs semantic variables (0:06-0:19).** Before: CSS with literal hex values for text, background, border and error colour. After: the same properties pointing to `var(--brand)`, `var(--bg-surface)`, `var(--border)`, `var(--error)`, followed by a 900-100 primary scale and a semantic swatch grid. Why it works: names carry intent, so a rebrand or dark theme is one token change, and nobody has to remember which hex means "error".
2. **Typography: flat vs hierarchical (0:21-0:32).** Before: heading and body in nearly the same size and weight, tagged "No hierarchy". After: a large heavy heading over regular body text, tagged "Clear hierarchy", backed by a size/weight table. Why: hierarchy is read from size and weight contrast before the words are read; equal sizes force the user to parse everything.
3. **Spacing: random vs system (0:33-0:41).** Before: stacked bars with 7px and 23px gaps. After: identical bars with 16px and 16px gaps. Then a spacing token ladder 4-64 px and a card layout with a "4px GRID" overlay. Why: consistent rhythm makes grouping predictable and reads as deliberate; uneven gaps look like mistakes even when the viewer cannot say why.
4. **Components: happy path vs all states (0:43-0:55).** Shown as a build-up rather than a bad version: buttons in four variants and three sizes, one input cycling default -> focus -> error ("Required field") -> disabled, a card, and status badges. Why: states are what users actually hit; a component without focus/error/disabled gets patched ad hoc in every screen.
5. **Motion: easing by intent (0:56-1:05).** Three squares animate with ease-out (enter), ease-in-out (move), ease-in (exit), then a duration ladder 100-500 ms with 300 ms marked as the interaction maximum, then presets. Why: deceleration on entry makes things feel responsive, acceleration on exit gets them out of the way, and short durations avoid blocking input.

## Do
- Name colours by role (background, surface, border, brand, success, error) and reference only the tokens in components.
- Generate a numbered shade scale (100-900) per hue and map semantic tokens onto it.
- Define each type step as size + weight + line height, with clear jumps between steps.
- Use a 4px base spacing scale and only its values for margin, padding and gap.
- Ship every component with variants, sizes and states (default, hover, active/pressed, focus-visible, disabled, plus error for inputs).
- Pick easing by intent: ease-out to enter, ease-in-out to move/resize, ease-in to exit; keep interaction feedback at or below 300 ms.

## Don't
- Don't hardcode hex or pixel values inline in components.
- Don't choose gaps by eye (7px here, 23px there).
- Don't give headings and body the same size and weight.
- Don't design only the default state of a button or input.
- Don't let animations block the user from acting.

## Scene by scene
- 0:00 Five tilted cards float in (colour swatches, "Aa" type card, spacing bars, a bezier curve, a button/input/badge card), then settle into a grid; title "Design system, 5 things you need".
- 0:04 "01 Colors": Before code block with literal hex values vs After block with `var(--brand)`, `var(--bg-surface)`, `var(--border)`, `var(--error)`; After gets a check mark.
- 0:09 "Primary scale" bar fills in from 900 to 100.
- 0:13 Semantic swatch grid: bg-primary, brand, success, error.
- 0:20 "02 Typography": Before card (heading and body similar size, "No hierarchy") vs After card (big bold heading, "Clear hierarchy").
- 0:24 Type scale rows appear one by one: 48/800, 36/700, 28/700, 22/600, 24/400, 20/400 with utility-class labels.
- 0:29 Weight row: Regular 400, Medium 500, Bold 700, Extrabold 800.
- 0:33 "03 Spacing": Random card (7px, 23px gaps) vs System card (16px, 16px).
- 0:37 Spacing token ladder space-1 4px ... space-16 64px.
- 0:40 Card layout mock with a "4px GRID" label.
- 0:43 "04 Components": buttons Primary and Secondary appear, then Ghost and Destructive, then Small / Medium / Large.
- 0:46 Email input cycles default, focus (accent border), error (danger border, "Required field"), disabled.
- 0:49 Card with image band, "Card Title", description and Action button; badges New, Active, Pending, Error.
- 0:56 "05 Motion": three squares labelled ease-out (Enter/appear), ease-in-out (Move/resize), ease-in (Exit/leave) loop their motion.
- 1:00 Duration ladder 100/200/300/400/500 ms with use cases; 300 ms row highlighted "MAX".
- 1:03 Preset tiles fade-in, slide-up, scale-in, bounce.
- 1:06 Product card "Design System Kit $14", icons for the five parts, "Link in bio".

## Voice-over summary
- Most design systems fail by skipping five basics.
- Colour: stop using raw hex; name colours by purpose and build a nine-shade primary scale as the single source of truth.
- Type: every step intentional (display, heading, body, small), each with size, weight and line height, so hierarchy is felt.
- Spacing: one base unit of 4 px; every margin, padding and gap is a multiple.
- Components: design every state, not only the happy path (default, hover, active, focus, disabled) for buttons, inputs, cards, badges; build once, reuse.
- Motion: right easing and duration for each animation, ease-out for entering, ease-in for exiting, never block the user, 300 ms max for interactions. Ends by advertising a paid kit.

## Notes for the skill
- CSS: define `--color-*` primitives (e.g. `--primary-100` ... `--primary-900`) and semantic aliases (`--bg`, `--surface`, `--border`, `--text`, `--text-muted`, `--brand`, `--success`, `--warning`, `--danger`) that components use exclusively; themes swap the alias layer only.
- Spacing tokens `--space-1: 4px` ... `--space-16: 64px` (keys = multiples of 4). Allow 2px only as a documented exception for hairline/icon nudges if needed.
- Type tokens should bundle size, weight and line height (and letter-spacing for display sizes). The on-screen table is not monotonic: `text-2xl` 22px sits above `text-lg` 24px, and the class names do not match Tailwind defaults (Tailwind: text-2xl 24px, text-lg 18px, text-base 16px). Treat the table as illustrative; a real scale must strictly increase with step name. A 20px body size is also larger than the usual 16px body default.
- The video names line height in the voice-over but shows no line-height values.
- Component states: the voice lists hover/active but the input demo shows default/focus/error/disabled. A complete set is default, hover, pressed/active, focus-visible, disabled, loading (buttons), error/invalid and read-only (inputs). Use `:focus-visible`, `aria-disabled`/`disabled`, `aria-invalid`.
- Motion: 300 ms is a cap for direct interaction feedback (hover, press, dropdown, modal open), not for all animation; the same screen lists 400 ms page transitions and 500 ms complex sequences. Exits can be shorter than entrances. Respect `prefers-reduced-motion` (drop movement, keep opacity or instant state change). "bounce" presets should be used sparingly in product UI.
- Disabled inputs typically fall below 4.5:1; WCAG exempts inactive components from contrast, but the label should still be readable and the reason for disabling discoverable.
- The ending is a paid product ad; the design content before it stands on its own.
