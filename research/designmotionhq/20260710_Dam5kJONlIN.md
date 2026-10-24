---
id: Dam5kJONlIN
reel_url: https://www.instagram.com/reel/Dam5kJONlIN/
pattern_page: https://designmotionhq.com/patterns/undo-ux
date: 2026-07-10
duration_s: 51
type: ui
category: feedback
topic: undo instead of confirmation: undo toast, soft delete, type-to-confirm for irreversible, undo stack, delayed send
sources: frames, voice-over, pattern page
---

# Undo UX: design for regret

**Caption:** Undo on delete actions
**Hook:** "Deleted. You have 5 seconds." The file disappears immediately and an Undo toast offers the way back.

## Main rule
For reversible actions, execute immediately and offer a time-limited Undo (with a visible countdown) instead of an "Are you sure?" dialog; implement deletion as a soft-delete state with a recovery window (30 days in trash, then purge); reserve heavy friction such as type-to-confirm for truly irreversible actions; keep a multi-step undo stack (Cmd/Ctrl+Z) in editors; and use a short send delay (10 s) where the action leaves your system.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 5 seconds | undo window on the delete toast | 0:00 voice, 0:01 on-screen "You have 5 seconds" |
| 3 clicks, every time vs 1 click, regret optional | confirm-dialog flow vs undo flow | 0:02-0:10 on-screen |
| "Punish the 1%" | share of users who make the mistake (rhetorical) | 0:04-0:10 on-screen caption |
| day 0 -> 30 days -> purged | soft-delete lifecycle: Deleted, Trash (30 days), Purged "gone for real" | 0:11-0:18 on-screen, 0:12 voice |
| `deleted_at = "2026-07-03T10:42Z"` vs `null` | soft-delete flag in the database row | 0:12-0:18 on-screen |
| friction scale: Undo (reversible) -> Confirm (annoying) -> Type to confirm (irreversible) | matching friction to cost | 0:19-0:27 on-screen |
| Cmd + Z x1, x2, x3 | undo stack walking back three steps | 0:28-0:37 on-screen |
| 10 seconds (countdown 10s, 9s, 8s, 7s, 6s) | delayed-send grace period with Undo | 0:38 voice, 0:38-0:44 on-screen |

## Before / after
- **Confirm dialog vs undo.** Same file (report.pdf). Confirm: click delete, a "Delete this file? This action can't be undone. Are you absolutely sure?" dialog appears, click Delete (tag "3 clicks, every time"). Undo: one click removes the file and shows a "Deleted" toast with a countdown icon and Undo ("1 click, regret optional"). The dialog taxes every user on every delete to protect the few who misclick, and habituated users click through it anyway; undo costs nothing for the majority and still rescues the mistake after the fact, when the user actually notices it.
- **Hard delete vs soft delete.** "What the user sees": Q3-report.pdf disappears from the list. "What the database sees": the row stays, its `deleted_at` changes from null to a timestamp. A timeline shows Deleted (day 0) -> Trash (30 days) -> Purged; at the end the row is struck out. Treating deletion as a state makes undo, trash and restore possible without backups.
- **Undo vs type-to-confirm.** Some actions cannot be reversed (deleting a repository with its issues and CI history). Here the dialog states "This cannot be undone", asks to type `acme/production-api`, and the danger-styled "I understand, delete this repository" button activates only after the name is typed. A friction scale slider moves from Undo to Confirm to Type to confirm. Friction should be proportional to the cost of a mistake, and placed only where no undo exists.
- **Single undo vs undo stack.** An editor with a History panel (Create frame, Add rectangle, Move rectangle, Add ellipse, Draw line). Pressing Cmd+Z removes Draw line (x1), then Add ellipse (x2), then moves the rectangle back (x3), each history entry greying out in order. One undo is a toast; a stack lets users explore freely because any sequence can be walked back.
- **Delayed send.** An email ("Q3 final numbers", body with a typo "finel") is sent; a "Sending..." bar counts down from 10s with an Undo button. At 6s Undo is pressed, the draft returns, the typo is highlighted and corrected to "final". The delay converts an irreversible external action into a reversible one for a short window.

## Do
- Execute reversible destructive actions immediately and show an Undo toast with a visible countdown.
- Implement delete as a soft-delete flag plus a trash/recovery period (30 days shown) before permanent purge.
- Reserve type-to-confirm for actions with no recovery path, and state exactly what will be lost.
- Provide a multi-level undo stack (Cmd/Ctrl+Z, and redo) for editing tools, with history visible where useful.
- Add a short hold-back window (10 s shown) before irreversible outbound actions such as sending a message.

## Don't
- Don't put an "Are you sure?" dialog in front of every destructive action.
- Don't hard-delete rows the moment the user clicks.
- Don't use type-to-confirm for actions that could simply be undone.
- Don't limit editing to a single undo step.
- Don't make the undo window so short that users cannot react (the page's own caution).

## Scene by scene
- 0:00 "Deleted." File list (Q2-report.pdf, Q3-report.pdf, budget.xlsx); Q3-report.pdf is deleted and slides out; a "Deleted" toast with a circular countdown and Undo appears. 0:01 subtitle "You have 5 seconds"; the cursor clicks Undo. Caption: reversibility beats confirmation.
- 0:02 "Undo beats confirm: One mistake. Two designs." Left "Confirm" panel: delete opens "Delete this file?" dialog, Delete clicked ("3 clicks, every time"). Right "Undo" panel: one click, file gone, "Deleted / Undo" toast ("1 click, regret optional"). The loop repeats. Caption: punish the 1%, or protect them.
- 0:11 "Soft delete: Off the screen, not the database." Top: files list as the user sees it (Q3 removed). Bottom: database table with id, name, deleted_at; row 42 q3-report.pdf gets a timestamp. Lifecycle bar: Deleted (day 0) -> Trash (30 days) -> Purged (gone for real); at 0:18 the row is struck out. Caption: deletion is a state, not an event.
- 0:19 "Type to confirm: Earn the irreversible." "Delete repository acme/production-api" card with a danger notice ("cannot be undone; repository, issues and CI history permanently deleted"), input "Type acme/production-api to confirm", disabled danger button; the name is typed letter by letter and at 0:24 the button "I understand, delete this repository" becomes active. Friction scale slider moves Undo -> Confirm -> Type to confirm. Caption: match friction to the cost.
- 0:28 "The undo stack: A stack is a time machine." Canvas with a rectangle, circle and line plus a History panel; Cmd + Z key caps with a counter x0 -> x1 -> x2 -> x3; the line, then the circle disappear, then the rectangle moves back; history rows grey out. Caption: Figma remembers, your app can too.
- 0:38 "Delayed send: The 10-second grace period." Email compose (to team@acme.co, "Q3 final numbers", attachment Q3-report.pdf); Send is clicked; "Sending..." bar with countdown 10s -> 6s and Undo; the typo "finel" gets highlighted; Undo clicked at 6s; draft returns and the word becomes "final". Caption: the delay is the feature.
- 0:47 Outro "Undo UX, reversibility: Design for regret." with a "Deleted / Undo" toast and follow/save prompts.

## Voice-over summary
- "Are you sure?" punishes everyone for one person's mistake; undo punishes nobody: the action happens instantly and regret gets a second chance.
- A deleted file left the screen, not the database: a deleted flag, 30 days in trash, then gone for real; deletion is a state, not an event.
- Some actions have no way back, and that is where friction belongs; GitHub makes you type the repo name before deleting ("Earn the irreversible").
- One undo is a toast, a stack is a time machine: Cmd+Z walks back every step in order, as Figma does.
- Gmail holds a sent email for 10 seconds; the delay catches the typo, the wrong recipient, the reply-all disaster.

## Notes for the skill
- Undo toast accessibility: announce it with `role="status"`/`aria-live="polite"`; the Undo button must be reachable by keyboard without losing it to the timer. Pause the countdown on hover and on focus, and make the window long enough or adjustable (WCAG 2.2.1 Timing Adjustable). A 5 s window is on the short side for screen-reader and motor-impaired users; common guidance is roughly 5-10 s, and the page itself warns against windows too short to react. Provide a persistent recovery path (Trash / "Recently deleted") so the toast is not the only chance.
- Show the countdown visually (draining ring or bar), but keep it decorative for assistive tech (do not announce every second).
- Support Cmd/Ctrl+Z as an alternative to the toast button for the most recent action where it does not conflict with text editing.
- Implementation of the immediate action: either perform it and reverse on Undo (soft delete makes this trivial) or delay the server commit until the toast expires; with the delayed-commit approach, flush pending actions on page unload so nothing is silently lost, and handle conflicts if another user touched the item.
- Soft delete: filter `deleted_at IS NULL` everywhere (queries, search, counts), purge with a scheduled job after the retention window, and consider legal deletion requirements (e.g. user-requested erasure may need true deletion sooner). Tell users the retention period in the Trash UI.
- Type-to-confirm: allow paste, trim whitespace, show the exact string in a copyable monospace element, and do not rely on a disabled button alone to explain the requirement (link the instruction via `aria-describedby`). The repo-name example is GitHub's flow, cited by the narrator.
- Undo stack: pair with redo (Shift+Cmd+Z / Ctrl+Y), group rapid micro-changes into one step (e.g. typing bursts, drags), and clear redo history when a new action is taken.
- Delayed send: label the state ("Sending in 6 s... Undo"), keep the window short (Gmail's default 5 s is configurable up to 30 s; the reel says 10 s), and show a definitive "Sent" state afterwards.
- "3 clicks every time" for the confirm flow is the reel's own count; a typical delete + confirm is two clicks. The point (constant tax on every user) stands regardless.
