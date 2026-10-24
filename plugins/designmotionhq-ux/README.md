# designmotionhq-ux

UI/UX pattern guidelines for Claude Code, distilled from the UI/UX videos of [@designmotionhq](https://www.instagram.com/designmotionhq/): motion timing, loading, empty and error states, forms, tables, navigation, overlays, accessibility, visual systems, honest persuasion, and how to stop UI from looking AI-generated.

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
| `ux-guidelines` skill | Automatically, whenever Claude builds or changes UI | 116 rules with IDs (`MOT-3`, `FRM-10`, …). Each has a severity, an **Applies to** line so it is only checked where its element exists, and a concrete rule; most have a detection hint and a fix |
| `/ux-audit [path]` | You run it | Checks the whole codebase (or a path) in two passes (designer's read, then rule by rule), scores each area 0 to 4 and writes a prioritised `UX-AUDIT.md`; changes no code |
| `/ux-review [ref \| range \| branch \| PR]` | You run it | Checks only the changes on your branch, in the working tree, or in a range or PR, and gives a verdict |
| `/ux-refactor [audit \| P0 \| F-001 … \| R-001 … \| path]` | You run it | Fixes problems from the audit, from the last review, or on a path; runs your checks and records what was fixed |

Full names are `/designmotionhq-ux:ux-audit`, `/designmotionhq-ux:ux-review` and `/designmotionhq-ux:ux-refactor`; the short forms work as long as no other plugin uses the same names. The commands carry a `ux-` prefix because Claude Code has a built-in `/review`.

Only rules whose element exists in the code are checked: a dropdown menu is checked against menu, overlay and motion rules plus the always-on accessibility rules, never against table or form rules. Add a `.ux-ignore.md` to the project to silence rules you have decided against (format in `references/report-format.md`).

## Typical flow

1. `/ux-audit` → read `UX-AUDIT.md`.
2. `/ux-refactor P0` → fix the blocking issues first, then `/ux-refactor audit` for the rest.
3. Before each merge, `/ux-review` on the branch, then `/ux-refactor R-001 …` for anything it finds.

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
