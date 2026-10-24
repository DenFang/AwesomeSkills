---
name: ux-guidelines
description: Use when building, changing or reviewing user-interface code (components, pages, CSS, Tailwind, React, Vue, Svelte, React Native, SwiftUI, Compose, Flutter), or when the user asks to make UI feel premium, less generic or more usable, or mentions designmotionhq. 116 rules with IDs (MOT, STA, FRM, DAT, INT, VIS, CON) covering motion timing, loading/empty/error states, forms, tables, navigation, overlays, accessibility, visual systems, honest persuasion and "doesn't look AI-made" polish, distilled from the @designmotionhq videos. Palette-independent: works with any brand colours.
---

# UX guidelines (designmotionhq)

Most @designmotionhq videos show one interface twice, a cheap version and a premium one, and name the few concrete decisions that separate them. This skill turns those videos into 116 rules you can apply while building and check while reviewing. Every rule has an ID (`MOT-3`, `FRM-10`, …), a severity, an **Applies to** line that says which elements it is about, and a concrete rule; most also have a detection hint and a fix.

The rules describe relationships, not a palette: "one accent, only on the primary action", "inner radius = outer − padding", "exits about 40% shorter than entrances". Always use the project's own colours, fonts and tokens. Never copy the colours shown in the videos.

## Core beliefs

1. **A component is a system, not a widget.** A table is alignment, density, sticky regions, empty cells and actions. A toast is position, timing, stacking and dismissal. Decide each part on purpose.
2. **Every state is designed.** Loading, empty, error, success, partial, disabled, focus, busy. The happy path alone is unfinished work.
3. **Numbers beat taste.** Durations, sizes, ratios and thresholds are written down once as tokens and reused.
4. **Feedback is immediate.** Something visible happens within 100 ms of every press and within 400 ms of every request.
5. **Decoration is a tell.** Generated-looking UI decorates because it has nothing concrete to show. Replace decoration with real content, real numbers and one clear focal point.
6. **Every input method reaches everything.** Keyboard, touch and pointer all reach every action; hover is never the only path.

## Step 1 · Read the context

Before writing or judging UI, establish four facts and keep them for the whole task:

1. **Design system**: tokens or CSS variables, Tailwind config, theme files, a `DESIGN.md`, the component library in use. Rules are applied through these, never around them.
2. **Product type**: a *tool* (app UI, admin, dashboard, editor: design serves the task) or *brand* (landing page, marketing, campaign: design is part of the product), or both in one codebase. Tools favour density, crisp motion and restraint (CON-7); brand pages favour hierarchy, story and lively motion (CON-2…5).
3. **Motion profile** (MOT-0): crisp or lively. If the project does not say, infer from the product type and state your assumption.
4. **Platform**: web (desktop, mobile web), or a native stack (see "Non-web stacks").

## Step 2 · Pick only the rules that apply

Rules are scoped. A rule is checked only where its subject exists: table rules on tables, toast rules on toasts, password rules on password fields. Never report a rule whose **Applies to** element is absent from the code you are looking at.

1. **Inventory** the code in scope: which elements and patterns it actually contains (a form, a table, a modal, a dropdown menu, a chart, navigation, animations, copy).
2. **Always-on rules** apply to any interactive UI: INT-1 (focus), INT-2 (real elements), INT-11 (targets), INT-12 (hover), VIS-1 (tokens), VIS-7 (contrast), VIS-8 (colour not alone), MOT-13 (reduced motion, when anything moves), CON-1 (copy, when there is text).
3. **Module rules** come from the routing table below, for each element in the inventory.
4. If an element sits on the border of two modules (a dropdown inside a table row), apply both modules' rules to that element only.

### Routing table

| Element in the code | Load | Rules |
|---|---|---|
| Fetches, submits or waits (any data component) | `states-feedback.md` | STA-1…10 |
| Form, sign-up, login, checkout | `forms.md`, `states-feedback.md` | FRM-1…11, FRM-18, STA-7, STA-10 |
| Password, OTP, masked input | `forms.md` | FRM-5, FRM-6, FRM-7 |
| Date picker, slider, toggle, inline edit, upload | `forms.md` | FRM-13…17 |
| Settings page | `forms.md`, `interaction.md` | FRM-12, FRM-13, INT-9 |
| Table, records list | `data-display.md` | DAT-1…9 |
| Search, filters, command palette | `data-display.md` | DAT-10…12 |
| Dashboard, charts, metric tiles | `data-display.md`, `content-persuasion.md` | DAT-1, DAT-13, DAT-14, CON-6 |
| Avatars, chat, ratings, calendar | `data-display.md` | DAT-15…18 |
| Modal, sheet, drawer, popover, tooltip, menu, dropdown | `interaction.md`, `motion.md` | INT-3…8, MOT-1, MOT-2, MOT-10 |
| Navigation, tabs, app shell | `interaction.md` | INT-16, INT-17 |
| Buttons, cards, any clickable element | `interaction.md`, `motion.md` | INT-10, MOT-3, MOT-9 |
| Destructive or bulk actions | `interaction.md`, `states-feedback.md`, `data-display.md` | INT-9, STA-14, DAT-4, DAT-5 |
| Drag and drop, swipe, pull to refresh | `interaction.md`, `motion.md` | INT-13…15, MOT-14 |
| Accordion, resizable panel, colour picker, custom widget | `interaction.md`, `motion.md` | INT-18…22, MOT-7, MOT-8 |
| Toasts, banners, badges, copy buttons, offline support | `states-feedback.md` | STA-11…16 |
| Any animation or transition | `motion.md` | MOT-0…14 |
| Styles, theming, dark mode, tokens, typography, icons, layering | `visual-system.md` | VIS-1…18 |
| Landing page, hero, pricing, onboarding | `content-persuasion.md`, `visual-system.md` | CON-2…5, CON-8, CON-9, VIS-12 |
| Interface copy (labels, errors, CTAs) | `content-persuasion.md` | CON-1, FRM-18 |
| "It looks AI-made" | `content-persuasion.md`, `visual-system.md` | CON-3, CON-6, CON-7, VIS-5, VIS-12 |
| Pricing, checkout, sign-up, cancellation, consent, feeds | `content-persuasion.md` | CON-8, CON-9 |
| Collaboration, presence | `interaction.md` | INT-20 |

All files are in `references/`. `sources.md` maps every video to the file that holds its rules. Load only the files the inventory needs.

## The numbers worth memorising

| What | Value |
|---|---|
| Press, hover, toggle feedback | under 100 ms |
| Entrance (modal, sheet, panel) | lively: 200 to 300 ms, ease-out; crisp: 150 ms max; dropdowns about 150 ms |
| Exit | about 40% shorter than the entrance (250 in, 150 out) |
| Crisp profile ceiling | hover about 80 ms, transitions under 150 ms, no overshoot |
| Attention motion (alerts only) | 500 to 800 ms, bounce allowed |
| List stagger | about 50 ms per item, cap the first 6 to 8 |
| No loader | for responses under about 300 ms |
| Must visibly react | within about 400 ms |
| Spinner vs progress bar | spinner under about 3 s, progress bar with % above |
| Tooltip delay | about 300 ms on hover, immediate on focus |
| Toast duration | about 4 s info, 7 s warning, errors until dismissed; max 3 visible |
| Undo window | 5 to 10 s with a visible countdown |
| Autosave debounce | about 800 ms after typing stops |
| Touch target | at least 44 × 44 px on touch, never below 24 × 24 px |
| Text contrast | 4.5:1 body, 3:1 large text and UI parts |
| Focus ring | 2 px, 2 px offset, 3:1 contrast, `:focus-visible` |
| Nested radius | inner = outer − padding |
| Colour roles | about 60% dominant neutral, 30% secondary surface, 10% one accent |
| Type | about 5 sizes on one ratio, 2 to 3 weights, measure 45 to 75 characters |
| Table rows | about 40 / 48 / 56 px density token |

## When you build UI

1. Apply the rules for each element as you write the code, through the project's tokens.
2. Before calling the work done, check every state the component can be in (STA-1) and every input method (INT-1, INT-2, INT-11, INT-12).
3. Check reduced motion (MOT-13) and contrast (VIS-7, VIS-8) for anything new.
4. In your reply, name the rule IDs you applied only when you created a new screen or component; for small edits apply the rules silently.

## Proportionality

- **Small change** to existing UI (a label, a colour, one prop): follow the rules quietly and match what the project already does. No lectures, no unrequested refactors.
- **New screen or component**: apply the rules fully and mention the main decisions in one or two lines.
- **Audit, review or refactor**: use the commands below.

## When rules seem to conflict

- Motion: the crisp profile caps every duration at 150 ms and turns springs off; the lively profile uses the 200 to 300 ms entrances and small springs (MOT-0).
- Shadows: floating layers get shadows; page panels and rows use surface steps and hairlines (VIS-11). Dark mode uses lightness for elevation (VIS-9).
- Zebra stripes: only for very wide tables; otherwise a hairline and hover tint (DAT-2).
- Validation: on blur by default, live after the first error, live checklists for rule-based fields like passwords (FRM-3, FRM-5).
- Disabled buttons: keep submit active and explain blockers; while a request runs the button is busy, not disabled (FRM-4, FRM-10).
- The project's established design system wins over a generic number here, unless it causes a P0 problem (accessibility, data loss, deception). Then say so.

## Non-web stacks

For React Native, SwiftUI, Jetpack Compose or Flutter, apply each rule's intent through the platform's equivalent and say in reports which CSS-specific checks were translated or skipped:

| Web | Native equivalent |
|---|---|
| Focus ring, `:focus-visible` | Accessibility focus and the platform focus engine (tvOS, keyboard on iPad and Android) |
| `aria-*`, roles | `accessibilityRole` / `accessibilityLabel` (RN), `.accessibilityLabel` and traits (SwiftUI), `semantics` (Compose, Flutter) |
| `prefers-reduced-motion` | `AccessibilityInfo.isReduceMotionEnabled` (RN), `accessibilityReduceMotion` (SwiftUI), animator scale settings (Android), `MediaQuery.disableAnimations` (Flutter) |
| 44 px target | 44 pt (iOS), 48 dp (Android) |
| `:hover` | Pointer and hover APIs where a pointer exists; otherwise the rule's touch fallback |
| CSS tokens | The theme object, asset catalogue colours, `MaterialTheme`, `ThemeData` |

## Missing design system

If the project has no tokens and the task is more than a small edit, propose a minimal token set (colour roles, spacing scale, type scale, radius scale, shadow levels, durations and easings) using the project's existing colours and fonts, and ask before introducing it across the codebase.

## Override rule

The user owns their product. If they insist on something a rule advises against, state the risk in one line and build it, unless it is a dark pattern or deceptive claim (CON-8, CON-9), which you do not build.

## Commands

This plugin also gives the user three commands that use these guidelines:

- `/ux-audit [path]` checks the whole codebase (or a path) and writes a prioritised report to `UX-AUDIT.md`.
- `/ux-review [base ref | range | branch | PR number]` checks only the changes on the current branch or in the working tree.
- `/ux-refactor [audit | P0 | F-001 … | R-001 … | path]` fixes problems directly, from the audit report, or from the last review.

Full names: `/designmotionhq-ux:ux-audit`, `/designmotionhq-ux:ux-review`, `/designmotionhq-ux:ux-refactor`. The shared report format is in `references/report-format.md`, and search patterns for finding violations quickly are in `references/detection.md`.
