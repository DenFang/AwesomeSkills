---
lesson: 059
kind: video
duration_s: 52
type: ui
category: navigation
topic: command palette (Cmd+K): fuzzy match, grouping, keyboard, empty state, async, nesting
sources: frames, voice-over, lesson notes
---

# Command palette: five rules that make Cmd+K fast

**Hook:** Press Cmd+K, type three letters, jump anywhere; a command palette is not a search box.

## Main rule
A command palette must match fuzzily (subsequence, matched letters highlighted), show results grouped by type (Recent, Actions, Pages), be fully operable by keyboard (arrows, Enter, Esc), open with recent commands instead of an empty list, keep itself open with an inline spinner while an async command loads, and support nested sub-menus where Esc goes back one level.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| Cmd + K | open shortcut | 0:00 on-screen key caps + voice |
| 3 letters ("stg") | query length that should already find the target | 0:01 voice, 0:01-0:09 on-screen |
| Group order: Recent, then Actions, then Pages | result section order | 0:13 voice, 0:11-0:17 on-screen |
| 3 recent items (Open settings, Deploy staging, New document) | prefilled empty state | 0:28-0:33 on-screen |
| "3" count badge on "Switch project..." | number of loaded sub-results after async fetch | 0:37-0:39 on-screen |
| Cmd + , (Settings), Cmd + D (Toggle dark mode) | inline shortcut hints on rows, right-aligned | 0:03, 0:20 on-screen (small key caps, read from single frames) |
| 1 level | how far Esc goes back in a nested menu | 0:44 voice, 0:46 on-screen |
No durations or pixel values are shown.

## Before / after
- **Exact match vs fuzzy match.** Exact substring search for "stg" returns "No results" (the panel even notes that "stg" is not "Settings"). Fuzzy subsequence matching returns Settings, Storage, Staging with the matched letters (S, t, g) highlighted. It works because users type abbreviations of what they mean; highlighting shows why each row matched, so the result feels trustworthy rather than random.
- **Flat list vs grouped.** A flat list of six mixed items (Open settings, Profile page, Deploy staging, New document, Search files, Docs home) forces reading every row. The grouped version puts the same items under small labelled headers (Recent, Actions, Pages), so the eye jumps to the right section first. Structure reduces scanning, which is what makes the palette feel fast.
- **Blank void vs recent commands.** An empty palette shows a "No results" placeholder with nothing to select. The good one opens with a "Recent" section of three commands and the first one already highlighted, so Enter works immediately. It removes the cold-start problem: the user can act before typing.
- **Frozen screen vs inline spinner.** Running "Switch project..." shows a spinner on that row only; the palette stays open and the three projects (marketing-site, design-system, api-gateway) load in place under a "Projects" header. The bad version puts a full-screen spinner with "Whole app blocked". Inline loading keeps context and lets the user keep navigating; a global block makes one network call cost the whole UI.
- **Nested commands.** "Change theme" has a chevron; selecting it replaces the list with Light, Dark, System and shows a "Change theme" chip (breadcrumb) in the input. Esc removes the chip and returns to the parent list with "Change theme" still highlighted, instead of closing the palette. This preserves place and makes deep commands cheap to explore.

## Do
- Match queries as fuzzy subsequences and highlight the matched characters in each result.
- Group results under labelled sections; order Recent, Actions, Pages.
- Highlight the first result by default so Enter runs it.
- Support Up/Down to move, Enter to run, Esc to close, with visible key hints.
- Show right-aligned shortcut hints on rows that have a global shortcut.
- Prefill the empty state with recent (or suggested) commands.
- For commands that fetch data, show a spinner on that row and load results in place, keeping the palette open; show a count when results arrive.
- Mark rows that open a sub-menu with a chevron; show the current level as a chip/breadcrumb in the input.
- Make Esc go back exactly one level in nested menus, and restore the highlight on the parent item.

## Don't
- Don't require exact substring matches.
- Don't dump all results as one flat list.
- Don't open to a blank "No results" state.
- Don't block the whole app with a global spinner while one command loads.
- Don't make Esc in a sub-menu close the whole palette.
- Don't make any step require the mouse.

## Scene by scene
- 0:00 Key caps Cmd + K, an empty palette ("Type a command or search...") fades in.
- 0:01 User types "stg"; results Settings (highlighted, with Cmd + , hint), Storage, Staging deploy, Settings docs. Caption: Cmd+K, type, jump anywhere.
- 0:04 "Fuzzy matching": "stg -> Settings" with matched letters highlighted in Settings, Storage, Staging. Caption: type less, find more.
- 0:08 Split: "Exact match" panel shows "No results" vs "Fuzzy match" panel with three hits. Caption: match the intent, not the string.
- 0:11 "Group your results: Flat list -> Grouped". A "Jump to..." palette with six flat rows.
- 0:13 Rows regroup under Recent (Deploy staging, Search files), Actions (Open settings, New document), Pages (Profile page, Docs home); each header pulses in turn. Caption: structure makes it fast.
- 0:18 "Hands off the mouse": key caps Up, Down, Enter, Esc; list "Navigate with arrows..." (Open settings, Deploy staging, Toggle dark mode with Cmd + D hint, New document, Profile page). The highlight moves down row by row as the Down cap lights up. Caption: arrows move, Enter runs.
- 0:22 Enter cap lights on "New document"; then the Esc cap lights and the palette fades out. Caption: Escape closes.
- 0:26 "Empty state": "Blank void" palette (search icon, "No results") vs "Recent commands" palette with Recent: Open settings (highlighted), Deploy staging, New document. Caption: give people a starting point.
- 0:34 "Async commands": query "switch", Command section "Switch project..." gets an inline spinner; caption: spinner inline, palette stays open.
- 0:37 Results load in place: count "3" on the row, Projects: marketing-site, design-system, api-gateway. Caption: results load in place.
- 0:38 Beside it a "Frozen screen" panel: full spinner, "Whole app blocked". Caption: spin inline, never freeze the screen.
- 0:40 "Nested commands": list Open settings, Change theme (chevron), Notifications (chevron). "Change theme" selected; list becomes Light, Dark, System with a "Change theme" chip in the input. Caption: one command opens another.
- 0:45 Hint "Esc: back one level"; chip disappears and the parent list returns with Change theme still highlighted. Caption: Escape walks back one level.
- 0:48 Outro: palette with query "follow" (Follow row, Save this video row) and a Save button.

## Voice-over summary
- Cmd+K plus three letters should get you anywhere; it is not a plain search box.
- Fuzzy matching with highlighted letters lets "stg" find Settings.
- Never show one flat list: group results, recent first, then actions, then pages; structure is what makes it fast.
- Fully keyboard: arrows move, Enter runs, Escape closes, so a power user can cross the app without the mouse.
- Opened empty, most palettes show nothing; show recent commands instead.
- Async commands spin inline and keep the palette open; nested commands drill into submenus and Escape goes back "one level, not all the way out".

## Notes for the skill
- ARIA (WAI-ARIA APG combobox pattern): input with `role="combobox"`, `aria-expanded`, `aria-controls` pointing at a `role="listbox"`; rows `role="option"` with `aria-selected`; keep DOM focus in the input and move the virtual highlight with `aria-activedescendant`. Group sections as `role="group"` with `aria-labelledby` on the header (headers must not be focusable options). The palette container is a modal dialog (`role="dialog"`, `aria-modal="true"`, labelled), with focus trapped inside and returned to the previously focused element on close.
- Announce result counts and async state through a polite live region (e.g. "3 projects loaded"), and set `aria-busy="true"` on the listbox while fetching.
- Shortcut: use Cmd+K on macOS and Ctrl+K on Windows/Linux; avoid hijacking the shortcut while focus is in a text editor that uses it. Also provide a visible button to open the palette for mouse/touch users and for discoverability.
- Fuzzy ranking: rank prefix and word-start matches above scattered subsequence matches, then by recency/frequency; render highlights with `<mark>` or a span, but keep the accessible name as the plain label.
- Arrow keys: consider wrap-around at the ends, Home/End, and PageUp/PageDown in long lists; keep the highlighted row scrolled into view.
- Nested level: Backspace in an empty input is a common secondary way to go up one level. Esc at the root closes the palette.
- Async: debounce remote queries, cancel stale requests, and keep the previous results visible (not cleared) while new ones load to avoid flicker. If the fetch fails, show the error inline in the palette.
- Highlight and selection state must not rely on colour alone (the video uses a left bar plus a background change; keep a shape/weight cue) and must meet 3:1 non-text contrast.
- On touch devices a Cmd+K palette is secondary; ensure rows are at least 44x44 px targets if it is exposed there.
