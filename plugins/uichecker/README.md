# uichecker

**137 UI/UX rules a senior product designer would hold your code to, checked only where they apply.**

Distilled from more than 140 short UI/UX lessons: motion timing, loading, empty and error states, forms, tables, navigation, overlays, accessibility, visual systems, honest persuasion, and how to stop UI from looking AI-generated.

- **No noise.** Every rule names the element it applies to, so a dropdown is never checked against table rules.
- **Any brand, any stack.** The rules describe relationships, not a palette.
- **Works while Claude builds**, and on demand through three commands: audit, review and refactor.

## Install

```text
/plugin marketplace add DenFang/AwesomeSkills
/plugin install uichecker@awesome-skills
```

From a terminal:

```bash
claude plugin marketplace add DenFang/AwesomeSkills
claude plugin install uichecker@awesome-skills
```

Update later with `claude plugin update uichecker@awesome-skills`.

## What you get

| Part | How it runs | What it does |
|---|---|---|
| `guidelines` skill | Automatically, whenever Claude builds or changes UI | 137 rules with IDs (`MOT-3`, `FRM-10`, …). Each has a severity, an **Applies to** line so it is only checked where its element exists, and a concrete rule; most have a detection hint and a fix |
| `/uichecker:audit [path]` | You run it | Checks the whole codebase (or a path) in two passes (designer's read, then rule by rule), scores each area 0 to 4 and writes a prioritised `UX-AUDIT.md`; changes no code |
| `/uichecker:review [ref \| range \| branch \| PR]` | You run it | Checks only the changes on your branch, in the working tree, or in a range or PR, and gives a verdict |
| `/uichecker:refactor [audit \| P0 \| F-001 … \| R-001 … \| path]` | You run it | Fixes problems from the audit, from the last review, or on a path; runs your checks and records what was fixed |

Commands are namespaced by the plugin. Bare `/audit` and `/refactor` also work while no other command uses those names; `/review` is a built-in Claude Code command, so type `/uichecker:review`.

Only rules whose element exists in the code are checked: a dropdown menu is checked against menu, overlay and motion rules plus the always-on accessibility rules, never against table or form rules. Add a `.ux-ignore.md` to the project to silence rules you have decided against (format in `references/report-format.md`).

## Typical flow

1. `/uichecker:audit` → read `UX-AUDIT.md`.
2. `/uichecker:refactor P0` → fix the blocking issues first, then `/uichecker:refactor audit` for the rest.
3. Before each merge, `/uichecker:review` on the branch, then `/uichecker:refactor R-001 …` for anything it finds.

## Rule areas

| File | Prefix | Covers |
|---|---|---|
| `motion.md` | MOT | Motion profile, durations, easing, stagger, hover, modals, scroll timelines, success moments, shared-element transitions, reduced motion |
| `states-feedback.md` | STA | Loading patterns, skeletons, optimistic UI, empty, error, partial, success, toasts, notifications, badges, undo, copy, offline, progress bars, typing indicators |
| `forms.md` | FRM | Field states, labels, validation timing, submit, passwords, masks, OTP, steppers, autosave, settings, toggles, dates, sliders, upload, inline edit, selection controls, chat and AI composers, payment forms |
| `data-display.md` | DAT | Numbers, tables, sorting, selection, bulk actions, responsive tables, pagination, scroll restoration, truncation, filters, search, command palette, charts, dashboards and KPI rows, avatars, chat, ratings, calendars, admin screens |
| `interaction.md` | INT | Focus, keyboard, overlay choice, dialogs, sheets, dropdowns, tooltips, menus, destructive actions, buttons, targets, hover, drag and drop, swipe, navigation, breadcrumbs, tabs, accordions, panels, presence, permission prompts, tree views, boards, voice recording, phone layouts |
| `visual-system.md` | VIS | Tokens, spacing, type, colour roles, contrast, dark mode, radius, elevation, hierarchy, grid, icons, optical corrections, gradients, glass, z-index, cards, modern CSS layout |
| `content-persuasion.md` | CON | Microcopy, landing structure, generated-look tells, flow psychology, honest persuasion, pricing sections, success screens, shortcuts, engagement mechanics, dark patterns to refuse |

Every lesson behind the rules is written up in [`research/ui-lessons/`](../../research/ui-lessons/INDEX.md).

## What it runs and writes

- Reads your project's UI files and runs read-only searches (`rg`/grep) and `git` (to collect a diff for review).
- `audit` writes only `UX-AUDIT.md`; `review` writes nothing; `refactor` edits the files of the findings it fixes and runs your project's own checks (lint, tests, build).
- Sends nothing anywhere and downloads nothing; no hooks, no MCP servers, no scripts.

## License

Licensed under [Apache-2.0](LICENSE). If you redistribute uichecker or build on it, keep the [NOTICE](NOTICE) file and credit the original: *Based on uichecker by DenFang (https://github.com/DenFang/AwesomeSkills)*.
