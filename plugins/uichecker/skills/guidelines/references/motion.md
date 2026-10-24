# Motion

Severity: **P0** breaks use or access, **P1** causes friction or reads as broken, **P2** polish.

---

### MOT-0 · One motion profile per product (P1)
**Applies to.** any project with transitions or animations.
**Rule.** Decide once how the product moves, store it as tokens, and never improvise per component.
- **Crisp** (dense tools, dashboards, editors, admin): hover feedback about 80 ms, every transition at most 150 ms, ease-out (ease-in on exits, MOT-2), no overshoot or bounce. A generic 300 ms transition is the tell of an untuned tool.
- **Lively** (consumer, marketing, onboarding, playful brands): entrances 200 to 300 ms, small spring overshoot on presses, modals and confirmations.
Both profiles share the timing rules below, but the profile's ceiling wins: on the crisp profile every duration in every rule (for example MOT-1, MOT-9, MOT-10, FRM-13, INT-17) is capped at 150 ms and springs are off.
**Detect.** Durations and curves written inline instead of tokens (`transition: all .37s ease`); more than about six distinct durations or four easing curves; a spring in one component and a hard cut in its sibling.
**Fix.** Create duration and easing tokens (`--dur-feedback` 80 to 100 ms, `--dur-fast`, `--dur-base` 250 ms, `--dur-exit` 150 ms, `--dur-slow`, `--dur-attention` about 600 ms, `--stagger-step` 50 ms, `--ease-out`, `--ease-in`, `--ease-in-out`, optional `--ease-spring`) and route every transition through them.

### MOT-1 · Entrance timing (P1)
**Applies to.** elements that enter the screen: modals, sheets, drawers, popovers, dropdowns, toasts, page transitions.
**Rule.** Things entering the screen (modals, sheets, panels, dropdowns, page transitions) land in 200 to 300 ms, 250 ms by default, with an ease-out curve. Under about 100 ms reads as a jump cut (the eye cannot see where it came from), over about 300 ms makes the user wait before they can act. Small surfaces such as dropdowns and popovers open in about 150 ms.
**Detect.** Entrance durations over 300 ms or under 100 ms; `linear` or `ease-in` on an entrance.
**Fix.** `--dur-base: 250ms; --ease-out: cubic-bezier(0.16, 1, 0.3, 1)` (or a similar decelerating curve).

### MOT-2 · Exits are faster than entrances (P1)
**Applies to.** anything that animates out.
**Rule.** The user already decided to dismiss, so the exit takes about 60% of the entrance, i.e. about 40% shorter: 250 ms in, 150 ms out (150 to 200 ms at most). A full-length exit holds the screen hostage. Exits use ease-in or a plain ease, never a spring.
**Detect.** The same duration on open and close; a symmetric keyframe reused in reverse.
**Fix.** Separate enter and exit durations (`--dur-exit: 150ms`).

### MOT-3 · Press feedback under 100 ms (P1; P0 when silence causes repeat submits on a primary action)
**Applies to.** every pressable or hoverable control.
**Rule.** Any press, tap, hover, toggle or copy must visibly start reacting within 100 ms of input (one frame is ideal), even if the work behind it takes longer; at 200 ms the control already feels laggy. Silence after a press reads as "it didn't work" and causes double taps. When the work runs past about 300 ms, show the loading pattern STA-2 picks. The same state change exists for keyboard focus and touch, not only hover (INT-12).
**Detect.** Buttons whose only reaction is the network result; hover or active styles missing; feedback delayed by a `setTimeout`; transitions on `:active` longer than 100 ms.
**Fix.** Immediate `:active` state (scale about 0.97 or a fill change), then the async state (see STA-2 and FRM-10).

### MOT-4 · Attention motion is the only long motion (P2)
**Applies to.** alerts, error toasts, notification indicators, validation wiggles on fields and code inputs.
**Rule.** Only things that must pull the eye (an error toast, a notification bell, a failed OTP) may run 500 to 800 ms with an overshoot or a short shake; peripheral vision catches it where a plain fade is missed. Play it once (or a fixed two or three times), never loop. Motion is never the only error signal: pair it with text, an icon and a `role="alert"` announcement, and swap it for a fade under reduced motion (MOT-13). Routine UI never bounces.
**Detect.** Bounce or shake on routine elements; long durations on non-urgent UI; `animation-iteration-count: infinite` on an alert; a shake with no error text beside it.
**Fix.** Reserve one attention preset (`--dur-attention`, about 600 ms) for alerts and errors.

### MOT-5 · Stagger lists about 50 ms apart (P2)
**Applies to.** groups of items that enter together (lists, menus, card grids, hover-revealed action rows).
**Rule.** When several items enter together (list rows, menu items, cards, revealed actions), offset them by about 50 ms (40 to 60 ms). 30 ms blurs into one block; 100 ms makes the list crawl and the last row arrives late. Cap the total so long lists do not take seconds: stagger the first 6 to 8 and show the rest with the last delay. On the way out, drop the delays so the group leaves together.
**Detect.** Lists that appear as one rigid block on a lively product; per-item delays of 100 ms or more; unbounded `index * delay`.
**Fix.** `animation-delay: calc(min(var(--i), 8) * 50ms)`.

### MOT-6 · Easing matches intent (P1)
**Applies to.** every transition and animation.
**Rule.** The eye reads the velocity profile, not the duration: the same distance in the same time feels mechanical, settled or physical depending on the curve. Linear is only for continuous motion (spinners, indeterminate progress, marquees) and for effects whose progress is driven by scroll position (MOT-12). Ease-out is the default for anything entering or settling, ease-in for leaving, ease-in-out for moving between two on-screen positions. Spring only for moments that should feel physical on a lively product (press, toggle, bottom sheet, modal, confirmation) and for gesture-driven motion, where a spring keeps the finger's velocity when interrupted. No curve wins everywhere. Overshoot stays small: a modal scale may peak around 1.03, never wobble.
On lively products a short anticipation beat (a slight squash or pull-back) before a larger or playful move gives it weight, but it never delays the visible response to a tap (MOT-3), and it goes under reduced motion.
**Detect.** `linear` on UI that starts and stops (scroll timelines excepted); springs with visible wobble; a different curve on every component.
**Fix.** Three or four easing tokens, used everywhere. Start springs at a low bounce (about 0.15 to 0.25, or stiffness 300 to 500 with damping 25 to 35); in CSS approximate one with `linear()` easing.

### MOT-7 · Linked parts move on one curve (P1)
**Applies to.** components with several moving parts (accordion, toggle, tabs, sheet with handle).
**Rule.** Parts of one change move together, on one duration and one curve: an accordion's chevron and its panel, a toggle's knob, rail colour, shadow and label, a tab indicator and its content fade. Even a few frames of lag reads as broken.
**Detect.** Different durations on the parts of one component; one part animated and the other snapping.
**Fix.** Drive all parts from the same state change and the same tokens.

### MOT-8 · Animate transform and opacity, not layout (P1)
**Applies to.** every transition and animation.
**Rule.** Animate `transform` and `opacity`. Never animate `height: auto` (it snaps); for collapsible content use `grid-template-rows: 0fr → 1fr` or a measured pixel height. Never scale a whole card or grid item on hover: a transform does not reflow neighbours but paints over the gap and the next card, gets clipped by `overflow: hidden` parents and blurs text, while changing width, height, padding, margin or border width on hover does shift the neighbours. Hover keeps the layout box identical; only transforms move it. Lift it (MOT-9) or animate the content inside a fixed footprint. Where supported, `interpolate-size: allow-keywords` can animate `height: auto`; keep the grid-rows fallback.
**Detect.** `transition: height`, `transition: all`, `width`/`top`/`left`/`margin` transitions, `transform: scale()` on a grid child's outer box.
**Fix.**
```css
.panel { display: grid; grid-template-rows: 0fr; transition: grid-template-rows var(--dur-base) var(--ease-out); }
.panel[data-open="true"] { grid-template-rows: 1fr; }
.panel > .inner { overflow: hidden; }
```

### MOT-9 · Hover anatomy for clickable cards (P2)
**Applies to.** clickable cards and tiles, including product cards with hover-revealed actions and card images.
**Rule.** Move the content, never the footprint. Lift the card about 8 px (`translateY(-8px)`) while its shadow grows in offset and blur in the same 200 ms ease-out transition; 100 ms twitches, 400 ms lags behind the cursor, and a lift without the shadow reads as a slide. Mark the hovered card with an edge in the accent or focus role (a brighter border, or a pulse or sweeping gradient that runs only while hovered); if that edge is the only hover signal it needs 3:1 against the surface. Reveal secondary actions (typically favourite, cart, share) in reserved space anchored to the bottom of the image, fully inside the card and never over the title, about 60 ms apart (MOT-5). Scale only the image, to about 1.05, inside an `overflow: hidden` frame while the card stays still. Revealed actions are visible by default on touch, stay in the tab order and appear on `:focus-within` (INT-12), and as icon-only buttons carry an accessible name and the INT-11 target size. On the crisp profile change the surface value or border instead of lifting; under reduced motion drop the lift and image scale and keep the shadow or border change.
**Detect.** Clickable cards with no hover state; hover that changes size or layout or scales the card (MOT-8); revealed actions overlapping the title, spilling past the card edge or appearing all at once; `opacity: 0` actions with no touch or focus fallback (INT-12); an `infinite` animation on a card border.
**Fix.** Gate hover effects with `@media (hover: hover) and (pointer: fine)`. Put the large shadow on a pseudo-element and transition its `opacity` rather than animating `box-shadow` every frame. Stagger actions with `transition-delay: calc(var(--i) * 60ms)` and remove the delay on hover-out.

### MOT-10 · Modal entrance and backdrop (P2)
**Applies to.** modals and dialogs.
**Rule.** A modal fades in with a slight scale (from about 0.95, or 0.9 with a small spring on lively products) while its backdrop dims and optionally blurs in on the same timing. Contents may follow the panel by a short delay. The exit is an eased fade and scale down, faster than the entrance.
**Detect.** Modals that hard-cut in, backdrops that pop while the panel animates, identical in/out timings.
**Fix.** Animate panel and backdrop from one state; `backdrop-filter: blur()` only where performance allows.

### MOT-11 · Tabs and indicators slide, never teleport (P2)
**Applies to.** tabs, segmented controls, any sliding indicator.
**Rule.** An active-tab indicator slides between tabs; content cross-fades (fade out, wait about 80 ms, fade in) with panel heights matched so the page below does not jump.
**Detect.** Indicator that jumps; content hard cut; layout shift when switching tabs.

### MOT-12 · Scroll-linked motion uses CSS timelines (P2; P0 when content stays hidden without support)
**Applies to.** scroll-linked effects: reveal-on-scroll sections and cards, reading-progress bars, shrinking or sticky headers, section indicators, parallax layers.
**Rule.** Drive scroll effects from the browser's timelines instead of scroll listeners and rect maths: `animation-timeline: view()` for each element that animates as it enters or leaves, `scroll()` for page or container progress (a reading bar, a header that shrinks, usually on a `position: sticky` element). Set `animation-range` so a reveal runs while the element enters (`entry 0% entry 100%`) and is done before it reaches mid-screen. Parallax is per-layer keyframes translating different distances on one scroll timeline. Declare `animation-timeline` after the `animation` shorthand, which resets it. Content must be fully visible without support, in print, in find-in-page and to screen readers: put the hidden starting state only inside `@supports`. Under reduced motion remove parallax and travel (MOT-13). A section indicator still needs script to set `aria-current` on the active link; a progress bar is `aria-hidden` unless it carries information.
**Detect.** `addEventListener('scroll', …)` driving styles every frame (`getBoundingClientRect`, `scrollY * speed`); scroll libraries used only for simple reveals; reveal styles that start at `opacity: 0` outside `@supports`.
**Fix.**
```css
@supports (animation-timeline: view()) {
  @keyframes reveal { from { opacity: 0; translate: 0 24px; } }
  .reveal { animation: reveal linear both; animation-timeline: view(); animation-range: entry 0% entry 100%; }
  @keyframes grow { from { scale: 0 1; } }
  .read-progress { transform-origin: left; animation: grow linear both; animation-timeline: scroll(root); }
}
```

### MOT-13 · Respect reduced motion (P0 for parallax, large travel or motion over 5 s without a control; P1 otherwise)
**Applies to.** any project with motion (always check).
**Rule.** Every non-essential animation turns off or becomes a short fade under `prefers-reduced-motion: reduce`. Parallax, auto-playing motion and large movements are removed entirely; shake and bounce become a fade, staggered cascades one quick fade, celebration bursts a static success state, animated counters the final number. Smooth scrolling counts too: put `scroll-behavior: smooth` inside `@media (prefers-reduced-motion: no-preference)`, and let scripted `scrollTo` or `scrollIntoView` with `behavior: 'smooth'` check the same preference. Essential progress indicators (spinners, indeterminate bars) are exempt from a global reset, or get a slow non-spatial pulse, so they never look frozen. Whatever the setting, anything that moves on its own for more than 5 s (looping glows, marquees, auto-rotating carousels) needs a pause or stop control (WCAG 2.2.2).
**Detect.** No `prefers-reduced-motion` handling anywhere; JS animations (Web Animations API, motion libraries) that ignore the setting; `scroll-behavior: smooth` set outside a reduced-motion query.
**Fix.**
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: 1ms !important; animation-iteration-count: 1 !important; transition-duration: 1ms !important; scroll-behavior: auto !important; }
}
```
And check `matchMedia('(prefers-reduced-motion: reduce)')` before starting JS animations.

### MOT-14 · Physical gestures carry weight (P2)
**Applies to.** drag, swipe and pull gestures.
**Rule.** Drag, swipe and pull gestures map finger distance to content distance elastically (resistance past a limit), fire only past a clear threshold, give one signal (haptic or visual tick) at the threshold while the finger is still down, and settle with a small overshoot on release.
**Detect.** Pulls that track the finger 1:1 with no resistance, actions that fire on any small movement, hard stops on release.
**See also.** INT-14 (swipe), INT-15 (pull to refresh), INT-13 (drag and drop).

### MOT-15 · Celebrate rarely and briefly (P2)
**Applies to.** success screens and completion states with celebration motion: confetti, particle bursts, check-mark pops.
**Rule.** Celebration is seasoning on an ending whose substance is already there (CON-5). Reserve it for meaningful completions (a first purchase, finishing onboarding), never routine saves, or it stops reading as a peak. Keep it under about 1 s, let it never block input, focus or the next action, and render a static success state under reduced motion.
**Detect.** Confetti libraries fired on every save or submit; celebration overlays that intercept pointer events or delay navigation; no `prefers-reduced-motion` check before firing a burst.

### MOT-16 · Shared-element transitions keep objects constant (P2)
**Applies to.** View Transitions and shared-element morphs: a card that becomes a page, list reorder and filter, a theme switch, a dialog that grows from its trigger.
**Rule.** When an element continues into the next state, morph it instead of cutting, so the user sees that the page header is the card they tapped. Give the old and the new element the same `view-transition-name` and run the DOM change inside `document.startViewTransition(() => update())`; for real page loads opt both pages in with `@view-transition { navigation: auto; }`. Feature-detect (`if (!document.startViewTransition) update()`): unsupported browsers just swap. A name identifies exactly one element per state; a duplicate aborts the whole transition, so list items take names from stable IDs, never indexes (`view-transition-name: var(--item)`). A dialog grows out of its trigger by moving the name from the button to the dialog inside the callback, back on close, while `showModal()` focus handling stays intact. A theme wipe from the toggle animates `::view-transition-new(root)` with an explicit `from` and `to` circle `clip-path` (the radius reaching the farthest corner) from the click point, or the button's centre for keyboard activation, with the default cross-fade turned off. Keep component morphs about 200 to 350 ms and full-page effects at most about 600 ms, since the page is not interactive during a transition; when aspect ratios differ, give text and image separate names or `object-fit: cover` on the snapshots so text does not stretch. Under reduced motion set `animation: none` on the `::view-transition-*` pseudo-elements.
**Detect.** `startViewTransition` with no feature check or reduced-motion handling; the same `view-transition-name` on several visible elements; names derived from array indexes; a clip-path keyframe with only a `from`; morphs longer than about 600 ms.
