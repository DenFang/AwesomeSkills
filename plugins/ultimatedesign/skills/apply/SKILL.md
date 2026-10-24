---
name: apply
description: Apply the fixes and the choices the user picked from an UltimateDesign audit or review, using the chosen skill's fix for each disagreement, then run the project's checks and update the report.
argument-hint: "[recommended | P0 | P0 P1 | U-001 … | D-1=A … ]"
disable-model-invocation: true
---

# UltimateDesign apply

Change the code so the chosen findings are fixed, without changing what the product does.

Target: `$ARGUMENTS`

## 1. Find the source

- After `/ultimatedesign:audit`: read `ULTIMATE-DESIGN.md` (the target path first, then the project root).
- After `/ultimatedesign:review` in this conversation: use that review.
- Neither exists: say so and suggest running one of them first.

Read `${CLAUDE_PLUGIN_ROOT}/shared/merge.md` and `${CLAUDE_PLUGIN_ROOT}/shared/report-format.md`.

## 2. Work out the set

| Target | What to fix |
|---|---|
| `recommended` | every open finding, P0 first, and every decision with its recommended option |
| A severity (`P0`, `P0 P1`) | the open findings of those levels |
| IDs (`U-003 U-007`) | those findings |
| Choices (`D-1=A D-2=B`) | those decisions with the chosen option; they can be combined with the forms above |
| Empty | ask which of the above, and show the open decisions with their recommendations |

A decision without a choice is not applied; list it at the end. A choice of an option that does not exist is an error: ask again.

## 3. Before the first edit

- Run `git status`. If there are uncommitted changes, say so, so the user can tell your changes from theirs.
- Check each selected finding still applies to the current code; mark the ones that do not as `fixed (already resolved)`.
- Read the safety list in uichecker's refactor command (`<uichecker>/skills/refactor/SKILL.md`, section "Fix well"); it applies to every fix here, whichever skill it came from. Changes it says need a decision are marked `needs decision (question)` and collected for the end.

## 4. Fix

- For a unified finding, apply its combined fix in the project's own components and tokens.
- For a decision, apply the chosen option exactly as that skill described it. If the chosen skill is installed and the fix is one of its named commands (an impeccable `/impeccable typeset` or `polish` step, a uichecker rule's **Fix**, a ui-ux-pro-max search result for the stack), read that skill's instructions for the change before editing, and stay inside the finding's scope.
- Fix the root once when many findings share it (one token, one shared component).
- Never apply two options of the same decision, and never undo a choice the user made in an earlier run without asking.

## 5. Check and record

Run the project's own checks (type-check, lint, tests, build) that apply to the changed files. If a check fails because of your change, fix it or revert that change and mark the finding `needs decision`.

Update each finding's **Status** and each decision's **Choice** in `ULTIMATE-DESIGN.md` (when working from it). Finish in the conversation with:

```markdown
## Apply result
Fixed: U-001, U-003 (n files changed) · Applied choices: D-1=A, D-2=B
Needs decision: U-009: <question> (recommended: <answer>)
Not chosen yet: D-3
Checks run: <checks and results>
```

Suggest re-running `/ultimatedesign:audit` (or `review`) to see the new score.
