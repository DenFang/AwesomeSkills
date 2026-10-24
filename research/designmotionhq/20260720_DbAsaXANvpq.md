---
id: DbAsaXANvpq
reel_url: https://www.instagram.com/reel/DbAsaXANvpq/
pattern_page: https://designmotionhq.com/patterns/live-cursors
date: 2026-07-20
duration_s: 51
type: ui
category: interaction
topic: multiplayer presence: live cursors, identity colour, avatar stack, selection locks, follow mode
sources: frames, voice-over, pattern page
---

# Live cursors and multiplayer presence

**Caption:** Multiplayer app UX tips
**Hook:** Three cursors land on your canvas and none of them are yours.

## Main rule
Treat multiplayer presence as one system: interpolate remote cursors between network ticks, give each user a stable colour derived from their ID, show who is present with an avatar stack, lock an element while someone edits it, and let users follow another person's viewport.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 10 updates/s (10 Hz) | server cursor position rate | 0:02-0:10 on-screen ("RAW · 10 Hz", "Server, 10/s") + voice |
| 60 frames/s | screen redraw rate for interpolated cursors | 0:03-0:10 on-screen ("Screen, 60/s") + voice |
| "10 updates in. 60 frames out." | interpolation summary | 0:03-0:10 on-screen subtitle |
| `hash(user_id) → hue` | colour derivation, "Deterministic, no server coordination needed" | 0:11-0:19 on-screen |
| 3 sessions (Monday, Wednesday, Friday) | same user keeps the same colour across sessions | 0:11-0:19 on-screen |
| 3 avatars + "+5" counter = "8 online" | avatar stack overflow (counter grows 2 → 3 → 8 online) | 0:20-0:27 on-screen + voice ("three faces, then a plus five") |
| 1 editor per shape | selection lock ("One shape, one editor") | 0:28-0:36 on-screen |
| 6 parts: cursors, interpolation, color, presence, locks, follow | summary chips | 0:45-0:50 on-screen |

The on-screen hash output is shown as a hex colour value; it is a demo value, not a rule (colour rule: not reproduced here).

## Before / after
1. **Raw vs interpolated cursor (0:03-0:10).** Raw: the cursor jumps between discrete dots, one per server tick (10 per second). Interpolated: the cursor glides smoothly through the same points at 60 fps. Why: motion perception needs continuous movement; jumps 100 ms apart read as lag or teleporting and make another person's intent hard to follow.
2. **Random vs hashed colour (0:11-0:19).** The user ID is hashed into a hue; the same person shows the same cursor/label colour on Monday, Wednesday and Friday. Why: a stable colour becomes a recognisable identity that can be tracked peripherally without reading the name label; random colours per session reset that learning each time. Deterministic hashing needs no server coordination.
3. **Presence before activity (0:20-0:27).** Avatar initials stack in the file header (1 → 3 faces, then "+5"), with an "8 online" count and the note "Presence renders before a single message". Why: users sense who is in the room before anyone edits or chats, which sets expectations for concurrent changes.
4. **Selection lock (0:28-0:36).** When Sarah selects a card it gets an outline and a lock badge with her name in her colour. Alex's cursor approaches; a tooltip "Sarah is editing" appears and he cannot take it; he moves away. Why: two simultaneous edits on one shape produce a corrupted result; the lock prevents the conflict instead of resolving it after the fact.
5. **Follow mode (0:37-0:44).** Clicking Maya's avatar frames the whole viewport in her colour with a "Following Maya" pill; her pans and zooms now drive the follower's screen. Why: it replaces screen sharing for design review, and the coloured frame makes the borrowed-viewport mode obvious.

## Do
- Interpolate remote cursor positions between server ticks so movement renders smoothly at display frame rate.
- Derive each user's colour from a stable hash of their ID so it survives across sessions.
- Show an avatar stack with an overflow counter (e.g. 3 faces + "+N") and an online count.
- Lock an element the instant someone selects it; outline and badge it in that editor's colour, and show "<Name> is editing" to others who try to grab it.
- Offer follow mode from the avatar stack, with a clear frame and label while following.

## Don't
- Don't draw cursors at the raw network tick rate.
- Don't assign random colours per session.
- Don't let two users edit the same element at the same time.

## Scene by scene
- 0:00 "Your canvas. Their cursors." A design canvas (file "onboarding-flow") with a profile card and a "Weekly actives 12,480" chart card; three labelled cursors (Sarah, Alex, Maya) drift in; pill "3 collaborators · live".
- 0:03 "Interpolation · 10 updates in. 60 frames out." Two panels: "RAW · 10 Hz" (cursor hops between dots) and "INTERPOLATED" (cursor glides). A "One second of traffic" strip: 10 server blocks vs 60 screen ticks filling.
- 0:11 "Color from identity · hash(user_id) → hue": an e-mail chip → scrambling hash digits settle → colour swatch; "Deterministic, no server coordination needed". Three session cards (Monday, Wednesday, Friday) each with Sarah's cursor in the same colour; footer "Same person, same color, every session".
- 0:20 "Presence · Feel the room before you read a name": file header avatar stack grows SC → SC AR MK → + "+5"; footer "2 online → 3 online → 8 online · Presence renders before a single message"; cursors appear on the canvas.
- 0:28 "Selection locks · One shape, one editor": Sarah selects the profile card; selection handles and a lock badge in her colour; Alex's cursor approaches, "Sarah is editing" tooltip, Alex leaves. Footer "Locks prevent the conflict before it exists".
- 0:37 "Follow mode · Click an avatar, ride their viewport": cursor clicks the MK avatar; viewport gets a frame in Maya's colour and "Following Maya"; the view pans/zooms with her cursor. Footer "A design review without the screen share".
- 0:44 Transition.
- 0:45 Outro "Multiplayer is a system. Presence is engineered, not accidental." avatar stack "+5 · 8 collaborators · live", six topic chips, follow button with the three cursors gathered on it.

## Voice-over summary
- The server sends about 10 positions per second while the screen draws 60; interpolation fills the gaps so cursors glide instead of teleporting.
- Each user's colour is hashed from their ID: same person, same colour, every session, recognisable from the corner of the eye.
- Avatars stack before anyone speaks: three faces and a "+5" counter tell you the room is full before you read names.
- When someone grabs a card it glows in their colour and locks, because two people editing one shape corrupts it.
- Clicking an avatar makes your viewport follow theirs, live, replacing screen share in design reviews.
- "Multiplayer is a system."

## Notes for the skill
- Interpolation: render remote cursors slightly behind real time (buffer about one tick, ~100 ms at 10 Hz) and lerp between the last two received points, or use a light spring; extrapolate only briefly. Use `requestAnimationFrame`; skip smoothing for the local cursor (never delay the user's own pointer).
- Throttle outgoing cursor updates (the 10/s figure) and drop updates when the tab is hidden; fade out idle cursors after a few seconds of inactivity.
- Hashed colour: hash a stable internal user ID, not the e-mail address (the demo uses an e-mail; avoid exposing personal data in client-side hashing). Map the hash to a curated set of hues tested for contrast, because the name label text sits on the user colour and needs at least 4.5:1; resolve visible collisions within one session if two present users land on near-identical hues. Never use colour as the only identifier: keep the name label on cursors and initials in avatars.
- Avatar stack: give each avatar an accessible name ("Sarah Chen, editing"), make the "+N" counter a button that lists everyone, and keep the stack in a fixed place (file header).
- Locks: release automatically on deselect, disconnect or a timeout so a crashed client does not hold a lock forever; explain the lock in text ("Sarah is editing") rather than silently ignoring clicks; consider a "request access" action. For text or fine-grained data, CRDT/OT merging can replace hard locks; locks suit discrete objects like shapes.
- Follow mode: any local pan, zoom or Esc should exit follow mode immediately, with a visible "Following <Name>" indicator and an explicit stop control. Respect `prefers-reduced-motion` by snapping the followed viewport rather than animating large pans and zooms.
