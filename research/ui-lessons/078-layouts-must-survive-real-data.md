---
lesson: 078
kind: video
duration_s: 51
type: ui
category: css / content resilience
topic: layouts that survive real data: min-width 0, middle truncation, tabular numbers, overflow-wrap
sources: frames, voice-over
---

# Layouts must survive real data

**Hook:** A member card looks fine until someone signs up with a 30-character real name and the action button is pushed out of the card.

## Main rule
Design and test components against real-length content. Four CSS fixes cover most breakage: `min-width: 0` on the flex child that must shrink, truncate in the middle for strings whose end carries meaning, `font-variant-numeric: tabular-nums` for numbers that update live, and `overflow-wrap: anywhere` for long unbroken strings. Test each with three fixtures: empty, 1 character, and 40 characters plus an emoji.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 30 characters | length of the real name that breaks the card ("Nothing else changed.") | 0:02 on-screen |
| short test data (about 10-12 characters; exact number unreadable) | length of typical fake test names | 0:04 faint on-screen line |
| `min-width: 0` | flex child holding the name | 0:12-0:16 on-screen code + voice |
| flex children default to `min-width: auto` | cause of the bug | 0:09-0:16 on-screen |
| `overflow: hidden; text-overflow: ellipsis;` | ellipsis rules that do nothing without `min-width: 0` | 0:04-0:16 on-screen code |
| keep `quarterly_rep` / drop `ort_fi` / keep `nal_v3.pdf` | middle-truncation split | 0:21-0:26 on-screen |
| 1,111 vs 8,888 "five characters, two widths" → "one width" | proportional vs tabular digits | 0:29-0:35 on-screen |
| `font-variant-numeric: tabular-nums` | live metrics | 0:32-0:35 on-screen code + voice |
| Active users / Requests/min / p95 latency (values change every second, e.g. 7,423 / 2,736 / 7,049) | live metric rows used as demo | 0:27-0:35 on-screen (illustrative) |
| 0 spaces in that URL, 0 break opportunities | why the URL overflows | 0:39-0:44 on-screen |
| `word-break: break-all` (rejected) vs `overflow-wrap: anywhere` (chosen) | long URL in a chat message | 0:40-0:47 on-screen code + voice |
| 4 fixes | min-width 0, truncate the middle, tabular-nums, overflow-wrap anywhere | 0:48 on-screen |
| 3 fixtures: empty, 1 character, 40 characters + an emoji | minimum test data for every text slot | 0:49 on-screen |

## Before / after
- **Ellipsis that never fires (0:04-0:16).** Bad: the name element has `overflow: hidden` and `text-overflow: ellipsis`, yet the long name stays full width and the "Manage" button is pushed outside the card (hatched overflow area). A bar diagram shows "available" width shorter than "content, refuses to shrink". Good: add `min-width: 0` to the name's flex item; the name truncates to "Bartholomew Vanderm…", the badge and "Manage" stay inside ("fits"). Why: a flex item's automatic minimum size is its min-content width, so it cannot shrink below its longest unbreakable text and overflow never happens inside it; `min-width: 0` lets it shrink so the ellipsis can trigger.
- **Cut the middle, not the end (0:17-0:26).** Bad: end truncation "quarterly_report_fina…", "design_system_tokens_…", "screenshot_2026_07_30…", "bartholomew.vandermee…" hides the extensions (.pdf, .json, .png) and the email domain. Good: middle truncation "quarterly_rep…nal_v3.pdf", "design_system…xport.json", "screenshot_20…14_22.png", "bartholomew.v…@northwind.io". Why: for filenames the extension and version suffix identify the file, for emails the domain identifies the organisation; keeping both ends preserves the distinguishing information.
- **Numbers that twitch (0:27-0:35).** Bad: proportional digits; "1,111" is visibly narrower than "8,888", so each live update shifts the unit labels and the row jitters. Good: `tabular-nums` gives every digit the same advance width; the text cursor after both numbers lines up. Why: constant-width digits keep columns aligned and remove motion that the eye reads as change.
- **One word, no break (0:36-0:47).** Bad: a chat message with a long URL (no spaces) stretches past the bubble. `word-break: break-all` is shown and rejected because it also chops normal words in half. Good: `overflow-wrap: anywhere` wraps the URL inside the bubble and only breaks where no other option exists. Why: browsers only wrap at break opportunities (spaces, hyphens); a URL has none, so the container grows instead.

## Do
- Put `min-width: 0` (or `overflow: hidden`, which also resets the automatic minimum) on any flex or grid child that must shrink and truncate.
- Truncate filenames, emails and paths in the middle so the extension, version and domain stay visible; keep the full value in a tooltip or `title`, and in the accessible name.
- Use `font-variant-numeric: tabular-nums` for counters, prices in tables, timers and any live-updating number.
- Use `overflow-wrap: anywhere` on user-generated text containers (messages, comments, cards) so URLs, tokens and IDs wrap.
- Test every text slot with empty, 1-character and 40-characters-plus-emoji fixtures before a demo.

## Don't
- Don't rely on `text-overflow: ellipsis` alone inside a flex row.
- Don't end-truncate strings whose suffix carries meaning.
- Don't use `word-break: break-all` for general text; it breaks ordinary words mid-word.
- Don't design only with short placeholder names.

## Scene by scene
- 0:00 "Team members" list: five rows (avatar initial, name, email, plan badge Pro/Team/Free, "Manage" button) with a dashed "container" guide on the right.
- 0:02 One row becomes "Bartholomew Vandermeer-Okonkwo"; the row widens past the container, "Manage" sits in a hatched overflow zone. Label "30 characters. Nothing else changed." 0:03 "Real content breaks layouts."
- 0:04 Section "01 the ellipsis that never fires": the broken row alone, code `.name { overflow: hidden; text-overflow: ellipsis; }` with a dim `min-width: 0`; ellipsis line gets struck through. Bars "available" vs "content, refuses to shrink". Notes "Manage, pushed outside the card", "flex children default to min-width: auto".
- 0:12 `min-width: 0` is added and highlighted; the name truncates with an ellipsis, guide reads "fits", note "Manage, inside the card". 0:13 "min-width: 0, or no ellipsis."
- 0:17 Section "02 cut the middle, not the end": four end-truncated strings; 0:20 their hidden endings (.pdf, .json, .png) appear outside in the danger colour; 0:21 a keep / drop / keep diagram; 0:23 strings switch to middle truncation with endings highlighted. 0:24 "Both ends carry meaning."
- 0:27 Section "03 numbers that twitch": three live metric rows updating each second; a box with "1,111" and "8,888" and cursors at different x positions, "five characters, two widths". 0:32 code `.metric { font-variant-numeric: tabular-nums; }`, cursors align, "five characters, one width". 0:33 "Digits should never move."
- 0:36 Section "04 one word, no break": chat message from Priya Raman "Can you check the July invoice before Friday?" plus a long URL that overflows the bubble into a hatched zone. 0:39 "0 spaces in that URL, 0 break opportunities". Code shows `word-break: break-all` then strikes it; caption "break-all chops normal words in half too. anywhere only breaks when there is no other option."
- 0:45 `overflow-wrap: anywhere` applied; URL wraps inside the bubble, "breaks anywhere it has to", "fits". 0:46 "Long strings need permission."
- 0:48 "THE FOUR FIXES" checklist with use cases: min-width: 0 (flex children that must shrink), truncate the middle (filenames, emails, paths), tabular-nums (anything that updates live), overflow-wrap: anywhere (URLs, tokens, IDs). 0:49 "Ship none of it untested. Three fixtures: empty / 1 character / 40 characters + an emoji". Outro "Follow for more UI systems. Save this before your next demo."
- A progress rail at the bottom (min-width, truncate, tabular, wrap) ticks off each section.

## Voice-over summary
- The card works until a real, long name appears; the ellipsis never fires.
- A flex child will not shrink below its text, so the name pushes the button off the card; set `min-width: 0` on the child that should shrink.
- Cutting the end throws away the answer: a filename is its extension, an email is its domain; truncate the middle.
- Proportional digits have different widths so live numbers nudge the layout; tabular numbers lock them to one width.
- Browsers never break inside a word, so one long URL stretches the card; `overflow-wrap: anywhere` permits the break.

## Notes for the skill
- CSS has no native middle truncation. Options: split the string into a shrinking head span (`overflow: hidden; text-overflow: ellipsis; white-space: nowrap; min-width: 0`) and a non-shrinking tail span (`flex-shrink: 0`) containing the last N characters or the extension; or compute in JS with a measured width. Keep the full string available: `title` for mouse users and the full text as the accessible name (screen readers must not hear the ellipsis-truncated value only).
- `min-width: 0` applies to flex items; in CSS grid the equivalent is `minmax(0, 1fr)` for the track. A parent that also refuses to shrink needs the same fix up the chain.
- `overflow-wrap: anywhere` also affects min-content size (it lets the container shrink), unlike `overflow-wrap: break-word`, which only breaks on actual overflow. Use `anywhere` in flex/grid children; `break-word` where intrinsic sizing should stay unchanged. `hyphens: auto` with a `lang` attribute is the better choice for long natural-language words.
- `tabular-nums` only works if the font has tabular figures (most UI fonts do; check display fonts). For right-aligned numeric columns also align on the decimal point by using fixed decimals.
- Live-updating metrics that change every second should not be announced on every tick; if a live region is needed use `aria-live="polite"` with throttling.
- Fixtures worth adding beyond the three shown: right-to-left text, CJK text (no spaces, so it breaks differently), and very long single words in a narrow mobile viewport (320px wide).
