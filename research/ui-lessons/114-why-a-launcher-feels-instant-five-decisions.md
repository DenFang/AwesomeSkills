---
lesson: 114
kind: video
duration_s: 52
type: ui
category: interaction
topic: command palette / launcher that feels instant (cached-first results, progress line, action bar, action panel, blur not dim)
sources: frames, voice-over
---

# Why a launcher feels instant: five decisions

**Hook:** Typing "clip" into a Raycast-style launcher shows results at once with no spinner; five design decisions explain why it feels instant.

## Main rule
For a search-driven palette: show the last cached results immediately and replace them row by row as fresh results arrive, signal background work with a thin progress line instead of a spinner or empty list, keep a bottom bar that always names the primary action and its key, put secondary actions in a ⌘K action panel that lists each shortcut, and blur (not dim) whatever sits behind the window.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 0 ms → 40 ms, "no spinner" | time-to-results badge on the demo launcher | 0:00-0:03 on-screen |
| 5 decisions | structure of the video (progress dots 1-5) | throughout, on-screen + voice |
| rows on screen: 7; fresh: 0/7 → 1/7 → 2/7 → 4/7 → 5/7 → 7/7 | cached rows replaced one by one by fresh rows (tags "cached" → "fresh") | 0:04-0:13 on-screen |
| "no spinner, no empty list" | progress-line decision | 0:11-0:13 on-screen |
| "Open Command ↵" / "Copy to Clipboard ↵" / "Open Application ↵"; "Actions ⌘K" | bottom action bar; label changes with the selected row type, keys stay in the same place | 0:14-0:23 on-screen |
| times seen: 1 → 2 → 3 → 4 → 6 → 9 → 12 (of 12) | repeated exposure to the action bar; at 9-12 the tag changes to "no tutorial needed"; "mouse: idle · keyboard only" | 0:14-0:23 on-screen |
| ↵ Paste to Terminal · ⌘↵ Copy to Clipboard · ⇧⌘P Pin Entry · ⌃X Delete Entry | ⌘K action panel for a clipboard entry, shortcut chips per action; delete styled in the danger colour | 0:24-0:34 on-screen |
| "next time: ⇧⌘P", "skipped the panel" | learning the shortcut from the panel | 0:33-0:34 on-screen |
| dim: black veil 60% → "context lost" | bad backdrop | 0:35-0:44 on-screen |
| blur 5px → 19px → 20px → "context kept", "readable" | good backdrop: desktop blurred behind the window | 0:35-0:44 on-screen |

## Before / after
- **Spinner/empty list vs cached-first.** The launcher renders the previous results for "clip" instantly (tagged "cached"), then swaps each row for a fresh one (fresh 0/7 → 7/7). Why: the user can act on familiar results immediately; perceived latency drops to near zero because the screen is never empty.
- **Spinner vs thin progress line.** A thin line under the search field shows ongoing work while the list stays in place ("no spinner, no empty list"). Why: a subtle, peripheral indicator communicates activity without stealing focus or blanking content.
- **Hidden vs named primary action.** The bottom bar always shows the main action for the selected row (Open Command, Copy to Clipboard, Open Application) with ↵, plus "Actions ⌘K", in the same spot for every row ("same keys, same spot, every row"). Why: constant, consistent exposure teaches the shortcuts passively; after a dozen views no tutorial is needed.
- **Action panel with shortcuts.** ⌘K opens a second palette for the selected row listing Paste, Copy, Pin, Delete, each with its shortcut. Why: the panel is discoverable for novices and teaches the direct shortcut, so experts skip it next time (⇧⌘P "skipped the panel").
- **Dim vs blur backdrop.** A 60% black veil hides the app behind ("context lost"); a ~20px blur keeps the app shape recognisable ("context kept", "app behind") while the list on top stays readable. Why: blur removes detail that would compete with the foreground text but keeps spatial context of where the user is.

## Do
- Cache the last results per query and render them on open; reconcile with fresh results row by row without reordering under the cursor.
- Use a thin, indeterminate progress line near the input for background fetches; keep the list visible.
- Keep a persistent footer that names the primary action for the current selection and its key, plus the key for more actions.
- Offer a secondary action menu (⌘K) per item, listing every action's shortcut; style destructive actions with the danger colour.
- Blur the backdrop behind floating launchers/panels (around 20px) instead of a heavy dark veil.

## Don't
- Don't clear the list and show a spinner on every keystroke.
- Don't hide shortcuts behind documentation or a tutorial.
- Don't move the action bar or change its key bindings per row type.
- Don't cover the context with a 60% black overlay for a lightweight utility window.

## Scene by scene
- 0:00 "Reverse-engineered · Raycast: Why does Raycast feel instant?" Empty "Search..." launcher with a "0 ms" badge.
- 0:01 Typing "clip": results Clipboard History (Command), Clip Snippet (Command), Clipboard Manager (Application) appear; badges "no spinner", "40 ms"; footer "Open Command ↵".
- 0:03 "Five decisions." Progress dots 1-5, "to copy in your launcher".
- 0:04 "Teardown · stale first: Last results show up first." Fuller launcher with Commands and Clipboard History sections; each row tagged "cached"; counters "rows on screen: 7", "fresh: 0/7".
- 0:09 Rows flip to "fresh" one by one (1/7, 2/7, 4/7, 5/7, 7/7) and content updates (e.g. older clipboard items replaced by newer ones); decision 2/5 "progress line", badge "no spinner, no empty list".
- 0:14 "Teardown · action bar: The bottom bar names the action." Footer highlighted: "Clipboard · Open Command ↵ · Actions ⌘K". Moving the selection changes the label (Copy to Clipboard, Open Application) while keys stay put; "times seen" counter climbs from 1 to 12, tag "browsing results" → "no tutorial needed"; "mouse: idle · keyboard only".
- 0:24 "Teardown · action panel: ⌘K opens a second palette." "you press: ⌘ K"; panel with "Search actions..." and Paste to Terminal, Copy to Clipboard, Pin Entry, Delete Entry, next to an info pane for "npm run dev".
- 0:30 "Every action shows its key." Shortcut chips light up; then "next time: ⇧ ⌘ P", "skipped the panel"; the row gets a pin icon.
- 0:35 "Teardown · blur, not dim: Blur the desktop. Never dim it." Top: "dim, black veil, 60%", tagged "context lost". Bottom: "Raycast-style, desktop blurred behind", blur slider 5px → 20px, tags "context kept", "app behind", "readable".

## Voice-over summary
- Asks why the launcher feels instant and promises five decisions.
- Typing shows the previous results immediately; fresh ones replace them row by row while a thin line under the search bar shows the work.
- The bottom bar always names the main action and its key; seeing Enter and ⌘K every time makes shortcuts stick without a tutorial.
- ⌘K opens a second palette on the selected row (Copy, Paste, Pin), each listing its shortcut so next time the panel can be skipped.
- The window blurs the desktop instead of darkening it, keeping the app behind recognisable while the list stays readable.
-

## Notes for the skill
- Stale-while-revalidate: key the cache by normalised query; mark stale rows internally, but avoid reordering rows the user is about to select. If the selected item changes identity on refresh, keep selection by item id, not by index.
- Show the progress line only after a short delay (about 100-200 ms) so fast responses do not flicker it; set `aria-busy="true"` on the results list while fetching.
- Combobox accessibility (WAI-ARIA APG): input with `role="combobox"`, `aria-expanded`, `aria-controls` pointing to a `role="listbox"`, `aria-activedescendant` for the highlighted option; announce result counts politely. The action panel is a menu (`role="menu"` / `menuitem`) opened from the selected option; Escape closes the panel first, then the palette.
- Show shortcuts with `aria-keyshortcuts` on the actions and as visible `<kbd>` chips; render platform-appropriate modifiers (⌘ on macOS, Ctrl elsewhere).
- Destructive actions in the panel (Delete Entry) should keep a confirm or undo, even with a shortcut.
- Blur backdrop: `backdrop-filter: blur(20px)` with a semi-transparent surface behind the text; check text contrast against the worst-case blurred background (blur does not guarantee 4.5:1; add a tinted surface layer). Provide a solid-colour fallback for `prefers-reduced-transparency` and for browsers/GPUs where backdrop-filter is costly.
- "Blur, never dim" fits lightweight, non-modal utility windows. For true modal dialogs that block the page, a dim scrim is still the standard way to signal that the background is inert; do not apply this rule blindly to modals.
- The 40 ms figure is the demo's badge, not a measured benchmark of the real product.
