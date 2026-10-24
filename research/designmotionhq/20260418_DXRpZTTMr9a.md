---
id: DXRpZTTMr9a
reel_url: https://www.instagram.com/reel/DXRpZTTMr9a/
pattern_page: https://designmotionhq.com/patterns/toast-notifications
date: 2026-04-18
duration_s: 49
type: ui
category: feedback
topic: toast notifications (position, timing, stacking, dismissal, type coding)
sources: frames, voice-over, pattern page
---

# Toast notifications: five rules

**Caption:** Toasts make you app feel reactive.
**Hook:** Most toasts break three of these five rules.

## Main rule
Place toasts at the edge (bottom-right on desktop, top on mobile, never centre), set dismiss time by
severity (info 4 s, warning 7 s, error until acknowledged), show at most 3 at once with spring-driven
reflow, make every toast dismissible (close button, swipe, pause on hover), and code types with an
icon plus a left border colour, never colour alone.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 5 | rules in the video | 0:00 voice, 0:45 end card "Five rules." |
| bottom-right | desktop toast anchor | 0:03-0:09 on-screen + voice, page |
| top | mobile toast anchor | 0:04-0:09 on-screen + voice, page |
| 4 s | info toast auto-dismiss ("4S · AUTO-DISMISS") | 0:11-0:18 on-screen + voice; page "~4s" |
| 7 s | warning toast hold ("7S · HOLDS LONGER") | 0:12-0:18 on-screen + voice; page "~7s" |
| ∞ | error toast stays "UNTIL ACKNOWLEDGED" | 0:12-0:18 on-screen + voice, page |
| 3 | maximum visible toasts ("MAX 3 VISIBLE") | 0:19-0:27 on-screen + voice, page |
| damping 20 | spring for stack reflow | 0:19-0:27 on-screen chip + voice (0:24) |
| stiffness 180 | spring for stack reflow | 0:19-0:27 on-screen chip + voice (0:24); mass not stated |
| 6% | share of users who "can't tell them apart" (colour vision deficiency) | 0:41-0:44 on-screen + voice, page "~6%" |
| 4 types | info, success, warning, error | 0:37-0:44 on-screen |
| $240.00, 2.4 MB, 1.2 GB, 92%, 5 seconds, v2.14.0, 2.15 | example toast contents (not rules) | throughout |

Calculation (not in the video): with mass 1, damping 20 and stiffness 180 give a damping ratio of
about 0.75, so roughly 3% overshoot and settling in about 0.4 s.

## Before / after
1. **Centre vs edge.** Bad: a toast in the middle of a desktop window ("Blocks content / User can't
   click through"), outlined in danger colour. Good: desktop toast at bottom-right ("Saved
   successfully"), mobile toast at the top. Why: the centre is where the user's task is; an overlay
   there hides content and intercepts clicks, while an edge position stays in peripheral vision.
2. **Fixed timer vs severity-based timer.** Good: "File uploaded" (info) depletes its progress bar
   in 4 s, "Session expiring" (warning) holds 7 s, "Payment failed" (error) never auto-dismisses.
   Voice: a fixed timer is a bug. Why: more important messages need more reading and reaction time;
   errors that vanish leave the user without the information needed to fix them.
3. **Pile-up vs capped stack.** Good: toasts enter at the bottom of the stack, older ones are pushed
   up with a spring (damping 20, stiffness 180) and the oldest leaves once there would be more than
   3 visible. Why: a cap keeps the region readable; spring reflow lets the eye track where each item
   went. Voice claims other motion "feels cheap" (opinion).
4. **Inescapable vs dismissible.** Good: a close button (click), swipe-to-dismiss on mobile, and a
   timer that pauses while hovered ("PAUSED" badge, "Timer freezes until you leave"). Why: users
   control when a message leaves; voice: a toast the user cannot escape is effectively a modal.
5. **Tint only vs icon + border.** Four toasts (Update available, Saved to drafts, Quota almost up,
   Connection lost) each with a type icon (info, check, warning triangle, cross) and a coloured left
   border. When the colour is removed (greyscale simulation) the icons still tell the types apart.
   Why: colour alone fails for colour-blind users; shape (icon) is a redundant channel. Voice:
   background tint alone is not enough.

## Do
- Anchor toasts bottom-right on desktop and at the top edge on mobile.
- Set duration by type: info about 4 s, warning about 7 s, errors stay until acknowledged.
- Show at most 3 toasts; add new ones at the bottom, push older ones up, queue the rest.
- Animate stack reflow with a spring (e.g. damping 20, stiffness 180).
- Provide a close button, swipe-to-dismiss on touch, and pause the timer on hover.
- Give each type an icon and a left accent border in addition to colour.

## Don't
- Don't place toasts in the screen centre.
- Don't use one fixed timer for every toast.
- Don't auto-dismiss critical errors.
- Don't let toasts pile up beyond 3 visible.
- Don't make a toast impossible to dismiss.
- Don't rely on background tint or colour alone to signal type.

## Scene by scene
- 0:00 Title "Toasts done right."; a success toast "Payment received / $240.00 from Maria Lopez" with close ×.
- 0:01 An info toast "New message / Alex sent you a file" stacks above it.
- 0:03 "RULE 01 / Position": desktop window with toast at bottom-right ("Saved successfully"), tag "✓ DESKTOP · BOTTOM-RIGHT".
- 0:04 Phone with toast at the top ("New message"), tag "✓ MOBILE · TOP".
- 0:06 Third window with a centred toast "Blocks content / User can't click through", tag "✗ CENTER · BLOCKS CONTENT".
- 0:07 Caption "Center blocks what users are actually doing."; 0:08 the bad window gets a danger outline.
- 0:10 "RULE 02 / Timing".
- 0:11 "File uploaded / Cover.png, 2.4 MB" (info, left border + bottom progress bar), label "4S · AUTO-DISMISS".
- 0:12 "Session expiring / Save your work soon" (warning) "7S · HOLDS LONGER"; "Payment failed / Waiting for user action" (error) "∞ · UNTIL ACKNOWLEDGED"; bars deplete at different speeds to 0:18.
- 0:19 "RULE 03 / Stacking", chips "DAMPING: 20", "STIFFNESS: 180", "MAX 3 VISIBLE"; first toast "New follower".
- 0:21 "Deploy complete / v2.14.0 is live" enters below; 0:22 "Build queued / main, ci pipeline" enters below.
- 0:23 "Low storage / 1.2 GB remaining" (warning) enters at the bottom, "New follower" leaves at the top with a springy shuffle.
- 0:25 "Backup saved / All data synced" enters; "Deploy complete" leaves; 0:27 stack thins as items exit.
- 0:28 "RULE 04 / Dismissible": "Close button / Always offer a way out" (tag CLICK), "Swipe to dismiss / Gesture on mobile" (tag SWIPE).
- 0:30 "Hover to pause / Timer freezes until you leave" (tag HOVER) with a depleting bar.
- 0:31 Cursor clicks the close × (ripple); 0:32 the swipe toast slides away; 0:33 demo resets.
- 0:35 Cursor rests on the hover toast: "PAUSED" badge, bar stops.
- 0:36 "RULE 05 / Color coding".
- 0:37 Toasts build: "Update available / Version 2.15 is ready" (info), 0:38 "Saved to drafts / Changes auto-backed up" (success), 0:39 "Quota almost up / 92% of plan used" (warning), 0:40 "Connection lost / Retrying in 5 seconds" (error), each with icon and left border colour.
- 0:41 All colour drains to grey; only icons differ; chip "6% of users can't tell them apart"; held to 0:44.
- 0:45 End card "Five rules. Zero excuses.", "Follow for daily design details", Follow / Save buttons.

## Voice-over summary
- Desktop toasts sit bottom-right, mobile toasts at the top, never in the centre, which blocks the user's work.
- Info dismisses at 4 seconds, warnings hold 7, errors stay until acknowledged; a fixed timer is a bug.
- Maximum three visible; new ones push old ones up with spring physics, damping 20 and stiffness 180.
- Always dismissible: close button, swipe on mobile, pause on hover; an inescapable toast is really a modal.
- Each type needs an icon plus a left border colour, because tint alone fails for the 6% who cannot distinguish the colours.

## Notes for the skill
- Live regions: render a persistent container with `role="status"` / `aria-live="polite"` for info and success, and `role="alert"` (assertive) only for errors. Do not move focus into a toast; if a toast has actions (Undo, Retry), give keyboard users a way to reach it (e.g. a documented shortcut that focuses the toast region) and make sure the action exists elsewhere too.
- Pause the timer on keyboard focus as well as hover, and when the window loses visibility (`document.hidden`); WCAG 2.2.1 Timing Adjustable applies to timed messages users must read or act on. Consider scaling duration with text length rather than fixed 4 s / 7 s.
- An error that stays until acknowledged is no longer a transient toast; for errors tied to a form or page, prefer an inline message or a persistent banner, and keep error toasts for background failures.
- Positions are conventions, not standards: Material places snackbars at the bottom on mobile too (above bottom navigation); the top edge on mobile can collide with the status bar and system notifications. Respect safe-area insets (`env(safe-area-inset-*)`) either way.
- Swipe-to-dismiss needs a non-gesture alternative (the close button) per WCAG 2.5.1; the close button needs an accessible name ("Dismiss notification") and a 44px touch target.
- Stack: cap visible items at 3, queue the rest (FIFO), dedupe identical messages (increment a counter instead of adding a new toast). New items at the bottom with older ones moving up is the reel's choice; whichever edge, keep it consistent.
- Spring 20/180: in libraries like Framer Motion use `{ type: "spring", damping: 20, stiffness: 180 }` (mass 1 default). Under `prefers-reduced-motion: reduce`, replace slide/spring with a short opacity fade.
- Colour vision deficiency affects about 8% of men and 0.5% of women (roughly 4-5% of a mixed population), so "6%" is a rough figure; the rule (icon + text + border, not colour alone, WCAG 1.4.1) holds regardless. Type colours on a dark surface still need 3:1 non-text contrast for borders/icons (WCAG 1.4.11).
