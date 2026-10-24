# Content, flow psychology and the "AI look"

Words, page structure, the psychology of flows, and the tells that make an interface look machine-generated. Persuasion rules come with honesty limits: the skill never builds dark patterns.

Severity: **P0** deceptive or harmful, **P1** confusing or generic, **P2** polish.

---

### CON-1 · Microcopy is interface (P1)
**Rule.** Buttons name the reward or result ("Create my free account", "Send 3 invoices"), never "Submit". Errors become next steps ("That email is already registered. Log in instead?"). Empty states give the first action (STA-6). Labels stay visible (FRM-2). Write like a helpful colleague: plain words, "you", no system jargon ("operation failed", "invalid input", "null"). Keep one voice across the product. Destructive confirmations repeat the verb and the object.
**Detect.** "Submit", "OK", "Click here", "Error occurred", "Invalid", "No data"; mixed tone; shouting capitals in body copy.

### CON-2 · Landing pages follow one skeleton (P1)
**Rule.** Hero → Proof → Problem → Solution → CTA. The hero answers what it is, who it is for and why it matters within about three seconds: one concrete headline, one subline naming the audience, one primary CTA. Proof sits directly under the hero (one specific testimonial with name, role and a measurable result; logos people recognise; one real number). Name the problem's real cost before the cure. The solution is at most three outcomes, not features. The final CTA repeats the hero CTA exactly.
**Detect.** Features before any proof; six-plus benefit cards; different CTA labels top and bottom.

### CON-3 · Remove the generated-hero tells (P1)
**Rule.** A generated page decorates because it has nothing concrete to show. Swap every decoration for the product itself:
| Tell | Fix |
|---|---|
| Gradient headline full of adjectives ("Supercharge your workflow") | Plain headline naming the outcome; subline naming the audience |
| Big blurry colour blob behind everything | Neutral background; the only colour on the product shot and one primary button |
| Two equal buttons side by side ("Get started" / "Learn more") | One primary button; the second becomes a text link with an arrow |
| "Trusted by 10,000+ users" over grey anonymous logos | One verifiable quote with name, role and a result with a unit |
| Three icon-in-a-circle cards with one word each (Fast, Secure, Easy) | One real product screenshot with three annotations pointing at real UI |
**Detect.** Search the copy for "supercharge", "seamless", "unlock", "revolutionize", "powerful", "next-gen", "all-in-one"; gradient-clipped headings; equal-weight CTA pairs; generic feature-card grids.

### CON-4 · Order is a decision (P2)
**Rule.** People remember the first and last items of a sequence and forget the middle. Put the most important item first and the strongest proof or CTA last: logo first and primary CTA last in a nav bar, strongest promise first and strongest proof last on a landing page, the hook first and the payoff last in onboarding.

### CON-5 · Design the peak and the end (P1)
**Rule.** People judge a flow by its most intense moment and its last moment. Plant one deliberate positive peak (a moment of delight, a useful surprise) and make the final screen warm, specific and useful (what happened, what is next). Never let a flow end on friction: a confusing confirmation, an error, an upsell wall.
**Detect.** Flows ending on a bare "Success" or a redirect with no context; checkout and onboarding ending in a modal upsell.

### CON-6 · Remove the generated-dashboard tells (P1)
**Rule.** Same principle as CON-3: decoration replaces content.
| Tell | Fix |
|---|---|
| Gradient on header, buttons and chart fills | One flat accent, only on the primary action |
| Coloured icon tiles next to every metric | Remove them; the number is the hero |
| Four equal cards | One primary metric, larger, three secondary |
| Heavy shadow on every panel | Shadows only on what floats (menus, popovers) |
| "Welcome back, Name 👋" and identical "+12.5%" badges | Title the page by what it shows; each number gets a real delta, unit and comparison, or a sparkline |

### CON-7 · The engineered look (crisp products) (P2)
**Rule.** For tools and dense apps, five decisions make a product read as engineered: dense text on a fixed row rhythm (about 13 px text, 32 px rows); depth from stacked surface values and hairline borders instead of shadows; one brand colour used only on selection and the primary action, everything else neutral, status as neutral icons rather than coloured pills; a keyboard shortcut on every frequent action, shown in menus and tooltips, with hover feedback near 80 ms and no bounce; a 4 px grid with labels left, numbers right, icons on the text line, nothing centred.

### CON-8 · Honest persuasion only (P0)
**Rule.** These are allowed only when the claims are true:
- **Anchoring**: show a real reference price (the actual previous or regular price, or the monthly price beside the yearly one).
- **Highlighting a plan**: isolate one tier (scale, elevation, a "Most popular" badge) only if it is actually the most chosen or the recommended fit.
- **Decoy pricing**: a middle option that makes the comparison clear is fine; an option that exists only to trick is not.
- **Loss framing** ("Save $240 a year") must use real numbers.
- **Progress pull** (Zeigarnik): an unfinished checklist or completion meter is fine when it leads to an outcome the user wants; never fake progress.
Social proof numbers must be real and current. If a claim cannot be verified from the codebase or the user, use a placeholder and flag it in the report.
**Detect.** Hard-coded "+2,847 chose Pro this month", invented strike-through prices, "Most popular" on the most expensive plan without data.

### CON-9 · Never build dark patterns (P0)
**Rule.** Refuse to add, and flag when found: hidden costs revealed only at the last step (show the full price including fees early); pre-checked upsells and opt-ins; confirmshaming ("No thanks, I don't like saving money"); fake scarcity or countdowns that reset; roach motels (easy to sign up, hard to cancel; cancellation must be as easy as signup); disguised ads; nagging that cannot be permanently dismissed; anxiety loops (manufactured urgency, streak guilt) and infinite feeds with no stopping point in products where that harms the user (offer natural stopping points and keep the footer reachable). If the user insists on a pattern that is deceptive, say so plainly and do not implement it.
**Detect.** Fees added in the final checkout step; `checked` default on marketing consent; cancel flows longer than signup; timers stored only client-side that restart on reload.

---
Sources: microcopy, landing-page-skeleton, de-ai-landing-hero, de-ai-dashboard, reverse-engineered-linear, serial-position, peak-end-rule, zeigarnik-effect, pricing-psychology, decoy-effect, von-restorff, and the account's dark-pattern series (hidden costs, manipulation, infinite scroll, anxiety). See `sources.md`.
