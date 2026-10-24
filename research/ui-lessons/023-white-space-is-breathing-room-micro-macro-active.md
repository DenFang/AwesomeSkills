---
lesson: 023
kind: video
duration_s: 35
type: ui
category: visual
topic: White space: micro, macro and active; card padding before/after
sources: frames, voice-over
---

# White space is breathing room: micro, macro, active

**Hook:** White space is not empty, it is breathing room.

## Main rule
Treat spacing as three deliberate layers (padding inside elements, margins between sections, and intentionally large gaps around the one thing that matters), and when a component feels cramped, roughly double its inner padding and gaps before changing anything else.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 3 | types of white space: micro, macro, active | 0:03-0:17 on-screen + voice |
| padding: 18px | micro example, inside a "Subscribe" button | 0:06-0:17 on-screen label |
| 48px | macro example, gap between two content blocks | 0:08-0:17 on-screen label |
| padding 16px, gap 8px | profile card BEFORE ("cramped") | 0:18-0:22 on-screen + voice |
| padding 32px, gap 16px | profile card AFTER, as spoken ("double it") | 0:24-0:26 voice |
| padding 40px, gap 22px | profile card AFTER, as labelled on screen | 0:23-0:31 on-screen label |
| 2x | scaling factor from before to after (voice); on-screen labels imply 2.5x padding, 2.75x gap | voice + calculation |
Voice and on-screen labels disagree for the AFTER card (32/16 spoken vs 40/22 shown). Both are listed; the rule of thumb in either case is "about double".

## Before / after
1. **Profile card (0:18-0:31).** Before, "Cramped version": padding 16 px, gap 8 px; name, role, bio, stats (248 Posts, 12.4K Followers, 892 Following, 36 Projects), four tags and a full-width Follow button pressed together; bio wraps in long lines with tight leading. After: padding doubled (32 px spoken / 40 px shown) and gaps doubled (16 px spoken / 22 px shown); a thin divider appears above the stats, the bio wraps to shorter lines, the button is taller. Overlay: "Same content. Feels premium." Why: larger padding separates the card's content from its edge so the boundary stops competing with the text, and larger gaps create distinct groups (identity, bio, stats, tags, action) that the eye can scan one by one; shorter line length improves readability.
2. **Three types (0:03-0:17).** Micro: padding inside buttons, inputs and cards (button with 18 px padding). Macro: margins between sections, the vertical rhythm of the page (48 px between blocks). Active: intentional emptiness to draw focus, "the space that makes one element pop" (a lone "Get Started Free" button with a glow surrounded by empty space).

## Do
- Define spacing at three levels: component padding (micro), section rhythm (macro), and generous isolation around the primary element (active).
- When a card feels cheap or crowded, increase inner padding and inter-group gaps together, roughly 2x.
- Keep the gap between groups inside a card larger than the spacing within a group.
- Use empty space around the single primary CTA to make it the focal point.

## Don't
- Don't pack a card at minimum padding with uniform small gaps; every element then competes equally.
- Don't fill every empty area with content or decoration; emptiness is a tool for focus.

## Scene by scene
- 0:00 Title "White Space" over a dense 3x3 grid of placeholder cards; subtitle "It's not empty. It's breathing room."
- 0:03 "3 Types of white space you should know": Micro card (padding inside elements, Subscribe button with "padding: 18px").
- 0:07 Macro card added (margins between sections, vertical rhythm; two blocks with "48px" between).
- 0:07 Active card added (intentional emptiness to draw focus; glowing "Get Started Free").
- 0:18 "Real example, watch the card transform in real-time", label "Before" with "padding: 16px", "gap: 8px": cramped Alex Rivera profile card.
- 0:23 Label "After", "padding: 16px gap: 8px -> padding: 40px gap: 22px"; the card expands and re-flows.
- 0:27 "Same content. Feels premium."
- 0:32 Outro "Give your designs room to breathe. Follow for daily design tips."

## Voice-over summary
- White space is not empty, it is breathing room.
- Three types: micro (padding inside a button), macro (margins between sections), active (intentionally large gaps that draw the eye to what matters).
- The cramped card has 16 px padding and 8 px gaps; doubling to 32 px padding and 16 px gaps makes the same content feel premium.

## Notes for the skill
- Implement with a spacing scale (for example 4/8/12/16/24/32/48 px tokens). The spoken after-values (32/16) sit on an 8-pt scale; the on-screen 40/22 values do not (22 is off-grid), so prefer the spoken pair or the nearest tokens.
- The "after" card also changes typography: larger body text, more line-height, shorter line length, a divider and a taller button. Spacing is not the only variable; for body text use line-height around 1.4-1.6 and a measure of about 45-75 characters.
- On narrow mobile widths, 32-40 px card padding eats content width; scale padding by breakpoint (for example 16-20 px on phones, 24-32 px on wider screens) while keeping the inside-vs-between-group ratio.
- More padding inside buttons also helps touch targets: keep interactive controls at least 24x24 px (WCAG 2.5.8), ideally 44x44 px.
- "Active white space" overlaps with the single-accent rule: isolation plus one accent is what makes the primary CTA pop; the glow is decorative and optional.
