---
lesson: 087
kind: video
duration_s: 48
type: ui
category: feedback
topic: copy-to-clipboard button
sources: frames, voice-over
---

# Copy-to-clipboard done right

**Hook:** One click, a check mark appears, and you paste nothing: the button claimed success that never happened.

## Main rule
A copy button must confirm only a copy that actually succeeded: swap the icon to a check on the same
frame the write resolves (no spinner), hold it about 2 s, then revert; copy the raw value, announce
"Copied" through a polite live region, and fall back (or report failure) when the Clipboard API is
blocked.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 0 bytes / received: 0 characters | failed copy shown as "Copied" (the lie) | 0:00-0:03 on-screen |
| 360 ms, 480 ms | spinner variant: wait before the check appears | 0:05-0:09 on-screen |
| 0 ms | instant variant: "confirms on the same frame" | 0:04-0:09 on-screen |
| ~2 s (voice "about two seconds") | how long the check is held before reverting | 0:09 voice, 0:10-0:17 on-screen |
| Holding 0.8 s, 1.8 s | countdown ring around the check during the hold | 0:11-0:12 on-screen |
| "Reset in 2s" vs "Stuck forever" | second copy: signals again vs no signal | 0:10-0:17 on-screen |
| aria-live="polite" | live region announcing "Copied to clipboard" | 0:28-0:35 on-screen |
| NotAllowedError | Clipboard API failure on an insecure origin (http) | 0:39-0:43 on-screen |
| execCommand('copy') | fallback path after the API is blocked | 0:37-0:43 on-screen |

## Before / after
- **Lying button (0:00-0:03).** Copy flips to "Copied", but the paste field shows "(nothing pasted)",
  "clipboard: 0 bytes", "You pasted nothing." Why it fails: the success state was set before (or
  regardless of) the clipboard write result, so the feedback is false.
- **Spinner vs instant (0:04-0:09).** Spinner card: a loader runs 360 to 480 ms, then the check
  ("waits, then confirms"). Instant card: the check appears at 0 ms ("confirms on the same frame").
  Why: a clipboard write is effectively instant; a spinner invents latency and makes a trivial action
  feel slow and uncertain.
- **Stuck forever vs reset in 2 s (0:10-0:17).** A ring counts down the hold ("Holding 0.8s, 1.8s"),
  the icon returns to "Reset", and a second click shows "Copied again". The "Stuck forever" row gives
  "no signal" on the 2nd copy; "Reset in 2s" "signals again". Why: if the check never reverts, the next
  click causes no visible change, so the user cannot tell whether the second copy happened.
- **Formatted span vs raw value (0:18-0:27).** Copying the visually wrapped span puts hidden
  characters into the clipboard (line break and an invisible character marked in the clipboard
  preview); the terminal shows "parse error: newline", tag "BREAKS". Copying the raw value pastes
  cleanly, "authenticated", tag "WORKS". Why: display formatting (wraps, zero-width joiners, thousands
  separators) is not part of the data.
- **Silent vs announced (0:28-0:35).** A plain `<div>Copied</div>` swap: screen reader "(silence)".
  With `aria-live="polite"`: the reader speaks "Copied to clipboard". Why: a visual icon swap produces
  no accessibility event; only a live region (or a status role) is announced.
- **No fallback vs fallback (0:36-0:43).** On an `http://` origin, `navigator.clipboard.writeText`
  throws NotAllowedError, 0 bytes copied, yet the button shows a check: "LIES". With `try { clipboard }
  catch { execCommand('copy') }`: "API blocked", "execCommand copied", tag "HONEST". Why: the async
  Clipboard API requires a secure context and permission; the success state must follow the real
  outcome.

## Do
- Set the copied state only after `await navigator.clipboard.writeText(value)` resolves (it resolves
  in well under a frame budget, so it still looks instant).
- Swap copy icon to check immediately, hold ~2 s, then revert to the copy icon (fade).
- Restart the 2 s timer on each new click so repeat copies always show feedback.
- Copy from a data attribute or the source string, not from rendered text.
- Announce the result via `role="status"` / `aria-live="polite"` ("Copied to clipboard").
- Catch failures: fall back to a hidden textarea + `document.execCommand('copy')`, and if that also
  fails, show an error state ("Couldn't copy, select and copy manually").

## Don't
- Don't show a spinner for a clipboard write.
- Don't leave the check permanently.
- Don't copy the formatted span with line breaks or zero-width characters.
- Don't show success when the API threw.

## Scene by scene
- 0:00 Browser card "API key" with a fake key and Copy button; below, "then paste it" and an empty paste field; badge "clipboard: 0 bytes".
- 0:01 Click: button turns "Copied" with a check.
- 0:02 Paste shows "(nothing pasted)", "received: 0 characters"; clipboard badge turns to danger colour.
- 0:03 Large text "You pasted nothing."
- 0:04 "Instant feedback: Flip the instant it fires." Two cards: Spinner and Instant.
- 0:05 Spinner counts 360 ms, then 480 ms before its check; Instant shows check at 0 ms; footer "Flip to a check instantly."
- 0:10 "Auto reset: Hold, then fade back." Icon labelled Ready.
- 0:11 Click: check with a circular countdown "Holding 0.8s", then "1.8s".
- 0:13 Icon reverts, label "Reset"; rows "Stuck forever, 2nd copy, no signal" vs "Reset in 2s, 2nd copy, signals again".
- 0:15 Second click: "Copied again". Footer "Reset after two seconds."
- 0:18 "Clean value: Copy the raw value." Formatted span (wrapped over two lines) vs raw value cards.
- 0:19 Formatted copy: clipboard preview shows marked hidden characters; terminal "parse error: newline", tag BREAKS.
- 0:22 Raw copy: clean clipboard, terminal "authenticated", tag WORKS.
- 0:28 "Screen readers: Say it out loud." Plain div Copied: screen reader "(silence)".
- 0:31 Button with aria-live="polite": reader types out "Copied to clipboard".
- 0:36 "Insecure origin: Fall back, don't lie." Two http:// cards, "No fallback" vs "With fallback".
- 0:38 No fallback: check shown, "0 bytes", "NotAllowedError", tag LIES.
- 0:42 With fallback: "API blocked", "execCommand copied", tag HONEST. Footer "Fall back, or the button lies."
- 0:44 Summary "Copy needs proof": 01 flip instantly, no spinner; 02 reset after two seconds; 03 copy the raw value; 04 announce via a live region; 05 fall back on insecure origins. Site link.

## Voice-over summary
- A check mark after an empty paste is a lie; the icon should flip the moment the copy fires, with no
  spinner or delay.
- Hold the check about two seconds then fade back; a stuck check makes the next copy silent.
- Copy the raw value, not the formatted span with line breaks and zero-width characters, or pasting
  into a terminal breaks.
- Icon changes are silent to screen readers; announce "copied" through a live region.
- On an insecure origin the clipboard call fails silently; fall back to the copy command. Closing
  line, paraphrased: a silent button lies.

## Notes for the skill
- States: `idle` -> `copied` (2 s, timer reset on re-click) -> `idle`; plus `error` (2 to 4 s, with
  a manual-copy hint). Keep the button width fixed so the "Copy"/"Copied" label swap does not shift
  layout; if icon-only, update `aria-label` too ("Copy API key" / "Copied").
- Live region: keep one persistent `role="status"` element in the DOM and change its text; a region
  inserted at the same moment as its content is often not announced. Clear it after the hold.
- `navigator.clipboard.writeText` needs a secure context (https or localhost), a user gesture, and in
  some browsers document focus; `document.execCommand('copy')` is deprecated but still the only
  synchronous fallback. If both fail, select the text so the user can press Ctrl/Cmd+C.
- Reduced motion: the icon swap can be instant; skip the fade and the countdown ring under
  `prefers-reduced-motion: reduce`.
- Secrets: for API keys, consider masking the display while still copying the full raw value, and
  never log the copied value.
- The "0 ms" is a simplification: the check should appear on the frame after the promise resolves,
  which is perceptually instant; showing it before the promise resolves recreates the lying button.
