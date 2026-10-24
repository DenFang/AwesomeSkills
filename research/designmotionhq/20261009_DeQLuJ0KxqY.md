---
id: DeQLuJ0KxqY
reel_url: https://www.instagram.com/reel/DeQLuJ0KxqY/
pattern_page: none
date: 2026-10-09
duration_s: 86
type: ui
category: forms
topic: choosing selection controls (switch, checkbox, radio, dropdown, segmented, tri-state, row target)
sources: frames, voice-over, caption
---

# Switch, checkbox, radio, segmented: pick the control by when it acts

**Caption:** "Checkbox, switch, radio. Only one matches what it does." (plus a plug for the author's UX Engine plugin)
**Hook:** One setting can be drawn as a checkbox, a switch or a radio pair, and only one of them matches its behaviour.

## Main rule
Choose a selection control by one question, "does it act now or on Save?": a switch applies immediately and never sits behind a Save button; a checkbox is a pending choice committed by Save. For one-of-many, use visible radios up to five options, a dropdown above five, and a segmented control for two to four exclusive options that must stay in view (e.g. view switching). A parent checkbox needs a third, mixed state, and the label plus whole row (at least 44 px tall) must toggle the control.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| "acts now = switch" | single on/off setting that applies immediately | 0:01-0:03 on-screen chip |
| "waits for Save" / "acts now" / "2 options, 2 taps" | the same "Mute all notifications" row as checkbox / switch / On-Off radio pair | 0:02-0:03 on-screen |
| "saved · 0 ms", "no Save button · ever" | switch screen: change is saved instantly, no Save button | 0:05-0:13 on-screen |
| "unsaved" → "saved", "Save changes" | checkbox screen: pending badge until Save is pressed | 0:09-0:13 on-screen |
| "live or not?" | mixed form: switches and checkboxes above one Save button | 0:14-0:17 on-screen + voice |
| ≤ 5 radio · > 5 dropdown | threshold between radio group and dropdown | 0:18-0:29 on-screen + voice ("up to five") |
| options: 4 → 5 → 9 | digest frequency options; 4 and 5 shown as radios "all visible", 9 flagged "9 radios", "rows off screen" | 0:19-0:27 on-screen |
| 9 options | Off, Daily, Every 2 days, Twice a week, Weekly, Every 2 weeks, Monthly, Quarterly, Weekdays only | 0:24-0:29 on-screen |
| "> 5 → dropdown" | the 9 options collapsed into a select showing "Weekly" | 0:27-0:29 on-screen |
| 2 to 4 · always visible | segmented control range | 0:30-0:41 on-screen + voice |
| "1 of 3 in view · hidden options" vs "3 of 3 in view" | dropdown vs segmented for Daily / Weekly / Monthly | 0:30-0:41 on-screen |
| "7 segments" (Day, Week, Month, Quarter, Half, Year, All time) | overfilled segmented control, truncated labels, marked wrong | 0:38-0:40 on-screen |
| "1 tap away" | every segment one tap from any other | 0:41 on-screen + voice |
| parent checkbox · 3 states: checked (all on), empty (none on), mixed (some on) | tri-state parent | 0:43-0:56 on-screen + voice |
| `el.indeterminate = true` · JS only, no HTML attribute | how to set the mixed state on a native checkbox | 0:43-0:56 on-screen |
| "1 click · all on" | clicking the mixed parent checks all children | 0:52-0:53 on-screen + voice |
| "looks off, 2 are on" | common bug: parent shows empty while 2 of 3 children are checked | 0:54-0:56 on-screen + voice |
| 44 px | minimum row height / hit target for a labelled checkbox row | 0:57-1:08 on-screen + voice |
| 16 px | bare checkbox box size in the "box only" version | 1:03-1:08 on-screen + voice |
| hits 3/3, hits 4/4 vs "miss", "2 taps · 0 hits" | tap test: label-wrapped row vs box only | 1:01-1:08 on-screen |
| `<label><input type="checkbox"> Email digest</label>` vs `<input type="checkbox"> <span>Email digest</span>` | markup for row target vs box only | 0:57-1:08 on-screen |
| 5 controls | Switch, Checkbox, Radio, Segmented, Row target | 1:09-1:13 on-screen + voice |
| $79 one time · 30 day refund · 12 months of updates | plugin price in promo tail | 1:24-1:25 on-screen (promo) |

## Before / after
- **Wrong control for an instant setting.** Bad: a checkbox (implies "waits for Save") or an On/Off radio pair ("2 options, 2 taps") for a setting that applies immediately. Good: a switch. Why: a switch mirrors a physical toggle; users expect the effect at the moment of flipping, and it takes one tap.
- **Switch screen vs checkbox screen.** Switch screen: flipping shows "saved · 0 ms" and there is no Save button at all. Checkbox screen (Email digest, Weekly summary, Product updates, plus "Send digest at 08:00"): ticking shows an "unsaved" badge until "Save changes" is pressed, then "saved". Why: each control's affordance promises a commit model; matching it removes doubt about whether a change took effect.
- **Mixed form.** Bad: a "Preferences" card with switches and a checkbox above a single "Save changes" button: the switches get "?" markers, "live or not?". Why: users cannot tell which settings are already live and which are pending, so they either lose changes or press Save needlessly.
- **9 radios vs dropdown.** Bad: nine radio options push "Send digest at" and other settings off screen ("rows off screen"). Good: past five, a dropdown that shows the current value and opens the full list. Why: radios cost vertical space per option; beyond about five the list dominates the screen and hides neighbouring settings.
- **Dropdown vs segmented for a view switch.** Bad: a "Daily" dropdown, "1 of 3 in view", other options hidden. Good: a segmented control Daily / Weekly / Monthly, "3 of 3 in view"; tapping switches the chart (Messages 337 → 2,403 → 8,890) and every option stays one tap away. Bad again: seven segments with truncated labels. Why: two to four short, exclusive options fit side by side and stay discoverable; more than that truncates and loses the benefit.
- **Two-state vs three-state parent.** Bad (most apps): "Notify me about" parent shows empty while Mentions and Replies are on ("looks off, 2 are on"). Good: parent is checked when all children are on, empty when none, and shows a dash (mixed) when some are; clicking the dash turns all children on. Why: the parent summarises the group truthfully and offers a one-click "select all".
- **Box only vs label-wrapped row.** Bad: a bare 16 px checkbox with the text in a separate span; taps on the text miss ("miss", "2 taps · 0 hits"). Good: the input is wrapped in a `<label>`, so tapping the text toggles it and the whole row (at least 44 px tall) is the target ("hits 4/4"). Why: a larger hit area reduces miss rate (Fitts's law) and the label association also gives screen readers the accessible name.

## Do
- Use a switch only for settings that apply immediately; show instant confirmation ("saved").
- Use checkboxes for choices that are committed by an explicit Save/Submit; show an unsaved indicator until then.
- Keep instant and deferred settings in separate sections or screens; one commit model per form.
- Use a radio group for one-of-many with up to five options, all visible, none hidden behind a click.
- Switch to a dropdown/select when there are more than five options.
- Use a segmented control for two to four exclusive, short options that must stay visible (time ranges, view modes).
- Give parent checkboxes three states (checked, unchecked, mixed) and make clicking a mixed parent check all children.
- Wrap each checkbox/radio and its text in a `<label>` (or use `for`/`id`) and make the full row at least 44 px tall.

## Don't
- Don't put a Save button behind switches.
- Don't mix switches and checkboxes above one Save button.
- Don't model a binary instant setting as an On/Off radio pair.
- Don't show more than five radios in a row-based settings list; don't hide two to four key options in a dropdown.
- Don't build segmented controls with 5+ segments or truncated labels.
- Don't leave a parent checkbox empty when some children are checked.
- Don't rely on a bare 16 px box as the only tap target.

## Scene by scene
- 0:00 A phone settings screen "Notification settings" (Tidepool, Maren Okafor · Harbor team) with one row "Mute all notifications" as an On/Off radio pair.
- 0:01 Tag "SELECTION CONTROLS · 01", "Only one matches.": the same row as checkbox ("waits for Save", wrong), switch ("acts now", right), radio pair ("2 options, 2 taps", wrong); the switch row is highlighted. Chip "acts now = switch".
- 0:04 Tag "02", "Switch acts. Checkbox waits.": two phones side by side. Left: switches (Mute all notifications, Do not disturb 22:00 to 07:00, Desktop badges, Message sound) with "saved · 0 ms" and "no Save button · ever". Right: checkboxes (Email digest, Weekly summary, Product updates) and a time select 08:00 above "Save changes"; ticking shows "unsaved", pressing Save shows "saved". Chips "switch · acts now", "checkbox · on Save", "switch = now · checkbox = on Save".
- 0:14 A "MIXED FORM · Preferences" card: switch + checkbox + switch above "Save changes"; the switches get "?" markers, label "live or not?".
- 0:18 Tag "03", "Radios: up to five.": "Digest frequency" radio group grows from 4 to 5 options ("all visible"), then to 9 with a danger counter, "9 radios", "rows off screen"; then it collapses into a select "Weekly" that opens the 9-item list, chip "> 5 → dropdown". Footer "≤ 5 radio · > 5 dropdown".
- 0:30 Tag "04", "2 to 4 options? Segmented.": desktop "Activity" dashboard with a Daily / Weekly / Monthly segmented control and a bar chart; cards "BEFORE · DROPDOWN (1 of 3 in view, hidden options)" vs "AFTER · SEGMENTED (3 of 3 in view)". The cursor taps Weekly and Monthly, the chart and stats update. A 7-segment version appears with clipped labels, "7 segments" (wrong). Then "1 tap away" on Daily. Footer "2 to 4 · always visible".
- 0:43 Tag "05", "Three states, not two.": "Notify me about" parent with children Mentions, Replies, Reactions; a legend of checked (all on), empty (none on), mixed (some on) highlights as children are toggled; parent label reads checked / empty / indeterminate; clicking the dash turns all on, "1 click · all on". Note "el.indeterminate = true · JS only, no HTML attribute". "BEFORE · MOST APPS": parent empty with 2 children on, "looks off, 2 are on".
- 0:57 Tag "06", "The row is the target.": zoomed "Email digest / Unread threads, every morning" rows. "AFTER · LABEL WRAPS IT" (`<label>` markup): tapping the text toggles, "tap the text → toggles", dashed 44 px row outline, "hits 3/3", "hits 4/4". "BEFORE · BOX ONLY" (`<span>` markup): 16 px box outlined, taps on text and near the box miss, "2 taps · 0 hits". Footer "row = target · 44 px".
- 1:09 Tag "07", "Five controls. One question.": the full settings phone with all control types and a list Switch, Checkbox, Radio, Segmented, Row target.
- 1:13 Promo: "Think like a senior UX designer.", Claude Code command menu (/ux-design, /ux-audit, /ux-review, /restyle), "UX Engine · Claude Code plugin" card with price, "Link in bio".

## Voice-over summary
- One setting, three possible controls, only one matches what it does: a switch acts the moment it flips and never has a Save button behind it.
- A checkbox waits and means nothing until Save; mixing the two in one form leaves users unsure which settings are live.
- Radios pick one of a few, up to five, all visible; past five the list pushes other settings off screen and becomes a dropdown.
- Two to four exclusive options that must stay in view get a segmented control; one tap switches the view, every option stays one tap away.
- A parent checkbox has three states (all checked, none empty, mix as a dash); clicking the dash turns every child on, and most apps wrongly show the parent empty.
- The label is part of the control: the whole row is the target, at least 44 px tall, because "a 16 pixel box alone gets missed by every thumb". Closes with "Does it act now or on save?" and a plugin pitch.

## Notes for the skill
- Switch semantics: native `<input type="checkbox" role="switch">` or a `<button role="switch" aria-checked>`; state changes should be persisted immediately with optimistic UI and rollback plus an error message on failure. Announce success politely (`aria-live="polite"`) if a visual "saved" chip is used.
- Checkbox commit model: track dirty state; show "unsaved" and guard navigation if changes are pending.
- Radio group: `<fieldset>` + `<legend>` (the setting name), arrow keys move selection within the group (native behaviour); one option should be preselected when a default exists.
- Dropdown threshold: "five" is a heuristic; Material and Apple HIG do not set an exact number. For 15+ options consider a searchable combobox.
- Segmented control is a single-select group: implement as radio inputs styled as segments, or as `role="radiogroup"`/`role="tablist"` if it switches views of content (then follow the tabs pattern: `aria-selected`, `aria-controls`).
- Tri-state checkbox: native `indeterminate` is a DOM property only (no HTML attribute) and is visual; also set `aria-checked="mixed"` when using a custom checkbox. The WAI-ARIA APG mixed-state example cycles mixed → checked → unchecked; the reel's "click dash = all on" matches its first step. Recompute the parent from children on every child change.
- Target size: WCAG 2.2 2.5.8 (AA) requires at least 24×24 CSS px; 44×44 is the AAA (2.5.5) and Apple HIG value, 48 dp in Material. The reel's 44 px row is the stronger recommendation.
- Keep visible focus styles on the row or control; a whole-row label should show the focus ring around the row.
