# Passes

How to find each member skill, how to brief each pass and what every pass must return. How the passes run (subagents, this session, or not at all) is set by the mode in `modes.md`.

## 1. Find the member skills

Below, `<uichecker>` is the uichecker plugin root (the folder that holds `skills/guidelines/`, `skills/audit/` and `skills/review/`); `<impeccable>` and `<ui-ux-pro-max>` are the folders that hold each skill's `SKILL.md`. The passes read files from these folders directly, so they do not depend on the Skill tool inside a subagent.

**uichecker** (this plugin depends on it): invoke the `uichecker:guidelines` skill once with the Skill tool. Its header names the skill's base directory; `<uichecker>` is two levels up from it.

**impeccable** and **ui-ux-pro-max**: look only in these places, in this order of preference, and ignore copies anywhere else (backups, marketplace clones):

| Kind | Path |
|---|---|
| project | `./.claude/skills/<name>/SKILL.md` |
| personal | `~/.claude/skills/<name>/SKILL.md` |
| plugin | `~/.claude/plugins/cache/*/*/*/skills/<name>/SKILL.md` |

```bash
for n in impeccable ui-ux-pro-max; do ls -d ./.claude/skills/$n ~/.claude/skills/$n ~/.claude/plugins/cache/*/*/*/skills/$n 2>/dev/null; done
```

If none is found but the skill list shows the skill (an organisation copy, or a plugin read from a local path), invoke it once with the Skill tool only to read the base directory from its header, and ignore the rest of the loaded instructions.

Take one copy per member: the first kind in the table; among copies of the same kind, the highest `version` in the frontmatter, or the version in the plugin cache path, otherwise "unknown". Say which copy you used. Never run two copies of the same member.

A missing member is reported, not fatal: run the others, mark its column "not installed" in the report and print its install command once:

```text
impeccable:     claude plugin marketplace add pbakaus/impeccable && claude plugin install impeccable@impeccable
ui-ux-pro-max:  claude plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill && claude plugin install ui-ux-pro-max@ui-ux-pro-max-skill
uichecker:      claude plugin install uichecker@awesome-skills
```

With fewer than two members available there is nothing to cross-check: say so and suggest running the one available skill directly.

## 2. Shared brief

Settle the context once and give the same facts to every pass, so they judge the same product:

- **Scope**: the files under review as a list of paths; for a review also the diff command, the changed files, and how to read each file (the working tree, or `git show <ref>:<path>` when the reviewed tip is not the working tree).
- **Stack**: framework, styling (CSS, Tailwind, CSS-in-JS, native), platform.
- **Product type**: tool (app UI, admin, dashboard: design serves the task), brand (landing, marketing: design is the product), or both, and which files are which.
- **Design system**: where tokens, theme and shared components live, or "none found".
- **Project notes**: `PRODUCT.md`, `DESIGN.md`, `.ux-ignore.md`, `.impeccable/critique/ignore.md` if present.

## 3. Rules for every pass

Put these in every pass brief verbatim:

1. Read-only. Do not edit, create or delete any project file. In particular: do not create `PRODUCT.md` or `DESIGN.md`, do not run impeccable `init`, `document` or `live-server`, do not persist critique snapshots, never run ui-ux-pro-max with `--design-system` or `--persist`, do not start dev servers, do not spawn subagents and do not ask the user questions.
2. If the skill's own setup wants something that would break rule 1 (for example impeccable's `scripts/impeccable context` reporting `NO_PRODUCT_MD` and routing to `init`), skip that step, use the shared brief instead and say so in `notes`.
3. Files and scripts belong to the skill's folder: wherever the skill's text gives a path through `${CLAUDE_PLUGIN_ROOT}/…`, `${CLAUDE_PLUGIN_ROOT}/.claude/skills/<name>/…`, `.claude/skills/<name>/…`, `<skill-base-dir>/…` or a bare `references/…`, replace the whole prefix up to and including the skill folder with the resolved folder, and run scripts from it.
4. Stay inside the scope. Report only what you can point at in the code, with `path:line`.
5. Judge only by your own skill. Do not try to guess what the other skills would say, and do not soften findings to agree with anything.
6. Return exactly one JSON block in the shape of section 5, then nothing else.

## 4. What each pass does

### uichecker pass
Read `<uichecker>/skills/guidelines/SKILL.md`, then follow `<uichecker>/skills/audit/SKILL.md` (audit mode) or `<uichecker>/skills/review/SKILL.md` (review mode) up to, but not including, writing the report: inventory the elements, check only the rules that apply, verify each finding. Use the scope and, in review mode, the diff and file list from the brief instead of its own scope and "Collect the change" steps. Native score: the area scores 0 to 4 from its report format. Rule field: the rule ID (`STA-7`).

### impeccable pass
Read `<impeccable>/SKILL.md` (setup and design guidance), `<impeccable>/reference/audit.md`, and the mode reference that matches the product type when present (`reference/mode-operate.md` for tool surfaces, `reference/mode-persuade.md` for brand surfaces, `reference/mode-read.md` for docs). Run its detector over the markup files in scope (not CSS-only files): `<impeccable>/scripts/impeccable detect --json <paths>` (exit 0 clean, 2 findings); older copies ship `node <impeccable>/scripts/detect.mjs --json <paths>` instead. If neither exists or it fails, write "deterministic scan unavailable" in `notes` and continue. Score the five audit dimensions 0 to 4 as `audit.md` defines them. In deep mode also follow `reference/critique.md` Assessment A only (heuristic scores, cognitive load, design-specificity verdict), inline: no subagents, no DEGRADED banner, no snapshot, no closing questions. Native score: the audit health score out of 20 with its band (plus the heuristics total in deep mode). Rule field: the dimension or anti-pattern (`Implementation Integrity · gradient text`).

### ui-ux-pro-max pass
Read `<ui-ux-pro-max>/SKILL.md` and, when present, `references/quick-reference.md` (the full rules of its ten priority categories: Accessibility, Touch and Interaction, Performance, Style Selection, Layout and Responsive, Typography and Color, Animation, Forms and Feedback, Navigation, Charts and Data) and `references/pro-rules.md` (common rules and the pre-delivery checklist, written for app UI). Check the scope against every category that has elements in scope; use `python3 <ui-ux-pro-max>/scripts/search.py "<query>" --domain <domain>` (and `--stack <stack>`) for the specific elements found, read-only. Native score: per category, the share of applicable quick-reference rules that pass, as a percentage, plus the overall share. Rule field: the category and rule (`Accessibility · focus states visible`).

## 5. Return shape

```json
{
  "source": "uichecker | impeccable | ui-ux-pro-max",
  "copy": "<resolved folder and version>",
  "mode": "audit | review",
  "native_score": {
    "summary": "14/20 Good | 3 areas at 2, … | 78% of applicable rules pass",
    "areas": { "<the skill's own dimension or area>": "<its score>" }
  },
  "coverage": {
    "accessibility": "checked | partial | not covered | n/a",
    "states-feedback": "…", "forms": "…", "data-display": "…",
    "interaction-navigation": "…", "motion": "…", "visual-system": "…",
    "layout-responsive": "…", "content": "…", "performance": "…",
    "distinctiveness": "…"
  },
  "findings": [
    {
      "id": "<source letter K, I or P>-<n>",
      "native_severity": "<as the skill states it>",
      "area": "<one of the coverage keys>",
      "where": "src/components/InvoiceList.tsx:84",
      "also": ["other path:line places with the same defect"],
      "nearby": false,
      "element": "invoice list error state",
      "problem": "one sentence",
      "evidence": "quoted code or behaviour",
      "fix": "concrete change, in the project's own components and tokens",
      "rule": "<rule ID, dimension or category rule>"
    }
  ],
  "strengths": ["things the scope already does well"],
  "notes": "skipped steps, assumptions, anything not checked"
}
```

- Source letters: K for uichecker, I for impeccable, P for ui-ux-pro-max.
- Coverage values: `checked` (the skill checked this area in scope), `partial`, `not covered` (the skill does not check this area), `n/a` (nothing in scope for this area).
- `nearby` is `true` only in review mode, for a P0 in an untouched line of a changed component.
- Each pass gives only `native_severity`; the shared level is set in `merge.md` step 1.

## 6. Running the passes

In full mode the passes are parallel subagents (the Agent tool, general-purpose type), one per available member, each brief holding: the member's resolved folder, the shared brief, the rules in section 3 verbatim, its section 4 text and the return shape in section 5. They must not see each other's output, because a pass that reads another's findings anchors on them and the cross-check loses its value. In current mode the same passes run one after another in this session (`modes.md` section 3). Lite mode does not use separate passes (`modes.md` section 4).
