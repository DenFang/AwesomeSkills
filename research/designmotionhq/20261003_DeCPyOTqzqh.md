---
id: DeCPyOTqzqh
reel_url: https://www.instagram.com/reel/DeCPyOTqzqh/
pattern_page: none
date: 2026-10-03
duration_s: 85
type: ui
category: overlays
topic: choosing modal vs bottom sheet vs side drawer; sheet snap points, dismiss velocity, drawer width, no stacking
sources: frames, voice-over, caption
---

# Modal, bottom sheet or side drawer: five rules for one container

**Caption:** One action, three containers, only one fits (ends with a plug for the author's Claude Code plugin).
**Hook:** The same action (edit the delivery address) can live in a modal, a bottom sheet or a side drawer, but only one fits.

## Main rule
Ask one question: does the user need to see the page while acting? If yes, use a bottom sheet (side drawer on desktop); if the action needs a full stop (destructive, irreversible), use a modal. Give sheets fixed snap points (peak, half, full), dismiss on fling velocity or past 50% distance, bound the desktop drawer between 320 px and 40% of the viewport, and never stack two sheets: replace content inside the one sheet and add a back arrow.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 1 question | "Need the page? -> Sheet" / "Need a stop? -> Modal" | 0:04-0:17 on-screen |
| 3 snap points: peek 15 %, half 50 %, full 92 % | bottom sheet heights as share of screen height | 0:23-0:33 on-screen markers + voice "three snap points" |
| 33 % ?, 44 % ?, 36 % ? | arbitrary "free height" positions (bad) | 0:19-0:22 on-screen |
| snap: 38 % -> half | release between two points springs to the nearest | 0:31-0:33 on-screen |
| velocity > threshold OR distance > 50 % | dismiss rule for drag-to-close | 0:34-0:45 on-screen "Dismiss when" |
| 1.4 px/ms | example flick velocity that closes the sheet | 0:41-0:45 on-screen |
| flick · 80 px · closed | a fast flick closes after only 80 px of travel | 0:42-0:45 on-screen |
| distance 35 % / 40 % · back | slow drag that stops short of 50 % returns | 0:44-0:45 on-screen |
| distance 55 % / 60 % · closed | slow drag past halfway closes | 0:43-0:45 on-screen |
| "distance only = stuck" | criticism of distance-only dismissal | 0:44-0:45 on-screen |
| 320 px <= drawer <= 40 % | desktop side drawer width bounds | 0:46-0:57 on-screen + voice |
| 240 px · 17 % -> form breaks | drawer too narrow | 0:50-0:52 on-screen |
| 933 px · 65 %, 1008 px · 70 % -> list gone | drawer too wide, becomes a page | 0:52-0:55 on-screen |
| 440 px · 31 % (also 442 px · 31 %) | good drawer width in the demo | 0:47-0:49, 0:56-0:57 on-screen |
| sheets open: 1 vs 2 ("2 sheets · which swipe?") | stacking vs replacing | 0:58-1:07 on-screen |
| 1 swipe · closed | one swipe dismisses the single sheet | 1:07 on-screen |
| 5 rules | context, snap points, velocity, drawer width, no stack | 1:08-1:11 recap |
| Order #4821, $48.00 / $36.00 / $52.00, Total $136.00 | demo order data (no rule meaning) | throughout |

## Before / after
- **Choosing the container (01 Only one fits).** Modal: "hides context" (page dimmed behind a scrim). Side drawer on a phone: "wrong screen". Bottom sheet: "keeps context" (order list still visible above the address form). Why: editing the address is a task that benefits from seeing the order; a sheet overlays only part of the screen.
- **Keep the page or stop it (02).** Sheet: the user edits "18 Harbor Lane, Apt 3" while the order stays visible. Modal: "Delete account?" with the consequence text (orders, returns and 8 saved addresses go with it, cannot be undone), Cancel and a danger-colour Delete, page hidden ("page hidden"). Why: a modal's job is to interrupt; it fits irreversible decisions, not tasks that need reference to the page.
- **Snap points (03 Three heights, nothing between).** Bad: the sheet rests at arbitrary heights (33%, 44%, 36%) marked "free height". Good: three snap points: peek 15% shows a one-line summary ("Delivery · 18 Harbor Lane"), half 50% shows the form, full 92% shows long content (saved-address list Home, Studio, Mum, Locker, Cabin, Office, Jonas, Old flat). Releasing at 38% springs to half. Why: predictable resting states make the sheet feel controlled and each height has a defined content role.
- **Dismiss by speed (04 Speed closes it, not distance).** Bad: distance-only dismissal ("distance only = stuck"): a short quick gesture does nothing. Good: dismiss when velocity exceeds a threshold OR distance exceeds 50%; a 1.4 px/ms flick closes after 80 px, a slow drag returns at 35-40% and closes at 55-60%. Why: users express intent through gesture speed; requiring long travel makes the sheet feel stuck.
- **Desktop drawer width (05 A bounded drawer).** Bad: 240 px (17%) breaks the form fields; 1008 px (70%) hides the order list, the drawer is now a page. Good: about 440 px (31%), list readable beside it. Mobile still uses the sheet ("mobile = sheet"). Why: below 320 px inputs wrap and labels truncate; above 40% the master list loses its usefulness.
- **No stacking (06 One sheet at a time).** Bad: tapping "Saved addresses" opens a second sheet over the first ("sheets open: 2", "2 sheets · which swipe?"). Good: the same sheet replaces its content with the saved-address list and gets a back arrow ("replace content"); one swipe closes everything ("1 swipe · closed"). Why: two stacked sheets make the dismiss gesture ambiguous and bury context.

## Do
- Choose by one question: need the page visible -> sheet (drawer on desktop); need a full stop -> modal.
- Reserve modals for destructive or irreversible confirmations, with the consequence spelled out.
- Define sheet snap points (the reel: 15% / 50% / 92%) and spring to the nearest on release.
- Give each snap point a content role: summary, form, long content.
- Dismiss on velocity above a threshold OR distance beyond 50%.
- On desktop, render the sheet as a side drawer between 320 px and 40% of the viewport width.
- Navigate inside one sheet (replace content, add a back arrow) instead of opening another.

## Don't
- Don't use a modal for a task that needs page context.
- Don't let a sheet rest at arbitrary heights.
- Don't dismiss on distance alone.
- Don't let a drawer go below 320 px or above 40% of the screen.
- Don't stack two sheets.

## Scene by scene
- 0:00 Three phones run the same "Edit delivery address" action: modal, bottom sheet, side drawer.
- 0:01 "Sheets are a system · 01 / Only one fits." Modal labelled "hides context", side drawer "wrong screen", bottom sheet highlighted "keeps context". Footer "context visible = sheet".
- 0:04 "02 Keep the page, or stop it." Order #4821 (arriving Thu, Oct 2, three items) with an address sheet below; choice chips "Need the page? -> Sheet" / "Need a stop? -> Modal"; footer "1 question".
- 0:06 Modal variant dims the page ("page hidden"); then back to the sheet where the street field is edited to "18 Harbor Lane, Apt 3".
- 0:13 "Delete account?" modal over a dimmed page; "Need a stop? -> Modal" highlights.
- 0:19 "03 Three heights. Nothing between." The sheet sits at "33 % ?", "44 % ?", "36 % ?" with a "free height" warning, "snap: none".
- 0:23 Markers "peek 15 %", "half 50 %", "full 92 %" appear; the sheet snaps to peek (summary row), half (form), full (saved-address list).
- 0:31 A release at 38% springs to half. Footer "peek · half · full".
- 0:34 "04 Speed closes it, not distance." Two phones "flick" vs "slow drag"; panel "Dismiss when: velocity > threshold OR distance > 50 %".
- 0:41 Flick at 1.4 px/ms closes after 80 px; slow drag at 35-40% springs back, at 55-60% closes; danger-colour tag "distance only = stuck". Footer "flick = close".
- 0:46 "05 Desktop: a bounded drawer." Orders table (Parcelo, 128 this week) with an "Edit delivery address" drawer at 440 px · 31%; guides "max 40 %" and "min 320 px"; small phone inset "mobile = sheet".
- 0:50 Drawer shrinks to 240 px · 17% ("form breaks"), then grows to 933 px · 65% and 1008 px · 70% ("list gone"), then settles at 440 px · 31%. Footer "320 px <= drawer <= 40 %".
- 0:58 "06 One sheet at a time." Tapping "Saved addresses" stacks a second sheet ("sheets open: 2", "2 sheets · which swipe?"); rewind; instead the same sheet swaps to the saved-address list with a back arrow ("replace content"); one swipe closes it ("sheets open: 0", "1 swipe · closed"). Footer "replace, don't stack".
- 1:08 "07 Five rules. One container.": Context, Snap points, Velocity, Drawer width, No stack.
- 1:10 Promo for the author's paid Claude Code plugin (/ux-design, /ux-audit, /ux-review, /restyle), "Link in bio".

## Voice-over summary
- One action, three containers: a sheet keeps the page visible, a modal hides it behind a scrim; need the order while editing the address -> sheet, need a full stop like deleting the account -> modal.
- A sheet never sits at a random height: three snap points, peek for a summary, half for the form, full for long content; release between two and it springs to the nearest.
- Drag-to-dismiss reads speed, not distance: a quick flick closes from anywhere, a slow drag must cross halfway; "distance alone makes the sheet feel stuck."
- On desktop the sheet becomes a side drawer: at least 320 px or the form breaks, at most 40% or it becomes a page.
- Never stack two sheets: replace the content, add a back arrow, one swipe to leave.

## Notes for the skill
- Platform alignment: iOS `UISheetPresentationController` detents (medium/large, custom) and Material 3 bottom sheets (standard vs modal, with partial/expanded states) match the snap-point idea. "Peek" here is what Material calls a collapsed or peek height.
- Velocity threshold: the reel shows 1.4 px/ms as an example of a flick that closes, not a defined threshold. Common implementations use roughly 0.5-1 px/ms (500-1000 px/s) for fling detection (general practice, not from the reel). Combine with direction: a downward fling at the top snap point steps down one snap point or dismisses depending on design.
- Snap math: on release, project the resting position with velocity (`position + velocity * k`) and pick the nearest detent; animate with a spring. Respect `prefers-reduced-motion` by shortening or removing the spring overshoot.
- Accessibility: drag is not the only way to close or resize. Provide a visible close button (shown in the reel), Escape to close, and a focusable grabber with a label (e.g. "Resize sheet") that toggles detents on Enter/Space (WCAG 2.5.7 Dragging Movements). A modal sheet needs focus trap, `aria-modal="true"`, and focus return to the trigger; a non-modal sheet that keeps the page interactive must not trap focus.
- Destructive modal: name the consequence and use a specific verb button ("Delete"), not "OK"; keep Cancel easily reachable, consistent with WAI-ARIA APG alertdialog pattern (`role="alertdialog"`).
- Drawer width: implement as `width: clamp(320px, <preferred>, 40vw)`; below the point where 320 px exceeds 40% of the viewport (viewport < 800 px), fall back to the bottom sheet or a full-screen view.
- Nested navigation inside a sheet: keep a small view stack inside the one container; the back arrow pops it, the close button or swipe dismisses the whole sheet. Manage focus to the new view's heading on each replacement.
- Peek 15% must still leave the summary readable and the grabber at least 44x44 pt as a touch target.
- The last 15 seconds are an advert for the author's paid plugin; no UX rule there.
