---
lesson: 041
kind: video
duration_s: 53
type: ui
category: feedback
topic: error states (type, recovery, severity-to-surface, copy, prevention)
sources: frames, voice-over, lesson notes
---

# Error states: five fixes

**Hook:** Error states are hurting users; five fixes follow, starting from a dead-end "Error 500 / An error occurred / OK" dialog.

## Main rule
Classify the error first (validation, network, server, permission), show it on the surface that
matches its severity (inline, toast/banner, full surface or modal), always give a recovery action,
write what happened and what happens next in plain words, and prevent field errors with live
validation before submit.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 5 | number of fixes/rules | 0:02 voice, 0:49 on-screen "5 rules" |
| 4 | error types: validation, network, server, permission | 0:04-0:13 on-screen "4 errors. 4 patterns." + voice |
| 500 | HTTP code in the bad example ("Error 500") | 0:00 on-screen, 0:11 "Don't show a 500 modal for a typo." |
| 3 | recovery elements: 1. Retry, 2. Escalate, 3. Explain | 0:20-0:21 on-screen tags |
| 30s | timeout stated in the "What happened?" details ("Network timed out after 30s.") | 0:19-0:21 on-screen |
| 3 tiers | severity scale: inline = recoverable, toast = transient, modal = blocking | 0:22-0:31 on-screen + voice |
| `0x80004005` | raw error code in the bad copy example | 0:32-0:36 on-screen |
| 5 seconds | reconnect countdown in the good copy example | 0:32 voice ("reconnecting in five seconds"); on screen the counter shows 3 then 1 |
| 80% | share of errors inline validation supposedly prevents | 0:39 voice, 0:46-0:48 on-screen; no source given; the page does not repeat the number |
| 8 characters | password rule "At least 8 characters" | 0:42-0:48 on-screen |
| 3 rules | password checklist: at least 8 characters, contains a number, contains a special char | 0:42-0:48 on-screen |

## Before / after
1. **Dead end vs recovery (opening).** Bad: a bright dialog "Error 500 / An error occurred. / OK".
   Good: "Lost connection. / We're trying to reconnect..." with a primary "Try again" and a secondary
   "Refresh page". Why: the good version names the problem in user terms, signals the system is
   already acting, and offers an action, so the user is not stuck. Caption: same error, better
   recovery.
2. **One pattern for all vs pattern per type.** Validation: small, inline, specific ("Email is
   invalid" under the field, field border in danger colour). Network: non-blocking, transient (an
   inline "No connection. Reconnecting..." strip with a spinner inside the content area). Server:
   full surface, blocking ("Something broke on our end." + "Try again"). Permission: gated, requires
   action ("You don't have access." + "Sign in" link over a dimmed area). Why: each type has a
   different cause and remedy; a 500-style modal for a typo over-alarms and blocks for no reason.
3. **"Something went wrong. / OK" vs actionable dialog.** Bad: OK is the only button. Good: "Try
   again" (primary) + "Contact support" (secondary) + an expandable "What happened?" block with
   technical detail ("Network timed out after 30s."). Why: retry handles transient failures,
   escalation handles persistent ones, explanation builds trust and helps support.
4. **Surface by severity.** Inline on a sign-up form ("Email already in use") for recoverable
   errors; a toast "Connection lost. Reconnecting..." with a close button on an inbox for transient
   ones; a modal "Delete account? This can't be undone." (Cancel / Delete) for blocking moments. A
   low-to-high severity bar sits under the three. Why: interruption should be proportional to
   consequence; modals for minor issues train users to dismiss without reading. Voice: most apps
   overuse modals.
5. **Machine copy vs human copy.** Bad: "An error occurred. Code: 0x80004005" (struck through).
   Good: "Lost connection" with "Reconnecting in N seconds..." and a spinner. Why: the user learns
   what broke, that the system is handling it, and when to expect recovery.
6. **Validate after submit vs live.** Bad ("After submit"): the user types "password", presses Sign
   up, then sees "Password must contain a number". Good ("Live validation"): a 3-item requirement
   checklist under the password field ticks each rule as it is met; Sign up stays disabled until all
   three pass, then the field gets a success border and the button becomes active. Why: requirements
   are visible before the mistake, feedback is immediate and positive, so the error never happens.
   Caption: prevent, don't catch.

## Do
- Decide the error type first, then choose the pattern for it.
- Put field validation errors directly under the field, short and specific.
- Show network problems without blocking the page, and say that reconnection is in progress.
- Give every error at least one way out: retry, refresh, sign in, or contact support.
- Offer optional technical details ("What happened?") below the main message.
- Match the surface to severity: inline for recoverable, toast/banner for transient, modal only for blocking.
- Write messages that say what happened and what happens next, with timing if known.
- Show input requirements up front and tick them live as the user types.

## Don't
- Don't show a full-screen or modal 500-style error for a validation typo.
- Don't ship an error whose only action is "OK".
- Don't surface raw codes ("0x80004005", "Error 500") or "An error occurred" as the message.
- Don't validate only on submit when the rules can be checked earlier.

## Scene by scene
- 0:00 Bad dialog "Error 500 / An error occurred. / OK" (bright card) above a good dark card "Lost connection. We're trying to reconnect..." with "Try again" (primary, retry icon) and "Refresh page".
- 0:01 Bad card dims; good card gains a danger-colour glow.
- 0:03 Caption "Same error. Better recovery."
- 0:04 Title "4 errors. 4 patterns. Match the error to its surface." and a 2x2 grid builds.
- 0:05 Grid: VALIDATION (email field "thibault@grouet", "Email is invalid", note "small. inline. specific."), NETWORK (inline strip "No connection. Reconnecting..." with spinner, "non-blocking. transient."), SERVER ("Something broke on our end.", "Try again", "full surface. blocking."), PERMISSION ("You don't have access.", "Sign in" link, "gated. requires action.").
- 0:12 Caption "Don't show a 500 modal for a typo."
- 0:14 Section "Recovery / Every error needs an exit.": dialog "Something went wrong." with only "OK".
- 0:16 Label "Add recovery actions" points at the dialog; OK fades out.
- 0:18 Buttons "Try again" + "Contact support" appear.
- 0:19 Details block "WHAT HAPPENED? Network timed out after 30s." (monospace).
- 0:20 Tags "1. RETRY", "2. ESCALATE"; 0:21 "3. EXPLAIN" and caption "Always offer a way out."
- 0:22 Section "Hierarchy / Severity → Surface."
- 0:23 Phone 1 "INLINE / RECOVERABLE": sign-up form, email field in error, "Email already in use".
- 0:24 Phone 2 "TOAST / TRANSIENT": inbox with a toast "Connection lost. Reconnecting..." and close icon at the bottom.
- 0:25 Phone 3 "MODAL / BLOCKING": dimmed settings with dialog "Delete account? This can't be undone." Cancel / Delete (danger).
- 0:27 Gradient bar "LOW SEVERITY → HIGH SEVERITY" under the phones; toast re-pulses.
- 0:30 Caption "Most apps overuse modals."
- 0:32 Section "Copy / Words do most of the work.": card "An error occurred. Code: 0x80004005" in muted neutral text.
- 0:35 The copy is struck through and removed.
- 0:37 New copy typed: "Lost connection", "Reconnecting in 3 seconds..." then "1 seconds..." with spinner; icon in danger colour.
- 0:39 Caption "Humans read humans."
- 0:40 Section "Prevention / Inline validation kills __ of errors.": "AFTER SUBMIT" form (Email, Password "password", Sign up).
- 0:42 After-submit form shows "Password must contain a number" below the button; "LIVE VALIDATION" form appears with empty checklist and disabled Sign up.
- 0:43 Typing: "At least 8 characters" ticks; 0:45 "Contains a number" ticks.
- 0:46 "Contains a special char" ticks, field border turns success colour, Sign up enables; headline fills in "80%".
- 0:48 Caption "Prevent. Don't catch."
- 0:49 "5 RULES" checklist: Match the type to the surface; Always offer a way out; Severity drives surface; Write copy for humans; Prevent with live validation.

## Voice-over summary
- Type the error first: validation, network, server and permission each need a different visual pattern; no 500 modal for a typo.
- Every error needs a way out (retry, refresh, contact us); a dead end is the worst experience to ship.
- Severity decides the surface: inline for recoverable, toast for transient, modal only when nothing else works; most apps overuse modals.
- Replace "an error occurred" with "lost connection, reconnecting in five seconds", because humans read human language, not machine output.
- Inline validation is claimed to prevent 80% of errors; disable submit until valid, show progress, catch problems early.

## Notes for the skill
- ARIA: inline field errors use `aria-invalid="true"` and `aria-describedby` pointing at the message; announce submit-time error summaries with `role="alert"`; connection status with `role="status"`/`aria-live="polite"`. Do not announce a countdown every second; announce the state change and the final result.
- Don't convey error only by border colour (WCAG 1.4.1); include an icon and text. Danger text on dark surfaces still needs 4.5:1 contrast.
- Toasts for errors are risky: they auto-dismiss and are easy to miss, and timed content conflicts with WCAG 2.2.1 unless the user can extend it. Use a toast only for transient issues that resolve themselves; keep persistent errors inline or in a banner until fixed.
- The "blocking modal" example in the video is a destructive-action confirmation ("Delete account?"), not an error. Treat it as "use a modal only when the user must decide before continuing"; a real blocking failure (server down, no permission) is better as a full-page/section state with retry or sign-in.
- "Disable submit until valid" is contested: a disabled button is skipped by keyboard focus and gives no reason why it is disabled. Safer rule: show requirements up front and validate live, but keep submit enabled and, on submit, focus the first invalid field with a summary (GOV.UK / Nielsen Norman guidance).
- Live validation timing: tick positive requirements while typing, but show negative error messages on blur or submit, not on the first keystroke (premature errors feel like scolding).
- Demo inconsistency: at 0:43 the field shows 3 masked characters yet "At least 8 characters" is already ticked; implement the check against real length.
- The 80% figure is unsourced; do not repeat it as a fact.
- State names worth modelling: `idle | validating | invalid | valid` per field; `offline | reconnecting(attempt, nextInMs) | restored | failed` for connection; error objects should carry `type` (validation/network/server/permission), `recoverable`, `actions[]`, and optional `details`.
