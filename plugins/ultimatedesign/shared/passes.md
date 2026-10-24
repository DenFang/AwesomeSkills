# Passes

UltimateDesign runs three independent passes over the same scope, one per member skill, and merges them afterwards (`merge.md`). This file says how to find each skill, how to brief each pass and what every pass must return.

## 1. Find the member skills

| Member | Look for | Copy to prefer |
|---|---|---|
| uichecker | the `uichecker:guidelines` skill (this plugin depends on it); on disk `skills/guidelines/SKILL.md` inside the `uichecker` plugin | the plugin |
| impeccable | an `impeccable` skill in the skill list (personal, project, plugin `impeccable:impeccable`, or an organisation copy); on disk a folder `impeccable/` holding `SKILL.md` and `reference/audit.md` | project, then personal, then plugin, then organisation |
| ui-ux-pro-max | a `ui-ux-pro-max` skill (personal, project, plugin `ui-ux-pro-max:ui-ux-pro-max`, or organisation copy); on disk a folder `ui-ux-pro-max/` holding `SKILL.md` and `scripts/search.py` | project, then personal, then plugin, then organisation |

Resolve each member to the folder that holds its `SKILL.md`, because the passes read the files directly and must not depend on the Skill tool being available inside a subagent:

```bash
find .claude ~/.claude -path '*/node_modules' -prune -o -name SKILL.md -path '*impeccable/SKILL.md' -print 2>/dev/null
find .claude ~/.claude -path '*/node_modules' -prune -o -name SKILL.md -path '*ui-ux-pro-max/SKILL.md' -print 2>/dev/null
```

For uichecker, which is a plugin and may be read from anywhere, invoke the `uichecker:guidelines` skill once with the Skill tool: its header names the skill's base directory, and the uichecker folder is two levels up from it (the folder that holds `skills/audit/` and `skills/review/`). Use the same trick for impeccable or ui-ux-pro-max when `find` returns nothing but the skill list shows them (for example a plugin read from a local path).

When several copies exist, take one per member by the order above and, among equals, the highest `version` in its frontmatter; say which one you used. Never run two copies of the same member.

A member that is missing is reported, not fatal: run the others, mark its column "not installed" in the report and print its install command once:

```text
impeccable:     claude plugin marketplace add pbakaus/impeccable && claude plugin install impeccable@impeccable
ui-ux-pro-max:  claude plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill && claude plugin install ui-ux-pro-max@ui-ux-pro-max-skill
uichecker:      claude plugin install uichecker@awesome-skills
```

With fewer than two members available there is nothing to cross-check: say so and suggest running the one available skill directly.

## 2. Shared brief

Settle the context once and give the same facts to every pass, so they judge the same product:

- **Scope**: the files or the diff under review, as a list of paths (and, for a review, the diff command).
- **Stack**: framework, styling (CSS, Tailwind, CSS-in-JS, native), platform.
- **Product type**: tool (app UI, admin, dashboard: design serves the task), brand (landing, marketing: design is the product), or both, and which files are which.
- **Design system**: where tokens, theme and shared components live, or "none found".
- **Project notes**: `PRODUCT.md`, `DESIGN.md`, `.ux-ignore.md`, `.impeccable/critique/ignore.md` if present.

## 3. Rules for every pass

Put these in every pass brief verbatim:

1. Read-only. Do not edit, create or delete any project file. In particular: do not create `PRODUCT.md` or `DESIGN.md`, do not run impeccable `init`, do not persist critique snapshots, never run ui-ux-pro-max with `--persist`, do not start dev servers.
2. If the skill's own setup wants something that would break rule 1 (for example impeccable's `context.mjs` reporting `NO_PRODUCT_MD`), skip that step, use the shared brief instead and say so in `notes`.
3. Scripts belong to the skill's folder: run them from the resolved folder (`node <impeccable dir>/scripts/detect.mjs`, `python3 <ui-ux-pro-max dir>/scripts/search.py`), not from paths the skill text assumes such as `.claude/skills/<name>/` or `${CLAUDE_PLUGIN_ROOT}`.
4. Stay inside the scope. Report only what you can point at in the code, with `path:line`.
5. Judge only by your own skill. Do not try to guess what the other skills would say, and do not soften findings to agree with anything.
6. Return exactly one JSON block in the shape below, then nothing else.

## 4. What each pass does

### uichecker pass
Read `<uichecker>/skills/guidelines/SKILL.md`, then follow `<uichecker>/skills/audit/SKILL.md` (audit mode) or `<uichecker>/skills/review/SKILL.md` (review mode) up to, but not including, writing the report: inventory the elements, check only the rules that apply, verify each finding. Native score: the area scores 0 to 4 from its report format. Rule field: the rule ID (`STA-7`).

### impeccable pass
Read `<impeccable>/SKILL.md` (setup and design guidance) and `<impeccable>/reference/audit.md`, plus `reference/product.md` or `reference/brand.md` for the register. Run its bundled detector over the markup files in scope if it exists (`node <impeccable>/scripts/detect.mjs --json <paths>`; exit code 2 means findings). Score the five audit dimensions 0 to 4 as `audit.md` defines them. In deep mode also follow `reference/critique.md` Assessment A only (heuristic scores, cognitive load, AI-slop verdict) without persisting anything. Native score: the audit health score out of 20 with its band (plus the heuristics total in deep mode). Rule field: the dimension or anti-pattern (`Anti-Patterns · gradient text`).

### ui-ux-pro-max pass
Read `<ui-ux-pro-max>/SKILL.md`: its rule categories by priority (Accessibility, Touch and Interaction, Performance, Style Selection, Layout and Responsive, Typography and Color, Animation, Forms and Feedback, Navigation, Charts and Data), its common rules and its pre-delivery checklist (in some versions these live in `references/quick-reference.md` and `references/pro-rules.md`). Check the scope against every category that has elements in scope; use `search.py --domain <domain> "<query>"` (and `--stack <stack>`) for the specific elements found, read-only. Do not generate or persist a design system. Native score: per category, the share of applicable checklist items that pass, as a percentage, plus the overall share. Rule field: the category and item (`Accessibility · focus states visible`).

## 5. Return shape

```json
{
  "source": "uichecker | impeccable | ui-ux-pro-max",
  "copy": "<resolved folder and version>",
  "mode": "audit | review",
  "native_score": {
    "summary": "14/20 Good | 3 areas at 2, … | 78% of checklist items pass",
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
      "severity": "P0 | P1 | P2 | P3",
      "native_severity": "<as the skill states it>",
      "area": "<one of the coverage keys>",
      "where": "src/components/InvoiceList.tsx:84",
      "element": "invoice list error state",
      "problem": "one sentence",
      "evidence": "quoted code or behaviour",
      "fix": "concrete change, in the project's own components and tokens",
      "rule": "<rule ID, dimension or category item>"
    }
  ],
  "strengths": ["things the scope already does well"],
  "notes": "skipped steps, assumptions, anything not checked"
}
```

Source letters: K for uichecker, I for impeccable, P for ui-ux-pro-max. Severity scales are normalised in `merge.md`; each pass fills `native_severity` with its own label and `severity` with the normalised one.

## 6. Running the passes

Launch the three passes as parallel subagents (the Agent tool, general-purpose type), one per available member, each with: the member's resolved folder, the shared brief, the rules in section 3 and its section 4 text. They must not see each other's output, because a pass that reads another's findings anchors on them and the cross-check loses its value.

If subagents are not available, run the passes one after another in this order: uichecker, impeccable, ui-ux-pro-max. Finish and record each JSON before reading the next skill, and do not revise an earlier pass after a later one.
