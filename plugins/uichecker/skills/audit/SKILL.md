---
name: audit
description: Audit the whole UI codebase (or a given path) against the designmotionhq UX guidelines and write a prioritised, scored report to UX-AUDIT.md. Read-only; it changes no code.
argument-hint: "[path or glob, default: whole project]"
disable-model-invocation: true
---

# UX audit

Audit the project's interface code against the guidelines in `${CLAUDE_PLUGIN_ROOT}/skills/guidelines/`. Do not modify any source file, install dependencies or change configuration. The only file you write is the report.

Scope: `$ARGUMENTS` (if empty, the whole project).

## 1. Load the guidelines

Read `${CLAUDE_PLUGIN_ROOT}/skills/guidelines/SKILL.md`, then `references/report-format.md` and `references/detection.md` from the same folder. Load the topic references only when the inventory (step 2) contains elements they cover.

## 2. Map the project

1. **Scope.** If the repository holds several apps or packages and no path was given, ask which one to audit (or offer to audit each in turn). If no UI files are found in scope, say so in one line and stop without writing a report.
2. **Context** (guidelines Step 1): stack and platform, design system location, product type (tool, brand or both), motion profile. Write down why for each.
3. **Inventory** (guidelines Step 2): list the screens or routes and, for each, the elements they actually contain: forms, tables, modals, menus, navigation, charts, uploads, animations, marketing sections and so on. This inventory decides which rules you check. A rule whose **Applies to** element is not in the inventory is not checked and not reported.
4. **Size.** Skip `node_modules`, build output, vendored code, generated files, stories and test snapshots unless asked. If the scope has more than about 150 UI files, audit shared components first, then at least one screen of each element type in the inventory, and list what you sampled under "Not checked".
5. **Ignore file.** Read `.ux-ignore.md` if it exists (format in `report-format.md`).

## 3. Holistic pass

Before checking rules one by one, read the main screens as a designer would and note, in a few lines:

- **First impression**: what the eye lands on first, and whether that is right; whether the purpose of each main screen is clear in a few seconds.
- **Generated look**: does it show the tells in CON-3 or CON-6?
- **Flows**: the main tasks (sign up, create, pay, find) from start to end: missing states, dead ends, unclear next steps, how flows end (CON-5).
- **Consistency**: do similar things look and behave alike across screens?

Keep these notes separate from the rule findings until step 5, so the systematic checks are not anchored by first impressions. Turn each holistic problem you can locate in code into a finding with the closest rule ID.

## 4. Systematic pass

1. **Fast sweep.** Run the searches in `references/detection.md` for the rules that apply. Treat every match as a lead and open the code to confirm. Count how often each pattern appears.
2. **Rules that can be P0 first**, wherever they apply: INT-1, INT-2, INT-4, INT-9, INT-11, INT-12, FRM-2, FRM-10, FRM-11, STA-1, STA-7, DAT-13, VIS-7, VIS-8, MOT-3, MOT-12, MOT-13, CON-8, CON-9, CON-10, CON-12. Several are P0 only in the case their heading names (for example CON-10 only when single-key shortcuts fire while typing); report the severity the evidence supports.
3. **Then the module rules** from the routing table for each element in the inventory, plus the always-on rules. For reference, the modules span states (STA-1…18), forms (FRM-1…21), data (DAT-1…19), interaction (INT-1…28), motion (MOT-0…16), visual system (VIS-1…21) and content (CON-1…13); a rule is checked only when its element is in the inventory. Read the code; do not report from a regex match alone.
4. **Verify** each candidate finding: the element is really there, the rule really applies to it, and the evidence shows the problem. Drop anything you cannot point at.

Static code cannot prove everything (contrast over images, the real feel of an animation, layout at a given width). If the app can be run without installing or configuring anything and a browser tool is available, you may check a few key screens; otherwise list such items under "Not checked" instead of guessing.

## 5. Write the report

Write `UX-AUDIT.md` at the root of the audited project or package (if it exists, read it first and replace it). Carry over earlier `wontfix` decisions with their reasons, matched by rule ID and file. Follow the audit layout in `references/report-format.md`:

- Score each area 0 to 4, or `n/a` when the scope has nothing it covers.
- Add the first-impression lines from the holistic pass and the systemic issues (patterns that repeat and are best fixed once).
- Group findings by area, P0 first, numbered `F-001`, `F-002`, … in report order.
- One finding per rule per pattern of violation, with the count of other places it occurs.
- Every finding has a real `path:line`, evidence, impact, a concrete fix in the project's own components and tokens, an effort size and `Status: open`.
- Include "What is already good" so the refactor keeps it, and "Not checked".

## 6. Reply

In the conversation, give a short summary: area scores, counts by severity, the top five fixes by impact with their IDs, any questions (for example whether a hard-coded claim is real), and the report path. Suggest `/uichecker:refactor P0` and then `/uichecker:refactor audit` as next steps. Do not paste the whole report.
