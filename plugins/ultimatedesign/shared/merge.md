# Merge and score

How the three pass results (`passes.md`) become one report. Do the steps in order.

## 1. Normalise severity

Every finding keeps its `native_severity` and gets one shared level:

| Shared | Meaning | uichecker | impeccable | ui-ux-pro-max |
|---|---|---|---|---|
| **P0** | Blocks a task, loses data, misleads, or fails WCAG A/AA in a way that stops someone | P0 | P0 | a CRITICAL-category item (Accessibility, Touch and Interaction) whose failure blocks a task or fails WCAG A/AA |
| **P1** | Works, but causes real friction or reads as broken | P1 | P1 | other CRITICAL items; HIGH-category items (Performance, Style, Layout, Navigation) |
| **P2** | Polish that users notice | P2 | P2 | MEDIUM-category items (Typography and Color, Animation, Forms and Feedback) |
| **P3** | Nice to fix, no real user impact | (uichecker groups these into P2) | P3 | LOW-category items (Charts and Data polish) |

A pass may raise or lower the mapped level when the evidence says so (a HIGH layout item that hides the checkout button is P0); it states why in `problem`.

## 2. Verify before merging

Open the code for every P0, and for every P1 that only one pass reported. Keep a finding only if the element is in scope, the code shows the problem and the cited rule applies to that element. Drop the rest and count them under "Dropped as unverified". Never add findings of your own in this step: the report is the three skills' view.

## 3. Group the same problem

Two findings are the same problem when they point at the same element (same file and component, lines within about ten of each other, or the same shared token or component) **and** describe the same defect, even in different words ("no visible focus" and "outline: none without replacement"). Merge them into one unified finding `U-001`, `U-002`, …:

- **Sources**: every pass that reported it, with its own ID and rule (`K-4 INT-1 · I-2 Accessibility · P-7 focus states`).
- **Agreement**: 3/3, 2/3 or 1/3 of the available passes. With only two passes available, use 2/2 and 1/2.
- **Severity**: the highest shared level among its sources. Lower it only when the code you read in step 2 shows the higher rating's reason does not hold here (for example an index key on a list that holds no state), and say so in a severity note; if the sources differ by two levels or more, name both in that note.
- **Fix**: when the sources' fixes agree, one combined fix that keeps the most specific detail from each.

Findings that share an element but are different defects stay separate.

## 4. Find the disagreements

A disagreement is a choice the user should make, written as `D-1`, `D-2`, …. It exists when:

- two sources prescribe fixes for the same element that cannot both be applied (one says "one sans family on a tight scale", the other "pair a display serif for character"), or
- one source flags something that another explicitly recommends (glass panels, a gradient hero, a bold accent).

Each decision lists 2 to 4 options, one per position, each with: the source, the change, what it gains, what it costs. Add a combined option only when one honestly exists. Recommend one, using this precedence:

1. Accessibility, honesty and data-safety claims (WCAG, dark patterns, lost input) win over taste, whichever skill makes them.
2. The project's existing design system and tokens win over generic advice from any skill.
3. Then the product type: for brand surfaces (landing, marketing) weigh impeccable's brand guidance highest; for tool surfaces (app UI, admin, dashboards) weigh uichecker's and ui-ux-pro-max's product guidance highest.
4. Otherwise the option most sources agree on, then the smaller change.

Severity disagreements alone are not decisions; step 3 already takes the higher level.

## 5. Coverage and gaps

Build the coverage matrix: the eleven areas (`accessibility`, `states-feedback`, `forms`, `data-display`, `interaction-navigation`, `motion`, `visual-system`, `layout-responsive`, `content`, `performance`, `distinctiveness`) by the available sources, each cell `checked`, `partial`, `not covered` or `n/a`, from the passes' `coverage` fields.

- **Single-source findings** are where one skill knows something the others do not: keep them as findings (agreement 1/3), and in the report group them under "Only one skill caught this" so the user sees what each skill adds.
- An area that only one source checked is marked "single coverage"; an area no source checked goes to "Not checked".

## 6. Score

**Native scores** are shown as each skill produces them, unchanged: uichecker area scores 0 to 4, impeccable's audit health score out of 20 with its band, ui-ux-pro-max's checklist pass rate.

**Unified area scores** (0 to 4) come from the merged findings in that area:

| Score | Merged findings in the area |
|---|---|
| 0 | two or more P0 |
| 1 | one P0, or four or more P1 |
| 2 | two or three P1 |
| 3 | one P1, or three or more P2 |
| 4 | at most two P2, any number of P3, or nothing |

Areas that are `n/a` for every source are left out, never scored 0.

**UltimateDesign score** = the mean of the scored areas divided by 4, times 100, rounded. Bands: 90 to 100 excellent, 75 to 89 good, 60 to 74 acceptable, 40 to 59 poor, under 40 critical.

**Agreement rate** = the share of unified findings reported by two or more sources. A low rate is not a bad sign in itself: it means the skills cover different ground, and the single-source sections show where.

## 7. Order

Sort findings by severity, then agreement (higher first), then how many places are affected. The top five by impact go into the summary.
