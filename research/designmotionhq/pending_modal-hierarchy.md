---
id: unknown
reel_url: unknown
pattern_page: https://designmotionhq.com/patterns/modal-hierarchy
date: unknown
duration_s: 49
type: ui
category: interaction
topic: choosing an overlay (modal, bottom sheet, drawer, popover)
sources: frames, voice-over, pattern page
---

# Modal hierarchy: pick the overlay by whether it blocks

**Caption:** not captured yet
**Hook:** There are five kinds of overlay and most apps pick the wrong one.

## Main rule
Ask one question first: does this need to block the user? If yes, use a modal (reserved for destructive actions, critical confirmations and decisions); if no, use a bottom sheet (mobile filters/options), a drawer (navigation, settings, secondary content) or a popover anchored to its trigger (small menus and filters, under about 200px wide).

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 5 overlays | number of overlay types claimed in the hook (only 4 are explained: modal, sheet, drawer, popover) | 0:00-0:02 "5 overlays. Pick the right one." + voice |
| > 3 fields | forms longer than three fields must not go in a modal | 0:12 checklist "× Forms longer than 3 fields" + voice |
| 12 fields | the bad example: "12-field signup modal" marked "DON'T" | 0:07-0:10 |
| < 200px | max popover width ("max 200px", "Tiny, under 200px") | 0:30-0:37 on-screen + voice; page: "~200px" |
| 90% | share of overlay mistakes fixed by the single "does it block the user?" question | 0:38-0:46 subtitle + voice |

## Before / after
1. **Modal used right vs wrong.** Good: "Delete account?" modal with a warning icon, "This can't be undone. Your data will be deleted forever.", Cancel and a danger-styled Delete; the dashboard behind is blurred/dimmed. Bad ("DON'T"): a 12-field signup form inside a modal. Why: a modal removes access to everything else, which is justified only when the decision must be made before anything else; long forms in modals trap the user, scroll awkwardly, and risk data loss on accidental dismiss.
2. **Bottom sheet.** A "Filters" sheet (genre chips, Sort by: Most popular / Newest / A-Z, full-width "Apply filters") rises from the bottom over a "Library" screen at partial height, with a drag handle; it is dragged up to a taller snap point. Why: on phones the bottom edge is within thumb reach, partial height keeps the underlying screen visible for context, and swipe-to-dismiss matches touch expectations.
3. **Drawer.** A side navigation panel (user "Thibault G., Pro plan", Home, Projects, Settings, Team, Logout) slides in from the left edge while the main screen stays visible to the right. Why: navigation and settings are secondary to the current view; an edge panel leaves the main view alive and returns users to where they were.
4. **Popover.** From a toolbar, the "⋯" button opens a small menu (Edit, Duplicate, Delete) and the filter icon opens a "STATUS" checklist (Active, Pending, Closed) anchored under the trigger, bracketed "max 200px". Why: anchoring to the trigger keeps cause and effect spatially linked; staying narrow keeps it feeling like a local, lightweight action.
5. **Decision tree.** "Does it block the user?" → YES: MODAL; NO: "Mobile or contextual?" → SHEET (mobile), POPOVER (anchored), DRAWER (side nav). Why: matching overlay weight to intent avoids adding blocking friction to routine actions.

## Do
- Use modals only for destructive actions, critical confirmations and decisions that must be answered first.
- Keep modal content short (no forms longer than 3 fields).
- Use a bottom sheet on mobile for filters, options and contextual actions; give it a drag handle and partial-height snap points.
- Use an edge drawer for navigation, settings and secondary content; keep the main view visible.
- Anchor popovers to their trigger and keep them narrow (under about 200px).
- Ask "does it block the user?" before choosing any overlay.

## Don't
- Put long forms (the video's 12-field signup) in a modal.
- Use a full-screen scrim/modal for routine, non-blocking actions.
- Let popovers grow wide or host blocking flows.
- Bury navigation inside a blocking overlay.

## Scene by scene
- 0:00 Five outlined overlay shapes drift and snap into place on a phone outline (centre card, left edge panel, small anchored card, bottom panel, small bar at the bottom); caption "5 overlays. Pick the right one."
- 0:03 "MODAL · BLOCKS EVERYTHING": a dashboard dims and blurs, a centred "Delete account?" dialog appears with Cancel / Delete.
- 0:07 A side card "× DON'T · 12-field signup modal" appears next to the phone.
- 0:11 Checklist builds: ✓ Destructive actions, ✓ Critical confirmations, × Forms longer than 3 fields.
- 0:13 "BOTTOM SHEET · MOBILE-FIRST OVERLAY": over a "Library" screen a "Filters" sheet slides up to partial height; genre chips, Sort by options, "Apply filters" button.
- 0:16 Cursor grabs the drag handle and pulls the sheet up to a taller snap point.
- 0:19 Checklist: ✓ Mobile-first, ✓ Swipeable, ✓ Partial heights.
- 0:21 "DRAWER · EDGE-ANCHORED PANEL": side panel slides in from the left with profile and nav items (Home active, Projects, Settings, Team, Logout); main content remains visible on the right.
- 0:27 Checklist: ✓ Settings & navigation, ✓ Edge slide-in, ✓ Background stays alive.
- 0:29 "POPOVER · ANCHORED, CONTEXTUAL": "⋯" opens Edit / Duplicate / Delete (Delete in danger style); filter icon opens a STATUS checklist under the trigger; bracket "max 200px".
- 0:36 Checklist: ✓ Anchored to trigger, ✓ Tiny, under 200px, ✓ Contextual actions.
- 0:38 "Picking the right overlay · One question fixes 90% of mistakes." Decision tree builds: "Does it block the user?" YES → MODAL; NO → "Mobile or contextual?" → SHEET (mobile), POPOVER (anchored), DRAWER (side nav).
- 0:45 Four icons: MODAL, SHEET, DRAWER, POPOVER; "Save this for your next overlay."

## Voice-over summary
- Five overlays exist and most apps choose wrong; modals block everything.
- Use modals for destructive actions, confirmations and critical decisions, never for forms longer than three fields.
- Bottom sheets are mobile-first, swipeable and partial height: good for filters, options and contextual actions on phones.
- Drawers slide from the edges for settings, navigation and secondary content while keeping the main view alive; popovers anchor to a trigger (tooltips, menus, filters) and should stay under 200 pixels wide.
- One question fixes most mistakes: does it block the user? If yes, modal; if no, sheet, drawer or popover.

## Notes for the skill
- The hook promises five overlays but only four are explained; the fifth shape (a small bar at the bottom) is never named (likely a toast/snackbar). Tooltips are folded into "popover" by the voice-over, which conflicts with APG: a tooltip is non-interactive, appears on hover/focus, and uses `role="tooltip"` + `aria-describedby`; a popover/menu is interactive and opened by click.
- Modal: native `<dialog>` with `showModal()` or `role="dialog"` + `aria-modal="true"`, `aria-labelledby`; trap focus, return focus to the trigger on close, close on Esc; for destructive confirmations consider `role="alertdialog"` and put initial focus on the least destructive action (Cancel). Lock background scroll and make the background `inert`.
- Non-modal overlays (drawer as nav, popover) must not trap focus; close on Esc and outside click; return focus to the trigger. Menus follow the APG menu button pattern (`aria-haspopup`, `aria-expanded`, arrow-key navigation).
- Bottom sheet: provide a visible close/Done in addition to swipe (swipe-only dismissal is not accessible); snap points (e.g. partial and full) should be keyboard-operable; respect safe-area insets; keep the primary action reachable at the bottom. A drawer that dims the page and blocks it is modal in behaviour, so treat it with modal semantics in that case.
- Popover width "under 200px" is a heuristic; content like date pickers or rich filters legitimately exceed it. The real rule: popover stays small relative to the viewport, positions itself against the trigger with collision handling (flip/shift), and switches to a sheet on small screens if content grows.
- "Never forms longer than 3 fields in a modal" is a rule of thumb; if a modal form is unavoidable, protect against data loss on accidental dismiss (confirm-discard or persisted draft).
- Use the danger colour only for the destructive button; scrim opacity should dim but keep context recognisable; animate overlays with transform/opacity and honour `prefers-reduced-motion`.
