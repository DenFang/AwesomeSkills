# Modes

Every audit and review runs in one of three modes. They share the members (`passes.md` section 1), the shared brief (section 2), the read-only rules (section 3), the merge (`merge.md`) and the report format; they differ in how the three skills are run.

| Mode | Flag | Runs | Independence | Cost |
|---|---|---|---|---|
| full | none (default) | one subagent per skill, in parallel | highest: no pass sees another | slowest, most tokens |
| current | `--current` | the same three passes, one after another in this session | weaker: the passes share one context | same depth, no subagents |
| lite | `--lite` | one pass in this session over a combined, de-duplicated rule list | none: rules are merged before the code is read | fastest |

## 1. Pick the mode

- No flag: **full**. If subagents are not available in this environment, switch to **current** and say so in one line.
- `--current` or `--lite`: that mode. Both given: ask which one and stop.
- `--deep` works in full and current. With `--lite`, say in one line that it is ignored.

Record the mode for the report header (`report-format.md`).

## 2. Full

Run the passes as `passes.md` section 6 describes: one general-purpose subagent per available member, in parallel, each with its resolved folder, the shared brief, the rules from section 3 verbatim, its section 4 text and the return shape from section 5. If a pass fails or returns no JSON, retry it once; if it fails again, continue without it and say so. Then follow `merge.md` steps 1 to 7.

## 3. Current

Run the same three passes yourself, in this order: uichecker, impeccable, ui-ux-pro-max.

1. For each member, follow its section 4 text with the rules from section 3, and write its JSON in the section 5 shape before you open the next member's files.
2. Do not revise an earlier pass after reading a later skill. Judge each pass only by its own skill: do not look for what an earlier pass found, and do not skip a problem because an earlier pass already reported it, since agreement is counted from what each pass finds on its own.
3. Then follow `merge.md` steps 1 to 7, exactly as in full mode.

In the report header, add: "Independence: same session (passes shared one context)".

## 4. Lite

One pass in this session. The three skills' guidance is merged at the rule level first, then the code is checked once. No subagents, no separate pass JSON, no native scores.

### 4.1 Inventory

List the elements in scope (forms, tables, dialogs, menus, navigation, charts, animations, copy, tokens and theme, page layout), as uichecker's guidelines skill does in its step 2.

### 4.2 Collect the guidance per element

For each element type in the inventory, collect what each available skill says about it. Read only what you need:

- **uichecker**: the rules its routing table lists for that element, plus the always-on rules (`<uichecker>/skills/guidelines/SKILL.md` step 2, then the listed `references/` files).
- **impeccable**: the anti-patterns and design guidance in `<impeccable>/SKILL.md` and the dimensions and checks in `<impeccable>/reference/audit.md` that apply to the element, plus the mode reference for the product type when present (`reference/mode-operate.md`, `mode-persuade.md` or `mode-read.md`).
- **ui-ux-pro-max**: the priority categories and checklist items in `<ui-ux-pro-max>/SKILL.md` (or its `references/quick-reference.md` and `references/pro-rules.md`) that apply to the element. A `search.py --domain <domain> "<element>"` query is allowed, read-only.

Do not run the members' full audit procedures, and do not write a JSON per member.

### 4.3 Merge the rules

Compare the guidance for each element and sort every item into one of three kinds:

1. **Same check, same verdict**: the skills ask for the same property or behaviour and would pass and fail the same code. Keep one item, the most detailed (concrete numbers, conditions, a detection hint, a fix). Record the others as "also: <skill> <rule>". Rules that check the same thing with different thresholds (a 44 px against a 48 px minimum target) are a conflict only where the code falls between the two; otherwise keep the stricter one and note the other.
2. **Different meaning or verdict**: the prescriptions cannot both hold for the same element, or one skill flags what another recommends (one sans family against a display serif pairing; glass panels flagged against glass panels recommended). Keep both as the options of a decision candidate.
3. **One skill only**: keep it and mark it single-source.

The result is one combined checklist per element. Each item carries its kept text, its source and the skills that share it.

### 4.4 Check the code once

Check every element in scope against its combined checklist, as uichecker's audit (or review) does with its rules: report only what you can point at with `path:line`, and follow the read-only rules in `passes.md` section 3. impeccable's detector may be run once, as in `passes.md` section 4 (`<impeccable>/scripts/impeccable detect --json <paths>`). Each finding cites the kept rule and lists the skills that share it, for example `Sources: uichecker INT-1 · also impeccable Accessibility · ui-ux-pro-max focus states`.

A decision candidate becomes a decision `D-#` only when the code in scope contains the element it is about. Write it as in `merge.md` step 4: options per skill with gains and costs, and a recommendation by the same precedence.

### 4.5 Merge and score

Then follow `merge.md`:

- step 1: severity from the kept rule's source, raised to the highest level any sharing skill gives that rule;
- step 2 is already done by 4.3: do not group again;
- step 3: verify P0s and single-source P1s against the code;
- step 4 is already done by 4.3 and 4.4;
- step 5: coverage per area by the skills that contributed rules to it (`checked` when at least one kept rule from that skill applied and was checked);
- step 6: unified area scores and the score out of 100; there are no native scores, so write "native scores: not run separately (lite)";
- step 7: order and number.

**Agreement in lite** means rule overlap, not independent detection: write it as `rule 3/3` (or `rule 2/3`, `rule 1/3`), and label the agreement rate "rule overlap" in the report.
