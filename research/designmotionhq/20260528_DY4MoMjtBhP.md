---
id: DY4MoMjtBhP
reel_url: https://www.instagram.com/reel/DY4MoMjtBhP/
pattern_page: https://designmotionhq.com/patterns/notification-system
date: 2026-05-28
duration_s: 50
type: ui
category: feedback
topic: notification system (toast, banner, modal, badge chosen by severity)
sources: frames, voice-over, pattern page
---

# Notification system: four surfaces, four volumes

**Caption:** not captured yet
**Hook:** Notifications are a system; pick the wrong surface and users tune out.

## Main rule
Treat notifications as one system of four surfaces with different volume and persistence: toast
(low, auto-dismiss with undo), banner (degraded state, stays until closed), modal (blocking, needs a
decision), badge (passive count, stays until cleared). Let the event's severity choose the surface,
never habit, and never stack blocking dialogs.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 4 | surfaces: toast, banner, modal, badge | 0:03-0:11 on-screen + voice, page |
| 4 s | toast auto-dismiss time ("AUTO-DISMISS 4S · UNDO") | 0:23 voice, 0:24-0:35 on-screen; page says only "a few seconds" |
| 2s | latency threshold in the banner copy "Latency above 2s. Investigating." (example content, not a rule) | 0:04-0:11 on-screen |
| 4242 | card ending in the declined-payment examples (example content) | 0:01, 0:05, 0:15 on-screen |
| 3 | unread count on the badge example | 0:05-0:22 on-screen + voice |
| 3 toasts | stack that "breathes" (works) | 0:35-0:45 on-screen + voice |
| 3 modals | stack labelled "trainwreck", "Users bail." | 0:38-0:45 on-screen + voice |

## Before / after
1. **Everything at once (opening).** Bad: a single "Payment failed" event fires as a banner, a toast
   and a modal at the same time on a dashboard, plus a badge dot on the bell. Why it fails: the
   same message on every channel is noise; the user cannot tell which one matters and dismisses all.
2. **Four volumes.** Toast slides into a corner (lowest), banner takes the full top width, modal
   blocks everything, badge just sits on an icon. (The voice says "same content", but on screen each
   tile shows a different example message.)
3. **Severity picks the surface.** New message → toast. Server degraded → banner. Card declined →
   modal (Cancel / Try again). 3 unread comments → badge. Why: interruption cost should match the
   consequence of ignoring the message; a blocking surface is only justified when the user cannot
   continue without deciding.
4. **Lifecycle (persistence is part of the contract).** Toast "Comment posted" with UNDO disappears
   after 4 s. Banner "Sync paused / Reconnecting..." stays until the user clicks ×. Modal "Delete
   project? This action cannot be undone." stays until Cancel or Delete. Badge "3 unread" stays
   quietly until cleared (then shows "cleared" and later "1 unread"). Why: users learn what each
   surface means by how long it lives; inconsistent persistence breaks that learned contract.
5. **Stacking.** Good: 3 toasts (Saved to drafts, Comment added, Item archived with UNDO) stack
   vertically with spacing, each readable. Bad: 3 modals (Card declined, Update available "Action
   required to continue", ...) pile on top of each other, skewed; label "Users bail." Why:
   non-blocking messages can coexist; blocking ones each demand exclusive attention, so stacking
   them makes none answerable.

## Do
- Define the four surfaces once and route each event type to exactly one of them by severity.
- Auto-dismiss toasts after a few seconds (4 s in the reel) and give them Undo for destructive or reversible actions.
- Keep banners until the user closes them or the condition resolves.
- Use a modal only when the user must make a choice before anything else can proceed.
- Let badges show a count passively until the items are viewed.
- Stack toasts with spacing so several can be read.

## Don't
- Don't send one event to several surfaces at once.
- Don't route everything to the loudest surface; over-escalation trains users to ignore all alerts.
- Don't queue multiple modals on top of each other.
- Don't use a blocking modal for a low-severity informational message.

## Scene by scene
- 0:00 Dashboard mock: sidebar, "Overview", MRR $48,210 (+12.4%), Active users 2,431, revenue bar chart, bell with a badge dot.
- 0:01 "Payment failed" appears as a top banner, a toast and a centred modal ("Card ending 4242 was declined. Try a different payment method." Cancel / Try another card) at once; background dims.
- 0:02 Caption "Notifications are a system."
- 0:03 Section "Four surfaces / Same content. Four volumes."; 2x2 grid TOAST, BANNER, MODAL, BADGE.
- 0:04 Toast "New message / Sarah Chen sent you a file." slides in; banner "Server v2.4 degraded / Latency above 2s. Investigating." with close ×.
- 0:05 Modal "Card declined / Card ending 4242. Use another?" (Cancel / Try again); badge bell with "3" pulsing.
- 0:06 Surfaces animate in and out in turn to show each one's behaviour.
- 0:10 Caption "Pick the volume that matches the message."
- 0:12 Section "Severity → Surface / The trigger picks the volume."
- 0:13 Row "TRIGGER New message" → toast; 0:14 "Server degraded" → banner; 0:15 "Card declined" → modal; 0:16 "3 unread comments" → badge; each output replays to 0:21.
- 0:22 Chip "Severity picks the surface".
- 0:23 Section "Lifecycle / How they live and die."
- 0:24 Four columns: toast "Comment posted / On Q3 roadmap doc." + UNDO ("AUTO-DISMISS 4S · UNDO"); banner "Sync paused / Reconnecting..." with cursor on × ("MANUAL CLICK X").
- 0:25 Modal "Delete project? This action cannot be undone." Cancel / Delete ("BLOCKING REQUIRES ACTION"); badge "3 unread" ("QUIET UNTIL CLEARED").
- 0:26 Badge switches to "cleared", later "1 unread"; toast fades out at about 0:30 and replays.
- 0:34 Caption "Persistence is part of the contract."
- 0:36 Section "Stack behavior / Three toasts? Three modals?": left panel "3 TOASTS STACKED · BREATHE", right panel "3 MODALS TRAINWRECK".
- 0:37 Toasts arrive one by one (Saved to drafts, Comment added, Item archived + UNDO); modals pile up skewed (Card declined, Update available with Skip / Install now); "USERS BAIL."
- 0:44 Caption "Wrong surface = zero attention."
- 0:46 End card: a row of four mini surfaces, "Follow for more UI systems.", "Save this for your next dashboard.", handle chip.

## Voice-over summary
- Notifications are a system; choosing wrong makes users tune out.
- Toast slides into a corner, banner takes the full top, modal blocks everything, badge just sits there: four volumes.
- Examples: new message → toast, server degraded → banner, card declined → modal, three unread comments → badge; severity picks the surface.
- Toasts auto-dismiss in four seconds with undo for destructive actions; banners stay until closed; modals demand a choice; badges wait until cleared.
- Three toasts stack fine, three modals are a trainwreck; mix surfaces by severity, never by habit, because the wrong surface gets zero attention.

## Notes for the skill
- Model it as a routing table: `event.severity` (info | warning | blocking | passive) → surface; one event, one surface. Keep a single notification service that owns queueing, dedup and persistence rules.
- 4 s is tight for a toast that contains an Undo button or more than a few words. Pause the timer on hover and focus, scale duration with text length, and keep actionable toasts visible longer (Material allows 4-10 s; actionable snackbars often stay until acted on or dismissed). WCAG 2.2.1 Timing Adjustable applies to timed content that users need to act on.
- Never put the only path to an important action in a toast; an undo toast should be backed by another way to recover (history, trash).
- ARIA: toasts in a polite live region (`role="status"`); urgent banners `role="alert"` sparingly; modal decisions as `role="alertdialog"` with focus moved inside, focus trapped, Escape mapped to the safe choice, focus returned on close; badge needs an accessible name ("3 unread notifications"), not just the number.
- Modal queue: if several blocking decisions are pending, show them one at a time (sequential queue) or merge them into one dialog; never render more than one modal layer.
- Toast stack: cap visible toasts (about 3), keep a consistent insertion edge, collapse older ones; respect `prefers-reduced-motion` for slide-ins.
- "Card declined" as a modal is right only inside the payment flow the user just triggered; a declined renewal discovered in the background is better as a persistent banner with a fix-it action.
- Do not convey severity only by colour (WCAG 1.4.1): pair with icon and wording.
