---
id: unknown
reel_url: unknown
pattern_page: https://designmotionhq.com/patterns/css-has-selector
date: unknown
duration_s: 79
type: ui
category: interaction
topic: CSS :has() to drive component state from the DOM instead of JS state
sources: frames, voice-over, pattern page
---

# CSS :has(): let the DOM drive UI state

**Caption:** not captured yet
**Hook:** One line of CSS makes a whole plan card react to its own radio button, with zero JavaScript.

## Main rule
When the state already exists in the DOM (checked, invalid, open, child present, child count), style the container with `:has()` instead of mirroring that state into framework state, props, change handlers and cleanup effects.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| `.plan:has(:checked) { border-color: var(--accent) }` | selected plan card highlights itself | 0:01-0:12 on-screen |
| Chrome 105 · Safari 15.4 · Firefox 121 · Edge 105 | minimum browser versions for `:has()` | 0:04-0:12 on-screen; voice: "every browser since 2023" |
| 20 years | how long CSS could only select "down and forward" (descendant/sibling) | voice 0:04 |
| `.field:has(:user-invalid) { border-color: var(--error) }` | field border, label and icon turn to the error colour together | 0:13-0:30 on-screen |
| 0 onChange · 0 useState | validation styling without handlers/state | 0:14-0:30 on-screen badge |
| `form:has(:user-invalid) button { opacity: .4; pointer-events: none }` | submit button dims while any field is invalid | 0:27-0:30 on-screen (page shows only `opacity: .4`) |
| `.app:has(aside) { grid-template-columns: 280px 1fr }` | layout gains a 280 px sidebar column when an `<aside>` exists, else `1fr` | 0:31-0:40 on-screen |
| `.plans:has(> :nth-child(n + 5)) { --density: compact }` | grid switches to compact density at 5 or more children | 0:41-0:51 on-screen |
| children 4 → `--density wide`; children 5 → `--density compact` | quantity-query threshold | 0:41-0:51 on-screen |
| 2 columns (4 cards) → 3 columns (5 cards) | grid reflow when the fifth card arrives | 0:45-0:46 on-screen |
| `body:has(dialog[open]) { overflow: hidden }` | scroll lock while a dialog is open | 0:52-0:66 on-screen |
| `body:has(dialog[open]) .app { opacity: .4 }` | page behind the dialog dims | 0:56-0:66 on-screen |
| 1 attribute · 2 rules; 0 props · 0 callbacks | dialog example summary | 0:52-0:66 on-screen |
| 5 selectors, 0 JS | summary | 0:67-0:79 on-screen |

## Before / after
1. **Selected card (0:00-0:12).** Before: only the small radio dot changes; the card itself stays neutral. After: `.plan:has(:checked)` gives the whole card an accent border. Why: the selection is visible at card scale, so the choice is recognisable at a glance; the state comes straight from the native radio, so it cannot drift out of sync.
2. **Field validation (0:13-0:26).** Before (struck-through code): `onChange={e => setError(...)}` plus `const [error, setError] = useState(false)`. After: `.field:has(:user-invalid)` turns border, label and the trailing icon to the error colour, with helper text "Enter a valid work email". Why: the browser already evaluates `type="email"`/`required`; `:user-invalid` (unlike `:invalid`) waits for user interaction, so the form is not red on first render.
3. **Submit button (0:27-0:30).** One rule on the form dims the Pay button to 40% opacity and blocks pointer clicks while any field is invalid. Why: no derived "isFormValid" state is needed. (See Notes: this hides the reason and does not block keyboard submit.)
4. **Sidebar layout (0:31-0:40).** Before: a `showSidebar`-style boolean prop toggles a layout class. After: the grid gains a `280px` column when `<aside>` (an "Order summary" panel) is rendered and collapses to `1fr` when it is removed. Tag: "State lives in the DOM, not in a prop".
5. **Quantity query (0:41-0:51).** Before (struck): `items.length > 4 ? "compact" : "wide"`. After: when a fifth plan card ("Agency") appears, all cards tighten (smaller padding, gap and type) and the grid reflows from 2 to 3 columns. Why: layout density follows content count without JS counting.
6. **Modal side effects (0:52-0:66).** Before (struck): `useEffect(() => () => (body.style.overflow = ""))` cleanup. After: two rules lock body scroll and dim the app while `dialog[open]` exists; pressing Esc closes the dialog and everything reverts by itself. Why: no cleanup to forget, so no stuck scroll lock after an unusual close path.

## Do
- Put the rule on the container (`.field`, `.plan`, `form`, `body`) so every child (border, label, icon, button) updates from one selector.
- Use `:user-invalid` rather than `:invalid` for error styling, so errors appear only after the user has interacted.
- Use `:has()` for layout that depends on what is rendered (sidebar present, number of items).
- Use quantity queries (`:has(> :nth-child(n + N))`) for density changes at a count threshold.
- Let the open state of a native `<dialog>` drive page-level effects (scroll lock, dimming).

## Don't
- Don't mirror DOM state (checked, invalid, open, child count) into framework state just to toggle a class.
- Don't write cleanup effects for scroll lock or dimming that a `:has()` rule reverses automatically.
- Don't count children in JavaScript just to pick a layout variant.

## Scene by scene
- 0:00 Checkout card "Choose a plan" with three plan cards (Starter $19, Team $49, Scale $149 per seat/month), work email, promo code, total $147.00/month, "Pay $147" button; badge "0 lines of JavaScript". Cursor selects Team; the whole Team card gets an accent border; code `.plan:has(:checked)` appears.
- 0:04 "CSS looks up now." Tree diagram: `.plan` with children `input:radio`, `.name`, `.price`; arrows labelled descendant and sibling, then a "parent" arrow from `input:radio :checked` up to `.plan`. Support pill: Chrome 105, Safari 15.4, Firefox 121, Edge 105.
- 0:13 "The whole field knows." Typing "sarah@acme" in Work email; the field border, the label and an alert icon switch to the error colour, helper text "Enter a valid work email". Badge "0 onChange · 0 useState"; struck-through React handler and useState lines.
- 0:27 Second rule `form:has(:user-invalid) button { opacity: .4; pointer-events: none }`; the Pay button fades to a disabled look.
- 0:31 "Layout follows the DOM." Browser frame; DOM chips `<main>` / columns `1fr`; an "Order summary" aside slides in (columns `280px 1fr`), is removed (back to `1fr`), returns. Tag "State lives in the DOM, not in a prop".
- 0:41 "The grid counts its children." Four plan cards in a 2x2 grid ("children 4 → --density wide"); a fifth (Agency $249) appears, grid becomes 3 columns with smaller cards ("children 5 → --density compact"); struck JS ternary. Tag "Quantity query · pure CSS".
- 0:52 "The document reacts to the modal." Cursor clicks Pay; a "Confirm payment $147.00" dialog opens with Cancel / Pay now; the page behind dims to 0.4 opacity, scrollbar locks; "0 props · 0 callbacks".
- 0:63 "Esc" key label; dialog closes, page returns to full opacity; struck useEffect cleanup line. Tag "1 attribute · 2 rules".
- 0:67 Summary "Five selectors. Zero JavaScript." listing all five selectors with a "0 JS" badge.
- 0:70 Product promo for the author's Claude Code plugin (command palette typing `/restyle`, price card). Not UI guidance.

## Voice-over summary
- `:has()` is the parent selector; for two decades CSS could only look down and forward, now it can look up, supported in every major browser since 2023.
- A field containing a user-invalid input recolours border, label and icon at once, with no change handler or React error state; the browser already knows the email is wrong.
- The form can react too: the pay button greys out while anything inside is invalid.
- A layout grows a column when a sidebar is in the DOM and collapses when it is removed, so layout follows the DOM, not a boolean prop.
- A grid with five or more children tightens all cards: a quantity query with no counting in JS.
- When a dialog is open the body locks scroll and the page dims; closing it reverts everything with no cleanup effect.

## Notes for the skill
- Browser support: `:has()` is Baseline since Dec 2023 (Firefox 121). `:user-invalid` arrived separately (Firefox 88, Chrome/Edge 119, Safari 16.5); check both if older browsers matter, and provide a fallback (e.g. `aria-invalid="true"` set on blur) where needed.
- Styling is not announcement: `:user-invalid` colouring does not tell screen readers anything. Still set `aria-invalid="true"` and link the error text with `aria-describedby`, and do not rely on colour alone (keep the icon and text, as the video does).
- The submit-button rule (`opacity: .4; pointer-events: none`) is risky: pointer-events does not stop keyboard focus or Enter-to-submit, the button gives no reason why it is unavailable, and 40% opacity usually drops text contrast below 4.5:1. Prefer leaving the button enabled and showing errors on submit, or, if you disable, explain why next to it. This also conflicts with the author's own "Disabled Buttons" pattern.
- `form:has(:user-invalid)` only reacts to fields the user has touched; untouched empty required fields do not match, so native/server validation on submit is still required.
- Prefer `body:has(dialog:modal)` over `dialog[open]`: `[open]` also matches non-modal dialogs opened with `show()`, which should not lock scroll. A modal `<dialog>` opened with `showModal()` also provides `::backdrop` for dimming, makes the rest of the page inert, traps focus and closes on Esc natively.
- `overflow: hidden` on body removes the scrollbar and can shift layout horizontally; add `scrollbar-gutter: stable` on the root to avoid the jump.
- Quantity query: `:nth-child(n + 5)` matches the 5th child onward, so the container matches at 5 or more children; use the `>` child combinator inside `:has()` so nested elements are not counted.
- Density changes (padding, gap, font size) should stay within readable sizes; do not shrink body text below about 14-16 px or touch targets below 24x24 CSS px (WCAG 2.2 AA) / 44 px (platform guidance) on touch devices.
