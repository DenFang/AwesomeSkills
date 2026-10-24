# Interaction, navigation and overlays

How controls respond, how people move around, which overlay to use, and how keyboard, mouse and touch all reach the same actions.

Severity: **P0** unreachable, inaccessible or destructive by accident, **P1** friction, **P2** polish.

---

### INT-1 · Focus is always visible (P0)
**Rule.** Never remove the focus outline without a better replacement: about 2 px, offset about 2 px, at least 3:1 contrast against both the element and its background, shown for keyboard users via `:focus-visible`. The focus style differs from the selected/active style. DOM order matches visual order. A skip link is the first focusable element on content-heavy pages.
**Detect.** `outline: none` / `outline: 0` without a `:focus-visible` replacement; `tabindex` > 0; CSS reordering (`order`, `flex-direction: row-reverse`) that changes the visual sequence of interactive items.
**Fix.**
```css
:focus-visible { outline: 2px solid var(--color-focus); outline-offset: 2px; }
```

### INT-2 · Real elements, real keyboard (P0)
**Rule.** Clickable things are `<button>` or `<a href>`, not `<div onClick>`. Custom widgets carry the right roles and states (`aria-expanded`, `aria-controls`, `aria-selected`, `aria-checked`, `aria-haspopup`) and keys: Enter/Space activate, arrows move within composite widgets (menus, tabs, listboxes, radio groups, grids), Home/End jump, Escape closes one level.
**Detect.** `onClick` on non-interactive elements without role and key handlers; accordions with `<div>` headers; menus that ignore arrow keys.

### INT-3 · Pick the overlay by one question: does it block? (P1)
**Rule.**
| Need | Overlay |
|---|---|
| Must be answered before anything else (critical or destructive decision) | Modal with full scrim, one decision |
| Contextual choice on a phone | Bottom sheet |
| Small contextual menu or quick action | Popover anchored to its trigger |
| Navigation or a secondary panel | Drawer from the edge |
| Passive hint | Tooltip |
Modals for routine actions add friction; never stack modals.
**Detect.** Modals for settings tweaks or info; popovers detached from their trigger; nested dialogs.

### INT-4 · Dialogs manage focus (P0)
**Rule.** On open, focus moves into the dialog (first field or the least destructive action); Tab cycles inside; Escape closes and returns focus to the element that opened it; the page behind is inert and does not scroll. Prefer native `<dialog>` with `showModal()` where possible. Label it with `aria-labelledby`.
**Detect.** Custom modals without focus trap or return; background still scrollable (`body:has(dialog[open]) { overflow: hidden }` is a CSS fix).

### INT-5 · Bottom sheets for thumbs (P1)
**Rule.** On phones, put menus and actions in the bottom third where the thumb rests. Sheets keep part of the page visible, have snap points (peek and full), a drag handle with drag-to-dismiss, a scrim, and lock the page scroll while open. Round only the top corners.
**Detect.** Mobile menus and action lists anchored at the top corners; desktop dropdowns reused unchanged on phones.

### INT-6 · Dropdowns and selects (P1)
**Rule.** The trigger is obviously clickable (comfortable hit area, a caret, a hover state). The menu flips upward or sideways when it would clip. Full keyboard (arrows, Enter, Escape, type-ahead). Add a search field once the list passes about ten items. Open in about 150 ms.
**Detect.** Menus clipped by the viewport or an `overflow: hidden` parent; long unsearchable lists.

### INT-7 · Tooltips are hints (P1)
**Rule.** Appear after about 300 ms on hover and immediately on keyboard focus; point at the trigger with an arrow; flip near edges; dismiss on mouse leave, blur, Escape and outside tap; one short sentence, width capped around 300 px. Never put essential information or interactive content in a tooltip; on touch there is no hover, so the information needs another home.
**Detect.** Tooltips with paragraphs or links; tooltips only on hover (not focus); icon-only buttons whose only label is a hover tooltip (they also need `aria-label`).

### INT-8 · Context menus measure first (P2)
**Rule.** Open at the cursor and stay inside the viewport (flip up or left). Group by intent with dividers, destructive action last and marked. Submenus stay open while the pointer travels diagonally toward them (a safe triangle or delay). Keyboard: arrows, letter jump, Escape closes one level. On touch, long press opens the same actions in a sheet.

### INT-9 · Destructive actions use every signal (P0)
**Rule.** The button names the action ("Delete project" / "Keep project", not Yes/No). Destructive buttons never sit where the primary confirm usually is. Danger colour only for destruction (VIS-6). Account- or data-level deletions live in a bordered "danger zone" at the bottom of settings. Prefer undo (STA-14) for recoverable actions; for irreversible ones add real friction: typing the resource name, hold-to-confirm (about 300 ms or more, release cancels), or a cancellable cooldown (for example 14 days before an account is deleted).
**Detect.** "Are you sure?" with Yes/No; delete in the primary button slot; one-click irreversible actions.

### INT-10 · Buttons feel alive (P1)
**Rule.** Every button has hover (where hover exists), pressed, focus, busy and, if truly needed, unavailable states. Press feedback within 100 ms (MOT-3). Primary is filled, secondary outline or ghost, tertiary a text link; one primary per view or form. On lively products a small press squash and release spring, or a ripple from the press point, make the control feel physical; on crisp products a fast value change is enough. Never linear easing.
**Detect.** Buttons with no `:hover`/`:active` styles; several primaries side by side; two equal-weight CTAs.

### INT-11 · Targets are big enough and close (P0 on touch)
**Rule.** Interactive targets at least 44×44 px on touch (24×24 px absolute minimum on desktop), even when the glyph is smaller; pad the hit area, keep the icon small. Put frequent targets near where the pointer or thumb already is: primary mobile actions at the bottom, menus at the cursor, edit in place rather than in a far modal. Use `@media (pointer: coarse)` to grow controls for touch.
**Detect.** 16 to 32 px icon buttons without padding on mobile; tiny close buttons; primary mobile actions at the top of the screen.

### INT-12 · Hover is an extra, never the only path (P0)
**Rule.** Touch has no hover; the first tap turns into a sticky hover and the action never fires. Gate hover styles with `@media (hover: hover)`. Never hide a primary action behind hover; hover-revealed extras also exist in the card, behind a menu, a swipe or a sheet on touch, and appear on keyboard focus (`:focus-within`).
**Detect.** `opacity: 0` actions revealed only on `:hover`; `mouseenter` handlers with no touch or focus equivalent.

### INT-13 · Drag and drop says where things land (P1)
**Rule.** The grabbed item visibly lifts (slight scale, deeper shadow, small tilt). Valid drop targets show before release: an insertion line between items, a highlight for a whole column, outlined slots. Structured surfaces snap; free canvases do not. Every drop gets a short undo (about 5 s). Provide a keyboard or menu alternative ("Move to…"). For file drops see FRM-16. While dragging, cover iframes and embeds with an overlay so they do not swallow the pointer.
**Detect.** Drag with no drop indication; no undo; drag as the only way to reorder.

### INT-14 · Swipe actions are discoverable and safe (P1)
**Rule.** Short swipe reveals actions; a long swipe past a clear line fires the primary one, with resistance between. Keep direction meaning consistent app-wide (one side safe, the other destructive). Teach the gesture once (a peek). Destructive swipes commit with undo. Every swipe action also exists as a visible button or menu item.
**Detect.** Swipe-only delete; full swipe deleting with no undo; inconsistent directions across lists.

### INT-15 · Pull to refresh (P2)
**Rule.** Fires only past a clear threshold, resists elastically, signals at the threshold before release, turns the pull indicator into the spinner, settles with a small overshoot, and never freezes or blanks the list; new items arrive at the top with a brief highlight.

### INT-16 · Navigation by platform and depth (P1)
**Rule.** Mobile: bottom tab bar with 3 to 5 top destinations, always visible; a hamburger only for secondary links. Desktop: persistent sidebar for 5+ sections, expanded by default. Command palette (Cmd/Ctrl+K) as an accelerator next to visible navigation, never instead of it. Breadcrumbs only when the hierarchy is deeper than two levels. The current location is always marked (`aria-current="page"`). Order matters: first and last slots are remembered best (CON-4).
**Detect.** Primary navigation hidden in a hamburger; collapsed-by-default desktop sidebars; breadcrumbs on flat sites.

### INT-17 · Tabs are a system (P1)
**Rule.** Indicator slides (MOT-11); overflow scrolls horizontally with edge fades (never wraps to two rows); arrows move between tabs, Home/End jump, Tab leaves the tab list; focus ring differs from the active state; content transitions without height jumps. On mobile: a segmented control for up to about 4 options, a sheet or select for more, not a squeezed desktop bar. Use `role="tablist"`/`tab`/`tabpanel`.

### INT-18 · Accordions and disclosures (P2)
**Rule.** Header is a `<button>` with `aria-expanded` and `aria-controls`. Panel and chevron animate together (MOT-7) using grid rows, not `height: auto` (MOT-8). Single-open for sequential steps, multi-open for FAQs. When an item low on the page expands, keep the tapped header where it was. `<details>`/`<summary>` is a valid native choice.

### INT-19 · Resizable panels (P2)
**Rule.** A 1 px visible divider with a wider (about 12 px) grab area; width clamped between a minimum and maximum; below a threshold the panel snaps closed instead of leaving a sliver; during drag, set the resize cursor on the body and cover embeds; keyboard-resizable (`role="separator"` with arrow keys); width persisted across reloads.

### INT-20 · Collaborative presence (P2)
**Rule.** Interpolate remote cursor positions between updates so they glide; colour each person from a stable hash of their ID; show presence (avatar stack with +N) before anyone acts; lock or outline an element in the editor's colour while someone has it selected; offer "follow" to ride another user's viewport.

### INT-21 · Colour pickers are decision tools (P2)
**Rule.** Show OKLCH (or HSL) next to hex so lightness and hue can be adjusted predictably; remember recent picks; show live contrast against the intended background; preview transparency on light and dark; generate a tint/shade scale from one pick.

### INT-22 · Let CSS read DOM state (P2)
**Rule.** When the state already lives in the DOM (checked, invalid, open, child count, a rendered sidebar), use `:has()` instead of mirroring it into JavaScript just to toggle classes: `.card:has(:checked)`, `.field:has(:user-invalid)`, `.layout:has(aside)`, `.grid:has(> :nth-child(5))`, `body:has(dialog[open])`. Keep a fallback where old browsers matter.

---
Sources: focus-states, accordion-disclosure, modal-hierarchy, bottom-sheets, dropdown-design, tooltip-design, context-menu, destructive-actions, settings-system, perfect-button, button-feedback, behind-the-button, fitts-law, hover-trap, drag-and-drop, drag-and-drop-tips, swipe-actions, pull-to-refresh, navigation-patterns, tabs-system, resizable-panels, live-cursors, color-picker-ux, css-has-selector. See `sources.md`.
