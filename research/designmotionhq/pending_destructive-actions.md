---
id: unknown
reel_url: unknown
pattern_page: https://designmotionhq.com/patterns/destructive-actions
date: unknown
duration_s: 55
type: ui
category: interaction
topic: destructive actions: hold-to-confirm, verb labels, placement, danger-colour budget, danger zone, cooldown
sources: frames, voice-over, pattern page
---

# Destructive actions as a design language

**Caption:** not captured yet
**Hook:** Hold to delete; let go early and nothing is deleted.

## Main rule
Protect destructive actions with friction that is built into the control itself rather than a generic "Are you sure?" dialog: a press-and-hold commitment, buttons labelled with the actual verb and object, a position away from where the primary/confirm button normally sits, the danger colour reserved exclusively for destruction, a bordered "Danger zone" at the end of settings, and a cancelable grace period for irreversible deletions.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| hold 300 ms | hold-to-delete commitment time (button sublabel "hold 300 ms") | 0:00 on-screen, 0:04 voice |
| 6% / 41% / 0% | hold progress readouts; released at 41% -> "Released" -> "Nothing deleted", file marked "Kept" | 0:00-0:02 on-screen |
| 0 / 100 / 200 / 300 ms | "Commitment window" timeline under the ring | 0:03-0:09 on-screen |
| 0 -> 164 -> 300 ms, "fired at 300 ms" | full hold completes and fires | 0:04-0:07 on-screen |
| 29 ms, 16 ms, then 0 ms "released, never fired" | early release cancels | 0:07-0:09 on-screen |
| "clicked in 0.4 s, read nothing" | time a user takes to click a generic "Yes" | 0:11-0:12 on-screen |
| 84 assets | dialog body: "permanently removes Q3 Campaign and its 84 assets for everyone on the team" | 0:10-0:17 on-screen |
| 6 -> 4 -> 1 | count of danger-coloured elements on one settings card (target: 1) | 0:28-0:33 on-screen |
| 14 days | cooldown / grace period before permanent account deletion | 0:43 voice, 0:41-0:47 on-screen |
| 14 -> 9 -> 5 -> 3 days to cancel | countdown states; low values shown in a warning colour | 0:41-0:46 on-screen |

## Before / after
- **"Are you sure?" dialog vs hold-to-confirm.** The dialog (crossed out on screen) is dismissed by habit. With hold-to-delete, a ring fills during a 300 ms press; the action fires only when the ring completes, and releasing before that cancels with nothing deleted. The gesture itself is the confirmation, so there is no extra modal to click through, and the commitment cannot happen by a single accidental tap.
- **"Yes / No" vs "Keep project / Delete project".** Same dialog body. With Yes/No the cursor clicks "Yes" in 0.4 s without reading. With the verb on the button (title "Delete this project?", buttons "Keep project" and a danger-styled "Delete project"), the label itself carries the consequence, so even a user who skips the body text reads the warning on the button they are about to press.
- **Delete in the primary spot vs delete moved away.** In "Close editor? You have unsaved changes in draft-hero.fig", the bad version puts "Delete draft" in the bottom-right primary position, so a habitual click on that spot deletes the draft ("Draft deleted, blind click"). The good version puts "Save draft" in the primary position and moves "Delete draft" to a separate outlined button above/left of the button row; the same blind click now saves ("Draft saved, same click"). Muscle memory targets position, so the safe action must own the habitual position.
- **Danger colour everywhere vs danger colour budget.** A settings card shows 6 danger-coloured elements: active tab underline, notification badge, a "Trial expired" banner, "Log out all", a toggle in the on state, and "Delete account". They are recoloured one by one to neutral until only the "Delete" button keeps the danger colour (6 -> 4 -> 1). When the colour is used for routine items it stops signalling danger and the real delete looks ordinary ("cries wolf").
- **Danger zone.** In a repository settings page (GitHub-style example), destructive actions sit only after scrolling past General, Features, Pull requests and Notifications, inside a bordered, labelled "Danger Zone" block: Transfer ownership, Archive this repository (described as reversible), Delete this repository (described as permanent, all issues, releases and CI history gone). Distance and the container act as friction and as a clear "you are in risky territory" signal.
- **Cooldown.** "Account scheduled for deletion" card with a "Scheduled" badge, the account email, "permanent on Jul 27", a large "14 days to cancel" counter and 14 day cells that cross out as days pass (14 -> 9 -> 5 -> 3; the number turns to a warning colour when low). A full-width primary "Cancel deletion" button; pressing it switches the badge to "Cancelled" and resets the counter. Time gives the user a last chance to reverse an irreversible action.

## Do
- Use press-and-hold with a visible progress ring for destructive actions where a modal would be habitual; cancel on early release.
- Label buttons with verb + object ("Delete project" / "Keep project"); name the object and the scope of loss in the dialog title and body (e.g. how many items, for whom).
- Put the safe action in the habitual primary position and move the destructive action out of it.
- Reserve the danger colour for destructive actions only; one danger-coloured element per view is the target shown.
- Group destructive settings at the end of the page in a bordered, titled "Danger zone"; distinguish reversible (archive) from permanent (delete) in the descriptions.
- For account or workspace deletion, schedule it with a grace period (14 days shown), show the exact final date, and keep a prominent "Cancel deletion" action.

## Don't
- Don't rely on a generic "Are you sure?" with Yes/No.
- Don't place a destructive button where Confirm/Save normally sits.
- Don't use the danger colour for logout, notification badges, upsell banners, active tabs or toggles.
- Don't put destructive actions at the top of settings or mixed in with routine options.
- Don't delete accounts immediately when a delay is feasible.

## Scene by scene
- 0:00 "Hold to delete." A file card (brand-refresh.fig, 38 MB) and a "Hold to delete / hold 300 ms" button; a ring and a bar fill (6%, "Holding"), the cursor releases at 41% ("Released"), the bar empties, "Nothing deleted" and the file shows a "Kept" badge.
- 0:03 "Pattern 01 Hold: The ring is the confirmation." Left "Before: dialog" ("Are you sure? This action cannot be undone", Cancel/Delete) gets crossed out; right "After: hold" ring counting ms with a trash icon, and a "Commitment window" scale 0-300 ms. Ring fills 0 -> 164 -> 300 ms, tag "fired at 300 ms"; then a short press at 29 ms / 16 ms drops back to 0, "released, never fired". Caption: release early, nothing fires.
- 0:10 "Pattern 02 Labels: Name the action." "Are you sure?" dialog about Q3 Campaign and its 84 assets, No / Yes; cursor clicks Yes, tag "clicked in 0.4 s, read nothing".
- 0:14 Dialog changes to "Delete this project?" with "Keep project" and a danger-styled "Delete project"; chips: "Yes", clicked blind vs "Delete project", read first. Caption: the verb is the warning.
- 0:19 "Pattern 03 Placement: Off the happy path." Two "Close editor?" dialogs; left "Delete in primary spot" (Cancel, Delete draft at bottom right), right "Delete moved away" (Delete draft as a separate outlined button above; Cancel, Save draft at bottom right). A dashed cursor path hits the same spot in both: "Draft deleted, blind click" vs "Draft saved, same click". Caption: muscle memory clicks blind.
- 0:27 "Pattern 04": title framing the danger colour as a budget. Settings card with 6 danger-coloured elements and an on-screen counter of danger-coloured elements at 6; elements turn neutral, counter goes to 4 then 1 (only Delete account keeps it). Caption: spend it on destruction only.
- 0:34 "Pattern 05 Danger zone: Bury it at the bottom." Repository settings (acme/design-kit) scroll from General down to a bordered "Danger Zone" with Transfer, Archive, Delete; the Delete row is emphasised. Caption: geography is friction.
- 0:41 "Pattern 06 Cooldown: The last line of defense." "Account scheduled for deletion" card, 14 days to cancel, day cells crossing out (9, 5, 3), cursor presses "Cancel deletion", badge becomes "Cancelled", counter back to 14. Caption: 14 days to change your mind.
- 0:48 Summary grid "Danger is a design language": Hold to confirm, Verb labels, Off the happy path, colour budget (danger colour for destruction only), Danger zone, Cooldown; follow button.

## Voice-over summary
- Holding is the confirmation: about 300 ms of commitment replaces a dialog, and releasing early never fires the action.
- Nobody reads "Are you sure? Yes"; name the action ("Delete project", "Keep project") because "the verb is the warning".
- Destructive buttons must not sit where confirm lives, because muscle memory clicks primary spots without looking.
- The danger colour is a limited budget; a danger-coloured logout button makes the real delete look routine.
- A GitHub-style danger zone (bordered, labelled, last on the page) turns location into friction.
- Some platforms add a cooldown (deletion scheduled, 14 days to cancel); time is the final safeguard.

## Notes for the skill
- 300 ms hold is very short. It filters out taps but not a slow click or a press-and-drag; many production hold-to-confirm controls use roughly 1-2 s for high-stakes actions. Treat 300 ms as the minimum shown in the reel, and scale the hold time with severity (my recommendation, not from the video).
- Hold interactions need alternatives: screen-reader users activate with a double-tap/click that cannot be "held", and some motor-impaired users cannot sustain a press. Provide a keyboard path (hold Space/Enter, or a focused button that opens a confirm step) and an alternative confirmation for assistive tech. Fire on completion and cancel on pointer-up/pointercancel/blur (fits WCAG 2.5.2 Pointer Cancellation). Announce progress/completion via `aria-live`, and give the button an accessible name that states the gesture ("Hold to delete brand-refresh.fig").
- Reduced motion: the ring can still fill (it is functional progress), but avoid extra pulsing/glow.
- Confirmation dialogs: use `role="alertdialog"` with `aria-labelledby`/`aria-describedby`; put initial focus on the safe action (Cancel/Keep), not on the destructive button (WAI-ARIA APG alert dialog guidance). Esc should equal the safe action.
- Button order varies by platform (macOS/iOS put the primary on the right, Windows often on the left); the rule is "the destructive action is never the default/primary position and never the Enter-key default", not a fixed side.
- Danger colour must not be the only cue: pair it with an icon, the verb label and position; meet 4.5:1 text contrast on danger buttons (WCAG 1.4.1 Use of Color, 1.4.3).
- For high-stakes deletions combine with typed confirmation (type the project name) or undo when the action is actually reversible; prefer undo (soft delete + toast) for frequent, recoverable deletions and reserve friction for truly irreversible ones.
- Cooldown: show the exact date and time zone of permanent deletion, send a notification/email with a cancel link, and make "Cancel deletion" reachable from sign-in. The low-day warning colour in the reel should be paired with text, not colour alone.
