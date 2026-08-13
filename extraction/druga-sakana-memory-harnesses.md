# SPIKE extraction — "Memory Harnesses for Long-Running Research Agents" (Stefania Druga, Sakana AI) — FOR REVIEW

Source transcript: `transcripts/druga-sakana-memory-harnesses.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/R3-anFK1YM8 — AI Engineer World's Fair, **Continual Learning track**, published 2026-08-12.
`stagingTimestamp` for the artifact and all dated nodes: 2026-08-12 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Shape of the talk: the track's **empirical ablation study**, and the shortest talk in it (~13 min). Frames memory as a write-manage-read control loop rather than a store, builds a harness over local models with a recall-policy ladder (none → vector RAG → decisions ledger → oracle), and reports a clean pair of findings: when the task fits in context, memory adds cost and no capability; when it does not, a **ranked decisions ledger** beats both vector RAG and gated recall — and costs less. Caption garbles: "context blow"/"context rot" → **context rot**, "Meter" → **METR**, "Qwen 27B" → likely **Qwen3 27B** (⚠ see review note 4), "Deep Seek V4 Flash"/"DS4 flash" → **DeepSeek V4 Flash**, "X-Bench" → **xbench**, "Diamond" → ⚠ unresolved repo attribution, "deep seed" → DeepSeek.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-druga-memory-harnesses` | Memory Harnesses for Long-Running Research Agents (Stefania Druga, Sakana AI — AI Engineer World's Fair) | youtube | https://youtu.be/R3-anFK1YM8 |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-stefania-druga`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-stefania-druga` | Stefania Druga (research scientist, Sakana AI, Tokyo; previously based in the Bay Area — describes AI engineering as her home community) | `AffiliatedWithCompany → co-sakana-ai` |

Referenced without coining: the CEO of Coinbase, cited for a two-day-old post on cutting AI spend while increasing usage — attributed to the company, not the person (see `co-coinbase`).

## Companies (2 new)

| slug | name | type | note |
|---|---|---|---|
| `co-sakana-ai` | Sakana AI | research | Tokyo-based AI research lab; the talk's sovereignty framing ("we believe in the importance of sovereign AI today more than ever") is stated as an institutional position, not a personal one. Hiring in Japan |
| `co-coinbase` | Coinbase | developer | Coined on reference to carry one signal: publicly reported reducing AI spend **while increasing AI usage**, by shifting to local models plus better routing, caching, context hygiene and per-task visibility |

## Elements (4 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-memory-write-manage-read` | Memory as a write-manage-read loop | concept | context | The mental model the talk asks the audience to adopt: memory is "not just a database store — it's actually a control loop around the model," with distinct write, manage and read stages. Instantiated as a harness with three blocks: a **core** of traces always shown to the agent, a **recall** block where retrieval policy varies, and an **archival** block tracking information across sessions. Deliberately built over research agents with *zero durable memory* so that all memory behaviour comes from the harness and can be ablated |
| `el-recall-policy-ladder` | The recall-policy ladder | concept | context | The experimental design, and the file's most reusable artifact: hold the model fixed and vary only the recall policy across four rungs — (1) **no recall** baseline, (2) **vector RAG**, pulling on similarity alone, (3) a **decisions ledger** recording what was decided each turn, so entries can be ranked and prioritized, and (4) an **oracle** that is handed the ground-truth memory for each loop. The oracle is the ceiling estimate, and the finding that it does *not* reach maximum performance is itself a result |
| `el-decisions-ledger` | Ranked decisions ledger | technology | context | The winning recall policy. Rather than embedding and retrieving by similarity, record the **decisions** made at each turn and rank them for retrieval. On xbench long-horizon questions it outperformed vector RAG, no-recall, and a **gated** policy that merely asks the model whether it needs memory at all — and reproduced across two models (Qwen 27B 4-bit and DeepSeek V4 Flash) and a second benchmark (Spider V2). Its second property is economic: it retrieves the right thing *and* spends fewer tokens |
| `el-recall-policy-as-metric` | Recall policy as a first-class metric | concept | context | The call to action: treat the recall function as something you design, measure and report — "what type of memories do you want to store, how do you rank them, how do you design your recall function, and what survives across multiple sessions and runs?" Backed by the cost heuristic the experiments produced: **bad memory is expensive**, because it burns tokens *and* sends the agent the wrong way, while a good structural recall policy saves both budget and error |

Element edges: all four `IdentifiedInArtifact → ia-aie-druga-memory-harnesses`.
`el-memory-write-manage-read` `EnablesElement → el-recall-policy-ladder`;
`el-recall-policy-ladder` `UsesElement → el-decisions-ledger`;
`el-decisions-ledger` `ExemplifiesPattern → pat-model-not-bottleneck` **[registry]**;
`el-recall-policy-as-metric` `UsesElement → el-decisions-ledger`, `el-recall-policy-ladder`.

Reused elements (no new nodes): `el-context-rot`-adjacent material (the corpus records context rot across several batches; no dedicated node is coined here), `el-hybrid-search` **[b8]** and vector-RAG machinery referenced only as the losing baseline. Local-model nodes are **not** coined for Qwen or DeepSeek V4 Flash — see review note 4.

## Signals (5 new)

All: `SpottedInArtifact → ia-aie-druga-memory-harnesses`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-sakana-ai` except where noted.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-memory-adds-nothing-when-context-fits` | context | The negative result, reported first and unusually plainly: on a literature-review task where all papers and relevant context fit in the window, "the memory actually didn't add more capability — it was the same performance with memory and without, and it only added more cost." The test case was deliberately adversarial for retrieval (a retracted Nature claim about 742,000 discovered materials, where the retraction is a far smaller needle than the headlines and citations), and memory still bought nothing. A vendor-neutral finding that cuts against reflexive memory adoption | `ContradictsPattern → pat-agent-memory-layer` — **HELD PATTERN-LESS** (see review note 1) | `OnElement → el-memory-write-manage-read`, `el-recall-policy-ladder` |
| `sig-ranked-ledger-beats-vector-rag` | context | The positive result: on xbench long-horizon tasks — where the answer sits at step 124 and the question is asked at step 500, entirely outside the context window — a **ranked decisions ledger** beat vector RAG, no-recall, and a gated policy that just asks whether memory is needed. Across 68 questions with multiple cells and seeds, reproduced on two models and on Spider V2. The structure of *what* is stored and *how it is ranked* mattered more than retrieval sophistication | `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-decisions-ledger`, `el-recall-policy-ladder` |
| `sig-oracle-does-not-saturate` | context | The subtlest finding, and the one most useful to anyone building evaluations: even the **oracle** condition — handed the correct memory for every loop — does not reach maximum performance, "because the Oracle provides the right memory but doesn't force the model to use it. The model can get the right memory and still retrieve the wrong information, or choose to ignore it, or be confused." Retrieval quality therefore has a hard ceiling below perfect, and a measurable share of memory-system failure is *utilization* failure rather than retrieval failure. Ablations with arbitrary, wrong-step and most-recent-step memories all confirmed the ranked policy as best | `FormsPattern → pat-verification-gap` **[registry]** | `OnElement → el-recall-policy-ladder` |
| `sig-bad-memory-is-expensive` | context | The cost inversion: better recall was also **cheaper**. "Bad memory is expensive because it spends more tokens and it can send the agent the wrong way, but a good structural policy for recall can save you a lot of tokens and budget." Turns recall-policy design from a quality knob into a cost lever, and supplies the argument for the talk's ask — treat recall policy as a first-class metric you design and report rather than a library you install | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-recall-policy-as-metric`, `el-decisions-ledger` |
| `sig-local-models-cross-the-agentic-line` | infra | The enabling condition, and the sovereignty argument. Local models are now usable for agentic tool-use work — DeepSeek V4 Flash runs on an M3 Ultra, GLM is "on everyone's minds especially with Fable going away," RAM remains the bottleneck — and the whole study ran on one 96GB/28-core desktop in Tokyo, controlled from a phone, with household fans stacked around it. Corroborated externally by Coinbase reporting **lower AI spend with higher AI usage** after moving to local models plus routing, caching and context hygiene. The research payoff is stated as control: "I got to control the data, the entire traces of compute and evaluations — I see that as an example of sovereignty." Cost admitted: serial-only evaluation, no batch querying on DeepSeek V4 Flash | `FormsPattern → pat-sovereign-ai` **[registry]** | `OnElement → el-memory-write-manage-read`; `RelevantCompany → co-coinbase`, `co-sakana-ai` |

## Insights (2 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-memory-earns-its-keep-only-past-the-window` | The two headline results form a decision rule that most memory adoption skips: below the context window, memory is pure overhead — same accuracy, higher cost — and above it, the *policy* rather than the machinery decides the outcome. Teams reaching for a memory system should first establish which regime they are in, because the honest answer for a large share of production tasks is that the task fits and the memory layer is buying nothing but tokens. That framing also explains why memory benchmarks disagree so violently: they are sampling different sides of the same threshold | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** | `ReliesOnElement → el-recall-policy-ladder`, `el-memory-write-manage-read` |
| `ins-retrieval-ceiling-is-utilization` | An oracle that hands the model exactly the right memory and still misses the maximum relocates a chunk of the memory problem from retrieval to **use**: the model can hold the correct evidence and still ignore, misread or be confused by it. Any memory evaluation that stops at retrieval precision is therefore measuring the easier half, and any memory product claiming wins on recall metrics has not yet shown the wins survive to task outcome. The oracle condition is cheap to add and belongs in every memory evaluation as the ceiling estimate it turns out not to be | `HighlightsPattern → pat-verification-gap` **[registry]** | `ReliesOnElement → el-recall-policy-ladder`, `el-decisions-ledger` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-druga-memory-harnesses`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-ablate-a-memory-harness` | Ablate the recall policy before buying a memory system | Model memory as a **write-manage-read control loop** around the model rather than as a store, and separate the always-present core, the recall block and the cross-session archive so each can be varied independently; build over agents with no durable memory of their own so every memory effect is attributable to the harness; **first check whether your task fits in context**, because below that threshold memory reliably adds cost without adding capability, and the interesting regime only begins where the relevant evidence sits outside the window; then hold the model fixed and climb a recall-policy ladder — no recall, vector similarity, a **ranked decisions ledger**, and an oracle handed the ground truth — since this isolates policy from model quality; expect the ledger of decisions to beat similarity retrieval and to beat merely gating on "do I need memory," and expect it to be **cheaper**, because bad memory both burns tokens and misdirects the agent; always include the **oracle arm**, and treat the gap between oracle and maximum as your utilization failure rather than assuming perfect retrieval implies perfect outcomes; run ablations that feed arbitrary, wrong-step and merely-most-recent memories to confirm the policy is doing the work; and reproduce across at least two models and two benchmarks before believing the ranking | `ReferencesElement → el-recall-policy-ladder`, `el-decisions-ledger`, `el-memory-write-manage-read`, `el-recall-policy-as-metric` |

## Dropped

- **The METR convergence framing** (longer-horizon tasks trending up while model releases become less frequent, converging later this year to make context rot a priority) — motivation; folded into the file header rather than coined, and the METR curve is already represented in the corpus.
- **The overheating-Mac anecdote** (evaluations still running in Tokyo, controlled from a phone, husband adding fans, "we're running out of fans") — colour, though it is also the evidence for the serial-evaluation cost admitted in `sig-local-models-cross-the-agentic-line`.
- **The 30+ runnable memory cookbooks repository** — pointed at from the stage as evidence the technique landscape is rich (short-term, long-term, cognitive techniques, evaluation-driven), but the attribution is garbled to "Diamond" and unrecoverable; see review note 3.
- **The hiring pitch for Sakana in Japan** — logistics; the sovereignty framing it sits inside is kept.

## Review notes

1. **⚑ The batch's cleanest counter-evidence on memory, and it is deliberately unhomed.** `sig-memory-adds-nothing-when-context-fits` would be a `ContradictsPattern` edge on `pat-agent-memory-layer` if that pattern existed. It does not yet, so the signal is **held pattern-less with the intended edge recorded in the FormsPattern column** — if review coins the pattern this batch (recommended, see the Khemani file), this signal should be attached as a **counter-edge on day one**, which is exactly the shape a healthy pattern should have. Paired with Asawa's finding that vanilla in-context learning tops the continual-learning leaderboard, the batch supplies two independent, non-commercial results arguing that memory machinery is often unnecessary. Do not let the ten-talk track's weight bury them.
2. **Why this is the highest-evidence memory talk in the batch despite being the shortest.** It is the only one with a controlled design: model held fixed, one variable, an oracle ceiling arm, ablations against arbitrary/wrong/recent memories, 68 questions with multiple seeds, reproduced across two models and two benchmarks. Every other memory talk in the batch is a survey, an architecture description or a product. If the corpus needs one citable memory result, it is `sig-ranked-ledger-beats-vector-rag`.
3. **⚠ Unresolved attribution.** The open-source repository of "over 30 runnable cookbooks" is attributed to something the captions render as "Diamond." Not recoverable from the transcript and not coined. Worth finding before seeding — a curated memory-technique cookbook collection would be a legitimate corpus element.
4. **⚠ Verify before seeding.** "Qwen 27B quantized at 4-bit" is very likely **Qwen3 27B** but is stated only once; DeepSeek V4 Flash's M3 Ultra claim, the 96GB/28-core machine spec, the 68-question xbench run, and the Spider V2 reproduction are all single-mention and caption-sourced. No element nodes coined for the two local models, on the b16 restraint precedent — they are the substrate here, not the subject. Add-option if review prefers.
5. **`co-coinbase` coined on reference** (b2 `co-openai` precedent) to carry `sig-local-models-cross-the-agentic-line`'s external corroboration. It is the only third-party quantitative support in the talk, and the spend-down/usage-up direction makes it a genuinely useful `pat-sovereign-ai` data point independent of Sakana's own position.
6. **Cross-file link in this batch.** The decisions-ledger result rhymes with b17's Dailey/Ref "doc as state, agent as action" and Gazit/GitHub shared-plan-docs findings: in all three, a structured record of *decisions* outperforms undifferentiated history. Three independent arrivals at decision-records-as-memory across two batches is worth a note in any future coin brief; no edge emitted.
