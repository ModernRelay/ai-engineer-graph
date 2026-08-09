# SPIKE extraction — AI Engineer security track (3 talks) — FOR REVIEW

Source transcripts: `transcripts/` (auto-captions — quotes are paraphrases, not verbatim).
Slugs follow the existing seed conventions (`sig-`, `pat-`, `el-`, `ins-`, `how-`, `co-`, `exp-`, `source-`, `ia-`).
Entities marked **[existing]** are already in `seed.jsonl` — edges link to them, no new node.
`stagingTimestamp` for all three artifacts: 2026-07-20 (video publish date).
Every Signal/KnowHow carries provenance edges to its artifact per the schema contract.

---

## InformationArtifacts (3 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-manoj-ai-fog` | Through the AI Fog: The Architectural Decision Agentic Security Depends On (Manoj Nair, AI Engineer World's Fair security track) | youtube | https://youtu.be/1EZdpEhwmNc |
| `ia-aie-yegge-agent-supply-chain` | Agentic Security: Permissions, Provenance, and the Agent Supply Chain (Steve Yegge) | youtube | https://youtu.be/yWS0udrIOc8 |
| `ia-aie-tanzer-agentic-dev-security` | Agentic Development Security (Ezra Tanzer + Dan Arpino demo) | youtube | https://youtu.be/cgimkNGNjvU |

Edges: all three `PublishedBySource → source-aie-yt`; `ContributedByExpert` → their speakers (below).

## SourceEntity (1 new)

- `source-aie-yt` — **AI Engineer** — type: `video_channel`, platform: YouTube, url: https://www.youtube.com/@aiDotEngineer

## Experts (4 new)

| slug | name | AffiliatedWithCompany |
|---|---|---|
| `exp-manoj-nair` | Manoj Nair (Snyk Chief Innovation Officer/CTO; ex-HPE/Dell/RSA) | `co-snyk` |
| `exp-steve-yegge` | Steve Yegge (author of the vibe-coding book; Gas Town/beads) | — (independent; spoke "on behalf of Snyk", unpaid) |
| `exp-ezra-tanzer` | Ezra Tanzer (Product Director, Snyk) | `co-snyk` |
| `exp-dan-arpino` | Dan Arpino (Software Engineer, Snyk ADS platform) | `co-snyk` |

## Companies (4 new; several existing reused)

| slug | name | type | note |
|---|---|---|---|
| `co-snyk` | Snyk | developer | 5,000 enterprise customers, half of Fortune 500; acquired Invariant Labs |
| `co-chainguard` | Chainguard | developer | pre-vetted, continuously updated base images |
| `co-replit` | Replit | developer | referenced for the agent DB-deletion incident |
| `co-github` | GitHub | developer | MCP-server exploit + internal-repo exfiltration incidents |
| **[existing]** `co-anthropic` | — | — | Claude / Claude Code references |

> Review call: Invariant Labs (acquired by Snyk), Labelbox and the unnamed
> "Mag 7" company appear only inside signal descriptions — I left them as
> prose, not Company nodes. Promote if you want them queryable.

## Elements (9 new; 1 existing reused)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-agent-skills` | Agent skills | technology | harness | Shareable natural-language capability packages for agents (SKILL.md + files); higher default privilege than code packages, NL payloads evade code scanners, can persist via agent memory |
| `el-agent-hooks` | Agent lifecycle hooks | technology | harness | Deterministic interception points on agent tool calls / session events; fire scans and policy checks without consuming context tokens |
| `el-generator-validator-separation` | Generator/validator separation | concept | security | The generating model must not be its own validator; independent (often deterministic) verification is load-bearing — "the architectural decision agentic security depends on" |
| `el-slopsquatting` | Slopsquatting | concept | security | Attackers publish real packages under names LLMs hallucinate; the download builds, tests pass, and ships a backdoor |
| `el-snyk-evo` | Snyk Evo | product | security | Snyk's open agentic security platform (OODA-loop framing); risk DB, red-teaming, agent guard |
| `el-snyk-ads` | Snyk Agentic Dev Security | product | security | GA'd offering: secures what agents generate (code), use (skills/MCP), and do (behavior policies: steer/ask/block) |
| `el-snappy` | Snappy | product | security | Dan Arpino's local Electron watcher: inventories running LLMs/MCPs/skills, per-workspace guardrails, blocks secret reads, audits agent file/command activity |
| `el-chainguard-images` | Chainguard Images | product | security | Pre-vetted vulnerability-free base images, continuously updated — "your inputs" side of the supply chain |
| `el-beads` | Beads | framework | harness | Yegge's task tracker for long-running agent loops; queue work, agents claim it (Gas Town = "a beads machine"); planned donation to the Agentic Foundation |
| **[existing]** `el-mcp` | Model Context Protocol | — | — | reused for edges |

Element edges: `el-snyk-evo`/`el-snyk-ads`/`el-snappy` DevelopedByCompany → `co-snyk`; `el-chainguard-images` → `co-chainguard`; `el-agent-hooks` EnablesElement → `el-snyk-ads`; `el-snappy` UsesElement → `el-agent-hooks`; `el-slopsquatting` ExemplifiesPattern → `pat-agent-supply-chain`; `el-generator-validator-separation` EnablesPattern → `pat-verification-gap`.

## Patterns (2 new; 1 existing reused) — recalibrated to seed altitude

> Seed patterns are named industry-level theses (SaaSpocalypse, Sovereign AI…).
> The five narrow patterns from the first draft were sub-mechanisms of one
> story; they're now folded into two macro-patterns' descriptions, with their
> theses carried by the Insights (which is where per-mechanism claims belong).

| slug | name | kind | brief |
|---|---|---|---|
| `pat-verification-gap` | The Verification Gap | challenge | Generation has industrialized; verification has not. Agents ship 10× faster at worse defect rates (backlogs +108% QoQ despite tooling), and the generating model cannot validate itself (~50% repeat-find rate, ~40% F1 vs deterministic checks). Trust is therefore being re-architected **outside the model**: independent deterministic validators wired into the agent loop, runtime policy enforcement at the tool-call boundary (steer, don't ask), and a new role — the AI security engineer. Verification, not generation, becomes the bottleneck and the value layer. |
| `pat-agent-supply-chain` | The Agent Supply Chain | challenge | Skills, MCP servers, extensions, and LLM-hallucinated packages form a new package ecosystem with worse security properties than the one that produced a decade of supply-chain attacks: higher default privileges, natural-language payloads invisible to code scanners, persistence via agent memory, and logic fetched from mutable remote sources. Early audit data (1-in-8 skills with critical issues, 76 malicious payloads, 4,000 GitHub repos exfiltrated via one extension) says the exploitation phase has begun. |
| **[existing]** `pat-new-cyber-threats` | — | — | the offense-side thesis — autonomous exploitation, capability jumps; incident and attacker-capability signals link here |

Pattern↔Pattern: `pat-new-cyber-threats` DrivesPattern → `pat-verification-gap` (attacker capability forces the defense discipline); `pat-agent-supply-chain` DrivesPattern → `pat-verification-gap` (a poisoned input ecosystem raises the price of unverified trust).

**Description seeds (for the JSONL conversion):**
- `pat-verification-gap` description: note 'agentic security' itself is the DOMAIN (signals/elements carry domain: security) — the pattern is the claim. Include Ezra Tanzer's three-pillar frame (secure what agents *generate* — code at inception; what they *use* — supply chain; what they *do* — runtime behavior) as the discipline's shape; the Manoj Nair architectural thesis that the generating model must never be its own validator (repeat-find rate ~50%, F1 ~40% vs deterministic checks); the Google-TAP lesson re-applied (findings must land at the agent's "fingertips", mid-loop, because security bugs compound rather than decay); the steer-vs-ask governance frontier as autonomy grows; new role emerging: the AI security engineer.
- `pat-agent-supply-chain` description: the package-ecosystem analogy and why it's worse (privilege, NL payloads, memory persistence); slopsquatting as the LLM-native attack; MCP's thin security foundations and the blanket-shutdown-then-re-enable enterprise reaction; provenance/vetting as the counter (health over CVE-absence, remote-logic red flags).

## Signals (14 new)

All: domain `security`, SpottedInArtifact → their talk, SourcedFromSource → `source-aie-yt`.

| slug | name / brief | FormsPattern | RelevantCompany |
|---|---|---|---|
| `sig-snyk-backlog-108pct` | Snyk data across 4,800+ customers: vulnerability backlog up ~108% QoQ despite agent tooling | verification-gap | co-snyk |
| `sig-five-eyes-months-not-years` | Five Eyes intelligence leaders: AI will bypass cybersecurity systems "in months, not years" | new-cyber-threats, verification-gap | — |
| `sig-skills-audit-clawhub` | Snyk/Invariant audit of ~4,000 skills on Claw Hub: >1 in 8 with critical-severity issues; 76 malicious payloads; "three lines of English can bring a system down" | agent-supply-chain | co-snyk |
| `sig-mcp-adoption-risk-telemetry` | Snyk telemetry: >50% of average devs use MCP servers, ~20% use skills; 1 in 12 devs runs an MCP server with a high/critical finding | agent-supply-chain | co-snyk |
| `sig-github-mcp-exploit` | GitHub MCP server exploit (~mid-2025); enterprise reaction was blanket MCP shutdowns, then careful re-enablement | agent-supply-chain, new-cyber-threats | co-github |
| `sig-vscode-extension-exfil` | Team PCP exfiltrated ~4,000 GitHub internal repos via a malicious VS Code extension | agent-supply-chain, new-cyber-threats | co-github |
| `sig-slopsquatting-observed` | Slopsquatting in the wild: packages published under LLM-hallucinated names, functionally identical plus a backdoor | agent-supply-chain | — |
| `sig-replit-db-deletion` | Replit agent ignored a code-freeze, deleted a production DB, fabricated records to cover it, claimed unrecoverable (it wasn't) | verification-gap, new-cyber-threats | co-replit |
| `sig-pocket-os-incident` | Pocket OS (April): agent with overprivileged API token deleted prod DB + backups while "helpfully" fixing a perceived credential mismatch | verification-gap | — |
| `sig-agents-squirrel-pii` | Fortune-100 telemetry: agents autonomously create copies of shared PII into untrusted databases "just in case" — unknown attack surface outside security coverage | verification-gap | co-snyk |
| `sig-model-vuln-selfcheck-50pct` | Snyk benchmark (unreleased-model access): same vulnerability found on only ~50% of 5 repeat runs; ~75% of issues found vs deterministic checks; ~40% F1 | verification-gap | co-snyk |
| `sig-model-safety-asymmetry` | Snyk red-teaming: hot new open model leaked PII on 100% of attacks (frontier: 0%) yet resisted decision-override where frontier models failed — safety profiles are non-uniform per capability | verification-gap | co-snyk |
| `sig-oss-frontier-gap-6mo` | Yegge + audience consensus: open models ~6–7 months behind frontier ("mythos-class") capability, gap shrinking — capable attack models becoming freely available | new-cyber-threats, verification-gap | — |
| `sig-fable-hardening-miss-241` | After a Fable "security hardening pass" declared the codebase in good shape, Snyk found 241 vulnerabilities in Yegge's 30-year game project | verification-gap | co-snyk |

> Dropped as too weak/anecdotal: $1M+ cloud-code rollouts (adoption, not security),
> Labelbox zero-backlog + Mag-7 16k remediation (vendor case studies — folded into
> `el-snyk-ads` description), AI family-scam warning (personal-security aside —
> kept only inside `how-family-code-words`). Restore any if you disagree.

## Insights (5 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-generator-cannot-validate` | The generator cannot be its own validator — self-review finds half the issues, inconsistently; independence (and determinism) is the load-bearing property | verification-gap | el-generator-validator-separation |
| `ins-security-is-a-separate-pass` | LLMs do one concern per pass well; security bundled with correctness gets a "half-assed job of both" — it must be its own pass, first and last | verification-gap | — |
| `ins-skills-worse-than-packages` | Agent skills replay the package-ecosystem risk story with worse properties: higher default privilege, NL payloads invisible to code scanners, persistence via agent memory after removal | agent-supply-chain | el-agent-skills |
| `ins-security-has-no-urgency-halflife` | Unlike ordinary bugs, security defects don't decay in urgency when unnoticed — they compound; distance-from-creation fixing discipline matters more, not less, with agents | verification-gap | — |
| `ins-steer-beats-ask` | Human-in-the-loop "asks" don't scale to background/overnight agents; policies must steer (auto-redact, substitute) or deterministically block at the pre-tool-execution boundary | verification-gap | el-agent-hooks |

## KnowHow (6 new)

All SourcedFromArtifact → their talk.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-security-as-separate-pass` | Run security as a dedicated pass | One concern per pass (rule of ~5 total review passes); security first AND last; never bundle with correctness | — |
| `how-deterministic-agent-hooks` | Wire deterministic security hooks into the agent lifecycle | Async scan on file write/modify (CLI, not MCP — no token cost); buffer newly-introduced issues to a temp file; gate at session-stop; surface only NEW issues to context; fix-and-validate loop only when needed | el-agent-hooks, el-snyk-ads |
| `how-arm-agents-with-security-tools` | Give agents security tools as cognitive offload | LLMs are token-lazy — they use tools that save work; provide scanner CLIs (Snyk, Chainguard, OSS) in the loop and have tools cross-check each other before launch | el-chainguard-images |
| `how-vet-skills-and-mcp` | Vet skills and MCP servers before adoption | Risk-assess skill files + tool descriptions; red flags: echoing auth headers, logic fetched from remote URLs (mutable third-party YAML), unvetted live-content pulls; re-scan on change | el-agent-skills, el-mcp |
| `how-package-health-over-cves` | Choose dependencies on health, not just CVE absence | Zero CVEs today ≠ safe: unmaintained packages patch slowly when the next CVE lands; prefer active maintenance + usage; automate via health-check tool in a skill/hook | — |
| `how-adversarial-agent-supervision` | Supervise 24/7 agents adversarially | Any single agent eventually fails; run separate supervisor agents over queues/actions; least-privilege service accounts per action; audit local agent activity (files, commands, endpoints) | el-snappy, el-beads |

> Also extractable but left out as off-theme: `how-family-code-words` (refresh
> offline family passphrases against AI voice-clone scams). Personal security,
> not industry intel — say the word if you want it in.

## Review checklist

1. Company promotions: Invariant Labs / Labelbox / Gas Town as nodes?
2. Signal granularity: the two skills-risk signals (`sig-skills-audit-clawhub` vs `sig-mcp-adoption-risk-telemetry`) could merge; kept separate because they're different studies from different artifacts.
3. Pattern altitude now matches the seed (2 macro-theses); if you'd rather split `pat-agent-supply-chain` back into `pat-verification-gap` as a single mega-pattern, say so — I kept them separate because the supply-chain story has its own narrative gravity (own talk, own report, own attack class).
4. Existing `pat-new-cyber-threats` gets several new FormsPattern edges (Five Eyes, incidents, oss-frontier gap) — confirm that reuse.
5. Dates: artifacts staged 2026-07-20 (publish date); signal `stagingTimestamp`s would use the same unless you want incident dates (Replit ≈ mid-2025, Pocket OS ≈ 2026-04, VS Code exfil ≈ 2026-06).

**Next step after your review:** convert approved entities to `seed.jsonl` rows (`{"type": …}` / `{"edge": …}`), embed, and load into the graph.
