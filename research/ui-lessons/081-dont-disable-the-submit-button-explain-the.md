---
lesson: 081
kind: video
duration_s: 49
type: ui
category: interaction
topic: disabled submit buttons vs validate-on-click and busy state
sources: frames, voice-over, lesson notes
---

# Don't disable the submit button, explain the blocker

**Hook:** Clicking a greyed-out button does nothing, and nothing tells the user why.

## Main rule
Keep the primary/submit button enabled; on click, validate, mark every field that blocks submission with an inline message, and move focus to the first one. For an in-flight request use a separate busy state (button stays focusable, shows a spinner and progress label, reports busy) instead of the disabled state.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| clicks 3 / events 0, "no state change" ×3 | three clicks on the disabled button produce no event and no feedback | 0:00-0:03 on-screen event log |
| stop 1/5 … 5/5 | tab order of the form: Project name, Region, Team, Terms, Cancel; "Create project" is skipped | 0:04-0:15 on-screen |
| tabindex −1 ("skipped") | how the demo labels the disabled button's absence from the tab order | 0:10-0:15 on-screen |
| 1.7:1 → 1.9:1 | measured contrast of the grey disabled label on grey surface (counter animates, settles at 1.9:1) | 0:12-0:15 on-screen |
| 4.5:1 required, "FAIL · WCAG AA" | normal-text contrast threshold the disabled label is compared to | 0:04-0:15 on-screen; page also says 1.9:1 vs 4.5:1 |
| `pointer-events: none` | style on the disabled button that kills hover, so its tooltip ("Pick a region first") never shows | 0:17-0:24 on-screen |
| "2 to fix" → "1 to fix" → "all clear" | validation panel counter after clicking Create | 0:28-0:35 on-screen |
| `aria-busy="true"` / `aria-busy="false"` | busy ("Creating…") vs done ("Project created") button states | 0:36-0:44 on-screen + voice |
| State audit: disabled no/no/no; busy yes/yes/yes; done yes/n/a/yes | rows "in the tab order", "announces progress", "keeps the user's place" | 0:37-0:44 on-screen |

## Before / after
- **Disabled submit vs live submit with validation on click.** Bad: "Create project" is greyed out; clicks are swallowed with no state change, so the user must guess that Region and Terms are missing. Good: the button is enabled; on click, Region and Terms get an error outline and inline messages ("Pick a region", "Accept the terms"), a validation summary lists "2 to fix", focus jumps to Region, and each fix flips its row to "fixed" until "all clear". Why: same protection against invalid submission, but the reason and the next step are visible and reachable ("same protection, no dead end").
- **Keyboard path.** Bad: Tab goes Project name → Region → Team → Terms → Cancel; the disabled button is skipped and the screen reader announces nothing for it, so a keyboard or screen-reader user never learns that a blocked submit exists. Good: an enabled button stays in the tab order and its click produces announced feedback.
- **Tooltip on a disabled button.** Bad: an explanatory tooltip is attached to the disabled button, but `pointer-events: none` means hover never fires ("hover → nothing", "no pointer events, no reason"). Side-by-side hover test: the enabled "Save draft" shows "Saves to your drafts", the disabled one shows nothing. Good: put the reason in reachable inline text tied to the field, not in a tooltip on a dead control.
- **Disabled while loading vs busy.** Bad: greying the button during the request removes it from the tab order, drops focus ("focus lost") and announces nothing. Good: busy state keeps focus on the button, shows a spinner with "Creating…", sets `aria-busy="true"`, then "Project created" with focus still kept. Why: the user keeps their place and gets progress feedback; double-submit can be blocked in code without disabling.
- **Contrast.** Bad: grey label on grey surface at about 1.9:1 is hard to read at all.

## Do
- Keep the submit button enabled and validate on click.
- On failed submit: outline each blocking field, show an inline message under it, list the blockers in a summary with a count, and move focus to the first invalid field.
- Update each blocker live as it is fixed (count decreases, inline success text such as "Region set to eu-west-1", "Terms accepted").
- For async actions use a distinct busy state: keep focus, show a spinner plus a verb label ("Creating…"), report busy, then a done state ("Project created").
- Guard against double submission in the handler (ignore clicks while busy) rather than by disabling.
- Put any explanation of a blocked action in visible text that keyboard and screen-reader users can reach.

## Don't
- Don't disable submit and leave the user to guess what is missing.
- Don't rely on a tooltip on a disabled control to explain why it is disabled.
- Don't treat loading as disabled; greying out mid-request drops focus and the user's place.
- Don't ship low-contrast grey-on-grey labels for controls the user still needs to read.

## Scene by scene
- 0:00 Form "New project" (Project name filled "northwind-api", Region empty "Select a region", Team "Core platform", unchecked "Accept the terms"), greyed "Create project" button and Cancel link. Cursor clicks the button three times; event log shows "click 1/2/3 · no state change", "clicks 3", "events 0".
- 0:02 Caption "Don't disable. Explain."
- 0:04 Section "Tab order: The keyboard skips right past it." Focus ring moves stop 1/5 to 4/5 through the fields; screen-reader panel reads each ("Project name, edit text, northwind-api", "Region, combo box, collapsed", "Team, combo box, Core platform", "Terms, checkbox, not checked"). Contrast panel "measuring…", "4.5:1 required".
- 0:09 Focus leaves Terms; a dashed arrow loops around the disabled button to Cancel; screen-reader panel briefly "silent (nothing announced)"; badge "skipped · tabindex −1"; stop 5/5 "Cancel, link".
- 0:12 Contrast readout counts up to 1.7:1 then 1.9:1 with a short danger-coloured bar far left of the "4.5 min" marker; badge "FAIL · WCAG AA".
- 0:16 Section "Pointer events: The tooltip never fires." Cursor hovers the disabled button; annotation `pointer-events: none`; the hint "Pick a region first" stays ghosted. Hover test panel: enabled "Save draft" shows tooltip "Saves to your drafts" ("hover → tooltip"), disabled "Save draft" shows "no event" ("hover → nothing"). Caption "no pointer events, no reason".
- 0:25 Section "Validate on click: Keep it live. Explain." Button becomes enabled (primary accent). Validation panel "runs on submit · Nothing is blocked yet, press Create to check."
- 0:28 Click: Region and Terms get warning outlines and messages "Pick a region", "Accept the terms"; panel "2 to fix" (Region: focus →, Terms: queued); focus ring lands on Region. Caption "same protection, no dead end".
- 0:31 Region set to "eu-west-1" (success check, "Region set to eu-west-1"); panel "1 to fix", focus moves to Terms; checkbox ticked, "Terms accepted", panel "all clear".
- 0:36 Section "Loading state: Busy is not disabled." Three rows: disabled ("focus lost"), busy "Creating…" with spinner, `aria-busy="true"`, "focus kept", done "Project created", `aria-busy="false"`, "focus kept". State-audit table fills in. Caption "busy keeps the focus".
- 0:46 End card "Don't disable. Explain." recap list: 01 Out of the tab order, 02 The tooltip never fires, 03 Explain the blocker, 04 Busy is not disabled; follow / save CTA.

## Voice-over summary
- A click on the grey button does nothing and nothing explains why.
- A disabled button leaves the tab order; keyboard users skip it and screen readers say nothing, so the block exists unannounced; grey-on-grey also fails contrast.
- A tooltip can't rescue it, because pointer events are dead on a disabled element; the reason becomes "unreachable by design".
- Keep the button live: on click, validate, highlight the two blocking fields and move focus to the first.
- Disabled and loading are different: during a request the button keeps focus, spins and reports busy; greying it out throws away the user's place.

## Notes for the skill
- Implementation: `<button type="submit">` stays enabled; on submit run validation, set `aria-invalid="true"` on failing fields, connect messages with `aria-describedby`, focus the first invalid field. An error summary at the top/bottom with links to fields is the GOV.UK-style pattern; announce it via a live region or by focusing it.
- If a control really must be unavailable, prefer `aria-disabled="true"` over the `disabled` attribute: it stays focusable and receives events, so a tooltip or explanation can still be reached; block activation in the click handler.
- Busy state: keep the button in the DOM and focused, change its label ("Creating…"), and ignore repeat clicks. `aria-busy` on a button has weak screen-reader support; also announce progress/completion through a polite live region (`role="status"`). Spinner should honour `prefers-reduced-motion`.
- Correction (WCAG): SC 1.4.3 explicitly exempts text in inactive (disabled) user-interface components from the 4.5:1 contrast requirement, so "fails WCAG AA" is not technically a failure. The usability point still stands: 1.9:1 is hard to read, and if you avoid disabling, the issue disappears.
- Correction (screen readers): a natively disabled button is skipped by Tab, but screen readers can still reach it in browse/virtual-cursor mode and announce it as "dimmed"/"unavailable". The real problem is that the reason is never announced, not that the button is invisible to assistive tech.
- Correction (events): the `disabled` attribute itself suppresses click and most mouse events in browsers even without CSS; the demo's `pointer-events: none` is a common design-system style that makes the hover failure certain. Either way, tooltips on disabled controls are unreliable; a wrapper element with the tooltip is a workaround, but it is still unreachable by keyboard.
- Edge case: disabling can still be appropriate where the reason is obvious and visible (e.g. a "Next" button in a paged list on the last page) or for permission-gated actions with visible explanatory text nearby.
