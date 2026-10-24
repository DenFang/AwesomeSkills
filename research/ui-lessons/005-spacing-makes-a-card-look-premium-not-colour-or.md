---
lesson: 005
kind: video
duration_s: 48
type: ui
category: visual
topic: card spacing (padding, element gap, line height, breathing room)
sources: frames, voice-over
---

# Spacing makes a card look premium, not colour or font

**Hook:** The social-post card looks cheap, and the cause is neither its colours nor its font: it is the spacing.

## Main rule
Before touching colour or type, fix spacing: give the card generous inner padding (about 28 px instead of 8 px), separate its sections with a real gap (about 18 px instead of 4 px), set body line height to about 1.6 instead of 1.1, and give the action row its own room. Content, components and colours stay identical.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| padding 8px → 28px (animated through 13px, 23px) | card inner padding | 0:07-0:14 on-screen chip + voice ("8 pixels to 28") |
| gap 4px → 18px (animated through 8px, 16px) | vertical gap between card sections: header (avatar + name), text, image, action row | 0:16-0:24 on-screen chip + voice ("four pixels to 18") |
| line-height 1.1 → 1.6 (animated through 1.2, 1.4) | post body text | 0:25-0:32 on-screen chip + voice |
| spacing 2px → 28px (animated through 7px, 22px) | "Breathing room": the action/icon row (likes 2.4K, comments 128, reposts 847, bookmark); exact property unclear on screen, visible change is subtle | 0:33-0:40 on-screen chip + voice ("the icons spread out") |
| 4 fixes | number of spacing changes | 0:01 on-screen "4 spacing fixes. Watch." |

## Before / after
- **Padding 8 → 28 px.** Bad: text and image almost touch the card border, so the card reads as a cramped box. Good: content pulls away from the edges. Why: the inset frame separates content from its container, so the card looks deliberate rather than squeezed in.
- **Section gap 4 → 18 px.** Bad: header, body text, image and action row are stacked almost touching and blur into one block. Good: each section separates as its own group. Why: proximity defines grouping; a clear gap between unrelated parts lets the eye parse the card in steps.
- **Line height 1.1 → 1.6.** Bad: three lines of body text "suffocate", lines nearly collide. Good: lines breathe and are easy to track. Why: enough leading lets the eye return to the start of the next line without losing its place.
- **Action row breathing room.** Bad: icons and counts sit tight to the image. Good: the action row gets its own space and the card gets its final polish.
- **Final comparison (0:40-0:45):** the BEFORE card next to the AFTER card, "Same card. Just spacing." Same content, same colours, only spacing differs.

## Do
- Use a card inner padding in the 24-32 px range for content cards (28 px shown).
- Put a consistent gap (about 16-18 px) between distinct sections of a card: header, text, media, actions.
- Set body text line height around 1.5-1.6 for multi-line copy.
- Give the action row separation from the media above it.
- Fix spacing first when a component "looks cheap"; change colour or font only afterwards.

## Don't
- Don't use single-digit padding (8 px) on content cards.
- Don't stack card sections with 2-4 px gaps.
- Don't set body copy at line height 1.1 (that value suits only large display headings).

## Scene by scene
- 0:00 Title "This card looks cheap." over a cramped dark social-post card (avatar, name with verified dot, handle and "2h", 3-line text, image placeholder, action row with 2.4K / 128 / 847 / bookmark). A warning-tone glow behind the card.
- 0:01 Subtitle "4 spacing fixes. Watch." The card glow shifts to a success tone for a moment.
- 0:06 "FIX #1 Padding": the padding area is highlighted inside the border; chip counts "padding 8px → 13px → 23px → 28px" while the content moves inward.
- 0:15 "FIX #2 Element Spacing": highlight bars mark the gaps between header, text, image and actions; chip "gap 4px → 8px → 16px → 18px", sections separate one by one.
- 0:25 "FIX #3 Line Height": chip "line-height 1.1 → 1.2 → 1.4 → 1.6", body text re-wraps and grows taller.
- 0:33 "FIX #4 Breathing Room": chip "spacing 2px → 7px → 22px → 28px", the action row spreads slightly; a soft accent glow appears above the card.
- 0:40 Label "BEFORE" (danger tone) with the original card, then the final card with "AFTER" (success tone) and a success-tone glow; caption "Same card. Just spacing."
- 0:46 End card "Want more design tricks? Follow for daily tips" with a "+ Follow" button.

## Voice-over summary
- The card looks cheap and the reason is spacing, not colours or font; four fixes follow.
- Padding from 8 to 28 px pulls content off the edges and makes it feel intentional and premium.
- Avatar, text, image and actions each need their own space: gap from 4 to 18 px.
- Text "suffocating" at line height 1.1 becomes readable at 1.6.
- Breathing room spreads the icons; same card, same content, same colours, only spacing differs.
- Closing line: spacing is "the most expensive pixel on your screen."

## Notes for the skill
- Implement as tokens: `--card-padding: 28px` (or a 4/8-based scale value like 24/32), `gap: 18px` on a flex/grid column for card sections (16 px if staying on an 8-pt or 4-pt scale), `line-height: 1.6` on body text.
- The video's values (18 px, 28 px) are off a strict 8-pt grid; in a real system snap to the project's spacing scale (16/24/32) rather than copying odd numbers.
- Internal spacing should be smaller than external: gap between sections (18) < card padding (28) keeps the card reading as one unit.
- Line height 1.6 suits body text; headings should go tighter (about 1.1-1.25). WCAG 1.4.12 requires layouts to survive user-set line height 1.5, so do not hard-limit card heights.
- Fix #4's exact target is not legible from the frames; treat it as "give the action row its own spacing" rather than a specific property.
