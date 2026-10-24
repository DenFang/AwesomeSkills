---
id: DbX0IKMtBKr
reel_url: https://www.instagram.com/reel/DbX0IKMtBKr/
pattern_page: https://designmotionhq.com/patterns/settings-system
date: 2026-07-29
duration_s: 55
type: ui
category: forms
topic: settings pages: apply model by stakes, task grouping, search, modified state with per-setting reset, danger zone with typed confirmation
sources: frames, voice-over, pattern page
---

# Settings is a system

**Caption:** Your settings page is harmless: until the last section. Settings is a system.
**Hook:** Most of a settings page is harmless, but the bottom of it can delete everything; so the page needs rules, not just a list.

## Main rule
Match each setting's apply model to its blast radius (low-stakes toggles apply instantly with a "Saved" confirmation; identity fields such as email get an explicit save bar with Cancel/Save), group settings by user task with advanced options collapsed, add a search that filters and shows the path of each match, mark every changed value with a dot and a per-setting reset, and quarantine destructive actions at the bottom behind typed-name confirmation.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 40 settings | size of the flat list that "reads like a phone book" | 0:12 voice; title "Forty settings, zero map" 0:13 |
| "39 settings hidden", "1 result" | search for "digest" filters 40 settings down to one | 0:27-0:29 on-screen |
| 3 levels | depth a setting can be buried; result path "Workspace > Email > Digest" | 0:24 voice, 0:27-0:29 on-screen |
| 1 click | to reveal advanced settings; to reset one setting | 0:16 voice (advanced), 0:36 voice (undo) |
| 3 tabs: Payments, Billing, Team | Stripe-style split "one tab per job" | 0:18 voice, 0:19-0:21 on-screen |
| 0 -> 1 -> 2 -> 1 modified | modified counter in the section header | 0:30-0:39 on-screen |
| Font size 14px -> 16px; Theme System -> Dark -> back to System | example overrides and reset | 0:31-0:39 on-screen |
| 6/14, 12/14, 14/14 | characters of the workspace name typed vs required ("acme-workspace" = 14); delete button enabled only at 14/14 | 0:45-0:48 on-screen |
| last position on the page | danger zone placement | 0:42-0:43 on-screen |

## Before / after
- **Instant vs explicit apply.** "Preferences" (tagged "applies instantly"): flipping Compact mode or Sound effects shows a small "Saved" chip next to the toggle, no save button. "Account": editing Email shows a modified dot and a bottom bar "You have unsaved changes" with Cancel and Save; only clicking Save commits (then shows "Saved"). Labels: "low stakes -> instant", "identity -> explicit". The mechanism: reversible, low-impact changes should not cost an extra step, while changes that affect sign-in or identity need a deliberate commit point and an easy way to back out.
- **Flat list vs grouped by task.** "Workspace settings" as "one flat list" of numbered rows (Digest frequency, Session timeout, Theme contrast, Export format, Webhook retries, Locale override, Time zone, Beta features, Email cadence, Sound volume...) vs "grouped by task": Account (Profile, Email addresses, Two-factor auth), Notifications (Push alerts, Mentions, Quiet hours), Billing (Payment method, Invoices) and a collapsed "Advanced" (Webhook signing, API version, Data export). Grouping by user intent instead of database/schema order makes the page scannable, and progressive disclosure keeps the common path short.
- **Scroll vs search.** A settings search field: typing "digest" filters to a single "Email digest" row with the match highlighted and a breadcrumb "Workspace > Email > Digest", plus "39 settings hidden" and "Enter opens it". Power users recall names, not locations; search with the path also teaches where the setting lives.
- **Silent changes vs visible modified state.** In "Appearance", each changed setting gets a dot before its label and a reset icon next to its control, and the header counts "N modified". A settings.json panel ("VS Code does this") marks overridden lines with a bar. Clicking reset on Theme returns it to System with a "Back to default" chip and the counter drops to 1. Visible, per-setting undo makes experimenting safe, because one change can be reverted without wiping the others.
- **Danger zone with typed confirmation.** "Danger zone" block (marked "Owner only") at the last position on the page, below Export workspace data and Transfer ownership; a diagram notes that on every screen of the page the danger action is pinned last. "Delete workspace" opens "Delete acme-workspace? This cannot be undone. Type the workspace name to confirm." with a progress count (6/14, 12/14); "Delete forever" stays disabled until the name matches (14/14), then becomes an active danger button. Caption: friction scales with severity.

## Do
- Apply low-stakes preferences instantly and confirm with a brief inline "Saved".
- Use an explicit save bar (unsaved-changes message, Cancel, Save) for identity and security fields such as email.
- Group settings by user task; collapse advanced options behind one expandable section; for large products split into tabs by job.
- Provide settings search that filters, highlights the match, shows the path, reports how many were hidden, and opens the result on Enter.
- Mark each modified value (dot/indicator), show a modified count, and offer a per-setting reset to default.
- Put destructive actions last in a bordered danger zone, restricted to the roles allowed to use them, behind a typed-name confirmation.

## Don't
- Don't use one global Save button for harmless toggles, and don't auto-save identity fields.
- Don't order settings by schema or org chart in one flat list.
- Don't bury settings in nested menus without search.
- Don't offer only "Reset all" when users need to revert one override.
- Don't let an irreversible delete fire on a single unguarded click.

## Scene by scene
- 0:00 A full settings page scrolls: Preferences (Dark mode, Notifications, Compact density), Account (Language, Timezone, Email digest, Public profile), Security (Two-factor auth, Active sessions "3 devices", Login alerts), Workspace (Members "12 members", Integrations "4 connected"), then a danger-tinted "Danger zone" with "Delete workspace". Overlay: most of it is harmless; settings is a system.
- 0:03 "Apply model: Instant. Or explicit." Preferences card ("applies instantly"): toggles flip, a "Saved" chip appears beside each. Account card: Email field is edited, a modified dot appears, a bar "You have unsaved changes" with Cancel/Save slides up; Save is clicked and shows "Saved". Side tags "low stakes -> instant", "identity -> explicit". Caption: instant for preferences, explicit for identity.
- 0:13 "Structure: Forty settings, zero map." A long numbered flat list tagged "one flat list" scrolls.
- 0:14 It becomes "grouped by task": Account, Notifications, Billing; at 0:17 an "Advanced" row expands to Webhook signing, API version, Data export. At 0:19 a caption "the Stripe pattern, one tab per job" with tabs Payments, Billing, Team (active tab moves). Caption: group by task, not by table.
- 0:22 "Search: Nobody scrolls to row 40." Settings page with a "Search settings" field; typing "di" then "digest" filters to "Email digest" with the match highlighted, path "Workspace > Email > Digest", "1 result", "39 settings hidden", "Enter opens it". Caption: type to filter, enter to jump.
- 0:30 "Modified state: Changed. Visibly." Appearance card "0 modified"; Theme changes System -> Dark (dot + reset icon, "1 modified"), Font size slider 14px -> 16px ("2 modified"); settings.json lines for the two overrides get a marker bar. At 0:38 reset on Theme returns it to System, chip "Back to default", "1 modified". Caption: undo is one click away.
- 0:40 "Danger zone: Quarantine the destructive." Danger zone ("Owner only") with "Delete this workspace: All data, members and integrations are removed." and an outlined danger "Delete workspace" button; bracket "last position on the page"; mini diagram "every screen of the page, danger pinned last".
- 0:44 Confirmation modal: typing the workspace name with counter 6/14, 12/14; "Delete forever" disabled until 14/14, then enabled and clicked. Caption: friction scales with severity.
- 0:49 Summary list "Settings is a system": Instant vs explicit, Group by task, Searchable, Reset per setting, Danger zone; follow and save buttons.

## Voice-over summary
- Most of a settings page is harmless, but the bottom deletes everything, so treat it as a system.
- Toggles apply instantly ("flip, done"); identity fields get a save bar and cancel: "Match the model to the blast radius."
- 40 settings in one list reads like a phone book: group by task, hide advanced behind one click, split by job like Stripe (payments, billing, team).
- Power users search instead of scrolling; one input finds a setting three levels deep, highlights the match and shows the path.
- Every changed setting shows a dot and a reset (VS Code marks overrides with a bar), so users experiment when undo is one click away.
- Destructive actions live in quarantine at the bottom with a danger border; deleting requires typing the name and the button stays inactive until it matches.

## Notes for the skill
- Instant-apply toggles: use `role="switch"` with `aria-checked` (or a native checkbox), update optimistically, show "Saved" via a polite live region, and roll back with an inline error if the request fails. Do not show the "Saved" chip for so short a time that screen-reader or slow readers miss it; the live region covers announcement.
- Explicit save bar: keep it visible (sticky) while there are unsaved changes, warn on navigation away (`beforeunload` / router guard), and make Cancel restore the last saved values. Email changes usually also need verification of the new address; show a pending state until confirmed.
- Mixing instant and explicit models on one page is fine only if each section labels its model clearly (the reel uses "applies instantly"); otherwise users wonder whether toggles in the save-bar section also need saving.
- Grouping: use headings (`h2`/`h3`) per group so screen-reader users can jump; the advanced disclosure is a button with `aria-expanded` controlling the region.
- Search: label the field, debounce lightly, announce result count ("1 result, 39 hidden") via `aria-live`, keep highlights as `<mark>`, and include synonyms/keywords (e.g. "password" finds "Two-factor auth"/"Security"). Provide an empty state with a way to clear the query.
- Modified indicator: the dot must not be colour-only; pair it with the reset button's accessible name ("Reset Font size to default (14px)") and/or visually hidden "modified" text. The section counter helps orientation.
- Typed confirmation: a disabled button gives no reason and is skipped by keyboard focus; describe the requirement next to the button (`aria-describedby`) or keep the button enabled and show an inline error if the name does not match. Allow paste, trim whitespace, and decide case sensitivity explicitly. Reserve typed confirmation for truly irreversible, high-impact actions; overusing it trains people to copy-paste without reading.
- Role gating ("Owner only"): hide or disable destructive actions for roles that cannot perform them, and say why.
