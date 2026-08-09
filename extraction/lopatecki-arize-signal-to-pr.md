# SPIKE extraction — "From Signal to PR: Anatomy of a Self-Improving Agent" (Jason Lopatecki, Arize) — FOR REVIEW

Source transcript: `transcripts/lopatecki-arize-signal-to-pr.txt` (auto-captions — quotes are paraphrases, not verbatim; heavy garbles: "Arise"→Arize, "cloud code"/"clouded session"→Claude Code, "Tanthropic"→Anthropic, "element as a judge"/"elements a judge"→LLM as a judge, "SR"→SRE, "AX"→Arize AX).
Video: https://youtu.be/9HbzAWnKbo4 — AI Engineer World's Fair (evals track), published 2026-07-24.
`stagingTimestamp` for the artifact, all signals, and knowhow: 2026-07-24 (publish date).
Entities marked **[registry]** already exist — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-lopatecki-signal-to-pr` | From Signal to PR: Anatomy of a Self-Improving Agent (Jason Lopatecki, Arize — AI Engineer World's Fair) | youtube | https://youtu.be/9HbzAWnKbo4 |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-jason-lopatecki`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-jason-lopatecki` | Jason Lopatecki (co-founder/CEO, Arize; self-described builder — personally builds the agents he demos, shipped Arize's first in-product agent ~2 years ago) | `AffiliatedWithCompany → co-arize` **[registry]** |

## Companies (0 new)

| slug | name | status |
|---|---|---|
| `co-arize` | Arize | **[registry, batch 8]** — reused; no new node. Speaker's company; ships AX (SaaS, VPC-deployable), Phoenix (open source), Signal (agent) |
| `co-anthropic` | Anthropic | **[registry, seed]** — reused; named as the managed-agent/sandbox option enterprises refuse to route production data to |
| `co-uber` | Uber | **[registry, batch 3]** — reused; named as a VPC-install customer |

## Elements (4 new, 4 reused)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-arize-signal` | Arize Signal | product | harness | Long-running background agent that turns production telemetry into a code fix: triggered on a schedule or on an error event, it pulls traces/logs/eval values through observability skills, lands the evidence as files in the repo next to the code, and opens a GitHub issue or PR. Fully open-box configuration — you pick the coding harness (Claude Code), the sandbox (Arize sandboxes, Anthropic managed agents, Daytona), the skills, and the driving prompt ("don't be aggressive", "look for security issues"); findings can be converted into an evaluator or added to a dataset. Ships in the AX SaaS platform (also VPC-deployable); shared entity — also the launch vehicle for agent-as-a-judge in `dhinakaran-arize-agent-as-judge.md` |
| `el-arize-alex` | Alex (Arize in-product agent) | product | harness | Arize's in-UI assistant agent, first shipped ~2 years ago ("our first version frankly sucked"); long memory, dynamically generated UI per interaction, search across very large trace volumes. Doubles as the company's own failure-mode laboratory — its dogfooded failures (forgetting context, not knowing when a task is done, looping on the same tool call) are the stated origin of both Signal and agent-as-a-judge. Shared entity — also referenced in `dhinakaran-arize-agent-as-judge.md` |
| `el-observability-skills` | Observability skills (agent-facing) | concept | harness | Skill surface that connects a coding agent to an observability platform, designed around what the *agent* needs rather than what a dashboard shows: scope the query (all traces for a session/cohort), pull the slice down as temp **files inside the repo** — "these harnesses are magical with files", 10 MB files sitting in the repo are fine — and expose composable per-tool affordances (Pyroscope memory-issue facets, cohort-by-customer) so the agent can chain its own investigation. Load-bearing claim: the differentiator is skill design, not pointing a coding agent at raw data |
| `el-continuous-fix-loop` | Continuous fix loop (signal → PR) | concept | harness | The inverted incident loop: trigger (periodic or error event) → context gathering via skills (traces, logs, eval aggregates, repo code path) → sandboxed coding harness → issue/PR with evidence attached, before any human has looked. Local-first development path — get it working on your laptop with your coding agent, then move the identical loop into a triggered sandbox. Reframes the human role from responder to reviewer/driver; the deliverable is a *cold start* with deep evidence, not necessarily an autonomous fix. ⚠ merge-adjacent to `el-prod-to-code` **[registry, batch 3]** and `el-agentic-vuln-pipeline` **[registry, batch 3]** — see review note 3 |
| `el-agent-skills` **[registry]** | Agent skills | — | — | reused — the composable unit the loop is built from; Arize pre-bakes skills and lets customers add their own |
| `el-claude-code` **[registry]** | Claude Code | — | — | reused — named as the default harness Signal runs ("this one's cloud code"); sessions are resumable locally |
| `el-anthropic-managed-agents` **[registry, seed]** | Anthropic managed agents | — | — | reused — offered as one sandbox backend alongside Arize's own; the option enterprises decline for production-data reasons |
| `el-arize-phoenix` **[registry, batch 8]** | Arize Phoenix | — | — | reused — named as the open-source on-ramp ("if you just want to start tomorrow"); Signal itself is AX-only |
| `el-prod-to-code` **[registry, batch 3]** | Prod-to-code runtime context | — | — | reused — the HUD element states the same primitive (production observability translated to the level a coding agent reasons at); Arize's skills-plus-files mechanism is a second independent implementation |

Element edges: all four new `IdentifiedInArtifact → ia-aie-lopatecki-signal-to-pr`; `el-arize-signal` and `el-arize-alex` `DevelopedByCompany → co-arize` **[registry]**; `el-arize-signal` `UsesElement → el-observability-skills`, `UsesElement → el-claude-code` **[registry]**, `UsesElement → el-anthropic-managed-agents` **[registry]**, `ExemplifiesPattern → pat-verification-gap` **[registry]**; `el-observability-skills` `UsesElement → el-agent-skills` **[registry]**; `el-observability-skills` `EnablesElement → el-continuous-fix-loop`; `el-continuous-fix-loop` `UsesElement → el-prod-to-code` **[registry]**; `el-continuous-fix-loop` `EnablesPattern → pat-verification-gap` **[registry]**; `el-arize-alex` `EnablesElement → el-arize-signal` (dogfood → product lineage).

## Signals (5 new)

All: `SpottedInArtifact → ia-aie-lopatecki-signal-to-pr`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | domain | name / brief | pattern edge | other edges |
|---|---|---|---|---|
| `sig-arize-signal-launch` | harness | Arize ships Signal: a background agent running continuously against production traces that puts up issues and one-to-two-line PRs on its own, hooked to the customer's GitHub repo, with harness/sandbox/skills/prompt all user-selectable and findings convertible into evaluators or datasets. Available in the AX SaaS platform (VPC-deployable); demoed against a financial-trading agent | `FormsPattern → pat-verification-gap` **[registry]** | `OnElement → el-arize-signal`, `el-continuous-fix-loop`; `RelevantCompany → co-arize` **[registry]** |
| `sig-observability-consumer-flips-to-agents` | harness | Observability's consumer is flipping from humans to agents: "observability used to be for humans — a UI you click, a graph you click"; 2.0 is coding agents plus skills for Pyroscope/Google Cloud, and telemetry is reframed as "smoke thrown off your system" that tells an agent which code path ran (without it, "there's a million paths it could have taken"). Vendor claim: observability platforms are becoming tied to the *fix*, not just the signal | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-observability-skills`, `el-prod-to-code` **[registry]**; `RelevantCompany → co-arize` **[registry]** |
| `sig-instrument-10x-for-agents` | harness | The instrumentation economics invert once agents are the reader: teams under-logged because "humans can't dig through all the logs, it's just noise"; the stated direction is tracing and logging 10× — "orders and orders of magnitude more than we do today", potentially every inch of the software — specifically so continuous loops can reconstruct the executed path and fix it | `FormsPattern → pat-verification-gap` **[registry]** | `OnElement → el-continuous-fix-loop` |
| `sig-bottleneck-is-confidence-not-fix` | harness | Practitioner claim from a vendor dogfooding its own loop: "the bottleneck is actually not the fix anymore" — with coding agents plus skills the scarce thing is confidence that this is the right fix to push. Consequence: "you can build at agent speed, but today you can't improve your systems at agent speed" — a governor sitting on the whole product loop | `FormsPattern → pat-verification-gap` **[registry]** | `OnElement → el-continuous-fix-loop`; `RelevantCompany → co-arize` **[registry]** |
| `sig-vpc-sandbox-boundary` | infra | Enterprise data-boundary observation: large customers (Uber, Booking.com named) "don't want to connect their production systems to Anthropic" and will not send database connections out, but are comfortable installing a vendor appliance into their own VPC — which is why the sandbox layer is sold pluggably (Arize sandboxes vs Anthropic managed agents vs Daytona) rather than as a single hosted backend | `FormsPattern → pat-sovereign-ai` **[registry, seed]** | `OnElement → el-anthropic-managed-agents` **[registry]**, `el-arize-signal`; `RelevantCompany → co-anthropic` **[registry]**, `co-uber` **[registry]**, `co-arize` **[registry]** |

## Insights (2 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-responder-to-reviewer` | Invert the incident loop and the human's job changes shape: instead of a person spotting an issue and an agent fixing it, the agent investigates before anyone looks, so you "wake up with an idea of the issues" and evidence already assembled. The honest current state is not autonomy but *cold start* — small fixes land as one-or-two-line PRs, and "the bigger it is the more likely a human's involved in spearheading it over the line", with the human driving steps two and three rather than merely reviewing step one | `HighlightsPattern → pat-verification-gap` **[registry]** | `ReliesOnElement → el-continuous-fix-loop` |
| `ins-skill-surface-is-the-moat` | Answer to the obvious objection ("why not just point Claude Code at your data and have it push the PR?"): you should — and that is exactly the product. The work is the skill surface, not the model: find the right slice of data, get it into the repo in a file format the harness handles well, and decompose capability into composable skills mapped to real tool affordances (Pyroscope memory-issue detection, facet/cohort-by-customer). "It's not just point Claude at the data." The observability vendor's differentiation in the agent era is skill design and data shaping, with the black box deliberately opened (bring your own harness, sandbox, skills, prompt) | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** | `ReliesOnElement → el-observability-skills`, `ReliesOnElement → el-agent-skills` **[registry]** |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-lopatecki-signal-to-pr`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-build-signal-to-pr-loop` | Build the trace-to-PR loop, local first | Prototype the loop locally with your coding agent before automating it, then run the identical thing on a trigger; wire two trigger classes — periodic (e.g. every five minutes) and event-based (each error) — and start from traces, since AI systems already have traces at the core of the agent framework, with logs alongside; assemble the combination that lets the agent act (production traces/logs pulled by skills + the repo so the code path is legible + eval values already layered on the traces); choose the pieces explicitly — harness (Claude Code), sandbox (own VPC sandbox, Anthropic managed agents, Daytona), skill set, driving prompt ("look for security issues"); track running agents as a fleet with viewable sessions and downloadable transcripts, and allow resuming a session locally to continue debugging by hand; close the loop by converting each confirmed issue into an evaluator or a dataset entry so the same failure is caught next time | `ReferencesElement → el-continuous-fix-loop`, `el-arize-signal`, `el-observability-skills`, `el-claude-code` **[registry]** |
| `how-design-data-skills-for-agents` | Design observability skills for a coding agent, not a dashboard | Design for retrieval first — the hard part is finding the right data (e.g. the group of traces belonging to one session); materialize it into the repo as files, accepting large ones (10 MB temp files in the repo are normal) because "these harnesses are magical with files"; pick the file format deliberately so the harness parses it cheaply; decompose into composable skills that mirror real tool affordances (Pyroscope memory-issue skills, facet use, cohort-by-customer to isolate one customer's failures) so the agent can chain steps rather than call one monolithic query; expose eval results as trace-attached data with skills that fetch aggregate eval values across traces, giving the agent pre-processed assessment on top of raw telemetry | `ReferencesElement → el-observability-skills`, `el-agent-skills` **[registry]**, `el-prod-to-code` **[registry]** |

## Dropped

- **Daytona** — named once as a third-party sandbox option; no company node coined (single passing mention, no content). Kept as prose inside `el-arize-signal`. Same for "Booking.com", carried only as prose in `sig-vpc-sandbox-boundary` (`co-uber` reused because the registry already has it).
- **Grafana** ("clicking around grafana UI") — rhetorical foil for the old observability model; no node.
- **Online evals** — Q&A defines them (evals layered onto production traces as trace-attached data, "an AI assessment that's always running", built from failures you've seen before like prompt injection). Deliberately NOT coined as an element: the content is the eval-tiering thesis already carried by `el-agent-as-a-judge` (this batch, `dhinakaran-arize-agent-as-judge.md`) and by `el-scenario-based-evals`/`el-eval-driven-development` **[registry]**. Retained as prose in `how-design-data-skills-for-agents`. Flip to a node at review if central wants an explicit online-vs-offline eval element.
- **The financial-trading-agent demo** — illustrative scaffolding for the product walkthrough; folded into `sig-arize-signal-launch`.
- **"SRE for AI"** — speaker explicitly distances from the "black box SRE agent" framing ("all we're really trying to do is take your local debugging experience and run it periodically"); kept as prose in `ins-skill-surface-is-the-moat`.

## Review notes

1. **Shared-entity contract with the sibling Arize talk.** `el-arize-signal` and `el-arize-alex` are defined **here** and referenced (not redefined) in `dhinakaran-arize-agent-as-judge.md`. `co-arize` and `el-arize-phoenix` come from batch 8 (`nabors-arize-frontier-on-device.md`); `exp-jason-lopatecki` and `exp-aparna-dhinakaran` are two distinct new experts on the same company. Cross-batch: `el-arize-signal` is also cited by the Snorkel talk in this batch (`feyzkhanov-snorkel-traces-to-simulations.md` recommends Arize for recording experiments) — that file carries `RelevantCompany → co-arize` on one signal, no element edge.
2. **Pattern candidate evidence (noted, NOT coined).** `pat-adaptive-software` / `pat-adaptive-harness` (batch-7/8 paired candidate): this talk's explicit north star is "how do I build systems that autonomously fix themselves… have this thing just improve itself", with the 2.0/3.0 framing (human-reviewed fixes today, continuous agent loops next). That is the self-modifying-production-system flavor of the candidate — comparable to Graziano's AutoAgent and RELAI's optimizer. Weak add to `pat-durable-execution` (loops living in triggered sandboxes rather than laptops). No new pattern coined; nothing here is seed-altitude on its own.
3. **`el-continuous-fix-loop` merge check.** Three registry near-neighbours were considered: `el-prod-to-code` (HUD — the *context translation*, edged as UsesElement), `el-agentic-vuln-pipeline` (Anthropic — the same loop shape scoped to security), and `el-agentic-ai-engineer`/`el-eval-driven-development` (batch 8 — the *development* loop, not the incident loop). Kept separate because this element is specifically the production-incident loop with trigger/sandbox/harness as configuration. If central reads it as a duplicate of `el-prod-to-code`, rehome the two knowhows and `ins-responder-to-reviewer` there.
4. **`pat-sovereign-ai` fit on `sig-vpc-sandbox-boundary`.** The seed pattern's description is regulation-driven (DORA / EU AI Act / on-prem GPU breakeven); this signal is the commercial data-boundary flavor — enterprises accept a VPC appliance but refuse to route production connections to a model vendor. Reads as the same "own your stack" thesis from the customer side; downgrade to pattern-less if you want `pat-sovereign-ai` kept regulatory.
5. **Caption garbles flagged:** "Arise"→Arize throughout; "cloud code"/"clouded session"→Claude Code; "Tanthropic"→Anthropic; "element as a judge"/"elements a judge"→LLM as a judge (Q&A, twice); "SR"/"S agent"→SRE; "bookings"→Booking.com; "AX" is the real product name (Arize AX), not a garble. Speaker self-identifies only as "founder"; the co-founder/CEO title in `exp-jason-lopatecki` comes from the batch brief, not the transcript.
6. **Q&A is load-bearing in this file.** Two of the strongest claims (`ins-skill-surface-is-the-moat`, the online-eval mechanism in `how-design-data-skills-for-agents`) come from audience Q&A, not the prepared talk — flagged in case you weight prepared content differently.
