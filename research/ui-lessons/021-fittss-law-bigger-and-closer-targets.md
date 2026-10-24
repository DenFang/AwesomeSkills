---
lesson: 021
kind: video
duration_s: 42
type: ui
category: interaction
topic: Fitts's law (target size, distance, thumb reach)
sources: frames, voice-over
---

# Fitts's law: bigger and closer targets

**Hook:** The time to hit a target depends on only two things: how far it is and how big it is.

## Main rule
Make important targets large and place them where the pointer or thumb already is: primary mobile
actions in the bottom thumb zone, touch targets at least 44pt (the video's "good" set is 48px+), and
actions that appear at the cursor or in place (context menu, FAB, inline edit) to cut distance to zero.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| T = a + b x log2(D / W + 1) | Fitts's law (Shannon form); D distance, W target width | 0:03-0:11 on-screen |
| 9.6 s, 9.0 s, 5.9 s, 4.5 s | illustrative "time to click" as the target grows (W up) | 0:00-0:07 on-screen |
| 4.2 s, 3.5 s, 3.0 s | illustrative "time to click" as the target moves closer (D down) | 0:08-0:11 on-screen |
| 12% vs 34% tap rate | primary "Buy Now" at top vs at bottom of a phone screen | 0:17-0:26 on-screen + voice (illustrative, unsourced) |
| 32px targets | icon row labelled "too small for fingers" | 0:20-0:26 on-screen |
| 48px+ targets | icon row labelled "comfortable tap targets" | 0:20-0:26 on-screen |
| 44pt minimum | Apple guideline cited for touch targets | 0:22-0:26 on-screen |
| D = 0 | right-click menu opens at the cursor | 0:27-0:38 on-screen |

## Before / after
- **Small far target vs big near target (0:00-0:11).** A cursor travels distance D to a narrow
  handle; "time to click" reads 9.6 s. The target widens into a "Click" button (9.0 to 4.5 s, "Bigger
  target = faster clicks"), then slides toward the cursor (4.2 to 3.0 s, "Closer target = faster
  clicks"). Why: movement time grows with the log of distance divided by width, so both enlarging W and
  shrinking D reduce it; the seconds are illustrative only.
- **Primary action at the top vs bottom (0:13-0:26).** Bad phone: "Buy Now" at the top, a line shows
  the long thumb stretch from the bottom; 12% tap rate. Good phone: full-width "Buy Now" docked at the
  bottom where the thumb rests; 34%. Why: on one-handed phone use the bottom of the screen is the
  natural thumb zone, so the travel distance to the action is shortest there.
- **32px vs 48px+ icon targets (0:20-0:26).** A row of 32px icon buttons is labelled too small for
  fingers; a row of 48px+ buttons is comfortable. Why: a fingertip contact area is much larger than a
  mouse pointer, so small targets cause misses and slower, more careful taps.
- **Distance reduced to zero (0:27-0:39).** Three cards: right-click menu ("menu appears at cursor,
  D = 0"), floating action button ("fixed position, always within reach"), inline editing ("edit in
  place, no modal needed"). Why: if the control appears where the pointer already is, the move cost
  disappears.

## Do
- Put the primary mobile action in the bottom area, full width or within thumb reach.
- Size touch targets to at least 44x44pt (iOS) / 48x48dp (Android); 48px+ is the video's "good" value.
- Offer contextual actions at the point of attention: context menus at the cursor, inline edit
  fields in place of a separate modal, a persistent FAB for the one main creation action.
- Increase the hit area (padding, invisible hit box) even when the visual icon stays small.

## Don't
- Don't place the key mobile CTA at the top of the screen, far from the thumb.
- Don't ship 32px icon-only touch targets.
- Don't send users to a distant modal for a small edit that could happen in place.

## Scene by scene
- 0:00 "FITTS'S LAW, the rule behind every great button": a line from cursor to a narrow target, labels D and W, "time to click 9.6s".
- 0:03 Formula T = a + b x log2(D / W + 1) appears.
- 0:05 "Bigger target = faster clicks": target grows into a "Click" button, time drops 9.0, 5.9, 4.5 s.
- 0:08 "Closer target = faster clicks": button slides toward the cursor, time 4.2, 3.5, 3.0 s.
- 0:10 Two summary cards: "Make targets BIGGER", "Put them CLOSER".
- 0:12 "Secret 01, size in action": bad phone with "Buy Now" at top vs good phone with "Buy Now" at bottom.
- 0:16 Thumb icons tap each; a line shows the long reach on the bad phone.
- 0:17 Tap-rate labels "12%" (bad) and "34%" (good).
- 0:20 "Touch target sizes": 32px icon row (too small for fingers) vs 48px+ row (comfortable).
- 0:22 "Apple's guideline: 44pt minimum".
- 0:26 "Secret 02, the distance trick, reduce distance to zero": right-click menu card (D = 0).
- 0:30 Floating action button card ("always within reach").
- 0:33 Inline editing card ("No modal needed"), field "Project name: My Project" gets focus.
- 0:36 Banner "The best target is already under your cursor".
- 0:39 Outro "Design smarter, not harder", follow button.

## Voice-over summary
- Fitts's law: time to reach a target depends on distance and size.
- Make buttons bigger and put them closer to where users already are.
- Mobile nav example: primary action at the top while the thumb sits at the bottom; moving it into
  thumb reach raises tap rate from 12% to 34% (claim).
- Context menus, floating action buttons and inline edit all cut distance to zero.
- Closing line, paraphrased: the best target is the one already under the cursor.

## Notes for the skill
- WCAG 2.2 SC 2.5.8 (AA) requires 24x24 CSS px minimum (or spacing); SC 2.5.5 (AAA) asks 44x44.
  Apple HIG: 44x44pt; Material: 48x48dp. Use 44 to 48 as the default and expand hit areas with padding
  or `::before` overlays rather than enlarging icons.
- The "time to click" values in seconds and the 12% to 34% tap-rate jump are illustrative, not
  measured data; real pointing times are a few hundred milliseconds. Do not quote them as benchmarks.
- Screen edges and corners are effectively infinite-size targets for a mouse (the pointer stops at
  the edge), a related Fitts corollary the video does not mention.
- FAB caveat: it can cover content and end-of-list actions; add bottom padding equal to the FAB area
  and keep only one FAB per screen. Bottom-docked CTAs must respect `env(safe-area-inset-bottom)`.
- Context menus are hidden affordances (not discoverable, no right-click on touch); always provide a
  visible alternative (overflow button with `aria-haspopup="menu"`, long press on touch).
- Inline edit: keep a visible edit affordance, commit on Enter/blur, cancel on Escape, and announce
  validation errors; follow keyboard focus rules.
