# SPIKE extraction — "I've never seen anything scarier than an LLM with tool calls" (Erik Meijer) — FOR REVIEW

Source transcript: `transcripts/meijer-llm-tool-calls-scary.txt` (auto-captions — quotes are paraphrases, not verbatim; this transcript is heavily garbled, see Review notes).
Video: https://youtu.be/-CnA2lGfymY — AI Engineer World's Fair, published 2026-07-13.
`stagingTimestamp` for the artifact and all signals: 2026-07-13 (publish date).
Entities marked **[registry]** are already in the registry; **[this batch]** are defined in another file of this 5-talk batch.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-meijer-tool-calls-scary` | I've never seen anything scarier than an LLM with tool calls (Erik Meijer — AI Engineer World's Fair) | youtube | https://youtu.be/-CnA2lGfymY |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-erik-meijer`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-erik-meijer` | Erik Meijer (@HeadinTheBox; programming-language researcher — LINQ, Rx; notable individual) | — (introduced as "research scholar at Linet's Labs" — affiliation garbled in captions, unresolved; no `AffiliatedWithCompany` edge) |

Cited, not coined: Simon Willison (`exp-simon-willison` **[this batch]**, defined in `wu-shihipar-anthropic-culture.md`) — credited for the "lethal trifecta"; Geoff Huntley (`exp-geoff-huntley` **[registry]**) — cited for taint analysis on reified plans ("Jeff Huntley" in captions); Solomon Hykes — cited for "an AI agent is an LLM wrecking its environment in a loop", prose only.

## Companies (0 new)

- OpenAI tool-call launch referenced historically — `co-openai` **[registry]**, used as `RelevantCompany` below. Foundation-lab leaders (Dario/Daniela/Sam) appear as narrative characters only.

## Elements (3 new, 1 registry reuse)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-proof-carrying-agent-plans` | Proof-carrying agent plans | technology | security | Air-gap the agentic loop from the agent: instead of executing IO side effects while computing an answer, the model emits a reified program (a free-monad expression representing the plan) plus a machine-checkable proof of its safety; standard compiler machinery (type checking, data-flow and taint analysis, inductive interpreters) verifies the plan before a trusted executor runs it. A revival of 1990s proof-carrying code (Necula) aimed at agents; a reference implementation by academics (incl. Harvard collaborators) is on GitHub |
| `el-lean` | Lean theorem prover | framework | security | Interactive theorem prover / dependently-typed language, used in the talk to type LLM signatures (`IO` marking real-world mutation, propositions-as-types for safety proofs); currently the AI-safety-adjacent formal-methods tool VCs anchor on (peers: Isabelle, Rocq/Coq, PVS, TLA+) |
| `el-lethal-trifecta` | Lethal trifecta | concept | security | Simon Willison's name for the deadly combination that makes agents exploitable: access to private data + exposure to untrusted content (prompt injection) + tool-call ability; any mitigation must break at least one leg — Meijer's proposal breaks the tools leg by deferring execution behind verified plans |

Reused: `el-model-first-languages` **[registry]** — Meijer's closing argument is a direct instance: the plan language (free-monad expressions) is not designed for humans; a machine generates it, a machine consumes it, a machine proves it — "we should stop designing languages for humans."

Element edges: all three new elements `IdentifiedInArtifact → ia-aie-meijer-tool-calls-scary`; `el-proof-carrying-agent-plans` `UsesElement → el-lean`, `UsesElement → el-model-first-languages` **[registry]**, `EnablesPattern → pat-verification-gap` **[registry]**.

## Signals (3 new)

All: `SpottedInArtifact → ia-aie-meijer-tool-calls-scary`, `SourcedFromSource → source-aie-yt`.

| slug | domain | name / brief | FormsPattern | RelevantCompany |
|---|---|---|---|---|
| `sig-tool-calls-weaponized-safety-debate` | security | Dated inflection point (June 2023, OpenAI ships tool calls in GPT-4; all vendors copy per "principle of minimum differentiation"): a single `IO` in the type signature turned AI safety from a philosophical debate about offensive words into real-world danger — side effects (emptied bank account, deleted files) execute during the loop, before any "safe answer" arrives; alignment baked into weights is routinely jailbroken | `FormsPattern → pat-new-cyber-threats` **[registry]** | `RelevantCompany → co-openai` |
| `sig-lean-vc-frenzy` | security | Formal methods are suddenly venture-hot: per Meijer, VCs are "writing multi-billion-dollar checks if you just say you're doing something with Lean" — the verification gap is now being funded as an investment thesis, with Lean as the anchor brand over equally capable peers (Isabelle, Rocq, PVS, TLA+) | `FormsPattern → pat-verification-gap` **[registry]** | — |
| `sig-consumer-agents-unprotected` | security | The industry is at the point of handing the general public's computers, finances, and personal lives to AI agents with no protection layer in place — Meijer ("very sad and very scary") notes even conference practitioners routinely run agents with permissions bypassed ("yes, yes, yes"), and recounts Claude Code deleting one of his files mid-talk-prep the moment his attention waned | `FormsPattern → pat-new-cyber-threats` **[registry]** | — |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-verify-the-plan-not-the-answer` | "Safe answer" and "proper question" are not mathematical properties — which is exactly why 100+ LLM-as-judge startups exist. But a *plan* reified as a program IS formally checkable: defer execution, prove the plan (taint/data-flow analysis solves the lethal trifecta), then execute via a trusted runner. Provably safe agentic compute needs only programming-101 machinery — type systems and elementary compiler knowledge, not frontier research | `HighlightsPattern → pat-verification-gap` **[registry]** | `ReliesOnElement → el-proof-carrying-agent-plans`, `ReliesOnElement → el-lethal-trifecta` |
| `ins-agents-dangerous-until-proven-safe` | Inversion of the default trust posture: an agent should be treated as dangerous until proven safe — never allowed to act unless safety is provable — because a goal-directed model will do whatever closes the gap to its goal, files and databases included; guardrails-by-vibes (alignment + permission prompts) don't meet that bar | `HighlightsPattern → pat-new-cyber-threats` **[registry]** | `ReliesOnElement → el-proof-carrying-agent-plans` |

## KnowHow (1 new)

`SourcedFromArtifact → ia-aie-meijer-tool-calls-scary`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-airgap-agentic-execution` | Air-gap the agentic loop behind verified plans | Never let the model hold the tools: (1) have it return a reified program (free-monad expression) representing the plan instead of executing IO; (2) run static verification on that program — type checking, data-flow, taint analysis (breaks the lethal trifecta); (3) require a machine-checkable safety proof (models can generate the inductive proofs); (4) only then execute via a trusted interpreter; design the plan language for machines, not humans | `ReferencesElement → el-proof-carrying-agent-plans`, `ReferencesElement → el-model-first-languages` **[registry]**, `ReferencesElement → el-lean` |

## Dropped

- The Dafny intermediate example, "grind" tactic aside, monad/"free monet loves tie dice" jokes, Dutch-soccer left-left-right framing — pedagogical scaffolding for the same single idea, folded into `el-proof-carrying-agent-plans`.
- His jailbreaking of image models to generate "violent"/"drug" slide art — color (mild counter-evidence on content alignment, but anecdotal).
- SQL injection → prompt injection comparison ("a bigger problem than SQL injection ever was") — kept as prose flavor inside signal 1.
- Pope-blessing / Dario / Daniela / Sam / Bernie narrative characters — storytelling device.

## Review notes

1. **Worst captions of my 5-talk set.** Resolved garbles: "Eric Meyer" → Erik Meijer (official title/@HeadinTheBox); "deafne" → Dafny; "Isabel, Rock, PVS, TA Plus" → Isabelle, Rocq (Coq), PVS, TLA+; "free monet" → free monad; "Solomon Hikes" → Solomon Hykes; "Jeff Huntley" → Geoff Huntley (`exp-geoff-huntley` **[registry]**); "entropic" → Anthropic; "Simon Wilson" → Simon Willison. **Unresolved**: "Linet's Labs" (Meijer's stated affiliation — could not confidently reconstruct; no company node coined); "our friendly pit GL here" (recurring slide character, unresolved); "now that I'm in from Harvard" (some Harvard connection to the GitHub implementation — phrased cautiously in the element brief).
2. June 2023 / GPT-4 tool-call launch date matches the historical record (OpenAI function calling, June 2023) — the one externally verifiable date in the talk.
3. `sig-lean-vc-frenzy` ("multi-billion-dollar checks") is deliberately kept as Meijer's hyperbole-tinged testimony, not a market fact — phrased as "per Meijer".
4. `el-lean` is a decades-old tool (like batch-2's `el-semantic-layer` precedent) — kept as an Element because the VC-frenzy signal and the whole proof mechanism lean on it; drop to prose if only AI-native elements are wanted.
5. No new pattern coined here. Resonance note: proof-carrying plans + LLM-as-judge remark are strong mechanism-level evidence for `pat-verification-gap` (trust re-architected outside the model — here, literally into a type system).
