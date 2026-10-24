---
name: review
description: Review only the UI changes on the current branch, in the working tree, or in a given range or PR with impeccable, ui-ux-pro-max and uichecker, then give one merged verdict with agreement and choices. Modes - default (parallel subagents), --current (same passes in this session), --lite (one fast pass over a de-duplicated rule list). Read-only.
argument-hint: "[base ref | commit range | branch | PR number] [--current | --lite]"
disable-model-invocation: true
---

# UltimateDesign review of changes

Review what changed, not the whole codebase. Do not modify any file.

Target: `$ARGUMENTS`: what to review (empty for the default), optionally one mode flag, `--current` or `--lite`.

## 1. Load the method

Read `${CLAUDE_PLUGIN_ROOT}/shared/modes.md`, `${CLAUDE_PLUGIN_ROOT}/shared/passes.md`, `${CLAUDE_PLUGIN_ROOT}/shared/merge.md` and `${CLAUDE_PLUGIN_ROOT}/shared/report-format.md`. Pick the mode (modes.md section 1); `--deep` has no effect in a review.

## 2. Find the members

As in passes.md section 1. One line to the user on which copies run and in which mode; fewer than two available: say so and stop.

## 3. Collect the change

Use the rules in uichecker's review command, section "Collect the change" (`<uichecker>/skills/review/SKILL.md`): the default base, ranges, branches, PR numbers read without checking out, and the filter that keeps only UI-relevant files. Not a git repository, or nothing UI-related changed: say so in one line and stop.

Write the shared brief (passes.md section 2) once, and add to it: the exact diff command, the list of changed UI files, and the instruction that findings must be introduced or touched by the change. A P0 in an untouched line of a changed component may be reported as "nearby".

## 4. Run and merge

Follow the chosen mode in modes.md, in review mode, on the change only:

- **full**: section 2, one subagent per member, then merge.md steps 1 to 7;
- **current**: section 3, the passes one after another in this session, then merge.md steps 1 to 7;
- **lite**: section 4, the rule-level merge and one check of the changed code.

impeccable and ui-ux-pro-max check the changed files only; uichecker follows its review procedure.

## 5. Reply

Answer in the conversation in the review layout of report-format.md, with the mode in the header:

- Verdict: ✅ ready (no P0 or P1), ⚠️ ready after the P1 fixes, ⛔ needs changes (any P0).
- Findings `U-001`, … with `path:line` in the new code, their sources and agreement, and a concrete fix.
- Decisions `D-1`, … where the skills disagree, each with a recommendation.
- Coverage gaps for this change, and one to three things the change does well.

Write the review to a file only if the user asks. Offer `/ultimatedesign:apply U-001 D-1=A …` to apply the fixes.
