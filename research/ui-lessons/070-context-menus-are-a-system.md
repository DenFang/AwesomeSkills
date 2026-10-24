---
lesson: 070
kind: video
duration_s: 53
type: ui
category: interaction
topic: context menus (collision flip, grouping, safe triangle, keyboard, long press)
sources: frames, voice-over, lesson notes
---

# Context menus are a system

**Hook:** Right-click near the screen edge and the menu flips, because a good context menu measures the space before it opens.

## Main rule
Anchor the context menu to the cursor, measure the viewport before placing it and flip vertically / mirror horizontally to stay fully visible; group items by intent with dividers and the destructive action alone at the bottom; protect submenus with a hover-intent safe triangle; support arrows, type-ahead and level-by-level Escape; and expose the same actions on touch via long press opening a bottom sheet.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| cursor 930 · 652, viewport 1080 × 1920 | demo readout: a right-click close to the right edge triggers "flip ←" | 0:00-0:02 on-screen |
| 4 placement outcomes | "fits ↓" (default, below-right), "flip ↑" (no room below), "mirror ←" (no room right), "flip ↖" (bottom-right corner, both) | 0:04-0:11 on-screen |
| 12 flat actions = noise | the ungrouped menu | 0:12-0:16 on-screen + voice |
| 3 groups by intent + 1 destructive | regrouped menu: Primary (Open, Open with…, Get info), Edit (Rename, Duplicate, Move to…, Compress), Share (Copy link, Share, Download, Add to favorites), Delete alone | 0:17-0:21 on-screen |
| triangle: vertex = cursor tip, base = submenu edge | safe-triangle geometry for hover intent | 0:22-0:31 on-screen |
| keys ↓ ↓ D ↓ → Esc | keyboard demo: arrows walk, "type-ahead: D" lands on Duplicate, → opens submenu, Esc closes one level ("parent stays") | 0:32-0:40 on-screen |
| ⌘O, ⌘I, ⌘D, ⌫ | shortcut hints shown right-aligned on Open, Get info, Duplicate, Delete | 0:32-0:40 on-screen |
| long press · 500ms | touch trigger duration for the bottom-sheet version | 0:41-0:46 on-screen |

## Before / after
- **Fixed placement vs measured placement.** Bad: menu always opens below-right of the cursor and gets clipped by the viewport edge. Good: compute menu size and available space first; flip up if no room below, mirror left if no room right, both in a corner, always keeping the top-left corner (or matching corner) anchored at the cursor. Why: the anchor keeps the spatial link to what was clicked, and clipping hides items (often Delete, which sits last).
- **12 flat actions vs grouped.** Bad: 12 items in arbitrary order (Rename, Copy link, Open, Delete, Duplicate, Share…), Delete buried mid-list. Good: three intent groups split by dividers plus Delete isolated at the bottom in the danger colour. Why: dividers let the eye scan chunks instead of 12 items, related actions sit together (Rename next to Duplicate, Copy link next to Share), and distance plus colour make the destructive item hard to hit by accident.
- **Naive hover vs safe triangle.** Bad ("No triangle", naive hover): moving diagonally from "Move to…" toward the submenu crosses "Share", which steals hover; the submenu closes ("submenu lost", "menu dies mid-path"). Good ("Safe triangle", hover intent, Figma-style): an invisible triangle from the cursor tip to the near edge of the submenu; while the pointer stays inside it, the parent keeps the submenu open and the user reaches "Archive" ("menu holds"). Why: users move toward a target along the shortest diagonal, not along a right-angle path.
- **Esc closes everything vs one level.** Good: Esc in a submenu closes only the submenu; the parent stays open with focus back on "Move to…". Why: preserves the user's position instead of forcing them to start over.

## Do
- Open the menu at the pointer position and measure it against the viewport before showing it; flip and/or mirror to keep it fully inside.
- Group actions by intent, separate groups with dividers, keep the destructive action last, alone, in the danger colour.
- Pair related actions: Rename with Duplicate, Copy link with Share.
- Implement a safe triangle (vertex at the cursor, base on the submenu's near edge) so diagonal movement keeps a submenu open.
- Support ↑/↓ to move, a typed letter to jump to the first matching item, → to open a submenu, Esc to close one level.
- Show shortcut hints right-aligned in the row.
- On touch, open the same action set from a long press (~500 ms) as a bottom sheet with the item name as a header.

## Don't
- Don't let the menu render partly off-screen.
- Don't dump a dozen ungrouped actions in one flat list.
- Don't close a submenu the instant the pointer leaves its parent row.
- Don't make Esc close the whole menu tree from inside a submenu.
- Don't ship right-click only; touch users have no right-click.

## Scene by scene
- 0:00 File list window ("Files: Projects", 7 files). Cursor right-clicks near the right edge of "roadmap.fig"; readout chips "cursor 930 · 652" and "viewport 1080 × 1920".
- 0:01 Menu (Open, Rename, Duplicate | Copy link, Share | Delete) appears to the left of the cursor; chip "flip ←".
- 0:02 Caption "It measured first."
- 0:03 Section "Measure, then open": wireframe viewport; chips "anchor: cursor", "measure → place", "collision: flip". Click in the middle: menu opens below-right, label "fits ↓".
- 0:06 Click near the bottom: menu opens upward, "flip ↑".
- 0:08 Click near the right edge: menu opens leftward, "mirror ←".
- 0:10 Click in the bottom-right corner: menu opens up and left, "flip ↖".
- 0:12 Section "Group by intent": big counter "12 flat actions = noise" beside a 12-item unordered menu; hover highlight wanders.
- 0:17 Items animate (reorder) into groups; counter becomes "3 groups by intent, +1 destructive".
- 0:19 Group labels appear on the right: Primary, Edit, Share; Delete slides to the bottom with a danger-tinted row and "Delete" label. Chips "group by intent", "dividers split", "destructive last".
- 0:22 Section "The safe triangle": two panels side by side, "Safe triangle (hover intent, Figma-style)" vs "No triangle (naive hover)". Chips "vertex: cursor tip", "base: submenu edge", "hover intent".
- 0:24 Left: a dashed translucent triangle spans from cursor to the submenu; cursor travels diagonally and lands on "Archive", label "menu holds". Right: the same path hovers "Share", submenu disappears, label "submenu lost" / "menu dies mid-path".
- 0:32 Section "Power users never aim": menu with shortcut hints; key caps ↓ ↓ D ↓ → Esc light up in sequence. Highlight moves Open → Get info → Rename, then "D" jumps to Duplicate ("type-ahead: D").
- 0:37 ↓ to "Move to…", → opens the submenu (Documents focused).
- 0:40 Esc closes only the submenu; note "Esc = one level · parent stays". Chips "arrows walk", "letters jump", "Esc closes one level".
- 0:41 Section "No right-click on mobile": desktop right-click menu on the left, phone "Library" grid on the right; a ring fills on a thumbnail (long press), then a bottom sheet rises with header "roadmap-v2.png · 8.1 MB" and the same actions. Highlight moves in sync on both. Chips "long press · 500ms", "same actions", "two triggers".
- 0:47 End card "Right-click is a system." with the grouped menu, follow CTA and "Save this for your next build".

## Voice-over summary
- Right-click near an edge and the menu flips: it measures before it opens, flips up without room below and mirrors left without room to the right, always anchored to the cursor and inside the viewport.
- Twelve flat actions read as noise; group by intent, split with dividers, keep Delete alone at the bottom in the danger colour.
- Submenus die when the cursor drifts, so Figma uses an invisible triangle from the cursor to the submenu; inside that path the menu holds ("That's hover intent").
- Keyboard: arrows walk, letters jump (D lands on Duplicate), Escape closes one level only.
- Mobile has no right-click: a long press opens the same actions as a bottom sheet; one menu system, two triggers.

## Notes for the skill
- ARIA (WAI-ARIA APG Menu pattern): container `role="menu"`, items `role="menuitem"`, dividers `role="separator"`, submenu parent `aria-haspopup="menu"` + `aria-expanded`. Focus moves into the menu on open (first item) and returns to the invoking element on close. Keyboard per APG: ↑/↓ move (optionally wrap), Home/End, → opens submenu and focuses its first item, ← or Esc closes the submenu and returns focus to the parent item, Enter/Space activates, printable characters do type-ahead. Tab should close the menu.
- Keyboard invocation of a context menu: also support Shift+F10 and the Menu/ContextMenu key; place the menu at the focused element rather than the pointer in that case. The video only shows pointer invocation.
- Placement: use a positioning engine (e.g. Floating UI `flip` + `shift` middleware) or measure `getBoundingClientRect()` of the rendered menu before making it visible; position with `position: fixed` relative to the client coordinates of the event. Re-check placement for submenus too (a submenu near the right edge should open to the left).
- Safe triangle: track the last pointer positions; while the pointer is inside the triangle (cursor point, submenu top-near corner, submenu bottom-near corner) and moving toward the submenu, delay switching the active item. Add a short timeout (commonly a few hundred ms) so a pointer that stops inside the triangle eventually changes the active row. Exact delay not given in the video.
- Delete: visually separate and use the danger colour plus an icon (not colour alone). Consider confirmation or undo for destructive actions; the video does not cover this.
- Long press 500 ms: matches common platform defaults (Android ~400-500 ms). Give progress feedback (the ring) and prevent the native text-selection/callout menu (`-webkit-touch-callout: none`, `user-select: none` on the target). Also expose the actions through a visible "more" (⋯) button, because long press is undiscoverable and not available to all assistive-technology users.
- Bottom sheet: add a header naming the target item (shown: file name + size), a drag handle, a scrim, and dismissal by tap outside / swipe down; trap focus while open.
- Reduced motion: the reorder/flip animations are demo flourishes; in product, open the menu instantly or with a very short fade/scale and honour `prefers-reduced-motion`.
