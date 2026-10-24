---
name: review
description: Review only the UI changes on the current branch or in the working tree against the designmotionhq UX guidelines, and give a verdict with findings. Read-only.
argument-hint: "[base ref, commit range, or PR branch; default: changes since the main branch plus uncommitted work]"
disable-model-invocation: true
---

# UX review of changes

Review what changed, not the whole codebase. Do not modify any source file.

Target: `$ARGUMENTS`

## 1. Load the guidelines

Read `${CLAUDE_PLUGIN_ROOT}/skills/ux-guidelines/SKILL.md` and `references/report-format.md` from the same folder. Load topic references only for the modules the diff touches (routing table in the guidelines).

## 2. Collect the change

- If the target is empty: find the default branch (`git symbolic-ref refs/remotes/origin/HEAD`, falling back to `main` or `master`), then review `git diff <merge-base>...HEAD` plus staged and unstaged changes (`git diff HEAD`) and new untracked UI files.
- If the target is a ref or range (`main`, `HEAD~3`, `abc123..def456`): review `git diff <target>` accordingly.
- If the target is a branch name: review `git diff <default>...<branch>`.
- Keep only UI-relevant files: components, pages, templates, styles, tokens, theme files, copy and i18n strings, and the handlers they call (submit, fetch, mutation code). Ignore lockfiles, generated output and unrelated backend code, except where server behaviour decides a UI rule (idempotency for FRM-10, server validation for STA-4).
- If nothing UI-related changed, say so in one line and stop.

## 3. Read in context

For each changed hunk, read enough of the surrounding file to understand the component: its states, its props, the tokens it uses, and the components it renders. Check the project's design system so you judge the change against the project's own conventions.

## 4. Check the change

For every module the diff adds or alters, check the rules that apply. Prioritise:

1. **P0 first**: missing focus style, non-semantic clickable elements, hover-only actions, dialogs without focus management, swallowed errors, possible double submit, contrast or colour-only meaning, dark patterns.
2. **New states**: new fetches and submits cover loading, empty, error and success (STA-1).
3. **Consistency**: new values come from existing tokens; new motion follows the project's motion profile; new copy follows the existing voice.

Report problems that the change introduces or touches. A pre-existing problem in an untouched line is out of scope, unless the change makes it worse or it is a P0 in the same component; then add it under "Nearby, not introduced by this change".

## 5. Reply

Answer in the conversation using the review layout in `references/report-format.md`:

- Verdict: ✅ ready, ⚠️ ready after the P1 fixes, or ⛔ needs changes (any P0).
- Findings with `path:line` in the new code, evidence, and a concrete fix (a small code suggestion when it helps).
- One to three things the change does well.

Write the review to a file only if the user asks. Offer `/designmotionhq-ux:refactor <IDs>` to apply the fixes.
