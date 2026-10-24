# Data display

Tables, lists, numbers, search, filters and charts. Data UI looks cheap when it is a grid of divs with default text; it looks engineered when alignment, density and state are decisions.

Severity: **P0** misleads or hides data, **P1** friction, **P2** polish.

---

### DAT-1 · Numbers are a system (P1)
**Applies to.** numbers shown in columns, counters, prices, stats, timestamps.
**Rule.** Any column, counter, price or live value uses tabular figures (`font-variant-numeric: tabular-nums`) so digits share one width and nothing wobbles. Numbers right-aligned, with their column header aligned the same way; text left-aligned. Large values abbreviate in tiles (1.2K, 3.4M) with the exact value on hover or in a tooltip. Times under a day are relative ("2h ago"), older are absolute ("Mar 3"). In columns, the currency symbol is pinned, decimals are consistent and the amounts align on the decimal. Format with `Intl.NumberFormat` / `Intl.DateTimeFormat` for the user's locale.
**Detect.** Numeric columns left- or centre-aligned; proportional digits in tables or counters; hand-rolled formatting with string concatenation.

### DAT-2 · Table: six decisions (P1)
**Applies to.** tables and data grids.
**Rule.**
1. **Align**: numbers right with tabular figures, headers aligned like their column, text left, nothing centred except icons.
2. **Rows**: one hairline and a hover tint. Compact rows never get stripes; subtle zebra stripes are acceptable only at comfortable or spacious density or on very wide tables (about 12+ columns).
3. **Density**: row height is a token with three values (about 36 compact, 48 comfortable default, 60 spacious), set on the table root and switched by one control; let the user or role pick and persist the choice. Compact rows are below a touch target, so offer them on fine pointers or keep the hit area taller than the row.
4. **Sticky**: header pinned on vertical scroll, identity column pinned on horizontal scroll, each with a soft shadow that appears only while content is under it.
5. **Cells**: missing values show a dash, never blank; long text truncates with a tooltip; numbers never truncate; one line per row.
6. **Actions**: no column of repeated pencils and bins; reveal row actions on hover and focus, keep a menu button on touch.
Use semantic `<table>` markup (or a full ARIA grid when cells are interactive), not divs. Sorting is DAT-3, selection DAT-4.
**Detect.** `<div>` grids pretending to be tables; centred numbers; blank cells; per-row icon clutter; header scrolling away; row heights hard-coded per screen instead of a density token; stripes on compact rows.

### DAT-3 · Sorting is tri-state and visible (P1)
**Applies to.** sortable tables and lists.
**Rule.** Clicking a header cycles ascending, descending, then back to the original order with no arrow, because the natural order (insertion, date) often carries meaning. The header label is a `<button>` inside the `<th>`; show the sort arrow only on the active column, and put `aria-sort="ascending"`/`"descending"` on that column alone. Rows that animate to their new positions reorder instantly under reduced motion.
**Detect.** Two-state toggles that lose the natural order; arrows on every column; click handlers on bare `<th>` elements.

### DAT-4 · Selection is application state (P1)
**Applies to.** lists or tables with multi-select, header select-all checkboxes, selection bars.
**Rule.** The header checkbox has three states (empty, an indeterminate dash for any partial selection, checked) and clicking the dash selects all, never clears; set `input.indeterminate` (or `aria-checked="mixed"`). The whole row is the selection target, not only the tiny checkbox, and a selected row shows redundant cues (tint, a leading accent bar and the tick, never tint alone) while the real checkbox, labelled with the row's name, remains the accessible control; if a row click also opens details, give details their own link. Shift-click selects the inclusive range from the last clicked row in the current sort order (Shift+Space or Shift+Arrow in grids). Selected IDs live in app state and survive paging, filtering and virtualisation. A selection bar shows "N of M selected" with Clear selection, announced politely. When select-all covers only the visible page, say so and offer "Select all 247 matching" with the true count (store it as a query-scoped flag plus excluded IDs, not every ID). When filters change, keep the IDs that still match and update the count live; never act on rows that no longer match without saying so.
**Detect.** Two-state header checkboxes; selection stored in DOM checkboxes; selection lost on page change; "Select all" that silently means "this page"; checkbox-only row selection.

### DAT-5 · Bulk actions run and offer undo (P1)
**Applies to.** bulk actions on selections and their selection bars.
**Rule.** Bulk actions echo the count in the button ("Delete 247", "Archive 12 projects") and in the result ("247 members deleted"), run immediately and offer an undo of about 10 s with a draining countdown instead of a confirm dialog, which gets clicked through and still offers no way back. That only works when the action is really reversible (soft delete, or a commit deferred until the window closes); the undo pauses while hovered or focused, stays keyboard reachable, is also offered in a "Recently deleted" view (STA-14), and is styled neutral or accent, not danger. After the action, the emptied or reduced view says what happened ("247 removed a moment ago"). Irreversible bulk actions (permanent purge, external side effects) still need explicit confirmation that states the count (INT-9).
**Detect.** "Are you sure?" modals before reversible bulk actions; bulk buttons without the count; undo toasts that auto-dismiss while focused.

### DAT-6 · Tables on narrow screens become rows, not tiny tables (P1)
**Applies to.** tables shown on narrow screens or in narrow containers.
**Rule.** Do not shrink a wide table or scroll it sideways on a phone. Rank columns by use: identity and value first, state second, the rest hidden. Each row becomes two lines (name left, amount right, state and secondary info below), amounts stay in one right-aligned tabular slot, ambiguous values get labels ("Due Mar 04"). Hidden columns are one tap away (expand or sheet), not on a new page. Let the table switch on its own width: give its wrapper `container-type: inline-size`, then use `@container (max-width: 700px)` rather than a viewport media query.
**Detect.** `overflow-x: auto` tables with six or more columns on mobile; font-size reduced to fit.

### DAT-7 · Pagination is stable and restorable (P1)
**Applies to.** paginated or infinitely loaded lists, pagers, "Load more" buttons.
**Rule.** Choose by job: numbered pages for tables people jump around in (with a "Go to page" input for large counts), "Load more" for user-paced lists, infinite scroll only for feeds, and then keep the footer reachable. Offset pagination drifts on live data: one insert shifts every page and shows an item twice, a delete skips one. Use cursor (keyset) pagination, ordered by a unique indexed key with opaque cursor tokens, for live lists, feeds and "Load more"; keep offset with jump-to-page only where data is mostly stable, or pin it to a snapshot ("created before" the first load). Truncate the pager to about seven cells: first, gap, current with its neighbours, gap, last, plus previous/next; on phones drop the neighbours or show "Page 500 of 833". Keep the page or cursor in the URL (`?page=500`, `?after=…`) so refresh, back and shared links keep the view. Mark it up as `<nav aria-label="Pagination">` with real links, `aria-current="page"`, named previous/next and non-interactive ellipses. After a page change move focus to the top of the results or announce "Page N of M"; after "Load more" announce how many items arrived and focus the first new one.
**Detect.** Offset pagination on live data; pagers with every page number; page held only in component state; pager buttons without `aria-current`; page changes that leave focus on the pager in silence.

### DAT-8 · Scroll position is state (P1)
**Applies to.** long lists with detail views, pages with sticky headers and anchors.
**Rule.** Returning from a detail view puts the user back where they were in the list, with the row they opened briefly highlighted. With client-side routing, save the scroll position per history entry together with the loaded count or cursor, and restore it only after the data has rendered (earlier lands in the wrong place), offsetting for sticky headers. Anchors get `scroll-margin-top` equal to the sticky header height.
**Detect.** Back navigation landing at the top of long lists; scroll restored before the list data arrives; anchor targets hidden under sticky bars.

### DAT-9 · Truncation never breaks the layout (P1)
**Applies to.** every text slot filled with user or database content.
**Rule.** Every user or database string will one day be empty, one character, or very long with an emoji. Use `min-width: 0` on flex children so ellipsis can work; truncate in the middle when both ends carry meaning (file names, emails); use `overflow-wrap: anywhere` so a long URL cannot burst its container; give the full value in a tooltip or title. Test each text component with empty, one-character and long fixtures.
**Detect.** `text-overflow: ellipsis` inside flex items with no `min-width: 0`; long tokens overflowing cards; file extensions cut off.

### DAT-10 · Filters show their logic and their effect (P1)
**Applies to.** filter chips, faceted filters and active-filter bars.
**Rule.** Chips have three distinct states: idle (surface and border), active (accent fill plus a check, never colour alone; text 4.5:1 on the fill, chip edge 3:1 against the page), and disabled when they would return nothing (prefer `aria-disabled` with the zero count shown, so the option stays discoverable). A toggle chip is `<button aria-pressed>`; an exclusive group is a radio group. Options combine with OR inside a group and AND across groups; make it visible whether a tap widened or narrowed the set. The result count updates on the same frame as the tap, because a silent tap gets tapped again and toggles off; with server results, flip the chip at once and show a pending count rather than freezing the old number, and announce the count politely with a debounce. One "Clear all" beside the active-filter count resets everything, is hidden or inactive at zero, and leaves focus on the count or first chip. On phones, chips sit in one horizontally scrolling row with an edge fade and end padding so the last chip can clear the fade; a wrapped wall of chips buries the results. Active filters stay pinned in a sticky bar of removable chips with the count, so users see why the list shrank.
**Detect.** Active and idle chips that look alike or differ only by colour; result counts that update late or never; no clear-all; `flex-wrap: wrap` on mobile chip rows; chips built from `<div>` without `aria-pressed`.

### DAT-11 · Search is five parts (P1)
**Applies to.** search inputs, autocomplete suggestion lists and search results.
**Rule.** A real label (visible or `aria-label`) plus a placeholder that says what can be searched ("Search by name, SKU or brand"); the placeholder is a hint, never the only label. On focus with an empty field, show recent searches (about five, one tap fills and runs, each removable plus clear-all, never in shared contexts without consent). Autocomplete keeps prefix matches, ranks by real usage (with a fallback before usage data exists), highlights the matched part, tags each row with a category or scope, and stays short enough to scan without scrolling (about 3 to 8 rows). Use the combobox pattern: `role="combobox"` with `aria-expanded` and `aria-controls` pointing at a listbox, `aria-activedescendant` for the highlighted option, Up/Down move, Enter selects, Escape closes, visible focus on the input and a non-colour cue on the active option, and the suggestion count in a polite live region. Debounce requests by about 150 to 300 ms, cancel stale ones and keep previous results visible while fetching. Zero results keep the query visible and editable and offer a way on: "Did you mean", popular searches, a category to browse, recently viewed items.
**Detect.** "Search…" as the only placeholder or label; empty dropdown on focus; suggestions sorted alphabetically; zero-results dead ends; requests per keystroke.

### DAT-12 · Command palette is a system (P2)
**Applies to.** command palettes and quick switchers.
**Rule.** Open with Cmd+K (Ctrl+K off macOS) and a visible button. Never empty on open: recent commands with the first one highlighted, so Enter works before typing. Match fuzzy subsequences ("stg" finds Settings), rank prefix and word-start matches above scattered ones and then by recency, and highlight the matched characters (`<mark>`, keeping the plain label as the accessible name). Group results under labelled sections (Recent, then Actions, then Pages), using `role="group"` labelled by a header that is not selectable. Keyboard-first: arrows move with the highlight scrolled into view, Enter runs, Escape closes; rows with a global shortcut show it right-aligned. Async commands keep the palette open with a spinner on that row only and load results in place with a count (`aria-busy` on the list, a polite announcement, errors inline), never a full-screen block. Rows that open a sub-level carry a chevron; the current level shows as a chip in the input, and Escape (or Backspace in an empty input) goes back exactly one level with the parent row still highlighted. Build it as a modal dialog holding a combobox and listbox with `aria-activedescendant`. It accelerates visible navigation; it never replaces it.
**Detect.** Exact substring filtering (`label.includes(query)`); one flat result list; a blank palette on open; a global spinner while one command loads; Escape closing the palette from a sub-level.

### DAT-13 · Charts tell the truth (P0)
**Applies to.** charts and graphs.
**Rule.** The visual change must equal the data change. Bar, column and area axes start at zero, no exceptions; a line chart may start elsewhere when the variation is the message, with visible tick labels. The question picks the form: bars compare, lines show change over time, pies only with about five slices or fewer (sorted, from 12 o'clock), otherwise a sorted bar chart. Proportion line charts so the average slope sits near 45°, neither squashed flat nor stretched into a spike. Remove non-data ink (heavy gridlines, 3D, shadows, boxed legends) and label series at the line end, keeping a legend or small multiples when labels would collide. Spend colour on meaning: one accent on the value that carries the message against neutral others; categorical scales for groups, sequential for magnitude, diverging around a meaningful midpoint, varying lightness and not only hue; data marks keep 3:1 against their neighbours. Title the chart with the takeaway ("Revenue flat since March"). Never encode a series by colour alone, and give the chart a text alternative stating the takeaway (`<figure>` with `<figcaption>`, or `role="img"` with a label) plus the values as a table. Animated axis changes respect reduced motion.
**Detect.** Truncated bar baselines (`beginAtZero: false`, a domain minimum above 0); pies with many slices; a different hue on every bar; rainbow series; 3D charts; generic metric titles.

### DAT-14 · Dashboards lead with the number that matters (P1)
**Applies to.** dashboards and metric tiles.
**Rule.** One primary metric, larger, with its breakdown; secondary metrics smaller. Each number has a shape: a delta with a unit and a comparison period ("+12.5% vs Jul"), or a sparkline. Title the page by what it shows ("Revenue · Aug 1–31"), not a greeting. No icon tiles competing with the numbers. See CON-6 for the other generated-dashboard tells.

### DAT-15 · Avatars are a system (P2)
**Applies to.** avatars and user identity chips.
**Rule.** Fallback chain: image, then initials from the name, then a generic icon; never a broken image. Background colour derives from a hash of the user ID, picked from a fixed set of the project's tokens that pass contrast with the initials, so the same person looks the same everywhere. Two initials by default, one at very small sizes. Groups overlap and cap with "+N". Presence is shown on the avatar ring, once. Three size tokens only.

### DAT-16 · Chat threads keep the reader in place (P1)
**Applies to.** chat, messaging and comment threads.
**Rule.** Group consecutive messages from one sender within a short window (about 2 min) under one avatar, tight inside a group and looser between groups. Date dividers instead of timestamps on every row; exact time on hover. The sent message appears instantly and confirms quietly; a failed one stays in place with "Not sent · Retry". When the reader has scrolled up, new messages do not move the viewport; show a "N new messages" pill. Typing indicators live in the message flow. The composer grows to about five lines then scrolls; Enter sends, Shift+Enter adds a line.

### DAT-17 · Ratings are honest (P2)
**Applies to.** star rating inputs, average rating displays and review summaries.
**Rule.** Keep two values: a preview that follows hover, focus or a touch drag, and the committed value. Render the preview when there is one, change the committed value only on click or release, and clear the preview on pointer leave, blur and `pointercancel`, so the display always snaps back to what was saved. Preview half stars only if halves are stored. On commit, fill the stars left to right about 30 ms apart (instantly under reduced motion). Averages render as fractional fills, clipping the last star to the exact fraction (4.4 is four stars and 44% of the fifth, never five), with the number printed beside it; compute summaries from the data and round to one decimal correctly, never in the flattering direction. Summarise with the number (or a ring), the review count and a distribution per star; keep the star row for input. The input is a radio group labelled per value ("4 stars") that arrow keys change; the read-only average has a text alternative ("Rated 4.4 out of 5 from 1,204 reviews") with decorative icons hidden; filled and empty stars differ by more than colour; each star is at least 24 px, ideally 44 px on touch.
**Detect.** `Math.round` or `Math.ceil` on averages before drawing stars; hover writing straight into the saved value; no reset on `pointerleave`/`blur`; star icons with no text value.

### DAT-18 · Calendar week views (P2)
**Applies to.** calendar day and week views.
**Rule.** Open scrolled to the current time, not midnight. Events use a coloured stripe on a faint tint of the event colour instead of a full saturated fill (contrast stays readable). Overlapping events split the column side by side instead of hiding behind "+1 more". Height equals duration with a one-line minimum. Drag on empty space creates an event snapped to 15 minutes; resize from the bottom edge. All-day events live in a pinned row above the grid.

---
Sources: number-formatting, data-table, data-table-system, responsive-table, bulk-actions, pagination, scroll-restoration, text-truncation, filter-chips, search-experience-system, command-palette, charts-that-lie, de-ai-dashboard, avatar-system, chat-ui-system, star-rating, calendar-week-view. See `sources.md`.
