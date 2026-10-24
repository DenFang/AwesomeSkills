# Report format

Shared by the audit, review and refactor commands so that their output can be read by people and by the next command.

## Severity

| Level | Meaning | Examples |
|---|---|---|
| **P0** | Blocks someone, loses data, misleads, or fails accessibility | No focus style, error swallowed, double charge possible, hover-only action on touch, contrast below 3:1, dark pattern |
| **P1** | Works, but causes friction or reads as broken | Generic error copy, spinner for a known layout, modal for a routine action, centred numbers in a table |
| **P2** | Polish that separates "fine" from "premium" | Stagger timing, optical corrections, icon stroke consistency |

Report a finding only when you can point at the code. If something is a judgement call, say so in the evidence line instead of inflating its severity.

## Finding

Every finding uses this block. IDs are sequential per report (`F-001`, `F-002`, …) so the refactor command can target them.

```markdown
### F-007 · P1 · STA-7 Errors say what happened and offer a way out
- **Where:** `src/features/invoices/InvoiceList.tsx:84`
- **Evidence:** `catch (e) { setError("Something went wrong") }` shows a generic message with no retry.
- **Fix:** Name the failure ("We couldn't load your invoices") and add a Retry button that calls `refetch()`; keep loaded rows visible if this is a refresh (STA-9).
- **Effort:** S
- **Status:** open
```

- **Where**: one primary location as `path:line`. If the same issue repeats, list the first three and give the total ("and 14 more in `src/components/**`").
- **Evidence**: the code or behaviour that proves it, quoted briefly.
- **Fix**: concrete, in the project's own components and tokens.
- **Effort**: S (minutes, one place), M (one component or a few files), L (cross-cutting, such as introducing tokens).
- **Status**: `open`, `fixed`, `wontfix (reason)`, or `needs decision (question)`.

Group repeated instances of one rule into one finding rather than one finding per line.

## Audit report (`UX-AUDIT.md`)

```markdown
# UX audit · <project name> · <YYYY-MM-DD>

Scope: <paths audited> · Stack: <framework, styling> · Motion profile: <crisp | lively, and why>
Design system: <where tokens live, or "none found">

## Summary
| Area | P0 | P1 | P2 |
|---|---|---|---|
| States and feedback | 2 | 4 | 1 |
| … | | | |

Top 5 fixes by impact: F-003, F-001, F-012, F-007, F-020

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
<anything out of scope or that needs running the app, e.g. real contrast over images>
```

## Review output

Posted in the conversation (and written to a file only if the user asks):

```markdown
## UX review · <ref range> · <N files>
Verdict: ✅ ready | ⚠️ ready after P1 fixes | ⛔ needs changes (any P0)

<finding blocks for issues introduced or touched by the change, P0 first>

Already good in this change: <1 to 3 bullets>
```

## Refactor log

After fixing, update each finding's **Status** in `UX-AUDIT.md` (when working from an audit) and finish with:

```markdown
## Refactor result
Fixed: F-001, F-003, F-007 (n files changed)
Skipped: F-012 needs decision: <question>
Checks run: <build / lint / tests / type-check and their results>
```
