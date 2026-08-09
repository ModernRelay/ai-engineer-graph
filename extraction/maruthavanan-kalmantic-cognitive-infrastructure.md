# SPIKE extraction — "Stop Renting Your Cognitive Infrastructure" (Thiyagarajan Maruthavanan, Kalmantic Labs) — FOR REVIEW

Source transcript: `transcripts/maruthavanan-kalmantic-cognitive-infrastructure.txt` (auto-captions — quotes are paraphrases, not verbatim; several product/app names garbled, see Review notes).
Video: https://youtu.be/Bck7ABCZRZI — AI Engineer World's Fair, published 2026-07-18.
`stagingTimestamp` for the artifact and all signals: 2026-07-18 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-maruthavanan-cognitive-infra` | Stop Renting Your Cognitive Infrastructure (Thiyagarajan Maruthavanan, Kalmantic Labs — AI Engineer World's Fair) | youtube | https://youtu.be/Bck7ABCZRZI |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-thiyagarajan-maruthavanan`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-thiyagarajan-maruthavanan` | Thiyagarajan Maruthavanan ("mtraj"; Kalmantic Labs — builder of consumer AI apps and own inference infrastructure; author of a book on inference infra-economics) | `AffiliatedWithCompany → co-kalmantic-labs` |

## Companies (2 new)

| slug | name | type | note |
|---|---|---|---|
| `co-kalmantic-labs` | Kalmantic Labs | developer | speaker's research lab; runs its own agents and inference infrastructure (DGX-based) |
| `co-uber` | Uber | bigtech | appears as an AI-consuming enterprise: its CTO's annual token budget story is a headline signal here |

Reused: `co-anthropic` **[registry]** (retailer inference-spend signal; the speaker's app initially ran on Anthropic).

## Elements (2 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-token-factory` | Token factory | concept | inference | The middle option between renting frontier APIs and owning hardware: open-source models pre-deployed by neoclouds / inference-endpoint providers and provisioned as tokens-per-second; also DIY-able locally (garage GPU rigs, DGX boxes). Fails enterprises on control (rate limits), auditability (third-party dependency), and reproducibility (no access to model internals) |
| `el-just-token-max` | Just Token Max | product | inference | Speaker's open-source inference cost-optimization project (input-token compression, context management for agent loops); benchmarked against Netflix's Headroom and claimed superior on many parameters (both names auto-caption-garbled — see Review notes) |

Element edges: both `IdentifiedInArtifact → ia-aie-maruthavanan-cognitive-infra`; `el-token-factory` `ExemplifiesPattern → pat-sovereign-ai` **[registry]**.

## Signals (5 new)

All: domain `inference`, `SpottedInArtifact → ia-aie-maruthavanan-cognitive-infra`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | FormsPattern | other edges |
|---|---|---|---|
| `sig-retailer-200m-inference-exit` | One of the largest US retailers reportedly spent close to $200M on Anthropic inference, decided it was out of hand, and built its own infrastructure (speaker's claim, unnamed customer) | `FormsPattern → pat-sovereign-ai` | `RelevantCompany → co-anthropic` |
| `sig-uber-token-budget-month-four` | Uber's CTO reportedly planned a full-year token budget that was exhausted by month four — enterprise inference forecasting failing at the largest scale (speaker cites "the news") | `FormsPattern → pat-sovereign-ai` | `RelevantCompany → co-uber` |
| `sig-consumer-app-inference-blowout` | Speaker's consumer app (reverse-Suno: given a song, recover the prompt) reached hundreds of thousands of users and cost hundreds of thousands of dollars in inference — far beyond anticipation; agent loops + uncompressed context on an endpoint blind to workload shape | `FormsPattern → pat-sovereign-ai` | — |
| `sig-stolen-api-key-drain` | ~3 weeks before the talk the speaker's API key was stolen ("someone in China") and the endpoint drained from ~$7,000 toward $10,000 in days before being arrested — inference credits as a theft target | `FormsPattern → pat-new-cyber-threats` **[registry]** | — |
| `sig-enterprise-rented-inference-walls` | Three enterprises (an investment fund, a hospital, a tax practice) asked the speaker to replicate his owned setup after hitting non-cost walls with rented inference: rate-limit control dictated by the vendor, an audit red-lining the third-party dependency, and inability to reproduce a model's recommendation without model internals | `FormsPattern → pat-sovereign-ai` | — |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-rent-to-learn-own-to-earn` | "Rent to learn, own to earn" (paraphrase): pre-product-market-fit you can rent intelligence; post-PMF — or when an enterprise budgets a project, which presumes PMF — you cannot afford not to own the inference infrastructure. The rented model's prepaid casino economics (load credits, no monthly anchor) make cost mentally un-anchorable | `HighlightsPattern → pat-sovereign-ai` | `ReliesOnElement → el-token-factory` |
| `ins-inference-market-noise` | The AI infra market re-writes its rules every 3–6 months and every vendor's pitch matches its position (Jensen Huang: token factories; Satya Nadella: unmetered local intelligence; neoclouds: endpoint providers capture the value) — so builders must derive the rent-vs-own answer from their own workload, not the marketplace narrative | `HighlightsPattern → pat-sovereign-ai` | — |

## KnowHow (1 new)

`SourcedFromArtifact → ia-aie-maruthavanan-cognitive-infra`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-rent-vs-own-inference` | Decide when to stop renting inference | Pre-PMF: rent (Airbnb the city before buying the house). Post-PMF or a budgeted enterprise project: build owned infrastructure. Check the three enterprise walls beyond cost — control (rate limits), audit (third-party dependency), reproducibility (model internals access). Even while renting, optimize the layer you control: input-token compression, context management, taming wasteful agent-loop calls. Expect memory to be the bottleneck when moving to local hardware (DGX-class) | `ReferencesElement → el-token-factory`, `ReferencesElement → el-just-token-max` |

## Dropped

- Suno.com — named only to explain the app concept; no node.
- The DGX box itself and "neoclouds" — kept as prose inside `el-token-factory` / knowhow.
- Book "Peak Inference: infra-economics of AI inference" and the speaker's site/handle (mtraj) — provenance detail, kept in expert brief.
- Jensen Huang / Satya Nadella — quoted one-liners; no Expert nodes (they didn't contribute to the artifact).

## Review notes

1. Heavy caption garbling of names: the app appears as "Ultrazone" and "Ulta Sono" (likely one app, perhaps "UltraSono"); the OSS project as "just token max" (slug normalized `el-just-token-max`); the Netflix comparison target as "headroom" — I could not confirm a Netflix OSS project named Headroom, treat the whole benchmark claim as unverified; the book as "peak inference infraeconomics of AI inference". None of these garbles are load-bearing for the pattern links.
2. The $200M-retailer and Uber-CTO stories are second-hand, unnamed/uncited claims by the speaker — kept as signals because they are concrete and dated to the talk, but mark them attributable to the speaker, not verified reporting.
3. `sig-stolen-api-key-drain` links `pat-new-cyber-threats` rather than `pat-sovereign-ai`: the observation is about stolen inference credits as an attack, though the speaker uses it as an own-your-infra argument. Could carry both edges if double-linking is acceptable.
4. Pattern fit: the whole talk is a clean evidence set for `pat-sovereign-ai` (own vs rent intelligence infrastructure). I did not coin any "own-your-inference" pattern — it would duplicate `pat-sovereign-ai`.
5. Speaker name: official listing "Thiyagarajan Maruthavanan"; captions never state it. Company "Kalmantic Labs" from the listing; captions only say "my research lab".
