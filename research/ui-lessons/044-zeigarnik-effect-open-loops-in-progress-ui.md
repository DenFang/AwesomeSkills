---
lesson: 044
kind: video
duration_s: 44
type: ui
category: feedback
topic: Zeigarnik effect: visible incomplete progress (checklists, completion meters)
sources: frames, voice-over, lesson notes
---

# Zeigarnik effect: open loops in progress UI

**Hook:** One progress bar pulls you in and the other does not, because unfinished tasks stay on your mind.

## Main rule
Show visible, specific remaining steps (an onboarding checklist with the next items unchecked, a completion meter with the next action) only for outcomes the user actually wants to reach; incomplete progress on things the user does not care about is noise, not motivation.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 100% ("Brain forgets") vs 80% ("Brain returns") | complete vs open-loop progress bars | 0:00-0:02 on-screen; voice 0:17-0:20 "100% complete? You forget. 80? It nags." |
| "up to twice as long" / "2x memory weight" | claimed retention of unfinished vs finished tasks | 0:05-0:08 voice; 0:08-0:10 on-screen "Incomplete = 2x memory weight" |
| recalled 0x vs 11x | completed "Sign up for newsletter" vs incomplete "Finish your portfolio bio" (counter animation) | 0:05-0:10 on-screen (illustrative) |
| 1 or 2 unchecked items | onboarding checklist | voice 0:10-0:14 ("one or two"); headline says "Leave 1 box unchecked" |
| 5 items, 3 checked = "Open · 60%" | onboarding checklist demo (Verify email, Add profile photo, Pick a workspace done; Invite a teammate, Connect calendar open) | 0:11-0:21 on-screen |
| 80% "Profile strength" + "Add 3 more skills" | profile completion meter | 0:22-0:29 on-screen + voice ("add three more skills") |
| notification "one step from 100%" repeated 7 days ago, 3 days ago, today, tomorrow | re-engagement nudge | 0:25-0:29 on-screen |
| 30% reading progress | marketing email ("wrong fit") | 0:30-0:39 on-screen + voice |
| 65% course progress, Module 4 of 6 | online course ("right fit") | 0:30-0:39 on-screen |

## Before / after
1. **Closed vs open bar (0:00-0:02).** A bar at 100% labelled "Complete, Brain forgets" fades; a bar at 80% labelled "Open loop, Brain returns" stays highlighted ("Unfinished wins."). Mechanism claimed: an unfinished task keeps tension in memory, so the user thinks about it and returns.
2. **Onboarding checklist (0:11-0:21).** Bad ("Closed", "User: gone, no return"): a setup checklist with all five items ticked. Good ("Open · 60%", "User: returns daily"): the same checklist with "Invite a teammate" and "Connect calendar" still open and outlined. Why: visible, concrete remaining steps give the user a reason and a path to come back.
3. **Profile meter (0:22-0:29).** A profile card shows "Profile strength 80%" with a single suggested action "Add 3 more skills, Reach 100% to unlock recommendations", plus recurring notifications "your profile is one step from 100%". "Not a suggestion. A trigger." The video attributes this to LinkedIn.
4. **Outcomes vs chores (0:30-0:39).** Wrong fit: a marketing email "Discover our new collection" with "Reading progress 30%" ("User doesn't want to finish. Just noise."). Right fit: "React Fundamentals, Module 4 of 6, Course progress 65%" ("User wants the cert. Loop pulls."). Why: progress only motivates when the end state has value to the user; otherwise it adds friction.

## Do
- Show a short onboarding checklist with real, valuable next steps and clear completion state per item.
- Pair a completion meter with one specific next action (e.g. "Add 3 more skills") and the benefit of finishing.
- Use progress indicators for goals users chose: courses, setup, profiles they want to be found by.
- Keep remaining work visible and easy to resume (deep link straight to the missing step).

## Don't
- Don't put progress bars on content or tasks the user does not care about (e.g. reading progress on a marketing email).
- Don't invent fake "incomplete" items just to keep the loop open.
- Don't nag with repeated notifications about the same missing step.

## Scene by scene
- 0:00 "Zeigarnik effect": two cards, "Complete 100%, Brain forgets" and "Open loop 80%, Brain returns"; the complete one fades, the open one enlarges; "Unfinished wins."
- 0:03 "How the brain processes tasks · Unfinished tasks hold weight." Brain icon, "Active memory"; cards "Completed: Sign up for newsletter, recalled 0x" vs "Incomplete: Finish your portfolio bio", counter climbing to 11x; "Incomplete = 2x memory weight".
- 0:11 "Onboarding · Application · Leave 1 box unchecked." Two Set up checklists: left all five ticked, "Closed", "User: gone, no return"; right three ticked and two open, "Open · 60%", "User: returns daily"; "100% complete? You forget. 80%? It nags."
- 0:22 "Big tech runs on this · Your profile is 80% done." Light profile card (avatar initials, name, title) with "Profile strength 80%" and "Add 3 more skills"; notification "one step from 100%" with timestamps 7 days ago, 3 days ago, today, tomorrow; "Not a suggestion. A trigger."
- 0:30 "One critical catch · Outcomes, not chores." Wrong fit (newsletter, reading progress 30%, "Just noise") vs right fit (React course module 4 of 6, 65%, "Loop pulls"); chip "Chore? x · Outcome user already wants ✓".
- 0:40 Outro "Don't close the loop. Leave it open." Chips Open loop -> Pull -> Return; "Save for your next onboarding", "Follow for more design psychology".

## Voice-over summary
- The brain treats unfinished tasks as open loops, claimed to stay in active memory up to twice as long as completed ones.
- Successful onboarding shows a checklist with one or two items unchecked, and the incomplete state pulls users back; at 100% you forget, at 80% it nags.
- LinkedIn's long-running "add three more skills" prompt is presented as a deliberate trigger to keep people in the app.
- The catch: it only works for tasks the user wants to finish; a 30% bar on a marketing email "isn't motivation. It's friction."
- "Use it on outcomes, not chores."

## Notes for the skill
- Evidence check: Zeigarnik's 1927 study reported better recall of interrupted tasks (roughly 2:1), but replications are inconsistent; the more robust finding is the tendency to resume interrupted tasks (Ovsiankina effect). Treat "2x memory weight" and "recalled 11x" as illustrative, not as data.
- Ethics: the video frames this as retention engineering ("keeping you in the app", repeated "one step from 100%" notifications). Withholding completion, faking unchecked items, or nagging is a manipulative pattern. The defensible rule: show honest progress toward a goal the user chose, let them reach 100% and acknowledge it (a completion state with a clear "done" message), and let them dismiss or hide the checklist. The page's "don't close every loop at 100%" should be read as "don't hide remaining real steps", not "never let users finish".
- Headline vs demo mismatch: the headline says "Leave 1 box unchecked", the demo leaves 2 of 5 unchecked (60%) while the caption says 80%. Use what is true for the user's actual remaining steps.
- Implementation: checklist as a list with real checkboxes or status icons with text ("3 of 5 complete"); progress bars need `role="progressbar"` (or native `<progress>`) with `aria-valuenow`, `aria-valuemin`, `aria-valuemax` and a label. Do not convey done/undone by colour only; use a tick and strikethrough or a "Done" text.
- Persist checklist state server-side so it survives devices; auto-complete items when the user does the task elsewhere in the app, so the list never asks for something already done.
- Keep re-engagement notifications opt-in and rate-limited.
