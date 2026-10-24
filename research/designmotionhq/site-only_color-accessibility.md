---
id: unknown
reel_url: unknown
pattern_page: https://designmotionhq.com/patterns/color-accessibility
date: unknown
duration_s: 58
type: ui
category: visual
topic: text contrast ratios and colour-blind-safe state signalling
sources: frames, voice-over, pattern page
---

# Colour accessibility: contrast ratio and never colour alone

**Caption:** none (this video is published on the pattern page only; no matching reel on the Instagram profile as of 2026-10-24)
**Hook:** The same light text colour is crisp on one card and nearly invisible on another, because legibility is decided by the contrast ratio against the background, not by the text colour itself.

## Main rule
Check every text/background pair against WCAG contrast thresholds (4.5:1 body text, 3:1 large text, 7:1 for critical text if you want AAA), and never let colour be the only carrier of meaning: every coloured state also gets an icon, label, arrow or pattern.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 15:1 | top row, labelled "Crystal clear" | 0:08-0:12 on-screen |
| 7:1 | AAA threshold, row labelled "AAA, recommended" | 0:08-0:14 on-screen + voice |
| 4.5:1 | AA minimum for body text; voice: below this readers struggle | 0:06-0:13 on-screen + voice |
| 3:1 (danger-coloured low-contrast digits, partly unreadable; label "Large text only") | AA large-text threshold; voice: below 3 text becomes invisible | 0:08-0:12 on-screen + voice; page states 3:1 for large text |
| 1.5:1 | bottom row, labelled "Invisible" | 0:08-0:12 on-screen |
| 1.8:1 FAIL | muted nav link "Home" in a sample dashboard | 0:14-0:17 on-screen |
| 2.1:1 FAIL | "Welcome back" heading/subtitle area | 0:15-0:17 on-screen |
| 1.5:1 FAIL | muted stat label "Revenue" | 0:16-0:17 on-screen |
| 1.5-2:1 | typical ratio of "decorative" muted greys (nav links, card labels, secondary headings) | pattern page only |
| 300 million | people with colour blindness (voice); on-screen counter animates up (111M, 265M seen; final value not legible in frames) | 0:17-0:20 voice + on-screen |
| ~8% | share of users with colour-vision deficiency | pattern page only |
| 1.5% / 6% / 0.01% | on-screen prevalence labels for protanopia / deuteranopia / tritanopia | 0:30-0:32 on-screen |
| 3.2:1 -> 4.0:1 -> 6.8:1 -> 7.1:1 | critical UI text being lightened until it passes AAA (badge turns from fail to check at 6.8 and 7.1) | 0:39-0:42 on-screen |
| 4 | number of fix rules (add icons, use patterns, 7:1 contrast, test and simulate) | 0:32-0:46 voice + on-screen |

The video pushes 7:1 for critical text; the pattern page only asks for 4.5:1 body and 3:1 large text. Both are WCAG levels (7:1 = AAA, 4.5:1 = AA).

## Before / after
1. **Same text colour, two backgrounds (0:00).** One light text colour on a dark card reads strongly; on a mid-light card it washes out. Mechanism: perceived legibility depends on the luminance difference between text and background, so a colour token is not "accessible" on its own; only a pair is.
2. **Contrast ladder (0:03-0:13).** Five rows of identical text with the background stepping lighter: 15:1, 7:1, 4.5:1, ~3:1, 1.5:1. A horizontal "fail zone" line is drawn under 4.5:1; the rows below get fail markers. Mechanism: shows the threshold as a hard line rather than a matter of taste.
3. **Typical app (0:14-0:17).** A dark dashboard whose muted nav link, subtitle and stat labels measure 1.8:1, 2.1:1 and 1.5:1. Mechanism: the "sleek" low-contrast secondary greys are where real products fail, not the main headings.
4. **Error vs success under colour blindness (0:18-0:32).** A form with an error-coloured invalid-email message and border next to a success-coloured Submit button. Simulated for protanopia, deuteranopia and tritanopia, the error text and the button collapse into the same muddy hue (tagged "SAME COLOR" on the deuteranopia card). Mechanism: red/green hue difference is exactly what red-green dichromats lose, so state that is encoded only by hue disappears.
5. **Error text: colour alone vs colour + icon (0:33-0:36).** "Invalid email" in error colour only (tag "Color alone") becomes the same text with a circled-x icon in front (tag "Color + Icon"). Mechanism: shape survives any colour-vision type and greyscale.
6. **Bar chart: flat fills vs patterns (0:37-0:39).** Revenue / Costs / Growth bars in three solid hues get diagonal stripes, dots and a grid texture ("Color Blind Safe"). Mechanism: texture is a second channel that distinguishes series without hue.
7. **Critical text contrast (0:40-0:42).** A "Critical UI Text" card's muted body text is lightened step by step from 3.2:1 to 7.1:1.
8. **Test & simulate (0:43-0:45).** A dashboard with "3 Errors / 12 Passed / 5 Pending" chips and a Deploy button, viewed through a deuteranopia simulator: errors, passed and the button all turn into similar olive tones. Badge "Test Before Ship".
9. **Final before/after dashboard (0:46-0:53).** A wipe line sweeps across: muted labels are lightened (no layout change), the Revenue stat gets an up arrow, Users a down arrow, the "3 issues found" banner gets a warning icon, the Continue button gets a check icon, each tagged "icon indicator". Ends with a "WCAG AA" pass badge. Mechanism: same palette and layout; only luminance of muted text and a redundant non-colour cue per state changed.

## Do
- Measure every text/background pair, including muted secondary text, nav links, card labels and placeholders, not only primary headings.
- Use 4.5:1 minimum for body text, 3:1 minimum for large text (and for UI component boundaries and meaningful icons), 7:1 for critical text where you can.
- Fix failing muted text by changing its lightness, keeping hue and layout.
- Pair every status colour with a second cue: icon on error/success messages, arrows on trend stats, labels or icons on chips.
- Give chart series patterns/textures or direct labels in addition to hue.
- Run a colour-blindness simulator (protanopia, deuteranopia, tritanopia) on key screens before release.

## Don't
- Don't separate error and success (or pass/fail, up/down) by red vs green hue alone.
- Don't ship low-contrast grey labels because they "look clean".
- Don't treat a colour token as accessible in isolation; contrast is always a pair.
- Don't rely on solid colour fills as the only distinction between chart series.

## Scene by scene
- 0:00 Two cards side by side, "HIGH CONTRAST" and "LOW CONTRAST", same heading text colour (the same hex chip appears under both); one is legible, one washed out.
- 0:02 Title "Rule 01 / Contrast Ratio"; five identical rows "Your users need to read this" stack in, each on a progressively lighter background.
- 0:06 Ratio readouts appear per row: 15:1, 7:1, 4.5:1, ~3:1, 1.5:1, with captions (crystal clear, AAA recommended, AA minimum for body text, large text only, invisible).
- 0:09 "AAA" and "AA" side badges, a "FAIL ZONE" line under 4.5:1; check marks on passing rows, x marks on failing ones.
- 0:14 Overlay "Most apps fail both." over a dark sample dashboard; callouts Home 1.8:1, Welcome back 2.1:1, Revenue 1.5:1, each tagged FAIL.
- 0:18 "Hidden problem / Color Blindness" with an animated counter (111M, 265M ...) above an email form: error-coloured field and message, success-coloured Submit.
- 0:20 "Same form. Same colors. Same problem." The form splits into three simulated copies labelled Protanopia (no reds), Deuteranopia (no greens), Tritanopia (no blues).
- 0:29 Deuteranopia copy highlighted with a "SAME COLOR" tag; prevalence labels 1.5%, 6%, 0.01%.
- 0:33 "Rule 01 / Add Icons": "Invalid email" text alone ("Color alone"), then with a circled-x icon ("Color + Icon").
- 0:37 "Rule 02 / Use Patterns": three coloured bars gain stripe, dot and grid textures; "Color Blind Safe" badge.
- 0:40 "Rule 03 / 7:1 Contrast": card "Critical UI Text"; ratio badge climbs 3.2 -> 4.0 -> 6.8 -> 7.1:1 as the text brightens.
- 0:43 "Rule 04 / Test & Simulate": browser mock with 3 Errors / 12 Passed / 5 Pending chips and Deploy Now button, then the same through a "Deuteranopia simulator"; badge "Test Before Ship".
- 0:46 "BEFORE" dashboard (Revenue $12,450, Users 2,847, danger-coloured "3 issues found" banner, success-coloured Continue button); a vertical wipe reveals "AFTER" with lightened labels, trend arrows, warning icon on the banner, check icon on Continue, "icon indicator" notes.
- 0:53 "WCAG AA" pass badge.
- 0:55 End card: save / follow call to action.

## Voice-over summary
- Contrast ratio is the brightness gap between text and its background; the same text colour can be readable or invisible depending on the background.
- Under 4.5:1 reading gets hard and under 3:1 text effectively disappears; WCAG AA needs 4.5:1, AAA 7:1, and the narrator claims most apps fail both.
- Roughly 300 million people are colour blind; a red error next to a green success button can look like one colour to them, and each type of colour blindness breaks the UI differently while users rarely report it.
- Four fixes: never use colour alone (add an icon or label), use patterns in charts, push critical text to at least 7:1, and test with a colour-blindness simulator before each release.
- The final fix keeps the same palette and layout; only contrast was raised and secondary indicators added.

## Notes for the skill
- Implement status with a token pair plus an icon slot: e.g. error message = icon (aria-hidden) + text; for form errors also set `aria-invalid="true"` and link the message with `aria-describedby` so the meaning is not visual at all.
- Trend stats: arrow icon plus a text sign ("+14%", "-3%"); screen readers should get the direction in text (visually hidden "up"/"down" or the signed number).
- Charts: use SVG patterns / textures or direct data labels per series; keep a legend with shapes, not only swatches.
- Test muted tokens (secondary text, placeholder, disabled-looking but active labels, nav links) in both themes; dark themes often fail on mid-grey labels.
- WCAG precision corrections:
  - 3:1 is the AA minimum for large text (about 24 px regular or about 18.7 px bold) and for non-text UI parts (SC 1.4.11: input borders, focus indicators, meaningful icons). AAA large text is 4.5:1, body AAA is 7:1. The voice line "below 3, invisible" is a rhetorical simplification, not a WCAG definition.
  - "Never colour alone" corresponds to WCAG SC 1.4.1 Use of Color.
  - On-screen prevalence numbers are loose: commonly cited figures are about 8% of men and 0.5% of women with some colour-vision deficiency. 6% roughly matches deuteranomaly (anomalous, milder) rather than true deuteranopia (about 1% of men); protanopia and deuteranopia both cause red-green confusion, so "protanopia kills reds, deuteranopia kills greens" is a simplification. Tritanopia is rare (on the order of 0.01%).
  - Contrast ratio is computed from relative luminance (WCAG formula), not a perceptual "brightness gap"; for large display text APCA can be a useful secondary check, but WCAG 2.x ratios remain the compliance bar.
- Uncertain: the 4th ladder value is drawn in low-contrast error-coloured digits; read as 3:1 from the "Large text only" caption and the voice/page, not legible directly. The colour-blindness counter's final value is not legible in frames (voice says 300 million).
