# SPIKE extraction — "Your Agent Failed in Prod. Good Luck Reproducing It." (Tisha Chawla & Susheem Koul, Microsoft) — FOR REVIEW

Source transcript: `transcripts/chawla-koul-microsoft-agent-failed-prod.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/Lc8zRh9muoY — AI Engineer World's Fair, published 2026-06-29.
`stagingTimestamp` for the artifact and all signals: 2026-06-29 (publish date).
Entities marked **[registry]** are already in the shared registry — edges link to them, no new node defined here.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-chawla-koul-agent-failed-prod` | Your Agent Failed in Prod. Good Luck Reproducing It. (Tisha Chawla & Susheem Koul, Microsoft — AI Engineer World's Fair) | youtube | https://youtu.be/Lc8zRh9muoY |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-tisha-chawla`; `ContributedByExpert → exp-susheem-koul`.

## Experts (2 new)

| slug | name | edges |
|---|---|---|
| `exp-tisha-chawla` | Tisha Chawla (Microsoft; runs agents against real production backends) | `AffiliatedWithCompany → co-microsoft` **[registry]** |
| `exp-susheem-koul` | Susheem Koul (Microsoft; co-presenter — demos the Chronicle record/replay PoC) | `AffiliatedWithCompany → co-microsoft` **[registry]** |

## Companies (0 new)

- **[registry]** `co-microsoft` — reused.

## Elements (2 new, 1 reused)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-chronicle` | Chronicle | framework | harness | Proof-of-concept record/replay framework for agents built by the speakers: a `boundary` annotation wraps any node (tool call, LLM call, RAG retrieval) and records its input/output pair plus frozen run state (model version, code/build version, sampling params) as a trace; replay mode stubs every node except the one under test, turning any recorded production failure into a rerunnable, zero-model-call test case with assertions |
| `el-inference-nondeterminism` | LLM inference non-determinism | concept | inference | Why temperature 0 ≠ reproducibility on hosted APIs: greedy sampling fixes only the argmax, not the underlying scores; floating-point non-associativity means operation ordering shifts logits and can flip the winning token; the real culprit is batch variance — a request is grouped with whatever traffic co-arrives that millisecond (a lone matmul is bit-stable); MoE expert-capacity limits reroute tokens depending on co-batched traffic. Identical prompts can yield dozens of distinct outputs over 1,000 runs |
| **[registry]** `el-agent-checkpoint-replay` | — | — | — | reused; Chronicle is a concrete instance of checkpoint-and-replay (record at boundaries → replay with stubs/modifications → assert against the recorded baseline) |

Element edges: `el-chronicle` and `el-inference-nondeterminism` `IdentifiedInArtifact → ia-aie-chawla-koul-agent-failed-prod`; `el-agent-checkpoint-replay` `IdentifiedInArtifact → ia-aie-chawla-koul-agent-failed-prod`; `el-chronicle` `UsesElement → el-agent-checkpoint-replay`; `el-chronicle` `DevelopedByCompany → co-microsoft` (⚠ see Review notes); `el-chronicle` `ExemplifiesPattern → pat-harness-over-model` **[registry]**.

## Signals (4 new)

All: `SpottedInArtifact → ia-aie-chawla-koul-agent-failed-prod`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-prod-agent-failure-unreproducible` | harness | Microsoft production-agent practitioners: the standard reflex after a prod agent failure — pull the raw prompt from telemetry, rerun locally on the same model — passes, ten out of ten times, while the one run that cost you stays unreproducible. Can't reproduce → can't debug → can't promise it won't hit the next customer | `FormsPattern → pat-verification-gap` **[registry]** | `RelevantCompany → co-microsoft` |
| `sig-clean-200-wrong-trade` | harness | Failure anatomy (illustrative broker-API scenario): user asks to sell $1,000 of stock; the agent drops the raw 1,000 into the quantity field and sells 1,000 shares at ~$190 — a ~$190K wrong action that returns a clean 200 OK in 30 ms. Zero exceptions, zero alerts, dashboards perfectly green: semantically wrong agent actions are invisible to conventional monitoring | `FormsPattern → pat-verification-gap` **[registry]** | — |
| `sig-temperature-zero-myth` | inference | Teams burn weeks trying to force determinism via temperature 0 and "walk away deciding the system is unknowable" (paraphrase); hard data from engineering threads (Reddit/HN) shows the same prompt at temp 0 still returns dozens of different responses across a thousand runs — GPU non-determinism, batch variance, and MoE routing make bitwise determinism unobtainable from hosted APIs | `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-inference-nondeterminism` |
| `sig-chronicle-replay-ci` | harness | Microsoft PoC Chronicle demonstrates boundary-recorded replay end to end: a recorded haywire trading run is replayed with the LLM node stubbed from the trace and the newly guardrailed tool live; an assertion verifies the bad order now blocks — the production failure becomes a free, deterministic CI test with zero model calls | `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-chronicle`; `RelevantCompany → co-microsoft` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-replayability-not-determinism` | The wrong question is "how do I make the model deterministic"; the right one is "how do I debug and retest a run I can't reproduce." Bitwise determinism is controllability — unobtainable from hosted APIs and undesirable, since sampling variation is what makes the model good; replayability is observability — re-validating a run that already happened, well enough to debug it. Don't freeze the model; capture what it did. You need the same state transition, not the same token | `HighlightsPattern → pat-harness-over-model` | `ReliesOnElement → el-agent-checkpoint-replay` **[registry]**, `ReliesOnElement → el-inference-nondeterminism` |
| `ins-two-test-planes` | Agent testing splits into two complementary planes: deterministic testing of the deterministic nodes (guardrails, tool calls) via frozen-trace stubbing — rerunnable and free because it never calls the model; and behavioral testing of subjective properties (tone, trajectory) where LLM-as-judge techniques belong. Trace stubbing "kicks the probability out of the window" (paraphrase) for the first plane | `HighlightsPattern → pat-verification-gap` | `ReliesOnElement → el-chronicle` |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-chawla-koul-agent-failed-prod`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-record-at-the-boundary` | Record agent runs at node boundaries, not the network layer | Network capture misses half the agent (local retrieval, in-process tools, memory) and shreds under streaming/async; wrap each node (tool / LLM / retrieval) and record what enters and leaves it — the meaning of each step, not the packets; know and log your session variables (LLM version, build ID, RAG chunks, sampling params); capture the full envelope, not just the prompt | `ReferencesElement → el-chronicle`, `ReferencesElement → el-agent-checkpoint-replay` **[registry]** |
| `how-replay-as-test-case` | Run the loop: annotate → record → visualize → understand → fix → replay → verify | Replay the recorded trace with every node stubbed except the one you changed (fix at the tool/guardrail layer — you cannot control the LLM); assert on the changed node's output; keep the trace as a permanent regression test in CI; and keep generation-time variation alive — don't pin temperature to zero, "that is what brings the agency into your agent" (paraphrase) | `ReferencesElement → el-chronicle` |

## Dropped

- "Boundary" as a separate element — captions oscillate between Chronicle (the system) and Boundary (the annotation / replay engine, "another tenet that Boundary offers"); modeled as one system, `el-chronicle`, with the boundary annotation as its mechanism. Flagged below.
- LLM-as-judge as an element — named only as the right tool for the behavioral test plane; prose in `ins-two-test-planes`.
- Reddit / Hacker News determinism threads — corroborating references, kept in `sig-temperature-zero-myth` prose.

## Review notes

1. **Co-presenter name garble:** captions say "I have Sachin with me as my co-presenter"; the official listing credits Susheem Koul — coined `exp-susheem-koul` from the official name and flagged the garble. No relation to registry `exp-sachin-gupta`.
2. **`el-chronicle` `DevelopedByCompany → co-microsoft` is a judgment call:** presented as "what we have done is we have built something called Chronicle" by two Microsoft engineers, with a QR to public code — possibly a personal OSS PoC rather than an official Microsoft product. Drop the edge at reconciliation if corporate attribution should be stricter.
3. **Chronicle vs Boundary naming:** the demo also uses "Boundary" as if a product ("enabled the replay mode on Boundary", "let Boundary handle the rest"). If the real project name turns out to be Boundary (or two components), rename/split `el-chronicle` before seeding — verify against the video/QR repo.
4. **Pattern ledger (no coin):** per instructions, this talk adds evidence to the UNCOINED `pat-durable-execution` candidate from the debugging side — boundary-recorded traces plus stubbed deterministic replay is the same record/replay machinery durable-execution runtimes are built on, framed here as "a core tenet of productionizing any AI agent" (paraphrase). Noted without edges; signals parked on `pat-harness-over-model` / `pat-verification-gap`.
5. The $190K example is an illustrative scenario ("the scenario I'm taking"), not a disclosed Microsoft incident — `sig-clean-200-wrong-trade` phrased accordingly, no RelevantCompany edge. Captions call the stock both "Intel" and "Acme" (the demo uses Acme); the transcript's own arithmetic is kept as told.
