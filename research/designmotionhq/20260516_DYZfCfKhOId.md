---
id: DYZfCfKhOId
reel_url: https://www.instagram.com/reel/DYZfCfKhOId/
pattern_page: https://designmotionhq.com/patterns/search-experience-system
date: 2026-05-16
duration_s: 45
type: ui
category: interaction
topic: search as a five-part system (placeholder, recent searches, ranked autocomplete, keyboard + focus, zero-results recovery)
sources: frames, voice-over, pattern page
---

# Search experience system: five parts most apps skip

**Caption:** Search is a system and not just an input.
**Hook:** Search is not one input but a system of five parts, and most apps ship only the bare box.

## Main rule
Design search end to end: a placeholder that states what is searchable, recent searches on focus, autocomplete ranked by popularity with category badges and only a few results, full keyboard operation with a always-visible focus indicator, and a zero-results state that offers recovery paths instead of a dead end.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 5 parts | placeholder, recent, autocomplete, keyboard, recovery | 0:00-0:03 on-screen "5 parts, most apps skip them" + voice; recap 0:40-0:45 |
| "Search 12,000 products" | example of a specific placeholder (also "Find a city, address, or POI", "Filter by tag, color, or size") | 0:07-0:10 on-screen |
| 3 placeholder jobs | What, How, Scope chips under the better placeholder | 0:07-0:10 on-screen |
| 5 recent searches | chips shown on focus (Nike Air Max, White sneakers, Cotton hoodie, Running shoes, Watch strap) | 0:11-0:17 on-screen |
| 2.4s | "No recent": time to type a query | 0:13-0:17 on-screen |
| 0.3s | "One tap": reuse last query | 0:13-0:17 on-screen |
| 8x | "Friction: drop measured" | 0:13-0:17 on-screen |
| 3 results | autocomplete list length; voice "three results beat 10", chip "Three results > ten" | 0:19-0:23 on-screen + voice + page |
| 46% / 11% / 5%, then 67% / 18% / 9% | click rate of suggestion #1 / #2 / #3 (bars animate to the final values) | 0:21-0:23 on-screen |
| 4 keys | Up/Down = navigate, Enter = select, Esc = close | 0:24-0:29 on-screen + voice |
| 2px | focus ring width ("2px focus ring, never invisible") | 0:25-0:29 on-screen |
| WCAG 2.4.7 | cited for visible focus ("A11y default, WCAG 2.4.7 compliant") | 0:25-0:29 on-screen |
| 3 recovery options | Try: shoes (popular search), Browse: Footwear (full category), Recent: Nike Air Max (last visited) | 0:33-0:39 on-screen |
| 4% vs 23% | recovery rate for dead-end vs with-suggestions zero-results screen | 0:36-0:39 on-screen |
| 5.8x | "Lift: more sessions saved" | 0:36-0:39 on-screen |

The on-screen metrics (2.4 s vs 0.3 s, 8x, click rates, 4% vs 23%, 5.8x) are illustrative numbers with no source given; do not quote them as research findings.

## Before / after
1. **Placeholder (0:03-0:10).** Bad ("Lazy"): placeholder reads just "Search" (struck through). Good ("Better"): "Search by name, SKU, or brand", annotated What / How / Scope, with more examples ("Search 12,000 products", "Find a city, address, or POI", "Filter by tag, color, or size"). Why: the placeholder is the only instruction most users read; naming searchable fields sets the query vocabulary and prevents failed searches before they happen.
2. **Empty focus state (0:10-0:17).** Bad: focusing the box shows nothing. Good: on focus a "Recent searches" panel appears with five chips; one click on "Nike Air Max" fills the bar ("Tap to reuse, one click fills the bar"). Metric chips: no recent 2.4 s to type, one tap 0.3 s, friction drop 8x. Why: recognition is cheaper than recall and tapping is cheaper than typing, especially on mobile.
3. **Autocomplete ranking (0:17-0:23).** For the query "sho" the list shows Shoes (#1, Apparel, Top), Shop New (#2, Section), Shorts (#3, Apparel), titled "Suggestions, ranked by popularity", with the typed prefix highlighted in each row. A click-rate chart (67/18/9%) justifies the order. Why: ranking by actual clicks puts the likely intent first; alphabetical order ranks by spelling, not relevance. The category badge disambiguates scope (a product category vs a site section). A short list is scannable at a glance.
4. **Keyboard and focus (0:23-0:29).** The highlighted row moves with Up/Down (Shop New, Shorts...), Enter selects, Esc closes the panel, with key caps animating on press. Chips: 2px focus ring never invisible, no mouse trap (every action keyboard-reachable), WCAG 2.4.7. Why: power users and keyboard/screen-reader users must be able to search without the mouse, and they can only do so if they can see where focus is.
5. **Zero results (0:30-0:39).** Bad ("Dead end"): "No matches for "xqzz", try different keywords." Good ("Recovery"): "Try one of these instead:" popular search, category browse, and last visited item, each a one-click link. Metrics: dead end 4% recovery vs with suggestions 23%, lift 5.8x; caption "Lose the user here, lose them for good." Why: a failed search is the moment of highest intent and highest frustration; offering next steps keeps the session alive.

## Do
- Write a placeholder that names searchable fields or scope ("Search by name, SKU, or brand", "Search 12,000 products").
- Show recent searches (and optionally popular ones) as soon as the field is focused and empty; one click fills and runs the query.
- Rank suggestions by popularity/clicks, highlight the matching part, tag each with a category/scope badge, and keep the list short (the video uses 3).
- Support Up/Down to move, Enter to select, Esc to close, and keep a clearly visible focus indicator on the input and the active option.
- On zero results, offer recovery: popular searches, category links, spelling alternatives, recently viewed.

## Don't
- Don't ship "Search" as the only placeholder text.
- Don't leave the focused empty state blank.
- Don't sort autocomplete alphabetically or dump ten noisy rows.
- Don't remove or hide focus styles in the suggestion list.
- Don't end a failed search on "No matches" with nothing to click.

## Scene by scene
- 0:00 A bare input "Search" on a dark background; typing "sho" produces nothing. Title "Search is a system. 5 parts, most apps skip them."
- 0:03 "01 Placeholder / Your first onboarding.": "Lazy" input with placeholder "Search" struck through, arrow to "Better" input "Search by name, SKU, or brand"; chips What, How, Scope; "More examples" cards.
- 0:10 "02 Recent / Empty state isn't empty.": the input gets focus and a "Recent searches" panel fades in with five chips; metric cards No recent 2.4s, One tap 0.3s, Friction 8x.
- 0:15 Cursor clicks "Nike Air Max"; the input fills with "Nike Air Max" and the chip leaves the list.
- 0:17 "03 Autocomplete / Rank by clicks, not alphabet.": typing "sho" shows "Suggestions, ranked by popularity": Shoes (#1, Apparel, Top), Shop New (#2, Section), Shorts (#3, Apparel); chips "Three results > ten", "Category badge = scope"; click-rate bars grow to 67%, 18%, 9%.
- 0:23 "04 Keyboard / Keep focus visible.": highlight moves through rows; key caps Up, Down (nav), Enter (select, lights up and selects Shop New), Esc (close, panel fades); chips "2px focus ring", "No mouse trap", "A11y default, WCAG 2.4.7 compliant".
- 0:30 "05 Zero results / Never a dead end.": query "xqzz"; "Dead end" card "No matches for "xqzz"" vs "Recovery" card with Try: shoes, Browse: Footwear, Recent: Nike Air Max; caption "Lose the user here, lose them for good."; metrics 4%, 23%, 5.8x.
- 0:40 Recap row of five tiles (Placeholder, Recent, Autocomplete, Keyboard, Recovery); "Save for your next search bar", tagline "The best UI feels invisible until it fails."

## Voice-over summary
- Search is a five-part system that most apps skip.
- The placeholder is the first onboarding: "Search" says nothing, naming searchable fields says everything.
- On focus, load recent searches so one click fills the bar and friction drops to zero.
- Rank autocomplete by clicks, not alphabet, give each option a category badge, and prefer three results over ten.
- Arrow keys navigate, Enter selects, Escape closes, and the focus ring must stay visible.
- Zero results must not be a dead end: suggest alternatives, popular searches or category jumps, because a bad empty state loses users at the worst moment.

## Notes for the skill
- Use the WAI-ARIA APG combobox pattern: input with `role="combobox"`, `aria-expanded`, `aria-controls` pointing to a `role="listbox"`, options with `role="option"`, and `aria-activedescendant` on the input for the highlighted option (DOM focus stays in the input). Esc closes the popup (a second Esc may clear the input); Enter selects the active option; Up/Down move; Home/End optional. Announce result count changes in a polite live region ("3 suggestions").
- A placeholder is a hint, not a label: keep a visible or `aria-label` label ("Search products"); placeholder text disappears on typing and often fails contrast (aim for 4.5:1 if it carries instructions).
- Focus indicator: WCAG 2.4.7 (AA) only requires focus to be visible; 2.4.11/2.4.13 (WCAG 2.2) add size/contrast expectations. A 2px outline with at least 3:1 contrast against adjacent colours is a sound default; the highlighted option also needs a non-colour cue (background + icon or bold) beyond hue.
- Recent searches: store per user/device, show 5 or so, allow removing individual items and clearing all (privacy). Do not show recents in shared/public contexts without consent.
- Ranking by clicks needs a fallback for cold start and should still respect prefix match; debounce input (about 150-300 ms) and cancel stale requests so results do not flicker out of order.
- "Three results beat ten" is a simplification: the right count depends on context (command palettes and e-commerce commonly show 5-8 grouped suggestions). Keep the list short enough to scan without scrolling.
- Zero results: also try typo tolerance / "Did you mean" before showing alternatives, and keep the user's query visible and editable.
