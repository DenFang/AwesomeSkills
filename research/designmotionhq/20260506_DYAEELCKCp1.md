---
id: DYAEELCKCp1
reel_url: https://www.instagram.com/reel/DYAEELCKCp1/
pattern_page: https://designmotionhq.com/patterns/animation-timing
date: 2026-05-06
duration_s: 56
type: ui
category: motion
topic: animation duration budgets by purpose (entrance, exit, feedback, attention, stagger)
sources: frames, voice-over, pattern page
---

# Animation timing: five duration budgets

**Caption:** not captured yet
**Hook:** The same confirm-dialog animation played at two durations (500 ms vs 250 ms) feels completely different; the viewer perceives the difference without being told.

## Main rule
Pick the duration from the animation's job, not from taste: entrances 200-300 ms (default 250 ms), exits shorter than entrances (about 150 ms after a 250 ms entrance), direct-manipulation feedback under 100 ms, attention-seeking motion 500-800 ms with overshoot/bounce, and list items staggered 50 ms apart.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 500 ms vs 250 ms | opening comparison: same confirm dialog, slow vs right timing | 0:02 on-screen labels |
| 50 ms (too fast) / 250 ms (perfect) / 700 ms (too slow) | modal entrance demo | 0:03-0:11 on-screen |
| 200-300 ms | entrances: page transitions, modals, panels | 0:03 voice, 0:12 on-screen |
| in 250 ms / out 150 ms (correct) vs in 250 ms / out 250 ms (wrong) | dialog enter/exit pair | 0:14-0:20 on-screen |
| 150-200 ms | exit duration range | 0:16 voice |
| "Exits are 30% faster" | ratio claimed on screen for 250 -> 150 | 0:21-0:23 on-screen. Page says "roughly 40% faster". Arithmetic: 150/250 = 0.6, i.e. the exit is 40% shorter; the on-screen 30% is inaccurate |
| 200 ms (laggy) / 100 ms (OK) / 50 ms (instant) | button press response demo | 0:24-0:30 on-screen |
| < 100 ms | feedback: press, hover, toggle | 0:24 voice, 0:31 on-screen |
| 500-800 ms + bounce | attention: errors, alerts/notifications, wiggle/shake | 0:34 voice, 0:35 and 0:41 on-screen |
| 30 ms (too fast) / 50 ms (perfect) / 100 ms (too slow) | per-item stagger in a 6-row settings list | 0:45-0:50 on-screen |
| 50 ms | stagger between list/menu items | 0:45 voice, 0:51 on-screen |
| Cheat sheet: Entrance 250 ms, Exit 150 ms, Feedback <100 ms, Attention 500-800 ms + bounce, Stagger 50 ms | summary | 0:53-0:55 on-screen |
| ease-out (cubic) for entrances; springs/bounce only for attention | easing pairing | pattern page only, no curve values shown in the video |

## Before / after
- **Entrance too fast vs right vs too slow (50 / 250 / 700 ms).** 50 ms reads as a jump cut: the eye cannot track where the modal came from, so it feels glitchy. 700 ms makes the user wait for the UI before they can act, so it feels heavy. 250 ms is long enough to read as intentional motion and short enough not to block input.
- **Symmetric exit (250 in / 250 out) vs shorter exit (250 in / 150 out).** When the user dismisses something, the decision is already made; a full-length exit animation holds the screen hostage and feels like drag. A shorter exit removes the element quickly while still giving a trace of where it went.
- **Feedback 200 vs 100 vs 50 ms.** Response to a press at 200 ms is perceptibly delayed, so the button feels broken or laggy even if the action itself is instant. At or below 100 ms the response is perceived as caused directly by the click.
- **Attention: smooth fade vs bounce + shake.** An error toast that only fades in is easy to miss ("boring"). The same toast with overshoot and a short shake over 500-800 ms is caught by peripheral vision. The longer duration is acceptable here because the goal is to be noticed, not to get out of the way.
- **Stagger 30 vs 50 vs 100 ms.** At 30 ms the six rows appear almost at once and blur into one block, so the stagger adds nothing. At 100 ms the list visibly crawls in and the last row arrives late. At 50 ms the eye is led top to bottom without waiting.

## Do
- Use 200-300 ms (250 ms default) for modals, panels, drawers and page transitions entering.
- Make the exit shorter than the entrance, e.g. 250 ms in / 150 ms out (exit roughly 60% of the entrance duration).
- Keep press, hover and toggle feedback under 100 ms.
- Reserve 500-800 ms with overshoot/bounce for things that must be noticed: errors, alerts, a validation wiggle.
- Stagger list and menu items about 50 ms apart.
- Use ease-out (decelerating) curves for entrances (page).

## Don't
- Don't run entrances past about 300 ms or below about 100 ms.
- Don't use the same duration for enter and exit.
- Don't animate feedback states (hover, active, toggle) at 200 ms or more.
- Don't use bounce or long durations for routine transitions; it turns every state change into an attention grab.
- Don't stagger at 100 ms or more per item, and don't use 30 ms or less (no visible sequence).
- Don't use linear easing for entrances (page).

## Scene by scene
- 0:00 Two phone mockups side by side, each showing a "Confirm / Delete this item permanently?" dialog with Cancel and an accent Confirm button, animating in.
- 0:02 Labels appear above the phones: 500 ms (left) and 250 ms (right). Caption: same animation, your brain knows.
- 0:03 "Secret 01 Entrance, 200-300ms is the sweet spot". Three columns: Too fast 50 ms, Perfect 250 ms, Too slow 700 ms; a small "Modal / Hello world." card loops its entrance in each column, the 700 ms one still mid-fade when the others are done.
- 0:12 Big number "200-300 ms" with subtitle "Page transitions. Modals. Panels."
- 0:14 "Secret 02 Exit, Faster than entrance". Two rows: "Correct: in 250ms / out 150ms" (success-coloured Confirm) and "Wrong: in 250ms / out 250ms" (danger-coloured Confirm), a "Saved! Your changes have been saved." dialog enters and leaves in each; footer: same speed = sluggish exit.
- 0:20 "250 -> 150, IN / OUT", text "Exits are 30% faster", subtitle "The user already decided."
- 0:24 "Secret 03 Feedback, The Doherty threshold". Three "Click me" buttons labelled Laggy 200 ms, OK 100 ms, Instant 50 ms; a cursor clicks each and the press response lags accordingly.
- 0:31 Big "<100 ms", "Press. Hover. Toggle.", subtitle "The Doherty threshold, feels instant."
- 0:34 "Secret 04 Attention, 500-800ms with bounce". Two error toasts ("Error / Something needs your attention."): top labelled "Smooth fade, boring" (muted, plain fade), bottom labelled "Bouncy + shake, eye-catching" (accent border, glow, bounces and shakes).
- 0:41 Bell icon, "500-800ms + bounce", "Errors. Alerts. Slow enough to notice."
- 0:45 "Secret 05 Stagger, 50ms between items". Three columns of a settings list (Account, Notifications, Privacy, Display, Storage, About) revealing row by row at 30 ms, 50 ms and 100 ms.
- 0:51 Big "50 ms", "Lists. Menus. The sweet spot."
- 0:53 "Cheat sheet" rows build in: Entrance 250 ms, Exit 150 ms, Feedback <100 ms, Attention 500-800 ms + bounce, Stagger 50 ms.
- 0:55 Cheat sheet dims; "Save these numbers." and a follow prompt.

## Voice-over summary
- Opening: the same animation at two timings is perceived differently.
- Entrances belong in 200-300 ms; faster looks broken, slower looks heavy. Applies to page transitions, modals, panels.
- Exits should be quicker, 150-200 ms, because the user has already decided; do not make them wait.
- Feedback (button press, hover, toggle) must stay under 100 ms or it reads as lag.
- Attention animations (errors, notifications, wiggle) take 500-800 ms with bounce: "Slow enough to notice. Fast enough to not annoy."
- Lists stagger 50 ms per item, not 30 and not 100.

## Notes for the skill
- Suggested tokens: `--dur-feedback: 80-100ms`, `--dur-exit: 150ms`, `--dur-enter: 250ms`, `--dur-attention: 600ms`, `--stagger-step: 50ms`. Entrance easing: an ease-out curve (the page names "cubic ease-out"; no cubic-bezier values are given in the video or page). Exit easing: ease-in or ease-in-out is the common pairing (not stated in the video).
- Stagger: implement with `transition-delay: calc(var(--i) * 50ms)` or `animation-delay`. Not covered by the video: cap the number of staggered items (e.g. the first 6-8 visible rows) so long lists do not take seconds to finish; items beyond the cap appear with the last delay.
- Exit ratio: the on-screen "Exits are 30% faster" is arithmetically wrong for 250 -> 150 ms (40% shorter duration). The page's "roughly 40%" matches the numbers. Use "exit about 60% of the entrance duration".
- "Doherty threshold" label is misapplied. The Doherty threshold (Doherty & Thadani, 1982) is about 400 ms system response time for keeping users productive. The "under 100 ms feels instantaneous" figure comes from the classic response-time limits (Miller 1968 / Nielsen: 0.1 s). The rule (<100 ms for feedback) is fine; the attribution is not.
- Feedback under 100 ms means the visual response must start within 100 ms of input. A press state can use a near-instant change (0-100 ms) even when the resulting action takes longer; if the action exceeds about 1 s, add a progress/loading state.
- Reduced motion: respect `prefers-reduced-motion: reduce`. Replace bounce/shake and slide entrances with an opacity fade or an instant change; WCAG 2.3.3 (AAA) covers motion triggered by interaction. Shake/bounce for errors must never be the only error signal: pair it with text, an icon and an `aria-live`/`role="alert"` announcement.
- Attention motion should play once (or a small fixed number of times), not loop; anything auto-moving for more than 5 seconds needs a pause/stop control (WCAG 2.2.2).
- Hover feedback is pointer-only; make sure the same state change exists for keyboard focus (`:focus-visible`) and touch (`:active`).
