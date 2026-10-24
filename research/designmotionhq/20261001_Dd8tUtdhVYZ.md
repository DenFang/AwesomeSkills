---
id: Dd8tUtdhVYZ
reel_url: https://www.instagram.com/reel/Dd8tUtdhVYZ/
pattern_page: none
date: 2026-10-01
duration_s: 85
type: ui
category: motion
topic: CSS View Transitions (shared-element morphs)
sources: frames, voice-over, caption
---

# View Transitions: a card becomes a page

**Caption:** A card becomes a page with zero animation libraries (plus a plug for the author's Claude Code plugin).
**Hook:** One CSS property and no animation library turn a card into a page.

## Main rule
Give the element in the old state and its counterpart in the new state the same unique
`view-transition-name`; wrap the DOM change in `document.startViewTransition()` (SPA) or opt both
pages into `@view-transition { navigation: auto; }` (MPA), and the browser morphs size, position and
corners between the two snapshots. Use the same mechanism for list reorder (one unique name per
item), a theme wipe from the toggle (`::view-transition-new(root)` with a circular clip-path), and a
dialog that grows out of its trigger (hand the name from button to dialog).

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 1 property, libraries: 0 | `view-transition-name` is the only required CSS | 0:01-0:03 on-screen |
| width 867px, top 105px, radius 4px | card image snapshot (old state, /guides) | 0:11-0:20 on-screen |
| width 1080px, top 64px, radius 0px | page header snapshot (new state, /lisbon) | 0:11-0:20 on-screen |
| `view-transition-name: hero` | shared name on `.card img` and `.page header` | 0:02-0:20 on-screen |
| `li { view-transition-name: var(--trip); }`, `--trip: trip-1` ... `trip-5` | one unique name per list row | 0:22-0:33 on-screen |
| 5 guides -> "3 of 5 guides" | Hide visited filter removes 2 rows; rows slide | 0:27-0:30 on-screen |
| InvalidStateError: duplicate name trip-3 | two rows with the same name: transition skipped | 0:31-0:33 on-screen + voice |
| `animation: reveal 600ms` | theme wipe on `::view-transition-new(root)` | 0:34-0:44 on-screen |
| `clip-path: circle(0 at var(--x) var(--y))` | `from` keyframe of the wipe | 0:35-0:44 on-screen |
| --x: 851px, --y: 36px | click coordinates of the theme toggle, wipe origin | 0:39-0:44 on-screen |
| name "share" moves from button to dialog | modal grows from its trigger | 0:45-0:54 on-screen |
| `@view-transition { navigation: auto; }` | on both pages for cross-document morph | 0:55-1:10 on-screen + voice |
| Chrome 126+, Safari 18.2+ supported; no support = instant swap | cross-document support shown | 1:00-1:10 on-screen |
| 4 morphs, 1 property | summary (card-to-page, list reorder, theme wipe, modal) | 1:11 on-screen + voice |

## Before / after
- **Card to page (0:00-0:20).** Clicking a guide card navigates to its page; with both the card
  image and the page header named `hero`, the image box animates from 867 px wide / 105 px top / 4 px
  radius to 1080 px / 64 px / 0 px instead of cutting. Why: the browser captures an old and a new
  snapshot and interpolates their geometry, so the user sees that the page header is the card they
  tapped (object constancy keeps orientation).
- **List reorder and filter (0:21-0:30).** "Sort by date" / "Newest first" and "Hide visited" with a
  unique name per row: every row slides to its new place ("each row slides, 0 animation code"). Why:
  continuous motion lets the eye track which item went where, instead of re-reading a list that
  changed instantly.
- **Duplicate names (0:30-0:33).** Two rows both named `trip-3`: badge "duplicate name, skipped" and
  an InvalidStateError; no animation runs. Why: a name must identify exactly one element per state;
  the browser aborts the whole transition on duplicates.
- **Theme toggle (0:34-0:44).** The whole page is the `root` snapshot; the new theme is revealed by a
  circle clip-path that starts at radius 0 at the toggle's coordinates and expands over 600 ms. Why:
  the change visibly originates from the control that caused it, linking cause and effect.
- **Modal from nowhere vs from its button (0:45-0:54).** Left card: "from nowhere", the Share trip
  dialog fades in at the centre. Right card: "grows from the button": the "Share trip" button holds
  `view-transition-name: share`; inside `startViewTransition` the name is removed from the button,
  given to the dialog, and `showModal()` is called, so the dialog expands from the button. Why:
  spatial origin tells the user what opened the dialog and where it will return.
- **Cross-document (0:55-1:10).** Real page loads between trips.html and lisbon.html (tagged "real
  page load") still morph the hero when both pages declare `@view-transition { navigation: auto; }`.
  Unsupported browsers get an instant swap ("nothing breaks"). Why: progressive enhancement; the
  animation is additive and navigation stays functional.

## Do
- Name exactly one element per state with a given `view-transition-name`; names must be unique on the page.
- For lists, set a per-item name from data (e.g. `style="--trip: trip-<id>"` and
  `li { view-transition-name: var(--trip); }`), keyed by stable id, not index.
- In SPAs, perform the DOM update inside `document.startViewTransition(() => update())`.
- For MPAs, add `@view-transition { navigation: auto; }` to both the source and destination pages.
- For a theme toggle, store the click coordinates in CSS variables and animate
  `::view-transition-new(root)` with a circle clip-path from those coordinates.
- For a dialog, move the shared name from the trigger to the dialog inside the transition callback
  (and back on close).
- Feature-detect (`if (!document.startViewTransition) update();`) so unsupported browsers just swap.

## Don't
- Don't give two visible elements the same name at the same time (the transition is skipped).
- Don't fade a modal in from nowhere when it has a clear trigger.
- Don't pull in an animation library for these four morphs.

## Scene by scene
- 0:00 A travel guides grid ("Guides for slow travel"); cursor clicks "Lisbon in 48 hours".
- 0:01 "View transitions 01: A card becomes a page." The article page appears; a style.css panel types `.card img, .page header { view-transition-name: hero; }`; badge "libraries: 0"; pill "1 property".
- 0:04 "02: Same name. Two snapshots." Before (/guides) and after (/lisbon) panels side by side; pill "same name = morph".
- 0:09 "old snapshot" frame on the card image, "new snapshot" frame on the header.
- 0:11 A ghost box morphs between them; readouts toggle between width 867px / top 105px / radius 4px and width 1080px / top 64px / radius 0px.
- 0:17 Code adds `// SPA: one call wraps the DOM update` and `document.startViewTransition(() => showPage());`.
- 0:21 "03: Every row, its own name." "Saved trips, 5 guides" list with Sort by date and Hide visited; row tags trip-2 ... trip-5 appear; code `li { view-transition-name: var(--trip); }`.
- 0:25 Sort by date: rows slide into new order.
- 0:27 Hide visited: two rows leave, counter "3 of 5 guides", remaining rows slide up; badge "each row slides, 0 animation code".
- 0:31 Two rows tagged trip-3 in the danger colour; "duplicate name, skipped"; code comment "InvalidStateError: duplicate name trip-3".
- 0:34 "04: A theme toggle that spreads." Page outlined as `root`; theme.css with `::view-transition-new(root) { animation: reveal 600ms; }` and `@keyframes reveal { from { clip-path: circle(0 at var(--x) var(--y)); } }`.
- 0:39 Cursor clicks the toggle; readout "--x: 851px, --y: 36px"; a circular edge sweeps across the page from the top-right. Pill "1 rule, circular wipe".
- 0:45 "05: A modal born from its button." Two cards: "from nowhere" vs "grows from the button"; share.js shows the name handoff and `dialog.showModal()`. Pill "origin = button".
- 0:55 "06: Works across real page loads." Browser chrome with trips.html and lisbon.html, "real page load" tag; both files show `@view-transition { navigation: auto; }`.
- 0:57 Clicking the card loads lisbon.html and the hero morphs; badges "no framework", "same morph".
- 1:04 Support chips turn on: "Chrome 126+ supported", "Safari 18.2+ supported"; "No support: instant swap"; "nothing breaks". Pill "no SPA needed".
- 1:11 "07: Four morphs. One property." Grid of the four demos with chips Same name, Unique per item, Root wipe, Button origin, Cross-page.
- 1:13 Ad: "Think like a senior UX designer", Claude Code command list (/ux-design, /ux-audit, /ux-review, /restyle), UX Engine plugin card, "Link in bio".

## Voice-over summary
- Give the card image and the page header the same view-transition name; the browser snapshots both
  states and morphs size, position and corners.
- In a single-page app one `startViewTransition` call wraps the DOM update.
- For lists give every item its own unique name and sort, filter or delete animate for free; two
  items with the same name skip the whole transition.
- Theme toggle: the page is one snapshot called root; animate a circle clip-path on its new
  snapshot so dark mode spreads from the clicked button.
- A modal can grow out of its button by moving the name from button to dialog; cross-page morphs
  need one at-rule on both pages; Chrome and Safari ship it, others get an instant swap. Ends with a
  plugin ad.

## Notes for the skill
- Reduced motion: wrap custom view-transition animations in
  `@media (prefers-reduced-motion: no-preference)` or set
  `::view-transition-group(*), ::view-transition-old(*), ::view-transition-new(*) { animation: none; }`
  under `reduce`; a full-screen circular wipe and large morphs are exactly the motion WCAG 2.3.3 warns about.
- The theme-wipe code as shown is incomplete: animating from `circle(0 ...)` to the implicit
  `clip-path: none` is not interpolable, so the clip would jump instead of growing. Add an explicit
  `to { clip-path: circle(R at var(--x) var(--y)); }` where R is the distance from the click point to
  the farthest corner (e.g. `Math.hypot(max(x, w - x), max(y, h - y))` in px), and disable the default
  cross-fade (`::view-transition-old(root), ::view-transition-new(root) { animation: none;
  mix-blend-mode: normal; }` before re-adding `reveal` on new). Set --x/--y from the click event, and
  for keyboard activation use the button's centre.
- Duplicates: the transition is aborted (promise rejects with InvalidStateError) but the DOM update
  still applies, so the UI stays correct, just unanimated. Newer engines also support
  `view-transition-name: match-element` / `auto` for lists, which avoids hand-made unique names
  (check current support before relying on it).
- Support claims: cross-document transitions match the on-screen Chrome 126+ / Safari 18.2+.
  Same-document `startViewTransition` has wider support (including recent Firefox); "Chrome and Safari
  only" is an oversimplification as of late 2026; verify current tables.
- Dialog handoff: also reverse on close (name back to the button) and keep focus management of
  `showModal()` intact (focus moves into the dialog, returns to the button on close). During a view
  transition the page is non-interactive; keep durations short (the reel's 600 ms is the upper end
  for a full-page effect; component morphs are usually 200-350 ms).
- Snapshots are images: text inside a morphing element can stretch during the transition; use
  `::view-transition-old(name), ::view-transition-new(name) { height: 100%; object-fit: cover; }` or
  separate names for text and image when aspect ratios differ.
