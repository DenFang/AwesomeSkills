---
name: ux-review
description: Review only the UI changes on the current branch, in the working tree, or in a given range or PR against the designmotionhq UX guidelines, and give a verdict with findings. Read-only.
argument-hint: "[base ref | commit range | branch | PR number; default: this branch since the default branch, plus uncommitted work]"
disable-model-invocation: true
---

# UX review of changes

Review what changed, not the whole codebase. Do not modify any source file.

Target: `$ARGUMENTS`

## 1. Load the guidelines

Read `${CLAUDE_PLUGIN_ROOT}/skills/ux-guidelines/SKILL.md` and `references/report-format.md` from the same folder. Load topic references only for the elements the change touches (step 3).

## 2. Collect the change

- **Not a git repository**: ask which files or folder to review, then review them as they are.
- **Empty target**: the base is `origin/<default>` if it exists, else the local `<default>` branch (find it with `git symbolic-ref --short refs/remotes/origin/HEAD`, falling back to `main`, then `master`). Review `git diff $(git merge-base <base> HEAD)`, which covers committed and uncommitted changes together, plus untracked files from `git ls-files --others --exclude-standard`. If HEAD equals the base and the tree is clean, review the last commit (`git diff HEAD~1 HEAD`) and say so.
- **A single ref that is an ancestor of HEAD** (`main`, `HEAD~3`, a SHA): use it as the base, as above.
- **A range** (`A..B`, `A...B`): `git diff <range>` exactly as given.
- **Any other branch name**: `git diff <base>...<branch>`.
- **A PR number**, with `gh` available: `gh pr diff <number>`.

Keep only UI-relevant files: components, pages, templates, styles, tokens, theme files, copy and i18n strings, and the handlers they call (submit, fetch, mutation code). Ignore lockfiles, generated output and unrelated backend code, except where server behaviour decides a UI rule (idempotency for FRM-10, server re-validation for STA-4). If nothing UI-related changed, say so in one line and stop. If more than about 60 UI files changed, review shared components and P0 rules first and list what you only skimmed.

## 3. Read in context and pick the rules

1. Read the project context once (guidelines Step 1): design system, product type, motion profile, platform.
2. For each changed hunk, read enough of the surrounding file to understand the component: its states, its props, the tokens it uses and the components it renders.
3. **Inventory the change** (guidelines Step 2): which elements the diff adds or alters (a menu, a form field, a table column, an animation, copy). Check the always-on rules plus the module rules for those elements only. A rule whose **Applies to** element is not in the change is not checked: a change to a dropdown menu is checked against INT-6, INT-3, MOT-1 and the always-on rules, not against table or form rules.
4. Read `.ux-ignore.md` if it exists.

## 4. Check the change

1. **P0 first**: missing focus style (INT-1), non-semantic clickable elements (INT-2), dialogs without focus management (INT-4), destructive actions without protection (INT-9), small targets (INT-11), hover-only actions (INT-12), missing labels (FRM-2), possible double submit (FRM-10), unsafe autosave (FRM-11), swallowed errors (STA-7), contrast and colour-only meaning (VIS-7, VIS-8), missing reduced motion (MOT-13), deceptive claims or dark patterns (CON-8, CON-9).
2. **New states**: new fetches and submits cover loading, empty, error and success (STA-1).
3. **Consistency**: new values come from existing tokens; new motion follows the project's motion profile; new copy follows the existing voice.

Report problems the change introduces or touches. A pre-existing problem in an untouched line is out of scope, unless the change makes it worse or it is a P0 in the same component; then add it under "Nearby, not introduced by this change".

## 5. Reply

Answer in the conversation using the review layout in `references/report-format.md`:

- Verdict: ✅ ready (no P0 or P1; P2 notes allowed), ⚠️ ready after the P1 fixes, or ⛔ needs changes (any P0).
- Findings numbered `R-001`, `R-002`, … with `path:line` in the new code, evidence, impact and a concrete fix (a small code suggestion when it helps).
- One to three things the change does well.

Write the review to a file only if the user asks. Offer `/ux-refactor R-001 R-002 …` to apply the fixes.
