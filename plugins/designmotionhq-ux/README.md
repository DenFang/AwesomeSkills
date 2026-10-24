# designmotionhq-ux

UI/UX pattern guidelines for Claude Code, distilled from every video on [@designmotionhq](https://www.instagram.com/designmotionhq/): motion timing, loading, empty and error states, forms, tables, navigation, overlays, accessibility, visual systems, honest persuasion, and how to stop UI from looking AI-generated.

The rules describe relationships, not a palette, so they work with any brand colours and any stack.

## Install

```text
/plugin marketplace add DenFang/AwesomeSkills
/plugin install designmotionhq-ux@awesome-skills
```

Or in one step (Claude Code 2.1.275+): `/plugin install designmotionhq-ux --marketplace DenFang/AwesomeSkills`.

## What you get

| Part | How it runs | What it does |
|---|---|---|
| `ux-guidelines` skill | Automatically, whenever Claude builds or changes UI | Applies about 120 rules with IDs (`MOT-3`, `FRM-10`, …), each with a severity, a way to detect it and a fix |
| `/designmotionhq-ux:audit [path]` | You run it | Checks the whole codebase (or a path), writes a prioritised `UX-AUDIT.md`, changes no code |
| `/designmotionhq-ux:review [ref]` | You run it | Checks only the changes on your branch or in the working tree and gives a verdict |
| `/designmotionhq-ux:refactor [audit \| F-001 … \| P0 \| path]` | You run it | Fixes problems from the audit or on a path, runs your checks, records what was fixed |

If no other plugin uses the same names, the short forms `/audit`, `/review` and `/refactor` work too.

## Typical flow

1. `/designmotionhq-ux:audit` → read `UX-AUDIT.md`.
2. `/designmotionhq-ux:refactor P0` → fix the blocking issues first, then `refactor audit` for the rest.
3. Before each merge, `/designmotionhq-ux:review` on the branch.

## Rule areas

| File | Prefix | Covers |
|---|---|---|
| `motion.md` | MOT | Motion profile, durations, easing, stagger, hover, modals, scroll timelines, reduced motion |
| `states-feedback.md` | STA | Loading patterns, skeletons, optimistic UI, empty, error, partial, success, toasts, notifications, badges, undo, copy, offline |
| `forms.md` | FRM | Field states, labels, validation timing, submit, passwords, masks, OTP, steppers, autosave, settings, toggles, dates, sliders, upload, inline edit |
| `data-display.md` | DAT | Numbers, tables, sorting, selection, bulk actions, responsive tables, pagination, scroll restoration, truncation, filters, search, command palette, charts, dashboards, avatars, chat, ratings, calendars |
| `interaction.md` | INT | Focus, keyboard, overlay choice, dialogs, sheets, dropdowns, tooltips, menus, destructive actions, buttons, targets, hover, drag and drop, swipe, navigation, tabs, accordions, panels, presence |
| `visual-system.md` | VIS | Tokens, spacing, type, colour roles, contrast, dark mode, radius, elevation, hierarchy, grid, icons, optical corrections, gradients, z-index |
| `content-persuasion.md` | CON | Microcopy, landing structure, generated-look tells, flow psychology, honest persuasion, dark patterns to refuse |

`sources.md` maps every video to the rules it produced.

## Credits

All ideas come from the free videos and breakdowns by [designmotionhq](https://www.designmotionhq.com/patterns). The wording, structure and commands are original; no videos, frames or paid content (UX Engine) are included. If you like the rules, follow the account.

License: MIT.
