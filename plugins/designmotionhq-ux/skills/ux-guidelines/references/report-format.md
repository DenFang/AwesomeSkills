# Report format

Shared by the audit, review and refactor commands so that their output can be read by people and by the next command.

## Severity

| Level | Meaning | Examples |
|---|---|---|
| **P0** | Blocks someone, loses data, misleads, or fails accessibility | No focus style, error swallowed, double charge possible, hover-only action on touch, text contrast below 4.5:1 (3:1 for large text and UI parts), dark pattern |
| **P1** | Works, but causes friction or reads as broken | Generic error copy, spinner for a known layout, modal for a routine action, centred numbers in a table |
| **P2** | Polish that separates "fine" from "premium" | Stagger timing, optical corrections, icon stroke consistency |

Use the severity written on the rule. When a rule gives a range (for example "P0 when …, P1 otherwise"), pick the level that matches the evidence. Report a finding only when you can point at the code. If something is a judgement call, say so in the evidence line instead of inflating its severity. Many P2 notes bury the important findings: report P2 only where it is clearly visible to users, and group the rest.

## Finding

Every finding uses this block. Audit findings are numbered `F-001`, `F-002`, … and review findings `R-001`, `R-002`, …, in report order, so the refactor command can target them.

```markdown

### F-007 · P1 · STA-7 · Errors say what happened and offer a way out
- **Where:** `src/features/invoices/InvoiceList.tsx:84`
- **Evidence:** `catch (e) { setError("Something went wrong") }` shows a generic message with no retry.
- **Impact:** A user whose invoices fail to load sees no reason and has no way to try again.
- **Fix:** Name the failure ("We couldn't load your invoices") and add a Retry button that calls `refetch()`; keep loaded rows visible if this is a refresh (STA-9).
- **Effort:** S
- **Status:** open
```

- **Where**: one primary location as `path:line`. If the same issue repeats, list the first three and give the total ("and 14 more in `src/components/**`").
- **Evidence**: the code or behaviour that proves it, quoted briefly.
- **Impact**: who is affected and how, in one sentence.
- **Fix**: concrete, in the project's own components and tokens. Name the element and the change ("make Save the only filled button in `InvoiceHeader`"), never a vague "consider improving the hierarchy".
- **Effort**: S (minutes, one place), M (one component or a few files), L (cross-cutting, such as introducing tokens).
- **Status**: `open`, `fixed`, `fixed (already resolved)`, `wontfix (reason)`, or `needs decision (question)`.

Group repeated instances of one rule into one finding rather than one finding per line.

## Area scores

Score each area that exists in the scope from 0 to 4. Mark an area `n/a` when the scope has nothing it covers (no forms, no motion), never 0.

| Score | Meaning |
|---|---|
| 0 | Broken: P0 problems across the area |
| 1 | Major gaps: several P0 or many P1 problems |
| 2 | Partial: works, with clear P1 problems |
| 3 | Good: minor P1 or P2 problems only |
| 4 | Excellent: nothing beyond small polish |

## Audit report (`UX-AUDIT.md`)

```markdown
# UX audit · <project name> · <YYYY-MM-DD>

Scope: <paths audited> · Stack: <framework, styling, platform> · Product type: <tool | consumer app | marketing site | mixed, and why> · Motion profile: <crisp | lively>
Design system: <where tokens live, or "none found">

## Summary
| Area | Score | P0 | P1 | P2 | Key finding |
|---|---|---|---|---|---|
| States and feedback | 1 | 2 | 4 | 1 | F-001 |
| Forms and input | n/a | | | | no forms in scope |
| … | | | | | |

First impression: <two or three sentences from the holistic pass: what the eye lands on, whether the purpose is clear, whether it looks generated>

Top 5 fixes by impact: F-003, F-001, F-012, F-007, F-020

## Systemic issues
<patterns that repeat across the codebase and are better fixed once, e.g. "no motion tokens: 23 inline durations", each pointing at its finding>

## Findings

### States and feedback
<finding blocks, P0 first>

### Forms and input

### Data display

### Interaction and navigation

### Motion

### Visual system

### Content and persuasion

## What is already good
<3 to 6 bullets, so the refactor keeps it>

## Not checked
<anything out of scope, rules that need the running app (real contrast over images, animation feel), translated or skipped checks on non-web stacks>
```

Leave out an area heading when the area is `n/a`.

## Review output

Posted in the conversation (and written to a file only if the user asks):

```markdown
## UX review · <ref range> · <N files>
Verdict: ✅ ready (no P0 or P1) | ⚠️ ready after the P1 fixes | ⛔ needs changes (any P0)

<R-NNN finding blocks for issues introduced or touched by the change, P0 first>

Nearby, not introduced by this change: <P0 finding blocks in the same components, if any>

Already good in this change: <1 to 3 bullets>
```

## Refactor log

After fixing, update each finding's **Status** in `UX-AUDIT.md` (when working from an audit) and finish with:

```markdown
## Refactor result
Fixed: F-001, F-003, F-007 (n files changed)
Needs decision: F-012: <question> (recommended: <answer>)
Checks run: <build / lint / tests / type-check and their results>
```

## Ignore file

If the project has `.ux-ignore.md`, read it before reporting. Each line names a rule ID, optionally with a path glob and a reason (`VIS-17 src/marketing/** gradients are brand-approved`). Do not report findings that match it; mention how many were suppressed.
