---
id: Degse6ngixY
reel_url: https://www.instagram.com/p/Degse6ngixY/
pattern_page: none
kind: carousel
date: 2026-10-15
type: ui
category: navigation
topic: breadcrumb rules (ancestor links, last crumb equals title, fold the middle past 4, keep the first level, 44 px mobile back link)
sources: caption, image slides 1-3 and 5-6, video slide (slide 4 of 6)
---

# Breadcrumbs: every level clickable, fold the middle, mobile back link

**Caption:** Deep pages need a way back that is not the browser button; four breadcrumb rules: every level links except the current page, the last crumb matches the page title, beyond 4 levels collapse the middle and keep both ends, on mobile use a 44 px back link to the parent.
**Hook (slide 1):** "Your breadcrumb hides the way back", over a trail whose first levels were folded away.

## Slide by slide
- **Slide 1 (cover, bad example).** Sample app window titled Orbit. The trail reads `... / 2026 / INV-2041`: the ellipsis has swallowed everything from the root down, including Billing. The page title below says Invoice 2041, while the last crumb says INV-2041. A dashed outline in the danger colour marks the header, with a danger tag reading Where is Billing? Below: contact Maya Ortiz (Northwind, billing admin), a table Item / Qty / Total with Pro seats 12 $960 and Storage 1 $280, a primary button Send again and a secondary Download.
- **Slide 2 (Save this: three values).** Headline: three values for a breadcrumb you can trust. Left, a mock panel (Orbit): trail `Billing / Invoices / INV-2041` in muted text, title INV-2041 in large bold text, a small table (Pro seats $960, Storage $280), and a bordered button `← Back to Invoices`. Leader lines to three numbers:
  - **4**: levels shown before folding (pointing at the trail).
  - **1**: title, the same as the last crumb (pointing at the title).
  - **44 px**: back link height on mobile (pointing at the back button).
- **Slide 3 (five checks before you ship a breadcrumb).** Three passes (accent check marks), two fails (danger cross marks):
  - Pass: every crumb but the last is a link.
  - Pass: the last crumb names this page.
  - Pass: middle levels fold into one menu.
  - Fail: the current page styled as a link.
  - Fail: folding the first level away.
- **Slide 4 (video, about 4.5 s loop).** Headline: every level is one click back. See Video slide.
- **Slide 5 (fold the middle, keep both ends).** Two cards:
  - Don't, every level shown: `Home / Team / Billing / Invoices / 2026 / INV-2041`, 6 levels that wrap to a second line, title INV-2041.
  - Do, middle folded: `Home / ... / Invoices / INV-2041` on one line, title INV-2041.
- **Slide 6 (closing promo).** The author's UX Engine product claims to check deep pages and fix paths that leave people stuck; link in bio. No new rule.

## Main rule
On deep pages give a breadcrumb where every ancestor is a link and the last crumb is the current page, shown as plain text (not styled as a link) with exactly the page title's wording. Show at most 4 crumbs; when the path is longer, fold the middle levels into one ellipsis menu while keeping the first level and the end of the trail. On mobile replace the trail with one back link to the parent, at least 44 px tall.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 4 levels | crumbs shown before the middle folds | slide 2; caption |
| 1 title | page title identical to the last crumb (INV-2041 / INV-2041) | slide 2 |
| 44 px | minimum height of the mobile back link (`← Back to Invoices`) | slide 2; caption |
| 6 levels, 2 lines | the Don't trail on slide 5, which wraps | slide 5 |
| 4 items, 1 line | the Do trail: first level, ellipsis, ancestor, current page | slide 5 |
| 1 menu | all hidden middle levels go into a single fold menu | slide 3 |
| 5 rows | vertical level list on the video slide: Home, Billing, Invoices, 2026, INV-2041 | slide 4 |

## Before / after
- **Root folded vs root kept (slides 1, 3, 5).** Bad: `... / 2026 / INV-2041`, so the user cannot see or reach Billing. Good: `Home / ... / Invoices / INV-2041`. Why: the first level names the section the page belongs to and is the most common escape target; the nearest ancestors are the other likely targets. The middle is the least useful part, so it is the part to hide.
- **Title differs from crumb vs identical (slides 1, 2).** Bad: crumb INV-2041 above the title Invoice 2041. Good: both read INV-2041. Why: two names for one page make the user wonder if they are the same place; identical wording ties the trail to the page and confirms the location at a glance.
- **Every level shown vs middle folded (slide 5).** Bad: 6 crumbs wrapping onto two lines. Good: 4 items on one line. Why: a wrapped trail is slow to scan and pushes content down; folding keeps the trail a single, scannable line while every hidden level stays one menu away.
- **Current page as link vs plain (slide 3).** Bad: the last crumb looks clickable. Good: ancestors are links, the current page is text. Why: a link to the page you are on does nothing visible, which reads as broken, and it weakens the signal of where you are.
- **Text-only targets vs full-row targets (slide 4).** Good: in the vertical level list every row is a link across its full width, and the current page keeps its own persistent highlight while another row is hovered. Why: a larger hit area is faster to point at, and keeping hover and current visually distinct preserves orientation during hover.
- **Desktop trail on mobile vs one back link (slide 2).** Good: a single `← Back to Invoices` button, 44 px tall, naming the parent. Why: a full trail on a narrow screen wraps or truncates into tiny targets; the parent is the step people take most, and naming it says where the button goes.

## Do
- Make every ancestor a real link; render the last crumb as plain text with the exact page title.
- Show up to 4 crumbs; past that, keep the first level and the end of the trail and put the middle into one ellipsis menu.
- Keep the trail on one line on desktop.
- On narrow screens show one back link labelled with the parent's name, at least 44 px tall.
- In vertical level lists, make the whole row the link and keep the current row marked while others are hovered.
- Give each link or row visible hover and `:focus-visible` states.

## Don't
- Don't fold the first level, or the current page, into the ellipsis.
- Don't style the current page as a link.
- Don't let the last crumb's label drift from the page title.
- Don't show every level when the trail would wrap.
- Don't rely on the browser Back button for moving up the hierarchy.

## Video slide
Slide 4, about 4.5 s loop. Sub-headline: hover any level, the whole row is a link, and your page stays lit. Panel titled Orbit with rows Home (house icon), Billing, Invoices, 2026 (folder icons) and INV-2041 (document icon; current: accent icon, accent bar on the left edge, raised row background).
- 0:00 Cursor below the panel; only the current row is highlighted.
- 0:00.5 Cursor on Home: the full-width Home row gets a hover background.
- 0:01 Cursor between rows, no hover.
- 0:01.5 Billing row highlighted.
- 0:02 Invoices row highlighted.
- 0:02.5 Between rows.
- 0:03 2026 row highlighted.
- 0:03.5 to 0:04 Cursor leaves the panel; back to only the current row highlighted.
Throughout, the current row keeps its marker, so hover and current states stay distinct.

## Notes for the skill
- WAI-ARIA APG breadcrumb pattern: wrap in `<nav aria-label="Breadcrumb">`, use an ordered list, and mark the current item with `aria-current="page"`. The APG example keeps the current item as a link with `aria-current`; the slides' rule (plain text, not styled as a link) is also valid, but put `aria-current="page"` on that element so it is still identified.
- Fold menu: the ellipsis is a real `<button>` with an accessible name such as Show hidden levels, following the APG menu button pattern (`aria-haspopup`, `aria-expanded`), so keyboard and screen reader users can reach every hidden level.
- Slide 5's Do trail keeps Invoices but hides 2026, the direct parent of INV-2041 in the Don't trail. Hidden levels should be one contiguous run and the direct parent should stay visible; read the rule as keep the first level plus the last ancestor and current page. Sample hierarchies also differ across slides (slide 2 has no Home or 2026 level), so treat them as illustrations, not one model.
- Separators (slashes, chevrons) should be decorative: CSS pseudo-elements or `aria-hidden="true"`, not text read between items.
- Ancestors in the mock are muted text with no underline; they still need a visible link affordance at least on hover and focus, and the muted text must keep 4.5:1 contrast against its background (WCAG 1.4.3).
- 44 px matches Apple HIG (44 pt) and WCAG 2.5.5 (AAA, 44 x 44 CSS px); WCAG 2.2 2.5.8 (AA) minimum is 24 x 24 CSS px; Material uses 48 dp. The label can stay small if padding makes the target 44 px.
- The video's vertical level list is a sidebar or tree style, not the inline horizontal breadcrumb of the other slides; the 4-level fold rule applies to the horizontal trail.
- Breadcrumbs reflect hierarchy (location), not visit history; do not build them from the navigation path.
