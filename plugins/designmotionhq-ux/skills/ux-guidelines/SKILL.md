---
name: ux-guidelines
description: UI/UX pattern guidelines distilled from every @designmotionhq video, covering motion timing, loading/empty/error states, forms, tables, navigation, overlays, accessibility, visual systems and "doesn't look AI-made" polish. Use it whenever you build, change or judge user interface code (web or app components, pages, CSS, Tailwind, React, Vue, Svelte, SwiftUI-like layouts), and when the user asks to make UI feel premium, less generic, more usable, or names designmotionhq. Palette-independent, so it works with any brand colours.
---

# UX guidelines (designmotionhq)

Each @designmotionhq video shows one interface twice, a cheap version and a premium one, and names the few concrete decisions that separate them. This skill turns those videos into rules you can apply while building and check while reviewing. Every rule has an ID (`MOT-3`, `FRM-10`, …), a severity, a way to detect it in code, and a fix.

The rules describe relationships, not a palette: "one accent, only on the primary action", "inner radius = outer − padding", "exits 40% faster than entrances". Always use the project's own colours, fonts and tokens. Never copy the colours shown in the videos.

## Core beliefs

1. **A component is a system, not a widget.** A table is alignment, density, sticky regions, empty cells and actions. A toast is position, timing, stacking and dismissal. Decide each part on purpose.
2. **Every state is designed.** Loading, empty, error, success, partial, disabled, focus, busy. The happy path alone is unfinished work.
3. **Numbers beat taste.** Durations, sizes, ratios and thresholds are written down once as tokens and reused.
4. **Feedback is immediate.** Something visible happens within 100 ms of every press and within 400 ms of every request.
5. **Decoration is a tell.** Generated-looking UI decorates because it has nothing concrete to show. Replace decoration with real content, real numbers and one clear focal point.
6. **Every input method reaches everything.** Keyboard, touch and pointer all reach every action; hover is never the only path.

## Before you write or judge UI

1. **Read the project's design system first**: tokens or CSS variables, Tailwind config, theme files, a `DESIGN.md`, the component library in use. Rules are applied through these, never around them.
2. **Note the motion profile** (MOT-0): crisp (tools, dashboards, editors) or lively (consumer, marketing). If the project does not say, infer from the product and state your assumption.
3. **Name the module** you are touching and load only the reference sections it needs (routing table below). Do not load every file for a one-component change.

## Routing table

| Module | Load | Key rules |
|---|---|---|
| Any data component (list, table, dashboard, feed) | `states-feedback.md`, `data-display.md` | STA-1…9, DAT-1…4 |
| Form, sign-up, login, checkout | `forms.md`, `states-feedback.md` | FRM-1…10, STA-7, STA-10 |
| Settings page | `forms.md`, `interaction.md` | FRM-12, FRM-13, INT-9 |
| Table, records list | `data-display.md` | DAT-1…9 |
| Search, filters, command palette | `data-display.md` | DAT-10…12 |
| Dashboard, charts | `data-display.md`, `content-persuasion.md` | DAT-13, DAT-14, CON-6 |
| Modal, sheet, drawer, popover, tooltip, menu | `interaction.md`, `motion.md` | INT-3…8, MOT-10 |
| Navigation, tabs, app shell | `interaction.md` | INT-16, INT-17, INT-1 |
| Buttons, cards, any clickable element | `interaction.md`, `motion.md` | INT-10…12, MOT-3, MOT-9 |
| Destructive actions, bulk actions | `interaction.md`, `states-feedback.md`, `data-display.md` | INT-9, STA-14, DAT-5 |
| Upload, drag and drop, gestures | `forms.md`, `interaction.md` | FRM-16, INT-13…15 |
| Notifications, toasts, badges | `states-feedback.md` | STA-11…13 |
| Animation pass | `motion.md` | MOT-0…14 |
| Visual polish, theming, dark mode, design tokens | `visual-system.md` | VIS-1…18 |
| Landing page, pricing, onboarding | `content-persuasion.md`, `visual-system.md` | CON-2…5, CON-8, VIS-12 |
| "It looks AI-made" | `content-persuasion.md`, `visual-system.md` | CON-3, CON-6, CON-7, VIS-5, VIS-12 |
| Chat, comments, collaboration | `data-display.md`, `interaction.md` | DAT-16, INT-20 |

All files are in `references/`. `sources.md` maps every video to the file that holds its rules.

## The numbers worth memorising

| What | Value |
|---|---|
| Press, hover, toggle feedback | under 100 ms |
| Entrance (modal, sheet, panel) | 200 to 300 ms, ease-out; dropdowns about 150 ms |
| Exit | about 40% faster than the entrance (250 in, 150 out) |
| Crisp profile ceiling | hover about 80 ms, transitions under 150 ms, no overshoot |
| Attention motion (alerts only) | 500 to 800 ms, bounce allowed |
| List stagger | about 50 ms per item, cap the first 6 to 8 |
| Show no loader | responses under about 300 ms |
| Must visibly react | within about 400 ms |
| Spinner vs progress bar | spinner under about 3 s, progress bar with % above |
| Tooltip delay | about 300 ms on hover, immediate on focus |
| Toast duration | about 4 s info, 7 s warning, errors until dismissed; max 3 visible |
| Undo window | 5 to 10 s with a visible countdown |
| Autosave debounce | about 800 ms after typing stops |
| Touch target | at least 44 × 44 px |
| Text contrast | 4.5:1 body, 3:1 large text and UI parts |
| Focus ring | 2 px, 2 px offset, 3:1 contrast, `:focus-visible` |
| Nested radius | inner = outer − padding |
| Colour roles | about 60% dominant neutral, 30% secondary surface, 10% one accent |
| Type | about 5 sizes on one ratio, 2 to 3 weights, measure 45 to 75 characters |
| Table rows | about 40 / 48 / 56 px density token |

## When you build UI

1. Apply the rules for the module as you write the code, through the project's tokens.
2. Before calling the work done, check every state the component can be in (STA-1) and every input method (INT-1, INT-2, INT-11, INT-12).
3. Check reduced motion (MOT-13) and contrast (VIS-7, VIS-8) for anything new.
4. In your reply, name the rule IDs you applied only when you created a new screen or component; for small edits apply the rules silently.

## Proportionality

- **Small change** to existing UI (a label, a colour, one prop): follow the rules quietly and match what the project already does. No lectures, no unrequested refactors.
- **New screen or component**: apply the rules fully and mention the main decisions in one or two lines.
- **Audit, review or refactor**: use the commands below.

## When rules seem to conflict

- Motion: crisp products drop springs and keep transitions under 150 ms; lively products may use small springs. Pick one profile (MOT-0).
- Shadows: floating layers get shadows; page panels and rows use surface steps and hairlines (VIS-11). Dark mode uses lightness for elevation (VIS-9).
- Zebra stripes: only for very wide tables; otherwise a hairline and hover tint (DAT-2).
- Validation: on blur by default, live after the first error, live checklists for rule-based fields like passwords (FRM-3, FRM-5).
- Disabled buttons: keep submit active and explain blockers; while a request runs the button is busy, not disabled (FRM-4, FRM-10).
- The project's established design system wins over a generic number here, unless it causes a P0 problem (accessibility, data loss, deception). Then say so.

## Missing design system

If the project has no tokens and the task is more than a small edit, propose a minimal token set (colour roles, spacing scale, type scale, radius scale, shadow levels, durations and easings) using the project's existing colours and fonts, and ask before introducing it across the codebase.

## Override rule

The user owns their product. If they insist on something a rule advises against, state the risk in one line and build it, unless it is a dark pattern or deceptive claim (CON-8, CON-9), which you do not build.

## Commands

This plugin also gives the user three commands that use these guidelines:

- `/designmotionhq-ux:audit [path]` checks the whole codebase (or a path) and writes a prioritised report to `UX-AUDIT.md`.
- `/designmotionhq-ux:review [git ref]` checks only the changes on the current branch or in the working tree.
- `/designmotionhq-ux:refactor [path | finding IDs | audit]` fixes problems directly, or works through the audit report.

The shared report format is in `references/report-format.md`, and search patterns for finding violations quickly are in `references/detection.md`.
