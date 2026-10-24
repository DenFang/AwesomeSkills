---
id: DXthiVKNCDd
reel_url: https://www.instagram.com/reel/DXthiVKNCDd/
pattern_page: https://designmotionhq.com/patterns/form-field-states
date: 2026-04-29
duration_s: 60
type: ui
category: forms
topic: the six states of a text field
sources: frames, voice-over, pattern page
---

# Six form field states

**Caption:** not captured yet
**Hook:** A text field has six states, and most apps only ship two of them.

## Main rule
Design and implement every text field with six explicit states: default (label outside, helper below), focus (ring with at least 3:1 contrast), error (colour + icon + message together), success (confirmed inside the field), disabled (flat greyscale fill, not-allowed cursor, not just 50% opacity), and loading (in-field spinner during async checks). A missing state shows up to users as a bug.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 6 states | default, focus, error, success, disabled, loading (counter "01/06" … "06/06") | whole video, on-screen + voice |
| "most apps ship two" | the claim in the hook | 0:02 on-screen + voice |
| 3:1 minimum | focus ring contrast against the background | 0:12-0:18 on-screen rule + voice + page |
| 4.6:1 ✓ | measured contrast of the demo focus ring | 0:12-0:18 on-screen badge |
| 12% of users | share of users the video/page says cannot perceive an error shown only by a danger-coloured border ("color vision deficiency") | 0:20-0:28 on-screen + voice + page ("~12%") |
| opacity 0.5 / 50% | the disabled styling to avoid ("looks like a loading state") | 0:37-0:44 on-screen + voice |
| cursor: not-allowed | disabled field cursor | 0:37-0:44 on-screen + voice |

## Before / after
- **Placeholder as label vs label outside.** Bad: the label lives in the placeholder and disappears as soon as the user types, so they lose the field's meaning mid-entry. Good: a persistent label above the field ("Email") and helper text below ("We'll never share your email"). Why: recognition over recall; the context stays visible during and after input.
- **Soft glow vs real focus ring.** Bad: a faint blurred glow that does not reach 3:1 against the background. Good: a solid ring meeting at least 3:1 (demo 4.6:1) plus a hint below ("Tab to confirm"). Why: keyboard and low-vision users must be able to find the active field.
- **Border-only danger colour vs colour + icon + message.** Bad: only the border turns to the danger colour. Good: danger border, an alert icon inside the field, and a specific message below ("Email format is invalid, check the @ symbol" for input "hello@@example"). Why: colour alone is not perceivable by users with colour-vision deficiency; the message says what is wrong and how to fix it.
- **Toast vs in-field success.** Bad: a toast elsewhere on screen that steals attention and vanishes before it is read. Good: a check icon inside the field, success border, and "Email available" below. Why: feedback appears where the user's attention already is.
- **Opacity 50% vs designed disabled.** Bad: fading the whole field to 50% opacity, which reads like a loading/transitional state. Good: a flat greyscale fill, muted label and value, not-allowed cursor, and a reason in the helper line ("Account locked, contact support"). Why: disabled and loading must look different, and the reason should be stated.
- **No loading state vs spinner.** Bad: no feedback during an async check, so users submit again (double submit). Good: spinner inside the field on the right, helper "Checking availability…", input blocked while the request is in flight.

## Do
- Put the label above the field and helper text below it; keep both visible while typing.
- Give focus a ring with at least 3:1 contrast against adjacent colours.
- Signal errors with three cues at once: danger colour, icon, and a written message naming the problem and the fix.
- Confirm success inside the field (icon + short text), not in a toast.
- Style disabled as a flat greyscale fill with `cursor: not-allowed` and say why it is disabled.
- Show an in-field spinner and status text ("Checking availability…") during async validation; block duplicate submission.
- Keep disabled and loading visually distinct.

## Don't
- Don't use the placeholder as the label.
- Don't rely on a soft low-contrast glow as the focus indicator.
- Don't signal an error with a danger-coloured border alone.
- Don't confirm field-level success with a toast.
- Don't fake disabled with `opacity: 0.5`.
- Don't ship async fields without a loading state.

## Scene by scene
- 0:00 Six email fields fly in and settle in a 2×3 grid showing all states (default, focus, error "Invalid email format", success "Looks good", disabled "frozen@locked.dev", loading with spinner). Badge "6 form states".
- 0:02 Caption "Most apps ship two."
- 0:03 "01/06 Default: At rest, anatomy of a field nobody is touching." Empty Email field, label above, helper "We'll never share your email". Rule chip "Label outside, helper below"; avoid chip "Placeholder-as-label vanishes when typing".
- 0:11 "02/06 Focus: In focus, the user is typing, make their target obvious." Field with accent ring, value "thibault@des", helper "Tab to confirm", badge "Contrast 4.6:1 ✓". Rule "Ring contrast 3:1 minimum"; avoid chip: a soft coloured glow fails accessibility.
- 0:19 "03/06 Error: Validation failed, be loud, clear, and accessible." Value "hello@@example", danger border, alert icon inside, message "Email format is invalid, check the @ symbol". Rule "Color + icon + message"; avoid chip: a border-only danger colour is "invisible to 12% of users".
- 0:30 "04/06 Success: It worked, confirm in-place, feedback lands where attention is." Value "thibault@designmotionhq.com", success border and check icon, "Email available". Rule "Confirm inside the field"; avoid "Toasts steal focus and disappear too fast".
- 0:36 "05/06 Disabled: Locked, visible to readers, untouchable to clicks." Dim greyscale field "frozen@locked.dev", helper "Account locked, contact support". Rule "Grayscale background + cursor not-allowed"; avoid "Opacity 0.5 looks like a loading state".
- 0:45 "06/06 Loading: Async in flight, disable input, show progress, prevent the double submit." Field with spinner on the right, helper "Checking availability…". Rule "Spinner inside + disable the input"; avoid "No loading state = double submit bug".
- 0:54 End card "6 states · 1 system. One forgotten = one bug." State chips appear one by one (Default, Focus, Error, Success, Disabled, Loading); save/follow CTA.

## Voice-over summary
- Six field states exist; most apps ship two.
- Default: label outside, helper below; a placeholder label disappears once typing starts.
- Focus: the ring needs 3:1 contrast; the common soft glow fails.
- Error needs colour shift, icon and message; the narrator says a danger-coloured border alone is invisible to 12% of users with colour-vision deficiency.
- Success shows a check inside the field, not a toast; disabled uses a greyscale background and not-allowed cursor instead of 50% opacity; loading puts a spinner inside and blocks input to stop double submits.
- "Six states, one forgotten equals one perceived bug."

## Notes for the skill
- Markup: `<label for>` always visible; helper and error text linked with `aria-describedby`; set `aria-invalid="true"` on error. Announce async results ("Email available", errors) via a polite live region so screen-reader users hear them.
- Focus: WCAG 2.1 SC 1.4.11 requires 3:1 for the focus indicator against adjacent colours; WCAG 2.2 SC 2.4.11/2.4.13 add "not obscured" and (AAA) a minimum area. Use `:focus-visible` with a solid outline/ring (e.g. 2px) plus offset rather than a blurred shadow only.
- Correction (12%): colour-vision deficiency affects about 8% of men and about 0.5% of women (roughly 4-5% of all users). "12% of users" is overstated; the rule (never colour alone, WCAG 1.4.1 Use of Color) is still correct.
- Correction (disabled + screen readers): a natively `disabled` input is removed from the tab order and is not submitted with the form; screen readers can still find it in browse mode. If the value must stay reachable and readable (as "visible to readers" implies), use `readonly` or `aria-disabled="true"` instead. Disabled text is exempt from WCAG 1.4.3, but keep it legible anyway and state the reason in the helper text.
- Correction (loading): disabling the input during an inline availability check interrupts users who are still typing and drops keyboard focus. Prefer: keep the field editable, show the spinner, debounce the check, ignore stale responses; block only the form submission (and the submit button's repeat clicks) while a request is pending. Hard-disabling fits the moment of form submit, not keystroke-level checks.
- Error timing: validate on blur or on submit, not on every keystroke, and clear the error as soon as input becomes valid (see the form-validation-timing pattern).
- Spinner should respect `prefers-reduced-motion` (static icon + text).
