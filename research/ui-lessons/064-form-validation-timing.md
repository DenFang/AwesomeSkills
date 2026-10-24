---
lesson: 064
kind: video
duration_s: 50
type: ui
category: forms
topic: when to run inline form validation (blur first, live after an error, confirm success)
sources: frames, voice-over, lesson notes
---

# Form validation timing

**Hook:** The error message fires while the user is still typing their email.

## Main rule
Validate each field when focus leaves it (on blur). Once a field has shown an error, re-validate that field live on every change so the error clears the moment it is fixed. Confirm valid fields with a success mark instead of staying silent.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 10 fields | example of how many fields a user may fill "blind" with submit-only validation | voice 0:02-0:05 (the on-screen form has 5 fields) |
| 5 fields → 5 error states at once | submit-only demo (Full name, Email, Password, Country, Phone) | 0:03-0:10 on-screen |
| 2 → 3 → 4 "checks fired · 1 per key" | keystroke validation counter while typing "alex" | 0:13-0:20 on-screen |
| state chips `ON ERROR → LIVE` | per-field mode switch after a failed blur check | 0:30-0:38 on-screen |
| "Silence: feels judged" vs "Confirm: feels safe" | effect of showing or omitting success feedback | 0:40-0:46 on-screen |

No timing values (ms, debounce) are given in the video or on the page.

## Before / after
1. **On submit only (0:03-0:10), "Too late."** The user fills five fields, presses Submit, and every field turns to the error colour in a cascade with messages ("Required", "Invalid email", "Too short", "Invalid number"), while the button greys out. Why it fails: errors arrive after the user has mentally finished, all at once, often above the fold, so they must scroll back and hunt; the cost of each mistake grows with form length.
2. **On every keystroke (0:12-0:20), "Correct, but cruel."** After typing just "a", the field already shows "Invalid email"; the error stays through "al", "ale", "alex" with one check per key. Why it fails: the input is judged before the user has finished the thought, so a correct-but-incomplete value is labelled wrong, which feels like nagging and adds noise.
3. **On blur (0:21-0:28), "Check on blur."** The user types "alex@email.com" with a neutral focus ring and no messages; pressing Tab (a TAB key hint is shown) moves focus away, and only then the field shows a success border, a check icon and "Looks good". Why it works: feedback arrives right after the user has finished that field but before submit, when the context is still fresh.
4. **After an error, go live (0:29-0:38).** A field left as "alex@ema" shows "Invalid email". When the user returns and types, the field switches to live checking (chip `ON ERROR → LIVE`): the error disappears as soon as typing resumes, and at "alex@email.com" "Looks good" appears instantly. Why it works: the user does not have to blur or submit again to learn the correction worked; the error is forgiven at the moment of fixing.
5. **Confirm success (0:39-0:46).** Same valid email shown two ways: neutral field with no feedback ("Silence, feels judged") vs success border + check + "Looks good" ("Confirm, feels safe"). Why it works: positive confirmation closes the loop after effort and shows which fields are done.

## Do
- Validate a field on blur, after the user has moved on.
- After a field has errored, re-validate it on each input event and clear the message as soon as the value is valid.
- Confirm valid fields with a success mark and short text.
- Keep a neutral focus style while the user is typing a field that has not yet been checked.

## Don't
- Don't hold every error until submit and reveal them all at once.
- Don't show errors on each keystroke before the user has finished typing.
- Don't stay silent on correct fields while loudly flagging wrong ones.

## Scene by scene
- 0:00 Single Email field with focus ring; user types "alex".
- 0:01 Headline "Still typing. Already wrong?"; field shows "alex@ema" with error border, alert icon and "Invalid email"; caption "The timing is the whole thing."
- 0:03 Tag "On submit", headline "Errors all at once": form with Full name, Email, Password, Country, Phone and a Submit button; caption "Too late."
- 0:06 Submit is clicked; error states cascade down the form field by field; Submit goes to a muted disabled look.
- 0:11 Transition (blank frame).
- 0:12 Tag "On keystroke", headline "Wrong before they finish": "a" already flagged invalid; counter pill "2/3/4 checks fired · 1 per key"; caption "Correct, but cruel."
- 0:21 Tag "On blur", headline "Check when they leave": empty field, user types "alex@email.com" with neutral focus; TAB key hint; success border, check icon, "Looks good" and a check badge pop in; caption "Check on blur."
- 0:29 Tag "After an error", headline "Then escalate to live": "alex@ema" with "Invalid email"; user types, error clears immediately, chip `ON ERROR → LIVE`; "Looks good" appears at ".com"; caption "After an error, go live."
- 0:39 Tag "On success", headline "Confirm it, don't just flag wrong": neutral field next to "Silence / feels judged", then success state with "Confirm / feels safe"; caption "Confirm right, not only wrong."
- 0:47 Outro "Timing is the UX." with the valid field and a follow button.

## Voice-over summary
- Submit-only validation lets people fill many fields blind, then every field switches to the error state at once and they scroll up hunting for the problem.
- Keystroke validation punishes people mid-word: flagging an email as invalid after the first letter is "Technically correct. Completely cruel."
- Validate on blur: wait until they leave the field, when they have finished the thought, so feedback reads as help, not nagging.
- Once a field is wrong, switch that field to live and clear the error the instant it is fixed; do not make them submit again.
- A success check is feedback too; silence after effort feels like the form is judging the user.

## Notes for the skill
- This is the "reward early, punish late" pattern: errors appear late (blur), success and error-clearing appear early (live). Implement per-field state: `pristine → touched (blurred) → invalid (live mode) → valid`.
- Do not fire "Required" on blur when the user merely tabs through an empty field they have not typed in; reserve required-field errors for submit, or for blur after the field was changed.
- Submit validation is still required as a safety net: on submit, validate all fields, move focus to the first invalid field (or to an error summary at the top for long forms) and keep the button enabled.
- In live mode, clear errors immediately but avoid re-showing a new error on every keystroke while the user is still correcting; re-flag on the next blur.
- Accessibility: set `aria-invalid="true"` and connect messages with `aria-describedby`; do not announce live re-validation on every keystroke (no assertive live region per keypress); error and success must not rely on colour alone (icon + text, as shown); error text contrast at least 4.5:1.
- Success marks are most useful on fields with format rules (email, password, phone); for trivial fields they can add noise. Never show a success mark for values the client cannot truly verify (e.g. an email that will still be checked server-side) in a way that implies final acceptance.
- Demo flaw: in the submit-only scene the Full name field contains "Alex Carter" but still shows "Required", and Country ("France") gets an error border with no message. Do not copy that; each error must match the actual value and always carry a text message.
