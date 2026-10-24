---
id: DZ7NPPItOoJ
reel_url: https://www.instagram.com/reel/DZ7NPPItOoJ/
pattern_page: https://designmotionhq.com/patterns/password-field-ux
date: 2026-06-23
duration_s: 57
type: ui
category: forms
topic: password field UX (entropy, live checklist, strength meter, reveal, paste, generated password)
sources: frames, voice-over, pattern page
---

# Password field UX: coach while typing, don't punish after submit

**Caption:** not captured yet
**Hook:** Eight characters and a symbol still makes a weak password: "P@ssw0rd!" passes every rule and is cracked in about two hours.

## Main rule
Measure password strength by entropy/guessability, not by composition checkboxes; show requirements and a strength meter live while the user types; provide a show/hide toggle; never block paste; and offer a one-tap generated password (the platform's suggested-password feature) as the default path.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 8+ characters, 1 symbol | composition rules in the opening form; "P@ssw0rd!" satisfies both and the meter still says Weak | 0:00-0:02 on-screen + voice |
| capital P, @ for a, 0 for o | the predictable substitutions in "P@ssw0rd!" | 0:03-0:12 on-screen chips + voice |
| 28 bits of entropy, crack time 2 hours (counter passes 14 min) | "P@ssw0rd!" (complex & short) | 0:06-0:12 on-screen + voice ("cracks in two hours") |
| 73 bits of entropy, crack time 3 centuries (counter passes 6 days) | "wrong-mango-battery-sky", 23 characters, zero symbols (simple & long) | 0:08-0:12 on-screen |
| 4 rules: 1 uppercase, 1 number, 8+ characters, 1 symbol | live checklist vs after-submit errors | 0:12-0:20 on-screen |
| 4-segment meter: Weak → Fair → Almost → Strong | live strength meter for "tango-r1ver-Lamp"; hint chips "first chars", "+ two words", "+ a number", "+ 16 chars" | 0:22-0:29 on-screen |
| 22 chars, unique | pasted password-manager value "horse-velvet-anchor-42" → Strong | 0:37-0:39 on-screen |
| 0 typing / 0 weak choices / 0 reuse | outcome of accepting a generated password ("kV9#mQ2-xT8&wNp4", 16 chars) | 0:41-0:51 on-screen + voice |

## Before / after
- **Composition rules vs entropy.** Bad: a checklist of 8+ characters, a symbol, a number, which "P@ssw0rd!" ticks completely while being a dictionary word with common substitutions (28 bits, about 2 hours). Good: score guessability; a long, symbol-free passphrase "wrong-mango-battery-sky" scores 73 bits (about 3 centuries). Why: attackers' dictionaries already include predictable substitutions; length multiplies the search space far more than one extra symbol class.
- **Rules after submit vs checklist while typing.** Bad ("Rules after submit"): user types, clicks Sign up, and only then gets three danger-coloured errors ("Must contain an uppercase letter / a number / a symbol"). Good ("Checklist while typing"): all requirements are visible under the empty field; each ticks to the success state as the input satisfies it; the Sign up button becomes active once all four are met (caption: every rule in the success state before the button is pressed). Why: users can meet requirements on the first attempt; hidden rules cause failed submits and frustration.
- **Errors vs meter.** Bad: errors that only appear after the fact. Good: a 4-segment meter that moves Weak (danger) → Fair (warning) → Almost → Strong (success) as the user adds words, numbers and length, with chips showing what raised the score. Why: incremental feedback coaches the user towards a stronger choice ("Meters coach while typing" vs "Errors punish after the fact").
- **Masked only vs reveal toggle.** Bad: masked dots hide typos (the user cannot see that they typed "Summer24!"). Good: an eye icon button in the field toggles plain text.
- **Block paste vs allow paste.** Bad: "Paste disabled"; the password manager cannot fill the field. Good: paste allowed; manager fills "horse-velvet-anchor-42" (22 chars, unique) and the meter jumps to Strong. Why: managers produce longer and more random passwords than people type.
- **User-invented vs generated password.** Best: on focus, offer "Use suggested password" (generated, e.g. "kV9#mQ2-xT8&wNp4"); one tap fills it, the meter reads Strong, chips "Generated", "Unique", "Saved to keychain", and Create account becomes active. Why: zero typing, zero weak choices, zero reuse. The video notes this is built into iOS, Android and every modern browser.

## Do
- Estimate strength by guessability (entropy, dictionary and pattern checks), not by counting character classes.
- Show every requirement before typing and tick each one live.
- Show a strength meter with words (Weak / Fair / Almost / Strong) plus colour, updating on every keystroke.
- Add a show/hide (eye) toggle inside the field.
- Allow paste and password-manager autofill.
- Let the platform offer a generated password (mark up the field so it can).

## Don't
- Don't reveal rules only after a failed submit.
- Don't treat "has a capital and a symbol" as proof of strength.
- Don't block paste or force manual retyping of long passwords.
- Don't rely on colour alone for meter levels.

## Scene by scene
- 0:00 "Create your account" card; password field filling with dots; checklist "8+ characters" and "1 symbol" both tick; meter shows one danger segment "Weak"; Create account inactive. Caption "Passes the rules. Still weak."
- 0:03 "Strength is entropy": two cards. Left "Complex & short" P@ssw0rd! with chips capital P / @ for a / 0 for o and ticks 8+ chars, symbol, number; right "Simple & long" wrong-mango-battery-sky "23 characters, zero symbols". Caption "Entropy = how many guesses it takes to crack."
- 0:06 Counters run: left crack time 14 min → 2 hours, 0 → 11 → 28 bits; right 0 → 21 → 58 → 73 bits, crack time 6 days → 3 centuries. Comparison bars below (short danger bar vs long success bar).
- 0:09 Caption "Length beats symbols."
- 0:12 "Show the rules early": top card "Rules after submit" (field, Sign up active), bottom card "Checklist while typing" (field with 4 grey rules, Sign up inactive). Click on top Sign up → three error lines and danger border.
- 0:16 Bottom field typed; rules tick one by one (1 uppercase, 1 symbol, 1 number, 8+ characters); Sign up becomes active. Caption: every rule turns to the success state before the button is pressed.
- 0:22 "Strength meter: A growing bar says almost." Typing "tan" (Weak) → "tango-" (Weak, chip "first chars") → "tango-r1v" (Fair, "+ two words") → "tango-r1ver-Lam" (Almost, "+ a number") → "tango-r1ver-Lamp" (Strong, "+ 16 chars"). Cards "Meters coach while typing" and "Errors punish after the fact" (the latter in danger colour once highlighted).
- 0:30 "Reveal & paste": eye toggle reveals "Summer24!" (Fair). Password manager chip slides in; with "Block paste" selected a "Paste disabled" warning appears.
- 0:37 "Allow paste" selected: field fills "horse-velvet-anchor-42", meter Strong, tag "pasted, 22 chars, unique". Caption "Managers type stronger passwords than humans."
- 0:40 "The strongest pattern: Built into iOS, Android and every modern browser." Focus on empty field shows "Use suggested password kV9#mQ2-xT8&wNp4"; tap fills it, meter Strong, chips Generated / Unique / Saved to keychain; counters "0 typing", "0 weak choices", "0 reuse" light up; Create account activates.
- 0:52 End card with the generated password and full meter, "Follow for more form UX", Save button.

## Voice-over summary
- "Eight characters, one symbol, still weak": P@ssw0rd! passes every rule and cracks in two hours.
- Strength is entropy, not checkboxes; length beats symbols.
- Rules revealed after submit cause rage; show the checklist live and tick each requirement before the button is pressed.
- A meter coaches in real time; errors only punish after the fact.
- Masked dots cause typos, so give an eye toggle; never block paste, because password managers type stronger passwords.
- Strongest pattern: offer the generated password in one tap (generated, unique, saved): zero typing, zero weak choices, zero reuse.

## Notes for the skill
- Markup for managers and generated passwords: `<input type="password" autocomplete="new-password">` on sign-up (and `autocomplete="current-password"` on sign-in), a username/email field with `autocomplete="username"` in the same form, optional `passwordrules` attribute (Safari) to describe constraints. Never set `onpaste="return false"`.
- NIST SP 800-63B (rev. 4) aligns with the video: no composition rules, allow paste, offer show-password, check against breached/common-password lists, and prefer length (15+ characters when the password is the only factor, at least 8 with MFA). Use a guessability estimator such as zxcvbn rather than character-class counts.
- The entropy and crack-time numbers on screen are illustrative, not reproducible: real crack time depends on the hashing algorithm and attacker hardware, and a 4-word passphrase from a typical wordlist is roughly 44-52 bits, not 73. Present the comparison, not the exact numbers.
- Reveal toggle: a real `<button type="button">` with `aria-label="Show password"` / "Hide password" and `aria-pressed`; it switches `type` between `password` and `text`. Keep focus and caret in the field. Touch target at least 24×24 CSS px (WCAG 2.2) and ideally 44×44.
- Live checklist and meter: link via `aria-describedby`; announce changes politely (or only on blur) so screen readers are not flooded on every keystroke. Each rule needs an icon + text state, not colour alone; the meter needs a text label (Weak/Fair/Almost/Strong).
- Conflict with the disabled-buttons pattern: this video keeps "Sign up"/"Create account" disabled until requirements are met. Prefer the enabled-button approach (validate on click, focus the field, show the unmet rules); the live checklist already makes the requirements visible.
- Do not save the password to analytics or logs while measuring strength; compute the meter client-side.
