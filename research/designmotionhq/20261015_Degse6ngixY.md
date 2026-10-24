---
id: Degse6ngixY
reel_url: https://www.instagram.com/p/Degse6ngixY/
pattern_page: none
kind: carousel
date: 2026-10-15
type: ui
category: navigation
topic: breadcrumb rules (links, last crumb, folding, mobile back link)
sources: caption, video slide (slide 4 of 6)
---

# Breadcrumbs: every level clickable, fold the middle, mobile back link

**Caption:** Deep pages need a way back that is not the browser button; four breadcrumb rules: every level links except the current page, the last crumb matches the page title, beyond 4 levels collapse the middle and keep both ends, on mobile use a 44 px back link to the parent.
**Hook:** Deep pages need an in-page way back up the hierarchy.

## Main rule
Give deep pages a breadcrumb trail where each ancestor is a link and the current page is shown but not linked, its label identical to the page title; when the trail exceeds 4 levels collapse the middle levels and keep the first and last; on mobile replace the trail with one back link to the parent at least 44 px tall.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 4 levels | threshold above which the middle of the trail folds | caption rule 3 |
| both ends kept | first (root) and last (current) crumbs stay visible when folded | caption rule 3 |
| 44 px | minimum height of the mobile back link | caption rule 4 |
| 5 levels below the app name | sample trail on the video slide: Home, Billing, Invoices, 2026, INV-2041 | video slide |
| 4 / 6 | slide position | video slide footer |

## Before / after
- **Browser back vs in-page trail (caption).** Bad: the only way up from a deep page is the browser Back button, which follows history, not hierarchy. Good: a trail of ancestor links. Why: users arriving from search or a deep link have no history to go back through; the trail also shows where they are.
- **Small text links vs full-row targets (video slide).** Good: each level is a full-width row; hovering anywhere on the row highlights the whole row, while the current page keeps its own persistent highlight. Why: a larger hit area reduces pointing time (Fitts) and the persistent current marker keeps orientation during hover.
- **Long trail vs folded trail (caption only).** Bad: 6+ crumbs wrapping or truncating every label. Good: first crumb, an ellipsis for the hidden middle, then the last levels. Why: the root anchors the context and the nearest ancestors are the likely targets.
- **Desktop trail on mobile vs back link (caption only).** Good: a single back-to-parent link with a 44 px target.

## Do
- Make every ancestor a real link; render the current page as plain text (or a link with `aria-current="page"`).
- Use the exact page title as the last crumb's label.
- Over 4 levels: show root, an ellipsis control, and the last one or two ancestors plus the current page; the ellipsis expands or opens a menu of the hidden levels.
- On narrow screens show one back link labelled with the parent name (e.g. back to 2026), at least 44 px tall.
- Give each row or link a visible hover and `:focus-visible` state.

## Don't
- Don't make the current page a link to itself without marking it as current.
- Don't let breadcrumb labels drift from page titles.
- Don't fold the root or the current page.
- Don't rely on the browser Back button as the navigation for hierarchy.

## Slide by slide
The carousel has 6 slides. Only slide 4 (animated) was available; the other image slides were not downloaded, so the list is reconstructed from the caption and the position of each rule is unknown.
- Slide 4 (seen, animated): headline that every level is one click back; a vertical hierarchy list with full-row hover.
- Other slides (not seen): presumably the cover, the remaining rules (last crumb matches the title; fold the middle past 4 levels; 44 px mobile back link) and a closing/save slide.

## Video slide
Slide 4, about 4.5 s loop. Sub-headline: hover any level, the whole row is a link and the current page stays highlighted. Panel titled Orbit (sample app) with rows Home (house icon), Billing, Invoices, 2026 (folder icons) and INV-2041 (document icon, current: accent icon, accent bar on the left edge, raised row background).
- 0:00 Cursor below the panel; only the current row is highlighted.
- 0:00.5 Cursor on Home: the full Home row gets a hover background.
- 0:01 Between rows, no hover.
- 0:01.5 Billing row highlighted.
- 0:02 Invoices row highlighted.
- 0:02.5 Between rows.
- 0:03 2026 row highlighted.
- 0:03.5-0:04 Cursor leaves; back to only the current row highlighted.
Throughout, the current row keeps its marker, so hover and current states are visually distinct.

## Notes for the skill
- WAI-ARIA APG breadcrumb pattern: wrap in `<nav aria-label="Breadcrumb">`, use an ordered list, mark the current item with `aria-current="page"`. The APG example keeps the current item as a link with `aria-current`; the caption's rule of not linking it is also acceptable, but the current item must still be identified (`aria-current` on the element) and must not look like a clickable link.
- Separators (slashes, chevrons) should be decorative: CSS pseudo-elements or `aria-hidden="true"`, not text read between items.
- The fold control is a real `<button>` with an accessible name like Show 3 hidden levels, opening a menu or expanding inline; keyboard and screen reader users must reach the hidden levels.
- The video slide shows a vertical list of 5 levels without folding, which is a sidebar/tree style trail rather than the inline horizontal breadcrumb the caption rules describe; the 4-level fold rule applies to the horizontal trail.
- 44 px matches Apple HIG (44 pt); Material uses 48 dp; WCAG 2.2 2.5.8 minimum is 24 x 24 CSS px, 2.5.5 (AAA) is 44 x 44. The text can stay small if the padding makes the hit area 44 px.
- Breadcrumbs reflect hierarchy (location), not history; do not build them from the visit path.
