---
lesson: 011
kind: video
duration_s: 43
type: ui
category: content
topic: pricing card persuasion (anchoring, social proof, loss aversion)
sources: frames, voice-over
---

# Pricing card: anchoring, social proof, loss framing

**Hook:** Plain pricing cards "leave money on the table"; three psychology tricks on one card fix it.

## Main rule
On a pricing card, show a reference price before the actual price, mark the recommended tier with a
popularity badge plus real usage proof, and express the discount as a concrete amount the buyer keeps
(per year), not just a lower number. Only do this with truthful prices and real data.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| $49 struck through, then $29 /mo | anchor (reference) price vs actual price | 0:02-0:19 on-screen, voice at 0:12 |
| "Save 40%" | discount pill under the price (49 to 29 is about 40.8%) | 0:02-0:09 on-screen |
| "+2,847 chose Pro this month" | social-proof count under the tiers | 0:22-0:26 on-screen |
| "Save $240/year" | loss-framed saving (($49 - $29) x 12) | 0:29-0:37 on-screen |
| 40% | voice: "Save 40%" framed vs "pay less" | 0:29 voice |
| +30% conversions, 3 tricks, 0 extra effort | outro claim stats (unsourced) | 0:39-0:42 on-screen |
| "double the conversions" | voice claim (unsourced, conflicts with the +30% on screen) | 0:37 voice |

## Before / after
- **Plain card vs optimised card (0:00-0:09).** Before: "Pro Plan $29/mo", three features, outline
  "Get Started" button, no badge, no reference price. After: "MOST POPULAR" badge on top edge, struck
  $49 next to a large $29, "Save 40%" pill, four features, full-width filled primary CTA "Start Free
  Trial", highlighted border and glow. Why: the after card gives the eye a comparison point, a
  default choice signal and a strong single action, so the decision needs less effort.
- **Anchoring (0:10-0:19).** A muted $49/mo appears alone first, then is struck through as $29
  appears in display weight. Why: the first number seen becomes the reference; the real price is then
  judged as a gain against it ("Brain sees $49 first").
- **Social proof (0:20-0:26).** A three-tier row; the middle tier gets the "MOST POPULAR" badge, a
  "Safe choice" tag and an avatar row with "+2,847 chose Pro this month". Why: when unsure, people
  copy what others chose; the badge reduces decision paralysis by naming a default.
- **Loss aversion (0:27-0:37).** Left: "Pro Plan $29/month, just the price". Right: same plan with
  struck $49, "Save $240/year" pill, success-coloured border, "Don't lose this!" tag labelled "Fear
  of missing out". Why: a named amount that would be lost weighs more than an equal gain; an annual
  figure is larger and more concrete than a monthly delta.

## Do
- Show the reference price (struck through, muted, smaller) immediately before the actual price,
  which gets display weight.
- Highlight exactly one recommended tier among 3 (badge on the card edge, stronger border, the only
  filled primary CTA); keep other tiers' buttons secondary/outline.
- Back the badge with a real, specific number of customers and a time window.
- Express savings as a concrete currency amount per year next to the price.
- Use an action-specific CTA label ("Start Free Trial") instead of a generic "Get Started".

## Don't
- Don't leave every tier visually equal with no default.
- Don't show only a bare price with no comparison point.
- Don't invent a "was" price, fake counts or fake urgency (see notes).

## Scene by scene
- 0:00 Headline "Your pricing cards are leaving money on the table"; a plain card fades in next to an optimised card ("vs").
- 0:02 Plain card gets a red cross; optimised card glows.
- 0:03 Optimised card alone, centred: "Here are 3 secrets to fix it".
- 0:05 Callout labels appear around the card: "Anchoring" (price), "Social Proof" (badge), "Loss Aversion" (save pill).
- 0:10 "Secret #1 Anchoring Bias": muted "$49 /mo" box appears alone.
- 0:12 $49 gets struck through, "$29 /mo" appears; tag "Brain sees $49 first".
- 0:13 Caption: "$29 feels like a steal. Show the reference price first. The brain compares automatically."
- 0:21 "MOST POPULAR" badge drops onto Pro; "Safe choice" tag above.
- 0:22 Avatar row "+2,847 chose Pro this month".
- 0:23 Caption: "If everyone picks it, it must be good. The badge removes decision paralysis."
- 0:27 "Secret #3 Loss Aversion": "$29/month, just the price" arrow to a card with struck $49, $29.
- 0:29 "Save $240/year" pill and "Don't lose this!" warning tag; label "Fear of missing out".
- 0:31 Caption: "Losing $240 hurts more than saving $240 feels good. Frame the discount as a loss they'll avoid."
- 0:38 Outro: "Design psychology. Not harder work." stats "+30% conversions, 3 simple tricks, 0 extra effort", follow button.

## Voice-over summary
- Opening claim: pricing cards lose revenue; three psychological tricks fix it.
- Anchoring: show the high price first; $29 feels cheap after a crossed-out $49.
- Social proof: a "most popular" badge removes doubt because people follow the majority.
- Loss aversion: "save 40%" lands harder than "pay less"; frame the discount as money lost without it.
- Closes with "three tricks, one card, double the conversions" (unsupported).

## Notes for the skill
- Markup: put the struck reference price in `<del>` or `<s>` with visually hidden text ("Original
  price $49, now $29 per month"), because screen readers often do not announce strikethrough.
- Badge: render "Most popular" as text inside the card's accessible name or via `aria-describedby`,
  not only as a decorative pill; ensure the badge text meets 4.5:1 contrast on its fill.
- Recommended tier: the visual emphasis should be redundant with text, not colour or glow alone.
- Legal and ethical limits the video skips: a struck-through "was" price must be a real price that was
  actually charged (EU Omnibus Directive requires the lowest price of the prior 30 days; US FTC rules
  on former-price comparisons are similar). Social-proof counts must be real. "Don't lose this!" style
  urgency and fear framing drift into dark patterns (false urgency / confirmshaming); prefer a neutral
  "Save $240/year" label.
- The "+30% conversions" and "double the conversions" claims are unsourced and contradict each other;
  do not cite them as benchmarks.
- "Save 40%" is rounded down from 40.8%; always compute discount labels from the real prices.
