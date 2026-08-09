# SPIKE extraction — "Research to Reality: Bringing Frontier ML Research to Production" (Vaidas Razgaitis, Higharc) — FOR REVIEW

Source transcript: `transcripts/razgaitis-higharc-research-to-reality.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/OXMMN-XbxwA — AI Engineer World's Fair, published 2026-06-28.
`stagingTimestamp` for the artifact and all signals: 2026-06-28 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-razgaitis-research-to-reality` | Research to Reality: Bringing Frontier ML Research to Production (Vaidas Razgaitis, Higharc — AI Engineer World's Fair) | youtube | https://youtu.be/OXMMN-XbxwA |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-vaidas-razgaitis`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-vaidas-razgaitis` | Vaidas Razgaitis (senior research engineer, Higharc Labs — the company's ML R&D arm) | `AffiliatedWithCompany → co-higharc` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-higharc` | Higharc | developer | AI-native home-building/design platform; its Labs team applies frontier ML (CV, agents, custom transformers, diffusion) to residential architecture and spatial reasoning |

## Elements (3 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-research-prototype-taxonomy` | Research Prototype Taxonomy (RPT) document | ops | infra | Higharc's required handoff artifact for every ML research prototype — a technical design document with ML twists: domain context and novel data representations (what a new hire from outside the field must learn), business goal, type contract between the core product repo and the ML repo, persistence-layer mapping (researchers map it, engineers build it), system anatomy (workflow? chained workflows? external LLM calls?), and a merge/decomposition plan |
| `el-ml-microservice-monorepo` | ML microservices monorepo | concept | infra | Repo structure for productionizing research: a Python monorepo, separate from the core product repo, of cleanly isolated, fully decoupled microservices at roughly a 1:1 researcher-to-service ratio — gateway-fronted on one Docker bridge network, each service a standalone layered FastAPI app (API routers → controllers → business logic → data) with its own Dockerfile, metadata, and lockfiles; shared CI, GPU notebooks, and tooling underneath |
| `el-graphite` | Graphite (stacked diffs) | product | — | Stacked-diff code-review tool; at Higharc the vehicle for decomposing large monolithic research prototypes into tightly scoped, dependency-ordered PRs that subject-matter experts review asynchronously (work continues up-stack while a domain specialist reviews below) |

Element edges: all three `IdentifiedInArtifact → ia-aie-razgaitis-research-to-reality`; `el-research-prototype-taxonomy` `EnablesElement → el-ml-microservice-monorepo` (the RPT's type/persistence/architecture mapping informs the decomposition into the repo).

## Signals (3 new)

All: `SpottedInArtifact → ia-aie-razgaitis-research-to-reality`, `SourcedFromSource → source-aie-yt` **[registry]**, `RelevantCompany → co-higharc`.

| slug | domain | name / brief | FormsPattern |
|---|---|---|---|
| `sig-handoff-is-the-bottleneck` | infra | Vertical-AI practitioner: the constraint on shipping frontier ML isn't the research — it's the researcher↔engineer baton pass. ML researchers who are paper-current but have never owned production-grade APIs must hand off to platform/back-end engineers unfamiliar with CV/LLM-training methodology; Higharc treats this explicitly as a systems-and-process problem with three levers — research legibility, repo structure, and decomposition/review | `FormsPattern → pat-model-not-bottleneck` **[registry]** |
| `sig-repos-built-for-agent-navigation` | context | Repository architecture now has coding agents as a first-class audience: Higharc keeps consistent skeletal backbones across its ML microservices and "really cleanly documented specs so that agents can navigate these repositories and help accelerate our ML researchers" (paraphrase) — repo legibility engineered for agents, not just humans | `FormsPattern → pat-context-graphs` **[registry]** |
| `sig-vertical-pulls-full-ai-stack` | — | A single home-building product ends up consuming nearly the whole applied-AI frontier at once — computer vision to parse hand-sketched floor plans into an internal data model, reasoning agents carrying users through agentic experiences, custom transformers (their data-driven entity-prediction model), and diffusion models for image generation — vertical spatial-reasoning products as full-stack AI consumers | — (pattern-less; see review note 2) |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-decomposition-is-design` | Getting a proven prototype into production is a design problem in decomposition: the axes you slice a monolithic prototype along — informed by the RPT's type, persistence, and architecture mapping — determine whether the right subject-matter experts can review each slice and whether delivery dates are estimable; chronic timeline unpredictability is a downstream symptom of upstream legibility or repo problems | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** | `ReliesOnElement → el-research-prototype-taxonomy`, `ReliesOnElement → el-graphite` |
| `ins-one-researcher-one-microservice` | A ~1:1 researcher-to-microservice ratio in a decoupled monorepo lets each research initiative grow and iterate independently behind a gateway while still conforming to production practice (layered architecture, type contracts, CI, containerization) — researcher velocity and production discipline stop trading off | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** | `ReliesOnElement → el-ml-microservice-monorepo` |

## KnowHow (3 new)

All `SourcedFromArtifact → ia-aie-razgaitis-research-to-reality`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-rpt-handoff-doc` | Require an RPT document from every research prototype | Write it before staffing engineers onto the project: (1) domain context + novel data representations (parti diagrams, circulation graphs, embeddings/latent spaces — "picture the software engineer we just hired from JP Morgan"); (2) business goal — why solving this matters; (3) type contract between core and ML repos and how types stay in sync; (4) persistence mapping — researchers should NOT go deep here, just map how far they got (a natural first entry point for engineering help); (5) system anatomy — workflow vs. chained workflows, external LLM calls, model weights pulled in CI/CD; (6) merge/decomposition plan | `ReferencesElement → el-research-prototype-taxonomy` |
| `how-stacked-diff-decomposition` | Decompose prototypes via stacked, SME-routed PRs | Study which axes to slice the monolithic prototype on and what the dependency graph looks like (the RPT's layer/persistence/type mapping informs this); use stacked diffs (Graphite) so review is asynchronous — keep building up-stack while a domain specialist reviews below; tap the specific subject-matter expert for each tightly scoped slice | `ReferencesElement → el-graphite`, `ReferencesElement → el-research-prototype-taxonomy` |
| `how-diagnose-research-pipeline` | Diagnose the research-to-production pipeline with three questions | (1) Legibility: when product people / software engineers / AI engineers join a research initiative, is it obvious where to concentrate and which tasks to pluck off? If ambiguous, fix the RPT process. (2) Repo: is it clear which bucket new code goes in, with templates and patterns to mimic — or are you fighting old abstractions every time (you've outgrown the architecture)? (3) Decomposition: can you consistently estimate timelines and name the right SME reviewers? Failures here usually point upstream to (1) or (2) | `ReferencesElement → el-research-prototype-taxonomy`, `ReferencesElement → el-ml-microservice-monorepo` |

## Dropped

- Modal (GPU compute for Jupyter notebooks), FastAPI, Docker, Poetry/UV, GitHub Actions — named plumbing inside `el-ml-microservice-monorepo`'s brief; no separate nodes.
- The Pragmatic Engineer blog reference (design docs align scaling teams) — lineage citation for the RPT, prose only.
- "Top secret topics I can't reveal" — nothing extractable.

## Review notes

1. **Caption garbles resolved from official title:** "Vitis" → Vaidas Razgaitis; "Hyark" → Higharc. Unresolved: "party diagram" → almost certainly **parti diagram** (architecture term for an organizing concept sketch) — flagged, written as "parti" in the knowhow; "data-driven entity prediction" as their custom transformer's name is plausible but unverified. Quotes are paraphrases.
2. `sig-vertical-pulls-full-ai-stack` is deliberately pattern-less — a vertical-AI texture datum with no matching registry pattern; not proposing a new one on one-talk evidence.
3. **Pattern-fit judgment call:** both `pat-model-not-bottleneck` links read the org-process/handoff layer as "the layers around the model" where failure and value migrated. If central reads that pattern as strictly technical layers (config/delivery/memory/trust), these signals need a rehome — nearest alternative is leaving `sig-handoff-is-the-bottleneck` pattern-less.
4. `sig-repos-built-for-agent-navigation` → `pat-context-graphs` is a judgment call (repo-as-structured-context engineered for agent consumption); alternative reading is `pat-harness-over-model`. One-sentence evidence in the transcript, but it is a distinct and quotable claim.
5. `el-graphite` coined without `DevelopedByCompany` (the company behind the tool is never discussed); brief disambiguates from the Graphite metrics database. Kind `product`, no AI domain — domain left null.
6. Spec-culture resonance: the RPT is the research-side sibling of spec-driven development (hanchett file, same batch) — both institutionalize written specs as the interface between humans/agents and implementation; noted for the registry's spec-related candidate ledgers, no candidate evidence claimed.
