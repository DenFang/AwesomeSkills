---
lesson: 058
kind: video
duration_s: 54
type: ui
category: forms
topic: one-time code (OTP) input
sources: frames, voice-over, lesson notes
---

# OTP input: paste-first, auto-advance, one string, OS autofill, throttled resend, instant result

**Hook:** Paste a six-digit code and all six boxes fill themselves; an OTP field is a small system, not six separate inputs.

## Main rule
Model the code as one string rendered as six slots; on paste strip non-digits and distribute across all slots; auto-advance on each digit and step back on Backspace in an empty slot; set `inputmode="numeric"` and `autocomplete="one-time-code"`; gate Resend behind a visible 30 s countdown; on submit, a wrong code shakes, clears and refocuses slot 1, a right code locks all slots in the success state with a "Verified" label.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 6 digits / 6 boxes | code length | throughout |
| `value.replace(/\D/g, "")` -> 847291 | sanitising pasted text such as "847 291 04" | 0:04-0:11 on-screen code |
| "paste -> strip -> 6 boxes" | paste pipeline | 0:06-0:11 |
| digit entered -> focus next box; backspace on empty -> jump back | focus rules | 0:12-0:18 |
| `useState(["","","","","",""])` (struck out) vs `useState("847291")` | state model: 6 values vs 1 string | 0:20-0:26 |
| `inputmode="numeric"` | forces numeric keypad on mobile | 0:27-0:32 |
| `autocomplete="one-time-code"` | OS offers SMS code above the keyboard ("From Messages") | 0:30-0:32 |
| 30 s timer (0:30 counting down to 0:00) | Resend button disabled with "Resend in 0:SS" | 0:33-0:40 |
| 429 Too Many Requests | result of spam-clicking Resend without a timer ("server bans the user") | 0:34-0:40 |
| wrong code example 099999 | shake + error state + "Wrong code, shake & refocus" | 0:41-0:43 |
| "cleared -> focus box 1" | after wrong code | 0:43 |
| per-box check marks + "Verified" | right code | 0:44-0:49 |

## Before / after
- **One wide input vs six slots with paste handling.** Bad: a single plain input receives "847 291 04" with spaces and extra digits; it overflows and validation chokes. Good: strip non-digits, take the code length, fill all six slots in one go. Why: paste (from SMS, email, password manager) is the main path; the UI must normalise, not reject.
- **Manual focus vs auto-advance and back-step.** Good: typing a digit moves focus to the next slot; Backspace in an empty slot moves to the previous one and clears it. Why: hands never leave the keyboard; correcting a typo never traps the caret.
- **Six states vs one string.** Bad: an array of six independent values that must be kept in sync. Good: one string as the source of truth, each box a view of one character. Why: paste, delete, validation and submit operate on one value; fewer sync bugs.
- **Manual typing vs OS autofill.** Good: numeric keypad plus one-time-code autocomplete; the phone suggests the texted code and one tap fills all six. Why: zero typing, fewer errors.
- **Unthrottled vs timed resend.** Bad: Resend always active; impatient users hammer it, get 429 and are temporarily locked out. Good: after sending, Resend shows a 30 s countdown ring and re-enables at zero. Why: sets expectation and protects both user and server.
- **Silent fail vs instant feedback.** Bad: wrong code, nothing happens. Good: wrong code shakes, shows an error state and message, clears, focuses slot 1; right code shows checks on every box and "Verified". Why: immediate, unambiguous outcome.

## Do
- Store the code as a single string; render slots from it.
- Handle paste in any slot: `replace(/\D/g, "")`, slice to length, fill, focus last filled or submit.
- Auto-advance on input; Backspace on empty moves back and clears.
- Use `inputmode="numeric"` and `autocomplete="one-time-code"`.
- Disable Resend with a visible countdown (30 s in the video).
- Give an immediate, distinct wrong/right result.

## Don't
- Don't rely on one plain wide input without sanitising pasted text.
- Don't keep six unsynced pieces of state.
- Don't let Resend be spammed into a rate-limit ban.
- Don't leave a wrong code sitting with no feedback.

## Scene by scene
- 0:00 A clipboard chip with the code; six empty boxes fill digit by digit after paste. Overlay: paste once, six boxes fill themselves.
- 0:04 "The paste problem": a single red input "One input chokes" holding "847 291 04"; code line `value.replace(/\D/g, "") -> 847291`; six boxes fill; "paste -> strip -> 6 boxes"; "One paste, six boxes, done."
- 0:12 "Auto-advance": typing on an on-screen keypad moves the focused box right ("digit entered -> focus next box"); backspace moves it back ("backspace on empty -> jump back"), then re-typing.
- 0:19 "State architecture: Six inputs? One value.": boxes labelled input[0]..input[5] collapse into one string "847291" with lines to each box; array useState struck out, string useState kept.
- 0:27 "Mobile autofill": phone with numeric keypad, `inputmode="numeric"` tag; an SMS banner "Your code is 847291" arrives; a "From Messages" suggestion fills all boxes; `autocomplete="one-time-code"` tag.
- 0:33 "Resend, throttled: Lock resend behind a timer": "No timer" Resend button spam-clicked -> "429 Too Many Requests", "Spam-clicks -> server bans the user"; "30s timer" side shows disabled "Resend in 0:29 ... 0:00" with a progress ring, "Button re-enables when it hits zero". Footer: no throttle means users rate-limit themselves.
- 0:41 "Instant feedback": 099999 entered, boxes turn error state and shake, "Wrong code, shake & refocus", then cleared with focus on box 1; correct code fills with per-box checks and "Verified". Comparison chips "Silent fail: nothing happens" vs "Instant feedback: shake or success".
- 0:50 Outro: follow, save for your next auth flow.

## Voice-over summary
- Most inputs choke on a pasted code; strip spaces and drop one digit per box.
- Type a digit to jump forward, backspace on empty to jump back; hands never leave the keys.
- It looks like six inputs but it is one value split across six slots: "Track one string, not six states."
- On mobile force the number pad and let the phone autofill the texted code.
- Offer resend but lock it behind a 30-second timer, otherwise users rate-limit themselves.
- Wrong code shakes, clears and refocuses box one; right code locks every box in the success state; never fail silently.

## Notes for the skill
- Accessibility: six separate inputs need an overall label ("Verification code") and per-slot names ("Digit 1 of 6"), plus `aria-describedby` for errors. Many teams prefer one real `<input maxlength="6" autocomplete="one-time-code" inputmode="numeric">` visually split into slots (letter-spacing or overlay), which keeps native paste, autofill and screen reader behaviour simpler; either way, the single-string model applies.
- Put `autocomplete="one-time-code"` on the first (or only) input; iOS fills the whole code into it, so the paste-distribution logic must also run on regular input events with more than one character. Android/Chrome can also use the WebOTP API with a domain-bound SMS.
- `inputmode="numeric"` (not `type="number"`, which drops leading zeros and adds spinners); add `pattern="[0-9]*"`.
- Error feedback must not rely on shake or colour alone: show a text message and announce it (`role="alert"`); under `prefers-reduced-motion` replace the shake with a static error state. Clearing the boxes on error is one option; keeping the code selected for quick retype is an alternative.
- Countdown: announce the remaining time sparingly (not every second) and announce when Resend becomes available; the server must enforce its own rate limit regardless of the UI timer.
- Auto-submit when the 6th digit lands is common and fine; keep a visible submit button for assistive tech and slow connections, and disable inputs while verifying.
- Pasted "847 291 04" stripped gives 8 digits; the video shows 847291, so truncation to the code length is implied but not stated.
