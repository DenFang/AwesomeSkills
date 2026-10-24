---
lesson: 061
kind: video
duration_s: 52
type: ui
category: feedback
topic: file upload as a system of states (drag feedback, honest progress, inline retry, preview, per-file queue)
sources: frames, voice-over, lesson notes
---

# File upload UX: five feedback signals

**Hook:** The same file upload can feel broken or safe; the difference is entirely in the feedback around it.

## Main rule
Treat upload as a set of states, not a bare file input: react to drag-over before the drop, show determinate progress with percent and time left, keep the file and offer inline resume on failure, confirm with a preview (thumbnail, type, size), and give every file in a batch its own progress and retry.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 3 signals | drag-over feedback: border, glow, copy change ("Release to upload") | 0:08-0:12 on-screen chips + voice |
| PNG, JPG, PDF, up to 50 MB | accepted types and size limit written inside the idle drop zone | 0:03-0:07 on-screen |
| 1.2 MB / 2.4 MB / 48 MB / 340 KB / 860 KB | example file sizes (brief.pdf, hero-banner.png, demo-recording.mp4, invoice-2026.pdf, avatar-photo.jpg) | throughout on-screen |
| 92% | intro "safe" progress bar | 0:01 on-screen |
| 5% -> 18% -> 31% -> 44% -> 57% -> 70% -> 83% -> 96% -> 100% | honest progress counter during the spinner comparison | 0:14-0:22 on-screen |
| 11s, 8s, 6s, 3s, 1s, 0s left | time remaining shown under the percent | 0:17-0:22 on-screen |
| 2.5, 1.9, 2.4, 2.0, 2.3 MB/s | live transfer speed under time left | 0:18-0:22 on-screen |
| 90% | failure point ("Paused at 90%, file kept in memory", "Upload failed / Connection lost") | 0:22-0:28 on-screen + voice |
| 92% -> 100% "Resuming from 90%..." | resume after one tap on Retry, no restart | 0:28-0:30 on-screen |
| 4032 x 3024, JPG, 2.4 MB | preview card metadata (dimensions, type badge, size) | 0:32-0:38 on-screen |
| 5 files | queue length on screen ("Uploading 5 files", counter "0 of 5 done" ... "5 of 5 done") | 0:39-0:46 on-screen |
| 10 files / "the other nine" | queue size in the voice-over (differs from the 5 shown on screen) | 0:39-0:46 voice |
| "2 of 5 - 1 failed", "3 of 5 - 1 failed" | queue header counting failures separately | 0:41-0:43 on-screen |

## Before / after
1. **Intro: spinner vs progress (0:00-0:02).** Top card ("BROKEN"): a generic spinner with "Uploading...". Bottom card ("SAFE"): drop zone glows on drag, a named progress bar at 92%, then "brief.pdf uploaded" with a check and solid success border. Why: the user can see their specific file moving and finishing.
2. **Drag feedback (0:02-0:12).** Bad: a file is dragged over a dashed drop zone and nothing changes ("Nothing reacts", "Users hesitate when nothing moves"). Good: as the file enters, the border turns to the accent colour, a soft glow appears inside the zone, the icon changes to an up arrow and the copy changes from "Drop your file" to "Release to upload" plus the file name and size. Why: the drop target confirms it will accept the file before the user commits, removing the hesitation of dropping into an unknown target.
3. **Mystery spinner vs honest progress (0:13-0:22).** Bad ("MYSTERY"): a spinner with a question mark and "Uploading...". Good ("HONEST"): file name and size, big percent counter, determinate bar, then "time left" and MB/s rows. Why: percent and time left let the user decide whether to wait or leave; an indeterminate spinner makes every wait feel open-ended and hides stalls.
4. **Failure at 90% (0:22-0:30).** The bar turns to the danger colour at 90% with "Paused at 90%, file kept in memory" and an inline "Upload failed / Connection lost" row with a Retry button. One click shows "Resuming from 90%..." and the bar continues to 100% and "Upload complete". Why: the work already done is preserved; re-selecting the file and restarting is the most punishing possible recovery.
5. **Filename vs preview (0:31-0:38).** Bad ("TEXT ONLY"): a single line "IMG_4032.jpg uploaded". Good ("PREVIEW"): thumbnail with dimensions overlay, file name, JPG type badge, 2.4 MB, "Uploaded just now", plus Replace and Remove actions. Labels build up: Thumbnail, Type, Size, Proof. Why: users recognise images and file types faster than cryptic file names, so they can confirm it was the right file and fix it in place.
6. **Batch queue (0:39-0:46).** Five rows, each with its own bar and percent; one (the 48 MB video) fails with its own Retry while the others keep going and complete with checks; header shows "x of 5 - 1 failed". After retry it resumes from 45% and finishes; "5 of 5 done". Why: isolating failures keeps successful work moving and makes the failed item obvious and recoverable.

## Do
- On `dragenter`/`dragover` change three things at once: border, background glow/tint, and the copy (e.g. "Release to upload" + file name and size).
- Show accepted types and size limit inside the idle drop zone.
- Use a determinate progress bar with percent; add time remaining (and optionally speed) for large files.
- On failure keep the file in memory/state, mark the point it stopped, and offer an inline Retry next to the error that resumes rather than restarts.
- After upload show a preview: thumbnail (images) or type icon, file type, size, and Replace / Remove actions.
- In multi-file uploads give each file its own progress, status and retry; summarise in a header ("3 of 5, 1 failed").

## Don't
- Don't leave the drop zone static while a file hovers over it.
- Don't use an indeterminate spinner for an upload whose progress you can measure.
- Don't discard the file and force re-selection after a network error.
- Don't treat "filename uploaded" text as sufficient confirmation.
- Don't let one failed file block or cancel the rest of the batch.

## Scene by scene
- 0:00 Split screen: "BROKEN" spinner card vs "SAFE" drop zone that glows, shows brief.pdf at 92%, then a success check "brief.pdf uploaded".
- 0:03 "Signal 01, Drag feedback / Nothing reacts.": hero-banner.png (2.4 MB) dragged over a static zone ("Drop your file", "PNG, JPG, PDF, up to 50 MB"); caption "Users hesitate when nothing moves."
- 0:07 "It has to answer back.": same drag, zone border lights up, inner glow, arrow icon, copy "Release to upload / hero-banner.png, 2.4 MB"; chips 1 Border, 2 Glow, 3 Copy appear one by one; caption "Three signals, before the drop."
- 0:14 "Signal 02, Honest progress / A spinner hides the truth.": MYSTERY spinner card vs HONEST card for demo-recording.mp4 (48 MB) counting 5% ... 100%, with time left and MB/s; chips percent, time left, wait or walk away; caption "Let them decide, wait, or walk away."
- 0:23 "Signal 03, Inline retry / It dies at ninety percent.": bar goes 80%, 89%, then 90% in danger colour, "Paused at 90%, file kept in memory", "Upload failed / Connection lost" with Retry; chips connection lost, file kept loaded.
- 0:28 Cursor clicks Retry; "Resuming from 90%...", 92%, 100%, "Upload complete"; chip one tap resumes; caption "Never make them start over."
- 0:31 "Signal 04, Upload preview / A filename is not feedback.": TEXT ONLY line "IMG_4032.jpg uploaded" vs PREVIEW card with thumbnail (4032 x 3024), JPG badge, 2.4 MB, "Uploaded just now", Replace / Remove; labels Thumbnail, Type, Size, Proof.
- 0:39 "Signal 05, Independent queue / Every file, its own lane.": "Uploading 5 files" with per-row bars; the video row fails with Retry, header "2 of 5, 1 failed"; others finish; caption "One failure never blocks the others."
- 0:44 Retry clicked on the failed row; it resumes (45%, 81%) and completes; "5 of 5 done".
- 0:47 End card: stacked uploaded file chips with checks, follow / save call to action.

## Voice-over summary
- Same file, one flow feels broken and one feels safe; the difference is feedback.
- A drop zone must answer back during drag: border, glow and copy shift give three signals before the drop.
- A spinner hides the truth; show percent and time left so users can choose to wait or walk away.
- If an upload dies at 90%, never make users start over: inline retry keeps the file and one tap resumes.
- A file name is not feedback; a thumbnail, type and size prove the right file arrived.
- In a batch, each file gets its own progress and retry, so one failure never blocks the others (voice says ten files; screen shows five).

## Notes for the skill
- The drop zone must also be a real control: a `<button>` or `<label>` bound to `<input type="file">` so keyboard and screen-reader users can upload without drag and drop; drag is an enhancement only.
- Drag state: toggle a `data-dragover`/`is-dragover` attribute on `dragenter`/`dragover` and clear it on `dragleave`/`drop` (track enter/leave counter to avoid flicker from child elements). Validate type/size on drop and show a reject state (danger border + reason) for files outside "PNG, JPG, PDF, up to 50 MB".
- Progress: use `<progress>` or `role="progressbar"` with `aria-valuenow/min/max` and an accessible name per file; announce completion and failure via an `aria-live="polite"` region (avoid announcing every percent). Smooth or throttle time-left estimates; raw estimates jump.
- Resume-from-90% requires backend support (chunked/resumable uploads such as tus or multipart with offsets). Without it, "Retry" must at least keep the file selected and restart automatically; do not promise "resume" in copy if the server restarts from 0.
- Error copy should name the cause and the action ("Connection lost. Retry"); the failed row should keep the danger colour plus an icon and text, not colour alone.
- Preview: generate thumbnails client-side with `URL.createObjectURL` and revoke them on remove; give the thumbnail meaningful alt text (file name) and keep Replace / Remove reachable by keyboard.
- Reduced motion: the glow and progress animations can stay as instant state changes; the information (percent, time) matters, not the animation.
