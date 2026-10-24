---
id: DdLvXSsNLpr
reel_url: https://www.instagram.com/reel/DdLvXSsNLpr/
pattern_page: https://designmotionhq.com/patterns/reverse-engineered-linear
date: 2026-09-12
duration_s: 82
type: ui
category: visual
topic: why a dense productivity UI feels premium (density, borders, one accent, shortcuts and fast motion, alignment)
sources: frames, voice-over, pattern page
---

# Reverse-engineered "expensive" app UI: five decisions

**Caption:** Why Linear feels expensive. Five decisions, none need a designer. Same defaults for your app: UX Engine, link in bio. motiondesign
**Hook:** A well-known issue tracker feels expensive because of five decisions, none of which need a designer.

## Main rule
For a dense productivity UI: use small text and tight rows (13px / 32px, letter spacing -0.01em), build depth from three background values plus a 1px low-opacity border instead of shadows, reserve the single accent colour for the selected row and the primary button, show a keyboard shortcut for every action with hover feedback near 80 ms and transitions at most 150 ms without overshoot, and align everything to a 4px grid (16px icons centred on the text line, labels left, numbers and dates right).

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 5 | decisions (Density, Borders, One color, Keyboard, Alignment); counter "0 / 5" to "5 / 5 decisions" | 0:00-0:04 on-screen + voice |
| 13px | list text size ("13 px text") | 0:06-0:16 on-screen + voice |
| 32px | row height ("32 px" bracket on a row) | 0:08-0:16 on-screen + voice |
| -0.01em | letter spacing (from 0em; voice "pulled in 1%") | 0:09-0:16 on-screen + voice |
| 8 → 14 rows | visible issues in the same viewport before / after; caption "14 rows, same height" | 0:05-0:16 on-screen; voice says "twice the issues"; page says 14 instead of 8 |
| 3 background values | canvas (background), list (surface1), hover (surface2), increasing in lightness | 0:17-0:32 on-screen token table + voice |
| `box-shadow: none` | rows, panels, sidebar | 0:17-0:32 on-screen chip |
| 1px border at 8% | hairline: 1px solid, light foreground colour at 0.08 alpha on a dark theme | 0:20-0:24 on-screen callout + voice; page "1px border at 8%" of the foreground |
| elevation 0 · surface2 | row hover state: background moves to the next surface value, elevation unchanged | 0:25-0:32 on-screen callout |
| 7 → 2 → 1 colours | palette count as status pills are replaced by icons and everything else turns grey | 0:33-0:44 on-screen counter |
| 1 | accent colour, used on the selected row and the primary button only | 0:33-0:44 on-screen "1 brand color · icons for status" + voice |
| C / ⌘K | create issue / search (command palette) | 0:45-0:59 on-screen keycaps + voice |
| P, C, I, ⌘K, ⌘B | shortcuts printed in the palette: Set priority, Create issue, Assign to me, Search, Toggle sidebar; F and a key on Filter / Display buttons; C badge on "New issue" | 0:48-0:59 on-screen |
| 80 ms | hover feedback | 0:45-0:59 on-screen meter + voice; page "about 80ms" |
| 150 ms | maximum transition duration ("150 ms max") | 0:45-0:59 on-screen meter + voice; page "under 150ms" |
| 300 ms | "generic" transition duration, struck through (rejected) | 0:45-0:59 on-screen meter |
| 0 overshoot | "bouncy" slider rejected, "snappy" selected | 0:45-0:59 on-screen + voice ("no bounce, no overshoot") |
| 4px grid | spacing / alignment base | 0:60-0:70 on-screen chip + voice |
| 16px | icons, "16 px · centered" on the text line | 0:62-0:70 on-screen + voice |
| x2.4 | zoom of the "loupe · one row" inspection view (presentation detail, not a design value) | 0:60-0:70 on-screen |

## Before / after
The video starts from a generic version of the same issue list and applies one decision at a time.
- **Density:** Before: larger text, roomy rows, about 8 issues visible (header still says 14), letter spacing 0em. After: 13px text, 32px rows, -0.01em tracking, all 14 issues visible without scrolling. Why: in a work tool, more items per screen means less scrolling and easier comparison; tight, even rhythm reads as a tool for experts ("density reads as competence").
- **Borders, not shadows:** Before: rows and panels separated by shadow / heavier treatment. After: `box-shadow: none`, three stacked background values (canvas, list surface, hover surface) and a 1px hairline at 8% foreground; hovering a row only shifts its background to the hover surface ("elevation 0 · surface2"). Labels "engineered" (kept) vs "decorated" (struck). Why: value steps create layering without blur, which stays crisp at small sizes and keeps the page calm; hover via surface value gives feedback without anything appearing to lift.
- **One colour:** Before: seven colours (coloured status pills such as In progress / Todo / Done, coloured priority words, coloured label chips, underlined accent links). After: status and priority shown as grey icons, labels grey, links plain text; the accent appears only on the selected row and the "New issue" button. Counter 7 → 2 → 1 colours. Why: when colour is rare it becomes a reliable pointer to "selected" and "primary action"; many colours compete and the UI reads as noisy.
- **Keyboard and motion:** Before: generic 300 ms transitions and a bouncy feel. After: every action shows its shortcut, C opens create, ⌘K opens a command palette that filters as you type ("pri" → "Set priority"); hover feedback 80 ms, transitions capped at 150 ms, no overshoot ("snappy"). Why: visible shortcuts teach the fast path in place; very short, non-bouncing transitions make the UI feel like it responds before the gesture finishes.
- **Alignment:** a magnified single row shows the status icon 16px and vertically centred on the text line, ID and title anchored left, date anchored right, marked "aligned". Why: consistent anchors form invisible columns; alignment is unnoticed when right and conspicuous when off.

## Do
- For dense desktop lists: about 13px text, 32px rows, letter spacing -0.01em.
- Separate surfaces with 2-3 background value steps and a 1px border at low opacity (about 8%) instead of shadows.
- Implement row hover as a background-value change, not an elevation change.
- Use the accent colour only for the selected item and the primary action; keep status and priority in neutral icons.
- Print the keyboard shortcut next to every action (buttons, menu and palette items); provide a Cmd / Ctrl K palette.
- Hover feedback around 80 ms; all transitions at most 150 ms; no bounce or overshoot.
- Use a 4px spacing grid, 16px icons centred on the text line, labels left-aligned, numbers and dates right-aligned, nothing centred in rows.

## Don't
- Don't use drop shadows to separate rows, panels or the sidebar.
- Don't encode status or priority with coloured pills when an icon can carry it.
- Don't spread the brand colour across links, labels and badges.
- Don't use 300 ms generic transitions or springy overshoot in a work tool.
- Don't centre labels or numbers in table rows.

## Scene by scene
- 0:00 Label "Reverse-engineered · [the issue tracker]". Generic issue list (coloured status pills, coloured priorities, underlined links, roomy rows); chips Density, Borders, One color, Keyboard, Alignment; counter "0 / 5 decisions".
- 0:01 A scan line sweeps the list and turns it into the refined version; chips light up, counter goes 2 / 5 then 5 / 5; title "Five decisions. No designer."
- 0:05 "Decision 01 · Density / Density reads as competence." Callout "13 px text" (0:06), row bracket "32 px" (0:08); rows compress; letter-spacing card "Migrate billing webhooks to v2" changes 0em → -0.01em (0:09); caption "14 rows, same height"; chip "13 px · 32 px rows · -0.01em".
- 0:17 "Decision 02 · Borders / Borders, not shadows." Token table canvas / list / hover (background, surface1, surface2); chip "box-shadow: none · 1px at 8%"; 0:20 callout on a row divider showing the 1px border at 8% foreground alpha.
- 0:25 Cursor hovers a row: callout "elevation 0 · surface2"; 0:29 "engineered" check vs "decorated" struck.
- 0:33 "Decision 03 · One color / One color. Everything else grey." Counter "7 colors" with the palette swatches; 0:38 status pills become icons; 0:41 swatches turn grey one by one, counter "2 colors", then "1 color" (only the accent remains on the selected row and the primary button). Chip "1 brand color · icons for status".
- 0:45 "Decision 04 · Keyboard / The UI answers first." Keycaps C (create) and ⌘K (search); timing meters hover 80 ms, transition 150 ms, generic 300 ms; sliders "bouncy" vs "snappy". 0:48 "New issue" button shows its C shortcut.
- 0:49 Command palette "Type a command" with Set priority P, Create issue C, Assign to me I, Search ⌘K, Toggle sidebar ⌘B; 0:50 typing "pri" leaves "Set priority". 0:52-0:59 meters fill to 80 / 150, 300 ms struck, "bouncy" crossed out, "snappy" kept. Chip "80 ms hover · 150 ms max · 0 overshoot".
- 0:60 "Decision 05 · Alignment / Invisible when right." Loupe on one row "NOR-147 Bulk edit for labels ... Sep 4": "16 px · centered" icon, "left" and "right" anchors, then "aligned". Chip "4 px grid · 16 px icons · numbers right".
- 0:71 "Five decisions, one afternoon."; 0:72-1:21 advertisement for the author's paid plugin (terminal slash commands, product card, "Link in bio"); not part of the pattern.

## Voice-over summary
- The app feels expensive because of five decisions that need no designer.
- Density: 13px text, 32px rows, letter spacing pulled in 1%, roughly twice the issues on one screen with no scroll; "density reads as competence".
- Borders: no shadows, a 1px border at 8% foreground alpha, depth from three background values; hover changes the surface value, not elevation; flat looks engineered, shadows look decorated.
- One colour: the accent only on the selected row and the primary button; status is an icon, not a coloured pill; everything else grey.
- Keyboard and motion: every action shows its shortcut (C creates, Cmd K searches), hover feedback in 80 ms, transitions under 150 ms, no bounce; alignment on a 4px grid with 16px icons centred, labels left, numbers right, nothing centred. Ends with a plugin advertisement.

## Notes for the skill
- Tokens, colour-independent: `--bg-canvas`, `--bg-surface-1`, `--bg-surface-2` as three steps of the theme's neutral scale; `--border-hairline: 1px solid color-mix(in srgb, var(--fg) 8%, transparent)`. In a light theme the same idea uses darker steps and a dark hairline at low alpha.
- The hairline at 8% is decorative separation; it fails 3:1 non-text contrast, which is acceptable only if it is not the sole indicator of a component boundary users must perceive (WCAG 1.4.11 applies to UI component boundaries needed to identify them). Selected and focused rows need a stronger indicator than the surface step: a visible focus ring with at least 3:1 contrast (WCAG 2.4.7 / 2.4.11).
- Hover as surface change: the difference between surface1 and surface2 is subtle; it is fine for hover (non-essential), but selection must not rely on it alone. The video uses the accent for selection, which is correct.
- Status as grey icons: icons must differ in shape (not only fill) so status survives without colour (WCAG 1.4.1), carry an accessible name (`aria-label` or visually hidden text), and keep at least 3:1 contrast against the row.
- 13px text and 32px rows suit pointer-driven desktop density; on touch layouts rows need at least 44pt / 48dp targets (WCAG 2.5.8 minimum 24 x 24 CSS px). Offer a density setting rather than hard-coding compact for everyone; respect user font-size scaling (use rem, so 13px = 0.8125rem).
- Negative letter spacing (-0.01em) should only be applied to small UI text in fonts designed for it; WCAG 1.4.12 requires that content still works if users override spacing.
- Shortcut display: render with `<kbd>`, show the platform-correct modifier (⌘ on macOS, Ctrl elsewhere), expose via `aria-keyshortcuts`. Single-key shortcuts (C, P, I) must be disableable or remappable, or only active when focus is on the component (WCAG 2.1.4 Character Key Shortcuts), and must not fire while typing in inputs.
- Motion: hover in about 80 ms, other transitions at most 150 ms, ease-out, no overshoot; under `prefers-reduced-motion: reduce` drop non-essential movement and keep opacity / colour changes.
- Alignment: numeric columns should use `font-variant-numeric: tabular-nums` and right alignment so digits line up; icons 16px on a 4px grid aligned with `align-items: center` to the text line box.
- The video names a specific product and its brand colour; the skill should keep the transferable rule (single accent used twice) and take the actual colour from the project theme.
