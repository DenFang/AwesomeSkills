---
id: unknown
reel_url: unknown
pattern_page: https://designmotionhq.com/patterns/bottom-sheets
date: unknown
duration_s: 52
type: ui
category: interaction
topic: bottom sheets for thumb-reachable mobile actions
sources: frames, voice-over, pattern page
---

# Bottom sheets: build for the thumb

**Caption:** not captured yet
**Hook:** Phones keep getting taller but thumbs do not, so menus anchored at the top of the screen are out of reach.

## Main rule
On mobile, surface contextual actions and secondary content in a bottom sheet anchored to the lower third of the screen instead of a top-anchored menu or a full-screen modal; give it snap points, drag-to-dismiss, a dimming scrim and a body scroll lock.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| bottom third of the screen | one-handed "comfort zone" where the thumb rests | 0:11-0:19 on-screen label "Bottom third = comfort zone" + voice |
| 2 snap points (peek, full) | sheet resting heights; dismiss is a third, closed state | 0:31-0:39 on-screen labels "PEEK" and "FULL" + voice |
| peek about the lower 30% of the screen, full about the lower 60-65% | sheet heights in the demo | 0:31-0:36, estimated from the mock-up (not stated) |

No ms, px or easing values are shown or said.

## Before / after
1. **Top-anchored menu vs bottom sheet (0:00-0:19).** Bad: an overflow menu (Account, Notifications, Settings, Log out; later Like, Share, Save) drops down from the top of the screen; the reach overlay shows the top band as a stretch/dead zone and only the lower part as reachable ("Reach stays the same"). Good: the same actions (Like, Share) appear in a sheet titled "Actions" that rises from the bottom edge. Why: thumb reach is fixed while screen height grows, so targets in the lower third can be hit one-handed without regripping; top corners require a stretch or a second hand.
2. **Full modal vs bottom sheet (0:20-0:30).** Bad: a full-screen "Details" modal with a close X replaces the "Places" list (labelled "PAGE GONE", "FULL MODAL"). Good: the same details (Address, Open until 9pm, 4.8 rating) appear in a bottom sheet while the list stays visible above, dimmed ("BOTTOM SHEET", "Context stays"). Why: the user keeps their spatial reference and can see where they came from, so returning costs no reorientation.
3. **Fixed height vs snap points (0:31-0:39).** The "Now Playing" sheet rests at PEEK (two rows visible), is pulled to FULL (third row "Liked songs" appears, more of the sheet is shown), then dragged down off screen. Why: height matches how much content the user wants; a downward swipe maps to the direction the sheet came from, so no small close target is needed.
4. **Scroll lock on vs off (0:40-0:48).** Good: "Comments" sheet over a dimmed "Feed", badge "PAGE LOCKED", only the sheet scrolls. Bad: badge "BOTH SCROLLING", the page behind (highlighted in the danger colour) scrolls together with the sheet ("Skip it, chaos"). Why: scroll chaining moves two surfaces under one finger, the user loses their place in both.

## Do
- Put frequent actions within thumb reach at the bottom of the screen.
- Use a sheet rather than a full-screen modal when the task is short and the page context matters.
- Keep the underlying page visible behind a scrim so the user knows where they are.
- Provide snap points (a peek height and a full height) so the user controls how much content is shown.
- Support drag-down to dismiss; show a grabber handle at the top of the sheet as the affordance.
- Dim the background and lock body scroll while the sheet is open.

## Don't
- Don't keep frequent menus in the top corners on tall phones.
- Don't block the whole screen with a modal when a sheet would do.
- Don't let the background scroll together with the sheet.

## Scene by scene
- 0:00 Phone mock-up with a top dropdown menu (Account, Notifications, Settings highlighted, Log out); a hand icon hovers mid-screen, unable to reach it. Caption: your thumb cannot reach.
- 0:03 Section "The problem": "Phones grew. Your thumb didn't." Feed screen; label "Menus still live up there".
- 0:06 Reach overlay: a dashed arc marks thumb reach, lower area highlighted with "Reach stays the same"; the top-left title and top-right button are outlined in the danger colour as out of reach.
- 0:11 Section "The fix": "Bring actions to the hand". Screen tinted in three bands (top = hard, middle = stretch, bottom = comfortable); label "Bottom third = comfort zone".
- 0:14 Top menu (Like, Share, Save) shown in the hard zone, then replaced at 0:17 by a bottom sheet "Actions" with Like and Share rows.
- 0:20 Section "Modal vs sheet": "A sheet keeps your place". Two phones: full modal "Details" (close X, "PAGE GONE", "FULL MODAL") vs "Places" list with a details sheet sliding up ("BOTTOM SHEET"). Label "Context stays".
- 0:31 Section "Snap points": "Peek, expand, dismiss". Library screen with "Now Playing" sheet at PEEK, side indicator dots mark the snap positions.
- 0:34 Sheet expands to FULL, adding "Liked songs".
- 0:37 Sheet dragged down and dismissed; label "Drag to dismiss".
- 0:40 Section "Scrim & scroll lock": "Dim, then lock scroll". Feed dims as a Comments sheet opens; badge "PAGE LOCKED", label "Lock the page".
- 0:46 Bad variant: badge "BOTH SCROLLING", page tinted in the danger colour, label "Skip it, chaos".
- 0:49 Outro "Bottom sheets: Build for the thumb." Player screen with a Now Playing sheet; CTA "Save this for your next app", "Follow for more mobile UX".

## Voice-over summary
- Screens got taller every year while thumb length stayed the same; the top corners are now a stretch, yet most menus still live there.
- The bottom third is where the thumb rests; a bottom sheet brings the actions down to the hand.
- A full modal covers the page and pulls the user out of context; a sheet slides up with the page still visible behind a dim layer.
- Sheets are not all-or-nothing: snap points allow a half-open peek or full height, and dragging down dismisses with no button.
- Dim the background to focus the sheet and lock page scroll, otherwise "both scroll at once. Chaos."

## Notes for the skill
- Implementation: native `<dialog>` with `showModal()` (gives inert background and Escape) or a `role="dialog"` + `aria-modal="true"` container with `aria-labelledby` pointing at the sheet title. Scrim as a fixed overlay; tapping it should dismiss (for non-destructive sheets).
- Scroll lock: `overflow: hidden` on the document scroller while open (watch iOS Safari, which may need `position: fixed` on body with saved scroll offset), plus `overscroll-behavior: contain` on the sheet's scroll container to stop scroll chaining.
- Snap points: CSS `scroll-snap` or a gesture library; respect velocity (a fast flick down dismisses even below the distance threshold). When the sheet is at full height and its content is scrolled, a downward drag should first scroll content to top before moving the sheet.
- Accessibility: drag-to-dismiss must not be the only way to close. Provide a visible close button or at least Escape and scrim tap, and make the grabber a focusable button that toggles snap points (WCAG 2.5.1 Pointer Gestures and 2.5.7 Dragging Movements require a single-pointer, non-drag alternative). The video says "No button needed", which is an oversimplification: keep a non-gesture close path for keyboard, switch and screen-reader users.
- Move focus into the sheet on open and return it to the trigger on close; trap focus while modal. A non-modal peek sheet (e.g. a persistent mini player) should not trap focus and should not lock scroll.
- Reduced motion: replace the slide-up with a short fade under `prefers-reduced-motion: reduce`.
- Keep sheet rows at least 44x44 pt (iOS) / 48x48 dp (Android) touch targets; respect the bottom safe-area inset (`env(safe-area-inset-bottom)`).
- The thumb-zone bands (bottom third comfortable) are a heuristic from one-handed-use research, not a hard rule; on tablets and desktop a sheet is usually the wrong component (use a popover or side panel).
