---
name: refactor
description: Fix UI code so it follows the designmotionhq UX guidelines, either directly on a path or by working through the findings in UX-AUDIT.md, then verify and record what was fixed.
argument-hint: "[path | audit | F-001 F-004 … | P0]"
disable-model-invocation: true
---

# UX refactor

Change the code so it follows the guidelines in `${CLAUDE_PLUGIN_ROOT}/skills/ux-guidelines/`, without changing what the product does.

Target: `$ARGUMENTS`

## 1. Load the guidelines

Read `${CLAUDE_PLUGIN_ROOT}/skills/ux-guidelines/SKILL.md` and `references/report-format.md` from the same folder, then the topic references for the modules you will touch.

## 2. Decide what to fix

| Target | What to do |
|---|---|
| `audit` | Read `UX-AUDIT.md` and fix every `open` finding, P0 first, then P1, then P2. |
| Finding IDs (`F-001 F-004`) | Fix those findings from `UX-AUDIT.md`. |
| A severity (`P0`, `P0 P1`) | Fix the open findings of that severity from `UX-AUDIT.md`. |
| A path or glob | Audit just that scope quickly (same checks as the audit command, no report file), then fix what you find. |
| Empty | If `UX-AUDIT.md` exists, ask whether to work through it or a specific path; otherwise ask which path to refactor. |

If the target refers to `UX-AUDIT.md` and the file does not exist, say so and suggest running `/designmotionhq-ux:audit` first, or offer to refactor a path directly.

Before editing, check that each finding still applies to the current code. Mark findings that no longer apply as `fixed (already resolved)`.

## 3. Ask before cross-cutting changes

Make local fixes directly. Stop and ask first (one short question, with your recommendation) when a fix would:

- introduce a token system, a new dependency or a new shared component library;
- change behaviour users rely on (navigation structure, what a button does, apply-on-change vs explicit save);
- touch more than about 15 files for one finding;
- change copy that looks product- or legally-owned (pricing, consent text).

Mark such findings `needs decision (question)` and carry on with the rest.

## 4. Fix well

- Reuse the project's tokens, components, utilities and patterns. Add a token only when the scale lacks a value, and add it to the existing token file.
- Make the smallest change that satisfies the rule. Keep public component APIs stable; add props rather than renaming them.
- Fix all instances a finding lists, not only the first.
- Keep everything the audit lists under "What is already good".
- Never remove functionality to satisfy a rule, and never build a dark pattern (CON-8, CON-9) even if a finding seems to ask for it.
- Add or update tests when the project has tests for the touched component (for example a new empty or error state).

## 5. Verify

Run the project's own checks that exist: type-check, lint, unit tests, build. Fix failures your changes caused. If a check fails for reasons unrelated to your change, say so instead of hiding it. If the app can be run and a browser tool is available, look at the main screens you changed.

## 6. Record and reply

- When working from `UX-AUDIT.md`, update each finding's `Status` (`fixed`, `needs decision (question)`, `wontfix (reason)`) and append the refactor result block from `references/report-format.md`.
- In the conversation, list what was fixed by ID, what is waiting for a decision (with the question), and the checks you ran with their results. Keep it short; the diff is the detail.
