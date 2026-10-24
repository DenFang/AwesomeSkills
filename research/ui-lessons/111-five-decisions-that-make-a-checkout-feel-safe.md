---
lesson: 111
kind: video
duration_s: 53
type: ui
category: forms / checkout
topic: checkout that feels safe: sticky order summary, card brand on first digit, errors on blur, wallets first, one column with labels above
sources: frames, voice-over
---

# Five decisions that make a checkout feel safe

**Hook:** Why does Stripe Checkout feel trustworthy? The video reverse-engineers it into five layout and validation decisions.

## Main rule
In a payment form: keep the order summary and total visible beside the form and repeat the exact total on the pay button; recognise the card brand from the first digit (positive feedback early); validate a field only when the user leaves it (errors late); put one-tap wallets above all card fields; lay the form out in a single column with persistent labels above each field.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 5 decisions | summary visible, brand on type, errors on blur, wallets first, one column | 0:02 on-screen + voice; progress dots "decision 1/5 ... 5/5" |
| $148.00 | order total: Arc Desk Lamp (Brass · Qty 1) $148.00, Subtotal $148.00, Shipping Free, Total due $148.00 | 0:04-0:11 on-screen |
| Pay $148.00 | button amount equals order total ("same total", "Button amount = order total") | 0:08-0:11 on-screen + voice |
| `position: sticky` | order summary column | 0:04-0:11 on-screen |
| digits 0/16 → 12/16 → 16/16, errors: 0 | card number field state in the intro | 0:00-0:02 on-screen |
| 1st digit | brand recognition point ("brand: 1st digit", "validation: later") | 0:12-0:18 on-screen + voice |
| starts 4 → Visa, starts 5 → Mastercard, starts 3 → Amex | brand prefix mapping shown | 0:13-0:18 on-screen |
| on input (checks every keystroke) vs on blur (checks on leave) | validation timing comparison | 0:19-0:27 on-screen |
| "Your card number is invalid." (on input, bad) / "No error while typing" (on blur, good) / "Your card number is incomplete." (shown on blur) | error copy | 0:19-0:28 on-screen |
| 1 tap, no typing vs 6 fields before she can pay | wallet buttons vs card form | 0:29-0:35 on-screen |
| eye jumps: 4 → 7 vs eye path: 1 line | two-column grid vs single column | 0:37-0:45 on-screen |
| Card details are encrypted; Free returns within 30 days | trust lines under the total | 0:04-0:11 on-screen |

## Before / after
- **Summary scrolls away vs stays in view (0:04-0:11).** Good: a two-column layout with the order summary on the start side (`position: sticky`); as the user fills email, card, expiry, name and country, the summary does not move ("The form moves. The summary does not."). A dashed connector links "Total due $148.00" to the "Pay $148.00" button. Why: the user can verify what they are paying for at any moment, and the final click carries no surprise because the number on the button matches the summary.
- **Brand on first digit (0:12-0:18).** Typing "4" immediately shows the Visa mark in the field; a timeline shows brand recognition at the first digit and validation "later". Why: an early positive signal confirms the form understands the input ("Recognized first, judged later") and builds confidence before any judgement.
- **Errors on keystroke vs on blur (0:19-0:28).** Bad ("on input"): after typing "4242 42" the field turns danger-coloured with "Your card number is invalid." while the user is still typing. Good ("on blur"): no error while typing ("event: input · no error shown"); when focus moves to MM / YY the field validates ("event: blur · validate now") and shows "Your card number is incomplete."; completing the number turns it valid ("event: input · valid"). Why: flagging an unfinished value as an error punishes normal typing and creates anxiety; validating on leave judges only finished input.
- **Fields first vs wallets first (0:28-0:35).** Apple Pay and Google Pay buttons sit above "Or pay with card", annotated "1 tap, no typing" versus "6 fields before she can pay"; an arrow "skip typing". Tapping the wallet opens a payment sheet (Card Visa •••• 4242, Contact, Pay Fernwood Supply $148.00) that ends in "Paid". Why: the fastest path is the default; users with a wallet skip all typing, and others still see the card form below.
- **Two-column grid vs one column (0:36-0:45).** Bad ("BEFORE"): fields in a 2-column grid (email/phone, card/expiry, CVC/name, country/ZIP) with placeholder-only labels; the eye path zigzags ("eye jumps: 4" growing to 7), and once "Name on card" is typed the placeholder vanishes ("what was this?"). Good ("STRIPE-STYLE"): one column, labels above each field ("Cardholder name, still visible"); "eye path: 1 line". Why: a single vertical path removes scanning decisions, and persistent labels keep context after the field is filled.

## Do
- Show the order summary (items, subtotal, shipping, total) next to the form on desktop and keep it in view (`position: sticky`).
- Put the exact total on the pay button ("Pay $148.00") and keep it in sync with the summary.
- Detect and show the card brand as soon as the prefix allows (usually digit one).
- Validate on blur; once a field is in error, re-validate on input so the error clears as soon as the value becomes valid.
- Place wallet buttons (Apple Pay, Google Pay) above the card form, with an "Or pay with card" divider.
- Use a single-column layout, one field per row (closely related short fields like MM / YY and CVC may share a row).
- Keep visible labels above fields; never rely on placeholders as labels.
- Add short trust lines near the total (encryption, returns policy).

## Don't
- Don't show errors on every keystroke for a field the user is still typing.
- Don't let the price change or appear only at the final step.
- Don't bury wallets below the card fields.
- Don't arrange checkout fields in a zigzag multi-column grid.
- Don't use placeholder text as the only label.

## Scene by scene
- 0:00 Label "REVERSE-ENGINEERED · STRIPE CHECKOUT", title "Why does Stripe Checkout feel safe?", chip "Fernwood Supply $148.00 · Stripe-style checkout". A card number field fills: counters "digits 0/16 → 12/16 → 16/16", "brand: visa", "errors: 0", a check appears.
- 0:02 "Five decisions." Progress dots 1-5.
- 0:03 The full checkout panel (customer "Nora Bell"): Apple Pay, Google Pay, "Or pay with card", Email, Card information, MM / YY, CVC, Cardholder name, Country or region (United States, ZIP 94107), full-width "Pay $148.00" button with a lock icon.
- 0:04 "TEARDOWN · ORDER SUMMARY / The total stays in view." Two-column checkout: summary left ("Pay Fernwood Supply $148.00", item, subtotal, shipping Free, highlighted "Total due $148.00", trust lines, tag `position: sticky`); form right fills field by field. Caption "The form moves. The summary does not." 0:08 dashed line from the total to the Pay button, tag "same total"; caption "Button amount = order total".
- 0:12 "TEARDOWN · CARD BRAND / The card is recognized on digit one." Typing "4" shows the Visa badge; a timeline marks "brand: 1st digit" and "validation: later"; rows show prefixes 4 → Visa, 5 → Mastercard, 3 → Amex. 0:16 caption "Recognized first, judged later".
- 0:19 "TEARDOWN · ERRORS ON BLUR" with a title saying the error colour waits until she leaves the field. Two mini fields: "on input, checks every keystroke" (danger border, "Your card number is invalid.") vs "on blur, checks on leave" ("No error while typing"). Main field "4242 42" with "event: input · no error shown"; the label "error colour on keystroke" is struck.
- 0:25 Cursor clicks MM / YY: card field gets a danger border and "Your card number is incomplete.", "event: blur · validate now". 0:27 number completed: "event: input · valid".
- 0:28 "TEARDOWN · WALLETS FIRST / The fastest way to pay sits on top." Wallet buttons bracketed "1 tap, no typing" vs the form bracketed "6 fields before she can pay"; arrow "skip typing". 0:32 Apple Pay sheet slides up (Card Visa •••• 4242, Contact nora.b@example.com, Pay Fernwood Supply $148.00), 0:35 "Paid" with a check.
- 0:36 "TEARDOWN · ONE COLUMN / Eyes go straight down." "BEFORE" two-column grid with placeholder labels and a zigzag eye path ("eye jumps: 4", then 7) vs "STRIPE-STYLE" single column with labels above and a straight line ("eye path: 1 line"). 0:41 the name field is filled: before shows "what was this?", after shows "Cardholder name, still visible".

## Voice-over summary
- Stripe Checkout feels safe because of five decisions.
- While Nora buys a desk lamp the order summary stays beside the form, and the total on the button matches it, so nothing changes at the end.
- One digit in, the Visa logo appears: the form recognises her card before it ever says something is wrong.
- Halfway through the number nothing switches to the error state; the form waits until she leaves the field and only then flags missing digits.
- Apple Pay and Google Pay sit above every card field, so the fastest way to pay is the default.
- One column moves the eyes straight down, and labels above fields stay visible while she types.

## Notes for the skill
- Validation timing is the "reward early, punish late" pattern: validate on `blur` (or on submit) for an untouched field, then switch that field to validating on `input` once it has shown an error, so the error disappears the moment the value becomes valid. In the video the "incomplete" message is still visible on the frame where the number is complete and valid; do not leave stale error text.
- Error accessibility: link the message with `aria-describedby`, set `aria-invalid="true"` only after blur/submit, and do not rely on the danger colour alone (icon plus text, WCAG 1.4.1, 3.3.1). On submit with errors, move focus to the first invalid field or an error summary.
- Card brand detection: "starts 3 → Amex" is a simplification. Amex is 34/37; 3-prefixes also include Diners (36, 38, 300-305) and JCB (3528-3589); Mastercard is 51-55 and 2221-2720. Show a generic card icon until the prefix is unambiguous. Use `autocomplete="cc-number"`, `inputmode="numeric"`, `autocomplete="cc-exp"`, `cc-csc`, `cc-name`, `postal-code` so browsers and password managers can fill the form.
- Brand logo appearing in the field: give it a text alternative (e.g. visually hidden "Visa detected") or announce via a polite live region; a logo alone is invisible to screen readers.
- Sticky summary: on mobile, collapse the summary into an expandable bar at the top showing the total, since a side column does not fit; keep the total on the pay button in both layouts.
- Wallet buttons: render only when the device/browser supports them (Payment Request API / platform checks) and follow each wallet's branding guidelines; the remaining form must work fully without them.
- One column: labels above fields are also the most robust option for zoom and translation (long labels do not break a grid). Placeholders can supplement with format hints (e.g. "MM / YY"), never replace labels (WCAG 3.3.2).
- "4242 4242 4242 4242" is Stripe's published test card number; use it only in test mode.
