---
lesson: 112
kind: video
duration_s: 54
type: ui
category: interaction
topic: hold-to-record voice message button (instant feedback, cancel threshold, lock, live waveform, scrubbable playback)
sources: frames, voice-over
---

# Voice message button: five decisions behind hold to record

**Hook:** Hold to record, slide to cancel: a small control that hides five design decisions.

## Main rule
A press-and-hold recorder must (1) confirm recording on the same frame as the press, visibly beyond the thumb (timer starts, button swells past the finger); (2) define a fixed cancel line on the horizontal drag, past which the hint turns into a trash icon and release deletes instead of sends; (3) let a vertical slide lock recording so the thumb is free, replacing the gesture with explicit stop and send buttons; (4) show a live input waveform and warn when it stays flat (muted mic); (5) render the received message as a scrubbable waveform with visible length and playback speed.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| Same frame, before a sound | timer and button swell appear on press, before the user speaks | 0:03-0:10 on-screen checklist ("Timer + swell") + voice |
| 0:00 → 0:06 | recording timer counting from the moment of press in the "past the thumb" demo | 0:04-0:10 on-screen |
| Fixed cancel line | threshold on horizontal drag; "Release: send" before it, "Release: delete" after it | 0:11-0:19 on-screen + voice |
| 0:41 → 0:50 | timer continuing after locking ("Long message · locked") | 0:20-0:30 on-screen |
| 2 seconds | silence before the warning "No sound for 2 seconds · Your mic looks muted" with an Unmute action | 0:34-0:36 on-screen |
| 1:24 | total length shown on the received voice bubble | 0:38 on-screen |
| 0:42, 0:52 | timestamped transcript lines under the bubble ("Step 3 asks for a credit card", "Users drop before they see the app") | 0:38-0:46 on-screen |
| 1x → 1.5x | playback speed toggle on the bubble | 0:43-0:46 on-screen + voice |
| Position 0:59, time left 0:16 at 1.5x | remaining time adjusts for speed (25 s of audio left ÷ 1.5 ≈ 16 s; calculation from the shown values) | 0:43 on-screen |

No animation durations, easing values or sizes are given.

## Before / after
- **Under the thumb vs past the thumb (press).** Bad: the mic button changes only under the finger (a grey button, no timer); the user wonders "Is it recording?". Good: on the same frame as the press a running timer appears in the input field and the button swells larger than the thumb with a pulsing ring: "Recording, she can see it". Why: feedback hidden under the finger is invisible; immediate, visible confirmation tells the user the mic is live before they start talking, so the first word is not lost.
- **Ambiguous release vs cancel line.** The drag-distance indicator shows "Release: send" until the thumb crosses a fixed line, then flips to "Release: delete"; the slide hint turns into a trash can. Why: the same physical action (lifting the thumb) has two outcomes, so the current outcome must be visible before release; a fixed threshold makes the boundary learnable.
- **Holding for a long message vs lock.** Bad: the user must keep the thumb on the button for a long recording ("Short message · hold the mic"). Good: sliding up onto a lock icon switches to "Long message · locked"; the gesture is replaced by a stop button and a send button and the live waveform. Why: a long hold is tiring and error-prone; explicit buttons mean nothing ends by accident.
- **Blind recording vs live waveform.** The waveform reacts to the voice ("voice detected"); when it goes flat the status turns to "silence" and after 2 seconds a banner offers Unmute. Why: a flat line is an instant signal that the mic is muted, before a whole minute is wasted.
- **Opaque bubble vs scrubbable playback.** The received bubble shows the waveform and length (1:24); the listener drags the playhead to the part they need, switches to 1.5x, and the bars fill as playback advances; position, speed and time left are visible. Why: length and a draggable timeline let the recipient skim instead of listening linearly.

## Do
- Start the timer and a visible "recording" state on the same frame as the press, outside the area covered by the thumb.
- Show the release outcome continuously while dragging; switch the hint to a delete icon past a fixed cancel threshold.
- Offer a lock gesture for long recordings and then show explicit Stop and Send buttons.
- Render a live input level/waveform during recording; detect sustained silence (2 s shown) and offer an Unmute action.
- On the message bubble show total length, a draggable waveform playhead, elapsed/remaining time and a speed toggle (1x / 1.5x).

## Don't
- Don't rely on feedback that sits under the user's finger.
- Don't make release ambiguous between send and delete.
- Don't force users to hold the button for long recordings.
- Don't record silently with no level indicator.

## Scene by scene
- 0:00 Title "Hold to record. Slide to cancel." A recording pill with timer 0:00 → 0:01, a "<" slide hint and a dashed "Cancel line"; status chips Recording / Past the line / Deleted.
- 0:02 The pill collapses into a trash icon over the message field; chip "Deleted" active.
- 0:03 "01 Press: Feedback before the first word." Two panels: "Under the thumb" (grey mic, empty message field, caption "Is it recording?") and "Past the thumb" (timer 0:00 → 0:06, enlarged glowing mic with a ring, caption "Recording, she can see it"). Checklist "Maya · voice note to Leo": Press (thumb on the mic), Timer + swell (same frame, before a sound), First word (already recording).
- 0:11 "02 Cancel: Past the line, letting go deletes." Chat with Leo Park ("Tell me, I'm driving. Voice note?"). Recording bar with timer; a "Drag distance" track below reads "Release: send".
- 0:14 Thumb drags left past the dashed line; track turns to "Release: delete"; the hint becomes a trash icon; on release the recording is removed and the message field returns.
- 0:20 "03 Lock: Lock it, and the thumb is free." A lock rail appears above the mic; the thumb slides up; mode cards "Short message · hold the mic" vs "Long message · locked · 0:41".
- 0:23 Locked: live waveform, stop button and send arrow replace the held mic; timer continues to 0:50.
- 0:31 "04 Mic check: A flat line means a muted mic." Panel "Maya · recording" with a reacting waveform, label "voice detected" (0:00-0:02).
- 0:34 The waveform flattens to dots, label "silence", status dot changes to a warning colour; banner "No sound for 2 seconds · Your mic looks muted · Unmute"; mic button shows a muted icon.
- 0:38 "05 Playback: Leo jumps to the part he needs." Voice bubble from Maya Chen with waveform, duration 1:24, speed 1x; transcript snippets at 0:42 and 0:52; info row Position / Speed / Time left.
- 0:41 The playhead is dragged into the middle (position 0:45, time left 0:38), then playback starts at 1.5x; bars fill as it plays (position 0:59, time left 0:16 → 1:22, 0:01).

## Voice-over summary
- When the mic is pressed, a timer starts and the button swells past the thumb, so the user knows it hears her before she speaks.
- Sliding left past a fixed line turns the hint into a trash can, so letting go deletes instead of sends.
- For a long message, sliding up locks recording and frees the thumb; a stop button replaces the gesture so nothing ends by accident.
- The waveform moves with the voice; when it goes flat, she knows the mic is muted before wasting a minute.
- The recipient sees the length in the waveform, drags to the part he needs and plays it faster while the bars fill.

## Notes for the skill
- State machine: `idle → recording(held) → {cancelArmed (past threshold) → cancelled on release | sent on release | locked → {stopped/review | sent}}`. Compute the cancel threshold in absolute distance (e.g. a fixed fraction of the bar width), and allow dragging back to disarm before release.
- Add a short haptic tick when recording starts, when the cancel line is crossed and when lock engages (platform haptics), since the user's eyes may not be on the button.
- Gesture-only controls fail WCAG 2.5.1 (Pointer Gestures) and 2.5.7 (Dragging Movements) unless a single-pointer alternative exists. Provide a tap-to-start/tap-to-stop mode with visible Cancel, Lock/Stop and Send buttons, and keyboard support; announce "Recording started", "Release to delete", "Locked" via a live region.
- Long press timing: do not start recording on accidental touches; many apps require a minimal hold (or tap shows a hint "Hold to record"). The video does not specify this.
- Silence detection: base it on input level over a window (2 s shown) and distinguish a muted/blocked mic (permission or hardware mute) from a quiet room; link Unmute to the actual cause.
- Playback: expose the scrubber as a `role="slider"` with `aria-valuetext` like "0:45 of 1:24", arrow-key seeking, and a labelled speed button; show remaining time adjusted for speed as in the video. Waveform animation should respect `prefers-reduced-motion` (static bars plus progress fill).
- Colour: recording and silence states in the video are paired with text labels ("voice detected", "silence") and icons (muted mic), which is the right pattern; keep a non-colour cue for every state.
