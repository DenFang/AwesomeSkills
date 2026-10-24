# Report format

## Unified finding

```markdown
### U-004 · P1 · 2/3 · Errors give no way out
- **Where:** `src/features/invoices/InvoiceList.tsx:84` (and 3 more in `src/features/**`)
- **Element:** invoice list error state
- **Sources:** uichecker K-6 (STA-7) · ui-ux-pro-max P-11 (Forms and Feedback · error recovery)
- **Evidence:** `catch (e) { setError("Something went wrong") }`, no retry.
- **Fix:** Name the failure and add Retry that calls `refetch()`; keep loaded rows visible on refresh.
- **Status:** open
```

`P1 · 2/3` is the shared severity and the agreement. **Status** is `open`, `fixed`, `fixed (already resolved)`, `wontfix (reason)`, `needs decision (question)`.

## Decision

```markdown
### D-2 · Heading typeface on the landing page
- **Where:** `src/styles/tokens.css:12`, `src/pages/index.astro`
- **A · impeccable:** pair a display serif for headings. Gains character on a brand page; costs a second font download.
- **B · uichecker (VIS-4):** keep one sans family and get hierarchy from size and weight. Gains consistency with the app; costs some personality.
- **Recommended: A**, because this is a brand surface and the app keeps its own tokens (merge.md step 4, rule 3).
- **Choice:** pending
```

## Audit report (`ULTIMATE-DESIGN.md`)

```markdown
# UltimateDesign audit · <project> · <YYYY-MM-DD>

Scope: <paths> · Stack: <…> · Product type: <tool | brand | both> · Design system: <where, or none found>
Skills used: uichecker <version> · impeccable <version, copy> · ui-ux-pro-max <version, copy> (or "not installed")

## Score
UltimateDesign score: **72 / 100** (acceptable) · Agreement rate: 41%

| Area | Unified | uichecker | impeccable | ui-ux-pro-max | Key finding |
|---|---|---|---|---|---|
| Accessibility | 2 | checked | checked | checked | U-001 |
| States and feedback | 1 | checked | not covered | partial | U-004 |
| … | | | | | |

Native scores: uichecker <area scores> · impeccable <14/20 Good> · ui-ux-pro-max <78% of checklist items>

Top 5 by impact: U-001, U-004, U-002, U-009, U-012
Decisions waiting for you: D-1, D-2

## Where all skills agree
<U-blocks with 3/3 (or 2/2), P0 first>

## Where two agree
<U-blocks with 2/3>

## Only one skill caught this
### uichecker
### impeccable
### ui-ux-pro-max

## Decisions (pick one option each)
<D-blocks>

## Coverage
<the coverage matrix; "single coverage" and "Not checked" areas named>

## What is already good
<3 to 6 bullets, marked with the skills that praised them>

## Dropped as unverified
<count per source, one line each>
```

Leave out a section that would be empty.

## Review output (in the conversation)

```markdown
## UltimateDesign review · <ref range> · <N files>
Verdict: ✅ ready | ⚠️ ready after the P1 fixes | ⛔ needs changes (any P0)
Skills used: … · Score for the changed scope: <n>/100 · Agreement: <n>%

<U-blocks introduced or touched by the change, P0 first, each with its agreement>
<D-blocks, if any>
Coverage gaps: <areas no skill checked for this change>
Already good in this change: <1 to 3 bullets>
```
