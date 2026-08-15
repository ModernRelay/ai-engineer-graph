# SPIKE extraction — "How Web Data Infrastructure Powers the Next Generation of AI" (Patricija Žemaitytė, Oxylabs) — FOR REVIEW

Source transcript: `transcripts/zemaityte-oxylabs-web-data-infrastructure.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/1UmZHb_E_SM — AI Engineer World's Fair, **Computer Use (CUA) track**, published 2026-08-14.
`stagingTimestamp` for the artifact and all dated nodes: 2026-08-14 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Shape of the talk: the track's infrastructure war-stories talk, told as three escalating customer demands. (1) A two-week ask for a 5PB/month video-data API that grew into a whole multimodal suite — "innovation is repeated adaptation under pressure; clients don't buy the first iteration, they buy your ability to adapt." (2) Sub-second SERP delivery, redesigned from a 4-second scraper to 550ms — "speed becomes product." (3) Scaling a web unblocker from 10k to 60k (now targeting 100k) requests/second — "scale is never a finish line." Closes on the thesis: the next generation of AI is powered by infrastructure around the model, not better models. Caption garbles: "Patricia" → **Patricija Žemaitytė** (per byline), "SERP/SER" → SERP, "stainless data" → **stale data**, "web and blocker/unblocker" → **Web Unblocker**, "pabytes" → petabytes, "instruction" → structuring.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-zemaityte-web-data-infrastructure` | How Web Data Infrastructure Powers the Next Generation of AI (Patricija Žemaitytė, Oxylabs — AI Engineer World's Fair) | youtube | https://youtu.be/1UmZHb_E_SM |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-patricija-zemaityte`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-patricija-zemaityte` | Patricija Žemaitytė (product manager, Oxylabs; came from engineering, led core-services and "UX" squads) | `AffiliatedWithCompany → co-oxylabs` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-oxylabs` | Oxylabs | developer | Founded 2015; "web intelligence platform and premium proxy provider" — infrastructure to extract public web data at scale. Products referenced: a video-data API suite (downloader, transcripts, subtitles, channel info, metadata), a Fast Search API (550ms avg), and Web Unblocker (proxy-integrated scraper). Scale cited: 400M → ~6B daily search requests; unblocker 10k → 60k (targeting 100k) req/s |

Reused **[registry]**, edge-only: `co-google` **[b2]** — Google's grounding documentation "explicitly positions Google Search as a way to connect models to current public knowledge"; SERP baseline.

## Elements (4 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-web-data-pipeline` | Web data as pipeline, not feature | concept | infra | The first war story's lesson: a client's "video API for AI training" ask (5PB/month, two-week deadline) "stops sounding like a product feature and sounds like infrastructure" — collection, transfer, storage, delivery, at AI-training reliability. It grew by iteration (downloader → transcripts → *actually* subtitles → search → metadata → channel info) into a full multimodal suite in ~3 months. "Clients don't buy the first product iteration, they buy your ability to adapt." AI infrastructure is increasingly multimodal — video, metadata, transcripts, subtitles, structural context around content |
| `el-speed-becomes-product` | Speed becomes product | concept | infra | The second war story: a sub-second SERP request against a 4-second baseline scraper. The insight was that it "was never about making the old scraper faster" — the regular scraper retrieves everything (ads, widgets, rich results, layouts) while a fast search API keeps only what AI systems need (organic results, top stories, news), cutting heavy layout. Redesigned from scratch to 550ms average / 650ms P90. "In AI era, speed is not just performance — speed defines what product can exist": at 4 seconds you have a slow pipeline; sub-second, something that can sit inside AI workflows. Grounding retrieval (Google's own framing) is the use case |
| `el-scale-is-not-a-finish-line` | Scale is never a finish line | concept | infra | The third war story: scaling Web Unblocker from 10k to 60k req/s in under two months (now "project 150" → ~100k). At that load "even adding 2,000 servers doesn't solve the problem — you need an architecture," reliable central components, observability that still tells the truth (telemetry becomes part of the load), and testing that resembles reality. The real bottleneck showed up in **load testing, not outages** — organic-traffic testing (behaving like real client usage) is far harder than synthetic; they hit a wall at ~20k req/s where the question became not "does it work" but "do we know it can go further," and uncertainty was the bottleneck. Ends accepting "real testing is with production traffic" |
| `el-adapt-forever-infrastructure` | Adapt-forever infrastructure | concept | infra | The synthesis: web-data infrastructure "is not a build-once business, it's an adapt-forever business" — targets, layouts, detection, market, and client needs all change constantly, so "innovation is the ability to keep adapting fast enough that changing requirements become new infrastructure." The value proposition: "you build the intelligence, we take the messy maintenance underneath." The closing thesis — "the next generation of AI will not be powered by better models; it will be powered by better infrastructure around it" that connects models to reality |

Element edges: all four `IdentifiedInArtifact → ia-aie-zemaityte-web-data-infrastructure`.
`el-web-data-pipeline` `DevelopedByCompany → co-oxylabs`;
`el-speed-becomes-product` `DevelopedByCompany → co-oxylabs`;
`el-scale-is-not-a-finish-line` `EnablesElement → el-adapt-forever-infrastructure`;
`el-adapt-forever-infrastructure` `ExemplifiesPattern → pat-model-not-bottleneck` **[registry]**;
`el-speed-becomes-product` `EnablesElement → el-adapt-forever-infrastructure`.

Reused elements (no new nodes): `el-multimodal-tax` **[b8]** adjacency (multimodal pipeline demand), edge left to review; `el-context-as-a-service` **[b20, Primor]** — the same-batch sibling category; Oxylabs is the raw-infrastructure layer under Primor's CaaS argument, cross-file edge proposed in note 3.

## Signals (4 new)

All: `SpottedInArtifact → ia-aie-zemaityte-web-data-infrastructure`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-oxylabs`.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-web-data-is-the-ai-substrate` | infra | An infrastructure vendor's framing: "my talk starts somewhere less glamorous — with infrastructure that decides whether models get fresh, usable, real-time data at all." Training still matters but "training alone is no longer enough; to stay useful models need fresh information, live search, real external data — without that even the smartest model is limited by what it knows." The next generation of AI is "powered by better infrastructure around it, not better models." A direct statement of the value-moves-around-the-model thesis, from the data-plumbing layer | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-web-data-pipeline`, `el-adapt-forever-infrastructure` |
| `sig-multimodal-web-pipelines-now-required` | data-eng | The market shift the first war story tracks: "AI infrastructure is becoming increasingly multimodal — no longer about text; companies now need pipelines for video, metadata, transcripts, subtitles, and structural context around the content." A 5PB/month video-data-for-training ask that grew into a full suite (downloader, transcripts, subtitles, search, channel info) is offered as evidence the demand is real and escalating — the supply-side signal for the training-data and multimodal threads | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-web-data-pipeline` |
| `sig-latency-gates-agentic-retrieval` | infra | The second war story's claim: sub-second web retrieval "defines what product can exist" — a 4-second scrape is a slow pipeline; 550ms "can sit and interact in your AI workflows." Achieved not by breakthroughs but by scoping (organic results only, cutting heavy layout) and "small decisions that add up." Directly serves grounding/retrieval pipelines (Google's own framing of Search as model-grounding), and the scale jump (400M → 6B daily requests) "changes the operating model — how you think about cost, observability, failure domains." Latency as the enabling constraint for agentic web access | `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-speed-becomes-product` |
| `sig-web-infra-is-adapt-forever` | infra | The synthesis signal: web-data infrastructure "is not a build-once business, it's an adapt-forever business" — targets, layouts, anti-bot detection, market and client needs change constantly, so the durable product is the *maintenance*, not any single scraper. "You build the intelligence, we take the messy maintenance underneath." Convergent with Primor's data-decay argument (same batch): the web's constant change is what makes the infrastructure layer a subscription and a moat. The maintenance-as-moat claim for the agent-data layer | `FormsPattern → pat-agent-memory-layer` **[registry]** | `OnElement → el-adapt-forever-infrastructure`, `el-scale-is-not-a-finish-line` |

## Insights (2 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-maintenance-is-the-moat` | The unglamorous claim under all three war stories is that the defensible product in the agent-data layer is *maintenance*, not any artifact: scrapers break, layouts shift, anti-bot detection evolves, so "you build the intelligence, we take the messy maintenance" is the actual value exchange. That is why the layer is a subscription and why it resists disintermediation — the same reason Primor's owned-context compounds and Klein's infrastructure consistency matters. Three vendors in one track converge on "the web's constant change is the business" | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** | `ReliesOnElement → el-adapt-forever-infrastructure`, `el-scale-is-not-a-finish-line` |
| `ins-latency-is-a-capability-gate` | Sub-second retrieval is not an optimization but a capability threshold: below it you have a batch pipeline, above it you have something an agent can call mid-reasoning, so latency decides which products can exist at all. And it's won by scoping and accumulation of small cuts, not breakthroughs — which means the agent-data layer competes on operational engineering, the same conclusion the CUA-infrastructure talks reach from the browser side. The 400M→6B request jump shows the reward: crossing the latency gate unlocks a different order of demand | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** | `ReliesOnElement → el-speed-becomes-product`, `el-web-data-pipeline` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-zemaityte-web-data-infrastructure`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-build-web-data-infrastructure` | Build web-data infrastructure for an adapt-forever business | Treat a big data-access ask as **infrastructure, not a feature** — collection, transfer, storage, delivery at the reliability your consumer (AI training or agent retrieval) demands — and expect the first iteration to be wrong: clients buy your ability to adapt, so instrument for fast iteration (downloader → transcripts → subtitles → search → metadata was one product's real path); for retrieval latency, don't just speed up the general scraper — **scope it** to what AI systems actually need (organic results, top stories) and cut heavy layout, because sub-second delivery is a capability gate that decides which products can exist, and it's won by many small cuts not a breakthrough; when scaling throughput, past a point **adding servers doesn't help — you need an architecture**, reliable central components, observability that stays truthful as telemetry becomes part of the load, and load tests using organic (real-usage-like) traffic, not just synthetic, accepting that the final test is production traffic; and design for **constant change** — targets, layouts, anti-bot detection and client needs all shift, so the durable product is the maintenance underneath, letting customers build intelligence on top while the messy upkeep stays with you | `ReferencesElement → el-web-data-pipeline`, `el-speed-becomes-product`, `el-scale-is-not-a-finish-line`, `el-adapt-forever-infrastructure` |

## Dropped

- **The "UX = client needs something unusual on a painful timeline" origin anecdote** — framing for `el-web-data-pipeline`.
- **The "still waiting for payment / 30 petabytes" punchline** — colour.
- **The blocked-mid-demo SERP story** — illustration of test-vs-reality; folded into `el-speed-becomes-product` and the KnowHow's production-traffic point.

## Review notes

1. **The batch's purest "value moves to infrastructure around the model" talk**, and it lands almost entirely on `pat-model-not-bottleneck` — four of five edges. It is a war-stories talk with no thesis-level novelty, so its signals are corroborative rather than pattern-defining; the strongest keep is `sig-web-infra-is-adapt-forever` (maintenance-as-moat), which feeds `pat-agent-memory-layer` from the raw-data-supply layer beneath Primor's CaaS.
2. **Same-batch sibling to the Bright Data talk.** Oxylabs (raw web-data infrastructure) sits *beneath* Primor's CaaS category — both argue the web's constant change makes the layer a subscription. Convergent, not redundant: Primor argues the economics (owned vs rented), Žemaitytė argues the operations (adapt-forever). Two web-data vendors on the same track the same day is itself a market signal for the agent-data-supply thread.
3. **⚠ Verify before seeding:** all figures vendor-stated — 5PB/month video ask, 550ms/650ms-P90 SERP latency vs 4s baseline, 400M→6B daily requests, 10k→60k→100k req/s unblocker, founded 2015, ~20k-req/s load-test wall. The Google-grounding-documentation reference is real but paraphrased.
4. **Proposed cross-file edge, left to review:** `el-context-as-a-service` **[b20, Primor]** `UsesElement → el-web-data-pipeline` **[here]** — CaaS is built on raw web-data infrastructure like this. Not emitted; both files are same-batch and the layering is thematic. Also `el-multimodal-tax` **[b8]** adjacency for the multimodal-pipeline demand.
