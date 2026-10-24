---
name: refactor
description: Fix UI code so it follows the designmotionhq UX guidelines, either directly on a path, from the findings in UX-AUDIT.md, or from the last review, then verify and record what was fixed.
argument-hint: "[audit | P0 | P0 P1 | F-001 F-004 … | R-001 … | path]"
disable-model-invocation: true
---

# UX refactor

Change the code so it follows the guidelines in `${CLAUDE_PLUGIN_ROOT}/skills/guidelines/`, without changing what the product does.

Target: `$ARGUMENTS`

## 1. Load the guidelines

Read `${CLAUDE_PLUGIN_ROOT}/skills/guidelines/SKILL.md` and `references/report-format.md` from the same folder, then the topic references for the elements you will touch.

## 2. Decide what to fix

| Target | What to do |
|---|---|
| `audit` | Fix every `open` finding in `UX-AUDIT.md`, P0 first, then P1, then P2. |
| A severity (`P0`, `P0 P1`) | Fix the open findings of that severity from `UX-AUDIT.md`. |
| Audit IDs (`F-001 F-004`) | Fix those findings from `UX-AUDIT.md`. |
| Review IDs (`R-001 R-003`) | Fix those findings from the most recent review in this conversation; if there is none, ask the user to run `/uichecker:review` first. |
| A path or glob | Inventory that scope and check the rules that apply (same method as the audit, no report file). List the findings first. Fix the P0 and P1 problems that are local and leave the look unchanged (labels, focus, states, semantics); ask before applying any that change visible design, and before any P2. |
| Empty | If `UX-AUDIT.md` exists, ask whether to work through it or a specific path; otherwise ask which path to refactor. |

Look for `UX-AUDIT.md` and `.ux-ignore.md` in the target path when it is a path, otherwise in the current directory, then at the repository root. If the target needs it and it does not exist, say so and suggest `/uichecker:audit`, or offer to refactor a path directly.

Before editing, check that each finding still applies to the current code. Mark findings that no longer apply as `fixed (already resolved)`.

## 3. Before the first edit

- Run `git status`. If there are uncommitted changes, say so, so the user can tell your changes from theirs.
- Read the project context (guidelines Step 1) and keep to its design system.
- If more than about 20 findings are open, work in batches by severity and run the checks (step 5) after each batch.

## 4. Fix well

Make local fixes directly. Do not make the change yourself when a fix would:

- introduce a token system, a new dependency or a new shared component library;
- change behaviour users rely on (navigation structure, what a button does, apply-on-change vs explicit save);
- touch more than about 15 files for one finding;
- change copy that looks product- or legally-owned (pricing, consent text, claims that need real numbers);
- change the value of an existing shared token (a colour, radius or type step) that other screens use, rather than adding a new one;
- replace a confirmation with undo, or otherwise need server changes (soft delete, idempotency keys, a new pagination model).

Mark such findings `needs decision (question)`, carry on with the rest, and ask all the questions together at the end, each with your recommendation.

While fixing:

- Reuse the project's tokens, components, utilities and patterns. Add a token only when the scale lacks a value, and add it to the existing token file.
- Make the smallest change that satisfies the rule. Keep public component APIs stable; add props rather than renaming them.
- Fix all instances a finding lists, not only the first.
- Apply only rules whose **Applies to** element is in the code you touch; do not "improve" unrelated components on the way.
- Keep everything the audit lists under "What is already good".
- Never remove functionality to satisfy a rule, and never build a dark pattern (CON-8, CON-9), even if a finding seems to ask for it.
- Add or update tests when the project has tests for the touched component (for example a new empty or error state).

## 5. Verify

Run the project's own checks that exist: type-check, lint, unit tests, build. Fix failures your changes caused. If a check fails for reasons unrelated to your change, say so instead of hiding it. If the app can be run without installing or configuring anything and a browser tool is available, look at the main screens you changed. If there are no checks at all, say that the changes are unverified.

## 6. Record and reply

- When working from `UX-AUDIT.md`, update each finding's `Status` (`fixed`, `fixed (already resolved)`, `needs decision (question)`; `wontfix (reason)` only when the user declined the fix) and append the refactor result block from `references/report-format.md`.
- In the conversation, list what was fixed by ID (or by rule ID and file in path mode), the questions that need a decision with your recommendation, and the checks you ran with their results. Keep it short; the diff is the detail. Do not commit unless the user asks.
