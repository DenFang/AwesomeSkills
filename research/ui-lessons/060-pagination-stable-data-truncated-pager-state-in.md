---
lesson: 060
kind: video
duration_s: 54
type: ui
category: navigation
topic: pagination: offset vs cursor, choosing numbered / load more / infinite, truncated pager, scroll restore, URL state
sources: frames, voice-over, lesson notes
---

# Pagination: stable data, truncated pager, state in the URL

**Hook:** 10,000 rows and a direct jump to page 500; offset pagination hides a bug.

## Main rule
Use cursor (keyset) pagination when rows are inserted or deleted while people browse; pick numbered pages for jumping, "Load more" for user-controlled appends and infinite scroll only for feeds; show a truncated pager (first, gap, current with neighbours, gap, last, about 7 cells); restore the list scroll position when returning from a detail page; and keep the page in the URL.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 10,000 rows (counter animates up from 7,840) | dataset size in the demo | 0:00-0:03 on-screen, 0:00 voice |
| page 500 of 833 | jump target and last page | 0:00-0:03 on-screen pager; page 500 shows rows #5989-#5994, i.e. 12 rows per page implied (not stated) |
| `OFFSET 10 LIMIT 10 · page 2` | offset query in the duplicate demo | 0:04-0:09 on-screen |
| `OFFSET 500 LIMIT 10` vs `WHERE id < :lastId` | offset vs cursor queries side by side | 0:11-0:17 on-screen |
| `?after=cursor_abc123` | cursor token in the request/URL | 0:11-0:17 on-screen |
| "skip 500" vs "after this ID" | voice framing of offset vs cursor | 0:10 voice |
| 3 patterns | numbered, load more, infinite scroll | 0:17-0:26 on-screen + voice |
| 500 links | anti-pattern: full list of page links ("spilling off-screen") | 0:27-0:29 on-screen |
| ~7 cells: 1, ..., 499, 500, 501, ..., 833 (plus prev/next arrows) | truncated pager | 0:30-0:36 on-screen "Show ~7 cells, never the whole range" |
| Scroll = 0 vs restored | returning from detail page | 0:37-0:42 on-screen |
| `app.com/users?page=500` | page state in URL; refresh keeps page 500 vs "refresh resets to page 1" | 0:43-0:49 on-screen |

## Before / after
- **Offset drift.** Page 2 is fetched with `OFFSET 10 LIMIT 10` (rows #11-#16). A new row is inserted at the top ("everything shifts down"); the row that was last on page 1 (#10) now reappears at the top of page 2, flagged "seen twice". Offset counts positions, and positions change when data changes, so users see duplicates (or miss items when rows are deleted).
- **Cursor stability.** Side by side, after "insert a row at the top", the offset list starts with a duplicate (tag "dup", "shifts") while the cursor list (`WHERE id < :lastId`) still starts at the same next row (tag "stable"). A cursor anchors to the last row seen rather than to a count, so inserts and deletes before it cannot shift the window.
- **Three patterns, three jobs.** Numbered (caption "jump to any page"), Load more ("user stays in control", a button appends rows), Infinite scroll ("best for feeds", rows append with a "loading..." row at the bottom). Choosing by task: random access and position awareness for tables, explicit control and a reachable footer for lists, frictionless consumption for feeds.
- **500 links vs truncated pager.** A wall of numbered buttons overflows the screen ("spilling off-screen"). The truncated pager shows first (1), a gap, current with neighbours (499, 500, 501), a gap, last (833), about 7 cells. It keeps orientation (where am I, how many pages) and the extremes one click away without overwhelming.
- **Scroll reset vs restore.** Returning from a detail page (user "Leo Hart"), the bad list is at scroll 0 ("lost your place"); the good list is scrolled back with the tapped row highlighted ("lands on your row"). Users scan, open, and return repeatedly; losing position makes them re-find their place every time.
- **No URL state vs `?page=500`.** With the page in the URL, refresh keeps page 500 and "Link copied" makes it shareable; without it, refresh resets to page 1. The address bar is the durable, shareable store for view state.

## Do
- Use cursor/keyset pagination (`WHERE id < :lastId ORDER BY id DESC LIMIT n`) for frequently changing data and for infinite scroll / load more.
- Choose the pattern by job: numbered for tables and jumping, load more for user-paced lists, infinite scroll for feeds.
- Render a truncated pager: first, last, current and its immediate neighbours, ellipsis for gaps, prev/next arrows.
- Provide a "Go to page" input for very large page counts (shown at 0:00).
- Restore scroll position (and highlight the row the user opened) on back navigation.
- Put pagination state in the URL (`?page=500`, or the cursor) so refresh, back and shared links keep the view.

## Don't
- Don't use OFFSET pagination on live data where rows are inserted at the top.
- Don't render every page link.
- Don't reset a list to the top when the user comes back from a detail view.
- Don't keep the current page only in component state.
- Don't use infinite scroll for content people need to jump around in or compare.

## Scene by scene
- 0:00 Data table (ID, User, Role) with a row counter climbing to "10,000 rows"; "Go to page" input gets "500"; pager ‹ 1 ... 499 [500] 501 ... 833 ›; rows #5989-#5994. Caption: 10,000 rows, one jump to page 500.
- 0:04 "Offset pagination", query chip `OFFSET 10 LIMIT 10 · page 2`, rows #11-#16; footer "OFFSET shifts every page -> duplicates".
- 0:06 Banner "New row inserted at top, everything shifts down"; list now starts with #10 Romy Cole, highlighted with a danger tint and "seen twice". Caption: the same item shows up twice.
- 0:10 "Offset vs cursor": two lists, Offset (`OFFSET 500 LIMIT 10`) and Cursor (`WHERE id < :lastId`), chip `?after=cursor_abc123`, footer "cursor = stable". After "Insert a row at the top", offset gets a "dup" row and "shifts", cursor keeps Zoe Quinn on top with "stable". Caption: paginate by ID, the list stays stable.
- 0:18 "Three patterns: Each one fits a different job." Three phone-width lists: Numbered (pager 1 2 3 4 cycling), Load more (button appends rows), Infinite scroll (list keeps growing with "loading...").
- 0:27 "Don't render 500 links": a dense grid of page numbers with a "...spilling off-screen" tag.
- 0:30 It collapses to ‹ 1 ... 499 500 501 ... 833 ›, labelled first / gap / current pages / gap / last; 1 and 833 outlined with "first" and "last" labels; "Show ~7 cells, never the whole range." Caption: keep first and last always reachable.
- 0:37 "Back from a detail page": two lists, "Scroll = 0" and "Restore scroll"; a row opens a detail card (Leo Hart, Back button); going back, the left list is at the top ("lost your place"), the right list returns to Leo Hart highlighted ("lands on your row"). Caption: restore scroll, or you lose your place.
- 0:43 "State lives in the URL": browser bar `app.com/users?page=500` with pager on 500, "Refresh keeps page 500", "Link copied" toast; below, `app.com/users` with "No URL state", after refresh the pager jumps to 1, "Refresh resets to page 1". Caption: page 500 becomes a link you can share.
- 0:50 Outro: faded table and pager, follow and save prompts.

## Voice-over summary
- With 10,000 rows you can jump straight to page 500, but offset pagination hides a bug: add one row at the top and every page shifts, so people see the same item twice.
- Cursors fix the drift: paginate "after this ID", not "skip 500"; the list stays stable as data changes.
- Numbered for jumping, load more for control, infinite for feeds; each fits a different job.
- Do not render 500 page links: first, a gap, the current pages, a gap, the last; first and last always reachable.
- Coming back from a detail page should land on the row you left; restore scroll.
- Put the page number in the URL so page 500 is shareable and survives refresh: "State lives in the address bar."

## Notes for the skill
- The video does not reconcile two of its own rules: cursor pagination cannot jump to an arbitrary page number, and `?page=500` is an offset concept. Practical rule: numbered pagination with jump-to-page (offset or a hybrid) for tables where data is mostly stable; cursor pagination (with the cursor in the URL, e.g. `?after=...`) for live lists, feeds and load more. If you need both, accept offset for jumps and mitigate drift (e.g. snapshot by a "created before" timestamp).
- Keyset details: order by a unique, indexed key (or a composite like `(created_at, id)`) so ties do not cause skips; make cursors opaque tokens; support `before` for backward navigation.
- Pager markup: wrap in `<nav aria-label="Pagination">`, use real links (`<a href="?page=499">`) so pages are crawlable and open in new tabs, mark the current page with `aria-current="page"`, give prev/next accessible names ("Previous page", "Next page"), render ellipses as non-interactive text hidden from or labelled for screen readers. Disable or hide prev on page 1 and next on the last page. Touch targets at least 44x44 px (24x24 minimum per WCAG 2.5.8).
- On small screens drop the neighbours first (e.g. ‹ 1 ... 500 ... 833 ›) or switch to "Page 500 of 833" with prev/next.
- After changing page, move focus to the top of the results (or announce "Page 500 of 833" via a live region) and scroll the table into view; otherwise keyboard and screen-reader users stay at the pager with no feedback.
- Infinite scroll caveats (not in the video): footer becomes unreachable, positions are hard to return to, and it is hard for keyboard users. Offer a "Load more" fallback, keep the footer reachable, and use `history.scrollRestoration` / stored offsets or virtualised lists with an anchor item for restore.
- Scroll restoration: in SPAs store scroll offset (and loaded item count/cursor) per history entry and restore after data is rendered; restoring before data loads lands at the wrong place.
- Load more: announce the number of items added and move focus to the first new item, so screen-reader users know content arrived.
