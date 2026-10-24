---
lesson: 015
kind: video
duration_s: 75
type: ui
category: visual / design system
topic: building a design system from tokens: colour harmony, type scale, 8px spacing, atomic composition
sources: frames, voice-over
---

# Build a design system from tokens

**Hook:** The gap between an amateur-looking app and a polished one is a system, and the video shows how to build one.

## Main rule
Define a small set of tokens first (a colour scheme derived from one harmony rule, four type sizes, spacing values that are multiples of 8px, a radius), apply them to every gap, padding and text, and compose components from those tokens: tokens → button (molecule) → card (organism). Never pick sizes or gaps ad hoc.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 3 colour schemes | monochromatic, complementary, analogous | 0:05-0:19 on-screen + voice |
| 1 hue, 4 lightness steps | monochromatic palette (4 swatches) driving Primary / Secondary / Ghost buttons | 0:05-0:09 on-screen |
| 2 opposite hues | complementary pair, "maximum contrast" | 0:10-0:14 on-screen |
| 3 neighbouring hues | analogous set, "harmonious & natural" | 0:15-0:19 on-screen |
| 14px (0.875×) | Caption size | 0:23-0:37 on-screen |
| 18px (base) | Body size | 0:24-0:37 on-screen |
| 32px (1.78×) | Heading size | 0:24-0:37 on-screen |
| 48px (2.67×) | Display size | 0:25-0:37 on-screen |
| 1 font family, 4 sizes | type system | 0:36 on-screen + voice |
| 8px | base spacing unit | 0:39 on-screen + voice |
| 8 / 16 / 24 / 32 / 48 px = xs / sm / md / lg / xl | spacing scale | 0:40-0:46 on-screen |
| 8, 16, 24, 40 "and beyond" | spacing steps as spoken (40 is not on screen) | 0:42 voice |
| 24px top, 16px between text and button, 24px bottom | card example "Applied to a card" | 0:43-0:46 on-screen |
| 18px / 22px / 10px | "RANDOM" column gaps (bad) | 0:47-0:53 on-screen |
| 16px / 16px / 16px | "8PX GRID" column gaps (good) | 0:47-0:53 on-screen |
| 4 atoms | Color, Type, Space, Radius | 0:55-0:58 on-screen + voice |
| weight 700, 16 × 28, r:12, token "primary" | button molecule spec chips (padding 16 × 28 px, radius 12) | 0:59-1:09 on-screen |
| 24px pad | organism (pricing card) padding chip, plus Heading / Body text / Button chips | 1:04-1:09 on-screen |

Ratio check: 32/18 = 1.78 and 48/18 = 2.67 match the labels, but 14/18 = 0.78, not 0.875 (0.875 = 14/16). The steps 18 → 32 → 48 are ×1.78 then ×1.5, so this is not a single fixed-ratio modular scale despite the label.

## Before / after
- **No system vs design system (0:00-0:02).** Left "NO SYSTEM": a card with three unrelated buttons ("click here" grey, "SUBMIT" uppercase saturated, "cancel" outlined), mismatched shapes and icon tiles. Right "DESIGN SYSTEM": the same layout with one consistent primary button ("Get Started"), a secondary outlined "Learn More", matching radius and a cohesive accent set. Why: consistent tokens make elements read as one family, so hierarchy comes from intent (primary vs secondary) instead of noise.
- **Random sizes vs a scale (0:21-0:37).** Four named sizes (Caption 14, Body 18, Heading 32, Display 48) applied to an article card ("The Future of Design" / "Why systems matter" / body / "Published Jan 2025 · 4 min read"). Why: large, consistent jumps between levels let the eye rank information instantly; near-identical random sizes blur hierarchy.
- **Random spacing vs 8px grid (0:47-0:53).** Same content (Title, Subtitle, Image, Body, Button). Left gaps 18 / 22 / 10 px; right gaps 16 / 16 / 16 px. Caption: "Consistent spacing = visual rhythm". Why: repeated identical intervals form a rhythm the eye can predict; irregular gaps imply relationships that do not exist and look accidental.
- **Ad hoc components vs atomic composition (0:54-1:09).** Atoms (Color, Type, Space, Radius) → molecule "Get Started" button annotated "primary · 700 · 16 × 28 · r:12" → organism "Pro Plan / Everything to scale your workflow. / Upgrade" card annotated "Heading · Body text · Button · 24px pad". Why: when bigger components are built only from tokens, a change to a token propagates everywhere and nothing drifts.

## Do
- Choose one colour harmony per product: monochromatic (one hue, several lightness/saturation steps), complementary (two opposite hues, use the opposite only for emphasis such as an alert action), or analogous (three neighbouring hues for related data like metric tiles).
- Derive button variants from one hue's lightness steps: primary (strongest), secondary (lighter), ghost (near background).
- Use one font family and four sizes with clear roles: caption, body (base), heading, display.
- Use a base spacing unit of 8px and only its multiples (8, 16, 24, 32, 48) for every gap and padding; name them (xs, sm, md, lg, xl).
- Keep equal gaps between sibling blocks in a card (e.g. 24px outer padding, 16px between content and action).
- Define atoms (colour, type, space, radius) as tokens and compose molecules and organisms from them.

## Don't
- Don't pick colours individually per screen; pick a scheme and stay in it.
- Don't invent font sizes per component.
- Don't use off-grid gaps like 10, 18 or 22 px.
- Don't style buttons differently on each screen (mixed casing, shapes and weights).

## Scene by scene
- 0:00 Split "NO SYSTEM" vs "DESIGN SYSTEM" app cards. Text: "The difference is a system. Here's how to build one." The systemised card then sits alone.
- 0:04 "01 Colors": a 12-dot colour wheel lights up.
- 0:05 "Monochromatic / One hue, vary lightness & saturation": one dot selected, 4 swatches, example Primary / Secondary / Ghost buttons.
- 0:10 "Complementary / Two opposites, maximum contrast": two opposite dots joined by a line, 2 swatches, example "Alert Banner / Action required" with a contrasting "Fix now" button.
- 0:15 "Analogous / 3 neighbors, harmonious & natural": three adjacent dots, 3 swatches, example metric tiles "$12k Revenue", "+28% Growth", "$4.2k Profit".
- 0:21 "02 Typography / Modular Scale / Each step is a fixed ratio, not random sizes": rows build up Caption 14px 0.875×, Body 18px base, Heading 32px 1.78×, Display 48px 2.67×. 0:27 "Mathematical ratios → always harmonious".
- 0:30 "Hierarchy in Action / Your eye follows the scale naturally": article card builds level by level with size labels (Display 48px, Heading 32px, Body 18px, Caption 14px). 0:36 "One font family. 4 sizes. Instant hierarchy."
- 0:39 "03 Spacing / One unit: 8px / Stack it to create every spacing value": stacked-block bars 8, 16, 24, 32, 48 px (xs-xl). 0:43 "Applied to a card": Card Title, description, Action button with 24px / 16px / 24px markers.
- 0:47 "Spot the Difference / Same content, different spacing": "RANDOM" (18 / 22 / 10 px, danger colour) vs "8PX GRID" (16 / 16 / 16 px, success colour). 0:52 "Consistent spacing = visual rhythm".
- 0:54 "04 Atomic Components / Atoms → Molecules → Organisms / Small pieces compose into bigger ones": atoms Color, Type, Space, Radius appear; arrow to molecule "Get Started" with spec chips; 1:03 arrow to organism "Pro Plan" card with Upgrade button and chips. 1:08 "Small tokens. Big systems."
- 1:10 Final screen: a "Welcome back" sign-in card (Email, Password, full-width "Sign In", "Don't have an account? Sign up") built from the same tokens. 1:12 "Every pixel. Intentional."
- 1:14 Outro "Design systems > random styling" with a Follow button.

## Voice-over summary
- A system is what separates polished UI from random styling.
- Colour: pick one hue and vary lightness (monochromatic), two opposites for contrast (complementary), or three neighbours for harmony (analogous); three techniques give endless palettes.
- Type: no random sizes; a modular scale where each step is a fixed ratio; display, heading, body, caption from one family gives instant hierarchy.
- Spacing runs on one 8px unit stacked into larger steps and applied to every gap and padding; random spacing feels off, an 8px grid feels intentional.
- Colour, type, spacing and radius are atoms; atoms build a button (molecule), molecules build a card (organism).

## Notes for the skill
- Implement as CSS custom properties: `--space-1: 8px; --space-2: 16px; --space-3: 24px; --space-4: 32px; --space-6: 48px;` plus `--text-caption`, `--text-body`, `--text-heading`, `--text-display`, `--radius-*`, colour role tokens (`--color-primary`, `--color-primary-weak`, `--color-surface`...). Prefer rem for font sizes so user zoom and browser font settings work (18px = 1.125rem).
- The on-screen scale is not a true modular scale: 14 / 18 / 32 / 48 has step ratios 0.78, 1.78, 1.5, and the 0.875× label for 14px is wrong relative to an 18px base. For a genuine modular scale pick one ratio (e.g. 1.25 or 1.333) and round; or keep a hand-tuned set of four sizes, which is also fine, but do not claim a fixed ratio.
- Voice says the spacing scale goes 8, 16, 24, 40; the screen shows 8, 16, 24, 32, 48. Both are multiples of 8; trust the on-screen set. A 4px half-step is commonly needed for icon gaps and tight inline spacing.
- Colour harmony is not a contrast guarantee. Whatever scheme is chosen, text and controls still need WCAG contrast: 4.5:1 for body text, 3:1 for large text and UI component boundaries. Light-lightness tints for "secondary" buttons often fail with light text; check each pair. Complementary pairs used as alert vs action should not rely on hue alone (add icon or text).
- A ghost button that is nearly the surface colour needs a visible boundary (3:1 non-text contrast) or it loses its affordance.
- Molecule spec "16 × 28" reads as vertical × horizontal padding; with 18px body text that yields a button about 50px tall, comfortably above the 44 × 44 px touch-target guideline.
- Atomic design (atoms / molecules / organisms) is Brad Frost's terminology; templates and pages are the next levels and are not covered.
