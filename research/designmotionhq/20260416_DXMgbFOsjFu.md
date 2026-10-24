---
id: DXMgbFOsjFu
reel_url: https://www.instagram.com/reel/DXMgbFOsjFu/
pattern_page: https://designmotionhq.com/patterns/empty-states
date: 2026-04-16
duration_s: 40
type: ui
category: feedback
topic: empty states (visual, tone, primary action, four kinds, onboarding)
sources: frames, voice-over, pattern page
---

# Empty states: five rules

**Caption:** Empty state shouldn’t be empty
**Hook:** The empty state is the user's first impression of a feature, and most apps waste it.

## Main rule
Never ship a bare "No data" screen: every empty state needs a small icon or illustration, a human headline and explanation, and one primary action that is the user's real next step; design separate variants for first run, no results, error and filtered-out, and use the first-run variant to show what a real item will look like.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 5 | rules in the video (illustration, human tone, primary CTA, context, onboarding) | 0:02 on-screen "5 rules most apps miss"; 0:37 recap |
| 1 | icon / illustration needed ("Add a single icon") | 0:04-0:06 on-screen hint + voice "one tiny illustration" |
| 4 | kinds of empty: first run, no results, error, filtered | 0:22-0:29 on-screen + voice |
| 42 | example count in the filtered state copy ("You have 42 items but filters are hiding them all.") | 0:23-0:29 on-screen |
| "under a minute" | promise in the first-run copy ("Let's set up your workspace in under a minute.") | 0:23-0:29 on-screen |
No timing, size or spacing values are shown.

## Before / after
- **Dead vs alive (0:00):** Dead: dimmed card with an X glyph, "No data" in monospace and a log-style line ("error: empty result"). Alive: icon in a tile, headline "Nothing here yet", sub-line "Create your first project to get started", primary button "+ New project". Why: the dead version is indistinguishable from a failure; the alive one states that emptiness is expected and what to do.
- **Rule 1, illustration vs void:** a "My Projects" window that shows only faint "No items" text, versus the same window with one icon in a tile, headline "Nothing here yet" and "Your projects will appear here once you create one." Why: a visual anchor signals the state is intentional, not a rendering bug or a blank load.
- **Rule 2, corporate vs human:** Corporate: warning triangle, "ERROR 404", "No items found. Result set empty.", footer "status: failed". Human: chat-bubble icon, "Looks quiet in here", "Add your first project and your team will see it instantly.", button "+ Add your first project". Why: system / log vocabulary reads as an error and blames the system; plain language with a benefit explains the situation and motivates the action.
- **Rule 3, refresh vs primary CTA:** "Inbox" window with a faint refresh icon, "Nothing to show" and a ghost "Try refreshing" button, versus a plus icon, "Your inbox is clear", "Create your first project to invite teammates.", a filled "+ Create project" primary button and a secondary text link "or import from file". Why: refreshing an empty list returns the same empty list; the CTA should be the action that actually fills the screen.
- **Rule 4, one generic screen vs four contexts:** First run: rocket icon, "Welcome aboard", "Let's set up your workspace in under a minute.", "Start tutorial". No results: search icon, "No matches found", "Try different keywords or check your spelling.", "Clear search". Error: warning icon, "Something broke", "We couldn't load your data. Try again in a moment.", "Retry". Filtered: funnel icon, "Hidden by filters", "You have 42 items but filters are hiding them all.", "Reset filters". Each uses its own status colour role and icon. Why: the cause differs, so the explanation and the recovery action differ; one generic screen gives wrong advice in three of four cases.
- **Rule 5, empty = onboarding:** "Tasks" window with only a sparkle icon and "No tasks yet", which then gains a ghost (skeleton-style) preview of a task card, a label "← This is how a task looks", and a dashed drop zone "Drag files here to start". Why: showing the shape of a future item teaches what the feature does before the user commits.

## Do
- Add one small icon or illustration that matches the context (inbox, search, warning, filter).
- Write a short human headline plus one sentence explaining why it is empty and what happens next.
- Provide exactly one primary action that is the real next step ("Create project", "Clear search", "Reset filters", "Start tutorial"); an optional secondary text link is fine ("or import from file").
- Design four variants: first run, no results, error, filtered-out, each with its own copy and action.
- In the filtered state, say how many items exist but are hidden.
- In first run, show a ghost preview of a real item and an inline way to start (e.g. a drop zone).

## Don't
- Don't show a bare "No data", a blank body, or a lone X.
- Don't use log / status-code copy ("ERROR 404", "Result set empty", "status: failed") for an empty list.
- Don't offer "Try refreshing" as the only action when the list is legitimately empty.
- Don't reuse one generic empty screen for every cause.

## Scene by scene
- 0:00 Side by side "Dead" (X, "No data", log line, dimmed) vs "Alive" (icon tile, "Nothing here yet", "+ New project"); alive card zooms to centre with a glow. Overlay "5 rules most apps miss".
- 0:03 "01 · Illustration > void": empty "My Projects" window with faint "No items", hint "Add a single icon →".
- 0:05 A cube icon pops in, then headline "Nothing here yet" and explanatory line.
- 0:09 "02 · Tone = brand voice": cards "Corporate" ("ERROR 404 / No items found. Result set empty. / status: failed") vs "Human" ("Looks quiet in here", "+ Add your first project"); the corporate card dims.
- 0:16 "03 · Primary CTA mandatory": "Inbox" window with refresh icon, "Nothing to show", "Try refreshing".
- 0:18 Replaced by plus icon, "Your inbox is clear", filled "+ Create project"; 0:20 secondary "or import from file" appears; cursor near the button.
- 0:22 "04 · Context = design": 2x2 grid builds card by card: First run, No results, Error, Filtered; each card is highlighted in turn (0:26-0:29).
- 0:30 "05 · Empty = onboarding": "Tasks" window, sparkle icon, "No tasks yet"; it morphs into a ghost task card, label "← This is how a task looks", then a dashed "Drag files here to start" drop zone.
- 0:36 Recap "5 empty state rules": 01 Illustration, 02 Human tone, 03 Primary CTA, 04 Context, 05 Onboarding; "Save" and "Follow" buttons.

## Voice-over summary
- The empty state is the first impression and is usually wasted.
- A blank screen gives no signal; one small illustration changes how it reads (the transcript literally says a blank screen "tells users nothing is wrong", likely a mishearing; the page says a blank screen reads as broken).
- Error-style copy sounds corporate; the empty state should sound like a product, "not a log file".
- Every empty state needs a primary action, not refresh: the step users would take if they knew what to do.
- There are four kinds of empty (first run, no results, error, filtered out), and each needs its own design; the empty state is the best onboarding moment to teach the feature.

## Notes for the skill
- Model the state explicitly: `status: 'first-run' | 'no-results' | 'filtered' | 'error' | 'ready'`; never infer "empty" from `items.length === 0` alone, because loading and error also yield zero items. Show a skeleton while loading, not the empty state.
- The "no refresh" rule has an exception the video itself shows: in the error variant, "Retry" is the correct primary action because the cause is transient. "Try refreshing" is wrong only when the list is legitimately empty.
- Error variant should be announced: use `role="alert"` (or a polite live region if it appears after a user action). Empty / no-results updates after search or filtering should be announced via `aria-live="polite"` (e.g. "No matches found"), WCAG 4.1.3 Status Messages.
- Decorative icons get `aria-hidden="true"`; the headline should be a real heading in the page outline.
- After "Clear search" / "Reset filters", move focus to the results region or the search input so keyboard users are not stranded on a removed button.
- Ghost preview items must be clearly non-interactive (reduced opacity, `aria-hidden="true"` or described as an example) so users do not try to click them; drop zones need a keyboard / click alternative (a file picker button), since drag-and-drop alone fails WCAG 2.5.7.
- Status colours per variant (danger for error, accent for first run, etc.) come from the theme roles; never rely on colour alone, the icon and text must carry the meaning.
- "ERROR 404" is an HTTP code for a missing resource, not an empty collection; an empty list returned successfully should never be phrased as an error.
