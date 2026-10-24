# States and feedback

A component is not done when the happy path renders. Anything that fetches, submits or waits has states, and every one of them is designed on purpose. The user must always know what is happening, what happened, and what to do next.

Severity: **P0** breaks use, loses data or misleads, **P1** friction, **P2** polish.

---

### STA-1 · Cover every state the component can really be in (P0 when a missing state blanks the screen or hides a failure, P1 otherwise)
**Applies to.** anything that fetches, submits or waits.
**Rule.** Anything that fetches or submits has loading, empty, error and success. Add **partial** only when data comes from several sources, pages or a stream, and **offline** only when the product is meant to work without a connection. Do not add states a component cannot reach; that is weight, not completeness. Model the state explicitly (`status: 'loading' | 'empty' | 'error' | 'ready'`): a zero-length array is not "empty" while the request is still running or after it failed.
**Detect.** `data.map(...)` with no branch for `isLoading`, `error`, or `data.length === 0`; a fetch hook whose `error` is never read; screens that render nothing while loading.
**Fix.** Branch explicitly on each applicable state and mark the rest "n/a: reason" in the report.

### STA-2 · Pick the loading pattern from what you know about the wait (P1)
**Applies to.** anything that fetches, submits or waits: page and section loads, buttons that save or submit, uploads, exports, long-running jobs.
**Rule.**
| What you know | Pattern |
|---|---|
| Resolves under about 300 ms | Show nothing; a loader that blinks for 200 ms reads as a glitch |
| Layout shape is known, wait over about 300 ms | Skeleton that mirrors the final layout (STA-3) |
| Unknown length, short (one action, under about 3 s) | Spinner inside the control that triggered it ("Saving…" → "Saved", FRM-10), never a lone spinner over a page or panel |
| Measurable progress, over about 3 s | Determinate progress bar (STA-17) |
| Reversible, low-stakes action that almost always succeeds | Optimistic update (STA-4) |
A single default (skeleton everywhere, or a full-panel "Loading dashboard…" spinner with no context) is the tell of an unconsidered UI. Implement "show nothing" as a delayed indicator: render the loader only if the request is still pending after about 300 ms, and once shown keep it for at least about 400 ms so it does not flicker out. When progress is measurable, prefer the determinate bar even for shorter waits. Never put a spinner on top of a skeleton for the same region.
**Detect.** A global page spinner for content with a known shape; spinners for multi-second operations with known progress; `isLoading && <Spinner />` with no delay, so the loader appears instantly on every request.

### STA-3 · Skeletons match the real layout (P1)
**Applies to.** skeleton loaders and placeholder screens.
**Rule.** Shape each placeholder like what replaces it: a circle for an avatar, a short line for a name, long lines for body text, a block at the real aspect ratio for media, a row for actions. Use the same count, sizes, gaps and padding as the loaded content so it lands one to one with no layout shift (reserve media with `aspect-ratio`, match real line heights); equal generic bars are the cheap version. Tint placeholders one subtle surface step from the background, not high-contrast blocks. Animate a soft shimmer in reading direction (left to right, flipped under `:dir(rtl)`); under reduced motion keep a static placeholder or a very slow opacity pulse (MOT-13). Skip the skeleton for loads under about 300 ms (STA-2). Past about 2 s, render content progressively as it arrives rather than holding the whole skeleton, and add context ("Loading 1,247 records…"); past about 10 s, offer cancel. Set `aria-busy="true"` on the loading region, hide the shapes with `aria-hidden="true"`, give one text status ("Loading posts…"), and remove `aria-busy` when content arrives.
**Detect.** Generic skeleton reused for different layouts; skeleton count unrelated to page size; content shift (CLS) when data arrives; shimmer keyframes hard-coded left to right in an RTL-capable app; placeholder shapes exposed to screen readers or no `aria-busy` on the region.

### STA-4 · Optimistic UI for cheap, reversible actions only (P1)
**Applies to.** actions that change server data: like, follow, save, bookmark, toggle, reorder, rename, chat send; and payments, transfers and deletes, which must not be optimistic.
**Rule.** For reversible, low-stakes actions whose real failure rate is very low, apply the change in the same frame as the input, send the request in the background, and reconcile with the server's answer when it arrives (the server count may differ from the local +1). Snapshot the previous state first; on failure restore it exactly and say so next to the control ("Couldn't save your like. Try again") with retry, keeping any draft the user typed; a silent revert looks like a bug. Rapid repeated toggles settle on the user's last intent (request id or last write wins), never a flicker. Payments, transfers, irreversible actions and anything whose result the server decides (order IDs, prices, stock) show the truth: an explicit pending state ("Processing payment…") and success only after the server confirms. A reversible delete may disappear at once only behind an undo window (STA-14). Toggle buttons update `aria-pressed` with the optimistic state, and a rollback is announced in a polite live region.
**Detect.** Spinners on a like button; optimistic updates with no rollback path (TanStack `onMutate` without `onError`, `useOptimistic` or SWR `optimisticData` without an error path); a checkout that shows success before the server confirmed; client-computed totals trusted by the server.
**Fix.** Snapshot → apply locally → request → on error restore the snapshot and notify inline → on settle refetch or apply the server value. Server re-validates everything the client validated.

### STA-5 · Respond inside 400 ms (P1)
**Applies to.** anything that fetches, submits or navigates, and every press, tap or key that triggers it.
**Rule.** Acknowledge every press, tap or key within about 100 ms (pressed state, toggle flip), and make every request produce a visible response within about 400 ms (the Doherty threshold, beyond which attention drifts). Treat 400 ms as a ceiling, not a target: a toggle that answers at 400 ms already feels late. The work itself can take longer as long as the UI answers inside the threshold: a skeleton for screens that open (STA-3), an optimistic update for actions that almost always succeed (STA-4), determinate progress with named steps for long tasks (STA-17). Perceived speed can be improved without changing real speed: show the layout first, assume success where safe, and give a determinate bar visible movement from the start. Never let a shaped bar stall near the end (a late stall reads as stuck, and bars that speed up towards the end are judged faster), never show 100% before the work is done, and use an indeterminate indicator rather than an invented percentage when progress is unknown.
**Detect.** Actions with no visible reaction until the network returns; a like or toggle that waits for the response before changing; navigation that freezes the old screen while the next one loads.

### STA-6 · Empty states explain and lead (P1)
**Applies to.** lists, tables, feeds, search results, inboxes, task boards and dashboards that can have no items.
**Rule.** "No data", a blank body or a lone X is a failure, not an empty state. Each empty state says why it is empty and what to do next: one small icon or illustration matching the context (decorative, `aria-hidden`), a human headline that is a real heading, one sentence in product language (never log or status-code vocabulary such as "ERROR 404" or "Result set empty"; a successful empty response is not an error), and one primary action that actually fills the screen, optionally with a secondary text link ("or import from file"). Distinguish the kinds:
| Cause | Treatment |
|---|---|
| First use | Teach the feature with a ghost preview of a real item (visibly non-interactive, `aria-hidden`) and the create action; an inline drop zone also needs a file-picker button |
| No results for a search | Say what was searched, suggest other terms or popular items, offer "Clear search" |
| Filtered out | Name the filter, say how many items it hides ("42 items hidden by filters"), offer "Reset filters" |
| Load failed | An error, not emptiness (STA-7): "Retry" is the right primary action here |
| No access | Explain and say who can grant access |
| Done by design | Confirm it is good news ("All caught up") |
"Try refreshing" is wrong only when the list is legitimately empty. Show a skeleton, not the empty state, while loading. Announce a no-results change after searching or filtering through `aria-live="polite"`, and after "Clear search" or "Reset filters" move focus to the search input or the results.
**Detect.** Blank areas when arrays are empty; one generic "No items found" for every cause; empty states whose only action is "Refresh"; the empty state rendered from `items.length === 0` while `isLoading` or `error` is true.

### STA-7 · Errors say what happened and offer a way out (P0 when an error is swallowed or leaves no way out; P1 for generic copy with a retry)
**Applies to.** every error path (catch blocks, failed responses, error boundaries, connection and permission failures).
**Rule.** Classify the error first (validation, network, server, permission): each has its own cause, remedy and surface (STA-8). Copy names what failed in the user's terms, what the system is doing about it and when ("Lost connection. Reconnecting in 5 s…"), and what to do now. "Something went wrong", "An error occurred", "Error 500", raw codes such as `0x80004005` and raw `err.message` are bugs. Every error offers an exit: retry for transient failures, an escalation (contact support, sign in, request access) for persistent ones, and optionally a collapsed "What happened?" block with the technical detail; a lone "OK" is a dead end. The fallback for unknown errors is still specific to the component ("We couldn't load the invoices. Try again."). Pair the danger role with an icon and text, never colour alone. Prevent what you can before it happens: show input rules up front and tick them live (FRM-3, FRM-5), but keep submit active (FRM-4). Announce a reconnect countdown at the state change and at the result, not every second.
**Detect.** Generic error strings; `catch {}` that swallows; `alert(err)`; error screens with only "OK"; one error component for every failure with no notion of type.
**Fix.** Give error objects `type`, `recoverable`, `actions[]` and optional `details` so the UI can choose copy, surface and recovery.

### STA-8 · Put each error on the surface that fits its severity (P1)
**Applies to.** every error path.
**Rule.**
| Error | Surface |
|---|---|
| Field validation | Inline under the field, short and specific |
| Action finished but failed (save, send) | Inline on the item, or a toast with retry |
| Connection lost, degraded service | Non-blocking: a persistent banner or inline strip that says it is reconnecting |
| Server failure for a whole view | Section- or page-level replacement with retry |
| No permission | Gated view with the way in (sign in, request access, who to ask) |
| The user must decide before continuing | Modal (INT-3), and only then |
Interruption is proportional to consequence: never a 500-style modal for a typo, and most apps overuse modals. Never put an error that needs action in an auto-dismissing toast; keep error toasts for transient, self-resolving or background failures. A failed chat message stays in place marked "Not sent · Retry"; a failed upload keeps its row and its file and retries inline (STA-17, FRM-16).
**Detect.** Toasts for validation errors; modals for errors the user can fix inline; full-page errors for a single failed widget; partial failures that blank the whole screen.

### STA-9 · Partial data degrades gracefully (P1)
**Applies to.** views built from several requests, paginated or streamed data.
**Rule.** When part of the data fails, show what loaded and mark only the missing part ("Couldn't load. Retry"). When the next page loads, keep the current page visible and show loading at the edge. Never blank a screen that already had content.
**Detect.** One `error` flag for several independent requests; pagination that clears the list while fetching.

### STA-10 · Success is visible, specific and short-lived (P1)
**Applies to.** actions that change data.
**Rule.** Silence after an action is ambiguous. Confirm where the user is looking: a field check for inline edits, the changed data plus a short "Saved" for forms that stay, context on the destination page for forms that navigate ("Created John Smith"), a count for batch actions ("Suspended 12 users"), and an undo for destructive ones. No context-free "Success!", no permanent success banners.

### STA-11 · Toasts: position, timing, limits, dismissal, announcement (P1)
**Applies to.** toast and snackbar systems, including undo and error toasts.
**Rule.** Anchor bottom-right (or bottom-centre) on desktop and at the top on mobile, inside the safe-area insets (`env(safe-area-inset-*)`), or above the bottom navigation where that is the platform's convention; never over the centre of the content, where it hides the task and intercepts clicks. Time by severity: about 4 s info, about 7 s warning, errors stay until acknowledged; give longer text or an action button more time. Pause the timer on hover, on keyboard focus and while the tab is hidden. At most 3 visible: new toasts enter at one consistent edge, older ones move along, the oldest leaves, the rest queue first in first out, and identical messages merge into a counter. On the lively profile animate the reflow with a spring (about stiffness 180, damping 20, mass 1: slight overshoot, settled in about 0.4 s); the crisp profile and reduced motion use a short fade. Always dismissible: a close button with an accessible name ("Dismiss notification") and an INT-11 target, plus swipe on touch and Escape; swipe is never the only way. Show type by an icon plus an edge or border in that type's colour role, never tint or colour alone, and keep that edge or icon at 3:1 against the surface. Announce through a live region that exists before the first toast: `role="status"` for info and success, `role="alert"` only for errors. Never move focus into a toast; any action in it (Undo, Retry) is keyboard-reachable and also available elsewhere.
**Detect.** Centred toasts; one fixed timeout for all types; unbounded stacks; toasts with no close; toasts not announced, or a live region mounted together with the toast (the announcement is lost); timers that keep running on hover or focus; type shown only by background tint.

### STA-12 · Notifications: one message, four volumes (P1)
**Applies to.** products with more than one notification surface (toast, banner, modal or alert dialog, badge) and the service that routes them.
**Rule.** Severity picks the surface, and one event goes to exactly one surface; "Payment failed" as a banner, a toast and a modal at once is noise. **Toast** for low-priority, transient news (auto-dismisses after about 4 s, with undo where the action is reversible), **banner** for ongoing conditions such as degraded service or paused sync (stays until resolved or closed), **modal** only when the user must decide before continuing (an `alertdialog`, INT-3), **badge** for passive counts (stays until cleared, STA-13). Persistence is part of the contract: users learn what a surface means from how long it lives, so keep it consistent. Toasts may stack (STA-11); blocking dialogs never do: show pending decisions one at a time or merge them, and never render a second modal layer. Context can change the volume: a declined card is a modal inside the checkout the user just submitted, but a persistent banner with a fix action when a background renewal fails. Over-escalating trains people to ignore everything.
**Detect.** Modals for informational messages; stacked modals; banners for one-off events; one handler raising both a toast and a modal or banner for the same event.
**Fix.** Route every event through one notification service that maps severity to surface and owns queueing, dedupe and persistence.

### STA-13 · Badges count and clear (P2)
**Applies to.** count badges and unread indicators.
**Rule.** A badge is a count you clear, not a status. Cap at 99+ (9+ on very small badges). Pin it to the icon's top-end corner (icon wrapper `position: relative`; badge `position: absolute; top: 0; inset-inline-end: 0; translate: 50% -50%`, flipped to `-50% -50%` under `:dir(rtl)`, `min-width` equal to its height so one digit is a circle and more become a pill, tabular figures) so it grows outward and the icon, which is the tap target, never moves or pushes its neighbours. Count up from the previous value (keep it in state, never mount with 0, so it never blinks to zero between updates), with a short roll under about 300 ms and none under reduced motion. Clear it when the surface is opened, or per item as items are viewed in a long list, and badge only what needs a decision (mentions, review requests), never promotions or product news. A dot means "changed", a number means "how many"; never both on one item. Give the control an accessible name that includes the count ("Notifications, 3 unread", "more than 99 unread" when capped) and hide the visual badge with `aria-hidden`. Presence (online/away) is a separate signal, shown on the avatar ring.
**Detect.** Uncapped counts that reflow navigation; a badge placed in the layout flow beside its icon; a count state initialised to 0 on every render; badges that never clear; badges on everything; a dot and a number on the same row; a badge number with no accessible label.

### STA-14 · Undo beats "Are you sure?" (P1)
**Applies to.** delete, archive, remove and other destructive actions; sending messages and emails; editors and canvases with an editing history.
**Rule.** For recoverable actions, act on one click and offer a time-limited undo (5 to 10 s, never shorter) with a visible draining countdown instead of an "Are you sure?" dialog, which taxes every user to protect the few who misclick and gets clicked through anyway. Pause the countdown on hover and focus, keep Undo keyboard-reachable, let Cmd/Ctrl+Z undo the last action outside text fields, and announce the toast politely without reading out each second. Back it with a soft delete (a `deleted_at` timestamp filtered out of every query, search and count, purged by a scheduled job after a stated period such as 30 days) and a Trash or "Recently deleted" view that shows that period, so the toast is never the only way back; honour real erasure requests. Match friction to the cost of a mistake: undo for the reversible, type-to-confirm only for the truly irreversible (state exactly what will be lost, show the string to type in a copyable monospace element, accept paste, trim whitespace, link the instruction with `aria-describedby`). Hold actions that leave your system for a short grace period ("Sending in 6 s… Undo", about 5 to 10 s), then show a definitive "Sent". Editors keep a multi-step undo stack with redo (Shift+Cmd+Z / Ctrl+Y), group typing bursts and drags into one step, and clear redo when a new action is taken.
**Detect.** Confirm dialogs on every delete; hard deletes with no recovery; undo toasts with no visible timer or a timer that runs on while focused; type-to-confirm on reversible actions; editors with a single undo level.
**Fix.** Either perform the action and reverse it on Undo (soft delete makes this trivial), or delay the server commit until the window ends and flush pending commits on page unload.

### STA-15 · "Copied" must be true (P1)
**Applies to.** copy-to-clipboard controls.
**Rule.** Set the copied state only after `await navigator.clipboard.writeText(value)` resolves, on the next frame: that is perceptually instant, so never show a spinner, and never show the check before or regardless of the result. Hold the check about 2 s, restart the timer on every click so a repeat copy signals again, then revert. Copy the raw value from the source string or a data attribute, never the rendered text, which carries wraps, zero-width characters and thousands separators. Keep the button width fixed so the label swap does not shift layout, and on an icon-only button change the accessible name too ("Copy API key" → "Copied"). Announce "Copied" through one persistent `role="status"` element whose text you change. `navigator.clipboard` is undefined on insecure origins and `writeText()` can reject (no user gesture, document not focused, permission denied): fall back to a hidden textarea with `execCommand('copy')`, and if that fails too show an error state ("Couldn't copy. Select and press Ctrl+C") and select the text. Secrets may be masked on screen but copy in full and are never logged. Under reduced motion swap the icon without a fade.
**Detect.** `navigator.clipboard.writeText` without try/catch or not awaited before `setCopied(true)`; copying `innerText` of a formatted element; permanent "Copied" state; a spinner on a copy button; a timer not reset on a second click.

### STA-16 · Offline only where offline is real (P1)
**Applies to.** products meant to work offline (PWAs, mobile, field tools, editors with local drafts).
**Rule.** For products used without a connection: detect offline (`navigator.onLine` plus failed requests), show a persistent banner ("Offline, your changes are saved locally"), queue mutations and replay them oldest first on reconnect, disable only actions that strictly need the network, and do not show errors for expected offline failures. Elsewhere, a failed request is just an error with retry.

### STA-17 · Progress bars show real, measurable progress (P1)
**Applies to.** progress bars and long-running operations: uploads, downloads, installs, imports, exports, processing jobs, multi-file queues.
**Rule.** When the system can measure progress, show it determinately: a bar with the percent, the item's name and size, and for large transfers the amount done of the total and time left, optionally the rate ("51% · 7.2 of 14.2 MB · 6 s left"). Smooth the time-left estimate so it does not jump, and split multi-stage work into named steps (Upload, Process, Done) so stages without a byte count still visibly advance. End in an explicit completion state ("Uploaded", with proof such as a preview, FRM-16), never a bar that silently vanishes. On failure keep the work already done, mark where it stopped (danger role plus icon and text) and offer retry inline; say "resume" only when the backend supports resumable transfers, and otherwise retry automatically restarts without making the user pick the file again. In a batch each item has its own bar, status and retry, a header counts done and failed separately ("3 of 5 done · 1 failed"), and one failure never stops the rest. Use `<progress>` or `role="progressbar"` with `aria-valuenow`, `aria-valuemin`, `aria-valuemax` and an accessible name, and announce completion and failure in a polite live region, not every percent.
**Detect.** An indeterminate spinner (`animate-spin`, `CircularProgress` without a value) on an upload or job whose `loaded`/`total` or step count is available; a bar with no text value; a bar that disappears with no done state; retry that requires reselecting the file; one bar for a whole multi-file batch.

### STA-18 · Pending indicators mirror real activity (P1)
**Applies to.** typing indicators, "thinking" and "generating" states in chat and AI products, presence of someone composing.
**Rule.** An indicator says something is happening, so it lives exactly as long as the activity. Drive typing presence from real events (start on input, stop on send or after a few seconds idle) and remove it the moment the message or the first streamed content arrives; stream AI answers as they are generated instead of holding a finished answer behind dots. Never insert an artificial delay between "indicator on" and "message shown" to make replies feel thoughtful, and never re-trigger pending dots to keep people watching: both are dark patterns (CON-9). An indicator that disappears with nothing sent simply expires; do not imply a message is coming. Announce new messages in a polite live region, not each indicator toggle, and under reduced motion replace bouncing dots with a static "typing…" label.
**Detect.** `showTypingIndicator(); await delay(…); send()`; indicators started on a timer rather than an input event; no idle timeout; a full AI answer rendered at once after a long "thinking" state when the API streams; a live region that announces "typing".

---
Sources: loading-states-system, skeleton-loading, doherty-threshold, perceived-performance, optimistic-ui, behind-the-button, empty-states, error-states, toast-notifications, notification-system, notification-badge, undo-ux, copy-to-clipboard, typing-indicators, ai-prompt-input, chat-ui-system, file-upload-ux, and the free MIT-licensed `ux-states` skill by designmotionhq. See `sources.md`.
