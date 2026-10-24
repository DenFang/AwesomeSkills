---
id: DeyuDIphgj3
reel_url: https://www.instagram.com/reel/DeyuDIphgj3/
pattern_page: none
date: 2026-10-22
duration_s: 20
type: ui
category: navigation
topic: mobile adaptation rules (tables to cards, no input zoom, thumb-size buttons, safe-area bottom bar)
sources: frames, caption
---

# Desktop UI made mobile: cards, no input zoom, thumb targets, safe area

**Caption:** AI coding tools build for desktop; version 2.3 of the author's Claude Code plugin adds mobile rules: tables become cards or keep only key columns, typing no longer zooms the page on iOS, buttons grow for thumbs, and the bottom bar clears the home indicator.
**Hook:** "Claude Code builds for desktop." A desktop table squeezed into a phone, then rebuilt for mobile.

## Main rule
When a desktop screen goes to a phone: turn table rows into cards (or keep only the key columns), prevent iOS from zooming when an input is focused, make action buttons large enough for a thumb, and keep any fixed bottom action bar above the home indicator (safe-area inset).

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 4 table columns → card fields | Request, Status, Due, Cost mapped onto a card: title "Bridge piling", status pill "Pending", Due "5 Oct · overdue", Cost "+€18,000" | 0:04-0:07 on-screen |
| "12 pending" | requests count in the section header | 0:01-0:09 on-screen |
| "2 selected" · "Approve 2" | bulk-action bottom bar after selecting two cards; the button label carries the count | 0:13-0:15 on-screen |
| UX Engine 2.3 · From $79 | product version and price (promo) | 0:02-0:03, 0:18-0:19 on-screen |
No pixel values are shown on screen; the reel names the rules without sizes.

## Before / after
- **Desktop table vs cards.** Bad (0:00): a wide "Portfolio" dashboard whose request rows (CR-0142 Bridge piling, Pending, 5 Oct · overdue, €18,000) run off the right edge of the phone. Good: each row becomes a card with an id line ("CR-0142 · HEL"), title, status pill top-right, label/value pairs for Due and Cost, and full-width Reject / Approve buttons. Why: a phone cannot show four columns at readable size; stacking label/value pairs keeps every field without horizontal scrolling.
- **Input zoom vs no zoom.** Good: tapping the search field and typing "CR-0142" keeps the page at its scale, callout "No zoom when you type" with a lock icon. Why: iOS Safari auto-zooms into inputs whose font size is below 16 px, which shifts the layout and forces the user to pinch back.
- **Small buttons vs thumb targets.** Good: Reject and Approve are two equal, wide buttons per card; a tap ripple shows the hit area, callout "Buttons your thumb can hit". Why: wide, tall targets reduce mis-taps with the thumb.
- **Bottom bar under the home indicator vs above it.** Good: after selecting two cards, a sticky bar "2 selected · Approve 2" sits above a hatched safe-area zone at the bottom, callout "Nothing hidden under the home bar". Why: content behind the home indicator conflicts with the system swipe-up gesture and can be unreadable or untappable.

## Do
- Render data-table rows as cards on narrow screens, mapping each column to a labelled field; or keep only the key columns.
- Use at least 16 px font size on inputs, selects and textareas on mobile to avoid iOS focus zoom.
- Make primary row actions full-width or wide buttons at a thumb-friendly height (44 px or more).
- Pad fixed bottom bars with the safe-area inset so they clear the home indicator.
- Show selection count in the bulk action ("Approve 2").

## Don't
- Don't ship a desktop table that scrolls horizontally on a phone as the only view.
- Don't disable zoom via `user-scalable=no` / `maximum-scale=1` to stop focus zoom; fix the input font size instead.
- Don't place bottom actions flush with the screen edge on devices with a home indicator.

## Scene by scene
- 0:00 Title "Claude Code builds for desktop." over a blurred, oversized desktop "Portfolio" layout overflowing a phone (Forecast +€5.3M vs budget, Off track 2 of 6, Requests list).
- 0:01 The layout snaps into a phone: search field, four stat cards (Forecast +€5.3M, Off track 2 of 6, To review 1 overdue, At risk 2 of 6), "Requests · 12 pending" with cards Bridge piling and Roof insulation.
- 0:02 Title "This plugin makes it mobile." with badge "UX Engine 2.3 · Claude Code plugin".
- 0:04 Camera zooms into the first card; floating column headers Request, Status, Due, Cost connect by lines to the card's title, status pill, due date and cost. Callout "Tables turn into cards".
- 0:07 Camera moves to the top; search field highlighted, typing "CR-014" → "CR-0142" with the keyboard up and no page zoom; callout "No zoom when you type".
- 0:10 Reject / Approve buttons outlined with dashed hit areas, tap ripple on Approve; callout "Buttons your thumb can hit".
- 0:13 Second card selected (check badge); sticky bottom bar "2 selected · Approve 2" above a hatched safe-area band; callout "Nothing hidden under the home bar".
- 0:16 Exploded 3D stack of the screen's layers with all four callouts.
- 0:18 End card "UX Engine 2.3, The UX plugin for Claude Code.", "New: responsive skill", "From $79 · designmotionhq.com".

## Voice-over summary
- No voice-over (music only; transcript contains only filler).
- On-screen text carries the message: tables turn into cards, no zoom when you type, buttons your thumb can hit, nothing hidden under the home bar.

## Notes for the skill
- This is mainly a product promo; the four mobile rules are the reusable content and are stated in the caption and callouts, without numeric values.
- Card mapping: keep the primary identifier as the card title, status as a pill, and secondary columns as label/value rows; preserve the semantic relationship for screen readers (e.g. a `<dl>` per card, or keep a real table with responsive CSS that exposes `data-label` headers).
- iOS focus zoom: triggered when the computed font size of a focused input is under 16 px. Fix with `font-size: max(16px, 1rem)` on form controls. Disabling user scaling breaks WCAG 1.4.4 (resize text) and should not be used.
- Safe area: requires `<meta name="viewport" content="..., viewport-fit=cover">`, then `padding-bottom: calc(12px + env(safe-area-inset-bottom))` on fixed bottom bars.
- Touch targets: Apple HIG 44×44 pt, Material 48×48 dp; WCAG 2.2 2.5.8 minimum 24×24 CSS px. Keep at least 8 px between adjacent targets like Reject / Approve.
- Destructive vs primary: Reject and Approve have equal size; consider visual weight (Approve as primary) and confirmation or undo for Reject if it is irreversible.
