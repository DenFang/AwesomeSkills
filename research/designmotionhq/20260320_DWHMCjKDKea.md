---
id: DWHMCjKDKea
reel_url: https://www.instagram.com/reel/DWHMCjKDKea/
pattern_page: https://designmotionhq.com/patterns/proximity-rule
date: 2026-03-20
duration_s: 52
type: ui
category: visual
topic: Gestalt proximity: grouping by spacing
sources: frames, voice-over, pattern page
---

# Proximity: spacing does the grouping

**Caption:** not captured yet
**Hook:** The same 12 icons, one layout chaotic and the other instantly clear, separated by one rule: proximity.

## Main rule
Make the gap inside a group clearly smaller than the gap between groups (the video uses 8 px inside vs 32 px between in a toolbar, and 12 px vs 40 px in a form), so related items read as one unit without borders or dividers.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 12 | number of icons in the hook grid (3 rows of 4) | 0:00 voice + on-screen |
| 32 px | gap between two groups of three squares in the basic demo | 0:09-0:12 on-screen |
| 8 px | gap between icons inside a toolbar group | 0:20-0:26 on-screen |
| 32 px | gap between toolbar groups (Navigate / Actions / System) | 0:20-0:26 on-screen |
| 12 px | gap between related form fields (Full Name, Email Address) | 0:29-0:37 on-screen; page says "~12px" |
| 40 px | gap between form sections (Personal Info -> Payment) | 0:30-0:37 on-screen; page says "~40px" |
| 8 links -> 3 groups (2 + 2 + 4) | dashboard sidebar before/after | 0:38-0:48 on-screen; page says "eight sidebar links" |
| ratio about 1:3 to 1:4 | inside-gap to between-gap (derived: 8:32 and 12:40) | calculation, not stated |

## Before / after
1. **Icon grid (0:00-0:05).** Bad ("Chaos"): 12 identical neutral squares in an evenly spaced 4x3 grid. Good ("Clear"): the same 12 split into three rows labelled Navigation, Content, Commerce with extra space between rows (and a distinct colour per group). Why: the visual system groups by distance before reading anything, so the structure is perceived instantly.
2. **Basic proximity (0:06-0:12).** Six equal squares in a row look like one set; moving them into 3 + 3 with a 32 px gap makes two "Related" groups. Caption: your brain processes this before you read.
3. **Toolbar (0:13-0:26).** Bad ("Equally spaced"): Home, Search, User, Edit, Share, Trash, Bell, Help all at the same spacing; the eye has nowhere to land. Good ("Grouped by function"): Navigate (Home, Search, User), Actions (Edit, Share, Trash), System (Bell, Help) with 8 px inside groups and 32 px between. Why: grouped controls reduce search time; users scan three chunks instead of eight items.
4. **Form (0:27-0:37).** Full Name and Email Address sit 12 px apart under "Personal Info"; Card Number, Expiry and CVV start 40 px lower under "Payment". "Zero dividers. Just spacing." Why: the larger gap creates the section boundary, so no lines or boxes are needed and the form looks lighter.
5. **Dashboard sidebar (0:38-0:48).** Bad: a flat list of eight links (Overview, Analytics, Users, Revenue, Settings, Profile, Support, Billing) at equal spacing. Good: three spaced groups with small headings: Dashboard (Overview, Analytics), Management (Users, Revenue), Account (Settings, Profile, Support, Billing). "Same links. Different clarity."

## Do
- Keep spacing within a group tighter than spacing between groups; make the difference obvious (roughly 3-4x in the examples).
- Group toolbar and navigation items by function or meaning.
- Separate form sections with a larger gap and a short section heading.
- Let whitespace carry the grouping before adding borders, boxes or dividers.

## Don't
- Don't space every element equally; it flattens hierarchy and forces item-by-item parsing.
- Don't add boxes and divider lines where a larger gap communicates the same grouping.
- Don't place a label closer to the wrong field (a label must sit nearer its own input than the previous one).

## Scene by scene
- 0:00 Split screen "Chaos" (12 neutral squares, even grid) vs "Clear" (three labelled, coloured rows: Navigation, Content, Commerce); magnet icon; caption "One rule."
- 0:06 "Proximity · Close = related. Far = separate." Six squares in a row, then split into 3 + 3 with a "32px" marker and "Related" underlines; brain icon; "Your brain processes this before you read."
- 0:13 "Secret 01 · Navigation": toolbar of eight labelled icons appears "Equally spaced".
- 0:19 Icons regroup "Grouped by function" into Navigate / Actions / System, each group tinted; spacing markers 8px / 32px / 8px / 32px / 8px; "Same items. Instant clarity."
- 0:27 "Secret 02 · Forms": Full Name, Email Address, Card Number fields; then section headings Personal Info and Payment appear with Expiry and CVV.
- 0:29 Spacing markers 12px (between Full Name and Email) and 40px (between sections); "Zero dividers. Just spacing."
- 0:38 "Dashboard Sidebar · Same links. Different clarity." BEFORE flat list of eight neutral-coloured links; AFTER grouped under Dashboard, Management, Account with a different dot colour per group.
- 0:49 Outro "One rule. Zero design degree." with 3 + 3 squares; "Follow @designmotionhq".

## Voice-over summary
- Same 12 icons: one layout is chaos, the other instantly clear, because of proximity.
- Close things feel related, far things feel separate, and the brain does this automatically.
- An evenly spaced toolbar leaves the eye nowhere to land; grouping into navigation, actions and settings makes it scannable.
- In forms, keep name and email tight as personal info and put the card number below with more space, so "zero dividers" are needed.
- A real dashboard sidebar goes from a flat list to grouped categories: same links, different clarity.

## Notes for the skill
- In the hook and sidebar demos the "after" also adds group colours and headings, so the improvement is not from spacing alone; spacing is the primary cue, headings and colour are reinforcing cues. Do not rely on colour for grouping (WCAG 1.4.1).
- Implementation: use spacing tokens, e.g. `gap: var(--space-2)` (8 px) inside a group and `gap: var(--space-6)` or margin (32 px) between groups; in forms, `fieldset` or a `section` per group with a visible heading (`legend` or heading element) so screen readers get the same grouping that sighted users see from spacing.
- Toolbars: use `role="toolbar"` with `aria-label`, and optionally `role="group"` per cluster; icon-only buttons need accessible names, and keep each target at least 24x24 px (WCAG 2.5.8), ideally 44 px.
- Form labels: keep the label closer to its own field than to the field above (label-to-input gap smaller than field-to-field gap), otherwise proximity mis-assigns labels.
- Edge case: on narrow screens a 40 px section gap can push content below the fold; scale gaps with a token set but keep the inside/between ratio.
