---
lesson: 004
kind: video
duration_s: 59
type: ui
category: visual
topic: Colour perception in UI: simultaneous contrast, pop-out, colour semantics
sources: frames, voice-over
---

# Three colour tricks: context, a single accent, semantic temperature

**Hook:** Two squares of the identical grey look different (one darker, one lighter) depending on the background; "your brain is lying".

## Main rule
Judge a colour only in its real surrounding (the same value reads darker on a light surface and lighter on a dark one), keep a single saturated accent for the one action that matters while everything else stays neutral, and map colour to meaning consistently: danger hue for destructive, success hue for confirm, neutral for cancel.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| identical 50% mid-grey (same value in both squares) | inner squares of the simultaneous-contrast demo | 0:02-0:03 and 0:14-0:16 on-screen badge "Both are ..." |
| 3 | number of tricks (contrast, pop-out, temperature) | 0:04-0:10 on-screen + voice |
| 6 buttons, 1 accent | pop-out demo: six buttons, five neutral + one accent in the good version | 0:23-0:33 on-screen |
| 3 roles | danger / success / neutral labels under Delete / Save / Cancel | 0:42-0:44 on-screen |
No timing, size or contrast-ratio numbers are shown.

## Before / after
1. **Simultaneous contrast (0:12-0:21).** The same grey square looks dark inside a light tile and light inside a dark tile. Applied to a CTA: a "Buy Now" button in the accent hue placed on a card of nearly the same hue is marked "Low contrast"; the same button on a dark neutral card is "High contrast". Why: perceived lightness and saturation are relative to the surround; a button only stands out when its surround differs from it in lightness, not just when the button itself is "bright".
2. **Pop-out effect (0:22-0:31).** Bad, "Everything screams": six buttons (Sign Up, Learn More, Buy Now, Subscribe, Download, Contact), each in a different saturated colour. Good, "One clear action": five buttons turned neutral grey, only Buy Now keeps the accent colour; a pointer label says "Eye goes straight here". Overlay: "When everything is bold, nothing is." Why: preattentive vision detects the single item that differs in colour without serial search; when every item differs, no item differs.
3. **Colour temperature (0:32-0:44).** "Same button" Subscribe shown in neutral grey, then in a danger hue with a chip "Urgent, act now!", then in a calm cool hue with "Safe & trustworthy", then in a success hue with "Go ahead, confirmed". Then "In the real world...": Delete (danger), Save (success), Cancel (neutral) with "It's not random." Why: users carry learned associations (warm/red = alert, cool/blue = calm, green = proceed), so the colour sets the expectation of the action before the label is read.
4. **Combined (0:45-0:55).** A Settings card (profile row, Notifications toggle, Cancel / Delete / Save Changes) with tags Contrast, Pop-out, Temperature appearing under it: dark neutral card for contrast, saturated colour only on the action buttons, and semantic hues for delete vs save.

## Do
- Check a colour against the actual background it will sit on; re-check accent buttons on every surface they appear on (light card, dark card, coloured hero).
- Give the primary CTA a surround that contrasts in lightness, not a tinted panel of the same hue.
- Reserve one saturated accent per view for the primary action; render secondary actions in neutral styling.
- Use colour semantically and consistently: danger role for destructive, success role for confirm, neutral for cancel or dismiss.

## Don't
- Don't give every button its own saturated colour; it removes the visual hierarchy.
- Don't place an accent button on a background of the same hue; it loses its edge even if both colours are vivid.
- Don't use a danger hue for a non-destructive action just to create urgency; it misleads.

## Scene by scene
- 0:00 Two tiles, light and dark, each with the same grey inner square; labels "Looks darker" / "Looks lighter"; badge that both squares share one value; overlay "Same color. Different feeling. Your brain is lying."
- 0:04 Title "Color tricks designers use on you"; preview cards cycle: Simultaneous Contrast, The Pop-Out Effect, Color Temperature, each "Coming up".
- 0:11 "Secret #1 Simultaneous Contrast": tiles with "Looks dark" / "Looks light", badge "Both are" one grey; "Same color. Two contexts."
- 0:17 "Low contrast" Buy Now on a same-hue card vs "High contrast" Buy Now on a dark card; "Context changes everything."
- 0:22 "Secret #2 The Pop-Out Effect": "Everything screams" grid of six multi-coloured buttons vs "One clear action" grid with only Buy Now coloured; "Eye goes straight here"; "When everything is bold, nothing is."
- 0:32 "Secret #3 Color Temperature": "Same button" Subscribe recoloured grey, then danger ("Urgent, act now!"), cool ("Safe & trustworthy"), success ("Go ahead, confirmed"); "Color has a voice. Make sure it says the right thing."
- 0:42 "In the real world...": Delete / Save / Cancel labelled danger / success / neutral; "It's not random."
- 0:45 "All three principles at work": Settings card; tags Contrast, Pop-out, Temperature appear one by one.
- 0:54 "Color isn't decoration. It's communication."
- 0:56 Outro "Want more design tricks? Follow for daily tips" with a Follow button.

## Voice-over summary
- Colour changes how a UI feels without the user noticing; three tricks: simultaneous contrast, pop-out, colour temperature.
- The same grey looks dark on light and light on dark; context changes everything.
- When every button demands attention nothing stands out; grey out everything except one element and the eye goes straight to it.
- Red signals danger and urgency, blue safety and trust, green go, confirm and success; the same button triggers different emotions by colour alone.
- Combined: high contrast makes the button pop, one accent guides the eye, temperature tells what each action means. "Color isn't decoration, it's communication."

## Notes for the skill
- Implement as tokens: `--color-accent` (primary CTA only), `--color-danger`, `--color-success`, neutral button styles for everything else. Theme-agnostic: the rule is the role mapping, not the hue.
- Contrast must be measured, not eyeballed (that is the lesson of simultaneous contrast): button label vs button fill at least 4.5:1 (WCAG 1.4.3), and the button boundary vs its background at least 3:1 (WCAG 1.4.11 non-text contrast) when the fill is the only cue identifying the control.
- The "good" pop-out grid renders secondary buttons as low-contrast grey that looks disabled. Secondary actions should be visually quieter (outline, ghost, neutral fill) but still meet text contrast and must not be confused with `disabled` state.
- Colour must not be the only carrier of meaning (WCAG 1.4.1): Delete needs a clear label and ideally an icon, and destructive actions should still have confirmation or undo. The combined Settings card shows both a saturated danger and a saturated success button side by side, which weakens the "single accent" rule; a common alternative is a quieter destructive button (outline or text in danger role) placed apart from the primary save.
- Colour-temperature associations are oversimplified: they are culture- and context-dependent (red can mean luck or price drop in some markets, and "red = urgency" is a persuasion tactic that can become a dark pattern). Use semantic colours for status and consequence, not for manipulation.
- Simultaneous contrast also matters for dark mode: a token tuned on a light surface can look washed out or too strong on a dark surface, so define per-theme values rather than reusing one value.
