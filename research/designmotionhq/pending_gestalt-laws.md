---
id: unknown
reel_url: unknown
pattern_page: https://designmotionhq.com/patterns/gestalt-laws
date: unknown
duration_s: 48
type: ui
category: visual
topic: Gestalt laws in UI (closure, similarity, continuity, figure-ground, common region)
sources: frames, voice-over, pattern page
---

# Five Gestalt laws for layout

**Caption:** not captured yet
**Hook:** The same elements can read as chaos or click instantly; five perception laws the brain already applies decide which.

## Main rule
Group and order UI with the brain's automatic perception: let implied shapes stand in for drawn ones (closure), give related items a shared property (similarity), align items on one axis (continuity), push overlays forward by dimming and blurring what is behind (figure-ground), and wrap related controls in a shared container (common region).

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 5 laws | Closure, Similarity, Continuity, Figure-Ground, Common Region | 0:02 title "5 GESTALT LAWS that fix any UI", numbered SECRET 01-05 |
| 16 identical elements (4 × 4 grid) | similarity demo before regrouping | 0:16-0:19 on-screen |
| 4 rows → 3 groups (1 row Navigation, 2 rows Content, 1 row Actions) | similarity demo after recolouring | 0:20-0:23 on-screen |
| 5 nav items (Home, Products, About, Blog, Contact) | continuity demo | 0:24-0:30 |
| 9 elements (3 icons, 3 labels, 3 toggles) | common region demo before grouping | 0:38-0:40 on-screen "9 elements. No structure." |
| 3 cards (Profile, Notifications, Privacy) | common region demo after grouping | 0:41-0:42 |

No timing, size or spacing values are given.

## Before / after
1. **Closure (0:00-0:16).** Three notched circles imply a triangle that is not drawn ("Your brain sees a shape that doesn't exist"); an open arc is read as a circle. Applied: a bottom navigation bar whose icons (home, search, heart, user) are drawn with gaps in their strokes, inside a barely visible dashed container: "Implied boundaries. Zero extra pixels." Why: the visual system completes incomplete contours, so a UI does not need to draw every edge or box; fewer lines means less visual noise.
2. **Similarity (0:16-0:23).** Before: 16 identical grey dots, no structure. After: only colour changes; the top row becomes one group (Navigation), the middle two rows another (Content), the bottom row a third (Actions). "Change one property. Instant hierarchy." Why: elements sharing a visual property are grouped pre-attentively, before conscious reading.
3. **Continuity (0:24-0:31).** Before: nav pills Home / Products / About / Blog / Contact scattered at random positions and angles: "Scattered. No flow." After: the pills snap into one vertical column connected by a thin line: "Aligned. Effortless." Why: the eye follows the smoothest continuous path; a shared axis turns separate items into a sequence and removes eye jumps.
4. **Figure-ground (0:31-0:37).** A list screen is blurred and dimmed, then a "Delete Project?" dialog (warning icon, "This action cannot be undone. All files and settings will be permanently removed.", Cancel and a danger-coloured Delete) appears on top: "Instant focus. Zero confusion." Why: reducing contrast and sharpness of the background makes it read as ground and the modal as figure, so attention goes to the one decision.
5. **Common region (0:38-0:42).** Before: 9 loose items (icons, labels Edit Name / Push Alerts / Visibility, toggles) scattered: "9 elements. No structure." After: each icon + label + toggle is wrapped in a row card with a section label (PROFILE, NOTIFICATIONS, PRIVACY): "Cards create meaning." Why: a shared boundary groups elements more strongly than proximity or similarity; the container says "these belong together" without extra labels.

## Do
- Use implied edges (spacing, alignment, partial outlines) before adding boxes and divider lines.
- Encode a group with one shared property (colour, shape or size) and change that one property to split groups.
- Align navigation and lists on a single axis.
- Dim and blur the page behind a modal dialog.
- Put each set of related settings in its own card or bordered region with a section heading.

## Don't
- Don't scatter navigation or list items at different positions or angles.
- Don't show a modal over an undimmed page; it competes with the background.
- Don't rely on proximity alone when related controls are far apart; add a container.
- Don't change several properties at once when you only want to express grouping; it creates noise instead of hierarchy.

## Scene by scene
- 0:00 Three notched circles form an implied triangle; title "5 GESTALT LAWS / that fix any UI"; caption "Your brain sees a shape that doesn't exist."; counter badge 5.
- 0:07 "SECRET 01 / CLOSURE / Your brain completes the picture": an incomplete circle stroke, "You see a circle."
- 0:12 Gapped line icons appear one by one (home, search, heart, user), then a faint dashed nav-bar container: "Implied boundaries. Zero extra pixels."
- 0:16 "SECRET 02 / SIMILARITY / Same property = same group": dots appear into a 4 × 4 grid, "16 identical elements".
- 0:20 Rows recolour into three groups labelled Navigation, Content, Actions: "Change one property. Instant hierarchy."
- 0:24 "SECRET 03 / CONTINUITY / Follow the smoothest path": tilted scattered nav pills, "Scattered. No flow."
- 0:27 Pills fly into one vertical column joined by a connector line: "Aligned. Effortless."
- 0:31 "SECRET 04 / FIGURE-GROUND / Blur creates focus": an app list screen, then it blurs and the Delete Project dialog appears: "Instant focus. Zero confusion."
- 0:38 "SECRET 05 / COMMON REGION / Borders create belonging": 9 scattered elements, "9 elements. No structure."
- 0:40 Elements gather into three row cards with headings PROFILE, NOTIFICATIONS, PRIVACY: "Cards create meaning."
- 0:43 Summary list 01-05 (Closure, Similarity, Continuity, Figure-Ground, Common Region), "Save this for your next project / Follow @designmotionhq".

## Voice-over summary
- Same elements, one layout chaotic, one instantly clear; five laws the brain already uses.
- Closure: incomplete shapes still read as whole, so implied boundaries "cost zero extra pixels".
- Similarity: same colour or shape groups instantly; change one property and the hierarchy shifts.
- Continuity: the eye follows the smoothest path, so alignment on invisible lines makes navigation effortless.
- Figure-ground: blur the background and the foreground pops; every modal and overlay relies on it. Common region: a border or card connects elements without a label.

## Notes for the skill
- The video skips Proximity, usually the strongest and cheapest grouping tool: related items closer together than unrelated ones (e.g. gap inside a group smaller than the gap between groups). Add it to the skill alongside these five.
- Similarity by colour alone is not accessible: WCAG 1.4.1 Use of Color forbids colour as the only means of conveying information. Back colour grouping with position, spacing, headings, shape or labels.
- Closure on icons: gapped icons are fine decoratively, but interactive icons still need accessible names (`aria-label`) and the icon must stay recognisable at small sizes; an "implied" container must not hide the tap target size (keep at least 24 × 24 CSS px per WCAG 2.5.8, ideally 44 × 44).
- Non-text contrast (WCAG 1.4.11, 3:1) applies to boundaries that identify a control or its state; a barely visible "implied" border is acceptable only when it is not the sole indicator of a control.
- Figure-ground for modals: use a scrim (`::backdrop` with a dim overlay and optional `backdrop-filter: blur()`), and implement the dialog semantics too (`<dialog>` with `showModal()` or `role="dialog"` + `aria-modal="true"`, focus moved into the dialog, focus trapped, Escape closes, focus returned to the trigger). Blur is costly on low-end devices; dimming alone is enough.
- Common region in code: `<fieldset>`/`<legend>` or a `section` with a heading for settings groups gives the same grouping to screen-reader users.
