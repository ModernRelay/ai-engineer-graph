# SPIKE extraction — "From fork() to Fleet: Designing an Agent Sandbox Cloud" (Abhishek Bhardwaj, OpenAI) — FOR REVIEW

Source transcript: `transcripts/bhardwaj-openai-agent-sandbox-cloud.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/OqM67QG_Ikk — AI Engineer World's Fair, published 2026-07-13.
`stagingTimestamp` for the artifact and all signals: 2026-07-13 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-bhardwaj-agent-sandbox-cloud` | From fork() to Fleet: Designing an Agent Sandbox Cloud (Abhishek Bhardwaj, OpenAI — AI Engineer World's Fair) | youtube | https://youtu.be/OqM67QG_Ikk |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-abhishek-bhardwaj`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-abhishek-bhardwaj` | Abhishek Bhardwaj (RL & agent infrastructure team, OpenAI; ex-Google, worked on CrosVM; builds sandbox infra for ChatGPT / Codex Web) | `AffiliatedWithCompany → co-openai` **[registry]** |

## Companies (0 new)

- `co-openai` **[registry]** — reused, no new node.

## Elements (3 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-microvm` | Micro VM | technology | infra | Hardware-virtualized minimal VM run by a lean Rust-based VMM (CrosVM → Firecracker / Cloud Hypervisor lineage): small memory footprint, fast boot, jailed virtio devices; isolation guaranteed at the CPU level (VMX root vs non-root), so even guest ring-0 compromise does not yield the host |
| `el-gvisor` | gVisor | technology | infra | User-space application kernel (Sentry, Go) plus file-system daemon (Gofer) that intercepts and services syscalls, shrinking the host-kernel attack surface; still sits on the host kernel, so a two-step chained exploit remains reachable | 
| `el-sandbox-snapshotting` | Sandbox disk snapshotting | concept | infra | Incremental, block-level checkpoint/restore of an agent sandbox's disk (copy-on-write base image + changed-extent diffs with lineage, uploaded to object storage): makes sandboxes survivable across node death, migratable across a fleet, and forkable for backtracking search |

Element edges:
- `el-gvisor` `DevelopedByCompany → co-google` **[registry]**
- `el-microvm`, `el-gvisor`, `el-sandbox-snapshotting` `IdentifiedInArtifact → ia-aie-bhardwaj-agent-sandbox-cloud`
- `el-microvm` `EnablesElement → el-sandbox-snapshotting` (memory snapshots + block-device model make cheap checkpoint/restore possible)
- `el-firecracker` **[registry]** — reused; mentioned as the Amazon fork of CrosVM powering Lambda; no redefinition.
- `el-openclaw` **[registry]** — reused (see `sig-agents-leave-laptops`).

## Signals (4 new)

All: domain `infra`, `SpottedInArtifact → ia-aie-bhardwaj-agent-sandbox-cloud`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | FormsPattern | other edges |
|---|---|---|---|
| `sig-sandbox-vm-convergence` | "Seven stages of sandboxing" (paraphrase): OpenAI's sandbox-infra lead reports every serious agent-sandbox effort converges on hardware-virtualized micro VMs after exhausting fork/exec, containers+seccomp, gVisor, and V8 isolates — every non-VM primitive still exposes the shared host kernel; OpenAI runs ChatGPT / Codex Web untrusted code on micro VMs | `FormsPattern → pat-new-cyber-threats` **[registry]** | `OnElement → el-microvm`, `RelevantCompany → co-openai` |
| `sig-models-as-exploit-chainers` | The sandbox threat model now includes the model itself: frontier models are getting good at reading bug reports and chaining multi-step exploits (e.g. Sentry→kernel), and "overzealous" models may attempt privilege escalation just to be helpful — unintentional attacks are in scope alongside malicious ones | `FormsPattern → pat-new-cyber-threats` | `RelevantCompany → co-openai` |
| `sig-agents-leave-laptops` | The OpenClaw wave — agents run on laptops with lids held open, rented Hetzner VPSs, and Mac minis in the cloud — read as "a slap in the face for 20 years of cloud computing" (paraphrase) and a preview: persistent, long-running agents will move into purpose-built sandbox clouds | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-openclaw` **[registry]** |
| `sig-storage-next-unlock` | Compute (a Linux box) was the first agent unlock; durable disk is the next: incremental snapshot/restore already supports multi-day Codex "gold mode" runs (speaker's record: 3 days) and enables Monte-Carlo-style checkpoint/backtrack exploration over many days — pitched as the primitive needed for drug-discovery-length agent tasks | `FormsPattern → pat-harness-over-model` **[registry]** (parked — see review note 2) | `OnElement → el-sandbox-snapshotting` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-security-cannot-be-retrofitted` | System tricks can cover performance problems but cannot hide a security breach, and trust is lost only once — so pick the most secure isolation primitive (micro VMs) first and buy back performance later, rather than climbing the container→gVisor→VM ladder in production | `HighlightsPattern → pat-new-cyber-threats` | `ReliesOnElement → el-microvm` |
| `ins-snapshots-as-scheduling-primitive` | Snapshot lineage doubles as an orchestration signal: score/route a restore to the node already holding the most snapshot layers, and hybrid warm-pool + memory-snapshot creation gets millisecond starts — persistence unifies reliability, scale, and search rather than being a bolt-on | `HighlightsPattern → pat-harness-over-model` | `ReliesOnElement → el-sandbox-snapshotting` |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-bhardwaj-agent-sandbox-cloud`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-pick-microvms-first` | Skip the seven stages: micro VMs from day one | Never bare fork/exec (kernel exposure + noisy neighbor); containers (namespaces/cgroups + seccomp) still share the host kernel and seccomp allowlists break agent products; gVisor leaves a two-step chain to the host; use a Rust-based micro VM with jailed virtio devices; accept the trade-offs — VM-exit overhead, reactive balloon-driver memory reclaim, GPU passthrough (VFIO) is single-tenant | `ReferencesElement → el-microvm`, `el-gvisor` |
| `how-design-sandbox-snapshotting` | Design sandbox persistence as incremental block-level snapshotting | Snapshot only diffs (never full gigabytes per turn); make the snapshot API cheap enough to call constantly — return before upload finishes; restore = create-from-snapshot, must be as fast as create; explicit save: CoW zero-copy layer over a base image + FIEMAP changed-extent bundling; always-on save: NBD block device over a tiered in-cluster cache writing back to object storage (avoid NFS — not performant, not POSIX-enough for models trained on POSIX) | `ReferencesElement → el-sandbox-snapshotting` |

## Dropped

- CrosVM, Cloud Hypervisor, QEMU, seccomp, virtio, NBD, FIEMAP, XFS reflinks — mechanism-level names kept as prose inside elements/knowhow; only `el-firecracker` already exists as a node.
- Kubernetes / control-plane / regional-cluster orchestration section — generic architecture, folded into `ins-snapshots-as-scheduling-primitive`.
- "Research wants throughput, product wants latency, both want reliability+security" framing — context, not a signal.

## Review notes

1. **Model-name garble**: "these models uh of like 5.6" — unresolved auto-caption garble (possibly a GPT version); left out of all nodes. "how many hours in strawberry" = "how many R's in strawberry". "gold mode in Codex" kept as-heard (paraphrase) — verify the real feature name before publication.
2. **`pat-durable-execution` resonance (strong)**: `sig-storage-next-unlock` + `ins-snapshots-as-scheduling-primitive` are a THIRD independent data point for the registry's at-threshold candidate "durable runtime as a stack layer" (after ZenML Kitaru and Inngest) — and the first from a frontier lab. Signals parked on `pat-harness-over-model` per convention; if `pat-durable-execution` is coined at review, rehome `sig-storage-next-unlock` there.
3. `sig-storage-next-unlock` also brushes `pat-accelerated-research` (multi-day Monte-Carlo rollouts "to solve diseases"); a second FormsPattern edge is defensible if you want it.
4. `el-microvm` vs existing `el-firecracker`/`el-microsandbox`: kept as the generic technology node since the talk's thesis is about the class, not one product. Add `el-firecracker UsesElement → el-microvm`-style edges at reconciliation if desired.
