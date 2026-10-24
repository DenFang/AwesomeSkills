---
id: DaclzgJNUeQ
reel_url: https://www.instagram.com/reel/DaclzgJNUeQ/
pattern_page: https://designmotionhq.com/patterns/optimistic-ui
date: 2026-07-06
duration_s: 55
type: ui
category: feedback
topic: optimistic UI (render success first, reconcile, roll back on failure)
sources: frames, voice-over, pattern page
---

# Optimistic UI: update first, sync after, roll back on failure

**Caption:** not captured yet
**Hook:** Two like buttons on the same network: one waits for the server and feels slow, the other updates immediately and feels instant.

## Main rule
For reversible, low-stakes actions (like, follow, save, bookmark, reorder), render the successful result immediately, send the request in the background, and if it fails roll the UI back to the previous state with a clear error message. Never do this for payments, transfers, deletes or anything that cannot be undone; show the real pending state for those.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 0.8 s | wait before the pessimistic like updates ("waits 0.8s") | 0:00-0:03 on-screen |
| 247 -> 248 | like count in both demo cards | 0:00-0:03 on-screen |
| 400 ms | claimed threshold below which a response reads as instant; above it a spinner reads as broken | 0:11-0:21 voice + gauge marker + page |
| 48, 49, 54, 45, 261 ms "feels instant"; 576, 720 ms "feels broken" | gauge needle values during the latency scene | 0:12-0:21 on-screen |
| 0-1000 ms | gauge scale (ticks at 200, 400, 600, 800) | 0:12-0:21 on-screen |
| 248 -> 247 | rollback of the like count after failure ("rolled back") | 0:24-0:30 on-screen |
| 99% (counter animates from 40%) | "of the time the bet was correct" | 0:40-0:43 on-screen + voice |
| 3 steps | User acts (tap the like) -> Render now (assume success) -> Reconcile (server confirms) | 0:34-0:43 on-screen |
| 4 + 3 + 1 | optimistic OK: Like, Follow, Save, Bookmark; show the truth: Pay, Transfer, Delete; then a "Processing payment..." pending button | 0:44-0:50 on-screen |

## Before / after
1. **Pessimistic vs optimistic like (0:00-0:10).** Bad: tapping like shows a spinner in the heart for about 0.8 s and only then turns the heart on and increments 247 to 248. Good: heart and count change on tap ("instant"). A timeline diagram shows the slow path as "Client UI" idle with a "dead time" bar while the server works, and the fast path as Client UI updated at once with the server row showing "sync", then a check. Why: the user's action gets feedback within the same frame, so there is no dead time to interpret; network latency moves out of the interaction loop into the background.
2. **Perceived latency (0:11-0:21).** A gauge with a marker at 400 ms: low values are labelled "feels instant", values past the marker (576, 720) "feels broken"; chips "Under 400ms = reads as instant" and "Spinner = reads as broken"; caption "You're buying the feeling, not the speed." Why: perceived responsiveness depends on whether something changes right after the action, not on actual round-trip time.
3. **Failure path (0:22-0:30).** The liked card (248) gets an inline toast "Network error / Couldn't reach the server, reverting"; the heart empties, the count returns to 247, a "rolled back" tag and "248 -> 247" appear. Why: optimistic does not mean ignoring errors; the UI tells the truth quickly once the server disagrees, and the state returns to exactly what it was.
4. **Boundaries (0:44-0:50).** Two columns: "Optimistic OK" (Like, Follow, Save, Bookmark, each with a check) vs "Show the truth" (Pay, Transfer, Delete, each with an x). The Pay action is shown as a danger/emphasis button reading "Processing payment..." with a spinner. Why: for irreversible or financial actions a false success is far worse than a short honest wait; the user must not believe money moved or data is gone before it actually happened.

## Do
- Apply the state change locally on the input event, then fire the request.
- Keep the previous state (snapshot) so you can restore it exactly on failure.
- On failure, restore the snapshot and show a short, specific message near the control ("Couldn't reach the server, reverting"), ideally with retry.
- Reconcile with the server response when it arrives (server count may differ from the local +1).
- Limit optimism to reversible, low-stakes, high-success-rate actions: like, follow, save, bookmark, toggle, reorder.
- For payments, transfers and deletes show an explicit pending state ("Processing payment...") and only show success after the server confirms.

## Don't
- Don't block simple toggles on a server round trip with a spinner.
- Don't silently swallow a failed optimistic request and leave the UI showing a state the server rejected.
- Don't show a charge, booking, transfer or deletion as done before the server confirms.
- Don't use optimistic updates where failures are common or where a rollback would surprise or harm the user.

## Scene by scene
- 0:00 Label "Same tap. Same network."; two post cards with a heart and "247 likes". Cursor taps both: left shows a spinner and "waits 0.8s" before turning on, right turns on instantly ("instant"). Caption "One didn't wait."
- 0:03 "Update strategy / Who updates the screen first?": rows "Slow, wait for server" (Client UI with a growing "dead time" bar, Server busy) vs "Fast, update first, sync after" (Client UI heart fills immediately, Server shows "sync" then a check). Caption "Same network. One stopped waiting."
- 0:12 "Perceived latency / Your brain's cutoff is 400ms.": speedometer 0-1000 ms with a 400 ms marker; needle at 48, 49, 54, 45, 261 ("feels instant", chip "Under 400ms = reads as instant"), then 576 and 720 ("feels broken", chip "Spinner = reads as broken"). Caption "You're buying the feeling, not the speed."
- 0:23 "Failure path / And when the request fails?": liked card at 248, then a "Network error, couldn't reach the server, reverting" toast; heart empties, count 247, tag "rolled back", "248 -> 247". Caption "Bet on success. Handle the rare miss."
- 0:34 "Optimistic UI / Assume the happy path.": three-step flow User acts -> Render now -> Reconcile lights up in sequence; counter 40% -> 99% "of the time the bet was correct"; caption "...it was right anyway."
- 0:43 "Boundaries / But not everywhere.": column "Optimistic OK" (Like, Follow, Save, Bookmark) vs "Show the truth" (Pay, Transfer, Delete), then a "Processing payment..." button with spinner. Caption "Irreversible? Show the truth."
- 0:51 End card "Make it feel instant." with the liked card; follow / save call to action.

## Voice-over summary
- The slow version waits for the server before anything changes; the fast one updates the screen first and syncs in the background, on the same network.
- The narrator claims anything under 400 ms reads as instant and that past it a spinner reads as broken even when the system works; you are buying the feeling of speed.
- If the request fails, the optimistic version rolls back: the like undoes itself and the count returns.
- Optimistic UI is betting on success, not ignoring errors: assume the happy path, render it now, reconcile when the server replies; it is right about 99% of the time.
- Never fake a payment, a transfer or anything irreversible; show those the truth even if that truth is a spinner.

## Notes for the skill
- Implementation: React `useOptimistic` / TanStack Query `onMutate` (snapshot + set) / `onError` (restore) / `onSettled` (invalidate/refetch); SWR `optimisticData` + `rollbackOnError`. Keep an idempotency key or request id so rapid double toggles resolve to the final user intent (debounce or last-write-wins), not to a flicker.
- State naming: `idle -> optimistic (pending) -> confirmed | rolledBack`. Expose pending subtly if needed (e.g. reduced opacity on the counter) without blocking input.
- Accessibility: toggle buttons need `aria-pressed` that updates immediately with the optimistic state; announce rollbacks through a polite live region (`role="status"`) so screen-reader users learn the action did not stick. Error text should not rely on colour only.
- Rollback animation should be noticeable but brief; with `prefers-reduced-motion`, switch state without animation but keep the message.
- The 400 ms "instant" threshold is a simplification. It comes from the Doherty threshold (system response under ~400 ms keeps users productive). Classic HCI guidance (Card/Miller/Nielsen) is about 100 ms for a response to feel instantaneous, about 1 s to keep the flow of thought, and about 10 s to keep attention. For direct manipulation like a toggle, aim for visual feedback within ~100 ms; 400 ms is already perceptibly delayed.
- The "99% of the time" figure is illustrative, not measured; optimism is appropriate only when your actual failure rate for that action is very low.
- Delete is listed as "show the truth": a common alternative for reversible deletes is optimistic removal with an Undo toast and delayed commit; that is safe only when the delete is genuinely reversible until the timer ends.
