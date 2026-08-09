# SPIKE extraction — "The 2026 State of AI Engineering" (Barr Yaron, Amplify Partners) — FOR REVIEW

Source transcript: `transcripts/yaron-amplify-state-of-ai-engineering.txt` (auto-captions — quotes are paraphrases, not verbatim; "Barr Yaron" renders as "Barren"/"Bar", "Vercel" as "Verscell").
Video: https://youtu.be/RGe6EjucbzI — AI Engineer World's Fair, published 2026-07-21 (premiere).
`stagingTimestamp` for the artifact and all signals: 2026-07-21 (publish date).
Entities marked **[registry]** already exist — edges link to them, no new node.

Context: annual survey talk, n=1,048 AI engineers (builder-heavy, self-selected; survey run with Notion and Vercel). Third-plus year of the series, so YoY deltas are the payload — numbers kept verbatim in briefs.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-yaron-state-of-ai-eng` | The 2026 State of AI Engineering (Barr Yaron, Amplify Partners — AI Engineer World's Fair) | youtube | https://youtu.be/RGe6EjucbzI |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-barr-yaron`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-barr-yaron` | Barr Yaron (investment partner, Amplify Partners; runs the annual State of AI Engineering survey) | `AffiliatedWithCompany → co-amplify-partners` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-amplify-partners` | Amplify Partners | investor | early-stage VC "investing in companies built by and for AI engineers"; owner of the annual State of AI Engineering survey |

## Elements (0 new)

None — survey name-drops (Nano Banana 1/2, ChatGPT Images 2.0, Notion, Vercel) stay prose.

## Signals (6 new)

All: `SpottedInArtifact → ia-aie-yaron-state-of-ai-eng`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | domain | name / brief | pattern edge | RelevantCompany |
|---|---|---|---|---|
| `sig-2026-agents-cross-write-threshold` | harness | Agents crossed the write threshold in 2026: 95% of surveyed teams use agents (~2x YoY) and 89% of those agents have write access (52% last year) — write-enabled share of all respondents up >3x YoY — while control stays blunt (top two: human-in-the-loop approvals, permission gating — "the toolkit you'd use to manage an intern"); below that, controls scatter (decomposition, retrieval, memory, sandboxing) — nobody has settled the agent control layer; ~2/3 name hallucination or lost context mid-task as the top agent frustration | `FormsPattern → pat-verification-gap` | — |
| `sig-2026-evals-still-top-challenge` | harness | Every year of the survey the #1 stack challenge is evaluating AI outputs — still true in 2026 though the margin is thinning; 96% of respondents report some stack problem; and "vibe review" remains the single most common eval method in production | `FormsPattern → pat-verification-gap` | — |
| `sig-2026-openweight-augments-closed` | inference | Open weights augment, not replace: 94% use closed models in production, 45% open-weight, and >90% of open-weight users also run closed models; open-vs-closed is a top-3 model-choice factor for only 5% of respondents (quality dominates, then agentic capability/tool-calling and cost tied; reliability named by only 1 in 5); 87% run multiple models, most routing by task type | `ContradictsPattern → pat-sovereign-ai` (mild counter-evidence — see notes) | — |
| `sig-2026-cost-first-class-constraint` | inference | Cost became a first-class engineering constraint: 40% say cost regularly shapes how ambitiously they use AI and another 36% say sometimes (~3 of 4 adjust usage on cost); cost/token usage is the #2 production monitoring item, right under quality — "monitored like an SLA"; 12 months ago none of this registered | — (see notes) | — |
| `sig-2026-nondev-shipping` | — | Role-boundary erosion quantified: 81% say AI blurs the line between engineering and product/design/marketing; over 1/3 of teams have non-developers shipping features (mostly small/internal) and 17% have non-devs regularly shipping customer-facing features; the bill: 9 in 10 feel negative downstream effects, led by review burden and erosion of deep technical skills / codebase understanding — while 97% still report net-positive org impact, top effect "cheaper failure" (more experiments, prototypes, bets) | `FormsPattern → pat-value-of-judgement` | — |
| `sig-2026-image-gen-doubles-audio-intent` | inference | Modality adoption 2026: share happily using image generation doubled 18% → 36% YoY (window includes Nano Banana, Nano Banana 2, ChatGPT Images 2.0); audio holds the highest intent-to-adopt for the second straight year and it is accelerating — 56% of non-users plan to adopt, up from 37%; text still dominates everything | — | — |

## Insights (3 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-standardization-of-stack-not-models` | The "great standardization" is happening one layer above models: >half of orgs are standardizing on fewer AI tools/platforms while staying deliberately plural on models (87% multi-model, routed by task type) — models are treated as swappable components; the platform is the commitment | `HighlightsPattern → pat-model-not-bottleneck` | — |
| `ins-reliability-now-threshold` | Reliability's near-absence from model-choice criteria (1 in 5) reads not as indifference but as saturation: models are reliable enough, reliability became a threshold requirement, and the real decision moved up the stack to quality, agentic capability, and cost | `HighlightsPattern → pat-model-not-bottleneck` | — |
| `ins-build-buy-boundary-follows-product-logic` | The build-vs-buy line traces the value line: inference/model serving is the most-bought layer, while product logic stays in-house (61% build their own prompt management — "everyone's prompts are special"; prompts, RAG, evals relatively in-house; fine-tuning "the clearest not yet") — differentiation lives in the layers around the model, not in serving the model | `HighlightsPattern → pat-model-not-bottleneck` | — |

## KnowHow (0 new)

None — the talk is descriptive survey data, not method.

## Dropped

- Five-year bets: 67% expect a leading lab will *declare* AGI within 5 years (press-release wording deliberate — "we asked about the press release, not the achievement"); only 9% bet transformers remain state-of-the-art in 5 years; 36%/38% split on more AI compute in space vs land. Parlor sentiment — kept out of the signal budget.
- Sentiment stats: 76% say AI boosted job satisfaction; 59% fear today's AI code creates long-term liabilities; only ~1/3 call software engineering "solved" (speaker herself flags the definitional slipperiness).
- Experience mix: of respondents with 10+ years software experience, over half have ≤3 years of AI experience; the median new engineer has nearly as much AI experience as the median 10-year veteran.
- Intro news aside: "Meta reportedly exploring selling AI compute" — undated, secondhand.
- Notion and Vercel as survey partners — prose (`co-notion` exists in registry; Vercel not coined, no load-bearing content).
- Barr's "intent to adopt ratio" as a coined metric — kept inside sig-6's brief.

## Review notes

1. **Pattern-candidate evidence (noted per instruction, NOT coined, no edges):**
   - `pat-ai-native-org` — strongest quantitative evidence yet for this candidate: **81% role-blur; >1/3 of teams with non-developers shipping features; 17% non-devs regularly shipping customer-facing features**. Prior evidence was anecdotal (Tan, Wu/Shihipar, Brunet, Doshi, An/Hoe, Noring, Grbic); this is the first broad-sample quantification.
   - `pat-agent-economy` — supportive context only: cost-as-first-class-constraint (**40% regularly + 36% sometimes shape usage by cost; cost the #2 monitored production metric**) quantifies the spend side, but shows no agent-to-agent transaction evidence. `sig-2026-cost-first-class-constraint` left pattern-less accordingly.
   - `pat-benchmark-trust-crisis` — weak adjacency at most: "vibe review is the #1 eval method" is eval *immaturity*, not benchmark distrust. Listed for completeness.
   - `pat-durable-execution` — no evidence in this talk.
2. **ContradictsPattern call** on `sig-2026-openweight-augments-closed`: read as mild counter-evidence to `pat-sovereign-ai` in the practitioner segment — sovereignty/openness is not what drives production model choice (top-3 factor for only 5%), and open weights function as augmentation, not replacement. If reviewers scope `pat-sovereign-ai` strictly to nation/enterprise level, drop the edge and leave the signal pattern-less.
3. `sig-2026-nondev-shipping` → `pat-value-of-judgement` is interpretive: execution industrialized/democratized (non-devs shipping) while the felt costs are review burden and eroded deep understanding — i.e. the residual engineering edge is judgment/verification. Alternative at review: leave pattern-less and count wholly toward `pat-ai-native-org` if that gets coined.
4. Three insights all highlight `pat-model-not-bottleneck` — deliberate; this survey is the broadest quantitative corroboration of that pattern in the corpus (multi-model plurality + platform standardization + buy-inference/build-product-logic + fine-tuning "not yet").
5. Survey caveats to keep attached: n=1,048, self-selected, builder-heavy; the speaker herself flags "95% using agents" as suspiciously high.
6. Garbles: "Barren"/"Bar" = Barr Yaron; "Verscell" = Vercel; "Alphaba and Glenda" = Elphaba and Glinda (Wicked joke). All percentages read clean against slide context.
