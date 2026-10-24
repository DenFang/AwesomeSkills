---
id: DcGQMxYNjxh
reel_url: https://www.instagram.com/reel/DcGQMxYNjxh/
pattern_page: none
date: 2026-08-15
duration_s: 56
type: ui
category: interaction
topic: resizable split panels (drag handle hit area, clamp, snap closed, drag overlay, cursor lock, persisted width)
sources: frames, voice-over, caption
---

# Resizable panels: six rules for one drag

**Caption:** Resizable panel layouts are a risky pattern; here is how to make them right.
**Hook:** A split view looks fine until one drag pushes the divider off the screen and the sidebar collapses to width 0.

## Main rule
Treat the divider handle as a real control: a 1px visible line with a 12px grab target, widths clamped between a min and a max, a snap to fully closed near the edge (never a thin sliver), a full-page invisible overlay and a page-wide resize cursor while dragging, and the chosen width persisted across reloads.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| width: 0 | broken state: sidebar dragged fully off, no way back | 0:02-0:03 on-screen tag |
| 1px | visible divider line | 0:04-0:11 cross-section "1px line" + voice |
| 12px | grab target (hit area) around the line | 0:04-0:11 cross-section "12px grab" + chip "1px line, 12px grab target." + voice |
| 240px | min sidebar width ("min 240" guide; slider locks at 240px) | 0:12-0:19 on-screen guide + slider |
| 640px | max sidebar width ("max 640" guide; slider locks at 640px) | 0:12-0:19 on-screen guide + slider |
| 340px | sidebar width at start of the clamp demo; also the default it resets to without persistence ("reset to 340") | 0:12 slider; 0:47-0:51 tag |
| 617px, 521px, 520px | intermediate widths while dragging inside the range | 0:15, 0:18, 0:19 slider readout |
| 44px | the "sliver" left by a half-closed panel (bad) | 0:20-0:28 tag "44px sliver" |
| width: 0 (with check) | snap closed state (good) | 0:24-0:28 tag |
| `pointer-events: none` | the iframe under the drag overlay while dragging | 0:33-0:36 tag |
| `.handle { cursor: col-resize }` vs `body { cursor: col-resize }` | cursor set on the handle only (bad) vs the whole body during drag (good) | 0:38-0:45 on-screen code |
| 460px | persisted width restored after reload ("kept 460", `panelW: 460px`); without persistence `panelW:` (empty) | 0:47-0:51 on-screen |
| 6 | rules in the summary (Hit area, Clamp, Snap, Overlay, Cursor, Persist) | 0:52-0:55 on-screen |

The snap threshold (how close to the edge triggers snap) is not given.

## Before / after
- **Hit area:** Before: the grab target equals the 1px line, so the pointer often misses and "the resize feels stuck". After: the line stays 1px visually, but an invisible 12px zone around it catches the pointer; the handle and line highlight on hover. Why: Fitts's law, a 1px target is nearly impossible to acquire; separating visual weight from hit area keeps the layout clean and the control easy to grab.
- **Clamp:** Before: dragging can push the sidebar to width 0 with no way to reopen it. After: drag is clamped to 240-640px; the readout shows a lock icon when it hits either limit. Why: limits guarantee every panel stays usable and recoverable; content never squeezes into an unreadable column or disappears by accident.
- **Snap:** Before ("HALFWAY = BUG"): releasing near the edge leaves a 44px sliver with clipped icons, which "reads as broken". After ("SNAP CLOSED"): inside a snap zone near the edge the panel commits to width 0, labelled "clearly intentional". Why: binary end states read as deliberate; an in-between width that shows nothing usable looks like a layout bug.
- **Overlay:** Before: drag overlay off; when the pointer passes over an embedded iframe, "iframe ate the mouse", the divider is "frozen mid-drag" and the status says "panel froze". After: overlay on; a transparent layer covers the whole page during drag (iframe gets `pointer-events: none`), status "drag held". Why: iframes and text selection capture pointer events away from the parent document; a full-page layer keeps every move event flowing to the drag handler.
- **Cursor:** Before ("HANDLE ONLY", `.handle { cursor: col-resize }`): drifting a pixel off the handle flips the cursor back to an arrow while still dragging. After ("WHOLE BODY", `body { cursor: col-resize }` during drag): the resize cursor stays locked. Why: the cursor is feedback for the current mode; flicker suggests the drag was lost.
- **Persist:** Before ("RELOAD → RESET"): after reload the sidebar returns to the default 340, `panelW:` (empty). After ("RELOAD → RESTORED"): "kept 460", `panelW: 460px`. Why: the width is a deliberate user choice; discarding it forces the same adjustment on every visit.

## Do
- Draw the divider as a 1px line, give it a hit area of about 12px (wider on touch), and highlight the handle on hover and during drag.
- Clamp width between explicit min and max values (the reel uses 240 / 640px) and signal when a limit is hit.
- Below a snap threshold near the edge, collapse the panel fully to 0 and keep a visible affordance to reopen it.
- During drag: add a transparent full-viewport overlay above iframes and content, set `cursor: col-resize` on `body` (or the overlay), and disable text selection.
- Persist the width per user (for example in local storage keyed by layout) and restore it on load, re-clamped to the current limits and viewport.

## Don't
- Don't make the grab target as thin as the visible line.
- Don't allow free resizing to 0 or beyond the viewport.
- Don't leave panels at an in-between "sliver" width after release.
- Don't set the resize cursor only on the handle.
- Don't reset a user-adjusted layout on reload.

## Scene by scene
- 0:00 Browser mock "halyard.app/projects": sidebar (Overview, Projects, Members, Billing, Settings) and a Projects list (Northwind migration · Active, Atlas redesign · Review, Orbit API · Shipped). Caption "A split view. Looks fine." The cursor grabs the divider.
- 0:02 Divider dragged to the left edge; red frame and tag "width: 0"; 0:03 "One drag from broken."
- 0:04 "HIT AREA · Grow the grab zone." Cross-section diagram: a 12px shaded grab zone around a 1px line; chip "1px line, 12px grab target." 0:06-0:11 the cursor approaches, the line and handle light up, the divider drags.
- 0:12 "CLAMP · Limits are the feature." Guides "min 240" and "max 640"; slider "sidebar width" 340px; 0:13 dragged left, readout locks at 240px; 0:15 617px; 0:16 locks at 640px; 0:18 back to 521 / 520px. Chip "Clamp between min and max."
- 0:20 "SNAP · Commit to open or shut." Left: "HALFWAY = BUG", "44px sliver", "reads as broken". Right: "SNAP CLOSED", dashed snap zone, the panel collapses to "width: 0", "clearly intentional". Chip "Snap closed, never a sliver."
- 0:28 "OVERLAY · Cover the page mid-drag." Mock "halyard.app/embed" with an `<iframe> embed`; toggle "drag overlay" off: "iframe ate the mouse", "frozen mid-drag", "panel froze". 0:31 toggle on: page tinted, tag "pointer-events: none", "drag held". Chip "Overlay the page while dragging."
- 0:38 "CURSOR · No flicker on drift." "HANDLE ONLY" `.handle { cursor: col-resize }` vs "WHOLE BODY" `body { cursor: col-resize }`; the pointer drifts off the handle. Chip "Lock the cursor on the body."
- 0:46 Transition.
- 0:47 "PERSIST · Survive the reload." "RELOAD → RESET" (reloading, "reset to 340", `panelW:` (empty)) vs "RELOAD → RESTORED" ("kept 460", `panelW: 460px`). Chip "Remember the width."
- 0:52 "Handles are UI. Six rules for one drag." Grid 01 Hit area (1px line, 12px grab), 02 Clamp (between min and max), 03 Snap (closed, never a sliver), 04 Overlay (the page mid-drag), 05 Cursor (locked on the body), 06 Persist (remember the width); site link.

## Voice-over summary
- The layout looks fine until the divider is dragged off the screen.
- The visible divider is 1px but the grab target must be 12px; miss it and resizing feels stuck.
- Clamp every drag between a min and max width so a panel can never collapse beyond recovery ("limits are the feature"); near the edge snap fully closed, because halfway states read like bugs.
- While dragging, put an invisible overlay over the whole page, otherwise an iframe or text selection steals the mouse and the panel freezes.
- Set the resize cursor on the whole body so it doesn't flicker on drift, and remember the width across reloads.

## Notes for the skill
- State: `width`, `isDragging`, `isCollapsed`; on pointer move: `if (raw < snapThreshold) collapse(); else width = clamp(raw, min, max)`. The clamp and the snap must be designed together: values between 0 and min either snap to 0 or clamp to min, never rest in between.
- Drag mechanics: use Pointer Events with `handle.setPointerCapture(e.pointerId)`; add the overlay (`position: fixed; inset: 0; z-index` above content; `cursor: col-resize`) and `user-select: none` on `body` only while dragging; remove all of them on `pointerup` and `pointercancel`. Throttle layout writes with `requestAnimationFrame`.
- Accessibility (WAI-ARIA APG Window Splitter): the handle is a focusable `role="separator"` with `aria-orientation="vertical"`, `aria-valuenow`, `aria-valuemin`, `aria-valuemax`, `aria-controls` pointing to the panel, and an accessible name (`aria-label="Resize sidebar"`). Left / Right arrows resize in steps, Home / End jump to min / max, Enter toggles collapse. Without this, the reel's pattern is pointer-only and fails WCAG 2.1.1 (Keyboard).
- WCAG 2.5.7 (Dragging Movements, AA) requires a single-pointer alternative to dragging: provide a collapse / expand button or a menu with preset widths. The collapsed state must keep a visible, focusable way to reopen the panel (rail button, toggle in the header, keyboard shortcut).
- Target size: 12px meets neither WCAG 2.5.8 (24 x 24 CSS px minimum, unless spacing exception applies) nor touch guidelines (44pt / 48dp). Use 12px as a minimum for mouse only and widen the hit area to at least 24px on coarse pointers (`@media (pointer: coarse)`).
- Focus and hover: show the handle highlight on `:focus-visible` too, with at least 3:1 contrast against adjacent surfaces (WCAG 1.4.11).
- Persistence: store the width in px or as a fraction of the container; on restore re-apply the clamp and check that the main panel still fits the current viewport. Persist the collapsed state separately from the last open width so reopening returns to the user's width.
- Reduced motion: if the snap animates, keep it short (about 150-200 ms) and make it instant under `prefers-reduced-motion: reduce`.
