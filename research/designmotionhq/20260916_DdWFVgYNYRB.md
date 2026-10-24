---
id: DdWFVgYNYRB
reel_url: https://www.instagram.com/reel/DdWFVgYNYRB/
pattern_page: none
date: 2026-09-16
duration_s: 76
type: ui
category: content
topic: chat / message thread UI system (grouping, timestamps, optimistic send, scroll anchoring, typing, composer)
sources: frames, voice-over, caption
---

# Chat UI as a system: six decisions that make a thread readable

**Caption:** Same thread, half the noise: six decisions make a chat UI read (ends with a plug for the author's Claude Code plugin).
**Hook:** A chat UI is a system of six decisions; the same thread can carry half the visual noise.

## Main rule
Group consecutive messages from the same sender within a short window under one avatar with tight internal spacing, show dates as dividers and exact times only on demand, render sent messages instantly with inline failure and retry, never yank the scroll position while the user reads, put the typing indicator in the message flow, and let the composer grow to a fixed maximum before scrolling.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 6 decisions | grouping, timestamps, optimistic send, scroll anchoring, typing indicator, composer | 0:00 voice, 0:02 badge "6 decisions", 1:01 recap |
| 13 avatars -> 6 | avatar count in the same thread, naive vs grouped | 0:00-0:04 on-screen pill |
| 39 % shorter | thread height after all decisions (badge; voice says "half the noise") | 0:04 on-screen badge |
| 2 min | grouping window: same sender within this time = one group | 0:05-0:13 on-screen "Grouping window 2 min"; voice "under two minutes" |
| 4 px | gap between messages inside a group | 0:08-0:13 on-screen + voice |
| 16 px | gap between groups | 0:10-0:13 on-screen + voice |
| 43 % shorter | height of the grouped two-sender example vs ungrouped | 0:07-0:13 on-screen |
| exact time on hover (e.g. 10:43, 10:45) | per-message timestamp revealed in the gutter on hover | 0:19-0:22 on-screen |
| Enter keypress -> bubble in list 0 f -> Sent +12 f | optimistic send timeline in frames: bubble appears at frame 0, "Sent" state about 12 frames later | 0:23-0:33 on-screen |
| 0 spinners | no spinner between the user and their sent message | 0:23-0:33 on-screen |
| 0 px shift | list position while new messages arrive and the user is scrolled up | 0:35-0:39 on-screen |
| "3 new messages" | count pill shown when scrolled up | 0:36-0:39 on-screen |
| 0 px moved | other messages when the typing indicator leaves | 0:50-0:51 on-screen |
| max 5 lines | composer auto-grow limit, then internal scroll | 0:52-1:00 on-screen + voice |
| Enter = send, Shift+Enter = new line | composer keys | 0:53-1:00 on-screen hints + voice |
| spec-v3.pdf 2.4 MB | example attachment chip shown above the text | 0:58-1:00 on-screen |
| 12 members | channel header count (demo) | throughout |

## Before / after
- **Grouping (Naive vs grouped).** Bad: every message gets its own avatar, name and timestamp (13 avatars). Good: consecutive messages from one sender within 2 minutes collapse under one avatar and name, 4 px between lines inside a group, 16 px between groups (6 avatars, 39% shorter thread). Why: proximity (Gestalt) makes each group read as one speaker turn; the reader scans people, not individual lines.
- **Timestamps (Precision on demand).** Bad: a time on every bubble. Good: a "Yesterday" / "Today" divider when the date changes; the exact time appears in the left gutter only when hovering a line ("exact time, on hover"). Why: most of the time readers need only the rough sequence; repeated timestamps are noise.
- **Optimistic send (The bubble lands first).** Bad: a spinner sits where the message should be until the server confirms. Good: Enter puts the bubble in the list immediately (frame 0); a small "Sent" status fades in afterwards (+12 frames). If sending fails, the message stays in place with "Not sent" and a "Retry" control on that message ("retry stays on the message"). Why: zero perceived latency; the user's own words are never hidden; the failure is attached to the exact message that failed.
- **Scroll anchoring (The list does not jump).** Bad: incoming messages auto-scroll the list while the user reads older content. Good: when scrolled up, the list holds still (0 px shift) and a "3 new messages" pill counts arrivals; tapping it slides to the bottom. Only when the user is already at the bottom does the list follow new messages ("scrolled up -> pill", "at bottom -> follow"). Why: moving content under a reader breaks their place and can cause mis-taps.
- **Typing indicator (Typing lives in the flow).** Bad: a "Sam is typing..." bar above the composer (crossed out on screen, "not a bar above the composer"). Good: three animated dots with the sender's avatar appear in the thread where the next message will land ("next message lands here", "avatar attached"); the real message replaces it, and when it leaves nothing else moves (0 px moved). Why: it previews location and author of the next message and avoids layout jumps around the composer.
- **Composer (Five lines, then it scrolls).** Good: the input grows line by line up to 5 lines (badge "max 5 lines"), then scrolls internally; Enter sends, Shift+Enter inserts a line break (hints shown in the composer); attachments preview as chips above the text, never inside it. Why: the composer stays usable for long messages without eating the thread; keyboard conventions match user expectations.

## Do
- Group consecutive messages by sender within about 2 minutes; show avatar and name once per group.
- Use about 4 px between lines inside a group and about 16 px between groups.
- Insert date dividers on date change; reveal exact time on hover (and on focus / long-press).
- Append the sent message immediately with a pending state; mark "Sent" afterwards.
- Show failure inline on the message with a retry action.
- Freeze scroll position when the user is scrolled up; show a "N new messages" pill that jumps to the bottom.
- Auto-follow new messages only when the user is already at the bottom.
- Show typing as an in-flow row with the typer's avatar at the insertion point.
- Auto-grow the composer to 5 lines, then scroll; Enter sends, Shift+Enter breaks.
- Preview attachments above the text field.

## Don't
- Don't repeat avatar, name and time on every message.
- Don't show a spinner in place of the user's own message.
- Don't report send failures only in a toast detached from the message.
- Don't auto-scroll a user who is reading history.
- Don't put the typing indicator in a bar that pushes the composer or list around.
- Don't put attachment previews inside the text area.

## Scene by scene
- 0:00 "Chat UI is a system · 01". A #design channel (Halo · Product design) labelled "Naive": every message by Maya Chen, Leo Park and Sam Okafor has its own avatar and time; pill "13 avatars -> 13".
- 0:02 Badge switches to "6 decisions"; messages merge into groups, a "Yesterday" section appears; pill counts down to 7, then 6; badge "39 % shorter".
- 0:05 "02 Same sender, one avatar." Three ungrouped Maya Chen messages collapse into one group; "43 % shorter" measure; panel "Grouping window 2 min", "inside a group 4 px", "between groups 16 px"; timeline 10:42-10:46 marks "one group" and "new group". Footer "1 sender = 1 avatar".
- 0:14 "03 Precision on demand." Thread rebuilds with "Yesterday" and "Today" dividers and no per-line times; hovering a line shows its exact time (10:43, then 10:45) in the gutter with the tag "exact time, on hover". Footer "Divider on date change · time on hover".
- 0:23 "04 The bubble lands first." Typing "Shipping the new onboarding today" and pressing Enter: bubble appears at once, "Sent" fades in; timeline "Enter keypress -> Bubble in list 0 f -> Sent +12 f"; badge "0 spinners".
- 0:28 A second message "Can you review PR 412?" fails: outlined in the danger colour with "Not sent" and "Retry" under it, tag "retry stays on the message".
- 0:34 "05 The list does not jump." User scrolled up in history; "0 px shift" marker; a "3 new messages" pill appears near the bottom and is clicked, sliding to the latest messages. Toggle chips "scrolled up -> pill" / "at bottom -> follow"; at the bottom new messages (Ines Duarte "Standup moved to 11:15 tomorrow", Leo Park "Noted, thanks") just append.
- 0:43 "06 Typing lives in the flow." Strike-through example "Sam is typing..." labelled "not a bar above the composer"; instead three dots under Sam Okafor's avatar in the thread ("next message lands here", "avatar attached"), replaced by his message; "0 px moved".
- 0:52 "07 Five lines, then it scrolls." Composer grows as a numbered recap is typed (lines 1-5), badge "max 5 lines", hints "Enter send", "Shift + Enter new line"; at 0:58 an attachment chip "spec-v3.pdf 2.4 MB" appears above the text. Footer "max 5 lines · attachments above".
- 1:01 "08 Six decisions. One thread that reads." Recap tiles: Grouping, Timestamps, Optimistic send, Scroll anchoring, Typing indicator, Composer.
- 1:03 Promo for the author's paid Claude Code plugin (commands /ux-design, /ux-audit, /ux-review, /restyle), "Link in bio".

## Voice-over summary
- A chat UI is a system of six decisions; the same thread with half the noise.
- Same sender under two minutes is one group with one avatar: 4 px inside, 16 px between groups; "the reader scans people, not lines."
- No time on every bubble: a date divider on date change and the exact time only on hover.
- Enter puts the bubble there immediately and the sent state fades in after; failure shows a retry inline on the message, never a spinner in front of your own words.
- New messages while reading: the list does not jump, a pill counts them; anchoring only when already at the bottom.
- Typing indicator sits in the flow with the avatar and leaves without moving anything; composer grows to five lines then scrolls, Enter sends, Shift+Enter breaks, attachments above the text.

## Notes for the skill
- Grouping key: same `senderId` and `createdAt - previous.createdAt < 2 min` and same day; break the group on a date divider or after a system message. Render the timestamp of the group head next to the name, as the reel does.
- Hover-only exact time is not reachable on touch or by keyboard: expose it on focus (`:focus-within`), on long-press, and in an accessible name or `<time datetime>` element so screen readers can read it. WCAG 1.4.13 applies if it is a hover popup (dismissible, hoverable, persistent).
- Optimistic send states: `pending -> sent -> (delivered/read)` and `pending -> failed`; keep a client id to reconcile the server echo and dedupe; reuse the same client id on retry so the server can treat it idempotently. "+12 f" is about 200 ms at 60 fps (calculation, assuming 60 fps; the reel shows only frames).
- Scroll anchoring: track `isAtBottom` (distance from bottom under a small threshold, e.g. 40-80 px); when false, append without changing `scrollTop` and increment an unread counter. CSS `overflow-anchor: auto` helps when content is inserted above; for prepending history in a reversed list, preserve the offset manually.
- Screen readers: announce new messages through a polite live region (`role="log"` on the message list), but throttle so a busy channel does not flood announcements; the pill needs an accessible label like "3 new messages, jump to latest".
- Typing indicator: render it as the last item of the list, reserve its height only while present, and respect `prefers-reduced-motion` for the bouncing dots (static ellipsis). Do not announce every typing start to screen readers.
- Composer: `rows` auto-grow with `max-height` = 5 x line-height, then `overflow-y: auto`. Enter-to-send must not fire during IME composition (`event.isComposing`); on mobile soft keyboards Enter usually inserts a newline and a send button is the primary action.
- The failed-message styling uses the danger colour; pair it with the "Not sent" text and icon, not colour alone.
- The final 13 seconds are an advert for the author's paid plugin; no UX rule there.
