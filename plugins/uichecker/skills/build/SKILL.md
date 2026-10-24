---
name: build
description: Build a new screen, flow or component with the uichecker guidelines applied from the start - every state, input method, motion and contrast rule for the elements it contains - then self-check it and run the project's checks.
argument-hint: "<what to build, and where>"
disable-model-invocation: true
---

# uichecker build

Build new UI so it already follows the rules, instead of fixing it afterwards.

Everything runs in this session: do not spawn subagents unless the user asks for it in the request.

Target: `$ARGUMENTS`: what to build and, if known, where it goes. Empty: ask what to build and stop.

## 1. Load the guidelines

Read `${CLAUDE_PLUGIN_ROOT}/skills/guidelines/SKILL.md`. Establish its Step 1 context (design system, product type, motion profile, platform) from real files.

## 2. Settle what you cannot infer

Ask the user, in one round, only what the code and the request do not answer and would change the build: where the UI lives (route, parent component), what data it shows and where that data comes from, and the product type if it is unclear. Use the structured question tool when available, with your best guess as the first option. Skip this step when the request and the code already settle these.

## 3. Plan

1. List the elements the new UI will contain (a form, a table, a dialog, navigation, a chart, animations, copy).
2. Load the rules for those elements from the routing table, plus the always-on rules and their files (guidelines Step 2).
3. Decide up front, in a short plan you show the user before writing code:
   - the states each data component needs (loading, empty, error, partial, success, disabled, busy) and what each one shows (STA-1);
   - the existing components and tokens you will use, and any new token you need (VIS-1; no raw colours or off-scale spacing);
   - durations and easing from the motion profile (MOT-0);
   - the copy for labels, errors, empty states and buttons (CON-1, FRM-18).
4. If the project has no design system and the build is more than one small component, follow guidelines "Missing design system": propose a minimal token set and ask before introducing it.

## 4. Build

Write the code with the project's own components, tokens and patterns, applying each loaded rule as you go. Match the existing file structure and naming. Never build a dark pattern or a deceptive claim (CON-8, CON-9), even if asked; say why and offer the honest version.

## 5. Self-check

Before calling it done, check the new code against the loaded rules:

- every state from the plan exists and is reachable (STA-1);
- keyboard, touch and pointer reach every action; real elements; visible focus (INT-1, INT-2, INT-11, INT-12);
- contrast and colour-not-alone (VIS-7, VIS-8);
- reduced motion for anything that moves (MOT-13);
- the module rules of each element, P0 rules first.

Fix what fails. Then run the project's own checks that apply to the new files (type-check, lint, tests, build); fix failures caused by your code.

## 6. Reply

Keep it short:

- what you built and where (files);
- the main decisions with their rule IDs, one line each;
- anything left open (a question, a token you proposed, a check you could not run).

Then suggest `/uichecker:review` before merging.
