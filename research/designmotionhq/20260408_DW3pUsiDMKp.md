---
id: DW3pUsiDMKp
reel_url: https://www.instagram.com/p/DW3pUsiDMKp/
pattern_page: none
kind: carousel
date: 2026-04-08
type: ui
category: css
topic: CSS one-liners replacing JS (smooth scroll, dark mode, truncation, sticky, scroll snap, accent color)
sources: caption, video slide (slide 1 of 8, cover)
---

# Six CSS one-liners that replace JavaScript

**Caption:** Argues against writing JavaScript for behaviour CSS provides natively and lists six one-liners: smooth scroll, dark mode, text truncation, sticky headers, scroll snap, system accent colours.
**Hook:** The cover crosses out JavaScript and replaces it with CSS, promising 6 one-liners.

## Main rule
Use the native CSS property for smooth scrolling, light/dark theming, truncation, sticky positioning, scroll snapping and form-control accent colouring before writing JavaScript for it, and wrap each in the accessibility guard it needs (reduced motion, readable full text, contrast).

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 6 one-liners | list length | caption; cover subtitle on the video slide |
| 8 slides | carousel length (likely cover + 6 + closing; assumed) | post metadata |
No other numbers. The code on the image slides was not available; the properties below are the standard CSS for each named item, not syntax seen in the post.

## Before / after
Bad = typical JS approach; Good = the native CSS each caption item almost certainly refers to (assumed, not verified on slides).
- **Smooth scroll.** JS scroll animation on anchor clicks → `scroll-behavior: smooth` on the scrolling element (usually `html`).
- **Dark mode.** JS reading the OS theme and toggling classes → `color-scheme: light dark` plus `prefers-color-scheme` media queries or the `light-dark()` function for tokens.
- **Text truncation.** JS measuring and cutting strings → single line `overflow: hidden; white-space: nowrap; text-overflow: ellipsis`, or multi-line `line-clamp` (`-webkit-line-clamp` with `display: -webkit-box`).
- **Sticky headers.** Scroll listeners toggling fixed positioning → `position: sticky; top: 0`.
- **Scroll snap.** Carousel libraries for snapping → `scroll-snap-type: x mandatory` on the container, `scroll-snap-align: start` on items.
- **System accent colours.** Custom-built checkboxes and radios to match the brand → `accent-color` on native form controls (the post's wording may instead mean the `AccentColor` system colour keyword; unclear without the slide).
Why it works: native features are declarative, run off the main thread or in the browser's scroll machinery, and keep built-in semantics and keyboard behaviour.

## Do
- Gate smooth scrolling: `@media (prefers-reduced-motion: no-preference) { html { scroll-behavior: smooth; } }`.
- Declare `color-scheme` so native controls, scrollbars and form fields follow the theme; build theme colours as tokens.
- Offer the full text of truncated content (tooltip on hover and focus, expand control, or detail view).
- Use `scroll-padding-top` equal to the sticky header height so anchor targets are not hidden under it.
- Keep native inputs and style them with `accent-color` instead of rebuilding them.

## Don't
- Don't force smooth scrolling for users who asked for reduced motion.
- Don't treat `color-scheme` alone as a full dark theme; it only switches browser defaults.
- Don't truncate critical information (prices, error messages, names needed to decide) with no way to read it.
- Don't use `mandatory` snapping on content taller than the viewport; items can become unreachable, prefer `proximity`.
- Don't place a sticky element inside an ancestor with `overflow: hidden`; sticky then stops working.

## Slide by slide
The carousel has 8 slides. Only slide 1 (the animated cover) was available; slides 2 to 8 were not downloaded, so this list is reconstructed from the caption.
- Slide 1 (seen, animated): cover crossing out JavaScript and pointing to CSS, subtitle 6 CSS one-liners you need to know with a swipe arrow.
- Slides 2 to 7 (not seen): presumably one one-liner each, in caption order (smooth scroll, dark mode, truncation, sticky headers, scroll snap, accent colours).
- Slide 8 (not seen): likely a closing/save slide.

## Video slide
Slide 1 (cover), about 3.5 s, centred text on a dark background with a soft radial glow.
- 0:00 First line fades in (stop writing), the second line is still faint.
- 0:00.5 Second line visible: JavaScript (in an accent colour) for this.
- 0:01 A strike-through line in the danger colour crosses out JavaScript.
- 0:01.5 A small down arrow and the word CSS fade in below, in the success colour; the glow appears.
- 0:02-0:03 CSS brightens to full; a muted subtitle (6 one-liners, with an arrow) fades in and holds.

## Notes for the skill
- Check current support for `light-dark()`, unprefixed `line-clamp`, and `accent-color` before relying on them; the older ones (sticky, scroll snap, smooth scroll, ellipsis) are long established but still test on target browsers.
- Smooth scroll: WCAG 2.3.3 (AAA) and general vestibular guidance call for honouring `prefers-reduced-motion`; scripted `scrollIntoView({behavior: 'smooth'})` should follow the same preference.
- Truncation: WCAG 1.4.10 (reflow) and 1.4.4 (resize text) mean truncation must not hide content that users need when text is enlarged; screen readers read the full DOM text, so sighted keyboard users are the group most likely to lose it. A `title` attribute alone is not keyboard or touch accessible.
- Dark mode: a theme toggle that overrides the OS preference still needs a little JS or a stored preference; CSS covers the default. Keep text contrast 4.5:1 in both schemes.
- `accent-color`: browsers adjust the check mark colour for contrast automatically, but the control's boundary still needs 3:1 non-text contrast against the background (WCAG 1.4.11).
- Sticky headers: cap their height on small screens (they consume viewport and can hide focused elements: WCAG 2.4.11 focus not obscured); `scroll-padding-top` helps.
- Scroll snap carousels still need visible controls or clear affordances and keyboard access to every item; snapping alone is not a carousel UI (see APG carousel pattern).
