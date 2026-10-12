# SEO pages: service, comparison, glossary, guide, integration, and programmatic templates

Read this when the page is meant to be found through search, or when you're writing a template or LLM generation prompt that will produce many pages. Everything in SKILL.md still applies: facts first, proof beside claims, no AI tells. This file adds what search changes.

Sources are in `sources.md` (SEO section). Figures marked † come from vendor studies, paywalled posts or single teardowns. Treat them as directional.

## Contents
1. The rule that sits above all the others
2. Before writing: read the results page
3. Playbooks by page type
4. Element rules
5. Writing to be cited by AI answers
6. Programmatic pages and generation prompts
7. What big domains get away with that you can't
8. Pre-publish checklist

---

## 1. The rule that sits above all the others

**A page should exist only if it has something that no other page on the web or on this site has.**

Google's spam policy calls this "scaled content abuse": many pages made mainly to rank, however they were produced. Its rater guidelines rate such pages Lowest "no matter how they are created". In September 2026 Google's John Mueller said a site generating pages from combinations of attributes can make Google lose faith in the whole site, and that recovery takes significant time. Lily Ray tracked 220+ sites built with AI content platforms. 54% lost at least 30% of their peak traffic, usually 6–18 months after a publishing burst.† The page types most at risk when scaled are:
- "X vs Y" pages
- "What is X" glossaries
- "Best X for Y" listicles, especially self-promotional ones
- competitor-alternative pages
- location or language variants
- FAQ farms (one question per URL)

AI use per page is not the problem. Ahrefs found near-zero correlation between AI use and rankings across 600k pages.† Volume without value is the problem, and it gets judged at the level of the whole site. A weak programmatic section can pull down the homepage and service pages with it.

## 2. Before writing: read the results page

Search the target query, and a few variants, before drafting. Write down:

- **The page type that ranks.** Match it. Examples:
  - "What is X" queries rank definitions.
  - "X development company" queries mostly rank comparison listicles, not service pages.
  - "How much does X cost" queries rank cost guides, which services firms win.
  - "X vs Y" queries rank decision pages.
- **The sub-questions** in "People also ask", related searches, and the H2s of the top 5 results. AI answers fan a query out into related sub-searches, so answering the adjacent questions matters.
- **The gap.** Find what every top result misses: a decision rule, real costs, failure modes, code, a first-hand result. Put it in the brief. A page that only collates the top 10 adds nothing (Animalz's "copycat content").
- **The intent rung.** Learning, evaluating or buying. This sets the CTA (see `proof-and-ctas.md`).

## 3. Playbooks by page type

| Page type | Open with | Must contain | Unique per page | CTA |
|---|---|---|---|---|
| **Service** ("RAG development services") | What you build, for whom, and how, in one or two sentences. The second block shows domain knowledge: where these systems usually fail | Scope, typical architecture, stack, timeline, cost band, named or anonymised results, "when this is the wrong approach", buyer FAQ | Failure modes, cost band, results, stack | Booking near the top and at the end |
| **Comparison** ("X vs Y") | The one-line difference | A criteria table (cost, latency, effort, freshness, failure modes), "choose X when / choose Y when", a small code sample in each where relevant, the version and date checked | Hands-on findings, the verdict | Contextual: case study or short call, after the verdict |
| **Glossary / "what is"** | "X is a [category] that [mechanism] so that [outcome]." Make that the meta description too | One example or diagram of the mechanism, a common mistake, how it's used in production, 3–5 related terms, a link to the service | The production note and the example | Soft: related guide or resource. No booking button above the answer |
| **Guide / how-to** | The answer or end state, then who it's for | Steps with real commands or config, pitfalls, how to verify it worked | Code, gotchas, measurements | Resource or "see how we built this" case study |
| **Cost guide** | The price range | A table of real project bands (scope → cost → timeline), what moves the price, a method note | Your project data | Scoping call after the table |
| **Integration** ("AI chatbot for Salesforce") | What the integration does in that platform's terms | The objects and APIs it touches, auth method, limits or quotas, sync direction, 2–3 concrete workflows, one known gotcha | All of the above | Booking, after the workflows |
| **Use case / workflow** | The task and the outcome | Trigger → steps → systems → human approval point → metric moved, a sample input and output | Systems, metric, approval point | Case study or call |
| **Shortlist / "Top N firms"** | The short answer and the methodology | Criteria, a disclosed relationship if you're listed, "what to watch" for every entry including yours | Real evaluation notes | Soft. Use sparingly. Never rank yourself #1 by default |

On shortlists: some services firms rank for commercial queries with "Top N" lists that include themselves. In Ray's October 2026 data, brands that ranked themselves #1 were left out of AI Overview recommendations 83% of the time.† Google is demoting listicles that are easy to substitute for each other. Write one only if the evaluation is real, and publish few of them.

## 4. Element rules

**Title tag**
- Unique per page, with the distinguishing entity first. Roughly 40–60 characters; Backlinko found the best CTR in that range.
- Brand at the end, or omit it. Google rewrote about 76% of titles in Q1 2025 and most often dropped the brand.†
- Match the H1's meaning, or Google will rewrite it.
- No keyword repetition. No dates unless the content changes with them.
- **Templates:** a title that differs from its siblings only by one swapped name is what Google calls "micro-boilerplate". Add the per-page differentiator: the outcome, the constraint, or the sub-intents covered. Google's own example: "What are AI agents? Definition, examples, and types".

**Meta description**
- One or two sentences that say what's on the page, including one concrete fact (a number, scope or deliverable).
- Never a keyword list.
- Programmatic descriptions are fine per Google, as long as they read naturally and vary from page to page. Check that the template doesn't produce broken grammar.
- On glossary pages, the definition sentence can serve as the description.

**H1.** One per page. State the subject plainly. It should agree with the title without copying it.

**First 100 words**
- Answer first, definitively. No throat-clearing ("In today's rapidly evolving…").
- Google's rater guidelines rate prominent filler Low. LLM citations skew toward the top third of a page.†
- Name the main entity and its key attribute in plain declarative sentences.
- A short Summary or TL;DR box under the H1 works well for guides and cost pages.

**H2s**
- Each one answers a sub-question the reader has, phrased the way they'd phrase it where that's natural. Don't force every heading into a question.
- Each section should make sense on its own: name the entity again, and avoid "as mentioned above". Search systems and AI answers pull individual passages.
- Keep the page coherent. Don't split it into micro-pages.
- Heading level order doesn't matter to Google. Clarity does.

**Body**
- Write in the domain's own vocabulary instead of repeating the head keyword. Put the head term in the title, H1 and first sentence, then use the specific terms: chunking, re-ranking, permission-aware retrieval, evals.
- High keyword density only works on huge domains.
- No word-count targets; Google says it has no preferred length.
- First-hand material is the differentiator: what was built, what broke, what was measured, what the client's constraint was. If a page claims experience, show the artifact: a diagram, a metric, a snippet.
- Link out to primary sources where a claim needs support.

**Tables**
- Use them for comparisons, specs, costs and decision criteria.
- Introduce each table with a sentence that states its takeaway, and keep it next to the text that explains it.
- A table of generic adjectives is filler.

**FAQ**
- 3–6 questions specific to this page, taken from real objections: sales calls, support tickets, the buyer's actual worries. Questions like "When is RAG the wrong tool?" or "Who owns the code?".
- Never harvest "People also ask" and answer each item generically. Google's rater guidelines use exactly that as a scaled-abuse example.
- Answers should add something the body doesn't. Never one question per URL.
- FAQ rich results are now limited to government and health sites, so markup is optional and only describes content that's visible on the page.

**Author and date**
- A named person with a relevant role and a profile page on guides, comparisons, cost pages and glossary entries. Add "Reviewed by" for technical claims.
- Show an updated date, and change it only when the content changes. Google lists changing dates without real changes as a red flag.
- Where AI substantially generated a page, a short "how this page was made" note fits Google's Who/How/Why guidance.
- Never invent an author.

**CTA.** On informational pages, one contextual CTA after the answer, tied to the reader's next step. Nothing above the answer, and no mid-article lead-capture blocks. Commercial pages can put the CTA in the hero, after the proof, and at the close.

**Internal links**
- Use descriptive anchors that make sense on their own, placed inside sentences. Never "click here".
- Link up to the hub, across to siblings, and between related page types: service ↔ integrations ↔ use cases ↔ glossary ↔ comparison ↔ cost guide.
- Every indexed page needs at least one internal link pointing to it.
- Avoid sitewide blocks of exact-match anchors.

**One topic, one URL.** Consolidate glossary, guide and blog pages that compete for the same term into one canonical page.

**Schema.** Match the page type (Article, Service, FAQPage, HowTo, SoftwareApplication). Mark up only content that is visible on the page. AI features need no special schema or files. An `llms.txt` or clean Markdown versions are cheap insurance, not a requirement.

## 5. Writing to be cited by AI answers

Good SEO is most of it. Google says AI Overviews and AI Mode need no extra optimization beyond being indexed and eligible for snippets. The levers that help on top of that:

- **Put definitive answers early on the page and early in each section.** Pages whose headline answers the query directly were cited more often in Kevin Indig's data.†
- **Make each section self-contained,** with the entity, the claim and its context, but keep it inside one coherent page. Google's Danny Sullivan warns against writing "bite-sized chunks" or separate versions for LLMs. Mike King and Aleyda Solis argue for self-contained passages. The two positions agree at the section level.
- **Focused pages beat "ultimate guides".** Cover the adjacent sub-questions, not every possible one.†
- **Give citable facts:** cost ranges, timelines, benchmarks, failure rates. Generic text gets filtered out. Turn data into sentences ("a 30-day high of 0.8929"), because answer engines quote sentences.
- **Comparison pages earn AI referrals.** Siege Media found versus pages were the strongest content predictor of AI traffic across 116 B2B sites.† Build the matchups you have evidence for, and no more.
- **Get mentioned off-site.** Brand mentions across the web correlated most strongly with AI Overview visibility (Ahrefs).† Talks, partner directories, open source and LinkedIn all count.
- **Ranking and citation are diverging.** In Ahrefs' data, the share of AI Overview citations taken from the top 10 fell from 76% to 38% between 2025 and 2026.† Precise long-tail pages can be cited without ranking for the head term.

## 6. Programmatic pages and generation prompts

Use this section when designing a template or an LLM prompt that will produce many pages.

**1. Make each page a data record, not a keyword slot.**
- Zapier's integration pages carry real trigger and action names. Wise's carry live rates. Toptal's carry real profiles. That per-page data is why they rank.
- Define the required fields for each page family (see the "Unique per page" column in §3). For example, an integration page needs auth method, objects touched, limits, workflows and a gotcha.
- **If the fields are empty, don't generate the page.** Fold the topic into its hub instead.

**2. Run the swap test.** Replace the entity name with a sibling's. If the page is still mostly true, it fails. The first 100 words, the FAQ and at least one insight must come from that page's own data. A useful prompt-level target is that most of the main content comes from page-specific inputs. That's a heuristic, not a Google number.

**3. Keep the shared modules separate.**
- Process, trust, engagement and CTA blocks sit below the page-specific content, look visibly separate, and are never the bulk of the page.
- Unique content goes in the first screen.

**4. Don't publish permutation matrices.** A {service × industry × technology} grid is the pattern Mueller flagged. Publish a combination only when it has a distinct need and distinct data.

**5. Use one source of truth.** Prices, counts and claims come from one dataset. Five of the services firms reviewed contradicted their own numbers across pages, and CTOs notice.

**6. Put these rules into the generation prompt:**
- Give the model the data record and forbid facts that aren't in it. That means no invented metrics, certifications, clients or uptime figures.
- Require the definitive answer in sentence 1 and page-specific FAQs.
- Give the ban list from `ai-tells.md` (stock words, presumptive intensifiers, redundant qualifiers, antagonism, not-X-but-Y).
- Say "omit the section" when its field is empty, instead of "write a section on X".
- Ask for varied structure where content differs. Eyebrows must not repeat the topic.
- Ask the model to return a list of missing facts alongside the page.

**7. Review and checks**
- An expert reviews every template and every high-value page.
- Sample the long tail and fix the template, not individual pages.
- Automated checks: hallucinated APIs and versions, near-duplicate similarity between sibling pages, banned phrases (`scripts/lint_copy.py`), and broken template tokens.
- Google now calls fact-checking AI content critical, including titles, meta descriptions, structured data and alt text.

**8. Roll out in cohorts.** Publish a few hundred to a couple of thousand pages, then watch indexing, impressions per page and engagement for 8–12 weeks before expanding. The drops in Ray's data lagged the publishing bursts by months.

**9. Control indexing and prune**
- Pages below the bar get `noindex`, or are never generated. Sitemaps list only pages that pass the gate.
- Every quarter, take pages with no impressions after 6 months, near-duplicates and outdated facts, and either improve them, merge and 301 them, or remove them.
- Prune for quality, not age.
- Refresh commercial comparisons roughly every 6 months.

## 7. What big domains get away with that you can't

IBM, AWS, Google Cloud, Toptal and old high-volume agencies still rank with:
- thin or dated technical content
- no author or date
- broken templated meta descriptions
- skill-swapped FAQs
- heavy keyword repetition
- mid-article lead capture

Domain authority covers for all of it. A smaller site gets none of that slack, and losing Google's trust costs it more. Copy their structure, which is often excellent: definition first, questions as H2s, dense links between related topics, a diagram of the mechanism. Don't copy their shortcuts.

Their services pages ("Reinvent the enterprise", "boundless potential") mostly don't rank for commercial queries, because enterprise buyers arrive through relationships. A firm whose buyers arrive through search should write its service pages in the voice of its best learning content: concrete scope, timelines, architecture, failure modes, named results. The same CTO reads both.

## 8. Pre-publish checklist (per page or per template)

- [ ] Results page reviewed; page type matches what ranks; the gap is written in the brief
- [ ] The page passes the deserve-to-exist gate and the swap test
- [ ] Title is unique, ~40–60 characters, entity-first, agrees with the H1, and isn't micro-boilerplate
- [ ] Meta description is unique, concrete and readable
- [ ] The answer appears within the first two sentences, with no filler
- [ ] Each H2 answers one sub-question and stands on its own
- [ ] At least one first-hand insight and one data point the top results don't have
- [ ] Every fact checked, including metadata, schema and code
- [ ] Tables carry real data, each with a takeaway sentence
- [ ] FAQ has 6 or fewer questions, page-specific, not harvested from "People also ask"
- [ ] Named author or reviewer; the date reflects real changes
- [ ] One contextual CTA, after the answer on informational pages
- [ ] Internal links go up, across and sideways with descriptive anchors; the page isn't orphaned
- [ ] Comparison pages are fair, criteria-based and disclose any bias
- [ ] `lint_copy.py` passes, apart from flags that are deliberate
- [ ] For programmatic pages: cohort size, monitoring window and prune rule are decided before launch
