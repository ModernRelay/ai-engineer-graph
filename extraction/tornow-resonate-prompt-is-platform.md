# SPIKE extraction — "The Prompt is the Platform" (Dominik Tornow, Resonate HQ) — FOR REVIEW

Source transcript: `transcripts/tornow-resonate-prompt-is-platform.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/DqtmZE6Hl0g — AI Engineer World's Fair, published 2026-06-29.
`stagingTimestamp` for the artifact, all signals, and knowhow: 2026-06-29 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-tornow-prompt-is-platform` | The Prompt is the Platform (Dominik Tornow, Resonate HQ — AI Engineer World's Fair) | youtube | https://youtu.be/DqtmZE6Hl0g |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-dominik-tornow`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-dominik-tornow` | Dominik Tornow (founder & CEO, Resonate; distributed-systems and agentic-engineering practitioner) | `AffiliatedWithCompany → co-resonate` |

## Companies (2 new)

| slug | name | type | note |
|---|---|---|---|
| `co-resonate` | Resonate (Resonate HQ) | developer | durable-execution platform built on minimalism/simplicity: reference server + SDKs for TypeScript, Python, Rust, Go, Java; repositioning the specification/protocol as the product |
| `co-synadia` | Synadia | developer | company behind NATS.io; Resonate infrastructure partner for a NATS-native durable-execution implementation |

## Elements (3 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-resonate` | Resonate | product | infra | Durable-execution platform whose protocol was shrunk over ~3 years to two core objects — a durable promise and a durable task ("what can we take away?" as method); reference server plus polyglot SDKs; now recast so the spec is the product and target-native servers are derived from it |
| `el-nats` | NATS.io | technology | infra | Open-source messaging system for distributed systems (queues, versioned key-value store, delayed/scheduled messages); the target platform of the case study — including legal-but-inconvenient consistency behavior (stale reads at old versions, optimistic-concurrency write rejections) a derived implementation must stay correct under |
| `el-deterministic-simulation` | Deterministic simulation testing | technology | harness | Simulated target environment (here: a Python simulation of NATS' versioned KV store) with deterministic randomness injecting legal failure behaviors (stale reads, failed compare-and-set writes), full reproducibility of any failing execution, fuzz testing, and trace events exposing "forbidden fruit" — facts production hides (whether a read was fresh or stale, the latest value the algorithm missed) that the algorithm may not use but the agent may, turning failures into visible cause-and-effect |

Element edges: `el-resonate` `DevelopedByCompany → co-resonate`; `el-nats` `DevelopedByCompany → co-synadia`; all three `IdentifiedInArtifact → ia-aie-tornow-prompt-is-platform`.

## Signals (4 new)

All: `SpottedInArtifact → ia-aie-tornow-prompt-is-platform`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | domain | FormsPattern | OnElement | RelevantCompany |
|---|---|---|---|---|---|
| `sig-platform-retirement-prediction` | Opening claim: in 2026, coding agents will quietly retire their first software platform — not because it's bad, because it's unnecessary. General-purpose implementations get replaced by bespoke implementations generated on demand, not as a new library/framework/platform but as a minimal extension of infrastructure already in place | infra | `FormsPattern → pat-saaspocalypse` | — | — |
| `sig-resonate-spec-as-product` | Dated vendor repositioning: Resonate — a durable-execution vendor with a server and five SDK implementations — declares its value has moved from implementation to specification: the protocol is the product, and multiple target-native servers are to be repeatedly synthesized from the one spec (reference implementation + partner-native ones), starting with NATS.io via a Synadia partnership | infra | `FormsPattern → pat-saaspocalypse` | `OnElement → el-resonate` | `co-resonate`, `co-synadia` |
| `sig-abstract-spec-agent-failure` | Experiment result: an agent asked to build a Resonate server in Rust on Postgres straight from the abstract spec produced a happy-path prototype — it passed the basic tests but broke on concurrency, process failure, and network failure. Inserting a human-driven *concrete specification* (schema, indices, SQL, transaction boundaries) got the agent to a production implementation — but the agent still couldn't help design | harness | `FormsPattern → pat-verification-gap` | — | `co-resonate` |
| `sig-dst-agent-designs` | With a deterministic simulator plus forbidden-fruit traces, the agent moved upstream on the NATS build: it produced a fuzz-verified proof-of-concept in simulation (discovering the correct algorithm under stale reads/partial failure), derived the concrete specification from it, then the production implementation — agent as design driver, humans still in the loop | harness | `FormsPattern → pat-verification-gap` | `OnElement → el-deterministic-simulation` | `co-resonate` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-spec-is-the-product` | If implementations become generatable on demand, reuse moves upstream: the durable asset is the specification/protocol, and the competitive question flips from "can we build a server?" to "can we repeatedly synthesize trusted servers from the same specification?" Corollary: the abstract spec must shed every target assumption — no schema, no indices, not even relational-vs-KV or weak-vs-strong consistency; only implementations are concrete | `HighlightsPattern → pat-saaspocalypse` | `ReliesOnElement → el-resonate` |
| `ins-simulation-is-executable-design` | Agents fail at design when abstract-spec-to-concrete-target is one jump; a simulated implementation is *executable design* — a place to discover correct algorithms under partial order and partial failure, where feedback is immediate, unambiguous, deterministic, and causally annotated ("the invariant broke because the algorithm decided from a stale view"). Verification tooling is what promotes agents from builders to designers | `HighlightsPattern → pat-verification-gap` | `ReliesOnElement → el-deterministic-simulation` |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-tornow-prompt-is-platform`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-spec-sim-spec-impl-pipeline` | Synthesize platforms via spec → simulation → spec → implementation | Never ask the agent to jump abstract-spec → concrete-implementation in one step. Pipeline: (1) abstract specification free of any target assumption; (2) simulated implementation as executable design — discover and fuzz-verify the algorithm under injected failures; (3) concrete specification making target decisions explicit (data schema, indices, queries, transaction boundaries) — write it only once the algorithm is known correct; (4) concrete implementation. Precondition: spend the effort making the protocol smaller and simpler first ("what can we take away? what abstraction can we erase?") — minimalism is the finish line, not the starting point | `ReferencesElement → el-resonate`, `ReferencesElement → el-deterministic-simulation` |
| `how-forbidden-fruit-traces` | Expose in simulation what production hides | Simulate the target's consistency model faithfully (versioned KV, deterministic stale-read injection, optimistic-concurrency write rejection). Emit trace events carrying forbidden facts: whether each read was fresh or stale, and the latest value the algorithm missed. Forbid the algorithm from depending on them; let the agent use them to explain *why* its algorithm was wrong. Keep runs deterministic and replayable so the agent repairs against the exact failing execution | `ReferencesElement → el-deterministic-simulation` |

## Dropped

- SDK language list and Discord CTA — folded into company brief / omitted.
- The foo/bar/baz versioned-KV walkthrough — folded into `el-nats` and the knowhow.
- "Two ingredients: minimalism and simplicity" — folded into `how-spec-sim-spec-impl-pipeline` as the precondition guideline.

## Review notes

1. **`pat-durable-execution` candidate (per instructions: noted, NOT coined, no edges):** this talk adds evidence — Resonate is another durable-execution vendor alongside Inngest / ZenML Kitaru / Agency in the candidate ledger, and its partner strategy ("durable execution right on top of their existing infrastructure with minimal additional dependencies", NATS-native via Synadia) is a distinct data point: durable execution being pushed down into infrastructure as a native layer rather than sold as a standalone platform. Counterweight: the talk's own thesis is that standalone platforms get retired by on-demand synthesis — read both ways at coin time.
2. **`pat-adaptive-software` / `pat-adaptive-harness` candidate (batch7 pair — noted, NOT coined):** "bespoke implementations generated on demand… reuse moves upstream to the specification… the prompt is the platform" reads as a third independent data point (after ten Teije's stem-and-divergences and Chandegra's harness-as-runtime-output), at the infrastructure layer. If that pattern is coined, `sig-platform-retirement-prediction` and `sig-resonate-spec-as-product` are the ones to rehome off `pat-saaspocalypse`.
3. Caption garbles: "Dominic Tornow" → Dominik Tornow (official title); "Natero" / "Nuts IO" → NATS.io; "Synadia" spelled correctly once — verify.
4. Deterministic simulation testing is an established industry technique (FoundationDB/Antithesis lineage); `el-deterministic-simulation` is coined generically, with the brief describing this talk's instantiation — not as a Resonate product.
5. `sig-platform-retirement-prediction` names no specific platform (rhetorical opener restated as the working theory); kept as a prediction-signal — demote to prose if the signal bar requires a falsifiable dated fact.
