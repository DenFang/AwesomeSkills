---
name: build
description: Build a new screen, flow or component by impeccable, ui-ux-pro-max and uichecker at once - their guidance for each element merged into one checklist, their disagreements put to the user as choices (asked before building, during building, or taken as recommended) - then self-check and run the project's checks.
argument-hint: "<what to build, and where> [--ask-first | --ask-along | --auto]"
disable-model-invocation: true
---

# UltimateDesign build

Build new UI by three design skills at once: what they agree on is applied, where they disagree the user chooses.

Everything runs in this session: do not spawn subagents, and do not let a member skill spawn them, unless the user asks for it in the request.

Target: `$ARGUMENTS`: what to build and, if known, where it goes, plus optionally one question mode:

| Flag | Questions |
|---|---|
| `--ask-first` | every decision is asked before any code is written |
| `--ask-along` | building starts at once; each decision is asked when the build reaches the part it affects, and only that part waits |
| `--auto` | no decision questions; the recommended option is taken for each and listed at the end |
| none | ask the user which of the three, in the first question round (step 4) |

Empty target: ask what to build and stop.

## 1. Load the method

Read `${CLAUDE_PLUGIN_ROOT}/shared/passes.md` (sections 1 and 2; its read-only rules are for review passes and do not apply here), `${CLAUDE_PLUGIN_ROOT}/shared/modes.md` (section 4) and `${CLAUDE_PLUGIN_ROOT}/shared/merge.md` (step 4).

## 2. Find the members

Resolve uichecker, impeccable and ui-ux-pro-max (passes.md section 1). One line to the user on which copies are used. With uichecker alone, say so and build as `/uichecker:build` does.

## 3. Context

1. Read the project: stack, design system, existing components and patterns, product type (passes.md section 2). Decide the visual authority as impeccable's `reference/new-work.md` section 1 does: established world (inherit it), incomplete brand (extend it), or none. A screen or component inside an established surface always inherits it.
2. List the elements the new UI will contain (forms, tables, dialogs, navigation, charts, animations, copy, landing sections).

## 4. First question round

Ask once, with the structured question tool when available (best guess first, at most four questions):

- the facts that change the work and cannot be read from the code or the request: where the UI lives, what data it shows, the task or the action it must drive (impeccable's new-work section 2 lists the right questions per surface type);
- without a question-mode flag: how to handle the design decisions: ask all first, ask along the way, or take the recommendations.

Skip what is already settled; never more than one round here.

## 5. Merge the guidance

For each element, collect each available skill's guidance and merge it as modes.md section 4.2 and 4.3 describe: same check and verdict → keep the most detailed rule and note who shares it; different meaning or verdict → a decision `D-1`, `D-2`, … with options per skill, gains, costs and a recommendation by merge.md step 4 precedence; one skill only → keep it. Add each skill's build guidance where it fits:

- uichecker: guidelines "When you build UI" and the states, tokens and motion decisions of `/uichecker:build` step 3;
- impeccable: `SKILL.md` "How to design" and the mode reference for the surface (`reference/mode-operate.md`, `mode-persuade.md`, `mode-read.md`);
- ui-ux-pro-max: `search.py "<element>" --stack <stack>` for stack guidance; when the project has no design system, `search.py "<product> <keywords>" --design-system` (without `--persist`) may supply a proposal, offered as one option of a decision.

The result is the build checklist: the kept rules per element, the decisions, and a short plan (states, tokens, motion, copy).

## 6. Decide

- `--ask-first`: show the plan, then ask the decisions (up to four per question call, recommended option first, each option naming its skill and its cost); build only after all are answered.
- `--ask-along`: show the plan and the list of open decisions, then start building everything the decisions do not affect (structure, data flow, states, shared tokens). Ask each decision when the build reaches the element it affects, and build that element with the answer.
- `--auto`: take the recommended option of every decision.

A decision the user leaves unanswered takes the recommendation; say so.

## 7. Build

Write the code with the project's own components, tokens and patterns, applying the build checklist and the chosen options. Rules that hold throughout:

- Do not create or overwrite `PRODUCT.md` or `DESIGN.md`, and do not run impeccable `init`, `document` or `live-server`, unless the user agrees in a question.
- Never run ui-ux-pro-max `--persist`, and never `--design-system` in a project that already has a design system. When there is none and the user chose the generated proposal, write its tokens into the project's own token file, not into a separate design-system folder, unless the user asks for that.
- Never build a dark pattern or a deceptive claim, whichever skill suggests it (uichecker CON-8, CON-9).

## 8. Self-check

Check the new code against the build checklist as modes.md section 4.4 does (the new files only): every state exists, every input method reaches every action, contrast, reduced motion, then each element's kept rules, P0 first. Fix what fails. Run the project's own checks that apply to the new files (type-check, lint, tests, build) and fix failures caused by your code.

## 9. Reply

Keep it short:

- what you built and where (files);
- the key choices, each with the skill and rule that drove it (`uichecker STA-7`, `impeccable Operate mode`, `ui-ux-pro-max Accessibility · touch targets`);
- the decisions: `D-1 → A (you chose)`, `D-2 → B (recommended)`, with the other options still available;
- anything left open.

Offer `/ultimatedesign:review --lite` on the result, and to switch any decision to another option.
