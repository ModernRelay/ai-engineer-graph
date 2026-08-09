# SPIKE extraction — "The AI Bugpocalypse Is Here. Now What?" (Jack Cable, Corridor) — FOR REVIEW

Source transcript: `transcripts/cable-corridor-ai-bugpocalypse.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/7JgIS42mz7U — AI Engineer World's Fair, published 2026-07-12.
`stagingTimestamp` for the artifact and all signals: 2026-07-12 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-cable-bugpocalypse` | The AI Bugpocalypse Is Here. Now What? (Jack Cable, Corridor — AI Engineer World's Fair) | youtube | https://youtu.be/7JgIS42mz7U |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-jack-cable`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-jack-cable` | Jack Cable (co-founder & CEO, Corridor; former senior technical advisor at CISA — secure-by-design initiative; ethical hacker, top-100 HackerOne rank; Stanford CS) | `AffiliatedWithCompany → co-corridor` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-corridor` | Corridor | developer | AI-coding security startup (~founded early 2025, "about 18 months ago"); prevents vulnerabilities before the pull request + gives visibility into AI coding-tool usage |

**[registry]** reused: `co-anthropic` (Mythos benchmark chart, Fable safeguards), `co-google` (Android memory-safety data).

## Elements (3 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-secure-by-design` | Secure by design | concept | security | CISA-originated doctrine (March 2023 paper Cable co-authored): build systems fundamentally resilient to known vulnerability classes rather than patching one-off; in the AI era, the frame for making AI the default code writer without exponential vulnerability growth |
| `el-memory-safe-languages` | Memory-safe languages | technology | security | Languages (Rust, Go — anything not C/C++) whose guarantees make memory-safety vulnerabilities impossible to introduce; ~60–70% of vulns in memory-unsafe products preventable; a control that holds no matter how smart attack models get |
| `el-baxbench` | BaxBench | framework | security | Academic benchmark (ETH Zurich / UC Berkeley, backsbench.com per captions) measuring security of LLM-written code; finds even the best models introduce vulnerabilities ~20–40% of the time |

Element edges: all three `IdentifiedInArtifact → ia-aie-cable-bugpocalypse`; `el-secure-by-design` `UsesElement → el-memory-safe-languages`.

## Signals (5 new)

All: domain `security`, `SpottedInArtifact → ia-aie-cable-bugpocalypse`, `SourcedFromSource → source-aie-yt`.

| slug | name / brief | FormsPattern | other edges |
|---|---|---|---|
| `sig-frontier-models-attack-chains` | Frontier models now find and exploit vulnerabilities better than a top-100-ranked human hacker (Cable's self-assessment); Anthropic's own chart shows Mythos executing increasingly autonomous attack chains; open-source libraries are the adversary's proving ground because anyone can run a smart model against them | `FormsPattern → pat-new-cyber-threats` **[registry]** | `RelevantCompany → co-anthropic` |
| `sig-ai-code-vuln-introduction-rate` | Even top models introduce vulnerabilities 20–40% of the time when writing code (BaxBench); Opus 46 introduced a smart-contract bug that cost a couple million dollars; introduced vulns are shifting from one-liner classes to contextual authorization/business-logic bugs the model has no company context for | `FormsPattern → pat-new-cyber-threats`, `FormsPattern → pat-verification-gap` **[registry]** | `OnElement → el-baxbench` |
| `sig-android-memory-safety-drop` | Google's Android data: memory-safety share of vulns fell ~75% (2019) → ~30% (2022) just by writing *new* code in memory-safe languages, no rewrite required — cited as proof that fundamental controls scale against AI-powered attackers | `FormsPattern → pat-new-cyber-threats` | `OnElement → el-memory-safe-languages`, `RelevantCompany → co-google` |
| `sig-ai-review-inflection` | Corridor's bet: within 6–12 months the majority of shipped code will be reviewed by AI, not humans — code review is now the bottleneck as agents run autonomously for hours from Slack, "and we're not going to accept that for very long" (paraphrase) | `FormsPattern → pat-verification-gap` | `RelevantCompany → co-corridor` |
| `sig-mythos-fable-export-controls` | 2026: export controls imposed on the Mythos and Fable frontier models; industry letter urged the White House to lift them (defender benefit outweighs risk; Anthropic added defender-skewed safeguards to Fable); distillation attacks are collapsing the closed-to-open-weight lag anyway; Cable testified to Congress days before the models shipped, recommending an American open-weight frontier ecosystem | `FormsPattern → pat-new-cyber-threats`, `FormsPattern → pat-sovereign-ai` **[registry]** | `RelevantCompany → co-anthropic` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-rewrites-beat-whack-a-mole` | Pouring millions into one-off AI vuln discovery in open-source libraries is whack-a-mole; a one-time rewrite of critical libraries into memory-safe languages gives programmatic guarantees that hold even as attack models get smarter — spend defender-AI capacity on fundamental controls, not patches | `HighlightsPattern → pat-new-cyber-threats` | `ReliesOnElement → el-memory-safe-languages` |
| `ins-security-cannot-be-the-blocker` | Acceleration always wins: the security-team question is no longer whether to allow coding agents but how to add guardrails, because autonomous development and AI-merged code only get a blessing if security tooling gives assurance without slowing anyone down | `HighlightsPattern → pat-verification-gap` | `ReliesOnElement → el-secure-by-design` |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-cable-bugpocalypse`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-secure-ai-coding-guardrails` | Put guardrails around coding agents, not gates | Prevent vulnerabilities *before* the pull request rather than after; give security teams visibility into how AI coding tools are used; hold AI-authored code to controls that let review itself be automated; never position security as the blocker on development acceleration | `ReferencesElement → el-secure-by-design` |
| `how-harden-open-source-foundation` | Harden the open-source foundation systemically | Treat open source as the adversary's proving ground; go beyond one-off discoveries/patches to systemic fixes; prioritize one-time memory-safe rewrites of critical libraries (guarantees survive smarter future models); pair with frontier-model-driven discovery for what remains | `ReferencesElement → el-memory-safe-languages`, `ReferencesElement → el-secure-by-design` |

## Dropped

- CISA as a Company node — the Company `type` enum (bigtech/developer/investor/research/hardware/media) has no slot for a government agency; kept in `exp-jack-cable`'s bio prose.
- MITRE top-exploited vulnerability-class list, Stack Overflow adoption stats (84% of developers, 30–40% of companies, "last year") — supporting statistics folded into signal/insight prose; not independently dated enough to carry their own signal.
- Cursor / Copilot / Claude Code name-drops — adoption color, no load-bearing content; no edges.
- "Opus 46" smart-contract incident as its own signal — folded into `sig-ai-code-vuln-introduction-rate`.

## Review notes

1. **Caption garbles:** "Backsbench"/"backsbench.com" is rendered as **BaxBench** (matches the real ETH Zurich secure-codegen benchmark); "Quarter" (line ~130) is clearly Corridor; the letter leader's name "Mikayla Gyalcsamis" is garbled beyond confident recovery — left out of the graph entirely, flag if the name matters.
2. Confirmed against transcript per the brief: Jack Cable is ex-CISA (senior technical advisor, secure-by-design initiative) and Corridor is his AI-coding-security startup — matches.
3. `sig-android-memory-safety-drop` is a pre-AI (2019–2022) datapoint deployed as an argument in an AI-era talk. Kept because it is concrete, dated, attributable, and load-bearing for the talk's thesis; drop to insight prose if your signal bar requires AI-era facts.
4. `sig-mythos-fable-export-controls` double-links `pat-new-cyber-threats` + `pat-sovereign-ai`. The sovereign link rests on the "American-made open-weight frontier models as a competitiveness requirement" recommendation; cut it if you read pat-sovereign-ai more narrowly.
5. No new pattern coined. The talk's dual-use/defender-acceleration thesis sits comfortably inside `pat-new-cyber-threats`.
