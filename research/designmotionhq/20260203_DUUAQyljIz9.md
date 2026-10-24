---
id: DUUAQyljIz9
reel_url: https://www.instagram.com/reel/DUUAQyljIz9/
pattern_page: none
date: 2026-02-03
duration_s: 55
type: ui
category: feedback
topic: Typing indicator as an engagement dark pattern
sources: frames, voice-over, caption
---

# Typing indicators: honest status vs engagement trap

**Caption:** "How do you feel knowing that?" (design-psychology reel, no further text).
**Hook:** The "..." typing dots are claimed to be engineered to keep you staring at the chat.

## Main rule
A typing / "thinking" indicator must mirror real state: show it only while input is actually being produced and remove it as soon as the content arrives or the activity stops. Padding its duration with artificial delay, or cycling it to hold attention, turns a feedback element into a manipulation pattern.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 1.5 s | time the sender actually spent typing "yes" | 0:05-0:10 on-screen counter + voice ("about one and a half seconds") |
| 6 s | time the typing indicator stayed visible for the same reply | 0:10-0:13 on-screen card + voice |
| 4x | indicator vs real typing ("4x longer than reality") | 0:10-0:13 on-screen |
| 0.1 s / 0.2 s, 0.8 s / 1.3 s, 1.5 s / 2.5 s, 1.5 s / 3.6 s, 1.5 s / 4.8 s | running timers, real typing vs indicator, as the two bars fill | 0:04-0:08 on-screen |
| `await delay(4000)` (4000 ms) | code snippet: `showTypingIndicator(); await delay(4000); sendMessage(text);` | 0:15-0:16 on-screen |
| 3 | "secrets" (fake duration, anxiety engine, ghost typing) | section labels SECRET #1-#3 |

Note: the code snippet's 4000 ms delay does not match the 6 s figure in the comparison; the reel does not reconcile them.

## Before / after
The reel shows only the manipulative versions; the honest counterpart is implied.
- **Fake duration.** Bad: the indicator is shown, then an artificial delay is awaited before the message is delivered, so dots run about 4x longer than real typing. Honest version: indicator lifetime equals the real activity; the message renders the moment it exists. Why: perceived latency should reflect real latency; inflated waits waste user time and erode trust once noticed.
- **Anxiety loop.** Bad: dots appear, message arrives (relief), new dots appear again, keeping the user in a stress / relief / repeat cycle. Why it works on people: an unresolved pending state holds attention (anticipation). Honest version: avoid re-triggering a pending indicator just to hold attention; let the conversation reach a resolved state.
- **Ghost typing.** Shown: dots appear under "What do you think?", vanish, nothing is sent; repeated three times ("Ghost #3 - Still nothing..."). The reel frames this as the other person typing and deleting. Implication for builders: an indicator that disappears without content leaves an ambiguous state; if you show typing presence at all, expire it cleanly and do not imply a message is coming.

## Do
- Bind the typing indicator to a real signal (keystrokes / stream in progress) with a short idle timeout.
- Remove the indicator the instant the message or streamed content arrives.
- For AI chat, stream tokens as they are generated instead of holding a finished answer behind "typing" dots.
- If a delay is a deliberate product choice, keep it short and never present it as someone working.

## Don't
- Don't insert `delay()` between "indicator on" and "message shown" to make replies feel "thoughtful".
- Don't cycle pending indicators repeatedly to keep users watching.
- Don't leave dots on screen after the activity has stopped.

## Scene by scene
- 0:00 Dark screen, a single typing-dots bubble pulses; floating chat, timer, brain icons. Text: why do you stare at these, they're designed to trap you, here's how.
- 0:04 SECRET #1 "Fake Duration": two rows, "Real Typing" (input field fills to "yes") vs "Indicator Shows" (dots bubble), each with a progress bar and timer (0.1/0.2 s up to 1.5/4.8 s).
- 0:10 Two stat cards: 1.5s Real typing vs 6s Indicator, caption "4x longer than reality".
- 0:15 Code card `showTypingIndicator(); await delay(4000); sendMessage(text);` with caption "Apps add artificial delay to make typing feel 'thoughtful'".
- 0:17 SECRET #2 "Anxiety Engine": dots bubble grows, "Your heart rate increases..."; then glowing brain icon, "Your brain releases dopamine while waiting for the message".
- 0:30 Three-step loop row: dots (Stress) -> "Hey!" (Relief) -> dots (Repeat), steps highlight in turn; text "Relief. New dots. Repeat."
- 0:35 SECRET #3 "Ghost Typing": phone mockup, sent bubble "What do you think?", dots appear ("Waiting..."), then vanish ("Gone. Nothing sent.").
- 0:43 Second phone: "Are we still on for tomorrow?", dots flicker on and off, three ghost icons fill up, "Ghost #3 - Still nothing...".
- 0:50 Dots bubble pulses alone, fades; end card "@designmotionhq, follow for more design manipulation".

## Voice-over summary
- Typing "yes" takes about 1.5 s, yet the indicator stays for 6 s; apps are said to add artificial delay so responses seem more considered and keep you on screen.
- When dots appear, the narrator claims heart rate rises and dopamine is released in anticipation; the reply brings relief, new dots bring stress again.
- This stress / relief cycle is described as a loop built to keep you watching.
- Ghost typing: dots appear and vanish because someone started typing, deleted it and left, while you keep watching.
- Closing: "Follow for more design manipulation."

## Notes for the skill
- Implementation: typing presence should be event-driven (e.g. emit `typing:start` on input, `typing:stop` on send or after about 3-5 s idle; this timeout is general practice, not a number from the reel). Render streamed content progressively rather than gating it.
- Accessibility: announce new messages via a polite live region (`aria-live="polite"`), not each typing-indicator toggle; repeated announcements of "typing" are noise for screen-reader users. Under `prefers-reduced-motion`, replace bouncing dots with a static "typing..." label.
- Claims to treat with caution: the heart-rate and dopamine statements are presented without evidence and are pop-psychology simplifications. The "apps add artificial delay" claim is not documented for person-to-person messengers (their indicators are driven by real keystrokes plus a timeout, which also explains "ghost typing"); deliberate delays are more typical of chatbots and customer-support bots. The 4000 ms code snippet and the 6 s on-screen figure disagree.
- Use this reel as an anti-pattern reference: feedback indicators must be truthful about system state (Nielsen heuristic "visibility of system status").
