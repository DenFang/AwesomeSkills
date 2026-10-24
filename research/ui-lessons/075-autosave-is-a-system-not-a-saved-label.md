---
lesson: 075
kind: video
duration_s: 49
type: ui
category: forms
topic: autosave as a system (debounce, status states, offline queue, conflicts, exit guard)
sources: frames, voice-over, lesson notes
---

# Autosave is a system, not a "Saved" label

**Hook:** The indicator said "Saved", but the connection had dropped mid-word and the edits never left the tab.

## Main rule
Build autosave as five cooperating parts: a debounced write (one request after ~800 ms of typing silence), an honest status indicator driven by an explicit state machine (typing, saving, saved, offline, error), a local queue that replays offline edits oldest first, conflict handling that merges or warns instead of last-write-wins, and a `beforeunload` guard when unsaved work exists.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 800 ms | debounce window: silence after the last keystroke before one write fires | 0:04-0:12 on-screen counter "N / 800 ms" + voice + page ("roughly 800ms") |
| 50, 140, 230 ms then reset to 80 ms | counter climbing between keystrokes, resetting on each key ("keystroke → reset") | 0:03-0:06 on-screen |
| 6 keystrokes → 1 write | result of debouncing the word "agenda" | 0:11 on-screen ("writes: 1") |
| PATCH /docs/offsite · 200 OK | the single write request after the window closes | 0:11 on-screen ("Write accepted") |
| 5 states | Typing, Saving, Saved, Offline, Error (shown as "Couldn't save") | 0:13-0:21 on-screen + voice |
| 4 pending edits, badge 0→1→2→4 | offline queue counter badge | 0:22-0:26 on-screen |
| Synced 2/4, 3/4, queue badge 4→3→2→0 | draining progress, oldest first | 0:27-0:29 on-screen |
| "3 changes pending", "3 edits never left this tab" | honest offline copy replacing the false "Saved" | 0:02 on-screen |
| "2 unsaved changes" | badge shown before the tab-close guard | 0:39-0:44 on-screen |

## Before / after
- **False "Saved" vs honest pill.** Bad: the pill keeps saying "Saved" while the network is down; the footer still claims "Last sync 12:04 · up to date". Good: the pill switches to a pending state with a count ("3 changes pending") and the footer says the edits never left the tab. Why: users trust the indicator more than the feature itself, so a lying indicator converts a recoverable network blip into silent data loss.
- **Write on every keystroke vs debounce.** Bad: a request per key (6 requests for "agenda"), noisy and racy. Good: a timer that starts when typing pauses and resets on every key; after 800 ms of silence exactly one write fires. Why: fewer requests, no out-of-order partial saves, and the "Saving" state appears only once per burst instead of flickering.
- **Last write wins vs merge.** Bad: Tab A adds "Intro: goals for H2", Tab B adds "Budget: venue & travel"; both show "saved 14:05", but the server keeps only Tab B's line and Tab A's edit vanishes. Good: the server merges both lines (each tagged with its source tab), or warns the user. Why: both tabs reported success, so nobody notices the loss until much later.
- **Silent tab close vs guard.** Bad: closing the tab with "2 unsaved changes" just closes it. Good: the browser's native "Leave site? Changes you made may not be saved." dialog appears with Leave / Stay. Why: one interruption costs seconds; lost work costs an afternoon.

## Do
- Debounce saves: start/restart a timer on each input event, write once after ~800 ms of no input.
- Drive the status pill from an explicit state machine with five states: typing, saving, saved, offline, error; update it from real request outcomes.
- Show "Saved" only after the server confirms the write (e.g. 200 response).
- While offline, append every edit to a local queue and show a badge with the pending count.
- On reconnect, drain the queue in order, oldest first, and show progress (e.g. "Synced 3/4").
- Detect concurrent edits on the same document; merge them or warn the user.
- Register a `beforeunload` handler only while unsaved or queued changes exist.

## Don't
- Don't fire a network write on every keystroke.
- Don't show "Saved" (or "up to date") when the change never reached the server.
- Don't use silent last-write-wins for multi-tab or multi-user editing.
- Don't let a tab close on unsaved work without the confirmation dialog.

## Scene by scene
- 0:00 Notes document "Team offsite notes", pill "Saved" with a wifi icon, footer "Last sync 12:04 · up to date". Title "Saved." appears.
- 0:01 Wifi icon turns to "off", pill glitches, title adds "It wasn't."; document header flips from "editing" to "offline".
- 0:02 Pill becomes "3 changes pending" (warning colour), footer "3 edits never left this tab".
- 0:03 Section "Debounce: A timer between you and the server". Keystroke tiles appear one by one (a, g, e, n, d, a); a "Debounce window" bar counts 50 → 140 → 230 ms, then snaps back to 80 ms with "keystroke → reset". Server card: "waiting for silence…". Footer caption: "800 ms of silence → one clean write".
- 0:07 Typing stops; bar fills 170 → 500 → 800 / 800 ms; "writes: 1".
- 0:11 Badge "6 keystrokes → 1 write"; server card "Write accepted · PATCH /docs/offsite · 200 OK".
- 0:13 Section "Status: That pill is a state machine". Diagram with five nodes (Typing, Saving, Saved, Offline, Error); the pill above changes Typing… → Saving… (spinner) → Saved (check) → Offline (warning colour) → "Couldn't save" (danger colour) as a dot travels along the edges. Caption: "Users trust the pill. Never let it lie."
- 0:22 Section "Offline queue: Every edit waits in line". Pill "Offline", "Local queue" card fills with timestamped edits ("Renamed section 'Agenda'", "Added bullet · budget", "Fixed typo · 'Thursday'", "Pasted venue map link"); count badge 0 → 1 → 2 → 4. Server: "waiting for connection…".
- 0:27 Pill "Back online"; server "draining queue, oldest first"; top item removed first, "Synced 2/4", "Synced 3/4", badge to 0. Caption "Reconnect → drain in order. Oldest first."
- 0:30 Section "Conflicts: Two tabs. One document." Tab A and Tab B both edit offsite.md and both show "saved 14:05". Server card tagged "Last write wins": Tab A's line appears, then is replaced by Tab B's line.
- 0:35 Server tag switches to "Merge"; both lines present, each labelled "from Tab A" / "from Tab B". Caption "Merge or warn, never overwrite in silence."
- 0:39 Section "Navigation guard: The browser asks first". Browser tab with "2 unsaved changes" badge; cursor clicks the tab's close button; code chip `window.addEventListener("beforeunload", warn)`.
- 0:40 Native-style dialog "Leave site? Changes you made may not be saved." with Leave / Stay; cursor clicks Stay. Caption "One ugly dialog beats an afternoon retyped."
- 0:44 Single "Saved" pill, then end card "Autosave is a system." with the list "Debounce · States · Queue · Merge · Guard", a mini state flow Typing → Saving → Saved, and a follow CTA ("Now save this one manually").

## Voice-over summary
- Opens on the false "Saved": the connection died mid-word and nothing was actually stored.
- Explains debounce: the timer starts on pause and resets on typing; 800 ms of silence produces one clean write.
- Calls the status pill a state machine with five states and stresses it must never lie, since users trust it more than the feature.
- Offline edits go into a local queue with a pending-count badge; on reconnect it drains in order, oldest first.
- Two tabs on one document with last write wins means someone loses an hour; merge or warn, never overwrite silently.
- Closing with unsaved work should trigger the browser's leave prompt; "one ugly dialogue beats an afternoon retyped."

## Notes for the skill
- State names to use in code: `typing | saving | saved | offline | error`. Transitions shown: typing → saving → saved; any → offline on network loss; offline → error / saving on retry. Treat "saved" as only reachable from a confirmed server response.
- Debounce implementation: clear and restart a timeout on every `input` event; on fire, send one PATCH. Consider a max-wait (flush every few seconds during continuous typing) so a long uninterrupted typing burst is not left unsaved; the video does not cover this.
- Offline queue: persist it (IndexedDB/localStorage), not just memory, so a reload does not drop it; replay FIFO; listen to `online`/`offline` events but also treat failed requests as offline, since `navigator.onLine` can be wrong.
- Conflicts: use a version/ETag on each write (`If-Match`) so the server can reject stale writes; then merge (CRDT/OT or line-level) or show a conflict warning. Tagging merged changes by source helps the user verify.
- `beforeunload`: modern browsers ignore custom text and always show their own generic message; call `event.preventDefault()` (and set `returnValue` for older browsers). Add the listener only while dirty, because a permanent listener can disable the back/forward cache. It does not fire for in-app (SPA) route changes; guard those in the router separately.
- Accessibility: announce status changes politely (`role="status"` / `aria-live="polite"`) and avoid announcing every "Typing…" flip; announce "Couldn't save" assertively or with a visible retry. Do not rely on colour alone: each state in the video pairs an icon and a word (pencil, spinner, check, crossed wifi, alert).
- Spinner on "Saving…" should respect `prefers-reduced-motion` (swap to a static icon or text).
