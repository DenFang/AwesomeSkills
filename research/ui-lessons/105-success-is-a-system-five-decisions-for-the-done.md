---
lesson: 105
kind: video
duration_s: 77
type: ui
category: feedback
topic: success states as a system (specific copy, next action, stakes-based dismissal, open loop, rare celebration)
sources: frames, voice-over
---

# Success is a system: five decisions for the "done" screen

**Hook:** Three identical "Success! / OK" screens versus one specific "Invoice sent" screen with next steps: only the last keeps the user moving.

## Main rule
A success state must (1) say exactly what happened with the specifics (what, who, when, amount), (2) offer one primary next action plus one way back, (3) choose its persistence by stakes (a self-dismissing toast with Undo for reversible low-stakes changes, a persistent page with a receipt for money), (4) leave one open loop that brings the user back, and (5) reserve celebration for rare milestones.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 0 next step vs 0 → 2 next steps | generic "Success! OK" screens vs specific "Invoice sent" screen | 0:00-0:05 on-screen |
| "1 primary next · 1 way back" | action budget on a success screen (View invoice primary, Send another secondary, "Back to invoices" link) | 0:18-0:26 on-screen |
| "2 next steps · 1 way back" | the good variant's tag | 0:23-0:26 on-screen |
| 4 s (countdown 3.5 s → 2.5 → 1.5 → 0.5, then "gone after 4 s") | auto-dismiss of a low-stakes "Notifications saved" toast with Undo | 0:30-0:37 on-screen + voice ("leaves in four seconds") |
| low stakes · toast / high stakes · page | dismissal pattern by stakes; caption "reversible = toast · money = page" | 0:28-0:39 on-screen |
| $48 / month, "Pay $48.00" → "Payment received" page with Download PDF and "Receipt sent to …" email; tag "stays" | high-stakes success | 0:31-0:39 on-screen |
| Sent → Opened → Paid tracker; "Notify me when paid" toggle | open loop example | 0:39-0:46 on-screen |
| "Invite 2 teammates"; report "€18,400 invoiced · 9 invoices · 2 overdue" with Share | further open loops ("1 thread to pull") | 0:43-0:49 on-screen |
| "6 confetti · 0 notice"; "noise" vs "signal" | confetti on every save is ignored; "First invoice paid", "Milestone 1" celebrated once | 0:50-0:59 on-screen |
| "Milestone 1 · one burst, never on every save" | celebration rule summary | 1:00-1:16 on-screen |
| 5 decisions: Specific, Next step, Stakes, Open loop, Rare joy | end summary | 1:00 on-screen |

## Before / after
- **Generic vs specific.** Bad: "Success! Your action was completed." with OK (labelled "GENERATED", then struck through and tagged "maybe?"). Good: "Invoice sent to Northwind Labs", "INV-2051 · sent just now from Ines Duarte", amount €2,400.00, recipient, due date Oct 12, 2026, each row tagged "specific" ("what · who · when"). Why: concrete details are the proof the action worked; vague success leaves the user unsure and prompts double-checking.
- **Dead end vs next action.** Bad: checkmark plus OK; clicking OK leaves an empty "Nothing left to do here" ("dead end") and the user closes the tab. Good: primary "View invoice", secondary "Send another", plus "Back to invoices". Why: the moment after success is when intent to continue is highest; giving a path keeps momentum.
- **Same dismissal for everything vs by stakes.** Low stakes: toggling notification settings shows a toast "Notifications saved" with Undo and a progress bar, gone after 4 s. High stakes: "Pay $48.00" leads to a "Payment received" page that stays, with plan, amount, card, date, "Download PDF" and an emailed receipt. Why: reversible changes need only a glance and an undo; money needs a durable record ("Nobody screenshots a toast").
- **Closed vs open loop.** The sent invoice shows a Sent → Opened → Paid tracker with "Notify me when paid"; later "Northwind Labs opened INV-2051 · just now" appears. Report offers Share; workspace offers "Invite 2 teammates". Why: an unfinished but trackable thread gives a reason to return.
- **Constant vs rare celebration.** Confetti on six "Saved" toasts: "6 confetti · 0 notice", tagged noise. A trophy card "First invoice paid · Milestone 1" with a single burst is tagged signal. Why: habituation; frequent celebration trains users to ignore it, rarity keeps it meaningful.

## Do
- Write success copy as "<object> <verb past> to <whom>" plus key facts (ID, amount, date, actor, timestamp).
- Offer exactly one primary next action, optionally one secondary, and one way back.
- Low-stakes, reversible actions: toast with Undo, auto-dismiss around 4 s.
- High-stakes or financial actions: persistent confirmation page with a receipt (downloadable) and an email copy.
- Add one forward-looking hook: status tracker, notify-me toggle, share, invite.
- Celebrate first-time milestones only, once.

## Don't
- Don't ship a bare "Success!" with an OK button.
- Don't end a flow on a screen with no next action.
- Don't confirm payments with a disappearing toast.
- Don't attach confetti or animation to routine saves.

## Scene by scene
- 0:00 "Success is a system · 01": three app panels (Settings, Billing, Invoices) each with a check, "Success!" and OK, tagged "0 next step"; caption "done ≠ dead end".
- 0:02 "Three done screens": Invoices panel expands into "Invoice sent" with To / Amount €2,400 / Due Oct 12 / Ref INV-2051.
- 0:03 "Only one keeps the user": "View invoice" (primary) and "Send another" appear; tag "0 → 2 next steps".
- 0:05 "· 02 Say what happened": a generated-looking "Success! Your action was completed." is selected and retyped as "Invoice sent to Northwind Labs" with "INV-2051 · sent just now from Ines Duarte", then rows Amount €2,400.00, Recipient, Due Oct 12, 2026 each tagged "specific"; the generic card below is struck through and tagged "maybe?". Caption "what · who · when".
- 0:17 "· 03 Offer the next action": browser tab "Invoices · Hatch"; OK button replaced by "View invoice" / "Send another" / "Back to invoices"; clicking View invoice shows the invoice lines (Brand system retainer €1,800.00, Motion toolkit license €600.00, Total €2,400.00). Comparison "checkmark only: 0 next step" vs "next action: 2 next steps · 1 way back". Clicking OK on the bad version yields "Nothing left to do here · dead end" and the tab closes. Caption "1 primary next · 1 way back".
- 0:28 "· 04 Dismissal follows stakes": notifications settings (Invoice paid, Invoice overdue, Weekly summary) tagged "low stakes · toast"; Save shows toast "Notifications saved · Undo" counting down 3.5 s to 0.5 s, then "gone after 4 s". Below, "Upgrade to Team, $48 / month", "Pay $48.00" tagged "high stakes · page" turns into "Payment received" with details, "Download PDF", "Receipt sent to ines@hatch.example", tag "stays". Caption "reversible = toast · money = page".
- 0:39 "· 05 Leave one open loop": invoice card with Sent / Opened / Paid tracker and "Notify me when paid" toggled on; September report gets Share; workspace gets "Invite 2 teammates"; an event "Northwind Labs opened INV-2051 · just now" appears and the tracker advances to Opened. Caption "1 thread to pull".
- 0:50 "· 06 Celebrate the rare win": six "Saved" toasts each with confetti, counter "6 confetti · 0 notice", they fade; invoice card "Awaiting payment" with timeline turns "Paid" and shows "First invoice paid" with a trophy, one burst and a "Milestone 1" badge; tags "noise" vs "signal". Caption "confetti = milestones only".
- 1:00 "· 07 Five decisions. One screen.": chips Specific, Next step, Stakes, Open loop, Rare joy; the combined success card (actions, tracker, chips "Receipt emailed", "Toast for settings", "Page for payments", "Celebration saved for the first paid invoice").

## Voice-over summary
- Success is a system: of three done screens only one keeps the user.
- Say what happened with specifics; "A vague success feels like a maybe."
- Every success screen offers the next action; a checkmark with no button is a dead end where the user closes the tab.
- Dismissal follows stakes: a saved setting gets a toast that leaves in four seconds, a payment gets a page that stays with a receipt and email.
- Leave one open loop (track the payment, share the report, invite the team) so people come back.
- Celebration scales with rarity: confetti on every save is noise, save it for the first invoice paid.

## Notes for the skill
- Toast timing: 4 s is short for a toast that contains an action (Undo). WCAG 2.2.1 (Timing Adjustable) and common guidance suggest pausing the timer on hover/focus and giving action toasts longer (often 6-10 s) or making them persistent until dismissed; at minimum keep Undo reachable elsewhere (e.g. history) after the toast leaves.
- Announce success: use `role="status"` (polite live region) for toasts; for a full confirmation page move focus to the heading (`h1` "Payment received") so screen-reader users hear the result.
- Do not convey success only by a check icon and colour; the specific heading text carries it.
- Primary vs secondary action: one filled accent button, the rest as secondary/tertiary styles; keep "back" as a link-style action.
- Open loops should be opt-in (a "Notify me" toggle), not automatic notification sign-up.
- Celebration animations (confetti) must respect `prefers-reduced-motion` and should not block interaction; trigger them on server-confirmed milestone events, once per milestone (persist a flag).
