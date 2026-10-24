# Data display

Tables, lists, numbers, search, filters and charts. Data UI looks cheap when it is a grid of divs with default text; it looks engineered when alignment, density and state are decisions.

Severity: **P0** misleads or hides data, **P1** friction, **P2** polish.

---

### DAT-1 · Numbers are a system (P1)
**Rule.** Any column, counter, price or live value uses tabular figures (`font-variant-numeric: tabular-nums`) so digits share one width and nothing wobbles. Numbers right-aligned, text left-aligned. Large values abbreviate in tiles (1.2K, 3.4M) with the exact value on hover or in a tooltip. Times under a day are relative ("2h ago"), older are absolute ("Mar 3"). In columns, the currency symbol is pinned and the amounts align on the decimal. Format with `Intl.NumberFormat` / `Intl.DateTimeFormat` for the user's locale.
**Detect.** Numeric columns left- or centre-aligned; proportional digits in tables or counters; hand-rolled formatting with string concatenation.

### DAT-2 · Table: six decisions (P1)
**Rule.**
1. **Align**: numbers right, text left, nothing centred except icons.
2. **Rows**: one hairline and a hover tint; zebra stripes only for very wide tables (about 12+ columns).
3. **Density**: row height is a token with three values (about 40 compact, 48 default, 56 comfortable); let the user or role pick.
4. **Sticky**: header pinned on vertical scroll, identity column pinned on horizontal scroll.
5. **Cells**: missing values show a dash, never blank; long text truncates with a tooltip; numbers never truncate; one line per row.
6. **Actions**: no column of repeated pencils and bins; reveal row actions on hover and focus, keep a menu button on touch.
Use semantic `<table>` markup (or a full ARIA grid), not divs.
**Detect.** `<div>` grids pretending to be tables; centred numbers; blank cells; per-row icon clutter; header scrolling away.

### DAT-3 · Sorting is tri-state and visible (P1)
**Rule.** Clicking a header cycles ascending, descending, then back to the original order. Show the sort arrow only on the active column, and expose `aria-sort`.
**Detect.** Two-state toggles that lose the natural order; arrows on every column.

### DAT-4 · Selection is application state (P1)
**Rule.** The header checkbox has three states (empty, indeterminate, checked) and partial resolves to select-all. The whole row is the selection target, not only the tiny checkbox. Shift-click selects a range. Selected IDs live in state and survive paging and filtering. When select-all covers only the visible page, offer "Select all 247 matching" with the true count, and keep the count live when filters change.
**Detect.** Selection stored in DOM checkboxes; selection lost on page change; "Select all" that silently means "this page".

### DAT-5 · Bulk actions run and offer undo (P1)
**Rule.** Bulk actions echo the count ("Archive 12 projects"), run immediately and offer an undo of about 10 s with a visible countdown instead of a confirm dialog. Irreversible bulk actions still need explicit confirmation (INT-9).

### DAT-6 · Tables on narrow screens become rows, not tiny tables (P1)
**Rule.** Do not shrink a wide table or scroll it sideways on a phone. Rank columns by use: identity and value first, state second, the rest hidden. Each row becomes two lines (name left, amount right, state and secondary info below), amounts stay in one right-aligned tabular slot, ambiguous values get labels ("Due Mar 04"). Hidden columns are one tap away (expand or sheet), not on a new page. Let the table switch on its own width with a container query (`@container (max-width: 700px)`) rather than the viewport.
**Detect.** `overflow-x: auto` tables with six or more columns on mobile; font-size reduced to fit.

### DAT-7 · Pagination is stable and restorable (P1)
**Rule.** Use cursor pagination when rows can be inserted or deleted (offset pagination shows duplicates and skips). Truncate the pager to first, last, current and neighbours with ellipses. Keep the page in the URL. Choose by job: numbered pages for jumping, "Load more" for on-demand, infinite scroll only for feeds, and then keep the footer reachable.
**Detect.** Offset pagination on live data; pagers with every page number; page held only in component state.

### DAT-8 · Scroll position is state (P1)
**Rule.** Returning from a detail view puts the user back where they were in the list. With client-side routing, save the scroll position per history entry and restore it, offsetting for sticky headers. Anchors get `scroll-margin-top` equal to the sticky header height.
**Detect.** Back navigation landing at the top of long lists; anchor targets hidden under sticky bars.

### DAT-9 · Truncation never breaks the layout (P1)
**Rule.** Every user or database string will one day be empty, one character, or very long with an emoji. Use `min-width: 0` on flex children so ellipsis can work; truncate in the middle when both ends carry meaning (file names, emails); use `overflow-wrap: anywhere` so a long URL cannot burst its container; give the full value in a tooltip or title. Test each text component with empty, one-character and long fixtures.
**Detect.** `text-overflow: ellipsis` inside flex items with no `min-width: 0`; long tokens overflowing cards; file extensions cut off.

### DAT-10 · Filters show their logic and their effect (P1)
**Rule.** Chips have three distinct states (idle, active with a check, disabled when they would return nothing). Options combine with OR inside a group and AND across groups. The result count updates on the same frame as the tap. One "Clear all" resets everything. On phones, chips sit in one horizontally scrolling row with an edge fade. Active filters are pinned visibly so users can see why the list shrank.
**Detect.** Active and idle chips that look alike; result counts that update late or never; no clear-all.

### DAT-11 · Search is five parts (P1)
**Rule.** A placeholder that says what can be searched ("Search by name, SKU or brand"); recent searches on focus; autocomplete ranked by usage with a category label, few and sharp results; full keyboard navigation with visible focus; a zero-results state with a way out (spelling suggestions, popular items, clear filters). Debounce requests and keep previous results visible while fetching.
**Detect.** "Search…" placeholders; empty dropdown on focus; zero-results dead ends; requests per keystroke.

### DAT-12 · Command palette is a system (P2)
**Rule.** Fuzzy matching ("stg" finds Settings), grouped labelled sections, keyboard-first (arrows, Enter, Escape), never empty on open (recents and suggestions), async results load in place with an inline spinner, nested commands show a breadcrumb and Escape goes back one level. It accelerates visible navigation; it never replaces it.

### DAT-13 · Charts tell the truth (P0)
**Rule.** Bar axes start at zero. The question picks the form: bars compare, lines show change over time, pies only with about five slices or fewer. Choose an aspect ratio where the average slope sits near 45°. Remove non-data ink (heavy gridlines, 3D, shadows, boxed legends) and label series directly. Spend colour on meaning: one highlighted series against neutral others, sequential or diverging scales for ordered data. Title the chart with the takeaway ("Revenue flat since March"). Never encode a series by colour alone.
**Detect.** Truncated bar baselines; pies with many slices; rainbow series; 3D charts; generic metric titles.

### DAT-14 · Dashboards lead with the number that matters (P1)
**Rule.** One primary metric, larger, with its breakdown; secondary metrics smaller. Each number has a shape: a delta with a unit and a comparison period ("+12.5% vs Jul"), or a sparkline. Title the page by what it shows ("Revenue · Aug 1–31"), not a greeting. No icon tiles competing with the numbers. See CON-6 for the other generated-dashboard tells.

### DAT-15 · Avatars are a system (P2)
**Rule.** Fallback chain: image, then initials from the name, then a generic icon; never a broken image. Background colour derives from a hash of the user ID so the same person looks the same everywhere. Two initials by default, one at very small sizes. Groups overlap and cap with "+N". Presence is shown on the avatar ring, once. Three size tokens only.

### DAT-16 · Chat threads keep the reader in place (P1)
**Rule.** Group consecutive messages from one sender within a short window (about 2 min) under one avatar, tight inside a group and looser between groups. Date dividers instead of timestamps on every row; exact time on hover. The sent message appears instantly and confirms quietly; a failed one stays in place with "Not sent · Retry". When the reader has scrolled up, new messages do not move the viewport; show a "N new messages" pill. Typing indicators live in the message flow. The composer grows to about five lines then scrolls; Enter sends, Shift+Enter adds a line.

### DAT-17 · Ratings are honest (P2)
**Rule.** Stars preview on hover separately from the committed value and snap back when the pointer leaves. Averages render as fractional fills (4.4 is not five stars). Pair an average with the count and distribution. Stars are keyboard operable (radio group semantics).

### DAT-18 · Calendar week views (P2)
**Rule.** Open scrolled to the current time, not midnight. Events use a coloured stripe on a light tint instead of a full saturated fill (contrast stays readable). Overlapping events split the column side by side instead of hiding behind "+1 more". Height equals duration with a one-line minimum. Drag on empty space creates an event snapped to 15 minutes; resize from the bottom edge. All-day events live in a pinned row above the grid.

---
Sources: number-formatting, data-table, data-table-system, responsive-table, bulk-actions, pagination, scroll-restoration, text-truncation, filter-chips, search-experience-system, command-palette, charts-that-lie, de-ai-dashboard, avatar-system, chat-ui-system, star-rating, calendar-week-view. See `sources.md`.
