---
id: DcLaVaGNfoy
reel_url: https://www.instagram.com/reel/DcLaVaGNfoy/
pattern_page: none
date: 2026-08-17
duration_s: 50
type: ui
category: navigation
topic: Scroll restoration, sticky-header offset, anchor margin, infinite-scroll footer
sources: frames, voice-over, caption
---

# Scroll is state: restore position on back

**Caption:** Restore the scroll position after the user opens a details page.
**Hook:** You press back and the post you had scrolled down to is gone.

## Main rule
Treat scroll position as navigation state: save it per history entry when leaving a list and restore it when the user comes back, offset by any sticky header. Give anchor targets `scroll-margin-top`, and do not hide a footer with essential links below an infinite feed.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 1840px | feed scroll position before opening a post | 0:00-0:02 "Scroll position" readout |
| 0px | scroll position after going back with a SPA router ("Back at the top. Your post is gone.") | 0:03 readout |
| scrollTop 2080 | debug label on the list during the route-change demo (does not match the 1840px readout; unclear on screen) | 0:04-0:06 |
| `scrollTop = 0` | client-side route change result ("your router forgot") vs full page load where the browser restores ("it used to remember") | 0:05-0:12 |
| "your post, 8 rows down" | how far the user's post is from the top after a reset | 0:13-0:21 |
| `history.scrollRestoration = 'manual'` | opt out of browser auto-restore before handling it in the app | 0:13-0:21 code |
| `save(key, scrollY)` on leave: /feed -> 1840; `scrollTo(saved)` on return: 1840 -> restored | per-entry save and restore | 0:13-0:21 code |
| 88px | sticky header height | 0:22-0:28 header badge |
| `scrollTo(y)` -> `scrollTo(y - 88)` | restore offset by the sticky header height | 0:22-0:28 code |
| `:target { scroll-margin-top: 96px; }` | jump-link target clearance under the bar (96px, 8px more than the 88px header in the previous scene; the reel does not tie them together) | 0:30-0:35 code |
| 105px / 12 loaded ... 7,575px / 64 loaded | infinite feed counter growing as items load | 0:36-0:45 |
| 2,535px away ... 7,575px away | distance to the footer ("Footer: never reached") growing with each load | 0:37-0:45 |
| 5 | recap items | 0:47-0:49 |

## Before / after
- **Back navigation.** Before: user scrolls the feed to 1840px, opens a post, presses back; the SPA renders the feed at 0px and the post is 8 rows down. After: position saved on leave (keyed by history entry) and restored on return; the tapped row is visible and highlighted ("restored"). Why: the user's place in a list is part of their mental context; losing it forces re-finding (search cost) and breaks the expectation set by native browser back.
- **Sticky header.** Before: restore scrolls the row to y, so it sits under the 88px sticky header ("Header hides your row"). After: `scrollTo(y - 88)` lands the row just below the header ("Header clears your row"). Why: the visual viewport top is the header's bottom edge, not 0.
- **Anchor links.** Before: tapping "#pricing" scrolls the "Pricing" heading under the bar, only its bottom edge visible ("Jump links land wrong"). After: `:target { scroll-margin-top: 96px }` lands the heading fully visible below the bar. Why: the browser aligns the target's border edge to the scrollport top unless a margin is declared.
- **Infinite feed.** Bad only: each load pushes the footer (About, Contact, Terms) further away, from 2,535px to 7,575px, "never reached". Why it matters: links that live only in the footer become unreachable. The reel states the problem; the fix (paginate / "load more" button / move links elsewhere) is implied, not shown.

## Do
- Save `scrollY` (or a container's `scrollTop`) per history entry key on leave; restore after the list has rendered its data.
- Set `history.scrollRestoration = 'manual'` when the app restores scroll itself.
- Subtract the sticky header height from any programmatic scroll target.
- Add `scroll-margin-top` (at least the header height) to anchor targets / `:target`.
- With infinite scroll, give users another path to footer content (a "Load more" button, a capped auto-load, or the links in a menu).

## Don't
- Don't reset scroll to 0 on every route change, especially on back/forward.
- Don't restore to the raw element offset when a fixed or sticky bar overlaps the top.
- Don't put the only copy of contact, legal or policy links below an endless feed.

## Scene by scene
- 0:00 Phone mockup of a reading app feed; readout "Scroll position 1840px"; finger taps "When to break your own rules", detail view opens.
- 0:03 Back pressed: feed at the top, readout 0px in danger colour, "Back at the top. Your post is gone."
- 0:04 "Route change: Routes reset to zero." Route label /post/42 -> /feed, debug scrollTop counts down to 0; rows "Full page load -> browser restores (it used to remember)" vs "Client-side route -> scrollTop = 0 (your router forgot)"; badge "Route change dumps you at zero."
- 0:13 "Restore: Back to the exact post." Two phones, "Without restore" (top of list, "your post, 8 rows down") vs "With restore" (tapped row highlighted, "restored" chip); code panel with `history.scrollRestoration = 'manual'`, on leave `save(key, scrollY)` /feed -> 1840, on return `scrollTo(saved)` 1840 -> restored; "Restore the exact position."
- 0:22 "Sticky header: Header hides your row." Header with 88px badge covers the target row; `scrollTo(y) -> scrollTo(y - 88)`; row then sits below the header, "Header clears your row." "Offset by the header height."
- 0:30 "#Anchor: Jump links land wrong." Docs screen, tap "#pricing", heading clipped under the bar; `:target { scroll-margin-top: ___ }` fills in 96px; heading lands fully visible, "Jump links land right."
- 0:36 "Infinite scroll: The footer runs away forever." Feed auto-loads (12 to 64 loaded), footer panel "Footer: never reached" with distance growing 2,535px to 7,575px; "Infinite scroll buries the footer."
- 0:47 Recap "Scroll is state.": 01 Save scrollY per entry, 02 A route is not a reset (`scrollRestoration = 'manual'`, then rehydrate), 03 Offset by the header, 04 scroll-margin-top, 05 Mind the infinite feed; CTA designmotionhq.com.

## Voice-over summary
- Pressing back in a single-page app loses the post you scrolled to, because the router resets scroll to zero on each route change.
- The browser used to remember the position on full page loads; client-side routers dropped that.
- Save the position for each history entry and put it back on return instead of sending the user to the top; "position is state".
- A sticky header hides the restored row unless you offset by its height; jump links need `scroll-margin-top` or headings tuck under the bar.
- Infinite scroll keeps pushing the footer away, so links, contact and terms there are never reached.

## Notes for the skill
- Key the saved position by the history entry (e.g. `history.state.key` / router location key), not by pathname, so two visits to /feed in the stack restore independently. Store in `sessionStorage` or router state.
- Restore only after the list content (and image heights) is rendered; restoring before data loads lands short. For virtualised lists, store the first visible item id plus offset instead of raw pixels.
- Frameworks: React Router `<ScrollRestoration />`, Next.js App Router handles back/forward by default, Vue Router `scrollBehavior(to, from, savedPosition)`.
- Prefer CSS over hard-coded subtraction: `html { scroll-padding-top: var(--header-h) }` covers anchor jumps, `scrollIntoView` and focus scrolling in one place; `scroll-margin-top` per target is the alternative. Keep the header height in a CSS custom property instead of literal 88.
- Accessibility: after restoring, keep keyboard focus on (or return it to) the item the user activated so screen-reader and keyboard users also land in context. WCAG 2.4.11 Focus Not Obscured: the sticky header must not cover the focused element, which `scroll-padding-top` also helps with.
- Infinite scroll: WCAG does not forbid it, but footer-only links become unreachable; provide a "Load more" button or stop auto-loading after N pages, and an accessible way to skip past the feed.
