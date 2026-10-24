---
id: unknown
reel_url: unknown
pattern_page: https://designmotionhq.com/patterns/behind-the-button
date: unknown
duration_s: 62
type: ui
category: interaction
topic: request round trip behind a Buy button, and where optimistic UI is allowed
sources: frames, voice-over, pattern page
---

# Behind the Button: the six-step round trip

**Caption:** not captured yet
**Hook:** One click on "Buy" triggers six separate steps before the loading spinner is allowed to stop.

## Main rule
Validate on the client for instant feedback and again on the server for trust, write multi-row changes in one transaction, and repaint the UI from the server's response (real IDs, real status). Use optimistic UI only for cheap, reversible actions; payments and other irreversible actions keep a pending state until the server confirms.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 6 steps | validate, request, server, logic, write, respond | 0:01-0:02 on-screen diagram + voice |
| 0 network calls | client-side validation stage (badge in the browser chrome) | 0:05-0:15 on-screen badge; page repeats "0 network calls" |
| `POST /api/orders` with `{"items": 1, "total": 89.00}` + `Bearer` token | example request body leaving the browser | 0:09-0:14 on-screen |
| `"total": 0.01` | forged request sent with `curl --data` | 0:19-0:20 on-screen |
| `403 rejected` | server response to the forged total | 0:20-0:21 on-screen |
| $89.00 "from the catalog, not the client" | server re-computes the total from its own data | 0:16-0:30 on-screen |
| 4 rows in one transaction (INSERT orders, INSERT order_items, UPDATE inventory 4 → 3, INSERT payments) | database write step | 0:29-0:35 on-screen |
| `200 OK` with `{"order_id": "#4127", "status": "confirmed"}` | server response that ends the spinner | 0:37-0:45 on-screen + voice ("Status 200 and the order ID") |
| like count 128 → 129 | optimistic like, repainted instantly | 0:47-0:49 on-screen |

No timing (ms) values are shown; "like repaint: instant" vs "payment confirm: waits/real" is shown only as two progress bars.

## Before / after
1. **Forged request vs server re-validation (0:19-0:21).** Bad: the server trusts the `total` field the client sends; a `curl` request with `total: 0.01` would be accepted. Good: the server re-checks schema and types, verifies the token signature, and re-computes the total from its own catalog, so the forged request is rejected. Why: anything in the request can be edited by the caller; client validation only exists to give fast feedback, it is not a security boundary.
2. **Partial write vs transaction rollback (0:30-0:35).** Bad: rows are written one by one; if `INSERT payments` fails, an order and decremented inventory remain without a payment. Good: all four writes sit in one transaction; one failure triggers `ROLLBACK, nothing written`, the retry then commits all four ("COMMIT, atomicity"). Why: the user never ends up with a half-created order; the UI can report one clear outcome (success or failure).
3. **Guessed UI vs server truth (0:38-0:46).** The checkout card shows "Processing payment..." with an empty Order ID slot until the response arrives, then shows "Order confirmed", Order ID #4127, the receipt e-mail and delivery date. Why: the order ID only exists once the server created it; showing a locally invented value would be a lie that may need correcting.
4. **Optimistic like vs waiting payment (0:46-0:56).** Side-by-side: the like button fills and the counter goes 128 → 129 immediately with a small "syncing..." note, later "server confirmed". The payment button shows a spinner with "waiting for server... pending, by design" until it turns into "Order confirmed" / "confirmed, for real". Why: a like is cheap and reversible, so a rare rollback costs little and instant feedback feels fast; a charge is irreversible, so faking success could mislead the user about money.

## Do
- Run instant client-side checks (format, required fields) with inline success/error marks and no network call.
- Send a minimal payload (item IDs, quantity) plus an auth token; let the server derive prices and totals.
- Re-run all validation on the server, stricter than on the client.
- Wrap related writes (order, items, inventory, payment) in one transaction.
- Keep the submit control in a visible pending state (spinner + "Processing payment...") until the server responds, then render values from the response.
- Use optimistic updates for likes, favourites, renames: repaint now, reconcile in the background, roll back on error.

## Don't
- Don't treat client validation as security, and don't skip it either; both layers are needed.
- Don't accept a price or total from the client.
- Don't write multi-row business records outside a transaction.
- Don't show a fake order ID or a "success" state before the server confirms a payment.
- Don't apply optimistic UI to payments or other irreversible actions.

## Scene by scene
- 0:00 Product checkout card (lamp, quantity 1, shipping free, total $89.00); cursor clicks the full-width Buy button, which shows a spinner. Caption "You click Buy."
- 0:01 Headline "Six things happen before the spinner stops."; a 6-node loop diagram builds (1 validate, 2 request, 3 server, 4 logic, 5 write, 6 respond). A step tracker of the same six steps stays at the bottom for the whole video.
- 0:03 Section "Steps 1-2 · The request: Validate. Then ship it." Checkout form (email, card number, billing zip) gains check marks field by field; a "0 network calls" badge appears in the browser bar; label "instant feedback · a frontend job".
- 0:09 A `POST /api/orders` card with JSON body and a masked Bearer token travels from "browser" to "api.lumen.shop" along a dashed line; tracker step 2 lights up.
- 0:15 Section "Steps 3-4 · Backend: Never trust the client." Server panel checks "schema + types", "token verified", "total re-computed" one after another.
- 0:19 A red-tinted `curl --data` card with total 0.01 slides in and gets knocked away; "403 rejected" pill appears.
- 0:22 Business logic rows fill with progress bars and checks: Stock check (4 in stock), Price check ($89.00 matches catalog), Payment charge (gateway approved).
- 0:28 Section "Step 5 · Database: All of it, or none of it." `orders_db` cylinder; a TRANSACTION box fills with four rows.
- 0:32 The payments row turns to the danger colour with "FAIL"; the box empties with "ROLLBACK, nothing written"; rows refill with "retrying..." and end with "COMMIT, atomicity".
- 0:36 Section "Step 6 · Response: Server truth comes back." A `200 OK` card travels back to the browser; checkout shows spinner "Processing payment..." and an empty Order ID.
- 0:42 Spinner becomes a check: "Order confirmed", Order ID #4127, receipt sent to the e-mail, delivery date; tag "server truth, not a guess".
- 0:46 Section "The twist · Optimistic UI: Fast apps cheat." Two cards: a social post (like) and the payment card. Like fills instantly (128 → 129, "syncing..."), payment button spins ("waiting for server... pending, by design"). Bars: "like repaint: instant", "payment confirm" filling slowly. Tag "cheap actions repaint now, money waits".
- 0:53 Payment card turns to "Order confirmed", bar labelled "real".
- 0:56 Outro "The full round trip." loop diagram with a dot travelling through the six nodes; follow/save buttons.

## Voice-over summary
- A purchase click runs six stages: client validation, request, server validation, business logic, database write, response.
- Client validation is instant and needs no network; immediate feedback is the front end's responsibility.
- The server validates everything again because "Client input is never trusted"; anyone can forge a request.
- One transaction wraps every row so that all commit or none do (atomicity).
- After the 200 response, the UI repaints with what the server returned, not a guess.
- Fast apps repaint likes, favourites and renames instantly and reconcile later, but payments earn the spinner.

## Notes for the skill
- State model for an irreversible submit: `idle → validating (client, sync) → submitting (button disabled + spinner + aria-busy="true") → success | error`. Prevent double submission while `submitting` (disable or ignore repeat clicks; an idempotency key on the request is the server-side safeguard).
- Announce the outcome to assistive tech: put "Processing payment..." and "Order confirmed" in a polite live region (`role="status"`), and move focus to the confirmation heading or an error summary when the step ends.
- Optimistic update pattern: update local state immediately, keep the previous value, send the request, on failure restore the previous value and show a non-blocking error (toast) explaining the action did not save. Show at most a subtle "syncing" hint, not a spinner.
- If the payment wait is long, give progress text ("Contacting your bank...") rather than an indefinite spinner, and handle timeouts with a clear retry path that cannot double-charge.
- The video uses `403` for a forged price. 403 means "forbidden" (authorisation); a tampered or invalid body is more conventionally a `400`/`422` validation error. The UX point (server rejects it) is correct; the status code is a simplification.
- The video's step 1 shows check marks on every valid field; for form-timing rules (when to show errors vs success) see the form-validation-timing breakdown.
