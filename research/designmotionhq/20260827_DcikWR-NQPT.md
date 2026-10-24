---
id: DcikWR-NQPT
reel_url: https://www.instagram.com/reel/DcikWR-NQPT/
pattern_page: none
date: 2026-08-27
duration_s: 54
type: ui
category: visual
topic: avatar component system (fallback chain, deterministic colour, initials, stacks, presence, sizes)
sources: frames, voice-over, caption
---

# Avatar as a system: fallback, colour from name, initials, stack, presence ring, three sizes

**Caption:** "Avatar UI tips".
**Hook:** The photo can fail; the avatar must not.

## Main rule
Treat the avatar as a small system: resolve image → initials → generic icon (never a broken image), derive the background colour deterministically from the name, show two initials by default (one only at tiny sizes), overlap group avatars and cap the row with a "+N" chip, put presence status on a ring around the avatar instead of an extra badge, and allow exactly three size tokens: 24, 32 and 40 px.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 4-step resolve order: image › initials › icon › broken (never) | fallback chain; "image: if it loads", "initials: from the name", "generic icon: last resort", "broken square: never" | 0:03-0:09 on-screen + voice |
| "Sarah Chen" → 0x629b2403 → % 6 = 1 → palette colour | deterministic colour: hash the name, take modulo palette size (6), index into a fixed palette | 0:10-0:17 on-screen + voice |
| 6 | palette size implied by "% 6" | 0:11-0:17 on-screen |
| 2 initials by default · 1 only when tiny | initials rule | 0:19-0:28 on-screen + voice |
| 48px, 32px, 24px show "SC"; 16px shows "S" | sizes in the initials demo; at 16 px "two letters turn to mush → drop to one" | 0:22-0:25 on-screen |
| JD ("a person") vs J ("a bug") | two vs one initial at normal size; "Jamie Dean commented" vs "J commented" | 0:26-0:28 on-screen + voice |
| 7 members → showing 4 · +3 more | stack overflow: cap 4 shown, overflow chip "+3" | 0:29-0:33 on-screen + voice |
| OVERLAP −52px · CAP 4 shown · OVERFLOW +3 | stack parameters as labelled (−52 px applies to the enlarged demo avatars; relative overlap looks like roughly a third of the diameter) | 0:32-0:33 on-screen |
| 7 collaborators | "Design Review" row with a compact stack and "+3" | 0:29-0:33 on-screen |
| Online / Away / Offline | ring states mapped to success / warning / neutral-grey colour roles | 0:34-0:40 on-screen + voice |
| 24 · LIST, 32 · HEADER, 40 · PROFILE | the only three avatar sizes, px | 0:41-0:46 on-screen + voice |

## Before / after
- **Broken image vs fallback chain.** Bad: the photo fails and a broken-image square with "image failed to load" appears. Good: the avatar silently falls back to initials ("fallback → initials", "the fallback ships anyway"); if there is no name, a generic person icon. Why: a broken square reads as a bug and destroys trust; a graceful fallback keeps the person identifiable.
- **Random palette vs deterministic colour.** Bad: the same user gets a different colour in the chat header, comment and member list ("Random palette · who is this?"). Good: one function maps the name to one palette colour on every screen ("One name, one color"). Why: colour becomes a recognition cue only when it is stable; random colours make users second-guess identity.
- **One letter vs two letters.** Bad: "J commented" with a single-letter avatar looks like a placeholder or error. Good: "JD", "Jamie Dean commented". Why: two letters read as a name; one letter reads as missing data. Exception: at 16 px two letters become illegible, so drop to one there.
- **Long row vs capped stack.** Bad: all 7 avatars in a row, wide and noisy. Good: overlap the avatars and show 4 plus a "+3" chip. Why: the overlap signals "a group" and the cap keeps width fixed regardless of member count, while the count stays visible.
- **Second badge vs ring.** Bad: an "Online" pill, an "active now" label and a status dot stacked on one avatar ("stacked, redundant"). Good: one coloured ring around the avatar ("one integrated signal"). Why: one signal per avatar is less visual noise and scales down to small sizes.
- **Arbitrary sizes vs three tokens.** Good: 24 in lists, 32 in headers, 40 on profiles, "nothing between". Why: a fixed scale keeps alignment and visual rhythm consistent across screens.

## Do
- Implement the resolve order image → initials → generic icon; hide the `<img>` on `error` and render the next fallback.
- Hash the display name (or better, the stable user ID) and use `hash % paletteLength` to pick the avatar background from a fixed theme palette.
- Show first + last initial by default; switch to a single initial only below about 20 px (16 px in the reel).
- Overlap stacked avatars, cap visible ones (4 shown in the reel) and end with a "+N" chip using the remaining count.
- Show presence as a ring around the avatar, one state at a time (online / away / offline).
- Define exactly three size tokens (24 / 32 / 40 px) and map them to contexts (list / header / profile).

## Don't
- Don't ever show the browser's broken-image glyph inside an avatar.
- Don't assign avatar colours randomly per render or per screen.
- Don't show single-letter initials at normal sizes.
- Don't stack an extra status pill or dot on top of a ring or on a plain avatar.
- Don't introduce ad hoc avatar sizes between the tokens.

## Scene by scene
- 0:00 Label "AVATAR · COMPONENT SYSTEM"; a broken-image placeholder with a danger chip "image failed to load", danger-tinted background. Mini chain "ONE FAILS → USE THE NEXT": image → SC → icon.
- 0:01 The avatar becomes "SC" initials with a progress-like ring; chip "fallback → initials"; footer "the fallback ships anyway".
- 0:03 Tag "FALLBACK · CHAIN", title "One image fails? Degrade, don't break."; four numbered cards: 1 image (if it loads), 2 initials (from the name), 3 generic icon (last resort), 4 broken square (never, danger-framed and crossed out). Bar "RESOLVE ORDER image › initials › icon › broken"; chip "Graceful degradation".
- 0:10 Tag "COLOR · DETERMINISTIC", "Same name, same color. Everywhere."; pipeline "Sarah Chen" → hash value scrolls → 0x629b2403 → "% 6 = 1" → avatar colour chip. Row "ONE FUNCTION · EVERY SCREEN" (chat header, comment, member list, same colour); row "RANDOM PALETTE · WHO IS THIS?" with three different colours cycling. Chip "One name, one color".
- 0:19 Tag "INITIALS · DEFAULT", "Two letters read as a person."; "Sarah Chen" → SC; then SC, MR, AO under their names.
- 0:22 Size ramp 48 / 32 / 24 / 16 px; at 16 px "SC" becomes "S" (danger colour) with note "two letters turn to mush → drop to one". Chip "2 by default · 1 only when tiny".
- 0:26 Two cards: "A PERSON" JD with "Jamie Dean commented" vs "A BUG" J with "J commented".
- 0:29 Tag "STACK · OVERFLOW", "Overlap the group, cap the row."; "7 MEMBERS" row of 7 overlapping avatars collapses to 4 plus "+3"; labels "OVERLAP −52px", "CAP 4 shown", "OVERFLOW +3"; a "Design Review · 7 collaborators" list row uses the compact stack. Chip "Overlap + overflow".
- 0:34 Tag "PRESENCE · RING", "Status lives on the ring."; "ON THE RING: one integrated signal" vs "SECOND BADGE: stacked, redundant" (Online pill + active-now label + dot, warning icon). Legend: SC online, MR away, AO offline with ring colours in success / warning / neutral roles. Chip "Status on the ring".
- 0:41 Tag "SIZE · SCALE", "Three sizes. Then stop."; avatars on a baseline labelled 24 · LIST, 32 · HEADER, 40 · PROFILE, with example rows (Editor / online / Product Designer). Chip "Three tokens, nothing between".
- 0:47 End card "More UI systems, One component, decoded every week." with a stack "+1", four summary cards (Fallback chain: photo, initials, icon; Color from name: same person, same hue; Two initials: one only when tiny; Status on the ring: never a second badge), "designmotionhq.com", "Link in bio", "Save".

## Voice-over summary
- When the photo fails the avatar should not: image first, initials on failure, generic icon as last resort, never a broken square.
- Generate the background colour from the name, so the same person has the same colour on every screen; no random palette.
- Two initials (first and last name) by default; one letter only at tiny sizes, because "JD reads as a person, a lone J reads as a bug."
- Overlap avatars to show a group; cap the row and spill the rest into "+3".
- A ring shows who is online; status goes on the ring, never in a second badge.
- Pick three sizes and stop: 24 in lists, 32 in headers, 40 in profiles.

## Notes for the skill
- Hash input: the reel hashes the display name; prefer a stable user ID so the colour survives a name change and two people with the same name can differ. Any simple stable hash (e.g. FNV-1a or djb2) mod palette length works; palette colours come from the project theme and must give initials at least 4.5:1 contrast (text under 18 px) against each background.
- Initials extraction: handle single-word names (take one or two letters of the word), multi-part names (first + last), non-Latin scripts and emoji; uppercase with locale awareness.
- Fallback implementation: render initials underneath and fade the image in on `load`; on `error` keep initials. Avoid layout shift by fixing width/height to the size token. Use `alt` on the image with the person's name; if the name is also printed next to the avatar, the avatar can be decorative (`alt=""`, `aria-hidden`).
- Stack: overlap is usually expressed as negative margin of about 25-35% of the diameter plus a ring in the surface colour to separate circles; the "+N" chip should have an accessible label ("3 more members") and ideally reveal the full list on hover/focus/tap.
- Presence ring: colour alone violates WCAG 1.4.1 (use of colour); add a text alternative (`aria-label="Sarah Chen, online"`, tooltip) and consider differing ring styles (solid / dashed / none) so away vs offline is distinguishable without colour. The reel's "never a second badge" is a visual guideline, not an accessibility exemption.
- Sizes: 24 px avatars used as tap targets fall below the 44 px touch-target recommendation; pad the hit area if the avatar is interactive.
- The reel shows the palette colour of the example as a hex code; the skill should keep it as a theme token.
