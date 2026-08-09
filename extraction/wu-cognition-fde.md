# SPIKE extraction — "How Forward Deployed Engineering is done at Cognition" (Jia Wu, Cognition) — FOR REVIEW

Source transcript: `transcripts/wu-cognition-fde.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/RVxym6mmIns — AI Engineer World's Fair, published 2026-07-28.
`stagingTimestamp` for the artifact and all signals: 2026-07-28T00:00:00Z (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node. **[this batch]** = defined in another file of this 4-talk FDE set.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-wu-cognition-deployed-engineering` | How Forward Deployed Engineering is done at Cognition (Jia Wu — AI Engineer World's Fair) | youtube | https://youtu.be/RVxym6mmIns |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-jia-wu`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-jia-wu` | Jia Wu (deployed engineering lead, Cognition; joined via the Windsurf acquisition) | `AffiliatedWithCompany → co-cognition` **[registry]** |

## Companies (0 new)

- `co-cognition` **[registry]** — `RelevantCompany` target for the signals below.
- Named in passing, no nodes: Windsurf (acquisition origin — see review note 3), Cursor, Nubank, "Built"/Builder (⚠ garble), an unnamed large Latin American bank.

## Elements (3 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-devin` | Devin | product | harness | Cognition's autonomous software-engineering agent. Debuted 2024 at ~13% on SWE-bench — "we're so back / we're so cooked" — then widely dismissed within a week as something you'd use only if desperate and out of ideas; Cognition ran with the joke in its SF ad campaign ("we're actually good now"). Today's surface area spans Devin Cloud (the cloud agent it is known for) plus a CLI and an IDE, the latter inherited from the Windsurf side. Positioned against "single-point tools that are just CLIs or just IDEs" on the claim that only an agent harness can lift a whole organization rather than individual engineers |
| `el-token-maxing` | Token maxing | concept | harness | Deploying agents with no specific direction so that consumption becomes the de-facto KPI. Described as the first era of deployed engineering (~1.5–2 years ago) when budgets were subsidized, nobody worried about spend, and maximizing token usage *was* the target; now an anti-pattern — "you're wasting tokens, burning spend, not getting any tangible outcomes" — as large regulated enterprises ask whether they are getting value or just burning tokens. Shared vocabulary across this FDE set: Ramp's failure mode for an unscoped agent pipeline is "a token maxing slop cannon" |
| `el-session-engineering-hours` | Session-derived engineering hours | concept | harness | Cognition's ROI instrumentation: one agent trace/trajectory is a "session", and metrics derive from sessions how many engineering hours were generated and how many were *productive*. Rolled up into three customer-facing deltas measured before vs after deploying the agent — headcount equivalent, delivery-timeline compression, and raw merged-PR counts — as the counter to the objection that session counts are just token maxing with extra steps |

Element edges: all three `IdentifiedInArtifact → ia-aie-wu-cognition-deployed-engineering`; `el-devin` `DevelopedByCompany → co-cognition` **[registry]**; `el-session-engineering-hours` `EnablesElement → el-devin` (the measurement layer that makes the deployment defensible); `el-session-engineering-hours` `ExemplifiesPattern → pat-saaspocalypse` **[registry]** (outcome-denominated selling); `el-forward-deployed-engineering` **[registry]** `IdentifiedInArtifact → ia-aie-wu-cognition-deployed-engineering`. `el-token-maxing` carries no pattern edge — it is named as an anti-pattern, and the schema has no Element→Pattern contradiction edge; the negative reading is carried by `sig-token-maxing-to-measured-outcomes`.

## Signals (5 new)

All: domain `harness`, `SpottedInArtifact → ia-aie-wu-cognition-deployed-engineering`, `SourcedFromSource → source-aie-yt` **[registry]**, `RelevantCompany → co-cognition` **[registry]**.

| slug | name / brief | FormsPattern | OnElement |
|---|---|---|---|
| `sig-cognition-internal-agent-leverage` | Cognition dogfooding number: over the last six months, "for better or worse we might have been behind on hiring", the org shipped almost an **order of magnitude more** good-quality robust PRs by deploying its own agent — described as a step-function increase in engineering leverage rather than an incremental one. Enterprise-side consumption of the agent described as parabolic growth in adoption and use cases | — (held pattern-less; `pat-ai-native-org` candidate resonance — see review note 4) | `OnElement → el-devin` |
| `sig-coding-solved-delivery-not` | Cognition's problem framing: coding itself is "a mostly solved problem" — models are good enough that with enough context engineering you get the code blocks you care about — and writing code faster is only ~20% of the problem. The remaining 80% is testing, reviewing, deploying and maintaining code across the enterprise, on real legacy rather than zero-to-one prompting, in languages nobody learns anymore (COBOL, JCL) | `FormsPattern → pat-verification-gap` **[registry]** | `OnElement → el-devin` |
| `sig-token-maxing-to-measured-outcomes` | The KPI shift in deployed engineering, dated by a practitioner: a year and a half to two years ago the target was maximizing token usage — budgets were subsidized, "you could just run anything you wanted"; now the largest and most regulated enterprises ask whether they are getting true value or burning tokens, and the problem "has really shifted into the delivery space". ROI measurement for agents is stated outright as an unsolved problem — "the company that will solve this will be a $5 trillion market cap" | `FormsPattern → pat-saaspocalypse` **[registry]** | `OnElement → el-token-maxing`, `el-session-engineering-hours` |
| `sig-org-level-not-engineer-level-10x` | Stated core differentiator: making individual engineers 10x faster is fine and still valuable, but the unlock is making an *organization* 10x faster — "including every single person that might be technical or non-technical across the company". Single-point tools that are just CLIs or just IDEs are argued to structurally fail at this, which is why the deployment is sold as a partnership rather than a seat | `FormsPattern → pat-saaspocalypse` **[registry]** | `OnElement → el-devin`, `el-forward-deployed-engineering` **[registry]** |
| `sig-cognition-deployment-case-numbers` | Deployment proof points offered on stage (anonymized case studies plus public ones): a 3-month embed delivering the equivalent of "+150% headcount"; ~82% reduction in delivery timelines measured on the customer's own pre/post agile metrics; roughly double the PR throughput versus single-point tools before an agent harness; Nubank's ETL migration, staffed with 50 engineers, delivered in about a third of the timeline autonomously; a large Latin American bank's tax-identification-system migration at half the required effort; and a public customer reporting ~10x weekly engineering output ("10x per week worth of engineering talent") | `FormsPattern → pat-saaspocalypse` **[registry]** | `OnElement → el-devin`, `el-session-engineering-hours` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-field-is-the-highest-fidelity-eval-set` | The deployed-engineering org is the vendor's best evaluation set: "we have the highest fidelity evaluation set that comes back from our customers — we are in the field every single day". Solving the customer's problem completely is only half the equation; the other half is carrying that context back so the product moves toward the customers' problems, maximizing the overlap of the two circles (what we build × what they need). Enterprise engineering challenges arrive "in similar shapes", so the field job is classification — is this challenge common across the enterprise or unique to this user, and should this workaround, hack or bug become a feature? — and the payoff is a de-risked roadmap where you know what to build for which revenue. The feedback is "half of the loop that makes the next deployment better than the previous deployment" | `HighlightsPattern → pat-saaspocalypse` **[registry]** | `ReliesOnElement → el-forward-deployed-engineering` **[registry]**, `el-devin` |
| `ins-t-shaped-with-spikes` | The FDE persona is deliberately undefined by title — "are you a sales engineer? are you a solutions architect? what are you?" — and hired as a T with genuine spikes: wide across people, business, process, customer and technology skill, deep in at least one. Cognition hires from product management (because if the cost of software engineering goes to zero, knowing how to design a product that makes sense is the scarce skill — "you can just prompt it"), from founders, and from spiky engineers: weak business sense can be taught, being the technical expert in the room while on the job cannot. Good deployed engineers do all of it; great ones add relentless curiosity about *why* this problem matters to the business, and relentless tie-in to the customer | `HighlightsPattern → pat-value-of-judgement` **[registry]** | `ReliesOnElement → el-forward-deployed-engineering` **[registry]** |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-wu-cognition-deployed-engineering`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-map-agent-capabilities-to-customer-problems` | Map agent capabilities onto named customer problems, then measure | Never deploy agents into a complex SDLC with no specific direction — that is token maxing. Split the day roughly 50/50 between customer calls and hands-on-keyboard work; use the calls to learn which strategic initiatives are highest-leverage for the business. Aim the agent at the specific inventory every enterprise has: the backlog nobody gets to, remediations, delayed code that never ships, tests nobody writes, alert triage. Then automate yourself out of the loop — set the agent up to fire on specific alerts and events rather than being manually triggered. Instrument from day one: sessions → engineering hours → productive hours, plus timeline and PR deltas against a pre-deployment baseline, because ROI measurement is the open problem and the customer will ask | `ReferencesElement → el-devin`, `el-session-engineering-hours`, `el-token-maxing` |
| `how-close-the-fde-product-loop` | Treat the field as the eval set and close the loop into the roadmap | Take the highest-fidelity signal you have — daily customer contact — and route it back to product deliberately, not incidentally. For each challenge, ask whether it is common across the enterprise or unique to one user, and whether a workaround, hack or bug should become a feature. Always ask why the problem matters to the business as a whole and whether it can be communicated back in a way that improves things for every other customer; the goal is a de-risked roadmap. Flag engineering practices that need fixing with no ego attached — "we are all in the same boat". Treat every role as go-to-market: the target is customer success at all costs, and everybody owns it | `ReferencesElement → el-forward-deployed-engineering` **[registry]**, `el-devin` |

## Dropped

- Windsurf as a company node — mentioned only as the speaker's route into Cognition (post-acquisition) and as an audience reference point; kept in the expert brief. Coin later if a Windsurf-centric talk appears.
- Cursor — one-word comparison ("if you've used something like Cursor, Windsurf, we also expose an IDE"); no edge to `co-cursor` **[registry]**.
- Nubank / the Latin American bank / "Built" — customer names inside `sig-cognition-deployment-case-numbers`; no company nodes (the last is a caption garble, see review note 2).
- The product/problem Venn-diagram framing ("maximize the overlap", PMF as the intersection) — pedagogical device, folded into `ins-field-is-the-highest-fidelity-eval-set`.
- "Cockroach Labs" — a caption garble for "Cognition", not a customer reference (see review note 1).

## Review notes

1. **Caption garbles — one is dangerous.** At the end of the product/problem section the captions read "*that is forward deployed engineering at Cockroach Labs*"; every surrounding sentence is about Cognition and the speaker never changes subject. This is a mis-transcription of "Cognition", **not** a Cockroach Labs customer reference — do not create `co-cockroach-labs` from it. Also: "Gia" = **Jia** (speaker name per the official listing); "Flood Code" = **Claude Code**; "SweepBench" = **SWE-bench**; "for deployed / four deployed" = **forward deployed** throughout; "Cog" = Cognition.
2. **"Built" is unresolved.** "if we think about the built card" and "Built has great engineers" — plausibly Builder.ai, Built Technologies, or a company called Built; the captions give no disambiguating context. Kept as prose inside the case-numbers signal with the ambiguity flagged; **verify before any public-facing use**, and do not coin a company from it.
3. **Numbers are vendor-reported and mostly anonymized.** "+150% headcount", "82% reduction", "double the PRs", "10x weekly output", "order of magnitude more PRs" are all self-reported by the vendor about its own product, several from anonymized case studies. They are recorded as claims-made-on-stage (which is what a Signal is), not as verified outcomes. The "+150% headcount" phrasing is itself ambiguous — spoken as "delivered about 150% like plus headcount" and then illustrated as "150 extra coworkers", i.e. the percentage and the headcount figure are conflated in the captions.
4. **`sig-cognition-internal-agent-leverage` is deliberately pattern-less.** It is fresh evidence for the uncoined **`pat-ai-native-org`** candidate (a frontier vendor's own engineering org shipping ~10x the PRs via its agent while behind on hiring), which per the registry ledger is the widest-evidenced uncoined candidate in the corpus. Following the `sig-org-redesign-demand` precedent (batch 5), no FormsPattern edge is asserted — if `pat-ai-native-org` is coined at review, this signal is a natural source. `sig-org-level-not-engineer-level-10x` carries secondary resonance for the same candidate.
5. **`el-token-maxing` is shared across this set** — defined here (Cognition uses it as the name of the previous era of deployed engineering) and reused by `mehr-ramp-fde.md` ("a token maxing slop cannon"). Two independent FDE vendors using the same coinage for the same anti-pattern in the same track is a decent argument for keeping it as a node rather than prose. Adjacent registry element to check at seeding: `el-lights-off-software-factory` shares the "spend without reading the output" flavour but is a different claim.
6. **Domain enum**: all five signals tagged `harness` per the `brunet-cursor-forward-deployed.md` precedent; `sig-token-maxing-to-measured-outcomes` is really a commercial claim and could be null.
7. **FDE-thesis proposal** (identical note in all four files of this set): *agentic products are customizable without limit, so implementation has moved from the buyer to the vendor; shipping software now means embedding engineers who co-build, measure and prove the outcome, which turns go-to-market into a delivery-and-product-feedback function.* Cognition supplies both halves in one talk — the field as the vendor's highest-fidelity eval set (feedback), and "everybody is go-to-market" with ROI measurement named the unsolved $5T problem (delivery/proof). Not coined; central reconciliation sees all eight talks.
