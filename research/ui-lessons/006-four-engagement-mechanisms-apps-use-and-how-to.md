---
lesson: 006
kind: video
duration_s: 91
type: ui
category: ethics / persuasion
topic: four engagement psychology mechanisms (variable rewards, Zeigarnik effect, loss aversion, social reciprocity)
sources: frames, voice-over
---

# Four engagement mechanisms apps use (and how to use them responsibly)

**Hook:** The average person spends about 7 hours a day on their phone, and the video claims that is engineered, not a personal failing.

## Main rule
Know the four retention mechanisms behind habit-forming products (unpredictable rewards, visible unfinished progress, fear of losing accumulated value, reciprocal social notifications) and use them only where they serve the user's own goal. Progress indicators and streaks are fine as honest feedback; artificial urgency, loss threats and notification loops designed to pull users back are manipulative (dark patterns) and should not ship.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 7h 23m daily average, "↑ 23% from last week" | demo Screen Time card (counts up 0h 00m → 6h 05m → 7h 23m) | 0:00-0:06 on-screen |
| 5.2h, 6.1h, 5.8h, 6.7h, 7h, 7.8h, 7.4h | Mon-Sun bars of the demo chart | 0:02-0:06 on-screen |
| Instagram 2h 47m, TikTok 2h 12m, Netflix 1h 34m | "Most Used" list | 0:02-0:06 on-screen |
| 7 hours a day | claimed average phone time | 0:00 voice + 0:02 on-screen |
| 2/5 watched, "3 remaining..." | Stories row (unfinished set) | 0:26-0:41 on-screen |
| 4/5 complete, "1 lesson left!", progress bar about 80% full | Duolingo-style lesson card | 0:31-0:41 on-screen |
| 2 → 67 → 131 → 147 | streak counter counting up | 0:42-0:45 on-screen |
| 147-day streak, "Expires in 2h, Send a snap now!" | urgency warning under the streak | 0:45-0:49 on-screen + voice ("147-day streak") |
| 59 → 0, "Streak lost forever." | streak collapse | 0:50-0:52 on-screen |
| 2x | losses feel about twice as strong as equal gains | 0:53 on-screen + voice |
| +1 streak day "Emotion: low" vs −147 day streak "Emotion: 2× HIGHER" | gain vs loss comparison cards | 0:54-0:59 on-screen |
| 3 new likes while you were gone | step 4 of the reciprocity sequence | 1:04 on-screen |
| 20 minutes | browsing time after "returning a favour" (voice claim) | 1:09 voice |
| 0/4 → 4/4 "manipulation score" | closing self-quiz | 1:21-1:27 on-screen |

## Before / after
The video is an explainer, not a fix; each section contrasts a neutral design with the engagement-optimised one.
- **Predictable vs variable feed (0:08-0:24).** Left column "Predictable": identical muted rows, a flat "DOPAMINE" meter, footer "User leaves...". Right column "Variable": most rows plain, some highlighted reward rows (star and heart) at irregular positions, the dopamine meter spikes irregularly. Mechanism: intermittent, unpredictable reinforcement (variable-ratio schedule) keeps people searching for the next reward, the same schedule as a slot machine.
- **Unfinished progress (0:25-0:41).** A stories row shows "2/5 watched, 3 remaining..." and a lesson card "4/5 complete, 1 lesson left!" with an almost-full bar. Mechanism: the Zeigarnik effect, people remember and are drawn back to incomplete tasks; showing the gap makes closing it feel necessary.
- **Streak and loss (0:42-0:59).** A streak climbs to 147 days, then an urgency banner "Expires in 2h" appears; the counter then breaks to 0 with cracks and "Streak lost forever." Side cards compare +1 day (low emotion) with losing 147 days (2× higher emotion). Mechanism: loss aversion; accumulated value turns daily use into protecting an asset rather than wanting the activity.
- **Reciprocity loop (1:00-1:16).** Numbered steps: (1) "Sarah liked your photo", (2) "You open the app ...to check", (3) "You like Sarah's photo back, Social obligation", (4) "3 new likes while you were gone, Now you're browsing...". A circular diagram (bell → phone → heart → bell, infinity sign) is captioned "Gets faster each cycle". Mechanism: social obligation to return a favour, triggered by a notification, converts one tap into a browsing session.

## Do
- Use progress indicators ("4/5 complete") when they reflect a goal the user chose, and let the user finish or dismiss the set.
- If you use streaks, add forgiveness: streak freezes, grace periods, or "longest streak" records that survive a missed day.
- Batch and rate-limit social notifications; give users per-type notification controls and quiet hours.
- Offer natural stopping points in feeds ("You're all caught up") instead of infinite variable-reward scrolling.
- Show usage data honestly when you show it (screen time, session length), as the demo card does.

## Don't
- Don't create countdown urgency around a streak or reward ("Expires in 2h, act now!") to force a session.
- Don't frame a lapse as permanent destruction ("lost forever") to exploit loss aversion.
- Don't send notifications whose purpose is to trigger reciprocal actions and pull the user back into a feed.
- Don't randomise reward placement in a feed purely to extend time-on-app.
- Don't show "incomplete" counters for sets the user never started or chose (unwatched stories as a debt).

## Scene by scene
- 0:00 Phone card "Screen Time" counts up from 0h 00m to 7h 23m daily average with a "↑ 23% from last week" chip, a Mon-Sun bar chart and a "Most Used" list. Text: "7 hours a day. / Not your fault. / Here's how." (last line in the danger/accent colour).
- 0:07 "SECRET #1 Variable Rewards". Two feed mockups: "Predictable" (all muted rows, flat meter, "User leaves...") vs "Variable" (irregular highlighted reward rows, spiking "DOPAMINE" bar chart). Feeds scroll continuously.
- 0:20 Caption "Same as a slot machine." then "You keep scrolling, hoping for a winner."
- 0:25 "SECRET #2 Zeigarnik Effect". Stories card: 2 rings marked "New!", 3 marked "Seen", "2/5 watched, 3 remaining...". 0:31 a Duolingo card appears: four check circles, a "5", "4/5 complete", "1 lesson left!", success-colour progress bar near full.
- 0:34 "Your brain can't forget unfinished tasks." then "That's why you always come back."
- 0:42 "SECRET #3 Loss Aversion". Snapchat streak card counts 2 → 67 → 131 → 147 "day streak". 0:45 warning chip "Expires in 2h, Send a snap now!".
- 0:50 Counter drops to 59, then the card flashes, cracks, and shows a skull with "0" and "Streak lost forever."
- 0:53 "Losing feels 2x worse than winning feels good." Two cards appear: "+1 streak day / 'cool I guess' / Emotion: low" (success colour, short bar) vs "−147 day streak / 'NO NO NO!' / Emotion: 2× HIGHER" (danger colour, full bar). 0:55 "Apps weaponize this against you."
- 1:00 "SECRET #4 Social Reciprocity". Numbered notification steps 1-4 appear one by one, then "THE RECIPROCITY LOOP" circle diagram with an arrow travelling around it, "Gets faster each cycle".
- 1:09 "They notify you just enough to bring you back." then "Then the loop starts again."
- 1:17 "How manipulated are you?" checklist: Variable Rewards (Instagram, TikTok), Zeigarnik Effect (Netflix, Duolingo), Loss Aversion (Snapchat, Duolingo), Social Reciprocity (Instagram, LinkedIn); boxes tick, score "0/4" jumps to "4/4 manipulation score", card "What's your score? Comment below".
- 1:28 Outro "Share your score. Follow for more." with a Follow button.

## Voice-over summary
- Opens with the 7-hours-a-day figure and says apps are built to exploit the brain.
- Variable rewards: a uniform feed bores people, an unpredictable mix of great and dull posts works like a slot machine.
- Zeigarnik effect: unfinished stories, lessons and progress bars nag until the user returns, which is why progress indicators are everywhere.
- Loss aversion: losing feels about twice as bad as gaining feels good; a 147-day streak is defended out of fear, not desire.
- Social reciprocity: a like creates an obligation to return it, the return visit becomes a 20-minute browse; "every notification is a hook".
- Closes with a self-score quiz and a call to share it.

## Notes for the skill
- Treat this video as a catalogue of persuasive mechanisms with an ethics boundary, not as a recipe. Relevant references: deceptive design / dark-pattern taxonomies (e.g. "nagging", "false urgency", "confirmshaming"), and regulators' guidance (EU DSA Art. 25 bans interface designs that materially distort users' free decisions; the FTC treats manipulative urgency as deceptive). Flag any streak countdown, guilt copy or loss framing in a design review.
- Healthy versions: progress bars tied to user-set goals; streaks with repair/freeze; "caught up" end-of-feed states; notification digests; easy, discoverable opt-out of engagement notifications.
- Accessibility and wellbeing: time-pressure banners ("Expires in 2h") conflict with WCAG 2.2.1 Timing Adjustable in spirit when the timer gates user content; never auto-expire user-earned state without warning and a way to extend.
- The "2x" figure is a simplification of Kahneman and Tversky's loss-aversion coefficient (empirically about 1.5 to 2.5); fine as a rule of thumb, not a constant. The 7-hours-a-day average is a widely quoted but contested statistic (it usually counts all screens, not only phones).
- The stories demo labels the two unwatched rings "New!" and the three watched ones "Seen" yet reads "2/5 watched"; the label logic is inverted on screen, the counter is what matters.
