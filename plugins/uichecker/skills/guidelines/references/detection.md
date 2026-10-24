# Detection patterns

Fast searches that surface likely violations. A match is a lead, not a finding: open the file and confirm before reporting, and check that the rule applies to that element (its **Applies to** line). Use the Grep tool or `rg`.

How to read the patterns:
- They are ripgrep regexes. Inside these tables `\|` is only the Markdown escape for `|`: type a plain `|` when you search.
- Search case-insensitively (`-i`) unless the pattern depends on case.
- Patterns marked *(literal)* are fixed strings: search them with `-F`.

Typical UI globs: `*.{tsx,jsx,ts,js,vue,svelte,astro,html,css,scss,sass,less}`, plus `*.{swift,kt,dart}` for native stacks. Exclude `node_modules`, build output, vendored libraries, generated files and test snapshots. On non-web stacks, translate each search to the platform's API (see "Non-web stacks" in SKILL.md).

## Accessibility and input

| Rule | Search for | Then check |
|---|---|---|
| INT-1 | `outline:\s*(none\|0)`, `outline-none` (Tailwind), `focus:outline-none` | A `:focus-visible` / `focus-visible:` replacement exists |
| INT-1 | `tab[iI]ndex=["{]?[1-9]` | Positive tabindex breaks order |
| INT-2 | `<div[^>]*onClick`, `<span[^>]*onClick`, `@click` on `div`/`span` | Has `role`, `tabIndex` and key handlers, or should be a `<button>` |
| INT-4 | `role="dialog"`, `Modal`, `Dialog`, `<dialog` | Focus moves in, is trapped, returns on close; Escape closes |
| INT-11 | `w-4 h-4`, `w-5 h-5`, `size-4`, `width:\s*(16\|20\|24)px` on clickable icons | Hit area padded to 44 px on touch |
| INT-12 | `:hover`, `hover:`, `onMouseEnter`, `group-hover:opacity` | Not the only way to reach an action; `@media (hover: hover)` gating |
| INT-7 | `title=`, `Tooltip` | Icon-only buttons also have `aria-label`; no essential content in tooltips |
| INT-9 | `delete`, `destroy`, `remove` handlers; `confirm\(` | Undo or a named confirmation; destructive styling only on destructive actions |
| INT-28 | `breadcrumb` | Last crumb is plain text with `aria-current="page"`; the first level never folds; one back link on phones |
| FRM-2 | `placeholder=` | A real `<label>` is associated |
| FRM-4 | `disabled=\{!`, `:disabled="!` | Submit greyed until valid |
| FRM-5 | `onPaste`, `type="password"` | Paste not blocked; reveal toggle; `autocomplete` set |
| VIS-7 | Muted text tokens and classes (`text-gray-400`, `text-slate-400`, `opacity-50` on text, `#999`, `#aaa`) | Contrast against the real background |
| MOT-13 | `prefers-reduced-motion`, `motion-reduce:`, `scroll-behavior:\s*smooth`, `behavior:\s*['"]smooth` | Exists at all; JS animation libraries and smooth scrolling honour it |
| FRM-21 | `Pay`, `checkout`, `cc-number`, `PaymentRequest`, `ApplePay`, `GooglePay` | Total on the pay button, wallets first, one column, `autocomplete="cc-*"` |
| FRM-1 | `:autofill`, `-webkit-autofill` | Autofill styled on themed or dark forms |
| FRM-6 | `type="number"` | Only on real quantities, never codes, postal codes or card numbers |
| FRM-19 | `role="switch"`, `Switch`, `Toggle` near a Save button; `indeterminate` | Commit model matches the control; parent checkbox has a mixed state |
| INT-23 | `requestPermission`, `getUserMedia`, `geolocation.getCurrentPosition`, `requestAuthorization`, `POST_NOTIFICATIONS` | Asked from a user action with a benefit card first; denied state links to settings |
| INT-27 | `user-scalable=no`, `maximum-scale=1`, `position:\s*fixed;?\s*bottom:\s*0`, `text-sm` or `font-size:\s*1[0-5]px` on inputs | No zoom lock; safe-area padding; 16 px inputs on phones |

## States and feedback

| Rule | Search for | Then check |
|---|---|---|
| STA-1 | `useQuery`, `useSWR`, `fetch\(`, `axios`, `createResource`, `load\(` | Loading, empty, error branches exist where they apply |
| STA-1 | `\.map\(` in JSX next to fetched data | Empty array handled |
| STA-7 | *(literal)* `Something went wrong`, `An error occurred`, `err.message`, `error.message`, `alert(` | Specific copy and a recovery action |
| STA-7 | `catch\s*(\([^)]*\))?\s*\{\s*\}`, `\.catch\(\s*\(\)\s*=>\s*\{\s*\}\s*\)` | Errors swallowed |
| STA-2 | `Spinner`, `Loader`, `animate-spin`, `CircularProgress` | Right pattern for the wait; no full-page spinner over known layouts |
| STA-6 | `No data`, `No results`, `No items`, `Nothing here`, `Empty` | Explains why and offers the next action |
| STA-11 | `toast\(`, `enqueueSnackbar`, `notify\(` | Duration by severity, errors persistent, dismissible, announced |
| STA-14 | *(literal)* `confirm(`, `Are you sure` | Undo instead, or named verbs on the buttons |
| STA-15 | `clipboard.writeText` | try/catch, raw value, reset, `aria-live` |
| STA-18 | `typing`, `isTyping`, `showTypingIndicator`, `delay\(`, `sleep\(` near message sending | Indicator bound to real activity; no artificial delay |
| STA-17 | `upload`, `onUploadProgress`, `progress` events with `animate-spin` | Determinate bar when `loaded`/`total` exist |
| FRM-10 | `onSubmit`, `handleSubmit`, `mutate\(`, payment and create handlers | In-flight guard, busy state, idempotency where money is involved |
| FRM-11 | `autosave`, `onChange=\{[^}]*save`, `debounce` | Debounced, honest status, conflict handling |

## Motion

| Rule | Search for | Then check |
|---|---|---|
| MOT-0 | `transition:`, `transition-`, `duration-`, `animation:`, `cubic-bezier`, `framer-motion`, `motion.` | Durations and curves come from tokens; count distinct values |
| MOT-1, MOT-2 | `duration-(500\|700\|1000)`, `transition: .*[0-9]{3,}ms`, `[0-9.]+s ease` | Entrances over 300 ms, symmetric exits |
| MOT-6 | `linear` in transitions | Only on continuous motion |
| MOT-8 | `transition:.*(height\|width\|top\|left\|margin)`, `transition: all`, `transition-all`, `hover:scale` on grid items | Layout animation, `height: auto`, footprint changes |
| MOT-12 | `addEventListener\(['"]scroll` | Could be a CSS scroll timeline |
| MOT-15 | `confetti`, `canvas-confetti`, `party` | Only on rare milestones; reduced motion |
| MOT-16 | `startViewTransition`, `view-transition-name` | Feature check, unique names, reduced motion |

## Visual system

| Rule | Search for | Then check |
|---|---|---|
| VIS-1 | `#[0-9a-fA-F]{3,8}\b`, `rgb\(`, `hsl\(` inside components | Raw colours instead of tokens |
| VIS-1, VIS-2 | `-\[[0-9]+px\]` (Tailwind arbitrary values), `margin:\s*[0-9]+px`, `padding:\s*[0-9]+px` | Off-scale spacing |
| VIS-4 | `font-size:`, `text-\[`, `fontSize` | Count distinct sizes; leading per size; measure on paragraphs |
| VIS-8 | `text-red`, `text-green`, `color: red`, `color: green`, status dots without text | Meaning also carried by text, an icon or a shape |
| VIS-9 | `invert\(`, `#000\b`, `#fff\b` in dark styles, `dark:` | Real dark surfaces, not inversion |
| VIS-10 | `border-radius:`, `rounded-` | Scale, nested radius (`R − b − p`), flush images and control thumbs, full radius on multi-line boxes |
| VIS-11 | `box-shadow:`, `shadow-` | Only floating layers; x offset 0 everywhere; contact plus soft layer; negative spread on the soft layer |
| VIS-18 | `z-index:\s*[0-9]{3,}`, `z-\[` | z-index wars, missing stacking contexts |
| DAT-1 | `tabular-nums`, numeric table cells, `text-center` on numbers | Tabular figures and right alignment |
| DAT-9 | `truncate`, `text-overflow: ellipsis` inside flex | `min-width: 0` present |
| DAT-8 | `scrollTo\(0,\s*0\)`, `scrollRestoration` | Position restored on back; sticky headers cleared with `scroll-padding-top` |
| VIS-2 | `:last-child\s*\{\s*margin` | Sibling spacing moved to `gap` on the parent |
| VIS-4 | `<h[1-6][^>]*>[^<]*<br`, `clamp\([^,]+,\s*[0-9.]+vw\s*,` | `text-wrap: balance` instead of hard breaks; a rem term in fluid sizes |
| VIS-21 | `addEventListener\(['"]scroll`, `100vh`, `height:\s*100%`, `translate\(-50%,\s*-50%\)`, `!important`, `innerWidth`, `scroll-snap-type:[^;]*mandatory` | Sticky, `dvh`, grid centring, container queries or `@layer` would state it directly |
| DAT-13 | `beginAtZero`, `min:` on value axes, `domain=` | Bar charts start at zero; deltas computed; series not told apart by colour alone |
| DAT-14 | `delta`, `trend`, `change`, `KpiCard`, `StatCard`, `progressbar` near goal or target | A period on every delta, colour by metric direction, at most 4 cards, `<meter>` for goals |
| VIS-20 | Nested `Card` components, `<a` wrapping a whole card with buttons inside | One entity, one target, no nested cards |

## Content

| Rule | Search for | Then check |
|---|---|---|
| CON-1 | *(literal)* `>Submit<`, `"Submit"`, `>OK<`, `Click here`, `Invalid input` | Outcome-named labels and helpful errors |
| CON-3 | `supercharge`, `seamless`, `unlock`, `revolutioniz`, `next-gen`, `all-in-one`, `bg-clip-text`, `text-transparent` | Generated-hero tells |
| CON-6 | *(literal)* `Welcome back` | Greeting as page title |
| CON-8 | Hard-coded counts near "chose", "users", "customers", strike-through prices | Claims backed by real data |
| CON-9 | `defaultChecked` on consent or upsell, fees added only in final checkout step, countdown timers | Dark patterns |
| CON-13 | `pricing`, `PricingCard`, `Most popular`, `annual`, `yearly` | One featured tier, one badge, one filled button, saving in money |
| CON-10 | `keydown` handlers matching single letters; `aria-keyshortcuts`, `<kbd` | Ignored while typing; keys shown in menu rows and tooltips, one binding per action |
| CON-12 | `streak`, `autoplay`, `IntersectionObserver` for infinite loading | Forgiving streaks, cancellable autoplay, an end state or Load more |
