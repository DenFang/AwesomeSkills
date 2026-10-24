---
lesson: 086
kind: carousel
type: ui
category: visual / design system
topic: UX checklists (intent first, one primary action, six states, audit and review checks, one decision per visual axis)
sources: image slides 1-7
---

# UX checklists: design before code, audit, review, restyle

**Hook (slide 1):** Claude skills for UX design, framed as a senior designer before the code.

Slides 2 to 6 each carry a five-item checklist that states concrete UI/UX rules. Those rules are extracted below.

## Slide by slide
- **Slide 2 (command 1 of 4: design it before you code).** Terminal pill: `/ux-design` runs the ux-designer sub-agent. Five numbered rows:
  1. User intent: who opens this screen and what they came to do.
  2. Wireframe plus spec, delivered before a single line of JSX.
  3. Action priority: one primary action per screen, and it is visible.
  4. All six states: loading, empty, error, success, partial, offline.
  5. DESIGN.md: a written contract every next screen has to obey.
  Footer line: it stops guessing and starts asking.
- **Slide 3 (command 2 of 4: find what's actually broken, on shipped UI).** Terminal pill: `/ux-audit [path or component]`. Five rows:
  1. Hierarchy: everything is loud, so nothing leads the eye.
  2. Missing states: what the screen does when data is empty or slow.
  3. Form friction: the field where people quietly give up.
  4. Dead affordance: actions that fire with no visible response.
  5. Ranked fixes: ordered by impact, each with the actual patch.
  Footer line: name the element, never write a vague suggestion to improve it. Bottom strip: ranked, not nitpicked.
- **Slide 4 (command 3 of 4: review the diff through a UX lens, last gate before merge).** Terminal pill: `/ux-review git diff · git diff main...HEAD`. Five rows:
  1. Reads your diff: uncommitted work or the full PR scope.
  2. ux-reviewer agent: a second pair of eyes with its own checklist.
  3. State regressions: the loading case someone dropped on the way.
  4. Drift control: new screen, same system, no third button style.
  5. Verdict per file: blocking or not, with the fix written out.
  Bottom strip: six sections, every diff.
- **Slide 5 (command 4 of 4: make it stop looking AI-made).** Terminal pill: `/restyle file · url · screenshot`. Five rows:
  1. Type: high contrast or deliberately low; the middle is not a choice.
  2. Color: a system with a role per value, not six vivid hues.
  3. Space: one scale, applied everywhere, including the tight parts.
  4. Finish: borders, radii and shadows that agree with each other.
  5. Before / after: visual only; logic and structure stay untouched.
  Footer line: generic is the absence of decisions. Bottom strip: four axes, one decision each.
- **Slide 6 (eight skills, one system).** Grid of skill names with one-line purposes: ux-intent-discovery (intent before pixels), information-hierarchy (what the eye hits first), state-completeness (all six states, always), form-ux (grouping, timing, validation), feedback-and-affordance (every action answers back), ux-auditor (specific, ranked, actionable), design-system (DESIGN.md, enforced), visual-character (one decision per axis). Pill: 2 sub-agents, ux-designer and ux-reviewer.

## Main rule
Decide intent, primary action and every data state before building a screen, then keep each visual axis (type, colour, space, finish) to one deliberate decision applied system-wide. Concretely: one visible primary action per screen; design all six states (loading, empty, error, success, partial, offline); every action gives a visible response; new screens reuse existing components instead of adding variants; audit findings name the exact element and come with a fix, ranked by impact.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 1 primary action | per screen, and it must be visible | slide 2 |
| 6 states | loading, empty, error, success, partial, offline | slides 2, 6 |
| 0 lines of code | wireframe and spec come before any JSX | slide 2 |
| 5 audit axes | hierarchy, missing states, form friction, dead affordance, ranked fixes | slide 3 |
| no third button style | drift limit: a new screen may not invent another button variant | slide 4 |
| 4 visual axes, 1 decision each | type, colour, space, finish | slide 5 |
| 1 role per colour value | colour system instead of many unrelated vivid hues | slide 5 |
| 1 spacing scale | used everywhere, tight areas included | slide 5 |
| 2 type contrast options | high, or deliberately low; not in between | slide 5 |

## Before / after
- **Code first vs design first (slide 2).** Bad: start writing UI and discover the purpose and states along the way. Good: intent, wireframe, spec, primary action and states settled before the first line. Why: states and priority are structural; adding them late means retrofitting layouts and usually skipping the empty, partial and offline cases.
- **Several equal buttons vs one primary (slide 2).** Good: one primary action per screen, clearly visible. Why: a single emphasized action tells the user what the screen is for; when several compete, none reads as the next step.
- **Everything loud vs a clear lead (slide 3).** Bad: every element has strong weight, size or colour. Good: one element leads and the rest step down. Why: emphasis only works by contrast with what is not emphasized; uniform loudness leaves the eye with no entry point.
- **Silent action vs visible response (slides 3, 6).** Bad: a click that does something with no visible change. Good: every action answers back. Why: without feedback users cannot tell if it worked, so they repeat the click or abandon the task.
- **Vague vs actionable findings (slide 3).** Bad: generic advice to consider improving something. Good: the named element, ranked by impact, with the patch. Why: a specific, ordered list can be executed; a vague one gets ignored.
- **Drift vs one system (slide 4).** Bad: a new screen adds a third button style. Good: reuse the existing variants. Why: each extra variant weakens the meaning of the existing ones and makes the product feel stitched together.
- **Middle-ground styling vs decided styling (slide 5).** Bad: medium type contrast, many unrelated vivid hues, ad hoc spacing, mismatched radii and shadows. Good: type contrast either strong or deliberately subdued, colours assigned by role, one spacing scale, borders, radii and shadows from one family. Why: a generic look comes from undecided defaults; a clear choice per axis, applied consistently, reads as intentional.

## Do
- Write down who opens the screen and what they came to do before designing it.
- Give each screen exactly one primary action and make it visible.
- Design loading, empty, error, success, partial and offline states for every data view, and keep the loading state when refactoring.
- Make every action produce a visible response.
- Reuse existing component variants; record the system in one contract document that new screens follow.
- Pick one type contrast strategy, a colour system by role, one spacing scale and one finish family (border, radius, shadow), and apply them everywhere.
- In reviews and audits, name the exact element, rank by impact and attach the fix.

## Don't
- Don't start JSX before intent, primary action and states are settled.
- Don't let every element shout; don't put several equal primary buttons on one screen.
- Don't ship actions with no visible response.
- Don't add a new button style for a new screen.
- Don't use many unrelated vivid hues, mixed radii or ad hoc spacing.
- Don't write findings like a generic suggestion to improve something.

## Video slide
None; all 7 slides are static images.

## Notes for the skill
- Partial state: some data loaded and some failed or is still coming (e.g. one widget errors on a dashboard). Show what is available and mark the failed part locally with a retry, instead of failing the whole screen. Offline: show cached data with a clear offline notice and queue or disable actions that need the network.
- Status changes (loading done, error, success, offline) that appear without focus moving should be announced through a live region (WCAG 4.1.3 Status Messages).
- Low type contrast means a small difference in size or weight between levels, not low colour contrast: text still needs 4.5:1 (3:1 for large text) against its background (WCAG 1.4.3).
- Colour by role (accent, danger, muted text, surface) also requires that meaning is not carried by colour alone (WCAG 1.4.1); pair danger colour with text or an icon.
- Visible response: the common usability heuristic is acknowledgement within about 100 ms; longer work needs a progress indicator.
- One primary action per screen does not mean one button; secondary actions stay but take lower emphasis. Destructive actions should not be the primary styled button unless destruction is the screen's purpose.
- The slides teach rules only as one-line checklist items; thresholds (which spacing scale, which type ratio) are not given and should come from the project's design system.
