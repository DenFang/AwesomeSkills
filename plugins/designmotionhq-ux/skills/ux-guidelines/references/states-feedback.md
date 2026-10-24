# States and feedback

A component is not done when the happy path renders. Anything that fetches, submits or waits has states, and every one of them is designed on purpose. The user must always know what is happening, what happened, and what to do next.

Severity: **P0** breaks use, loses data or misleads, **P1** friction, **P2** polish.

---

### STA-1 · Cover every state the component can really be in (P0 when a missing state blanks the screen or hides a failure, P1 otherwise)
**Applies to.** anything that fetches, submits or waits.
**Rule.** Anything that fetches or submits has loading, empty, error and success. Add **partial** only when data comes from several sources, pages or a stream, and **offline** only when the product is meant to work without a connection. Do not add states a component cannot reach; that is weight, not completeness.
**Detect.** `data.map(...)` with no branch for `isLoading`, `error`, or `data.length === 0`; a fetch hook whose `error` is never read; screens that render nothing while loading.
**Fix.** Branch explicitly on each applicable state and mark the rest "n/a: reason" in the report.

### STA-2 · Pick the loading pattern from what you know about the wait (P1)
**Applies to.** anything that fetches, submits or waits.
**Rule.**
| What you know | Pattern |
|---|---|
| Resolves under about 300 ms | Show nothing; a flash of a loader reads as a glitch |
| Layout shape is known, wait over 300 ms | Skeleton that mirrors the final layout |
| Short wait, unknown shape (one action, under about 3 s) | Spinner, in place, inside the control |
| Measurable progress, over about 3 s | Progress bar with percent and time left |
| Reversible, low-stakes action | Optimistic update (STA-4) |
A single default (skeleton everywhere, or a full-page spinner) is the tell of an unconsidered UI. Delay showing the loader by about 300 ms so fast responses never flash it.
**Detect.** A global page spinner for content with a known shape; spinners for multi-second operations with known progress; loaders that appear instantly on every request.

### STA-3 · Skeletons match the real layout (P1)
**Applies to.** skeleton loaders.
**Rule.** Same number of items, same approximate dimensions, same gaps and padding as the loaded content. Animate a subtle shimmer in reading direction (a static grey block reads as broken; keep it static under reduced motion, MOT-13). Replace it in place with no layout jump. If loading passes about 2 s, add context ("Loading 1,247 records…"); past about 10 s, offer cancel.
**Detect.** Generic skeleton reused for different layouts; skeleton count unrelated to page size; content shift (CLS) when data arrives.

### STA-4 · Optimistic UI for cheap, reversible actions only (P1)
**Applies to.** actions that change server data.
**Rule.** Likes, saves, toggles, reorders, renames and sent chat messages update the instant the user acts, sync in the background, and roll back cleanly with a short explanation if the request fails (keep any draft the user typed). Money, irreversible actions and anything whose result the server decides (order IDs, prices, stock) wait for the server and then repaint with the server's answer.
**Detect.** Spinners on a like button; optimistic updates with no rollback path; a checkout that shows success before the server confirmed; client-computed totals trusted by the server.
**Fix.** Apply locally → request → on error restore previous value and notify inline. Server re-validates everything the client validated.

### STA-5 · Respond inside 400 ms (P1)
**Applies to.** anything that fetches, submits or navigates.
**Rule.** The interface must visibly react within about 400 ms (under 200 ms feels instant). The work can take longer as long as the UI answers inside the threshold with a skeleton, an optimistic update or honest progress. Perceived speed can be improved without changing real speed: show the layout first, assume success where safe, and start progress bars fast rather than linear.
**Detect.** Actions with no visible reaction until the network returns; navigation that freezes the old screen while the next one loads.

### STA-6 · Empty states explain and lead (P1)
**Applies to.** lists, tables, feeds, search results, inboxes, dashboards that can have no items.
**Rule.** "No data" is a failure, not an empty state. Each empty state answers why it is empty and what to do next, with one primary action that is the real next step, in a human sentence. Distinguish the kinds:
| Cause | Treatment |
|---|---|
| First use | Teach the feature (a ghost preview of a real item helps) and offer the create action |
| No results for a search | Say what was searched, suggest alternatives or popular items |
| Filtered out | Name the filter and offer "Clear filters" |
| No access | Explain and say who can grant access |
| Done by design | Confirm it is good news ("All caught up") |
One small icon or illustration signals intent; text-only is fine if the design system has none.
**Detect.** Blank areas when arrays are empty; one generic "No items found" for every cause; empty states whose only action is "Refresh".

### STA-7 · Errors say what happened and offer a way out (P0)
**Applies to.** every error path (catch blocks, failed responses, error boundaries).
**Rule.** Copy names what failed in the user's terms, optionally why, and what to do now. "Something went wrong", "Error 500" and raw `err.message` are bugs. Every error offers an exit: retry if transient, an alternative path if persistent, support or details if neither. The fallback message for unknown errors is still specific to the component ("We couldn't load the invoices. Try again.").
**Detect.** Generic error strings; `catch {}` that swallows; `alert(err)`; error screens with only "OK".

### STA-8 · Put each error on the surface that fits its severity (P1)
**Applies to.** every error path.
**Rule.**
| Error | Surface |
|---|---|
| Field validation | Inline under the field |
| Action finished but failed (save, send) | Inline on the item, or a toast with retry |
| Connection lost, degraded service | Persistent banner |
| Server failure or no permission for a whole view | Page-level replacement with recovery |
| Needs an immediate decision | Modal |
Never put an error that needs action in an auto-dismissing toast. A failed chat message stays in place marked "Not sent · Retry"; a failed upload keeps its row with inline retry.
**Detect.** Toasts for validation errors; full-page errors for a single failed widget; partial failures that blank the whole screen.

### STA-9 · Partial data degrades gracefully (P1)
**Applies to.** views built from several requests, paginated or streamed data.
**Rule.** When part of the data fails, show what loaded and mark only the missing part ("Couldn't load. Retry"). When the next page loads, keep the current page visible and show loading at the edge. Never blank a screen that already had content.
**Detect.** One `error` flag for several independent requests; pagination that clears the list while fetching.

### STA-10 · Success is visible, specific and short-lived (P1)
**Applies to.** actions that change data.
**Rule.** Silence after an action is ambiguous. Confirm where the user is looking: a field check for inline edits, the changed data plus a short "Saved" for forms that stay, context on the destination page for forms that navigate ("Created John Smith"), a count for batch actions ("Suspended 12 users"), and an undo for destructive ones. No context-free "Success!", no permanent success banners.

### STA-11 · Toasts: position, timing, limits, dismissal, announcement (P1)
**Applies to.** toast or snackbar systems.
**Rule.** Bottom-right (or bottom-centre) on desktop, top on mobile, never over the centre of the content. Time by severity: about 4 s info, about 7 s warning, errors stay until acknowledged. Pause the timer on hover and focus. At most 3 visible, the rest queue. Always dismissible (close button, swipe on mobile, Escape). Type is shown by icon and accent, never colour alone. Announce through an `aria-live` region.
**Detect.** Centred toasts; one fixed timeout for all types; unbounded stacks; toasts with no close; toasts not announced to screen readers.

### STA-12 · Notifications: one message, four volumes (P1)
**Applies to.** products with more than one notification surface.
**Rule.** Severity picks the surface: **toast** for low-priority and transient news (auto-dismiss, often with undo), **banner** for ongoing conditions (stays until resolved or dismissed), **modal** only when the user must decide before continuing (never queue several modals), **badge** for passive counts. Over-escalating trains people to ignore everything.
**Detect.** Modals for informational messages; stacked modals; banners for one-off events.

### STA-13 · Badges count and clear (P2)
**Applies to.** count badges and unread indicators.
**Rule.** A badge is a count you clear, not a status. Cap at 99+, pin it to the icon's corner so the icon never moves, only count up (never blink to zero between updates), clear it when the surface is opened, and badge only what needs the user. A dot means "changed", a number means "how many"; never both on one item. Presence (online/away) is a separate signal, shown on the avatar ring.
**Detect.** Uncapped counts that reflow navigation; badges that never clear; badges on everything.

### STA-14 · Undo beats "Are you sure?" (P1)
**Applies to.** delete, archive, remove and other destructive actions.
**Rule.** For recoverable actions, do it immediately and offer a time-limited undo (5 to 10 s) with a visible countdown, backed by a soft delete (keep data for a period such as 30 days). Reserve heavy friction (typing the resource name) for the truly irreversible. Delayed send is a form of undo. Editors support an undo stack (Cmd/Ctrl+Z).
**Detect.** Confirm dialogs on every delete; hard deletes with no recovery; undo toasts with no visible timer.

### STA-15 · "Copied" must be true (P1)
**Applies to.** copy-to-clipboard controls.
**Rule.** Flip to a check on the same frame, hold it about 2 s, then reset so the next copy can signal again. Copy the raw value, not the formatted text (no stray spaces or newlines). Announce through `aria-live`. `navigator.clipboard` is undefined on insecure origins and `writeText()` can reject (document not focused, permission denied); guard for both, then fall back or report failure. Never show a check over an empty clipboard.
**Detect.** `navigator.clipboard.writeText` without try/catch; copying `innerText` of a formatted element; permanent "Copied" state.

### STA-16 · Offline only where offline is real (P1)
**Applies to.** products meant to work offline (PWAs, mobile, field tools, editors with local drafts).
**Rule.** For products used without a connection: detect offline (`navigator.onLine` plus failed requests), show a persistent banner ("Offline, your changes are saved locally"), queue mutations and replay them oldest first on reconnect, disable only actions that strictly need the network, and do not show errors for expected offline failures. Elsewhere, a failed request is just an error with retry.

---
Sources: loading-states-system, skeleton-loading, doherty-threshold, perceived-performance, optimistic-ui, behind-the-button, empty-states, error-states, toast-notifications, notification-system, notification-badge, undo-ux, copy-to-clipboard, chat-ui-system, drag-and-drop-tips, file-upload-ux, and the free MIT-licensed `ux-states` skill by designmotionhq. See `sources.md`.
