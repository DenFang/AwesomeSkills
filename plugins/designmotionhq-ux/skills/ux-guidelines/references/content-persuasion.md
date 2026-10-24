# Content, flow psychology and the "AI look"

Words, page structure, the psychology of flows, and the tells that make an interface look machine-generated. Persuasion rules come with honesty limits: the skill never builds dark patterns.

Severity: **P0** deceptive or harmful, **P1** confusing or generic, **P2** polish.

---

### CON-1 · Microcopy is interface (P1)
**Applies to.** all interface copy: button labels, error messages, empty states, field labels and hints, confirmations.
**Rule.** The button label is the last thing read before committing, so it names the reward or result ("Create my free account", "Send 3 invoices"), never "Submit". Errors name the cause in plain words and hand over the fix as a link or action ("That email is already registered. Log in instead?"): a detour, not a dead end. Empty states give one action, the first step (STA-6), so they never look like a bug. Labels stay visible after typing; a placeholder is not a label (FRM-2). Write like a helpful colleague: plain words, "you", no system jargon ("operation failed", "invalid input", "null"), and stay specific: friendly but vague ("Hmm, that didn't go through") still needs the cause when it is known, and jokes stay out of serious failures (payments, data loss). Keep one voice across the product. Destructive confirmations repeat the verb and the object. On login and password reset, never reveal whether an account exists; use a neutral message there.
**Detect.** "Submit", "OK", "Click here", "Error occurred", "Invalid", "No data"; a `placeholder` with no `<label>`; mixed tone; shouting capitals in body copy.

### CON-2 · Landing pages follow one skeleton (P1)
**Applies to.** landing and marketing pages: hero, social-proof block, problem section, benefits or solution section, final CTA.
**Rule.** Hero → Proof → Problem → Solution → Final CTA. The hero answers what it is, who it is for and why it matters within a few seconds: one concrete headline, one subhead naming the audience, one primary CTA and one product visual, never a carousel or slider. On mobile it stacks text, CTA, visual with the CTA above the fold; on desktop text and CTA sit left, the visual right. Proof sits directly under the hero, never only at the bottom, because trust is decided early: logos people recognise, one testimonial with name, role and a measurable result, and one real number. Name the problem's cost in concrete time, money or effort before the cure. The solution is at most three benefits, each a measurable outcome ("Save 10 hours a week"), not a feature label. The final CTA repeats the hero CTA's label, style and destination. Longer pages may add how-it-works, pricing or FAQ between Solution and Final CTA; the five beats keep their order. An animated proof counter puts the final value in the DOM and skips the count under reduced motion.
**Detect.** Features before any proof; proof only above the footer; six-plus benefit cards; a carousel or slider component in the hero; different CTA labels or `href`s top and bottom.

### CON-3 · Remove the generated-hero tells (P1)
**Applies to.** hero sections.
**Rule.** A generated page decorates because it has nothing concrete to show. Swap every decoration for the product itself:
| Tell | Fix |
|---|---|
| Gradient headline full of adjectives ("Supercharge your workflow") | Plain headline naming the outcome; subline naming the audience |
| Big blurry colour blob behind everything | Neutral background; the only colour on the product shot and one primary button |
| Two equal buttons side by side ("Get started" / "Learn more") | One primary button; the second becomes a text link with an arrow |
| "Trusted by 10,000+ users" over grey anonymous logos | One verifiable quote with name, role and a result with a unit |
| Three icon-in-a-circle cards with one word each (Fast, Secure, Easy) | One real product screenshot with three annotations pointing at real UI |
The H1 is the outcome (verb plus result), the subtitle the category plus audience, both in solid text: gradient-clipped text has no single contrast value and breaks in forced-colours mode. The secondary text link stays a real link or button, recognisable without colour (underline or arrow, the arrow `aria-hidden`), with at least a 24 × 24 px hit area. Annotations are real text, not baked into the image, and become a numbered list under it on narrow screens; the screenshot gets meaningful `alt`. With no real, attributable quote, show the product rather than inventing proof (CON-8).
**Detect.** Search the copy for "supercharge", "seamless", "unlock", "revolutionize", "powerful", "next-gen", "all-in-one"; gradient-clipped headings; two adjacent CTAs with the same size and fill; large blurred decorative blobs (`filter: blur()` on an absolutely positioned gradient); a quote with no name, role or number; generic feature-card grids.

### CON-4 · Order is a decision (P2)
**Applies to.** navigation bars, landing page section order, onboarding slides, ordered lists of features or steps.
**Rule.** People recall the first and last items of a sequence best and the middle much less. Give the edge slots to what matters and put necessary but forgettable items in the middle: logo first and primary CTA last in a nav bar, strongest promise first and strongest proof (testimonial, logo wall, case study) last on a landing page, the hook on the first onboarding slide and the payoff on the last. Use position to pick the edge slots, never to hide links people need: menus people revisit are scanned, so grouping and labels still decide findability, and conventions win (on a mobile tab bar the most used destination goes first). A critical middle step (a permission, a data connection) gets its own emphasis rather than relying on position.
**Detect.** The primary CTA sitting among the nav links; key proof sandwiched between filler sections; the decisive onboarding step buried mid-sequence.

### CON-5 · Design the peak and the end (P1)
**Applies to.** multi-step flows and their final screens: checkout, onboarding, sign-up, upload, submission.
**Rule.** People judge a flow by its most intense moment and its last one, not the average. Plant one genuine positive peak (a result that beats expectation, a real perk; one is enough) instead of polishing every step equally. Make the final screen substantive: a heading confirming the outcome, the reference (order number), what happens next (delivery date, confirmation sent) and a next action, with focus moved to that heading or the message announced via `role="status"`. Celebration motion is optional seasoning (MOT-15). Never let a flow end on friction (a confusing confirmation, an upsell wall): if the last step can fail, as payment can, keep the entered data, give the cause in plain words and offer the fix in place ("Try another card"), so the recovery becomes the ending.
**Detect.** Flows ending on a bare "Success", a small "Order placed." or a redirect with no context; checkout and onboarding ending in a modal upsell; a final-step error that clears the form or sends the user back to the start.

### CON-6 · Remove the generated-dashboard tells (P1)
**Applies to.** dashboards.
**Rule.** Same principle as CON-3: decoration replaces content.
| Tell | Fix |
|---|---|
| Gradient on header, buttons and chart fills | One flat accent, only on the primary action |
| Coloured icon tiles next to every metric | Remove them; the number is the hero |
| Four equal cards | One primary metric, larger, three secondary |
| Heavy shadow on every panel | Shadows only on what floats (menus, popovers) |
| "Welcome back, Name 👋" and identical "+12.5%" badges | Title the page by what it shows; each number gets a real delta, unit and comparison, or a sparkline |

### CON-7 · The engineered look (crisp products) (P2)
**Applies to.** dense tools on the crisp motion profile: issue lists, inboxes, admin lists and tables, sidebars, panels.
**Rule.** Five decisions make a tool read as engineered. Density: about 13 px text (0.8125rem), 32 px list rows and -0.01em tracking on small UI text, for pointer-driven desktop only; touch layouts keep 44 px rows, and a density setting beats forcing compact on everyone. Borders, not shadows: three stacked surface values (canvas, list, hover) and a 1 px hairline at about 8% foreground alpha; rows, panels and sidebar carry no shadow, and row hover moves to the next surface step instead of lifting. One accent, only on the selected row and the primary action; status and priority are neutral icons that differ in shape and carry an accessible name, not coloured pills. Keyboard: a visible shortcut on every frequent action (CON-10), hover feedback about 80 ms, transitions at most 150 ms, no overshoot (MOT-0). Alignment: a 4 px grid, 16 px icons centred on the text line, labels left, numbers and dates right in tabular figures (DAT-1), nothing centred in rows. The hairline and surface step are decoration only: a focused row still gets a 3:1 focus ring (INT-1), and selection never relies on the surface step alone.
**Detect.** `box-shadow` on rows, panels or sidebars; coloured status pills; the accent spread over links, labels and badges; 300 ms or springy transitions; centred cells; letter spacing in px; compact rows kept at touch breakpoints.

### CON-8 · Honest persuasion only (P0)
**Applies to.** pricing, plans, upsells, social proof, progress meters.
**Rule.** These are allowed only when the claims are true:
- **Anchoring**: show a real reference price (the actual previous or regular price, or the monthly price beside the yearly one).
- **Highlighting a plan**: isolate one tier (scale, elevation, a "Most popular" badge) only if it is actually the most chosen or the recommended fit.
- **Decoy pricing**: a middle option that makes the comparison clear is fine; an option that exists only to trick is not.
- **Loss framing** ("Save $240 a year") must use real numbers.
- **Progress pull** (Zeigarnik): an unfinished checklist or completion meter is fine when it leads to an outcome the user wants (CON-11); never fake progress, invent unchecked items or withhold completion.
Social proof numbers must be real and current. If a claim cannot be verified from the codebase or the user, use a placeholder and flag it in the report.
**Detect.** Hard-coded "+2,847 chose Pro this month", invented strike-through prices, "Most popular" on the most expensive plan without data.

### CON-9 · Never build dark patterns (P0)
**Applies to.** pricing, checkout, sign-up, cancellation, consent, feeds, notifications (always check these flows).
**Rule.** Refuse to add, and flag when found: hidden costs revealed only at the last step (show the full price including fees early); pre-checked upsells and opt-ins; confirmshaming ("No thanks, I don't like saving money"); fake scarcity or countdowns that reset; roach motels (easy to sign up, hard to cancel; cancellation must be as easy as signup); disguised ads; nagging that cannot be permanently dismissed; anxiety loops (manufactured urgency, streak guilt) and infinite feeds with no stopping point in products where that harms the user (offer natural stopping points and keep the footer reachable). If the user insists on a pattern that is deceptive, say so plainly and do not implement it.
**Detect.** Fees added in the final checkout step; `checked` default on marketing consent; cancel flows longer than signup; timers stored only client-side that restart on reload.

### CON-10 · Keyboard shortcuts are shown and safe (P1; P0 when single-key shortcuts fire while typing)
**Applies to.** keyboard shortcuts on buttons, menu items, tooltips and command palettes.
**Rule.** Print the shortcut beside every action that has one (on the button, in menus, tooltips and the command palette, DAT-12) so the fast path is taught in place, with Cmd/Ctrl+K opening the palette. Render keys with `<kbd>`, show the platform's modifier (⌘ on macOS, Ctrl elsewhere) and expose it with `aria-keyshortcuts`. Single-character shortcuts (C to create, P for priority) never fire while focus is in a text field, and can be turned off or remapped, or work only while their component has focus (WCAG 2.1.4).
**Detect.** `keydown` handlers matching bare letters without checking whether `event.target` is an input, textarea, select or `contenteditable`; shortcuts that exist in code but appear nowhere in the UI; a hard-coded ⌘ shown on every platform.
**Fix.** Return early when `event.target.closest('input, textarea, select, [contenteditable]')`; list shortcuts in settings with an off switch.

### CON-11 · Progress checklists serve goals the user chose (P1)
**Applies to.** onboarding checklists, setup guides, profile-completion meters, course progress bars.
**Rule.** Visible remaining steps pull people back only toward an outcome they want (finishing setup, a course, a profile they want to be found by); progress on a chore, such as a read meter on a marketing email, is noise. Show the real remaining items and pair the meter with one specific next action and its benefit ("Add 3 more skills to get recommendations"), linking straight to that step. Tick items off when the user does the task anywhere in the app, keep the state on the server so it follows them across devices, let them reach 100% and see a done state, and let them hide the checklist. Reminders are opt-in and rate-limited. Show progress as text ("3 of 5 done") and as a native `<progress>` or `role="progressbar"` with values and a label; done items carry a tick and text, never colour alone.
**Detect.** Meters with no next action; items still unchecked after the task was done elsewhere; checklists that cannot be dismissed or completed; checklist state only in `localStorage`; repeated "one step from 100%" notifications.

---
Sources: microcopy, landing-page-skeleton, de-ai-landing-hero, de-ai-dashboard, reverse-engineered-linear, serial-position, peak-end-rule, zeigarnik-effect, pricing-psychology, decoy-effect, von-restorff, and the account's dark-pattern series (hidden costs, manipulation, infinite scroll, anxiety). See `sources.md`.
