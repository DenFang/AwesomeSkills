---
lesson: 016
kind: video
duration_s: 30
type: ui
category: visual
topic: 60-30-10 colour proportion rule for UI
sources: frames, voice-over
---

# 60-30-10: dominant, secondary, accent

**Hook:** Stop picking colours at random; one ratio is all you need.

## Main rule
Distribute colour by area: about 60 % one dominant base (the page background), about 30 % a secondary surface derived from the same hue with slightly higher lightness (cards, navigation, containers), and about 10 % a single high-contrast accent reserved for primary actions and the one data point that matters.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 60 % | dominant base colour, one dark background ("60% is just background", "Pick ONE dark color. It covers 60% of your screen.") | 0:05-0:10 on-screen + voice |
| 30 % | secondary: same hue, "+lightness"; used for cards, nav, containers | 0:11-0:18 on-screen + voice |
| 10 % | accent: "Warm · max contrast"; labelled "CTA"; "ONE bold color. Only for CTAs and key actions." | 0:19-0:22 on-screen + voice |
| 3 colours | the whole palette in the demo ("3 colors. Zero guesswork.") | 0:23 on-screen |
| 60 : 30 : 10 | donut chart filling segment by segment as each role is introduced | 0:05-0:22 on-screen |

The video shows concrete hex swatches for the three roles; they are omitted here on purpose (the skill is colour-independent). The relationships are what matter: base and secondary share a hue and differ only in lightness; the accent is a contrasting (warm against a cool base) hue at maximum contrast.

## Before / after
- **No system vs 60:30:10 (0:00-0:04).** A wipe line splits the same dashboard. Left, "No system": a saturated header bar, a multi-colour revenue bar (four different hues), a coloured panel for Active Users, a filled primary-colour Upgrade button next to a different-colour pill, and the revenue number in yet another colour. Right, "60:30:10": the same components on neutral dark surfaces with only the Upgrade, View All and the active bar segments in the accent. Why the right side works: when most of the screen is one quiet base, the eye has nothing competing with the accent, so the accent reliably signals "act here"; many unrelated hues each claim attention and nothing stands out.
- **Building it up (0:05-0:22).** Empty window ("60% is just background") → secondary surfaces add the nav bar, two stat cards (Revenue $24,500, Users 1,234) and a Monthly Revenue chart in neutral greys → the accent lands only on "Upgrade to Pro", "View All", the latest chart bar and the small "+12%" / "+8%" deltas. Mechanism: hierarchy by scarcity; the accent's power depends on how rarely it appears.

## Do
- Pick one base colour for the page background and let it cover most of the screen.
- Derive card, nav and container surfaces from the base hue by raising lightness a step, rather than introducing a new hue.
- Reserve a single accent for the primary CTA and the key highlighted value (e.g. the current period's bar).
- Keep chart bars neutral and highlight only the bar you want read.

## Don't
- Don't give every panel, metric and segment its own hue.
- Don't use the accent for decoration or for several competing buttons.
- Don't mix a coloured header, coloured panels and a coloured button on the same screen.

## Scene by scene
- 0:00 Title "60 : 30 : 10 · The only color rule you need" over a dashboard split by a vertical wipe: left labelled "No system" (many saturated colours), right labelled "60 : 30 : 10" (neutral surfaces, one accent). "Save for later" hint below.
- 0:05 "01 DOMINANT 60%" with a donut chart filling to 60 %. A browser window "dashboard.app" is empty, watermark "60% is just background"; a swatch labelled "60% · Base". Caption "Pick ONE dark color. It covers 60% of your screen."
- 0:11 "02 SECONDARY 30%": donut adds the 30 % segment; nav tabs (Dashboard, Analytics, Reports, Settings), "Welcome back / Here's your overview for today", stat cards and a Monthly Revenue bar chart appear. Swatch strip shows the base → slider "Same hue · +lightness" → "30% · Cards". Caption "Same hue, slightly lighter. Cards, nav, containers."
- 0:19 "03 ACCENT 10%": donut adds the 10 % segment; "Upgrade to Pro" button, "View All" chip and the last chart bar switch to the accent; deltas "+12%" and "+8%" appear. Swatch strip adds "Warm · max contrast" → "10% · CTA". Caption "ONE bold color. Only for CTAs and key actions."
- 0:23 Finished dashboard, caption "3 colors. Zero guesswork."
- 0:25 End card "Stop guessing colors. Use 60 : 30 : 10" and a follow button.

## Voice-over summary
- Stop picking colours randomly; the 60-30-10 rule is all you need.
- 60 % is the dominant colour: one dark background that sets the tone.
- 30 % is the secondary: same hue, slightly lighter, for cards, nav and containers.
- 10 % is one bold accent, only for buttons and key actions.
- "Three numbers. Zero guesswork."

## Notes for the skill
- Implement as role tokens, not literal colours: `--surface-base` (60 %), `--surface-raised` (30 %, base hue with higher lightness), `--accent` (10 %, CTA and key highlight), plus text tokens. The ratio describes visual area, not a count of tokens.
- The rule is a heuristic from interior design; real UIs also need text colours, borders, and semantic states (success, warning, danger, info). Those sit outside the 60-30-10 budget and should be used sparingly and only for their meaning; the video does not mention them.
- Contrast: body text on both base and raised surfaces must reach at least 4.5:1 (WCAG 1.4.3); the accent button's label against the accent fill must reach 4.5:1 too, and the button boundary against the surface should reach 3:1 (WCAG 1.4.11). "Max contrast" for the accent is about salience, not a guarantee of text contrast.
- The demo also uses the accent for small "+12%" delta text; small accent-coloured text on a dark surface often fails 4.5:1, and positive deltas are usually better shown with the success role plus an arrow or sign, not colour alone.
- The rule works in light themes too: the base becomes a light neutral and the raised surface steps toward white or uses borders; the video shows only the dark case.
