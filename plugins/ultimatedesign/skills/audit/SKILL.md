---
name: audit
description: Run impeccable, ui-ux-pro-max and uichecker over the whole UI (or a path), merge their findings into one scored report with agreement, disagreements to choose from and gaps, and write it to ULTIMATE-DESIGN.md. Modes - default (parallel subagents), --current (same passes in this session), --lite (one fast pass over a de-duplicated rule list). Changes no code.
argument-hint: "[path] [--deep] [--current | --lite]"
disable-model-invocation: true
---

# UltimateDesign audit

Do not modify any source file; the only file you write is `ULTIMATE-DESIGN.md`.

Target: `$ARGUMENTS`: a path (or empty for the whole project), optionally `--deep` (also runs impeccable's heuristic critique) and one mode flag, `--current` or `--lite`.

## 1. Load the method

Read `${CLAUDE_PLUGIN_ROOT}/shared/modes.md`, `${CLAUDE_PLUGIN_ROOT}/shared/passes.md`, `${CLAUDE_PLUGIN_ROOT}/shared/merge.md` and `${CLAUDE_PLUGIN_ROOT}/shared/report-format.md`. Pick the mode (modes.md section 1).

## 2. Find the members

Resolve uichecker, impeccable and ui-ux-pro-max to their folders (passes.md section 1). Tell the user in one line which copies you will use, which are missing (with the install command for a missing one) and which mode runs. Fewer than two available: stop after saying so.

## 3. Scope and shared brief

1. Scope: the given path, or every UI file in the project (components, pages, templates, styles, tokens, theme, copy). Skip `node_modules`, build output, vendored and generated files. If the repository holds several apps and no path was given, ask which one. If there are no UI files, say so and stop. If the scope has more than about 150 UI files, audit shared components, tokens and at least one screen of each element type first, and list the rest under "Coverage".
2. Write the shared brief (passes.md section 2): stack, product type, design system, project notes. Read real files to decide; do not guess from the folder name.

## 4. Run and merge

Follow the chosen mode in modes.md, in audit mode:

- **full**: section 2, one subagent per member, then merge.md steps 1 to 7;
- **current**: section 3, the passes one after another in this session, then merge.md steps 1 to 7;
- **lite**: section 4, the rule-level merge and one code check.

With `--deep` in full or current, the impeccable pass also does its deep-mode step.

## 5. Write the report

Write `ULTIMATE-DESIGN.md` at the project root in the audit layout of report-format.md, with the mode in the header and the audited path in the Scope line. If one already exists, replace it, note the previous score and its mode in the summary line ("was 64, full"), and carry over `wontfix` statuses and choices already made, matched by element and sources, so renumbered findings and decisions keep them.

## 6. Reply

In the conversation, keep it short:

- the mode, the UltimateDesign score and band, the agreement rate (rule overlap in lite) and, in full and current, each skill's native score, on one line;
- the top five findings by impact, one line each with ID, severity and agreement;
- each decision as a one-line question with its options and your recommendation;
- what is missing (a skill not installed, an area nobody checked).

Then offer the next step: `/ultimatedesign:apply` with the recommended choices (for example `/ultimatedesign:apply recommended`, or `/ultimatedesign:apply P0 D-1=A D-2=B`). After a lite audit, mention that a full audit gives independent agreement.
