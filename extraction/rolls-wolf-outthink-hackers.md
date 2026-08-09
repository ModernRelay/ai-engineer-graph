# SPIKE extraction — "Training Frontier Models to Out-Think Hackers" (Uri Rolls, Arithmetic & Thom Wolf, Hugging Face) — FOR REVIEW

Source transcript: `transcripts/rolls-wolf-outthink-hackers.txt` (auto-captions — quotes are paraphrases, not verbatim; speaker "Yuri"/"Fury" → **Uri Rolls**, "Thomas" → **Thom Wolf**; company "arithmetic" and benchmark "Masov"/"Bach" are caption-sourced — see Review notes).
Video: https://youtu.be/O-CBZ3JtRvo · published 2026-07-24 (AI Engineer, World's Fair).
`stagingTimestamp` for the artifact and all signals: 2026-07-24 (publish date).
Entities marked **[registry]** already exist — edges link, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-rolls-wolf-outthink-hackers` | Training Frontier Models to Out-Think Hackers (Uri Rolls & Thom Wolf — AI Engineer World's Fair) | youtube | https://youtu.be/O-CBZ3JtRvo |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-uri-rolls`, `ContributedByExpert → exp-thom-wolf`.

## Experts (2 new)

| slug | name | AffiliatedWithCompany |
|---|---|---|
| `exp-uri-rolls` | Uri Rolls (founder, Arithmetic; Harvard dropout; leads a team of vulnerability researchers building AI cyber capabilities) | `co-arithmetic` |
| `exp-thom-wolf` | Thom Wolf (co-founder & CSO, Hugging Face; advised on the benchmark) | `co-hugging-face` **[registry]** |

## Companies (1 new; 1 registry reuse)

| slug | name | type | note |
|---|---|---|---|
| `co-arithmetic` | Arithmetic | developer | AI cyber-security startup: builds black-box cyber-capability benchmarks and aims to post-train (open-source) models to defend faster than attackers can exploit |
| **[registry]** `co-hugging-face` | Hugging Face | developer | Thom Wolf's company; open-source model advocate in the talk |

## Elements (3 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-masov-benchmark` | Masov (access-control exploitation benchmark) | framework | security | Arithmetic's first released benchmark: a black-box, live-environment eval where a low-privileged agent must exploit real, self-found zero-days chained across real applications (Keycloak → Vault → broker) to escalate privilege; the model sees neither the code nor the vuln and has no internet/codebase access, only basic execution tooling; extremely hard (one solve at K1) (⚠ name caption-sourced — see Review note 3) |
| `el-deterministic-partial-grading` | Deterministic partial grading | concept | security | Grading scheme for long-horizon exploitation tasks: a binary pass grader ("did the underprivileged user do something it wasn't allowed to?") plus per-step deterministic graders across the whole discovery→exploitation chain, so you can measure exactly how deep a model got even when it fails the final leap |
| `el-access-control-vulnerabilities` | Access-control logic vulnerabilities | concept | security | The #1 OWASP vulnerability class (~$30B industry): logic-based access breaks (not code bugs) where two very large systems check the same thing differently and a seam lets a low-privileged user reach privileged actions — requires reasoning across the system, not pattern-matching |

Element edges: `el-masov-benchmark` `DevelopedByCompany → co-arithmetic`; `el-masov-benchmark` `UsesElement → el-deterministic-partial-grading`; all three `IdentifiedInArtifact → ia-aie-rolls-wolf-outthink-hackers`.

## Signals (4 new)

All: `SpottedInArtifact → ia-aie-rolls-wolf-outthink-hackers`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | domain | FormsPattern | OnElement | RelevantCompany |
|---|---|---|---|---|---|
| `sig-cyber-offense-economics-shifting` | The economics of cyber are shifting dramatically: frontier models find primitives and zero-day exploits at scale, so a skilled attacker can now choose many targets at once; defensive systems must operate at scale with very limited human intervention, so defenders are bound by out-of-the-box model capability — the 20-year cyber stack was built on the opposite assumption (attackers must pick targets, defenders react) | security | `pat-new-cyber-threats` **[registry]** | `el-access-control-vulnerabilities` | `co-arithmetic` |
| `sig-access-control-exploit-benchmark-hard` | Arithmetic's Masov — a black-box access-control exploitation benchmark built from self-found zero-days chained across real services — is incredibly hard: only one solve at K1; at K5 only GPT-5.5 solves; models capture nearly all discovery-phase information but can't make the exploitation "leap" (e.g. rename the admin to inherit its name-checked privilege); ~16-step logic requires holding a live model of a permissioning system where each action changes state | security | `pat-new-cyber-threats` **[registry]** | `el-masov-benchmark`, `el-access-control-vulnerabilities` | `co-arithmetic`, `co-openai` **[registry]**, `co-anthropic` **[registry]** |
| `sig-models-cant-build-world-model` | Wolf's framing (anchored to ARC-AGI-3 / "RKGI3"): current frontier models score ~1-2% on generic world-model games because they can't build a dynamic model of any world on the fly; the cyber benchmark is hard for the same reason — the model must understand and act on a world model it builds live, not pattern-match | security | `pat-new-cyber-threats` **[registry]** | `el-masov-benchmark` | `co-arithmetic` |
| `sig-open-source-models-for-cyber-defense` | Proposed answer to shifting offense economics: the defense must be the models themselves — specifically an array of strong open-source models, post-trained per-environment for cyber and run fast on specialized hardware, made available to every company, rather than relying on "two companies everyone knows"; speed (attacker vs defender) is the decisive variable | security | `pat-new-cyber-threats` **[registry]** | `el-masov-benchmark` | `co-arithmetic`, `co-hugging-face` **[registry]** |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-defense-must-be-model-native` | The only way to replace the old cyber stack is through the models: with very high-quality evals, data, and benchmarks plus post-training, defenders can be made to out-perform attackers durably — because doing the exploitation leap fast and reliably is a lasting capability attackers don't uniquely have | `pat-new-cyber-threats` **[registry]** | `el-masov-benchmark` |
| `ins-humans-find-oob-then-models-scale` | Data quality is the lever: finding out-of-distribution zero-days still needs human vulnerability researchers; humans discover novel exploits in widely-used open-source software, which become deterministically-graded black-box environments used to post-train models to reason (not pattern-match) across an entire attack surface | `pat-new-cyber-threats` **[registry]** | `el-deterministic-partial-grading` |

## KnowHow (1 new)

`SourcedFromArtifact → ia-aie-rolls-wolf-outthink-hackers`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-blackbox-cyber-eval` | Build cyber-capability evals as black-box, self-found-zero-day environments | Find your own zero-days in widely-used open-source software (submit to maintainers); chain real applications/services into a live black-box environment where the model sees neither code nor the vuln; deny internet and codebase access but give the basic execution tooling a real attacker would use; make every step deterministically gradable — a binary "did it do something an underprivileged user shouldn't?" grader plus per-step partial graders — so you can measure how deep in the exploitation chain the model reaches; keep tasks long-horizon (16+ step logic) to test live world-model-holding, not pattern-matching | `el-masov-benchmark`, `el-deterministic-partial-grading`, `el-access-control-vulnerabilities` |

## Dropped

- "Mythos" (the static "read the code and find the vulnerabilities" approach the benchmark is contrasted against) — passing reference, likely a caption garble; kept in prose, no element (not `el-claude-mythos-preview` **[registry]**, which is unrelated).
- "Bach" (Arithmetic's internal eval orchestrator) — internal tooling named in the live demo; folded into prose, no node.
- Eugene "from Entropic" credited for the eval graphic (inputs → agent [model+harness+black-box tooling] → verifiable grader → per-step deterministic grading) — likely `exp-eugene-yan` **[registry]** / Anthropic; a graphic credit, not load-bearing content; noted here, no edge.
- "Fall time" failure-mode trace (3-hour unsolved run) — demo illustration.

## Review notes

1. Two-speaker talk: `exp-uri-rolls` (Arithmetic, presents the benchmark) + `exp-thom-wolf` (Hugging Face, framing/advisory). Both `ContributedByExpert`.
2. **Company name "Arithmetic" — flagged.** The transcript renders it lowercase and uses it consistently as the company ("a benchmark that arithmetic ... has been developing", "our goal in arithmetic"), so the transcript *does* support it, but it is caption-sourced — verify spelling/capitalization before public-facing use.
3. **Benchmark name "Masov" — caption-uncertain.** Rendered "Masov" once ("excited to show you Masov"); the internal orchestrator is "Bach". Both are auto-caption best-guesses; verify before seeding. Kept as one element (`el-masov-benchmark`) because the benchmark's construction is the talk's durable content.
4. All four signals `FormsPattern → pat-new-cyber-threats` **[registry]** (seed brief: "AI models exploiting vulnerabilities autonomously + agentic enterprise attack surfaces; capability jumps are discontinuous"). `sig-open-source-models-for-cyber-defense` also resonates with `pat-sovereign-ai` **[registry]** (open-weight models as strategic necessity, not relying on two labs) — noted, not edged, to keep one pattern home.
5. Model result strings ("GPT 5.5", "opus") are auto-transcribed; `co-openai`/`co-anthropic` **[registry]** attached as `RelevantCompany` on the results signal only.
