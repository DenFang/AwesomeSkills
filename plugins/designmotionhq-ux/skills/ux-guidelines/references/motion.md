# Motion

Motion is judged in milliseconds and curves. The same element with the same distance feels premium or broken depending on duration, easing and order. Pick one motion profile per product (see MOT-0) and apply it everywhere.

Severity: **P0** breaks use or access, **P1** causes friction or reads as broken, **P2** polish.

---

### MOT-0 · One motion profile per product (P1)
**Applies to.** any project with transitions or animations.
**Rule.** Decide once how the product moves, store it as tokens, and never improvise per component.
- **Crisp** (dense tools, dashboards, editors, admin): hover feedback about 80 ms, every transition under 150 ms, ease-out only, no overshoot or bounce.
- **Lively** (consumer, marketing, onboarding, playful brands): entrances 200 to 300 ms, small spring overshoot on presses, modals and confirmations.
Both profiles share the timing rules below, but the profile's ceiling wins: on the crisp profile every duration in MOT-1, MOT-9, MOT-10 and FRM-13 is capped at 150 ms and springs are off.
**Detect.** Durations and curves written inline instead of tokens (`transition: all .37s ease`); more than about six distinct durations or four easing curves; a spring in one component and a hard cut in its sibling.
**Fix.** Create duration and easing tokens (`--dur-fast`, `--dur-base`, `--dur-exit`, `--dur-slow`, `--dur-attention`, `--ease-out`, `--ease-in`, `--ease-in-out`, optional `--ease-spring`) and route every transition through them.

### MOT-1 · Entrance timing (P1)
**Applies to.** elements that enter the screen: modals, sheets, drawers, popovers, dropdowns, toasts, page transitions.
**Rule.** Things entering the screen (modals, sheets, panels, dropdowns, page transitions) land in 200 to 300 ms with an ease-out curve. Under about 100 ms reads as a glitch, over about 300 ms reads as in the way. Small surfaces such as dropdowns and popovers open in about 150 ms.
**Detect.** Entrance durations over 300 ms or under 100 ms; `linear` or `ease-in` on an entrance.
**Fix.** `--dur-base: 250ms; --ease-out: cubic-bezier(0.16, 1, 0.3, 1)` (or a similar decelerating curve).

### MOT-2 · Exits are faster than entrances (P1)
**Applies to.** anything that animates out.
**Rule.** The user already decided to dismiss, so the exit is about 40% shorter than the entrance: 250 ms in, 150 ms out. Exits use ease-in or a plain ease, never a spring.
**Detect.** The same duration on open and close; a symmetric keyframe reused in reverse.
**Fix.** Separate enter and exit durations (`--dur-exit: 150ms`).

### MOT-3 · Press feedback under 100 ms (P1; P0 when silence causes repeat submits on a primary action)
**Applies to.** every pressable or hoverable control.
**Rule.** Any press, tap, hover, toggle or copy must visibly react within 100 ms (one frame is ideal), even if the work behind it takes longer. Silence after a press reads as "it didn't work" and causes double taps.
**Detect.** Buttons whose only reaction is the network result; hover or active styles missing; feedback delayed by a `setTimeout`; transitions on `:active` longer than 100 ms.
**Fix.** Immediate `:active` state (scale about 0.97 or a fill change), then the async state (see STA-2 and FRM-10).

### MOT-4 · Attention motion is the only long motion (P2)
**Applies to.** alerts, error toasts, notification indicators.
**Rule.** Only things that must pull the eye (an error toast, a notification bell, a failed OTP) may run 500 to 800 ms with a bounce or shake. Routine UI never does.
**Detect.** Bounce or shake on routine elements; long durations on non-urgent UI.
**Fix.** Reserve an `--anim-attention` preset for alerts and errors.

### MOT-5 · Stagger lists about 50 ms apart (P2)
**Applies to.** groups of items that enter together (lists, menus, card grids).
**Rule.** When several items enter together (list rows, menu items, cards, revealed actions), offset them by about 50 ms (40 to 60 ms). 30 ms blurs into one block; 100 ms makes the list crawl. Cap the total so long lists do not take seconds: stagger the first 6 to 8 and show the rest at once.
**Detect.** Lists that appear as one rigid block on a lively product; per-item delays of 100 ms or more; unbounded `index * delay`.
**Fix.** `animation-delay: calc(min(var(--i), 8) * 50ms)`.

### MOT-6 · Easing matches intent (P1)
**Applies to.** every transition and animation.
**Rule.** Linear is only for continuous motion (spinners, progress, marquees). Ease-out for entering, ease-in for leaving, ease-in-out for moving between two on-screen positions, spring only for moments that should feel physical (press, toggle, modal on a lively product). Overshoot stays small: a modal scale may peak around 1.03, never wobble.
**Detect.** `linear` on UI that starts and stops; springs with visible wobble; a different curve on every component.
**Fix.** Three or four easing tokens, used everywhere.

### MOT-7 · Linked parts move on one curve (P1)
**Applies to.** components with several moving parts (accordion, toggle, tabs, sheet with handle).
**Rule.** Parts of one change move together, on one duration and one curve: an accordion's chevron and its panel, a toggle's knob, rail colour, shadow and label, a tab indicator and its content fade. Even a few frames of lag reads as broken.
**Detect.** Different durations on the parts of one component; one part animated and the other snapping.
**Fix.** Drive all parts from the same state change and the same tokens.

### MOT-8 · Animate transform and opacity, not layout (P1)
**Applies to.** every transition and animation.
**Rule.** Animate `transform` and `opacity`. Never animate `height: auto` (it snaps); for collapsible content use `grid-template-rows: 0fr → 1fr` or a measured pixel height. Never scale a whole card or grid item on hover: it overlaps its neighbours, gets clipped by `overflow: hidden` parents and blurs text. Lift it (MOT-9) or animate the content inside a fixed footprint. Where supported, `interpolate-size: allow-keywords` can animate `height: auto`; keep the grid-rows fallback.
**Detect.** `transition: height`, `transition: all`, `width`/`top`/`left`/`margin` transitions, `transform: scale()` on a grid child's outer box.
**Fix.**
```css
.panel { display: grid; grid-template-rows: 0fr; transition: grid-template-rows var(--dur-base) var(--ease-out); }
.panel[data-open="true"] { grid-template-rows: 1fr; }
.panel > .inner { overflow: hidden; }
```

### MOT-9 · Hover anatomy for clickable cards (P2)
**Applies to.** clickable cards and tiles.
**Rule.** A clickable card answers the cursor without changing its footprint: lift about 4 to 8 px with a deeper shadow over about 200 ms ease-out, optionally scale the image to about 1.05 inside an `overflow: hidden` frame, and reveal secondary actions staggered from the bottom. On the crisp profile, change the surface value or border instead of lifting.
**Detect.** Clickable cards with no hover state; hover that changes size or layout; hover-only actions with no touch fallback (see INT-12).
**Fix.** Gate hover effects with `@media (hover: hover)`.

### MOT-10 · Modal entrance and backdrop (P2)
**Applies to.** modals and dialogs.
**Rule.** A modal fades in with a slight scale (from about 0.95, or 0.9 with a small spring on lively products) while its backdrop dims and optionally blurs in on the same timing. Contents may follow the panel by a short delay. The exit is an eased fade and scale down, faster than the entrance.
**Detect.** Modals that hard-cut in, backdrops that pop while the panel animates, identical in/out timings.
**Fix.** Animate panel and backdrop from one state; `backdrop-filter: blur()` only where performance allows.

### MOT-11 · Tabs and indicators slide, never teleport (P2)
**Applies to.** tabs, segmented controls, any sliding indicator.
**Rule.** An active-tab indicator slides between tabs; content cross-fades (fade out, wait about 80 ms, fade in) with panel heights matched so the page below does not jump.
**Detect.** Indicator that jumps; content hard cut; layout shift when switching tabs.

### MOT-12 · Scroll-linked motion uses CSS timelines (P2)
**Applies to.** scroll-linked effects (reveals, progress bars, shrinking headers, parallax).
**Rule.** Bind scroll effects (reveal on enter, progress bars, shrinking headers, parallax) to `animation-timeline: scroll()` / `view()` with `animation-range`, instead of scroll listeners and rect maths. Keep a static fallback where unsupported.
**Detect.** `addEventListener('scroll', …)` driving styles every frame; scroll libraries used only for simple reveals.
**Fix.**
```css
@supports (animation-timeline: view()) {
  .reveal { animation: reveal linear both; animation-timeline: view(); animation-range: entry 0% cover 30%; }
}
```

### MOT-13 · Respect reduced motion (P0)
**Applies to.** any project with motion (always check).
**Rule.** Every non-essential animation turns off or becomes a short fade under `prefers-reduced-motion: reduce`. Parallax, auto-playing motion and large movements are removed entirely.
**Detect.** No `prefers-reduced-motion` handling anywhere; JS animations (Web Animations API, motion libraries) that ignore the setting.
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

---
Sources: animation-timing, easing-curves, card-hover-anatomy, modal-backdrop, perfect-button, button-feedback, tabs-system, accordion-disclosure, toggle-anatomy, scroll-driven-animations, reverse-engineered-linear, atomic-design, pull-to-refresh. See `sources.md`.
