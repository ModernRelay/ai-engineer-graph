# SPIKE extraction — "How Forward Deployed Engineering is done at Ramp" (Leo Mehr, Ramp) — FOR REVIEW

Source transcript: `transcripts/mehr-ramp-fde.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/ITMXwI6QL6A — AI Engineer World's Fair, published 2026-07-28.
`stagingTimestamp` for the artifact and all signals: 2026-07-28T00:00:00Z (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node. **[this batch]** = defined in another file of this 4-talk FDE set.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-mehr-ramp-scoping-tokens` | How Forward Deployed Engineering is done at Ramp (Leo Mehr — AI Engineer World's Fair) | youtube | https://youtu.be/ITMXwI6QL6A |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-leo-mehr`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-leo-mehr` | Leo Mehr (director of engineering, Ramp; joined ~2.5 years ago when FDE was two engineers, now leads ~30 engineers across forward deployed, developer API and a new AI-services business) | `AffiliatedWithCompany → co-ramp` **[registry]** |

## Companies (0 new)

- `co-ramp` **[registry]** — `RelevantCompany` target for all signals below.
- Named in passing, no new nodes: `co-notion` **[registry]** (Ramp runs the FDE request workflow on Notion and built the intake agent with Notion agents — "if any of you work at Notion, thank you"), `co-sap` **[seed]** (the S/4HANA integration request), Waymo (analogy only).

## Elements (3 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-always-be-scoping` | Always be scoping | concept | — | Ramp's first FDE principle, against the belief that an FDE's job is to say yes to the customer: you want to find a way to say yes, but you have to deliver good software and build the *right* thing. Practically it is a context-gathering interrogation before any build — what is actually driving the urgency (an end-of-quarter sales rep chasing quota is not the customer), who will use this, have all workarounds been exhausted, is there a manual stopgap, does the customer have technical resources to hit the API instead — and, most important, does anyone else in the pipeline or customer base benefit. Validate even the most basic assumptions ("horses with rockets strapped to their legs" is what saying yes without scoping builds) |
| `el-scale-with-tokens` | Scale with tokens | concept | harness | Ramp's second FDE principle: unless you are scaling with model capabilities you fall behind, so jobs must be reinvented continuously — whatever knowledge work you do today, figure out how models and agents do it for you. Applied to FDE it means taking the whole lifecycle (gather context → scope the request → write the spec → implement the feature) and replacing each stage with agents. Daunting whole, tractable in pieces: the first stage and the last stage are largely solved (intake agents; frontier models one-shot medium-size features), the middle is "gnarly, unformed and difficult" and is where the investment goes |
| `el-fde-request-intake-agent` | FDE request intake agent | product | harness | Ramp's internal agent on the `#fde-requests` channel, where account managers, solutions and sales reps post any prospect/customer blocker large enough to escalate; the underlying Notion workflow holds the detail. The problem it attacks is variance — some submitters write a thorough customer-sourced request, others write one line ("we need this SAP integration") — which previously forced FDEs to read, interpret, check what already exists in the product, and run manual back-and-forth. The V1, built with Notion agents, only read the request and asked a couple of questions; the current version runs several rounds of questioning with the submitter until it judges the request ready to become a spec (with a penguin persona to make it approachable). Results reported after a couple of weeks: reply latency from hours or days down to seconds, reps engaging with the agent directly, and roughly 20% of scoping time saved |

Element edges: all three `IdentifiedInArtifact → ia-aie-mehr-ramp-scoping-tokens`; `el-fde-request-intake-agent` `DevelopedByCompany → co-ramp` **[registry]**; `el-fde-request-intake-agent` `EnablesElement → el-scale-with-tokens`; `el-fde-request-intake-agent` `UsesElement → el-always-be-scoping` (the agent automates the scoping interrogation, it does not replace it); `el-scale-with-tokens` `UsesElement → el-software-factory` **[this batch]** (defined in `reyes-factory-fde.md` — Mehr's "building out this factory / agent factory" is the same construct one function deep); `el-always-be-scoping` `ExemplifiesPattern → pat-value-of-judgement` **[registry]**; `el-scale-with-tokens` `EnablesPattern → pat-harness-over-model` **[registry]**; `el-forward-deployed-engineering` **[registry]** `IdentifiedInArtifact → ia-aie-mehr-ramp-scoping-tokens`.

## Signals (4 new)

All: domain `harness`, `SpottedInArtifact → ia-aie-mehr-ramp-scoping-tokens`, `SourcedFromSource → source-aie-yt` **[registry]**, `RelevantCompany → co-ramp` **[registry]**.

| slug | name / brief | FormsPattern | OnElement |
|---|---|---|---|
| `sig-ramp-fde-inside-engineering` | Counter-framing from a non-vendor FDE org: the meme that FDE is "the final evolution / boss mode of technical go-to-market roles" is called "totally wrong" for Ramp. FDE there lives **inside the engineering organization**, its goal is to help Ramp win up-market, and the work is the core product plus new agentic features made to work well for the largest enterprise customers. Growth trajectory: 2 engineers ~2.5 years ago → ~30 engineers today across forward deployed, developer API and a new AI-services business. Opening admission: "no one knows what FDE is" — a running theme of the track | `FormsPattern → pat-saaspocalypse` **[registry]** | `OnElement → el-forward-deployed-engineering` **[registry]** |
| `sig-scoping-beats-yes` | Two field stories as the evidence for scoping discipline. (1) Friday night, an enterprise sales rep says a strategic logo only closes if Ramp builds an SAP S/4HANA integration; the default engineering reflex is to go find the SAP API docs, the trained FDE reflex is to ask what is driving the urgency — often the rep's end-of-quarter quota rather than the customer. (2) The painful one: a large enterprise needed a mobile reimbursement feature, the mobile team was swamped, two FDEs taught themselves iOS *and* Android and shipped both in a couple of weeks — then the customer revealed it mandates iOS devices for all employees. The Android half was wasted because the most basic assumption went unvalidated | `FormsPattern → pat-value-of-judgement` **[registry]** | `OnElement → el-always-be-scoping` |
| `sig-fde-lifecycle-agentified` | An FDE org agentifying its own job function, stage by stage. Shipped: the request-intake agent (hours/days → seconds, ~20% of scoping time saved, reps now talk to it directly). Already easy: spec → working software, because frontier models one-shot medium-size features. The remaining middle of the pipeline is "super gnarly and unformed" and is where the team is investing. Mehr's 6–12-month projection of what FDE at Ramp *is*: applied-AI problems — keeping the agent harness running each stage smooth, keeping per-stage output quality good with evals, rubrics and human feedback, and the biggest challenge, getting the agent the right context (a product manager's head-knowledge; Notion docs, knowledge base and help articles only go so far; skills, memories, tools) | `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-scale-with-tokens`, `el-fde-request-intake-agent` |
| `sig-slop-cannon-without-scoping` | The talk's closing claim, stated as a two-way failure mode: build the agent factory without scoping discipline and you get "a token maxing slop cannon"; keep the scoping discipline without investing in the factory and "your agent-native competitors are just going to overtake you and outcompete" — "it's going to be over for you". Both principles are required, and the throughline that survives the automation is that the FDE still owns taste and judgment over the final output | `FormsPattern → pat-value-of-judgement` **[registry]** | `OnElement → el-always-be-scoping`, `el-scale-with-tokens`, `el-token-maxing` **[this batch]** (defined in `wu-cognition-fde.md`) |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-scoping-and-tokens-are-multiplicative` | The two principles are a product, not a sum: scoping without an agent factory loses to agent-native competitors on speed; an agent factory without scoping industrializes building the wrong thing. Automating an unexamined intake pipeline does not produce leverage, it produces volume — the same failure the iOS/Android story produced by hand, at machine scale. Which is why Ramp put its first agent on the *scoping* stage rather than the implementation stage | `HighlightsPattern → pat-value-of-judgement` **[registry]** | `ReliesOnElement → el-always-be-scoping`, `el-scale-with-tokens` |
| `ins-taste-and-judgment-remain-the-fde-job` | When every stage of your own job — context gathering, scoping, spec writing, implementation — is being handed to agents, what remains is responsibility for taste and judgment over the final output; that is the throughline of the role, and the reason the job description survives its own automation. The corollary is that the FDE's future work is applied-AI work: harness smoothness, per-stage output quality via evals/rubrics/human feedback, and the context-supply problem of getting a product manager's head-knowledge into an agent | `HighlightsPattern → pat-value-of-judgement` **[registry]** | `ReliesOnElement → el-scale-with-tokens`, `el-forward-deployed-engineering` **[registry]** |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-mehr-ramp-scoping-tokens`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-scope-an-inbound-request` | Interrogate an inbound customer request before building anything | Do not treat "yes" as the job. Before touching the integration docs, ask: what is actually driving the urgency, and is it the customer or the rep's quarter? Who will use this? Have we exhausted the workarounds? Is there something manual we can do in the meantime? Does the customer have technical resources — can they hit our API so we don't build this at all? Then look past the request: which other prospects in the pipeline and existing customers benefit, so what you build is generalizable rather than bespoke. Validate the basics explicitly — platform, user list, mandated devices — before committing engineering weeks; the assumption you never thought to check is the one that wastes the sprint | `ReferencesElement → el-always-be-scoping` |
| `how-agentify-the-fde-pipeline` | Replace your own job stage by stage with agents | Break the lifecycle into stages (gather context → scope → spec → implement) and attack them one at a time; whole-pipeline replacement looks daunting and is tractable in pieces. Start where variance and latency are worst — request intake — and ship a trivial V1 (read the request, ask a couple of questions) rather than the full design; the latency drop alone changes behaviour, and submitters start engaging with the agent directly. Iterate to multi-round questioning until the agent can judge a request spec-ready. Measure it (reply latency, share of scoping time saved). Expect the last stage to be nearly free (frontier models one-shot medium features) and budget your effort for the gnarly middle. Wrap each stage with evals, rubrics and human feedback for output quality, and treat context supply — the product knowledge in a PM's head that Notion docs and help articles don't capture — as the hard problem, addressed with skills, memories and tools. Keep taste and judgment over the final output as a human responsibility | `ReferencesElement → el-fde-request-intake-agent`, `el-scale-with-tokens` |

## Dropped

- The "FDE is the final boss of technical GTM" meme image — kept in prose inside `sig-ramp-fde-inside-engineering` as the position being rejected; no node.
- Notion / Notion agents as an element — the build platform for the V1 intake agent; kept in the `el-fde-request-intake-agent` brief with `co-notion` **[registry]** named in prose. No edge to `el-notion-workers` / `el-notion-auto-model` **[registry]** (batch 10): the captions never say which Notion agent surface was used.
- SAP S/4HANA as an element — it is the example integration in the scoping story, not a subject; `co-sap` **[seed]** named in prose only.
- Waymo / horses-with-rockets analogy, the penguin persona — illustration; the penguin is kept in the element brief because it is a stated adoption mechanism ("more friendly and approachable").
- "Greg" (a CSM who posted the example request) — internal individual, no expert node.

## Review notes

1. **Caption garbles.** "FDE" and "FTE" alternate and always mean **forward deployed engineer**; "four deployed" = **forward deployed**; "FD" = FDE; "when you're making the alarm call" is unrecoverable — most likely "when you're making the *LLM call*"; "SAP S/4HANA" is transcribed correctly but spoken quickly. One profanity is masked in the captions (`[\h__\h]`). The percentage figures ("20% of the time", "a large percentage, I don't know, 20%") are explicitly hedged by the speaker.
2. **`el-scale-with-tokens` → `el-software-factory` [this batch] is a cross-file edge.** Mehr twice calls the agentified pipeline "this factory" / "building out this agent factory" without defining it; Reyes defines exactly that construct in the same track on the same day. Reusing rather than coining a fourth factory synonym — but the edge is our inference of equivalence, not a stated claim, so drop it if you want strict transcript fidelity. Note also the third node in this family, `el-lights-off-software-factory` **[registry]** (batch 11), which is a *different* claim (see review note 3 of `reyes-factory-fde.md`).
3. **Best non-vendor data point in the set.** Ramp is the only one of these four talks where FDE is not the vendor's go-to-market arm for an AI product — it is an engineering function at an AI-*consuming* fintech, reporting into engineering rather than sales, aimed at winning up-market. That makes `sig-ramp-fde-inside-engineering` the corpus's cleanest counter-example to reading FDE as purely a GTM motion, and it is worth weighting when the eight-talk reconciliation decides whether the FDE cluster states one thesis or two.
4. **`pat-value-of-judgement` load.** Three of four signals plus both insights home there; this is the talk in the set that most directly restates Osmani's thesis (execution industrialized, judgment is the durable edge) from inside a job function that is automating itself. `sig-fde-lifecycle-agentified` is the exception, homed on `pat-harness-over-model` because its content is per-stage harness quality, evals and context supply.
5. **Domain enum**: `harness` on all four signals per the `brunet-cursor-forward-deployed.md` precedent. `el-always-be-scoping` deliberately has no domain — it is a delivery-discipline concept with no technical domain.
6. **FDE-thesis proposal** (identical note in all four files of this set): *agentic products are customizable without limit, so implementation has moved from the buyer to the vendor; shipping software now means embedding engineers who co-build, measure and prove the outcome, which turns go-to-market into a delivery-and-product-feedback function.* Ramp is the partial counter-instance that sharpens it — same function, same principles, but pointed at its own product for its own enterprise customers rather than at a customer's codebase, and reporting into engineering. If the eight-talk reconciliation coins the thesis, this file is the evidence that the mechanism is not vendor-specific. Not coined here; central reconciliation sees all eight.
