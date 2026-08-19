# SPIKE extraction — "Infra behind Krea 2: How to train and serve at scale" (Gabriel Menezes, Krea) — FOR REVIEW

Source transcript: `transcripts/menezes-krea-infra-train-serve.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/byn9PURoBNY — AI Engineer World's Fair, **Generative Media track**, published 2026-08-18.
`stagingTimestamp` for the artifact and all dated nodes: 2026-08-18 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Shape of the talk: a distributed-training-infra war-stories talk — how Krea trained its from-scratch image model **Krea 2** on thousands of Infiniband-connected GPUs and serves it from the same cluster. Two hard-won lessons: **metrics are everything** (GPU-utilization is a lie; use tensor-core / InfiniBand / NVLink metrics; let it crash and resume), and a **priority-scheduling + GPU-spot-arbitrage system** that flips production out to external providers when a training job needs the cluster, via virtual-kubelet. Caption garbles: "Korea"/"Korea 2"/"Create 2" → **Krea / Krea 2** (systematic), "SEF" → **Ceph**, "Q" → **Kueue** (the scheduler), "nickel timeouts" → **NCCL timeouts**, "DCGM" kept, "cerebra.ai" → likely **krea.ai** hiring alias (⚠ see review note 3).

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-menezes-krea-infra` | Infra behind Krea 2: How to train and serve at scale (Gabriel Menezes, Krea — AI Engineer World's Fair) | youtube | https://youtu.be/byn9PURoBNY |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-gabriel-menezes`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-gabriel-menezes` | Gabriel Menezes (infrastructure, Krea; built the training + serving cluster system) | `AffiliatedWithCompany → co-krea` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-krea` | Krea | developer | Generative-media company (krea.ai); trained **Krea 2** from scratch (no base checkpoint) on thousands of GPUs, open-sourced two checkpoints (raw + turbo), serves in production. Positioning: tools for creatives to explore "out of distribution" images, against "soulless" AI images |

Reused **[registry]**, edge-only: `co-nvidia` **[b2]** (GPU metrics — DCGM, NVLink, InfiniBand), `co-meta` **[seed]** (the failure-rate paper for large-scale pre-training). Referenced: Kubernetes, Kueue, virtual-kubelet, Ceph, Prometheus.

## Elements (4 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-training-metrics-truth` | Training metrics that tell the truth | concept | infra | "Metrics are everything — don't go blind." The load-bearing ones for large-scale pre-training, several NOT exported by default: **GPU temperature** (pull any GPU above ~78°C immediately — throttling destabilizes training; don't debug, replace); **tensor-core utilization** as the real proxy, because **GPU-utilization "is a lie"** (it shows the GPU doing *work*, not *good* work — reads 100% while under-utilized); and **InfiniBand + NVLink metrics** (wait times, error counts, packet types) — "if you're doing multi-node pre-training with no InfiniBand metrics you're doing something wrong," since most failures were cross-node communication. Custom exporters required |
| `el-crash-and-resume-training` | Let it crash, checkpoint hard | concept | infra | The reliability stance: at scale, jobs crash constantly and often silently (NCCL timeouts, metrics all green). Early paranoia (swap-node, change-node) gave way to "sometimes you just let it crash" — a run crashes hourly then runs 12–24h on the same machines/code/data. The fix is aggressive **checkpointing** on a fast filesystem (they moved off Ceph after losing trust in it; a paid cluster doing ~1.8 TB/s reads, ~1 TB writes let them checkpoint every 20–30 min, producing a terabyte in <30s without stalling training). Meta's failure-rate paper as the pattern, though their runs failed far more often |
| `el-priority-gpu-scheduling` | Priority scheduling + GPU spot-arbitrage | technology | infra | The system that lets one cluster run both training and production: researchers "don't think about GPUs" — they submit to a **gang-scheduling queue (Kueue)** with workload priority over normal Kubernetes priority. Training pods always outrank inference, so a submitted training job **evicts inference**, which is then **flipped to another cluster or external GPU rental** via a **virtual-kubelet** fake node that routes evicted pods to a provider. A **taint** system adds/removes taints as in-cluster GPUs free up, and a **descheduler** (not no-execute, to avoid taking production down all at once) slowly migrates pods back — a self-healing system where you "mark the pod failed and let Kubernetes handle it" |
| `el-inference-on-bad-gpus` | Diffusion inference on any GPU | concept | infra | A serving observation specific to diffusion transformers (unlike large LLMs needing multi-node inference): "whatever GPU works — the GPU can be hot, falling out of the bus, exploding, inference still runs." So low-priority production inference can run on the worst, cheapest, most-preemptible capacity while the good GPUs do training, and users feel nothing |

Element edges: all four `IdentifiedInArtifact → ia-aie-menezes-krea-infra`.
`el-priority-gpu-scheduling` `UsesElement → el-crash-and-resume-training`;
`el-training-metrics-truth` `EnablesElement → el-crash-and-resume-training`;
`el-priority-gpu-scheduling` `EnablesElement → el-inference-on-bad-gpus`;
`el-priority-gpu-scheduling` `DevelopedByCompany → co-krea`, `ExemplifiesPattern → pat-model-not-bottleneck` **[registry]**.

Reused elements (no new nodes): `el-kubernetes` **[b6]** (the substrate), `el-sandbox-snapshotting`/`el-microvm` adjacency (none coined). This talk shares the cross-cluster-compute theme with b18 Jiang (RL cross-datacenter) and b20 Menezes-adjacent infra; edge left to review.

## Signals (4 new)

All: `SpottedInArtifact → ia-aie-menezes-krea-infra`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-krea`.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-gpu-util-is-a-lie` | infra | A practitioner correction with teeth: the default **GPU-utilization metric "is a lie"** — it reads 100% during pre-training while the cluster is under-utilized, because it measures time-doing-work not efficiency. Use **tensor-core utilization** as the real proxy (it rises as image resolution scales through training stages), and export **InfiniBand/NVLink** metrics yourself (NVIDIA doesn't) since most large-scale failures are cross-node communication. Infra observability, not model quality, as the binding constraint on frontier training | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-training-metrics-truth` |
| `sig-let-it-crash-checkpoint-hard` | infra | The reliability lesson from thousands-of-GPU runs: jobs crash constantly and silently (NCCL timeouts, green metrics), and the winning response is not node-swapping paranoia but **letting it crash and checkpointing aggressively** on a fast filesystem — every 20–30 min, a terabyte in under 30s, off Ceph onto trusted paid storage. Durability of long training runs bought by cheap frequent checkpoints plus resume, not by preventing failure | `FormsPattern → pat-durable-execution` **[registry]** | `OnElement → el-crash-and-resume-training`, `el-training-metrics-truth` |
| `sig-gpu-spot-arbitrage-across-clusters` | infra | The capacity system: one cluster serves both training and production, with a **gang-scheduling queue** giving training strict priority so a training job **evicts inference**, which is **flipped to another cluster or external GPU rental via virtual-kubelet** — taints free/reserve in-cluster GPUs and a descheduler migrates production back slowly so it never drops. Scattered/heterogeneous GPU capacity made fungible for a media lab; convergent with b18 Jiang's "inference capacity becomes RL capacity" and Hooker's distributed-returns argument, from the media-training side | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-priority-gpu-scheduling`, `el-inference-on-bad-gpus` |
| `sig-researchers-dont-think-about-gpus` | infra | The abstraction goal that shaped the system: "I don't want my researchers to think about GPUs — they just launch stuff; if we have GPUs, we have GPUs; if not, it queues." Production runs at lower priority so research throughput isn't blocked, and the value extracted from GPUs doing training is judged higher than from production. An infra-as-product claim: the scarce resource is researcher iteration speed, and the platform's job is to hide capacity management entirely | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-priority-gpu-scheduling` |

## Insights (2 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-observe-the-fabric-not-the-gpu` | The transferable lesson is that at multi-node scale the binding constraint is the interconnect, not the accelerator, and the default dashboards hide exactly that — GPU-utilization flatters, while the InfiniBand/NVLink metrics that actually predict failure are unexported and must be built. Any team scaling past a single node that trusts the vendor's default utilization number is flying blind on the thing most likely to kill its runs, which is why "metrics are everything" is the first lesson rather than an afterthought | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** | `ReliesOnElement → el-training-metrics-truth`, `el-crash-and-resume-training` |
| `ins-durability-from-cheap-checkpoints` | Krea's answer to constant silent failure is the same shape as the durable-execution thread elsewhere in the corpus: don't prevent the crash, make recovery cheap and automatic — frequent checkpoints on fast storage plus "mark the pod failed and let Kubernetes recreate it." The spot-arbitrage system extends the same logic to capacity: treat every GPU as preemptible, flip work between clusters, and let the scheduler self-heal. Reliability is engineered as cheap resume, not as uptime | `HighlightsPattern → pat-durable-execution` **[registry]** | `ReliesOnElement → el-crash-and-resume-training`, `el-priority-gpu-scheduling` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-menezes-krea-infra`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-run-large-scale-media-training` | Run large-scale training on a shared cluster | Invest heavily in **metrics before anything else** — do not trust GPU-utilization (it reads 100% while under-utilized); use **tensor-core utilization** as the real efficiency proxy, pull any GPU over ~78°C immediately rather than debugging it, and build custom exporters for **InfiniBand and NVLink** (wait times, errors, packets) because NVIDIA doesn't export them and most multi-node failures are cross-node communication; expect constant, often silent crashes (NCCL timeouts with green metrics) and **let it crash** rather than node-swapping — the same machines often run fine for 12–24h after — while **checkpointing aggressively** (every 20–30 min) on a fast trusted filesystem, not Ceph; share one cluster between training and production with a **gang-scheduling queue** that gives training strict priority, evicting inference and flipping it to another cluster or rented GPUs via **virtual-kubelet**, using taints to reserve/free in-cluster GPUs and a **descheduler (not no-execute)** to migrate production back slowly so it never drops; run low-priority **diffusion inference on the worst, cheapest, most-preemptible GPUs** since it tolerates bad hardware; and hide all of this from researchers so they just submit jobs | `ReferencesElement → el-training-metrics-truth`, `el-crash-and-resume-training`, `el-priority-gpu-scheduling`, `el-inference-on-bad-gpus` |

## Dropped

- **The Krea 2 product framing** ("soulless AI images," open-source checkpoints, styles) — motivation; folded into `co-krea`. The research side is covered in the companion Lee talk (`lee-krea-training-krea2.md`).
- **The live-slide-advance heckle** — stagecraft.
- **The hiring pitch** — logistics (the `cerebra.ai` alias is likely a garble; see review note 3).

## Review notes

1. **The strongest media-track talk for the corpus's infra/durable-execution threads** — it lands on `pat-model-not-bottleneck` (value in the training/serving infra around the model) and `pat-durable-execution` (coined 2026-08-16: cheap-checkpoint-and-resume + self-healing scheduling is a clean product-side data point). Convergent with b18 Jiang (cross-cluster compute fungibility) and b14 Borucki (HF serving at scale).
2. **⚠ Verify before seeding:** GPU temperature threshold (~78°C); the ~1.8 TB/s read / 1 TB write filesystem figures; "Kueue" (captioned "Q"); "Ceph" (captioned "SEF"); the Meta failure-rate paper; and especially the hiring alias "cerebra.ai" — likely a mis-hearing of the krea.ai domain, NOT Cerebras. Confirm before it touches `co-krea`'s brief.
3. **Companion talk.** Sangwu Lee's `lee-krea-training-krea2.md` (same batch) covers the *research/data* side of the same Krea 2 model; this covers *infra*. Recommend widening `co-krea`'s brief to cover both at seeding.
