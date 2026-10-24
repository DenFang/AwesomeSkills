---
lesson: 014
kind: video
duration_s: 42
type: ui
category: content
topic: decoy effect in pricing tiers
sources: frames, voice-over
---

# Decoy effect: a third pricing tier that exists to sell the top one

**Hook:** A three-plan pricing table is not a real choice; the middle plan is a decoy.

## Main rule
On a pricing page, the plan placed next to the target plan is judged against its nearest comparable neighbour, not against all options. A third plan priced close to the top plan but with clearly fewer features (an asymmetrically dominated "decoy") makes the top plan look like the obvious deal and pulls choices away from the cheapest plan. Know the mechanism to read pricing pages critically and, if you design one, use tier anchoring honestly (real, useful plans, transparent feature comparison).

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| Basic $8: 5 pages, Email support, 1 user | two-plan baseline, cheap plan | 0:03-0:10 on-screen + voice |
| Premium $16: Unlimited, Priority support, 10 users | two-plan baseline, target plan | 0:03-0:10 on-screen + voice |
| 80% Basic / 20% Premium | choice split with two plans (illustrative bars) | 0:07-0:10 on-screen; voice "most people pick basic" |
| Pro $14: 15 pages, Email support, 3 users, tagged "THE DECOY" | added third plan | 0:10-0:18 on-screen + voice |
| "Almost same price as Premium... but way fewer features" | decoy description | 0:12-0:18 on-screen |
| 20% Basic / 20% Pro / 60% Premium; "Premium jumps from 20% → 60%" (bars pass through 21% / 59%) | choice split with the decoy (illustrative) | 0:19-0:23 on-screen; voice "60% choose premium" |
| $2 more | price gap Pro $14 → Premium $16 ("Only $2 more for way more value") | 0:30-0:36 on-screen + voice |
| The Economist: Web Only $59 / Print Only $125 (decoy) / Web + Print $125 (target) | real-world example | 0:24-0:28 on-screen |
| Apple iCloud: Free 5 GB / iCloud+ 50 GB $0.99 (decoy) / iCloud+ 200 GB $2.99 (target) | example as labelled by the video | 0:25-0:28 on-screen |
| Netflix: Standard w/ Ads $6.99 / Standard $15.49 (decoy) / Premium $22.99 (target) | example as labelled by the video | 0:26-0:28 on-screen |
| Intro tiles: Pro "20 pages", Basic "Basic support" | opening teaser cards; differ from the later "15 pages" / "Email support" | 0:01-0:02 on-screen (inconsistency in the video) |

## Before / after
- **Two plans vs three plans with a decoy.** Before: Basic $8 vs Premium $16. The cheap plan is the natural pick (80/20) because the comparison is cheap-versus-expensive and the price doubles. After: Pro $14 is inserted between them with fewer features than Premium. Choice shifts to Premium (illustrated 60%). Why: people evaluate options relative to the closest comparable one. Pro and Premium are easy to compare feature by feature (15 vs Unlimited pages, Email vs Priority support, 3 vs 10 users), and Premium dominates Pro for only $2 more. Basic is a different kind of option, harder to compare, so it drops out of attention ("Basic? Already forgotten").

## Do
- When designing tiers, show a side-by-side feature comparison with aligned rows (pages, support, users, price), since that is what users compare.
- Highlight the recommended plan clearly (border, label "Most popular" or similar) and make its advantages explicit in the same rows.
- Keep each plan genuinely useful to some segment; if a plan only exists to steer, users notice and trust drops.
- Present the price delta between neighbouring plans explicitly if it is the real value story ("$2 more for ...").

## Don't
- Don't add a plan that no one should buy just to manipulate choice; regulators and users increasingly treat this as a deceptive pattern.
- Don't let the table hide the cheapest viable option or make it visually unreachable.
- Don't treat the video's percentages as data: the bars are illustrative.

## Scene by scene
- 0:00 Title "How apps use the decoy effect"; three plan cards appear (Basic $8, Pro $14, Premium $16 highlighted with an accent fill); a cursor clicks Premium. Text "This is not a real choice." Captions burn in word by word.
- 0:03 "Two options. Simple choice.": Basic $8 and Premium $16 cards with feature lists; two progress bars "Choose Basic" / "Choose Premium" fill to 80% / 20% (passing 76% / 8%). "Makes sense, right?"
- 0:10 "Now add a third option...": the Pro $14 card fades in between them, framed in a danger tone with tag "← THE DECOY"; caption "Almost same price as Premium... but way fewer features". "Now watch what happens..."
- 0:19 "The Shift": three bars "Choose Basic / Choose Pro (decoy) / Choose Premium" animate from 80/0/20 to 20/20/60; pill "Premium jumps from 20% → 60%".
- 0:24 "It's everywhere.": three example strips stack in: The Economist, Apple iCloud, Netflix, each with the middle option marked DECOY and the top option marked TARGET.
- 0:29 "Your brain compares what's comparable": a two-column comparison Pro (THE DECOY) vs Premium (TARGET) fills row by row: Pages 15 vs Unlimited ✓, Support Email vs Priority ✓, Users 3 vs 10 ✓, Price $14 vs $16, "Only $2 more for way more value"; then "Pro vs Premium? Easy. Premium wins. Basic? Already forgotten."
- 0:37 End card "Next time you see 3 options... You'll know. Follow for more." with "+ Follow".

## Voice-over summary
- Opens by saying the three-plan table is not a real choice but the decoy effect.
- With two plans, Basic $8 and Premium $16, most people pick Basic.
- Adding Pro at $14, with fewer features than Premium at almost the same price, makes about 60% choose Premium.
- Claims The Economist, Apple and Netflix use it.
- The brain compares what is comparable: Pro versus Premium is easy, "$2 more, way more value", and Basic is forgotten.

## Notes for the skill
- Mechanism name: asymmetric dominance / decoy effect (Huber, Payne & Puto 1982; popularised by Ariely's Economist subscription example). The video's percentages are not the published ones (Ariely reported roughly 16% / 0% / 84% with the decoy vs 68% / 32% without); the video's numbers are illustrative.
- The video shows the decoy itself taking 20% of choices; in the classic effect the decoy is rarely chosen. Treat the bar chart as a cartoon, not evidence.
- The iCloud and Netflix tiers are labelled "decoy" by the video itself; that is the author's interpretation, not established fact.
- Pricing table implementation: use a real `<table>` (or an ARIA grid with row headers) for feature comparison so screen readers can read "Support: Email / Priority" per row; do not encode "better" with colour alone, add checkmarks or text ("Unlimited").
- Ethics and compliance: deliberately steering choice with non-viable options can fall under deceptive design rules (e.g. EU DSA Article 25, FTC guidance on dark patterns). A skill should recommend clear recommended-plan labelling and honest tiers, and flag pure decoys in reviews.
- The opening tiles contradict later frames (Pro "20 pages" vs "15 pages", Basic "Basic support" vs "Email support"); the later, longer-held values are used above.
