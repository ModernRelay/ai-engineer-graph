# SPIKE extraction — "Intelligence + Continual Learning = Expertise" (Yu Su, NeoCognition) — FOR REVIEW

Source transcript: `transcripts/su-neocognition-continual-learning-expertise.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/I6aiEf3aEFQ — AI Engineer World's Fair, **Continual Learning track**, published 2026-08-12.
`stagingTimestamp` for the artifact and all dated nodes: 2026-08-12 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Shape of the talk: the **conceptual keynote of the continual-learning track** — deliberately non-technical. Draws one distinction (intelligence vs expertise) and uses it to explain why coding agents work and almost nothing else does, then argues continual learning is the bridge between the two and proposes scaling expertise as a new axis. Caption garbles: "Isu" → **Yu Su**, "The Neo Cognition" → **NeoCognition**, "token mixing" → **token maxxing**, "scene done" → *seen/done*, "word models" → **world models**, "generate to lead to" → *generalize*.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-su-continual-learning-expertise` | Intelligence + Continual Learning = Expertise (Yu Su, NeoCognition — AI Engineer World's Fair) | youtube | https://youtu.be/I6aiEf3aEFQ |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-yu-su`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-yu-su` | Yu Su (professor at The Ohio State University; also COO at NeoCognition, working on agents and continual learning) | `AffiliatedWithCompany → co-neocognition`, `AffiliatedWithCompany → co-ohio-state` |

Referenced, not contributors: Andrew Ng (the "decade of agents, not year of agents" claim, attributed and dated as possibly stale), Satya Nadella ("two weeks ago" — the human-AI learning loop as institutional memory). Neither coined; both are single-clause attributions.

## Companies (2 new)

| slug | name | type | note |
|---|---|---|---|
| `co-neocognition` | NeoCognition | developer | Startup building agents and continual learning; the talk's thesis (scaling expertise, per-microworld specialization) is its positioning |
| `co-ohio-state` | The Ohio State University | research | Speaker's academic affiliation; coined to carry the dual-affiliation edge per the b8 `co-university-of-maryland` precedent |

Reused **[registry]**, edge-only: `co-anthropic` **[seed]** — cited for the revenue curve (≈400× growth in under two years to ~$40B, "newest number maybe $60B annualized"), used as the evidence that coding is the language agent's first mass market. ⚠ figures are caption-sourced, see review note 4.

## Patterns (1 new — **COINED at review 2026-08-14**)

| slug | name | kind | brief |
|---|---|---|---|
| `pat-continual-learning-turn` | The Continual Learning Turn | dynamic | The frontier of model improvement is shifting from pre-training scale to post-deployment learning, making the accumulation loop — not the base model — the locus of compounding advantage. Six legs in the evidence: a claimed **new axis of scale** (expertise as orthogonal to intelligence; compute-on-context as a fourth axis once data and model size are fixed); **algorithms** that learn from production rather than curated environments (on-policy self-distillation, offline/online hint taxonomies); **measurement** built to detect accumulation rather than point capability (the gain metric; benchmark instances being designed independent and therefore unchainable); **supply economics** (public data exhausted, and the commercial data layer structurally cannot cross into private corpora); systems **already shipping** the loop outside the weights; and **enterprise reality** — most organizations sitting on production traces asking to be made better. **Contested from birth:** an observability vendor with cross-customer visibility reports seeing little real continual learning in production, an independent benchmark finds plain in-context learning beating engineered context management on both cost-adjusted frontiers, and the field's own practitioners describe the current state as "pseudo continual learning" — batch updates offline, then re-upload |

Defined here because this file is the track's conceptual keynote and states the new-axis claim most explicitly. Coinage record and full ledger in registry § "Batch-19 additions" and § "Coinage record — 2026-08-14".

## Elements (5 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-intelligence-vs-expertise` | Intelligence vs expertise | concept | harness | The talk's load-bearing distinction. **Intelligence** = "the capacity to reason through unfamiliar problems from available context" — what frontier models are increasingly good at, where every episode is independent. **Expertise** = "accumulated and situated competence… the ability to act reliably, efficiently, and with judgment" in a particular domain. They differ on which way context flows (intelligence *consumes* supplied context; expertise *knows what context to bring*) and on search behaviour (intelligence expands the search, brute-forcing 100 parallel attempts; expertise **compresses** it, having learned the shortcuts). Drawn from cognitive science: experts don't know more facts, they *see differently* — pattern recognition, deep structure, conditional rules with known exceptions, and taste including "when it's good enough" |
| `el-microworlds-thesis` | Millions of microworlds | concept | harness | Why generalist agents underperform outside code: "modern society is really not just one unified world, it's millions of these micro worlds." Every domain, profession and company is idiosyncratic — even the same software is configured differently per company — each with "its unique local physics: different structures, constraints, affordances and dynamics." Too heterogeneous and dynamic "for any monolithic model to compress into one static representation," so agents must learn on the job per microworld. ⚠ terminology collision with `el-microworlds` **[registry, b6]** — see review note 3 |
| `el-modern-moravec-paradox` | The modern Moravec's paradox | concept | harness | The framing for why coding worked first: classical Moravec says hard things are easy for AI and easy things hard; the modern version is that models excel at symbolic reasoning — coding, maths, "the crown jewel of intelligence" — while still failing at everyday digital work, because those require a different set of cognitive competencies. Code was the privileged first market precisely because it is "already a language-native world": symbolically represented, structurally recorded, with rewards and tests already in place |
| `el-continual-learning-definition` | Continual learning as adaptive compression | concept | training | A working definition offered to disambiguate an overloaded term: "adaptive compression of experience into reusable structures for future behavior," with four independently-instantiable axes — *what experience* (episodes, semantic facts, procedures, human or environment feedback), *how compressed* (embeddings, symbolic indexes, distillation into parameters, RL), *into what structure* (adapters, vectors, graphs, skills, world models), and *used how* (recall, state prediction, planning, actuation, value function). The claim that the field is confusing because these four axes are conflated is the definition's main work |
| `el-escape-intelligence` | Escape intelligence (unbounded expertise from bounded intelligence) | concept | training | The talk's most speculative claim, presented as its most interesting future: plot raw intelligence on x and expertise on y and they are largely **orthogonal**. Without continual learning, scaling intelligence produces "the world's smartest novice" — brilliant at any single problem, accumulating nothing, brute-forcing every time. With it, the continual-learning algorithm sets the *slope*. The conjecture: past some intelligence threshold, a strong enough algorithm yields unbounded expertise without stronger models — "do we need to continually train these larger and larger models, or are they already good enough and what we're missing is better continual learning algorithms?" |

Element edges: all five `IdentifiedInArtifact → ia-aie-su-continual-learning-expertise`.
`el-modern-moravec-paradox` `EnablesElement → el-microworlds-thesis`;
`el-microworlds-thesis` `EnablesElement → el-intelligence-vs-expertise`;
`el-continual-learning-definition` `EnablesElement → el-escape-intelligence`;
`el-escape-intelligence` `UsesElement → el-intelligence-vs-expertise`;
`el-continual-learning` **[registry, b8]** `UsesElement → el-continual-learning-definition`.

Reused elements (no new nodes): `el-continual-learning` **[b8, Feizi/RELAI]** — this file supplies the definitional scaffolding the b8 node lacked; **recommend widening its brief at seeding**. `el-world-model` family: the talk asserts experts "have built a world model of their environment" in a generalized sense — kept in `el-intelligence-vs-expertise`'s brief rather than edged, given the outstanding `el-company-world-model`/`el-monday-world-model` merge-check.

## Signals (5 new)

All: `SpottedInArtifact → ia-aie-su-continual-learning-expertise`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-neocognition`.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-coding-was-the-privileged-market` | harness | An explanation, from an academic-turned-operator, for why agent success is so unevenly distributed: code is "already a language-native world" — symbolic representation, structured records, tests and rewards already in place — so it was the one domain where language agents could be dropped in whole. Evidence offered is Anthropic's revenue curve (≈400× in under two years, largely coding-driven). Outside that privileged world, deployment goes badly enough that Andrew Ng's "decade of agents, not year of agents" is quoted as still standing. The corollary is uncomfortable for generalist-agent roadmaps: the first market was not a beachhead but an outlier | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-modern-moravec-paradox`, `el-microworlds-thesis` |
| `sig-expertise-not-intelligence-is-scarce` | harness | The reframing: "intelligence is already becoming abundant — the frontier models are probably smarter than average humans — but expertise is still scarce." Expertise is defined as accumulated situated competence, distinguished from intelligence on two operational axes: expertise *supplies* the right context rather than consuming it, and *compresses* the search rather than expanding it. That second axis is offered as the direct cause of the token-inefficiency now driving company-wide token-maxxing crackdowns — a smart novice brute-forces because it has no learned shortcuts | `FormsPattern → pat-value-of-judgement` **[registry]** | `OnElement → el-intelligence-vs-expertise` |
| `sig-scaling-expertise-as-new-axis` | training | The call to action and the track's organizing thesis in one line: "let's start scaling expertise" as a **new axis of scale**, orthogonal to raw intelligence, with the continual-learning algorithm setting the slope. Pushed to its strongest form as *escape intelligence*: past a threshold, a good enough algorithm might yield unbounded expertise from bounded intelligence, which would make further pre-training scale optional. The anchor statement of `pat-continual-learning-turn`, coined in this file | `FormsPattern → pat-continual-learning-turn` | `OnElement → el-escape-intelligence`, `el-continual-learning-definition` |
| `sig-private-microworlds-next-data-frontier` | data-eng | The economic argument under the thesis: public training data is exhausted, and "the next internet-scale data opportunity is actually in all of these different private worlds." If specialized agents can learn in situ inside each company's idiosyncratic configuration, that learning can be channelled back to the general model. Paired with a sovereignty framing borrowed from Satya Nadella — every company building its own learning loop into institutional memory, "to still be in charge of their means of production." A data-supply claim and an enterprise-moat claim in the same breath | `FormsPattern → pat-sovereign-ai` **[registry]** | `OnElement → el-microworlds-thesis` |
| `sig-reliability-plasticity-tension` | training | The open problem named as the field's central conflict: agents must be simultaneously **reliable** and **plastic**, and these are inherently opposed — "reliable systems resist change; plastic systems like change." Offered with an existence proof rather than a solution ("we are incredibly plastic but manage to be dependable most of the time") and a technical bet that **both parametric and non-parametric learning are needed**, with the synergy between them unsolved. The stability/plasticity leg of the pattern; the same tension Asawa's benchmark operationalizes independently in this batch | `FormsPattern → pat-continual-learning-turn` | `OnElement → el-continual-learning-definition`, `el-continual-learning` **[registry, b8]** |

## Insights (2 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-agent-success-tracks-symbolic-legibility` | The distribution of agent success across domains is better predicted by how symbolically legible a domain already is than by how hard it is. Code came with its own representation, its own version history, and its own oracle — so the agent inherited a world it could read and a verifier it could trust. Every domain that has resisted agents so far lacks one of those three, and no amount of model scale supplies them. The implication for anyone picking an agent market is to audit for pre-existing representation and reward before capability | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** | `ReliesOnElement → el-modern-moravec-paradox`, `el-microworlds-thesis` |
| `ins-orthogonality-changes-the-scaling-question` | If intelligence and expertise are genuinely orthogonal axes rather than points on one curve, then the industry's central question stops being "how much smarter can the model get" and becomes "how steep can the accumulation slope be." That reframing is what makes the whole continual-learning track commercially coherent: it locates a source of compounding advantage that is not buying more pre-training compute, and it explains why the same frontier model can be transformative in one company and useless in another — the model is the intercept, the learning loop is the slope | `HighlightsPattern → pat-value-of-judgement` **[registry]** | `ReliesOnElement → el-escape-intelligence`, `el-intelligence-vs-expertise` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-su-continual-learning-expertise`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-target-agent-domains-by-legibility` | Pick agent domains by symbolic legibility, then build the learning loop | Before committing an agent to a domain, check what code got for free — is the world already represented symbolically, is the work already recorded structurally, and does a cheap oracle already exist? Where any of the three is missing, expect the brittleness that shows up outside coding, and plan to supply it rather than to out-scale it; treat each customer, team or configuration as its own **microworld** with local physics that must be learned rather than assumed, instead of expecting one static model to compress them all; when specifying a continual-learning system, force the four axes to be answered separately — *what* experience you capture, *how* you compress it, into *what* structure, and *how* it is used at inference — since most disagreement in this space is people instantiating different axes and using the same word; expect to need both parametric and non-parametric learning rather than picking a side; and hold reliability and plasticity as an explicit trade-off to be tuned, not a bug to be fixed | `ReferencesElement → el-microworlds-thesis`, `el-continual-learning-definition`, `el-intelligence-vs-expertise` |

## Dropped

- **The "standing between you and lunch" opener** — logistics.
- **The pre-history of AI agents** (1960s–80s expert systems and logical agents; 2010s deep-RL agents; multimodal LLMs as the first unified representation conducive to symbolic reasoning) — good context for `el-modern-moravec-paradox`, folded into its brief; no separate node.
- **The abundance peroration** (personal healthcare, financial advisors and tutors for everyone; lowering friction until new categories of work cross the threshold of worth doing) — motivational close; the substantive claim survives in `sig-scaling-expertise-as-new-axis`.

## Review notes

1. **⚑ RESOLVED — `pat-continual-learning-turn` COINED at review 2026-08-14, defined in this file.** Originally proposed here as a candidate. Thesis: *the frontier of model improvement is shifting from pre-training scale to post-deployment learning, making the accumulation loop — not the base model — the locus of compounding advantage.* This file is its **conceptual anchor**: an explicit new-axis-of-scale claim, a definition, and an orthogonality argument. Nine further data points arrive in the same batch (Morris/Engram, Malde/Trajectory, Denton/Applied Compute, Asawa/Berkeley, Hooker/Adaption, Khemani, Trivedy/LangChain, Druga/Sakana, plus Anthropic's dreaming feature). Two signals held pattern-less here. See registry § "Batch-19 additions" for the consolidated ledger and the coin recommendation.
2. **Pattern homing was deliberately conservative.** Only two signals took coined-pattern edges (`pat-model-not-bottleneck` for the coding-is-privileged argument, `pat-value-of-judgement` for expertise-is-the-scarce-thing). The `pat-sovereign-ai` edge on `sig-private-microworlds-next-data-frontier` is the weaker of the three — it rests on the Nadella "means of production" framing rather than on regulation or on-prem economics. **Drop-option:** if review reads sovereignty narrowly, hold that signal pattern-less for the same candidate ledger instead.
3. **⚠ Terminology collision — `el-microworlds` (b6).** Batch 6 coined `el-microworlds` from a different talk. Su's "millions of microworlds" is a distinct claim (idiosyncratic per-organization environments requiring per-instance learning), so it is coined here as **`el-microworlds-thesis`** rather than merged. Grep both before seeding; if review reads them as one concept, merge into the b6 node and widen the brief.
4. **⚠ Verify before seeding.** The Anthropic revenue figures (≈400× in under two years; ~$40B, "newest number maybe $60B annualized") are caption-sourced, hedged by the speaker himself, and used as third-party evidence rather than as the speaker's own data. They are the only quantities in the talk. The Nadella quote ("two weeks ago") is undated and unsourced beyond the attribution.
5. **Track context.** This is talk 1 of a 10-talk continual-learning track published the same day. It is the only one that argues at the conceptual level rather than presenting a method, a benchmark or a product, which is why its elements are concepts rather than technologies — and why it is the natural definitional home if the candidate pattern is coined.
