---
id: DcYUpuzthq-
reel_url: https://www.instagram.com/reel/DcYUpuzthq-/
pattern_page: none
date: 2026-08-23
duration_s: 45
type: ui
category: feedback
topic: preventing double submit on a critical (payment) button
sources: frames, voice-over, caption
---

# Double-submit prevention: one tap, one charge

**Caption:** Prevent double tap on your critical submit button.
**Hook:** The moment the pay button is tapped it disables itself; a slow network must never let the user buy twice.

## Main rule
On a critical submit (payment, order), lock the button on the first tap, show a spinner inside the same button with its width locked, guard the handler in code and send an idempotency key to the server, resolve to an explicit success check or an inline error, and re-enable only when the real request settles, never on a timer.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 1 intent -> 1 charge | goal: extra taps never reach the server | 0:07-0:09 on-screen card |
| slow · 3G; 0.0s -> 3.4s | simulated network, request in flight | 0:00-0:09 on-screen network panel |
| 2nd tap, 3rd tap "ignored" | extra taps while the request is in flight | 0:03-0:09 on-screen request log |
| layout shift +30px | button collapses to spinner width and content below moves | 0:11-0:17 on-screen (Reflows variant) |
| 0px · nothing moved | width-locked button with spinner | 0:11-0:17 on-screen (Locked variant) |
| jumps this session x2 vs x0 | count of layout jumps, reflow vs locked | 0:11-0:17 on-screen counters |
| charges captured 0 -> 1, stays 1 after 2nd tap and retry | client guard + server idempotency | 0:18-0:26 on-screen |
| `setTimeout(enable, 2000)` (timer 2.0s vs request 3.6s) | wrong re-enable: button live while charge still pending | 0:36-0:40 on-screen |
| `onSettled(() => enable())`, request 3.6s, enable "now" | correct re-enable on response | 0:36-0:40 on-screen |
| "a full beat" | how long the success check is held before navigating | 0:29 voice (no ms value given) |
| 5 rules | disable, spinner in place, guard + key, resolve, re-enable | 0:41-0:44 recap list 01-05 |
| $49.00, Visa •••• 0117 | demo checkout data (no rule meaning) | throughout |

## Before / after
- **Disable on first tap.** Bad (implied): a live button on a slow network lets repeated taps fire repeated POST /pay requests. Good: the first tap disables the button (a "disabled" tag appears); the request log shows one "POST /pay in flight" and the 2nd and 3rd taps marked "ignored". Why: on slow connections users re-tap because nothing seems to happen; each tap must not become a new charge.
- **Spinner in place, width locked (Reflows vs Locked).** Bad: the label is swapped for a spinner and the button shrinks to a small pill, the row below jumps (+30px, 2 jumps per session). Good: the spinner sits inside a full-width button whose size never changes (0px shift, 0 jumps). Why: layout shift reads as something broken and can move other targets under the user's finger.
- **Guard the handler + idempotency key.** Bad: relying only on the disabled UI. Good: client code `if (inFlight) return; inFlight = true; fetch('/pay', { headers: { 'Idempotency-Key': key } })`; a 2nd tap hits the guard and returns; a network retry reaches the server with the same key and the server returns the same charge ("key seen? -> return the same charge"); charges captured stays 1. Why: a disabled attribute does not stop programmatic calls, fast double events before re-render, or automatic retries; only the server can guarantee one charge.
- **Resolve to a check or an error.** Good success: the spinner morphs into a check mark, "Payment confirmed", then "moving you along -> Receipt". Good error: the button becomes an outlined danger-state "Card declined" with the message "Try another card, nothing was charged" directly below it. Why: the outcome appears where the user is looking; the error states the cause and reassures that no money moved.
- **Re-enable on the response, not a timer.** Bad: `setTimeout(enable, 2000)` re-enables "Pay $49" at 2.0s while the request still runs until 3.6s ("button live while the charge is still pending"). Good: `onSettled(() => enable())` re-enables exactly when the response lands at 3.6s ("enabled the instant the response lands"). Why: network latency is unknown; any fixed timer either re-opens the double-charge window or blocks the user too long.

## Do
- Set an in-flight state synchronously on the first tap and disable the submit control.
- Show progress inside the same button and lock its width and height.
- Guard the handler itself (`if (inFlight) return`) in addition to disabling the UI.
- Generate one idempotency key per user intent and reuse it on retries; dedupe on the server.
- On success, show a check for a noticeable moment before navigating.
- On error, restore the button and show the reason inline next to it, saying whether anything was charged.
- Re-enable only when the request settles (success or failure).

## Don't
- Don't let the button resize when its label becomes a spinner.
- Don't rely on the disabled attribute alone.
- Don't re-enable on a timeout or a guess.
- Don't move the spinner or error away from the button into a distant toast.
- Don't generate a new idempotency key for a retry of the same intent.

## Scene by scene
- 0:00 "State · Disable / One intent, one request." Phone checkout (Nordic Chair $49, Total $49.00, Visa •••• 0117) with a "Pay $49" button; side panels: Network "slow · 3G" with a request timer, and a Requests log.
- 0:01 Tap: the button shows a spinner and a "disabled" tag; log shows "POST /pay in flight"; timer counts 0.2s ... 3.4s.
- 0:03 Repeated taps: "2nd tap ignored", later "3rd tap ignored".
- 0:07 Card "1 intent -> 1 charge, extra taps never reach the server". Footer "Disable on the first tap."
- 0:10 "State · Spinner / Spinner in place, width locked." Two cards: "Reflows" (button collapses to a small spinner pill, dashed outline of the old size, "layout shift +30px", jumps x1 then x2) vs "Locked" (full-width button with centred spinner, "0px · nothing moved", jumps x0).
- 0:18 "State · Guard / UI off isn't enough. Guard it." Client code panel (pay.ts) with GUARD and KEY lines highlighted, server panel "Idempotency-Key: a3f81c…", counter "charges captured 0".
- 0:20 A POST /pay travels to the server; charges captured becomes 1. A "2nd tap -> return" chip stops at the client guard.
- 0:23 A "retry" chip reaches the server; "key seen? -> return the same charge" highlights; charges captured stays 1.
- 0:27 "State · Resolve / Land on a check or an error." Success card: spinner -> check, "Payment confirmed", "moving you along -> Receipt". Error card: outlined "Card declined" button with "Try another card, nothing was charged". The loop replays.
- 0:35 "State · Re-enable / On the response, not a timer." Top: `setTimeout(enable, 2000)` labelled GUESS, timer 2.0s vs request 3.6s, warning "button live while the charge is still pending". Bottom: `onSettled(() => enable())` labelled RESPONSE, enable "now" at 3.6s, "enabled the instant the response lands".
- 0:41 Recap "One tap, one charge.": 01 Disable on the first tap, 02 Spinner in place (lock the width, no layout shift), 03 Guard + idempotency key (client guard, server dedup), 04 Resolve to check or error (say why, right on the button), 05 Re-enable on the response (not a timer, not a guess). Footer designmotionhq.com.

## Voice-over summary
- The button disables itself instantly on tap; a slow network must not cause a second purchase.
- Swap the label for a spinner inside the same button with the width locked; "Layout shift reads as broken."
- Disabling the UI is not enough: guard the handler in code and give the server a real idempotency key.
- On success, morph the spinner into a check and hold it a full beat before moving on; on error, snap back and explain on the button.
- Re-enable only after the real request resolves, not on a timer or a guess.

## Notes for the skill
- State machine for the button: `idle -> submitting -> success | error -> idle`. Derive `disabled` and the label from this state; set it synchronously in the event handler (a ref or a module flag), not only through async state, so two events in the same frame cannot both pass.
- Width lock: reserve the widest content (min-width from the idle label, or render label and spinner stacked in one grid cell with the label `visibility: hidden` while loading). The reel shows a fixed full-width button.
- Accessibility: prefer `aria-disabled="true"` plus the handler guard over the native `disabled` attribute while submitting, so focus is not lost and screen readers still find the button; set `aria-busy="true"` and announce progress and the result through a polite live region ("Processing payment", "Payment confirmed", "Card declined"). Move focus to the error message or keep it on the button with the error referenced via `aria-describedby`.
- Error copy should state the cause and the money state ("nothing was charged"); keep the danger colour paired with an icon and text, not colour alone.
- "A full beat" for the success hold is not quantified in the reel; a few hundred ms up to about 1 s is common practice so the check is perceived before navigation.
- Idempotency keys are generated per intent (e.g. per checkout attempt), stored until the intent completes, and reused for automatic and manual retries of that same attempt; a new attempt after a decline gets a new key.
- Reduced motion: replace the spinner-to-check morph with an instant swap; keep the textual status.
