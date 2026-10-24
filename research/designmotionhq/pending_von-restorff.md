---
id: unknown
reel_url: unknown
pattern_page: https://designmotionhq.com/patterns/von-restorff
date: unknown
duration_s: 36
type: ui
category: visual
topic: Von Restorff (isolation) effect: one emphasised element per view
sources: frames, voice-over, pattern page
---

# Von Restorff effect: isolate the one thing you want chosen

**Caption:** not captured yet
**Hook:** Three identical pricing cards get no clicks; changing one thing is claimed to triple conversions.

## Main rule
Against a calm, uniform baseline, make exactly one element per view break the pattern (the target plan, the primary CTA, the main form button) by combining several cues: size, fill with the accent colour, weight, elevation/glow and a label. Keep everything around it visually quiet.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 3x more conversions | claimed result of isolating one pricing card | 0:02-0:06 on-screen + voice; page subtitle "3× more conversions" |
| 3 cards: Basic $9, Pro $19, Team $49 /month | first pricing demo | 0:00-0:06 on-screen |
| 3 cards: Basic $9/mo, Pro $29/mo, Enterprise $99/mo | second pricing demo ("Isolate your target") | 0:14-0:22 on-screen |
| 7 list items, 1 different | classic isolation demo (six plain words, one capitalised accent word) | 0:07-0:13 on-screen |
| Attention 80% | attention meter on the isolated nav CTA | 0:24-0:30 on-screen |
| 1 element per view | limit of emphasis | page |

The 3x and 80% figures are not sourced; treat them as illustrative.

## Before / after
1. **Identical pricing cards (0:00-0:06).** Before: three cards with the same size, surface, button style ("Choose Plan") and type weight: "Nobody clicks." After: the middle (Pro) card scales up and lifts above the row, gets the accent fill, a "Most Popular" badge, a richer feature list and a filled button, while Basic and Team dim. Why: with a uniform baseline the eye has no entry point; one element that differs in several dimensions becomes the first fixation and the default choice.
2. **Isolation in a list (0:07-0:13).** A vertical list of fruit names with one item set in capitals, the accent colour and bracket marks; the other items fade. Subtitle "What's different gets remembered." Why: memory and attention favour the item that breaks the group's pattern (the isolation effect from von Restorff's 1933 experiments).
3. **Isolate your target (0:14-0:22).** Second pricing set: Pro becomes taller, accent-filled, badged "Most Popular", with the button label changed to "Get Pro"; Basic shows struck/dimmed missing features; "The target" pointer below. Why: a specific CTA label plus visual isolation steers the decision without removing the alternatives.
4. **Break the pattern in navigation and forms (0:23-0:30).** A top nav (Home, Features, Pricing, Blog as quiet text links) where "Get Started" becomes an accent-filled button; attention meter fills to 80%; caption "Different color. Different weight." Below, a "Create Account" form (email, password) whose Sign Up button changes from a muted fill to the accent fill. Why: the primary action is the only filled, high-contrast control, so the next step is never ambiguous.

## Do
- Start from a uniform baseline (same card size, same quiet button style), then change one element.
- Combine cues: scale, accent fill, weight, elevation or glow, and a text badge ("Most Popular").
- Give the isolated CTA a specific label ("Get Pro", "Get Started") rather than the generic label the others use.
- Keep secondary actions and alternatives muted but still readable.
- Limit emphasis to one element per view.

## Don't
- Don't ship identical options and hope users pick the intended one.
- Don't highlight two or three elements at once; competing emphasis cancels out.
- Don't rely on colour alone to mark the standout.

## Scene by scene
- 0:00 "Nobody clicks." Three identical pricing cards (Basic $9, Pro $19, Team $49 per month, each "5 projects / Basic support", "Choose Plan").
- 0:02 The Pro card grows and rises, gets the accent fill, "Most Popular" badge, three features (Unlimited projects, Custom domains, Priority support) and a lighter "Choose Plan" button; side cards dim. Headline "3x more conversions", a large "3x" counts in below.
- 0:07 "The Von Restorff Effect · What's different gets remembered": list apple, banana, cherry, [one capitalised accent word], fig, grape, kiwi; brackets appear around the odd item and the rest fade.
- 0:14 "Isolate your target": Basic $9/mo, Pro $29/mo, Enterprise $99/mo in equal cards; Pro then scales, accent-filled, badged, "Get Pro" button; "The target" pointer label.
- 0:23 "Break the pattern": nav bar "AppCo" with four text links and a "Get Started" button that switches from a neutral to an accent fill; "Attention" dot meter reaching 80%; caption "Different color. Different weight."
- 0:25 A "Create Account" card (Email address, Password) appears; its Sign Up button changes from muted to accent-filled.
- 0:31 Summary rows: Pricing "Isolate the target plan", Navigation "One CTA breaks the pattern", Forms "Highlight the primary action".
- 0:33 "Follow for design psychology · Save this".

## Voice-over summary
- Three pricing cards and nobody clicks; change one thing and conversions are claimed to triple.
- The brain ignores patterns and remembers what breaks them: the Von Restorff effect.
- In pricing, make the target plan bigger, coloured and labelled; the other plans exist to make it shine.
- In navigation, one button breaks the pattern with a different colour and weight; that is the conversion magnet.

## Notes for the skill
- Claims: the isolation effect is well established in memory research; "3x more conversions" and "Attention 80%" are unsourced marketing numbers. Do not cite them.
- Colour alone is not enough (WCAG 1.4.1 Use of Color): combine accent fill with size, elevation, border and a text badge so the standout works for colour-blind users and in greyscale.
- Dimmed alternatives must stay readable: muted text still needs at least 4.5:1 contrast (3:1 for large text and for button boundaries). Reduce emphasis through weight, fill and elevation rather than by dropping text contrast below the minimum; users still need to compare plans.
- The badge must be truthful ("Most Popular" only if it is); fake popularity labels and visually hiding cheaper options are dark patterns.
- Demo inconsistency: in the nav + form scene both the nav "Get Started" and the form "Sign Up" end up accent-filled at the same time, which breaks the video's own one-emphasis-per-view rule. When a primary form action is on screen, demote the nav CTA (outline or text style) or keep the form button as the single filled control.
- On mobile, stacked pricing cards lose the side-by-side contrast; put the target plan first or keep its badge and fill, and avoid scaling transforms that cause horizontal overflow.
- Implementation: express emphasis as a component variant (`variant="primary"` vs `"secondary"`/`"ghost"`) so only one primary exists per view; for the featured card use a `featured` prop that changes elevation, border and badge, not just a colour token.
