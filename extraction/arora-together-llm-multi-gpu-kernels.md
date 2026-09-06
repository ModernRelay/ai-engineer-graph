# SPIKE extraction — "Can LLMs Write Fast Multi-GPU Kernels?" (Simran Arora, Together AI) — FOR REVIEW

Source transcript: `transcripts/arora-together-llm-multi-gpu-kernels.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/pOvWgX7IJsc — AI Engineer World's Fair, published 2026-08-27.
`stagingTimestamp` for the artifact and all dated nodes: 2026-08-27 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Shape of the talk: a research talk from Together AI's frontier performance team (Hazy Research lineage; incoming Caltech professor). With FlashAttention-style kernels, memory-efficient architectures and better DSLs, the bottleneck moved from intra-GPU memory to **multi-GPU communication** — which hardware improved 2–3× while tensor cores improved 7.2× (A100 → B200). NCCL-style bulk collectives fall below 50% of the communication-aware roofline; DSLs can't keep up with networking changes; hand-tuned kernels take months per precision. Their answer: **Parallel Kittens**, a small set of primitives capturing the few real trade-offs (transfer mechanism, intra- vs inter-SM overlap, buffering/sync), in production at Together and Cursor. Then **ParallelKernelBench** (87 real-workload problems): the best frontier model solves 28/87 zero-shot (22 faster than PyTorch+NCCL), plateaus ~31% fast with sampling, succeeds only on internet-familiar patterns, and "does not understand how to reason through these trade-offs even when we provide them in context"; a mini-SWE-agent harness lifts solves to 35/87 then plateaus. Caption garbles: "Siman" → **Simran**, "Chris Ray" → **Chris Ré**, "nickel"/"Rickle" → **NCCL / RCCL**, "pietorch" → **PyTorch**, "tileang" → **TileLang**, "gluon" kept, "3D Taurus" → **3D torus**, "gem" → **GEMM**, "flashdoe" → ⚠ likely a fused-MoE kernel, "cutless" → **CUTLASS**, "mini sui agent" → **mini-SWE-agent**, "fast one at K" → **fast₁@k**, "Nemo vocab parallel" → NeMo vocab-parallel.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-arora-together-llm-multi-gpu-kernels` | Can LLMs Write Fast Multi-GPU Kernels? (Simran Arora, Together AI — AI Engineer World's Fair) | youtube | https://youtu.be/pOvWgX7IJsc |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-simran-arora`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-simran-arora` | Simran Arora (Principal Scientist, Together AI; incoming professor, Caltech; Hazy Research PhD) | `AffiliatedWithCompany → co-together-ai` **[registry]** |

## Companies (0 new)

Reused **[registry]**, edge-only: `co-together-ai` **[b15]** — new facts: a frontier performance research team building systems, frameworks and algorithms for hardware utilization; author of Parallel Kittens (in production at Together and at Cursor) and ParallelKernelBench. Reused `co-nvidia` (H100/B200, NVLink/NVSwitch, TMA, 72- and 576-GPU scale-up domains), `co-cursor` (production user of Parallel Kittens), `co-deepseek` (memory-efficient architectures; DeepSeek V4 Pro as the weakest model benchmarked), `co-openai` (GPT-5.5 as the best), `co-google` (Gemini 3 Pro in the agent harness), `co-amd` — *not coined* (XGMI, RCCL, HipKittens references), Stanford (Hazy Research), Caltech.

## Elements (5 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-multi-gpu-communication-bottleneck` | The bottleneck moved to multi-GPU communication | concept | infra | Years of work on intra-GPU efficiency — FlashAttention, Mamba and sparse attention, DSLs (TileLang, Mojo, Triton, Gluon, ThunderKittens), megakernels, multi-vendor ports — shifted the limit to networking: on production distributed training and inference, communication consumes most of the runtime and MFU is low at scale. A100 (2020) → B200 (2024): BF16 tensor-core speed 7.2×, intra-node communication 3×, inter-node 2×. Networking stacks are the least standardized part of the hardware (NVLink/NVSwitch with in-network reductions, AMD XGMI, TPU 3D torus with optical wraparound), workloads are disaggregating across hardware (KV cache across GPU/CPU/disk/remote; prefill/decode/speculation split), and scale-up domains are growing (72 GPUs; 576 planned for 2027) with device-initiated primitives (TMA) for fine-grained control |
| `el-parallel-kittens` | Parallel Kittens | framework | infra | A minimal set of primitives and templates for multi-GPU kernels, built by first doing the manual work to understand the trade-offs "rather than throwing an LLM at the problem." Roughly a dozen lines added over a single-GPU kernel; state-of-the-art versus strong baselines across data, sequence and expert parallelism; in production at Together AI and Cursor. The baselines it beats: PyTorch + NCCL bulk collectives (most problems below 50% of the communication-aware roofline; synchronization before and after transfers), DSLs like Triton-distributed that don't adapt across architectures (tuned on H800, fails on H100), and hand-tuned operators (DeepEP, Comet, ring attention, distributed GEMMs) that take five or six months to move to another precision |
| `el-multi-gpu-kernel-tradeoffs` | The few trade-offs that govern multi-GPU kernels | concept | infra | **Transfer mechanism**: the host-initiated copy engine (peak bandwidth on large messages, spares registers and SMs) vs device-initiated TMA (saturates NVLink with small messages, few registers/SMs — ideal for fine-grained overlap, but can't use in-network compute) vs register-level LD/ST/red-multimem instructions (can exploit NVSwitch reductions). **Overlap schedule**: intra-SM warp specialization (compute and communication warps sharing inputs — must align; wins on GEMM + reduce-scatter) vs inter-SM specialization (SMs dedicated to compute, communication or memory; wins on GEMM + all-reduce via in-network reductions, and when resources would split misaligned). **Buffering and synchronization** left under developer control |
| `el-parallel-kernel-bench` | ParallelKernelBench | technology | infra | 87 problems drawn from real workloads (GitHub repos, optimized libraries, DSL kernels) across a taxonomy of parallelism compositions (data, sequence, tensor, context, layer, pipeline, expert), each an unoptimized PyTorch + torch.distributed reference plus a topology spec, to be rewritten as a performant CUDA kernel with unified virtual addressing. Metrics: pass@k (correct) and **fast₁@k** (correct *and* faster than the PyTorch+NCCL baseline). Results: best frontier model zero-shot 28/87 correct, 22 faster; multiple samples raise correctness to ~36 but fast plateaus ~31%; GPT-5.5 best, DeepSeek V4 Pro bottom, all dropping fast as the speed-up threshold rises. Speed-ups come from replacing NCCL staging with direct NVLink loads/stores; successes concentrate on collectives, tensor-parallel GEMMs and Ulysses-style context parallelism — patterns heavily represented on the internet. A mini-SWE-agent harness with Gemini 3 Pro and bash raises solves from 24 to 35/87 (26 faster), then plateaus with more time. Early "signs of life": net-new kernels (a NeMo vocab-parallel filter, a Hyena context-parallel kernel, a SAM 3 IoU-suppression kernel) |
| `el-models-dont-reason-about-hardware-tradeoffs` | Models compile but don't reason about the trade-offs | concept | infra | With error feedback and sampling, models get kernels to compile, but "the deeper issues are not CUDA syntax": they struggle with collective ordering, data partitioning, intra- vs inter-SM scheduling and transfer-mechanism choice, rarely use register-level transfers or TMA, and fail to apply the principles "even when we provide them in context." Reasoning-model claims don't transfer from single-GPU benchmarks — "are we benchmaxxed on benchmarks of the past?" |

Element edges: all five `IdentifiedInArtifact → ia-aie-arora-together-llm-multi-gpu-kernels`.
`el-parallel-kittens` `DevelopedByCompany → co-together-ai` **[registry]**;
`el-parallel-kernel-bench` `DevelopedByCompany → co-together-ai` **[registry]**;
`el-parallel-kittens` `UsesElement → el-multi-gpu-kernel-tradeoffs`, `el-multi-gpu-communication-bottleneck`;
`el-parallel-kernel-bench` `UsesElement → el-pass-at-k` **[registry]**, `el-mini-swe-agent` **[registry]**, `el-models-dont-reason-about-hardware-tradeoffs`;
`el-models-dont-reason-about-hardware-tradeoffs` `UsesElement → el-multi-gpu-kernel-tradeoffs`;
`el-multi-gpu-communication-bottleneck` `UsesElement → el-deepgemm` **[registry]**;
`el-parallel-kernel-bench` `ExemplifiesPattern → pat-benchmark-trust-crisis` **[registry]**;
`el-parallel-kittens` `ExemplifiesPattern → pat-harness-over-model` **[registry]**.

Reused elements (no new nodes): `el-pass-at-k` **[registry]**, `el-mini-swe-agent` **[registry]**, `el-deepgemm` **[registry]** (DeepSeek's kernel lineage), `el-rollout-serving` **[registry]** (disaggregated inference), `el-benchmark-as-software` **[registry]**.

## Signals (4 new)

All: `SpottedInArtifact → ia-aie-arora-together-llm-multi-gpu-kernels`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-together-ai` **[registry]**.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-frontier-models-cannot-write-fast-multi-gpu-kernels` | infra | On 87 real multi-GPU problems the best frontier model (GPT-5.5) solves 28 zero-shot with 22 faster than PyTorch+NCCL; sampling lifts correctness to ~36 but "fast" plateaus around 31%; successes are the internet-familiar patterns. Models compile with feedback but don't reason about collective ordering, partitioning, SM scheduling or transfer mechanisms even with the principles in context — "benchmaxxed on single-GPU benchmarks of the past." A measured limit on autonomous systems research at the hardware frontier | `FormsPattern → pat-benchmark-trust-crisis` **[registry]**; `ContradictsPattern → pat-accelerated-research` **[registry]** | `OnElement → el-parallel-kernel-bench`, `el-models-dont-reason-about-hardware-tradeoffs` |
| `sig-agent-harness-lifts-kernel-solves-then-plateaus` | infra | Wrapping Gemini 3 Pro in a mini-SWE-agent loop with a bash environment (the Claude Code shape) raised solved problems from 24 to 35 of 87, 26 faster than baseline — then plateaued as time scaled; "additional techniques would be required." The harness buys a step, not a curve, when the model lacks the underlying reasoning | `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-parallel-kernel-bench`, `el-mini-swe-agent` **[registry]** |
| `sig-principles-first-then-primitives-beat-llm-first` | infra | The team's method: do the manual work to find the small set of trade-offs governing multi-GPU kernels, encode them as Parallel Kittens primitives (a dozen lines over a single-GPU kernel, state-of-the-art across parallelism schemes, in production at Together and Cursor), and only then ask whether models can use them. Human systems judgement produced the reusable abstraction the models could not | `FormsPattern → pat-value-of-judgement` **[registry]**; `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-parallel-kittens`, `el-multi-gpu-kernel-tradeoffs` |
| `sig-bottleneck-shifted-to-gpu-networking` | infra | Compute improved 7.2× A100→B200 while intra-node communication improved 3× and inter-node 2×; communication now dominates production distributed training and inference runtime; networking stacks are the least standardized layer across vendors; workloads disaggregate across hardware and scale-up domains head to 576 GPUs. NCCL-style bulk collectives sit below half the roofline, DSLs can't track the hardware, hand-tuning takes months per precision — the frontier of AI efficiency is the interconnect | | `OnElement → el-multi-gpu-communication-bottleneck`, `el-deepgemm` **[registry]** |

## Insights (1 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-hardware-tradeoff-reasoning-is-where-models-stop` | The durable finding is a boundary on autonomous research: given a real benchmark where success requires reasoning about a handful of hardware trade-offs, frontier models reproduce the patterns they have seen and stall on the ones they haven't — even with the trade-offs supplied — and an agent harness moves the number once, not continuously. The corpus's accelerated-research thesis gets a measured counter at exactly the layer (interconnect-bound kernels) where the next efficiency gains live | `HighlightsPattern → pat-benchmark-trust-crisis` **[registry]** | `ReliesOnElement → el-parallel-kernel-bench`, `el-models-dont-reason-about-hardware-tradeoffs`, `el-parallel-kittens` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-arora-together-llm-multi-gpu-kernels`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-approach-multi-gpu-kernels-with-and-without-llms` | Learn the trade-offs by hand, encode them as primitives, then test the models on real problems | Recognize the bottleneck has moved to communication and study the baselines first — bulk collectives (NCCL/RCCL) usually sit under half the communication-aware roofline; do the manual work to identify the few governing trade-offs — transfer mechanism (copy engine vs TMA vs register-level instructions with in-network reductions), intra- vs inter-SM overlap, buffering/sync — and encapsulate them as reusable primitives (Parallel Kittens: ~a dozen lines over a single-GPU kernel); benchmark models on **real** workload problems with a topology spec and two metrics, pass@k and fast₁@k, and expect zero-shot success only on internet-familiar patterns; use an agent harness with a bash environment for a one-time lift but don't expect it to scale with more time; watch for the failure modes — collective ordering, partitioning, scheduling, mechanism choice — rather than CUDA syntax; and keep human systems judgement in the loop for the net-new kernels | `ReferencesElement → el-multi-gpu-communication-bottleneck`, `el-multi-gpu-kernel-tradeoffs`, `el-parallel-kittens`, `el-parallel-kernel-bench`, `el-models-dont-reason-about-hardware-tradeoffs` |

## Dropped

- **The H100 die tour** (SMs, L2, HBM, register bandwidth ~130 TB/s) — preliminaries; folded into the bottleneck element as needed.
- **The GEMM + reduce-scatter vs GEMM + all-reduce example** — one clause in the trade-offs element.

## Review notes

1. **⚑ `ContradictsPattern → pat-accelerated-research`** is deliberate and measured: 28/87 zero-shot, ~31% fast plateau, harness lift then plateau, at the systems layer that gates inference/RL efficiency. The pattern (coined on Karpathy loops, AlphaEvolve, Tao's proofs) needs this boundary condition in its brief.
2. **`sig-bottleneck-shifted-to-gpu-networking` is held pattern-less** — infrastructure texture with no coined home; relates to the uncoined `pat-compute-liquidity` (b18) only loosely. Recorded as a ledger entry for an infra thread.
3. **⚠ Verify before seeding:** the 7.2× / 3× / 2× figures, 28/87 and 22, ~36 and ~31%, 24→35 and 26, "GPT-5.5" and "DeepSeek V4 Pro" as benchmarked, 72/576-GPU domains, and the production use at Cursor.
