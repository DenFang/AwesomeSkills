---
id: DYzSokhRAXG
reel_url: https://www.instagram.com/reel/DYzSokhRAXG/
pattern_page: https://designmotionhq.com/patterns/stepper-wizard
date: 2026-05-26
duration_s: 52
type: ui
category: forms
topic: multi-step form (stepper wizard)
sources: frames, voice-over, pattern page
---

# Stepper wizard: chunk a long form into steps

**Caption:** Wizard is the key for structured forms
**Hook:** Twelve fields make one wall; four steps make one path.

## Main rule
Split a long form into a few steps grouped by meaning (e.g. Personal, Shipping, Payment, Review), show one progress indicator, validate each step before allowing Next, and persist entered data on every step change so Back and refresh never lose it.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 12 fields | single-page "wall" checkout | 0:00-0:10 on-screen badge "12" / "12 fields" + voice |
| 4 steps | wizard length ("Step 1 of 4") | 0:00-0:52 on-screen + voice |
| 3 fields | amount read "without effort" ("Effortless, 3 fields") | 0:03-0:10 on-screen + voice |
| 4 x 3 fields | chunked layout: four steps of three fields | 0:05-0:10 on-screen |
| cognitive load 18% / 95% / 42% | meters under 3-field, 12-field and chunked forms | 0:05-0:10 on-screen (illustrative animation) |
| 3 indicator types | linear bar, numbered dots, step labels ("pick one") | 0:11-0:19 on-screen + voice |
| 0%, 8%, 24%, 41%, 57%, 76%, 99%, 100% | linear bar values animating through steps 1-4 | 0:12-0:19 on-screen (animation frames, not a rule) |
| 25% / 50% / 75% / 100% | bar value at steps 1-4 in the validation demo | 0:31-0:39 on-screen |
| 4 contexts | Personal, Shipping, Payment, Review | 0:20-0:29 on-screen + voice |

No timing values.

## Before / after
1. **Wall vs path (0:00-0:10).** Bad ("Fatigue, 12 fields"): a single Checkout card with first name, last name, email, phone, street, city, state, zip, card number... that scrolls. Good ("Chunked, 4 x 3 fields"): one step at a time with numbered dots and three fields (Address, City, Zip). A three-field card is labelled "Effortless". Why: a small visible chunk fits working memory and hides the remaining effort, so starting feels cheap; a long wall exposes total effort up front and causes scroll fatigue.
2. **Progress (0:11-0:19).** Three equivalent indicators advance together: a linear bar "Step N of 4" with a percentage, numbered dots that turn into ticks, and step labels Personal / Shipping / Payment / Review (completed ones ticked, current one highlighted). "Users need to feel the end is close." Why: showing position and remaining steps reduces uncertainty and motivates completion (goal-gradient).
3. **Boundaries by context (0:20-0:29).** Four cards appear: Personal (name, email, phone), Shipping (address, city, zip), Payment (card number, expiry, CVC), Review (summary rows with edit pencils and "Ready to submit"). "Each step earns its own screen. Random splits feel arbitrary." Why: steps that match a mental category feel coherent; splitting every N fields breaks related data apart.
4. **Validation timing (0:30-0:39).** Good ("Inline · instant"): on step 1 the email field shows "Enter a valid email address" and "Next is blocked until valid", Next disabled. Bad ("Final · too late"): the invalid email "not-an-email" passes with a tick, the user proceeds through Shipping (50%) and Payment (75%), and only at Review (100%) sees "Invalid format" and a banner "Email invalid on step 1, go back", with Submit disabled. Caption: an inline error beats final-screen rejection. Why: fixing an error in context is cheap; discovering it at the end forces backtracking and feels like rejection after the user thought they were done.
5. **State persistence (0:40-0:47).** Payment step filled (card, expiry, CVC). Pressing Back shows Shipping still filled; pressing Refresh restores Payment with all values and a "Data intact" badge; caption shows state saved to local storage ("localStorage.wizardState = { step, fields }"). "Lose the form once, you lose the user forever."

## Do
- Group steps by meaning (who you are, where to ship, how to pay, review), typically 3-5 steps.
- Show exactly one progress indicator style with the current step and total.
- Validate fields within the step; keep the user on the step (or block Next) until it is valid, and explain why Next is blocked.
- End with a Review step that summarises entries with edit links back to each step.
- Save state on every step change so Back, refresh and accidental navigation keep the data.

## Don't
- Don't put 12 fields in one scrolling wall when they can be chunked.
- Don't split steps by an arbitrary field count.
- Don't surface a step-1 error only on the final screen.
- Don't let Back or refresh wipe what the user typed.

## Scene by scene
- 0:00 Top: a 12-field "Wall" checkout card; bottom: "Path" card "Personal · Step 1, Step 1 of 4" with First name, Email, Phone and a Next button, progress filling 0% -> 25%; caption "Twelve fields, one wall. Four steps, one path."
- 0:03 "01 · Chunking": three cards "Effortless 3 fields", "Fatigue 12 fields", "Chunked 4 x 3 fields" with cognitive-load meters rising to 18%, 95%, 42%; "Chunking lowers cognitive load."
- 0:11 "02 · Progress", "Currently on Step 1/4": linear bar, numbered dots and step labels advance in sync to Step 4/4 and 100%; "Users need to feel the end is close."
- 0:20 "03 · Boundaries": Personal, Shipping, Payment, Review cards appear one by one; Review shows edit icons and "Ready to submit"; "Each step earns its own screen. Random splits feel arbitrary."
- 0:30 "04 · Validation": left "Inline · instant" (typing "not-an-email" triggers "Enter a valid email address", "Next is blocked until valid", helper "Validation runs as you type"); right "Final · too late" (same email accepted, user advances 25% -> 50% -> 75% -> 100%, then "Invalid format" and banner "Email invalid on step 1, go back"); Caption: an inline error beats final-screen rejection.
- 0:40 "05 · State": Payment step with Back and Refresh chips; Back shows Shipping still filled, Refresh returns to Payment with values intact ("Data intact"); note about saving to localStorage; "Lose the form once, you lose the user forever."
- 0:48 Outro: completed 4/4 stepper with all labels ticked; "Follow for more UX systems.", "Save this for your next signup flow."

## Voice-over summary
- 12 fields are a wall, 4 steps are a path; three fields read without effort, twelve in a row trigger scroll fatigue, and chunking lowers cognitive load.
- Progress shows where you are: linear bar, numbered dots or step labels; pick one, users need to feel the end is close.
- Group fields by context, not count: personal, shipping, payment, review; each step earns its own screen.
- Validate inside the step: a wrong email on step 1 should not surface on step 4; block Next when invalid.
- Save state on every step change; Back must preserve data and refresh too ("Lose the form once, you lose the user forever").

## Notes for the skill
- Security problem in the demo: it shows card number, expiry and CVC persisted to `localStorage`. Never store CVC anywhere (PCI DSS) and do not keep full card numbers in client storage; persist non-sensitive fields only (or use `sessionStorage` with the payment step excluded) and let the payment provider's fields handle card data. Also clear saved state after successful submit.
- Validation timing: the demo validates on every keystroke and shows an error while the user is still typing ("not-an"). Prefer validating on blur or on Next, then re-validate live once a field has been flagged. Disabling Next is debatable: a disabled button gives no explanation and is not focusable; many guidelines (e.g. GOV.UK) keep Next enabled and show the error summary on press. If you disable it, show the reason next to it, as the demo does ("Next is blocked until valid").
- Accessibility: render the stepper as an ordered list with `aria-current="step"` on the current item and text like "Step 2 of 4: Shipping"; move focus to the step heading on step change and announce it; link errors with `aria-describedby` and `aria-invalid`.
- Progress: one indicator is enough; the label variant is the most informative (users see what is left). Count steps honestly; if a step is conditional, update the total rather than jumping.
- Browser Back: map steps to URL state (`history.pushState` or route per step) so the browser Back button moves one step instead of leaving the wizard.
- The cognitive-load percentages and the "3 fields without effort" figure are illustrative, not research thresholds; working-memory limits (about 4 chunks) motivate the principle but do not define a field count. Short forms (under about 6 fields) are usually better as a single page.
