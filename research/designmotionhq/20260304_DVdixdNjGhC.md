---
id: DVdixdNjGhC
reel_url: https://www.instagram.com/reel/DVdixdNjGhC/
pattern_page: none
date: 2026-03-04
duration_s: 54
type: ui
category: visual
topic: glassmorphism card recipe in four CSS properties
sources: frames, voice-over, caption
---

# Glassmorphism card: four CSS properties

**Caption:** Glassmorphism in seconds.
**Hook:** A frosted-glass card takes just four lines of CSS.

## Main rule
Build a glass surface from exactly four layers, in order: a translucent light tint as background, a backdrop blur of the content behind it, a 1px semi-transparent light border that defines the edge, and a soft low-alpha drop shadow for lift. The effect only reads when there is varied, colourful content behind the card.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 4 | properties / lines of CSS (checklist "Pour in transparency, Mix in the blur, A pinch of border, Finish with shadow", steps "01 / 04" to "04 / 04") | 0:00-0:02 title "4 Lines of CSS." + voice; step counters 0:04-0:37 |
| `background: rgba(255,255,255, 0.35)` | glass base: light tint at alpha 0.35 (slider "opacity 0.35") | 0:07-0:11 on-screen code + slider; voice "low opacity" |
| `backdrop-filter: blur(20px)` | frosted blur of whatever is behind the card (slider animates 18px → 20px) | 0:15-0:20 on-screen code + slider |
| `border: 1px solid rgba(255,255,255, 0.5)` | edge highlight: 1px light border at alpha 0.5 | 0:24-0:28 on-screen code; voice says "one pixel, low opacity" |
| `box-shadow: 0 8px 32px rgba(0,0,0,0.15)` | lift: y-offset 8px, blur 32px, black at alpha 0.15 (slider 0.14 → 0.15) | 0:32-0:37 on-screen code + slider |
| `.glass-card { ... }` | full recipe in a file named `glass.css`, the same four declarations in the same order | 0:45-0:48 on-screen |

Note the mismatch: the voice calls the border "low opacity", but the code uses 0.5, which is higher than the 0.35 background. Trust the code value (0.5) as what the reel actually rendered.

## Before / after
- **Opaque card → translucent (step 1):** Before: a solid dark card hides the coloured blobs behind it. After: background set to a light tint at 0.35 alpha, the blobs show through. Why: partial transparency lets the backdrop participate in the surface, which is the base of the glass illusion; alone, though, sharp shapes behind make the card look like a dirty overlay.
- **Translucent → frosted (step 2):** `backdrop-filter: blur(20px)` softens the shapes behind into colour fields. Why: blur removes high-frequency detail behind the card, so foreground text competes less with the background and the surface reads as frosted glass rather than a tinted window.
- **No edge → defined edge (step 3):** a 1px light border at 0.5 alpha appears (highlighted in the reel). Why: on a blurred, low-contrast backdrop the card boundary dissolves; a bright hairline mimics light catching the glass edge and gives the shape a crisp silhouette.
- **Flat → lifted (step 4):** `0 8px 32px` shadow at 0.15 alpha. Why: a large, soft, downward-offset shadow separates the card from the page plane and adds depth without a hard outline.
- **Applied to other widgets (0:38-0:44):** weather card (24°), message notification, music player, profile card (1.2K / 8.4K / 342 stats), focus timer (25:00), all with the same recipe over the same blobs; the claim is that it works on any card.

## Do
- Apply the four properties together, in this order: translucent tint, backdrop blur, 1px light edge, soft shadow.
- Put varied, colourful or image content behind glass; on a flat single-colour background the effect is invisible.
- Keep text on glass at full opacity and check contrast against the worst-case area of the blurred backdrop.
- Use the same glass token set for every glass surface so the material is consistent.
- Provide a solid fallback background for browsers or user settings without backdrop filtering.

## Don't
- Don't use transparency without blur; sharp shapes behind translucent text hurt legibility.
- Don't skip the edge border; without it the card edge disappears into the blur.
- Don't use a hard, dark, short shadow; the reel's shadow is large (32px blur), offset down (8px) and faint (0.15).
- Don't stack many glass layers or animate large blurred areas; backdrop blur is expensive to render.

## Scene by scene
- 0:00 Title "4 Lines of CSS." over a tilting glass music-player card ("Midnight Dreams / Glass Orchestra") above blurred coloured blobs.
- 0:03 The card resets to a solid dark surface; 0:04 "01 / 04 · POUR IN TRANSPARENCY".
- 0:07 Slider "opacity 0.35"; the card turns translucent, blobs visible behind; code `background: rgba(255,255,255, 0.35);`; 0:08 checklist with the first item ticked.
- 0:12 "02 / 04 · MIX IN THE BLUR"; 0:15 slider "blur" 18px → 20px; code `backdrop-filter: blur(20px);`; 0:17 second item ticked.
- 0:21 "03 / 04 · A PINCH OF BORDER"; 0:24 the border flashes highlighted, code `border: 1px solid rgba(255,255,255, 0.5);`; 0:25 third item ticked.
- 0:29 "04 / 04 · FINISH WITH SHADOW"; 0:32 slider "shadow" 0.14 → 0.15; code `box-shadow: 0 8px 32px rgba(0,0,0,0.15);`; 0:34 all four ticked.
- 0:38 "SAVE FOR LATER": weather (24°), "New Message" notification, player, profile "Sarah Chen" (1.2K, 8.4K, 342), "Focus time 25:00" with a Start button, all in glass.
- 0:45 Code window `glass.css` with `.glass-card` and the four declarations.
- 0:49 "Save this recipe", glass "Follow" button and handle until 0:53.

## Voice-over summary
- The glass effect is four lines of CSS.
- First a semi-transparent background (low-opacity RGBA) makes the card see-through: the glass base.
- Then backdrop-filter blur frosts everything behind the card.
- A subtle 1px light border catches light on the edges and sells the illusion.
- A soft box shadow lifts the card and adds depth; four properties, same recipe on anything, save it.

## Notes for the skill
- Tokens, theme-driven: `--glass-bg` (a light tint around 0.35 alpha on dark themes; on light themes use a light tint at higher alpha, roughly 0.5-0.7, or a dark tint), `--glass-blur: 20px`, `--glass-border: 1px solid` light tint around 0.5 alpha, `--glass-shadow: 0 8px 32px` dark at 0.15. Take the tint from the theme's foreground / surface roles rather than hard-coding pure white and black.
- Browser support: `backdrop-filter` is supported in current Chromium, Firefox and Safari (older Safari needs `-webkit-backdrop-filter`). Wrap it: `@supports not (backdrop-filter: blur(1px)) { .glass-card { background: <opaque surface>; } }`.
- Accessibility: text contrast must be at least 4.5:1 (WCAG 1.4.3) against the lightest and darkest regions that can appear behind the card, not against the average. Glass over user images or video needs a stronger tint or a scrim. Honour `prefers-reduced-transparency: reduce` (and Windows "transparency effects off" / macOS "Reduce transparency") by switching to an opaque surface, and `prefers-contrast: more` by raising tint alpha and border strength.
- The 1px border at 0.5 alpha is decorative; if the card is an interactive control, its boundary or state indicator still needs 3:1 non-text contrast (WCAG 1.4.11), and focus needs a real focus ring, not the glass edge.
- Performance: `backdrop-filter` forces re-rendering of the area behind the element; avoid it on long scrolling lists, very large areas or many overlapping layers, and avoid animating the blur radius itself on low-end devices.
- `backdrop-filter` only blurs what is behind the element in the same stacking context; a parent with `overflow: hidden`, `opacity < 1`, `filter`, `transform` or `will-change` can change what gets blurred. Test the card in its real container.
- The reel's claim "works on anything" is overstated: on a plain or uniformly dark background the recipe produces a flat grey card, and over busy content it can reduce legibility.
