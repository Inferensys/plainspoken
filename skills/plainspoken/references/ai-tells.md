# Generic and AI-sounding copy: what to look for and what to do instead

Buyers increasingly complain that vendor content is "too generic". In Demand Gen Report's 2024 survey, 51% said so, up from 38% the year before. A 2024 WSU study found that the bare term "AI" in a product description lowered trust and purchase intent, most of all for high-risk purchases. The patterns below are why. Most of them come from Wikipedia's "Signs of AI writing" (WikiProject AI Cleanup) and the humanizer skill. The rest come from reviewing landing copy.

**Why AI text sounds this way.** A model picks the choice that fits the widest range of readers. A human writer picks for one reader and one subject. Every pattern below is a default choice made where a specific one was needed. So the fix is almost never a synonym. It is usually a fact, or a cut.

## Contents
1. The master test
2. Presumptive intensifiers and redundant qualifiers ("real", "already", "existing")
3. Antagonistic and us-vs-them framing
3b. Clever compression: lines that need a second read
4. Staging instead of stating
5. Rhythm by rule
6. Inflation and borrowed authority
7. Formatting by rule
8. Leftovers from chat and drafting
9. Landing-page-specific tells
10. When not to act
11. Process to de-generic a draft

---

## 1. The master test

> Could a competitor put this sentence on their site unchanged?

If yes, the sentence needs a fact only this client has: a number, a name, a term, a trade-off or an exclusion. If there is no such fact, cut the sentence or leave a placeholder.

A second test applies to every sentence you keep: does it add something the reader didn't already have from the line before it?

## 2. Presumptive intensifiers and redundant qualifiers

**Watch for:**
- real, real users, real-world, real business, real work, real results
- actually, already, truly, genuinely, simply, just (as emphasis), literally, finally, proper
- the right next step, the right solution, a next step you can act on, what matters, things that matter

**Problem.** These words imply that the reader's current situation is fake, lesser or misguided. "Works for real users" implies the reader's users aren't real. "The tools you already run" turns a neutral fact into a reassurance nobody asked for. "A next step you can act on" implies other next steps are useless. Models add them to sound grounded, and they read as a sales tic. The sentence almost always says the same thing without the word.

| Before | After |
|---|---|
| Answers well in the demo and badly for real users. | Answers well in the demo and badly in production. |
| Built on the models and tools you already run. | Works with OpenAI, Anthropic, open models, Postgres and Pinecone. (List what's true.) |
| Routing based on how the system is actually used. | Routing based on usage logs. |
| You leave with a next step you can act on. | You leave with a written next step. (Only if true.) |
| Who actually does the work? | Who does the work? |

**Redundant qualifiers** are the same habit pointed the other way. The word states something the reader can't avoid knowing: "your product's existing screens" (a product only has existing screens), "your current stack", "your own data", "the actual system", "end users", "live production". Delete the word. If the sentence still feels like it's missing something, the gap is a fact, not a qualifier.

| Before | After |
|---|---|
| Built into your product's existing screens. | Built into your product. |
| Works with your current stack. | Works with OpenAI, Postgres and Pinecone. (Name it.) |
| Search over your own internal data. | Search over your docs, tickets and wiki. |

Keep "real" or "actually" only when it's literal: "real-time", "real estate", or correcting a stated misconception ("The bottleneck is actually retrieval, not the model").

## 3. Antagonistic and us-vs-them framing
3b. Clever compression: lines that need a second read

**Watch for:**
- unlike other agencies, most vendors, other consultancies
- no fluff, no BS, no hype, no buzzwords, no jargon
- "slop", body shop, butts in seats
- tired of…?, stop wasting…, forget everything you know
- we're not like…, we don't do X (as a pose rather than a scope statement)
- "the model is the easy part", "AI is more than LLMs" and other dunks on how the reader currently thinks

**Problem.** It picks a fight the reader didn't start. It implies the reader made bad choices (hired the wrong agency, believed the hype), and the writer gets credit for being contrarian without saying anything specific. Models reach for this to sound confident and opinionated. Buyers read it as insecurity, or as being lectured. It also contradicts itself: "no buzzwords" is a buzzword.

**Do instead:**
- **State scope as plain fact.** "We work alongside your engineers" beats "We're not a body shop." "We take projects from $X" beats "We don't do small stuff."
- **Name alternatives neutrally.** If the comparison helps the reader, describe the trade-off fairly: "Hiring in-house takes longer to start and keeps the knowledge inside. We start in [N] weeks and hand over the code and evals."
- **Hold opinions as positions, not dunks.** "We set up evals before the first feature" is an opinion. "Most teams get evals wrong" is a dunk.
- **Say exclusions calmly.** "Not a fit if you need staff augmentation or an RFP response" is useful. Swagger isn't.

## 3b. Clever compression: lines that need a second read

**Watch for:** lines that squeeze a process into a twist of phrasing so the reader has to decode it.
- "You leave knowing what we'd build first."
- "Evals before features."
- "From demo to dependable."
- "Built for the day after launch."
- Nouns used as verbs, chained possessives, a sentence whose subject is buried at the end.

**Problem:** Models compress to sound punchy and senior. On a landing page, anything the reader has to parse twice gets skimmed instead. The reader also can't tell what happens next, which is the one thing a CTA section has to make clear.

**Test:** could a non-native English speaker, skimming, say back what happens? If not, write what literally happens, in order, with a plain subject and verb.

| Before | After |
|---|---|
| You leave knowing what we'd build first. | At the end of the call, we tell you what we would build first. |
| Evals before features. | We set up tests for answer quality before we add features. |
| From demo to dependable. | We take your prototype to production. |

A short, punchy line is fine when it's also instantly clear. "Read our code before you hire us" works because there's nothing to decode.

## 4. Staging instead of stating

These are the strongest tells. Act on a single sighting.

**4.1 Not X but Y.** This covers "not just X, but Y", "it's not X, it's Y", "X rather than Y", the split form ("This doesn't mean X. It means Y.") and the clipped tail (", no guessing"). The negative half names something nobody claimed, so the positive half sounds bigger. State the point directly. Keep a contrast only when it corrects a belief the reader actually holds, or when both halves carry information.
- Before: "This isn't just tooling, it's a managed service."
- After: "We build it, then run it after launch."

**4.2 One-line closers and dramatic fragments.** "That's the difference." "Simple as that." "Read that again." A row of fragments: "No drama. No delays. No surprises." Cut the closer. Merge the fragments into one sentence with a specific claim.

**4.3 Sayings that sound deep.** "The real question is…", "At its core…", "In reality…", "X is the language of Y", "X becomes a trap". Replace each with the specific claim.

**4.4 Staged run-ups.** "Here's the thing:", "Let's be honest.", "Honestly?", "Look,", "Here's what you need to know." Delete the run-up and make the point.

**4.5 Arguing with no one.** "To be clear…", "Don't get me wrong…", "This isn't about…", "You might think… but…". The copy rebuts an objection nobody raised. Delete the rebuttal. If it hid a real claim, state the claim.

**4.6 Rhetorical-question hooks.** "Sound familiar?", "Ready to ship?", "Reading about X because you have to build it?", `{Topic}?` headline templates. State the situation instead: "Your prototype answers well in demos and fails in production."

## 5. Rhythm by rule

**5.1 Forced triads.** Lists of three that exist because three sounds complete: "Faster, smarter, safer." Check that each item is distinct and true. Use the one that's provable, or vary the structure. Keep three when there really are three.

**5.2 Repeated openings.** Several sentences or bullets in a row starting with "We…" or "You…". Merge them, change the subject, or lead with the action. Readers skip list items that start the same way.

**5.3 Dashes as the universal connector.** Em and en dashes, and " -- ", used where a comma, colon, period or parentheses would do. One is fine. A page full of them is a tell. Match the client's samples if they use dashes.

**5.4 Stacked qualifiers.** "could potentially", "might arguably", "in some cases it may". Keep one qualifier where it's needed, or none.

**5.5 Uniform sentence length.** Every sentence 10–14 words long. Mix short and long.

**5.6 Same-shaped sections.** Every section is eyebrow + claim + three cards + "Read more". Vary the structure to fit the content.

## 6. Inflation and borrowed authority

**6.1 Overused AI words.** additionally, align with, bolster, crucial, deep dive, delve, enduring, enhance, garner, highlight (verb), interplay, intricate, key (adjective), landscape, meticulous, pivotal, quietly, robust (figurative), showcase, tapestry, testament, underscore, valuable, vibrant.

**6.2 Stock marketing words.** seamless, unlock, elevate, empower, leverage, harness, supercharge, streamline, revolutionize, cutting-edge, next-gen, state-of-the-art, world-class, best-in-class, innovative, tailored, bespoke, holistic, solutions, synergy, journey, ecosystem, "AI-powered" with no mechanism, "drive results", "trusted partner", "in today's fast-paced world".

**6.3 Inflated significance.** critical, immense, absolute, game-changing, nightmare, "plays a key role", "marks a pivotal moment", "the future looks bright". Keep the fact and drop the significance. End on the last concrete fact.

**6.4 Vague association.** "associated with", "connected to", "tied to". Name the actual relationship: built, maintains, partnered under contract X. If you don't know it, ask.

**6.5 Shallow -ing riders.** "…, ensuring reliability", "…, enabling teams to…", "…, fostering trust". Delete the rider, or turn it into its own sentence with the evidence behind it.

**6.6 Sales language.** rich, profound, renowned, featuring, "diverse array", stunning, "in the heart of". State what the thing is.

**6.7 Borrowed authority.** "Experts agree", "industry reports show", "trusted by leading companies" with no names. Cite the named source, or cut the claim.

**6.8 Dodging is/are/has.** "serves as", "stands as", "functions as", "boasts", "features". Write "is" or "has".

## 7. Formatting by rule

- **Title Case Headings.** Use sentence case. Check the CSS too: `text-transform: capitalize` forces Title Case even when the copy is written correctly.
- **Bold on every list label** ("**Speed:** …"). Remove it, or turn the list into prose when the labels add nothing.
- **Emoji, arrows and horizontal rules** used as decoration.
- **Eyebrows that repeat the H2** or the page topic in capitals.
- **Curly quotes** where the codebase uses straight ones. This is a weak signal on its own.
- **Hyphenated compounds after the noun** ("the report is high-quality"). Drop the hyphen there. Keep it before the noun ("a high-quality report"). Weak on its own.

## 8. Leftovers from chat and drafting

- **Chatbot residue:** "Great question!", "I hope this helps", "Let me know if…", "Here is a…". Remove it.
- **Knowledge-limit hedges:** "based on available information", "while details are limited". Remove them, or ask for the fact.
- **The heading restated in the first sentence** ("## Speed / Speed matters."). Delete the restatement.
- **Copy about the page itself:** "The table below compares…", "This section explains…". Delete it unless the reader couldn't otherwise tell.

## 9. Landing-page-specific tells

- Round, unsourced percentages ("cuts costs by 60%"), and certifications or uptime figures nobody supplied.
- Stat tiles with no baseline, and "Over 1,000+".
- Five or more different CTA labels on one page. "Free consultation".
- Industry rotators or lists ("AI for Healthcare / Finance / Retail") with no work in those industries behind them.
- "Partnered with" next to vendor logos, when the relationship is really "we use their API".
- Typos in a section about quality. NN/g lists typos as a top trust-killer.
- Fake casualness added to "sound human": slang, winks, forced jokes. Human copy sounds like a specific person with specific knowledge. Add specifics, not attitude.

## 10. When not to act

- Leave a watched word alone when it's literal or technical: real-time, robust estimator, end-to-end encryption, critical path.
- Leave it alone inside a quotation, a proper name, or the client's own tagline (flag that one instead).
- If the client supplies a voice sample, match it, including its dashes and humour.
- One tell alone is weak evidence. Several together are the signal.

## 11. Process to de-generic a draft

1. Run `scripts/lint_copy.py` and work through every flag. Treat its flags as prompts to look at a line, not as automatic fixes.
2. Highlight every sentence that fails the master test. Rewrite it around a fact from the inventory, or cut it, or leave a placeholder.
3. Re-read for the patterns the linter can't catch:
   - not-X-but-Y split across two sentences
   - dunks on the reader's current approach
   - triads
   - repeated openings
   - closers that restate the paragraph
4. Read it aloud as if to the client's CTO over coffee (Peep Laja's conversation test). Rewrite anything you wouldn't say out loud.
5. Check that the rewrite didn't add or drop a fact, number, name or claim. An unsupported addition is an error.
