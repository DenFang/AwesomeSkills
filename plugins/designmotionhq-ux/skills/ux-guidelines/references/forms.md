# Forms and input

Forms are where users do work and where products lose them. Every field has states, every rule is visible before it is broken, and nothing the user typed is ever lost.

Severity: **P0** blocks, loses data or fails accessibility, **P1** friction, **P2** polish.

---

### FRM-1 · Six field states, designed explicitly (P1)
**Rule.** Every text field has default, focus, error, success, disabled and loading, each distinct by more than colour (icon, text, border weight). Focus ring at least 3:1 contrast. Error combines colour, icon and a message that says what is wrong and how to fix it. Success is confirmed inside the field. Disabled and loading look different: disabled is inert, loading shows an in-field spinner and blocks input.
**Detect.** Inputs with only default and error styles; error shown only as a red border; no focus style; disabled and loading sharing one look.
**Tip.** When the state already lives in the DOM, let CSS read it: `.field:has(:user-invalid)`, `form:has(:user-invalid) .submit-hint`.

### FRM-2 · Labels live outside the field (P0)
**Rule.** Every input has a persistent visible label (above or beside it) tied with `for`/`id` or wrapping. A placeholder is an example, not a label; it vanishes on typing. Helper text sits under the field and is linked with `aria-describedby`.
**Detect.** Inputs with `placeholder` but no `<label>`; labels not associated; floating labels that overlap typed text.

### FRM-3 · Validate on blur, then live (P1)
**Rule.** Do not validate on every keystroke (it flags words before they are finished) and do not wait for submit (a wall of errors after the fact). Validate a field when focus leaves it. Once a field has shown an error, switch that field to live validation so the error clears the moment it is fixed. Confirm correct fields too (a check). Exception: rule-based fields such as passwords show their checklist live while typing (FRM-5).
**Detect.** `onChange` validation showing errors from the first character; submit-only validation; errors that persist after the value is corrected.

### FRM-4 · Keep submit live; explain what blocks it (P0)
**Rule.** Do not grey out submit until the form is valid. Disabled buttons leave the tab order, cannot show a tooltip, usually fail contrast and never say why. Keep the button active, validate on click, highlight the blocking fields, move focus to the first one, and name the blocker in text. If a button must be unavailable, use `aria-disabled="true"` with a visible reason, not `disabled` with silence.
**Detect.** `disabled={!isValid}`; disabled buttons with tooltips that never fire; low-contrast disabled labels.

### FRM-5 · Password fields coach, never punish (P1)
**Rule.** Show the requirements before and during typing and tick each live. Score strength by length and entropy, not by a symbol checklist (a long passphrase beats `P@ss1`). Provide a show/hide toggle. Never block paste. Support password managers (`autocomplete="new-password"` / `current-password`) and offer a generated password where you can.
**Detect.** Rules shown only after a failed submit; `onPaste={e => e.preventDefault()}`; no reveal toggle; missing `autocomplete`.

### FRM-6 · Masked inputs format as you type and store raw (P1)
**Rule.** Group digits as the user types (card numbers in groups of four, phone numbers in the local pattern), keep the caret right after the character just typed, show the detected brand from the first digits, clean pasted values (strip spaces and dashes) instead of rejecting them, validate on blur, and store the unformatted value. Use the right keyboard: `inputmode="numeric"`, proper `autocomplete` (`cc-number`, `tel`).
**Detect.** Caret jumping to the end after formatting; paste rejected for spaces; formatted strings sent to the API.

### FRM-7 · One-time codes are one string (P1)
**Rule.** Model the code as a single string and render the boxes as a view of it. Paste anywhere fills all boxes (strip non-digits). Focus advances on each digit; backspace on an empty box moves back and clears. Use `inputmode="numeric"` and `autocomplete="one-time-code"`. Resend sits behind a visible countdown (about 30 s). On submit: a wrong code shakes, clears and refocuses; a right one locks into a verified state.
**Detect.** An array of six independent inputs with separate state; paste only filling the first box; resend with no cooldown.

### FRM-8 · Long forms become steps grouped by meaning (P1)
**Rule.** Past about seven fields, split into steps grouped by context (Personal, Shipping, Payment, Review), not by count. Show progress (bar, numbered steps or labels). Validate inside each step before Next. Persist entered data across Back, refresh and accidental close.
**Detect.** Twelve-plus field single-page forms; errors from step one only shown on the last step; state lost on Back or reload.

### FRM-9 · Group related fields with spacing (P2)
**Rule.** Tight spacing within a group (about 12 px between related fields), clearly larger gaps between groups (about 32 to 40 px). Spacing does the grouping; borders and dividers become optional.
**Detect.** Uniform gaps between every field; dividers used where space would do.

### FRM-10 · One tap, one request (P0 for payments and creates)
**Rule.** On the first tap, mark the button busy (spinner in place, `aria-busy="true"`, width locked so the layout does not shift) and ignore further taps with an in-flight guard. Send an idempotency key so the server de-duplicates retries. Resolve on the button itself: a check with a specific success, or an error that says what happened ("Card declined, nothing was charged"). Re-enable when the response lands, never on a timer.
**Detect.** Submit handlers without an in-flight flag; `setTimeout(() => setDisabled(false), 2000)`; buttons that shrink when the label becomes a spinner; payment endpoints without idempotency.

### FRM-11 · Autosave is a state machine (P0)
**Rule.** Debounce writes (about 800 ms after typing pauses), never per keystroke. Drive the status indicator from explicit states (editing, saving, saved, offline, error) and never show "Saved" before the write landed. Queue edits locally while offline and replay oldest first. Merge or warn on concurrent edits from two tabs or users; never overwrite silently. Use `beforeunload` when unsaved changes exist.
**Detect.** `onChange={save}` with no debounce; "Saved" set before the request resolves; no handling for offline or conflicts.

### FRM-12 · Settings match the apply model to the stakes (P1)
**Rule.** Low-risk toggles apply instantly with a quiet confirmation; identity and high-impact fields (email, password, billing) use explicit Save and Cancel. Group by user task, not by data model. Add search when there are many settings. Mark changed values and allow per-setting reset. Put advanced options behind a disclosure. Wall off destructive actions in a labelled danger zone at the bottom, gated by typing the resource name (see INT-9).
**Detect.** Mixed apply models with no indication; one long flat list ordered by schema; delete account as a single click.

### FRM-13 · Toggles look and behave like switches (P1)
**Rule.** A toggle is for an immediate on/off effect; use a checkbox when the change needs a Save. Proportions: rail about twice the knob, knob inset evenly. Rail colour, knob position, shadow and label change together over about 250 ms. Keyboard: Space toggles; visible focus ring; `role="switch"` with `aria-checked`. For async settings: flip immediately, show progress inside the knob, roll back with an explanation on failure. State is never shown by colour alone.
**Detect.** Toggles inside forms that also have a Save button; div-based switches without role or keyboard support.

### FRM-14 · Date pickers lead with presets (P1)
**Rule.** Offer one-click presets first (Today, Yesterday, Last 7 days, Last 30 days, This quarter), then a custom range: hover previews the range, first click sets start, second sets end, edges stay adjustable. Show two months side by side for ranges. Full keyboard support (arrows, Page Up/Down for months, typing the date, Enter, Escape). On mobile, a full-screen sheet with a large confirm button, not a tiny popover.
**Detect.** Range selection that needs many "next month" clicks; no typed entry; desktop popover reused on phones.

### FRM-15 · Sliders design around finger imprecision (P1)
**Rule.** Fill the track to the thumb so length shows the value, make the whole row the drag target, snap to steps when round values matter (with ticks), float the current value above the thumb while dragging, and support the keyboard (arrows, Home, End). For ranges, two thumbs with a filled band. Offer a number input next to it when exact values matter.
**Detect.** Bare 4 px tracks as the only hit area; free values like 47.3 where steps make sense; no keyboard.

### FRM-16 · File upload is five signals (P1)
**Rule.** The dropzone reacts while a file hovers (border, highlight, copy change). Progress is honest: percent, time left, ideally rate. A failure gets inline retry that resumes rather than restarts. Success shows proof: thumbnail, name, type and size. In a queue each file has its own row, progress and retry, so one failure never blocks the rest. Validate type and size before uploading and say the limits up front.
**Detect.** A bare `<input type="file">`; one spinner for a multi-file upload; failed uploads that must start over.

### FRM-17 · Inline editing keeps every pixel (P2)
**Rule.** Editable text hints its affordance on hover (subtle background or pencil). The input appears in exactly the same box with the same font, size and padding; only the border changes. Enter commits, Escape cancels, and blur follows one rule app-wide (save or discard; pick one). Save optimistically; on failure roll back, keep the draft, say why. Expensive edits get an explicit Edit action instead.
**Detect.** Edit modes that shift layout; inconsistent blur behaviour; lost drafts on error.

### FRM-18 · Button labels name the outcome (P1)
**Rule.** Labels say what the user gets or what will happen ("Create my account", "Send invoice", "Delete project"), not the mechanism ("Submit", "OK", "Yes"). See CON-1 for microcopy.

---
Sources: form-field-states, form-validation-timing, disabled-buttons, password-field-ux, input-masking, otp-input, stepper-wizard, proximity-rule, double-submit-guard, autosave-ux, settings-system, toggle-anatomy, date-pickers, range-sliders, file-upload-ux, drag-and-drop-tips, inline-editing, microcopy, css-has-selector. See `sources.md`.
