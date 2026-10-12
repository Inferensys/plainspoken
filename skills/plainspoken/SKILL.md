---
name: plainspoken
description: Write, rewrite, or critique conversion copy for homepages and landing pages (hero headline, subhead, section headings, proof, CTAs, FAQ, form microcopy), especially for B2B services firms, agencies, consultancies, and technical products sold to expert buyers. Use this whenever the user asks for website copy, a homepage or landing page rewrite, a value proposition, hero or headline options, CTA labels, "make this page convert", "our copy sounds generic / AI-written", or positioning that has to end up as page copy, even if they never say "copywriting". Not for blog articles, emails, ads, or social posts.
---

# Plainspoken: landing page copy

Good landing copy does four things for the right visitor. In about five seconds they see their own situation named. They believe the main claim because proof sits right next to it. They can tell why this beats the alternative they were considering. And they know exactly what the next step costs them: time, people, money, risk.

This skill turns research and facts into that copy. It does not polish weak copy into nicer-sounding weak copy.

## The one idea everything else depends on

**Specific facts persuade. Phrasing on its own does not.**

The most common failure, and the one that makes copy read as AI-written, is a writer with no facts covering the gap with tone. You get clever reframes, rhetorical questions and warm reassurance, and none of it says anything the reader can check. A buyer has seen thousands of these lines and skips them.

Every line that matters should carry something the reader can picture or check. That might be:
- a number with a unit and a baseline ("2 hrs → 3 min per workflow")
- a named client or person
- a contract term ("you pay against shipped milestones")
- a duration ("45 minutes with our founders")
- a stack name
- a price or range
- a stated trade-off or exclusion ("not for RFP processes")

When the fact is missing, never invent one, and never paper over the gap with style. Put in a visible placeholder such as `[RESULT: metric, before → after, timeframe, client]` and list it under "Facts needed". A page full of honest placeholders is a better deliverable than a page of confident filler, because the user can fill the gaps. Fabricated stats and certifications also hurt trust and create legal risk.

## Workflow

### 1. Collect the raw material first

Read everything the user can give you before drafting:
- the existing page
- case studies, pricing or engagement terms, the process page, team bios
- sales-call notes, customer reviews or quotes
- competitor pages

If you can browse, pull the competitor pages yourself.

Then build a **fact inventory**: a list of every concrete, usable fact, each with its source. Proof is usually the thinnest part. When it is, ask the user targeted questions such as:
- Which client result can we name?
- What is a typical engagement length and price range?
- Who takes the first call?
- What do you refuse to do?

Ask before writing. Do not draft around the gaps.

When the user wants a draft anyway, write it with placeholders and say plainly which claims are unsupported.

### 2. Write a short positioning brief

Positioning has to be settled before messaging, otherwise the copy claims value that any vendor could claim. Fill in the brief from `references/positioning-brief.md`. It covers:
- the real alternatives, including "do nothing", "hire in-house" and "buy a SaaS tool"
- unique attributes, and the value each one creates
- the best-fit buyer, and who the page is **not** for
- the market insight the buyer must accept
- one single-minded proposition

Also set the reader's **awareness stage** (Schwartz), because it decides how long the page should be and what it opens with. A most-aware visitor needs the offer and the terms. A problem-aware visitor needs their pain reflected back accurately before any pitch.

If the positioning is unclear or contested, show the brief to the user before drafting. A five-minute correction here saves a full rewrite later.

### 3. Wireframe with headings only

Lay out the message hierarchy as section headings. The order buyers need is:
1. What is it?
2. Is it for me?
3. What do I get?
4. Why you over the alternative?
5. Proof
6. Risk
7. Next step

Read the headings alone, top to bottom. Most visitors only scan headings, so the headings by themselves should make the page's argument. If they read like labels ("Our Approach", "Why Choose Us", "Key Features"), rewrite them as claims before writing any body copy.

### 4. Draft every element

Follow the element rules below. `references/elements.md` has fuller guidance and before/after examples from real sites.

### 5. Edit in passes

A rough first draft is fine. Then run these passes in order:
- **Clarity:** could a smart outsider explain the offer back to you?
- **Voice:** does it sound like the best person at the firm talking to a peer?
- **So what:** does each claim connect to something the reader wants?
- **Prove it:** is proof next to every claim?
- **Specificity:** have you swapped every abstraction for a fact?
- **Emotion:** is the reader's real fear or frustration named, plainly?
- **Zero risk:** have you answered the objections at the moment they come up, near the CTA?

Then cut about a third, run `scripts/lint_copy.py` on the draft, and fix what it flags. Finally, read the copy as if it were going out to the client's CTO under your own name.

### 6. Deliver in the output format below

## Element rules

**Hero headline.**
- Say what it is or what it gets the reader, in words the buyer would use themselves.
- If the offer is unique, state it plainly. If it isn't, lead with the sharpest outcome, the biggest objection handled, or a clear niche.
- Run Harry Dry's three tests: Can the reader picture it? Could it be proven false? Could a competitor say it word for word? The third answer should be no.
- Write with conviction. "We help companies…" is weak.
- Avoid stacked abstract nouns ("Intelligent Analysis, Decision & Execution"), category-plus-buzzword lines ("Your go-to AI partner"), and puns that only work if the reader already knows you.

**Subhead.** One or two sentences on *how* the headline is true: the mechanism, the scope, and one credibility anchor. This is where insider vocabulary belongs. Used correctly, it signals that the writer is a peer.

**"Is it for me" section.** Name three or four *situations* the reader would recognise, not industries. Weak: "for startups and enterprises". Strong: "You have an AI team, and delivery is stuck." Say who the page is not for. Turning some readers away makes the rest of the page more believable.

**Section headings.** Each heading is a claim or a conclusion, and its first two words carry the meaning. Use sentence case.

**Body copy.**
- One idea per paragraph, and the key point in the first two sentences.
- Short sentences in plain words, but keep precise technical nouns: experts trust their own vocabulary.
- Show scenes and numbers instead of adjectives.
- Mention table-stakes items (security, support, integrations) briefly, and give the space to what's different.

**Proof.** Put it beside the claim it supports, not saved for a testimonials block. The strongest forms, roughly in order:
1. A named client with a before → after result, timeframe and scope
2. A quote with the person's name and title
3. Commercial terms (pricing, milestone billing, guarantees, IP ownership)
4. Public work (open source, benchmarks, published methods)
5. The named people who do the work
6. Logos (weak without outcomes)

See `references/proof-and-ctas.md`.

**CTAs.**
- Use one primary action with one consistent label across the page, plus at most one lower-commitment secondary.
- The label names what happens next ("Book 30 minutes with an engineer", "See pricing", "Read the triage case study").
- Put the risk-reducing detail right next to the button: how long, with whom, what you leave with, NDA, no prep needed.
- Avoid "Free consultation", "Get started" on a services firm, a bare "Learn more", and exclamation marks.
- Match the CTA to the reader's intent using the ladder in `references/proof-and-ctas.md`.

**FAQ.** Use real objections in the buyer's words: price, IP and code ownership, data and security, who does the work, timeline, what happens if it fails, handoff. Answer in the first sentence, then explain.

**Forms and microcopy.**
- Ask only what you'll use, and say why you need anything unusual.
- Say what happens after submit, and when.
- Placeholder text can model a good answer.
- Confirmation and error messages should sound like a person wrote them.

## Voice

Picture the most senior, most likeable person at the firm, explaining the offer to a peer they respect. That gives you plain verbs ("is", "costs", "ships"), precise nouns, a mix of short and long sentences, and direct "you" and "we".

Personality comes from substance:
- an opinion the reader could disagree with, stated as your position rather than a dig at theirs
- an honest trade-off
- a named alternative, described fairly
- a sharp, specific detail

Two habits sound confident but read as AI and put buyers off:

- **Presumptive intensifiers.** "Works for real users", "the tools you already run", "how it's actually used", "a next step you can act on". Each implies the reader's current situation is fake or lesser. Delete the word, and the sentence still says the same thing.
- **Redundant qualifiers.** "Your product's existing screens", "your current stack", "your own data". The word states the obvious. Cut it, or replace it with the specific thing.
- **Clever compression.** "You leave knowing what we'd build first." If a line needs a second read, rewrite it as what literally happens: "At the end of the call, we tell you what we would build first." Plain beats clever on a landing page.
- **Antagonism.** "Unlike other agencies", "no fluff", "slop", "the model is the easy part". These dunk on the reader's past choices or current thinking. State your scope and method as plain fact instead.

Personality also does not come from rhetorical questions, slang, forced jokes, or `{Topic}?` headline templates. Those are what a model adds when it's trying to sound human, and readers recognise them for exactly that. Wit is welcome in the body, but only after the line is clear.

Aim for a reading level around 8th grade in prose sentences, but never at the cost of the right technical term. Unbounce's data shows simpler pages converting at roughly twice the rate. NN/g found plain, objective, scannable text far more usable than promotional writing.

If the user supplies a brand voice guide or writing samples, follow those over these defaults.

## What reads as generic or AI-written

Read `references/ai-tells.md` before your editing passes. The short version:
- copy that would still be true on a competitor's site
- presumptive intensifiers and redundant qualifiers: real, actually, already, truly, simply, existing, current, "your own", "the right next step"
- clever compression: any line the reader has to decode ("Evals before features", "You leave knowing what we'd build first")
- antagonistic or us-vs-them framing: "unlike other agencies", "no fluff", digs at how the reader works now
- "Not just X, it's Y" contrasts
- reflexive lists of three
- one-line dramatic closers
- dashes everywhere
- stock words (seamless, robust, unlock, elevate, empower, cutting-edge, leverage, solutions)
- Title Case headings
- stat tiles with no baseline
- seven different CTA labels
- "AI-powered" with no mechanism behind it

The lint script catches the mechanical ones. Only you can catch "a competitor could say this".

## Output format

For a new page or a rewrite, return:

```
## Brief
Reader & situation · Awareness stage · Alternatives they're weighing ·
Single-minded proposition · Not for · Page's one job · Primary CTA

## Copy
### [Section name, e.g. Hero]
Headline: …
Subhead: …
CTA (primary): … | CTA (secondary): … | Next to CTA: …
(Repeat per section, in page order. Give 2-3 headline options for the hero
with one line each on the angle; recommend one.)

## Facts needed
Every placeholder used, with the exact question to ask the client.

## Notes
Anything structural (section order, cutting a section, where proof should
move) and any claim you softened or removed and why.
```

For a **critique** of existing copy, go element by element. Quote the current line, name the specific problem in a few words (for example "no proof", "competitor could say it", "label not claim", "salesy CTA"), say which fact would fix it, then give the rewrite or a placeholder. Rank the problems by impact on conversion, and put the hero and CTAs first.

## Reference files

- `references/positioning-brief.md`: voice-of-customer mining, Dunford positioning, awareness stages and page length, the brief template. Read it at step 2.
- `references/elements.md`: per-element guidance with real before/after examples. Read it while drafting.
- `references/proof-and-ctas.md`: proof formats, risk reversal for services, the CTA intent ladder, CTA label do/don't. Read it for proof, CTAs and any page with low-intent traffic.
- `references/ai-tells.md`: the full catalogue of generic/AI patterns and how to replace each one. It covers presumptive intensifiers, antagonism, and the humanizer patterns: staging, rhythm, inflation, formatting and chat leftovers. Read it before the edit passes.
- `references/sources.md`: the experts and studies behind these rules, with links, for when the user asks why.
- `scripts/lint_copy.py`: run `python3 scripts/lint_copy.py <file>` (or pipe text on stdin). It flags stock and AI words, presumptive intensifiers, antagonistic phrases, contrast formulas, run-ups, closers, -ing riders, dashes, exclamation marks, Title Case headings, inconsistent CTA labels, sentence-rhythm uniformity, and reading grade. Treat its output as hints, not verdicts.
