# Detection patterns

Fast searches that surface likely violations. A match is a lead, not a finding: open the file and confirm before reporting. Adjust globs to the stack (add `vue`, `svelte`, `astro`, `html`, `scss`, `css-in-js` files as needed). Use the Grep tool or `rg`.

Typical UI globs: `*.{tsx,jsx,ts,js,vue,svelte,astro,html,css,scss,sass,less}`. Exclude `node_modules`, build output, vendored libraries, generated files and test snapshots.

## Accessibility and input

| Rule | Search for | Then check |
|---|---|---|
| INT-1 | `outline:\s*(none\|0)`, `outline-none` (Tailwind), `focus:outline-none` | A `:focus-visible` / `focus-visible:` replacement exists |
| INT-1 | `tabindex=["{]?[1-9]` | Positive tabindex breaks order |
| INT-2 | `<div[^>]*onClick`, `<span[^>]*onClick`, `@click` on `div`/`span` | Has `role`, `tabIndex` and key handlers, or should be a `<button>` |
| INT-4 | `role="dialog"`, `Modal`, `Dialog`, `<dialog` | Focus moves in, is trapped, returns on close; Escape closes |
| INT-11 | `w-4 h-4`, `w-5 h-5`, `size-4`, `width:\s*(16\|20\|24)px` on clickable icons | Hit area padded to 44 px on touch |
| INT-12 | `:hover`, `hover:`, `onMouseEnter`, `group-hover:opacity` | Not the only way to reach an action; `@media (hover: hover)` gating |
| INT-7 | `title=`, `Tooltip` | Icon-only buttons also have `aria-label`; no essential content in tooltips |
| FRM-2 | `placeholder=` | A real `<label>` is associated |
| FRM-4 | `disabled=\{!`, `disabled={!isValid`, `:disabled="!` | Submit greyed until valid |
| FRM-5 | `onPaste`, `type="password"` | Paste not blocked; reveal toggle; `autocomplete` set |
| VIS-7 | Muted text tokens and classes (`text-gray-400`, `text-slate-400`, `opacity-50` on text, `#999`, `#aaa`) | Contrast against the real background |
| MOT-13 | `prefers-reduced-motion`, `motion-reduce:` | Exists at all; JS animation libraries honour it |

## States and feedback

| Rule | Search for | Then check |
|---|---|---|
| STA-1 | `useQuery`, `useSWR`, `fetch(`, `axios`, `createResource`, `load(` | Loading, empty, error branches exist where they apply |
| STA-1 | `.map(` in JSX next to fetched data | Empty array handled |
| STA-7 | `Something went wrong`, `An error occurred`, `Error:`, `err.message`, `error.message`, `alert(` | Specific copy and a recovery action |
| STA-7 | `catch\s*\([^)]*\)\s*\{\s*\}`, `.catch(() => {})` | Errors swallowed |
| STA-2 | `Spinner`, `Loader`, `animate-spin`, `CircularProgress` | Right pattern for the wait; no full-page spinner over known layouts |
| STA-6 | `No data`, `No results`, `No items`, `Nothing here`, `Empty` | Explains why and offers the next action |
| STA-11 | `toast(`, `enqueueSnackbar`, `notify(` | Duration by severity, errors persistent, dismissible, announced |
| STA-14 | `confirm(`, `Are you sure` | Undo instead, or named verbs on the buttons |
| STA-15 | `clipboard.writeText` | try/catch, raw value, reset, `aria-live` |
| FRM-10 | `onSubmit`, `handleSubmit`, `mutate(`, payment and create handlers | In-flight guard, busy state, idempotency where money is involved |
| FRM-11 | `autosave`, `onChange={.*save`, `debounce` | Debounced, honest status, conflict handling |

## Motion

| Rule | Search for | Then check |
|---|---|---|
| MOT-0 | `transition:`, `transition-`, `duration-`, `animation:`, `cubic-bezier`, `framer-motion`, `motion.` | Durations and curves come from tokens; count distinct values |
| MOT-1/2 | `duration-(500\|700\|1000)`, `transition: .*[0-9]{3,}ms`, `[0-9.]+s ease` | Entrances over 300 ms, symmetric exits |
| MOT-6 | `linear` in transitions | Only on continuous motion |
| MOT-8 | `transition:.*(height\|width\|top\|left\|margin)`, `transition: all`, `transition-all`, `hover:scale` on grid items | Layout animation, `height: auto`, footprint changes |
| MOT-12 | `addEventListener\(['"]scroll` | Could be a CSS scroll timeline |

## Visual system

| Rule | Search for | Then check |
|---|---|---|
| VIS-1 | `#[0-9a-fA-F]{3,8}\b`, `rgb\(`, `hsl\(` inside components | Raw colours instead of tokens |
| VIS-1/2 | `-\[[0-9]+px\]` (Tailwind arbitrary values), `margin:\s*[0-9]+px`, `padding:\s*[0-9]+px` | Off-scale spacing |
| VIS-4 | `font-size:`, `text-\[`, `fontSize` | Count distinct sizes; leading per size; measure on paragraphs |
| VIS-9 | `invert(`, `#000\b`, `#fff\b` in dark styles, `dark:` | Real dark surfaces, not inversion |
| VIS-10 | `border-radius:`, `rounded-` | Scale, nested radius, full radius on multi-line boxes |
| VIS-11 | `box-shadow:`, `shadow-` | Shadows on every panel vs only floating layers |
| VIS-18 | `z-index:\s*[0-9]{3,}`, `z-\[` | z-index wars, missing stacking contexts |
| DAT-1 | `tabular-nums`, numeric table cells, `text-center` on numbers | Tabular figures and right alignment |
| DAT-9 | `truncate`, `text-overflow: ellipsis` inside flex | `min-width: 0` present |

## Content

| Rule | Search for | Then check |
|---|---|---|
| CON-1 | `>Submit<`, `"Submit"`, `>OK<`, `Click here`, `Invalid input` | Outcome-named labels and helpful errors |
| CON-3 | `supercharge`, `seamless`, `unlock`, `revolutioniz`, `next-gen`, `all-in-one`, `bg-clip-text`, `text-transparent` | Generated-hero tells |
| CON-6 | `Welcome back` | Greeting as page title |
| CON-8 | Hard-coded counts near "chose", "users", "customers", strike-through prices | Claims backed by real data |
| CON-9 | `defaultChecked` on consent or upsell, fees added only in final checkout step, countdown timers | Dark patterns |
