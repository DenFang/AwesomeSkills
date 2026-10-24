---
lesson: 013
kind: video
duration_s: 53
type: ui
category: motion
topic: Premium modal: spring entrance, staggered content, scaled exit, blurred backdrop, button feedback
sources: frames, voice-over
---

# Cheap vs premium modal: entrance, backdrop, micro-interactions

**Hook:** The same "Delete project?" modal shown twice, cheap vs premium: "Same modal. Different feeling. Here's how."

## Main rule
Do not toggle a modal on and off: enter with a slight scale-up plus fade (spring with a tiny overshoot) and stagger its inner content, exit by scaling down to about 0.95 while fading to 0, separate it from the page with a blurred backdrop and a deep shadow, and give every button in it hover and press feedback.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| scale 0.934, opacity 0.68 | modal mid-entrance (sampled frame, not a keyframe spec) | 0:09 on-screen readout |
| scale 1.001, opacity 1.00 | overshoot just past 1 during spring settle (sampled; true peak not shown) | 0:10 on-screen readout |
| scale 1.000, opacity 1.00 | resting state | 0:11-0:16 on-screen readout |
| +0f, +5f, +10f, +15f | stagger offsets in frames for icon, title, body text, buttons | 0:10-0:16 on-screen markers |
| about 167 ms per step at 30 fps (83 ms at 60 fps) | stagger step derived from 5 frames; frame rate not stated | calculation, not stated |
| scale 0.950, opacity 0.00 | exit end state ("scale down, fade out") | 0:17-0:21 on-screen readout |
| backdrop-filter: blur(20px) | backdrop behind the premium modal (19px read during the transition) | 0:23-0:30 on-screen |
| 3 | secrets: entrance and exit, backdrop and depth, micro-interactions | 0:03-0:07 on-screen + voice |
No durations in ms, spring stiffness/damping or shadow values are shown.

## Before / after
1. **Entrance and exit (0:08-0:22).** Cheap: the modal "just appears" (hard cut) and vanishes the same way. Premium: spring scale from below 1 to 1 with a very small overshoot, opacity rising with it; content rows stagger in 5 frames apart (icon, title, description, buttons); on close it scales to 0.95 and fades to 0 instead of disappearing. Why: motion shows where the layer came from and went; a small scale change keeps spatial continuity without travelling far, and staggering gives a reading order instead of a wall of content appearing at once.
2. **Backdrop and depth (0:22-0:30).** Cheap: a flat dark overlay over the Projects dashboard. Premium: the page behind is blurred (`backdrop-filter: blur(20px)`) and the dialog gets a deep shadow, "now it floats". Why: blur removes competing detail from the background while keeping context recognisable; the shadow creates a clear elevation difference so the dialog reads as the top layer.
3. **Micro-interactions (0:31-0:43).** Cheap: hovering Delete changes nothing, no feedback. Premium: Delete gains a glow on hover, compresses on press and springs back, and even the small close (X) button reacts to hover. Why: immediate state change confirms the control is interactive and that input was received.
4. **Combined (0:44-0:50).** Over the dashboard: spring entrance, blur backdrop, responsive buttons, labelled with chips "Spring entrance", "Blur backdrop", "Micro-interactions": "Now it feels expensive."

## Do
- Enter with scale (from roughly 0.93-0.95) plus opacity, settling with a barely visible overshoot.
- Stagger inner content in short equal steps (4 groups, 5 frames apart in the demo).
- Exit with a reverse transform: scale to about 0.95 and fade to 0.
- Blur the page behind the dialog (about 20 px) and add a strong shadow to the dialog surface.
- Give primary, secondary and close buttons hover, pressed and focus states.

## Don't
- Don't hard-cut a modal in or out.
- Don't rely on a flat dimming layer alone when the background is busy and competes with the dialog.
- Don't leave buttons inside a dialog without hover or press feedback, including the close icon.

## Scene by scene
- 0:00 Split "Cheap" vs "Premium": the cheap modal is shown static, the premium one is still animating in; "Same modal. Different feeling. Here's how."
- 0:03 "3 secrets to premium modals": cards Entrance & Exit, Backdrop & Depth, Micro-interactions, each "Coming up".
- 0:08 "Secret #1 Entrance & Exit": empty stage, "A cheap modal just appears"; 0:09 modal mid-animation with readout scale 0.934 / opacity 0.68.
- 0:10 Readout scale 1.001 (overshoot), then 1.000; frame markers +0f, +5f, +10f, +15f next to icon, title, text, buttons; "A premium modal? ... overshoot. Content staggers in."
- 0:17 Exit: readout scale 0.950 / opacity 0.00, modal gone; "doesn't vanish", "Scale down", "Fade out", "Smooth".
- 0:22 "Secret #2 Backdrop & Depth": Projects dashboard (Landing Page, Mobile App, Dashboard, API Docs, Design System cards) with "A cheap modal?"; then "Flat dark overlay".
- 0:24 Readout `backdrop-filter: blur(20px)`, background blurred, dialog with deep shadow; "A premium modal blurs background. Add a deep shadow. Now it floats."
- 0:31 "Secret #3 Micro-interactions": cursor on Delete, "Cheap buttons, no feedback"; then "Premium?": Delete glows, press bounce, close button responds; "Every pixel reacts."
- 0:44 "Put it all together": dashboard, modal enters, chips Spring entrance, Blur backdrop, Micro-interactions appear; "Now it feels expensive."
- 0:51 Outro "Design is in the details. Follow for more."

## Voice-over summary
- Same modal, different feeling, through three secrets: entrance and exit, backdrop and depth, small details inside.
- A cheap modal just appears; a premium one uses a spring scale with overshoot, staggers its content in and on close scales down and fades out.
- A cheap modal uses a flat dark overlay; a premium one blurs the background and adds a deep shadow so it floats.
- Cheap buttons give no feedback; premium ones glow on hover, bounce back on press, and even the close button responds.
- Spring entrance, blur backdrop, responsive buttons: "Design is in the details."

## Notes for the skill
- CSS sketch: enter `opacity: 0; transform: scale(.95)` to `opacity: 1; transform: scale(1)` with a spring-like curve (for example a `linear()` spring or a cubic-bezier with slight overshoot); exit back to `scale(.95)` and `opacity: 0`, typically shorter than the entrance. Overshoot must stay tiny for a dialog (the readout shows 1.001); a visible bounce on a destructive confirm dialog is inappropriate.
- Stagger only a few groups and keep the total short so the primary action is usable fast; do not block clicks until the stagger finishes.
- `backdrop-filter: blur()` is expensive on low-end devices and large viewports; provide a fallback (a semi-opaque scrim via `@supports not (backdrop-filter: blur(1px))`) and keep a dimming scrim anyway so the dialog text contrast does not depend on what is behind.
- Accessibility the video skips: use `<dialog>` with `showModal()` or `role="dialog"` + `aria-modal="true"`, label it with the title (`aria-labelledby`) and description (`aria-describedby`), move focus into the dialog (for a destructive confirm, initial focus on Cancel, per WAI-ARIA APG), trap focus, close on Escape, and return focus to the trigger on close. Make the inert page truly inert (`inert` attribute), not just blurred.
- Under `prefers-reduced-motion: reduce`, drop the scale and stagger and keep a short opacity fade.
- Hover glow is invisible on touch and to keyboard users: also define `:focus-visible` and `:active` (press) states. The close button needs an accessible name and a target of at least 24x24 px (WCAG 2.5.8), ideally 44 px.
- "Premium = more effects" is a simplification: the mechanisms that matter are spatial continuity, layer separation and feedback; glow and blur are one stylistic way to get there.
