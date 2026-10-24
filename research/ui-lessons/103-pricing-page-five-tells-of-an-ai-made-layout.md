---
lesson: 103
kind: video
duration_s: 76
type: ui
category: landing / pricing
topic: pricing page: five "AI-made" tells and their fixes (highlight, badge, feature diff, one primary CTA, savings in money)
sources: frames, voice-over
---

# Pricing page: five tells of an AI-made layout

**Hook:** Three identical tiers, a badge on each card and 12 checkmarks per card: five tells that the pricing section was generated, not designed.

## Main rule
A pricing section must make one recommendation: lift a single tier (usually the middle) and let the others recede, put the only badge and the only filled button on that tier, list per tier only what it adds over the previous one ("Everything in X, plus" and 3-4 items), and express the annual discount as an amount of money, with the monthly price struck through.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 3 tiers: Starter $19/mo, Team $49/mo, Business $129/mo | demo pricing ("Lumen", "Simple pricing for growing teams / No setup fee. Cancel anytime.") | 0:00-0:47 on-screen |
| 5 tells | 1 three identical cards, 2 badge on all 3, 3 twelve checks, 4 three gradients, 5 percent off | 0:00-0:06 on-screen annotations + voice |
| 1 highlight · 2 quiet | tier emphasis rule | 0:07-0:16 on-screen chip |
| 3 → 1 badges, "1 badge · 0 runner-up" | badge count after the fix | 0:17-0:26 on-screen |
| 12 lines per card → Starter 4, Team 3, Business 3 | feature list length before/after ("12 → 4", "12 → 3", "12 → 3") | 0:27-0:37 on-screen |
| 12 checkmarks | the repeated list the voice calls "a wall" | 0:00, 0:29 voice + on-screen "12 checks" |
| 3 lines | "Everything in Starter, plus" + 3 items (Multi-entity, Approval flows, Priority support) | 0:30-0:37 on-screen + voice ("in three lines") |
| 3 → 1 primary buttons, "1 filled · 2 outlined" | CTA rule | 0:38-0:47 on-screen |
| −17% | percent badge on the billing toggle (the bad version) | 0:00-0:52 on-screen |
| $49 × 12 = $588 · annual $490 · save $98 | savings calculation for Team | 0:49-0:59 on-screen (typed) |
| "Save $98 / year" | savings chip shown when Annual is selected | 0:53-1:00 on-screen + voice ("$98 off beats 17% off") |
| $16 / $41 / $108 per month, billed annually; struck $19 / $49 / $129 | annual prices with the monthly price struck through | 0:54-1:00 on-screen |

Arithmetic note: $41 × 12 = $492, while the calculation says annual $490 (the true discounted rate is $40.83/mo). The $98 saving and the 17% ratio (490/588) are consistent; the displayed $41 is rounded.

## Before / after
- **Tell 1: three equal cards vs one lifted tier (0:07-0:16).** Bad: three identical light cards, equal weight ("flat", "equal"). Good: the Team card is raised, larger and on a brighter surface while Starter and Business recede onto a muted surface ("1 lifts, 2 step back"); Business is labelled "anchor" and makes Team "feel fair". Why: equal cards make no recommendation and force the user to compare everything; a single lifted card gives the eye a default, and a high-priced top tier works as a price anchor that makes the middle look reasonable.
- **Tell 2: "Popular" on every card vs one "Most popular" (0:17-0:26).** Bad: a "Popular" pill on all three tiers (3 badges). Good: only Team carries "Most popular"; the others get nothing, not a smaller badge (alternatives "Best value" / "Enterprise" are shown and struck as "runner-up badges"; annotation "nothing here", "silence"). Why: a label only signals when it is rare; badging everything cancels the signal.
- **Tell 3: 12 repeated checkmarks vs the diff (0:27-0:37).** Bad: each card lists the same 12 features ("a wall"). Good: Starter lists its 4 base features; Team says "Everything in Starter, plus" and 3 additions (Multi-entity, Approval flows, Priority support); Business says "Everything in Team, plus" and 3 additions (Dedicated accountant, Custom roles, SSO and audit log) ("a comparison"). Why: users choose by differences; showing only what changes reduces reading by about two thirds and makes the upgrade reason explicit.
- **Tell 4: three gradient buttons vs one primary (0:38-0:47).** Bad: identical gradient "Get started" buttons on all three cards (`linear-gradient(...)` struck through). Good: one filled primary button on the pick ("Start with Team"), outlined secondary buttons on the rest ("Choose Starter", "Talk to sales"), each with a specific label. Why: one high-emphasis control per view gives the eye a single landing point; equal buttons compete.
- **Tell 5: percent vs money (0:48-1:00).** Bad: a "−17%" chip next to the Monthly/Annual toggle. Good: switching to Annual shows "Save $98 / year", the −17% chip is struck, prices roll down to $16 / $41 / $108 with the old monthly prices struck through and "billed annually" underneath. Why: nobody computes percentages at checkout; an absolute amount is concrete and immediately comparable, and the struck price shows the reference point.

## Do
- Emphasise exactly one tier (scale, elevation, brighter surface or accent border); keep the others visually quieter.
- Keep a higher top tier as an anchor next to the recommended one.
- Put a single badge ("Most popular") on the recommended tier only.
- Write tier features as increments: "Everything in [previous tier], plus" followed by 3-4 differentiators.
- Use one filled primary CTA (on the recommended tier) and outlined buttons for the rest; label CTAs by tier or action ("Start with Team", "Talk to sales").
- On the billing toggle, state the annual saving in currency ("Save $98 / year"), show the discounted monthly equivalent, strike the monthly price and say "billed annually".

## Don't
- Don't render three identical cards.
- Don't add consolation badges ("Best value", "Enterprise") to the other tiers.
- Don't repeat the full feature list with checkmarks on every card.
- Don't give every tier a gradient or filled button.
- Don't communicate the discount only as a percentage.

## Scene by scene
- 0:00 Label "DE-AI YOUR UI · EP. 03 · PRICING", title "Three tiers. Same card. AI made." A light pricing panel (brand "Lumen", "−17%" chip, Monthly/Annual toggle) with three identical cards, each with a "Popular" pill, 12 checked features and a gradient "Get started" button. Numbered annotations appear: 1 "3 identical cards", 2 "badge on all 3", 3 "12 checks", 4 "3 gradients", 5 "percent off", plus an "AI made" tag. A five-step tracker (tiers, badge, checks, buttons, toggle) sits underneath.
- 0:07 "TELL 01 · HIGHLIGHT / Only one tier gets the highlight." Bars under the cards read flat → equal; then Team lifts and the side cards dim ("picked" vs "quiet"); annotations "1 lifts, 2 step back", "anchor" on Business pointing to "feels fair" on Team. Chip "1 highlight · 2 quiet".
- 0:17 "TELL 02 · BADGE / A badge on every card is a badge on none." The three "Popular" pills disappear except Team, which becomes "Most popular"; 0:22 runner-up badges ("Best value", "Enterprise") flash on the side cards and get struck; annotations "nothing here", "silence"; counter badges 3 → 1. Chip "1 badge · 0 runner-up".
- 0:27 "TELL 03 · FEATURES / List what changes, not what repeats." Each card "12 lines"; Team's list collapses to "Everything in Starter, plus" + 3 items (12 → 10 → 3), then Business (12 → 3), then Starter (12 → 4). Labels "a wall" (struck) vs "a comparison". Chip "list the diff, not the set".
- 0:38 "TELL 04 · BUTTON / One primary button on the page." "3 gradients" annotation, `linear-gradient(...)` struck; 0:44 buttons become "Choose Starter" (outlined), "Start with Team" (filled, success/accent colour), "Talk to sales" (outlined); primary count 3 → 1; a cursor hovers the primary. Chip "1 filled · 2 outlined".
- 0:48 "TELL 05 · TOGGLE / Write the saving in money." Billing toggle card ("Switch anytime. Prorated on your next invoice.", chip "−17%"); a terminal line types "$49 × 12 = $588 · annual $490 · save $98". 0:53 the cursor clicks Annual: chip "Save $98 / year" appears, "−17%" is struck; prices roll to $16 / $41 / $108; 0:57 struck monthly prices and "billed annually" appear. Chip "$ not %".
- 1:01 "Five tells fixed. One tier that sells." checklist: Highlight, Badge, Features, Button, Toggle, over the fixed pricing panel.

## Voice-over summary
- Three identical tiers, a badge on each and 12 checkmarks are AI tells; five of them get fixed.
- Only one tier is highlighted: the middle lifts, the others step back, and the top tier exists to make the middle feel fair.
- "Most popular" goes on one tier; the rest get nothing, because the silence is what makes the label work.
- List what changes between tiers ("Everything in Starter, plus" in three lines) instead of 12 repeated checks.
- One primary button on the page: filled on the pick, outlined on the rest, instead of gradients everywhere.
- Annual toggle: write the saving in money ("$98 off beats 17% off"), keep the monthly price struck through.

## Notes for the skill
- Implementation: give the recommended card `data-recommended` and drive elevation, border and badge from it; keep the DOM order Starter → Team → Business so keyboard and screen-reader order matches the visual order (do not visually reorder with CSS `order`).
- Accessibility: the visual lift is not perceivable to screen readers; include "Most popular" or "Recommended" as text inside the card heading region. Struck-through prices need text equivalents (e.g. visually hidden "was $49 per month, now $41 per month billed annually"); `<s>` / `<del>` are not reliably announced. The Monthly/Annual control should be a radio group or a toggle button with `aria-pressed`, and price changes after toggling can be announced with a polite live region.
- Price roll animation on toggle: keep it short and use `tabular-nums` so the cards do not jitter; skip under reduced motion.
- Contrast: the "quiet" tiers sit on a muted surface with muted text; their prices and CTA labels still need 4.5:1 text contrast and outlined buttons need a 3:1 boundary.
- The middle-tier recommendation and the anchoring/decoy effect are well documented, but they are persuasion techniques: keep the recommendation honest (the tier that actually fits most users) and keep all features findable, e.g. a full comparison table below the cards for people who want the complete set.
- Rounding: make the displayed monthly equivalent and the stated yearly saving consistent (here $41 × 12 = $492 versus the $490 used for "save $98"); show "billed annually at $490" to avoid a mismatch at checkout.
