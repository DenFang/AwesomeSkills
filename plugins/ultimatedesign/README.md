# UltimateDesign

One pass of three design skills over the same UI, merged into one scored report:

- **[uichecker](../uichecker/README.md)**: 137 scoped UI/UX rules (states, forms, tables, navigation, motion, visual system, honest persuasion), checked only where their element exists.
- **[impeccable](https://github.com/pbakaus/impeccable)** by Paul Bakaus: design fluency, anti-AI-slop guidance, technical audit (accessibility, performance, theming, responsive, anti-patterns) and heuristic critique.
- **[ui-ux-pro-max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)** by Next Level Builder: a searchable design database (styles, palettes, font pairings, UX guidelines, stacks) and a priority-ranked checklist.

Each skill reviews the code on its own, in a separate subagent, so none of them anchors on another. UltimateDesign then:

1. normalises their severities to one P0 to P3 scale and verifies every blocking finding against the code;
2. groups the same problem reported by several skills into one finding with an agreement mark (3/3, 2/3, 1/3);
3. turns contradictions between skills into decisions (`D-1 · A or B`), each with the trade-off and a recommendation, so you pick the approach you like;
4. keeps what only one skill caught in its own section, so the gaps of one skill are covered by the others, and shows a coverage matrix by area;
5. scores each area 0 to 4 and the whole UI out of 100, next to each skill's own score.

## Install

```text
/plugin marketplace add DenFang/AwesomeSkills
/plugin install ultimatedesign@awesome-skills
```

From a terminal:

```bash
claude plugin marketplace add DenFang/AwesomeSkills
claude plugin install ultimatedesign@awesome-skills
```

`uichecker` is installed with it as a dependency. impeccable and ui-ux-pro-max come from their authors; any copy works (a plugin, a personal skill in `~/.claude/skills`, a project skill, or one your organisation provides):

```bash
claude plugin marketplace add pbakaus/impeccable && claude plugin install impeccable@impeccable
claude plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill && claude plugin install ui-ux-pro-max@ui-ux-pro-max-skill
```

If one of them is missing, UltimateDesign runs with the other two and says what it could not check.

## Commands

| Command | What it does |
|---|---|
| `/ultimatedesign:audit [path] [--deep]` | Whole project (or a path). Writes `ULTIMATE-DESIGN.md`: score, agreed findings, single-skill findings, decisions, coverage. `--deep` adds impeccable's heuristic critique. Changes no code. |
| `/ultimatedesign:review [ref \| range \| branch \| PR]` | Only the changes on your branch, in the working tree, or in a range or PR. Verdict in the conversation. |
| `/ultimatedesign:apply [recommended \| P0 \| U-001 … \| D-1=A …]` | Applies the fixes and the options you chose, runs your checks, updates the report. |

Use the full names: uichecker has commands with the same short names (`/uichecker:audit`, …), and `/review` is built into Claude Code.

## Typical flow

1. `/ultimatedesign:audit` → read the score and the decisions in `ULTIMATE-DESIGN.md`.
2. `/ultimatedesign:apply P0 D-1=A D-2=B` → blocking issues plus your choices; or `/ultimatedesign:apply recommended`.
3. Before each merge: `/ultimatedesign:review`, then `/ultimatedesign:apply U-…` for what it finds.

## What it runs and writes

- Reads your project's UI files and the member skills' own files; runs `git` (to collect a diff), `find` (to locate the installed skills) and, read-only, the member skills' bundled local scripts: impeccable's `detect.mjs` detector and ui-ux-pro-max's `search.py` database search.
- Starts one subagent per member skill for each audit or review.
- Writes only `ULTIMATE-DESIGN.md` during an audit; `apply` edits the files of the findings you choose and runs your project's own checks (lint, tests, build).
- Sends nothing anywhere and downloads nothing; no hooks, no MCP servers.

## Credits

impeccable (Apache-2.0) and ui-ux-pro-max (MIT) belong to their authors and are not bundled here; UltimateDesign only finds and runs the copies you have installed. The orchestration, merge rules and scoring are original (MIT).
