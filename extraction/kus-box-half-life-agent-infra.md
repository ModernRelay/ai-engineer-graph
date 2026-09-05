# SPIKE extraction — "The Half-Life of Agent Infrastructure" (Ben Kus, Box) — FOR REVIEW

Source transcript: `transcripts/kus-box-half-life-agent-infra.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/sM1iYgz93HI — AI Engineer World's Fair, published 2026-08-29.
`stagingTimestamp` for the artifact and all dated nodes: 2026-08-29 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Shape of the talk: Box's CTO (exabyte of content, tens of millions of users, ~1 trillion tokens heading to 10 trillion) argues that the classic enterprise advice — pick a stack, go deep, switch rarely — is wrong for AI: **the half-life of agent infrastructure is measured in months, not the 3–5 years of everything else.** He walks the ladder of "best approach at the moment" for models, agents and retrieval (each replaced within a year, including his own graph-based agent talk from last year's conference), and gives three moves: prepare people (change is not a mistake), build swappable abstractions with a six-month review and eval sets as the switching arbiter, and pick vendors by their change track record. Caption garbles: "Ben Kuss" → **Ben Kus**, "openi"/"open orthropic" → **OpenAI / Anthropic**, "codec" → **Codex**, "Opus 40 to Opus 45" → **Opus 4.0 → 4.5**, "Kaparthy" → **Karpathy**, "RM style agent" → ⚠ unclear (see note 4), "tic search" → ⚠ likely **agentic search**.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-kus-box-half-life-agent-infra` | The Half-Life of Agent Infrastructure (Ben Kus, Box — AI Engineer World's Fair) | youtube | https://youtu.be/sM1iYgz93HI |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-ben-kus`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-ben-kus` | Ben Kus (CTO, Box) | `AffiliatedWithCompany → co-box` **[seed]** |

## Companies (0 new)

Reused **[seed]**, edge-only: `co-box` — new facts: over an exabyte of content, tens of millions of users, hundreds of billions of files, ~1 trillion tokens processed and "probably 10 trillion soon"; rebuilt its agent approach repeatedly within a year (graph-based → looping/deep agent → …); has an agent abstraction that swaps the underlying approach without customer-visible change; reviews every AI technology choice every six months. Also reused: `co-anthropic` **[seed]** (Opus 4.0→4.5 named as the inflection), `co-openai` **[registry]** (Codex-style agent as the "one agent to rule them all" alternative), `co-google` **[registry]** (Gemini as frontier option).

## Elements (6 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-agent-infra-half-life` | The half-life of agent infrastructure | concept | infra | Classic infrastructure (databases, identity, multi-cloud storage) has a half-life of 3–5 years — "MySQL is still pretty good" — and switching is avoided because migrations always break something. AI infrastructure's half-life "is measured in months": a few months after adopting the best possible thing there is a significant chance you must replace it. It hurts engineers (what they just built is obsolete), startups (the first AI wave is being disrupted by the second), buyers ("good luck with a three-year deal") and VCs |
| `el-agent-approach-succession` | The approach ladder | concept | harness | Each rung was "arguably the leading approach for that moment": **models** — train your own → fine-tune → frontier API → open-weight self-hosted → bring-your-own-key → adaptive model selection; **agents** — single-shot LLM call → chain-of-thought → graph-based agent (Kus's own talk a year ago) → planning agent that figures out what to do → dedicated sub-agents → generic recursive agent with skills → agent with a code sandbox ("agents are great programmers; let them live in their own computer") → **bring your own harness**; **retrieval** — BM25/keyword → RAG embeddings/ANN ("mimics randomness as you keep going") → graphs ("difficult to get working well, probably not the best") → hybrid lexical+semantic with rank fusion → agentic search. Today's pick: adaptive models, a recursive skilled agent, agentic search over hybrid — "and it's going to change again" |
| `el-swappable-agent-abstraction` | Swappable agent abstraction | technology | harness | Box's agent abstraction lets the underlying approach be swapped — the customer's agent "still works the same but is better underneath." The structural answer to a months-long half-life: build so that what's underneath can change without a migration the customer sees |
| `el-six-month-review-cadence` | Six-month technology review | ops | infra | Box now reviews every AI technology choice every six months regardless of satisfaction — "this is great, we love it, review in six months" — where everything else is on a three-year cadence. Paired with the cultural rule "change is not a mistake: nobody knew six months ago, nobody today will know six months from now" |
| `el-eval-sets-decide-switching` | Eval sets as the switching arbiter | ops | harness | "Don't change because of a trend or a new paper." Define change: same inputs, expected outputs, graded on cost, speed, quality and capability — what the customer cares about. If the new approach beats the eval sets, strongly consider switching; if not, don't bother (or finish exploring). The CEO-forwarded-a-paper reflex is explicitly named as the thing this rule blocks |
| `el-vendor-change-track-record` | Vendor selection by change track record | concept | infra | Nobody can keep up with everything (Karpathy included), so you rely on platforms and vendors. Beyond current capability and roadmap, look at how they handled the last transitions — "many vendors I like have reinvented themselves three times in the last year; I now trust that if something else comes along they're very good at this." The evaluation shifts from *what they do now* to *how they change* |

Element edges: all six `IdentifiedInArtifact → ia-aie-kus-box-half-life-agent-infra`.
`el-agent-approach-succession` `UsesElement → el-model-routing` **[registry]**, `el-agent-skills` **[registry]**, `el-agentic-retrieval` **[registry]**, `el-hybrid-search` **[registry]**, `el-graphrag` **[registry]**;
`el-swappable-agent-abstraction` `UsesElement → el-agent-infra-half-life`;
`el-eval-sets-decide-switching` `UsesElement → el-golden-dataset` **[registry]**, `el-six-month-review-cadence`;
`el-swappable-agent-abstraction` `DevelopedByCompany → co-box` **[seed]**;
`el-agent-approach-succession` `ExemplifiesPattern → pat-harness-over-model` **[registry]**;
`el-eval-sets-decide-switching` `EnablesPattern → pat-benchmark-trust-crisis` **[registry]**;
`el-six-month-review-cadence` `ExemplifiesPattern → pat-ai-native-org` **[registry]**.

Reused elements (no new nodes): `el-model-routing` **[registry]** ("adaptive model selection" as the current rung), `el-agent-skills` **[registry]**, `el-agentic-retrieval` **[registry]**, `el-hybrid-search` **[registry]**, `el-graphrag` **[registry]**, `el-golden-dataset` **[registry]** (the eval-set discipline), `el-claude-code` **[registry]** / `el-codex` **[registry]** (the "one agent to rule them all" enterprise choice).

## Signals (5 new)

All: `SpottedInArtifact → ia-aie-kus-box-half-life-agent-infra`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-box` **[seed]**.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-agent-infra-half-life-measured-in-months` | infra | The CTO of an exabyte-scale enterprise vendor: the generic advice that carried every prior platform shift — pick a technology, get good at it, switch rarely — "is not good advice right now," because other than generative AI existing, most things that power it are changing dramatically. Classic infra half-life is 3–5 years; agent infra's is months. Box rebuilt its agent approach repeatedly within a year (his own graph-based-agent conference talk was obsolete within months), at real morale cost — "it's a leadership problem, a technology problem, a team problem, and if you're not careful it can destroy you" | `FormsPattern → pat-ai-native-org` **[registry]** | `OnElement → el-agent-infra-half-life`, `el-agent-approach-succession` |
| `sig-opus-45-began-the-agent-model-epoch` | inference | Kus names one model change as the pivot of the last year: "Opus 4.0 to Opus 4.5 — suddenly you got a model that could do instruction following at really high scale; to me the beginning of the epoch of the new agent models." A senior enterprise builder attributing the approach-ladder's latest rungs (planning agents, recursive agents) to a model capability step rather than to harness work — a measured counter to the corpus's harness-first consensus | `ContradictsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-agent-approach-succession` |
| `sig-agentic-search-displaces-hybrid-and-graphs` | context | The retrieval rungs from the inside: embeddings/ANN "doesn't really scale well and almost mimics randomness as you keep going"; graphs are "difficult to get working well, probably not the best"; hybrid lexical+semantic with rank fusion was the answer until "agents are actually way better at finding data because they can apply their intelligence to get to it." Box's current pick is agentic search powered by hybrid — an exabyte-scale content company demoting graph retrieval | `ContradictsPattern → pat-context-graphs` **[registry]** | `OnElement → el-agentic-retrieval` **[registry]**, `el-hybrid-search` **[registry]**, `el-graphrag` **[registry]** |
| `sig-bring-your-own-harness-is-the-current-rung` | harness | The agent ladder's latest rung is to stop building the agent at all: "don't even bother — bring your own harness, let people select which system they want," alongside enterprises deciding between one agent to rule them all (Claude- or Codex-style) and agents from multiple platforms. Together with adaptive model selection, the unit of enterprise choice has moved from the model to the harness — and a vendor's job is to accommodate whichever harness arrives | `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-agent-approach-succession`, `el-swappable-agent-abstraction`, `el-model-routing` **[registry]** |
| `sig-eval-sets-not-trends-decide-switching` | harness | The operating rule for surviving a months-long half-life: build an abstraction so what's underneath can swap; review every choice every six months "no matter what"; and switch only when your own eval sets — same input, expected output, graded on cost/speed/quality/capability — say the new approach is better, never because of a paper or a trend. Private eval sets as the only trustworthy switching signal; vendors judged by how they handled their last three reinventions | `FormsPattern → pat-benchmark-trust-crisis` **[registry]**; `FormsPattern → pat-ai-native-org` **[registry]** | `OnElement → el-eval-sets-decide-switching`, `el-six-month-review-cadence`, `el-vendor-change-track-record` |

## Insights (2 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-adaptability-is-the-moat-until-it-isnt` | The durable claim is organizational: when the best approach is replaced every few months, the competitive asset is not the approach but the capacity to swap it — prepared people, a swappable abstraction, a fixed review cadence, and eval sets that decide. "The company that will dominate tomorrow is being born today, and its technology approach will change multiple times before it does." Build-for-change "is arguably the moat — until that changes" | `HighlightsPattern → pat-ai-native-org` **[registry]** | `ReliesOnElement → el-agent-infra-half-life`, `el-swappable-agent-abstraction`, `el-six-month-review-cadence`, `el-eval-sets-decide-switching` |
| `ins-the-approach-ladder-is-the-harness-story-told-honestly` | Read end-to-end, the ladder is the corpus's harness thesis with dates attached: model choice became routing, agent design became "bring your own harness," retrieval became an agent's job — every rung moved intelligence out of a fixed structure and into a swappable one. But the ladder also carries its own counter: Kus dates the epoch to a *model* step (Opus 4.5), which keeps `pat-model-not-bottleneck` honestly contested from a source with no stake in either side | `HighlightsPattern → pat-harness-over-model` **[registry]** | `ReliesOnElement → el-agent-approach-succession`, `el-vendor-change-track-record` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-kus-box-half-life-agent-infra`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-build-for-a-months-long-half-life` | Three moves for infrastructure that expires in months | **Prepare people**: tell AI teams to expect change as normal — "change is not a mistake; nobody knew six months ago" — and say it repeatedly, because the rebuild-what-you-just-shipped conversation is a morale and leadership problem before it is a technical one; **build to swap**: put an abstraction over the agent/model/retrieval approach so the customer-facing behavior stays stable while what's underneath changes, and review every AI choice every six months regardless of satisfaction; **define change by evals, not trends**: keep eval sets (same input, expected output, graded on cost, speed, quality, capability) and switch only when a new approach beats them — never because of a paper, a demo, or the CEO's link; and **choose vendors by change track record**: beyond roadmap, ask how they handled the last transitions — those that have reinvented themselves repeatedly are the ones to trust with the next one | `ReferencesElement → el-agent-infra-half-life`, `el-swappable-agent-abstraction`, `el-six-month-review-cadence`, `el-eval-sets-decide-switching`, `el-vendor-change-track-record` |

## Dropped

- **The career retrospective** (internet → mobile → cloud → AI; two startups, IBM and Box acquisitions) — motivation only.
- **The engineer-rebuild anecdote** ("we ship Tuesday; Wednesday we rebuild") — folded into `sig-agent-infra-half-life-measured-in-months`.
- **Box booth / unstructured-content pitch** — nothing to extract.

## Review notes

1. **⚑ Held pattern-less in spirit: the half-life thesis is `pat-liquid-software` evidence.** `sig-agent-infra-half-life-measured-in-months` is edged to `pat-ai-native-org` (the organizational response) but the core claim — approaches dissolving and regenerating on a months-long cycle, adaptability as the asset — is the uncoined `pat-liquid-software` framing from a CTO-level source. Recommend adding to that ledger; coin decision unchanged.
2. **Two healthy counters from a neutral source.** `sig-opus-45-began-the-agent-model-epoch` → `ContradictsPattern pat-model-not-bottleneck` (the epoch is dated to a model step) and `sig-agentic-search-displaces-hybrid-and-graphs` → `ContradictsPattern pat-context-graphs` (graphs demoted at exabyte scale). Both are calibrated, not polemical; keep as counter-edges.
3. **`sig-eval-sets-not-trends-decide-switching` → `pat-benchmark-trust-crisis`** is a widening: private eval sets as the only trustworthy signal for *infrastructure* decisions, not just model claims. Review may prefer `pat-verification-gap`.
4. **⚠ Verify before seeding:** "RM style agent" (possibly "Ralph-loop"/"recursive" — the corpus has `el-ralph-loop`), "tic search" (agentic search), the token figures (~1T → 10T), and that the graph-based-agent talk was at the 2025 World's Fair.
