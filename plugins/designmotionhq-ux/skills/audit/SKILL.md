---
name: audit
description: Audit the whole UI codebase (or a given path) against the designmotionhq UX guidelines and write a prioritised report to UX-AUDIT.md. Read-only; it changes no code.
argument-hint: "[path or glob, default: whole project]"
disable-model-invocation: true
---

# UX audit

Audit the project's interface code against the guidelines in `${CLAUDE_PLUGIN_ROOT}/skills/ux-guidelines/`. Do not modify any source file. The only file you write is the report.

Scope: `$ARGUMENTS` (if empty, the whole project).

## 1. Load the guidelines

Read `${CLAUDE_PLUGIN_ROOT}/skills/ux-guidelines/SKILL.md`, then `references/report-format.md` and `references/detection.md` from the same folder. Load the topic references (`motion.md`, `states-feedback.md`, `forms.md`, `data-display.md`, `interaction.md`, `visual-system.md`, `content-persuasion.md`) as you reach each area in step 4.

## 2. Map the project

1. Identify the stack: framework, styling approach (CSS, CSS modules, Tailwind, CSS-in-JS), component library, animation library, routing.
2. Find the design system: token files, CSS variables, Tailwind theme, `DESIGN.md`, a shared components folder. Note where tokens live, or that there are none.
3. Decide the motion profile (MOT-0) from the product type and existing code, and write down why.
4. List the UI surface: pages or routes, shared components, and which modules each contains (forms, tables, modals, navigation, dashboards…). Skip `node_modules`, build output, vendored code, generated files, stories and test snapshots unless asked.
5. If the scope has more than about 150 UI files, audit shared components and the most-used screens first, sample the rest, and say so under "Not checked".

## 3. Run the fast sweep

Run the searches in `references/detection.md` across the scope. Treat every match as a lead and open the code to confirm. Count how often each pattern appears, because repeated issues become one finding with a total.

## 4. Check each area properly

Go module by module using the routing table in the guidelines. For each component or screen, read the code and check the rules that apply. Pay particular attention to:

- **States** (STA-1): for every fetch or submit, are loading, empty, error and success handled? Partial and offline only where they really apply.
- **Input methods**: focus visible (INT-1), real buttons and keyboard (INT-2), dialogs manage focus (INT-4), touch targets (INT-11), nothing hover-only (INT-12).
- **Forms**: labels, validation timing, submit behaviour, double submit (FRM-1…10).
- **Motion**: durations and curves from tokens, enter vs exit, reduced motion (MOT-0…13).
- **Visual system**: raw values vs tokens, contrast, colour-only meaning, dark mode, radius and elevation (VIS-1…18).
- **Content**: button labels, error copy, generated-looking hero or dashboard, persuasion claims, dark patterns (CON-1…9).

Static code cannot prove everything (for example contrast over images or the real feel of an animation). If the app can be run and a browser tool is available, you may check a few key screens; otherwise list such items under "Not checked" instead of guessing.

## 5. Write the report

Write `UX-AUDIT.md` at the project root (if it exists, read it first and replace it; keep any `wontfix` decisions it records). Follow the audit layout in `references/report-format.md`:

- Group findings by area, P0 first, and number them `F-001`, `F-002`, … in report order.
- One finding per rule per pattern of violation, with the count of other places it occurs.
- Every finding has a real `path:line`, evidence, a concrete fix in the project's own components and tokens, an effort size and `Status: open`.
- Include "What is already good" so the refactor keeps it, and "Not checked".

## 6. Reply

In the conversation, give a short summary: counts by severity, the top five fixes by impact with their IDs, and the report path. Suggest `/designmotionhq-ux:refactor audit` (or specific IDs such as `F-001 F-003`) as the next step. Do not paste the whole report.
