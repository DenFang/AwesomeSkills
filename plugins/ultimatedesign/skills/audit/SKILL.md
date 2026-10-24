---
name: audit
description: Run impeccable, ui-ux-pro-max and uichecker over the whole UI (or a path) as three independent passes, merge their findings into one scored report with agreement, disagreements to choose from and gaps, and write it to ULTIMATE-DESIGN.md. Read-only.
argument-hint: "[path] [--deep]"
disable-model-invocation: true
---

# UltimateDesign audit

Three design skills look at the same code on their own, and you combine what they found: where they agree, where they disagree (the user picks) and what only one of them knows. Do not modify any source file; the only file you write is `ULTIMATE-DESIGN.md`.

Target: `$ARGUMENTS` (a path, or empty for the whole project; `--deep` also runs impeccable's heuristic critique).

## 1. Load the method

Read `${CLAUDE_PLUGIN_ROOT}/shared/passes.md`, `${CLAUDE_PLUGIN_ROOT}/shared/merge.md` and `${CLAUDE_PLUGIN_ROOT}/shared/report-format.md`.

## 2. Find the members

Resolve uichecker, impeccable and ui-ux-pro-max to their folders (passes.md section 1). Tell the user in one line which copies you will use and which are missing, with the install command for a missing one. Fewer than two available: stop after saying so.

## 3. Scope and shared brief

1. Scope: the given path, or every UI file in the project (components, pages, templates, styles, tokens, theme, copy). Skip `node_modules`, build output, vendored and generated files. If the scope is very large (more than about 300 UI files), audit shared components, tokens and the main screens first and list the rest under "Coverage".
2. Write the shared brief (passes.md section 2): stack, product type, design system, project notes. Read real files to decide; do not guess from the folder name.

## 4. Run the passes

Launch one subagent per available member, in parallel, in audit mode (passes.md section 6). Each brief contains: the member's folder, the shared brief, the scope list, the rules from passes.md section 3 verbatim and the member's section 4 text, and the return shape from section 5. With `--deep`, the impeccable pass also does its deep-mode step.

Collect the JSON from each. If a pass fails or returns no JSON, retry it once; if it fails again, continue without it and say so.

## 5. Merge

Follow merge.md steps 1 to 7: normalise, verify P0s and single-source P1s against the code, group into `U-` findings, write `D-` decisions with a recommendation, build the coverage matrix, score, sort.

## 6. Write the report

Write `ULTIMATE-DESIGN.md` at the project root (or inside the target path when one was given) in the audit layout of report-format.md. If one already exists, replace it and note the previous score in the summary line ("was 64").

## 7. Reply

In the conversation, keep it short:

- the UltimateDesign score and band, the agreement rate and each skill's native score on one line;
- the top five findings by impact, one line each with ID, severity and agreement;
- each decision as a one-line question with its options and your recommendation;
- what is missing (a skill not installed, an area nobody checked).

Then offer the next step: `/ultimatedesign:apply` with the recommended choices (for example `/ultimatedesign:apply recommended`, or `/ultimatedesign:apply P0 D-1=A D-2=B`).
