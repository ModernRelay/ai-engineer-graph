# SPIKE extraction — "Using LLMs to Secure Source Code" (Eugene Yan, Anthropic) — FOR REVIEW

Source transcript: `transcripts/yan-anthropic-llms-secure-source-code.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/imFedndyXYQ — AI Engineer World's Fair, published 2026-07-17.
`stagingTimestamp` for the artifact and all signals: 2026-07-17 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-yan-secure-source` | Using LLMs to Secure Source Code (Eugene Yan, Anthropic — AI Engineer World's Fair) | youtube | https://youtu.be/imFedndyXYQ |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-eugene-yan`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-eugene-yan` | Eugene Yan (member of technical staff, Anthropic; works with security teams on Claude-driven vulnerability find-and-fix) | `AffiliatedWithCompany → co-anthropic` **[registry]** |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-mozilla` | Mozilla | developer | appears as a defender case study (Firefox security bug-fix volume); maker of Firefox |

Reused: `co-anthropic` **[registry]**.

## Elements (1 new, 2 reused)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-agentic-vuln-pipeline` | Agentic vulnerability pipeline | concept | security | The six-step loop most teams converge on for LLM-driven security work: threat model + sandbox as per-codebase setup, then a discovery → verification → triage → patch loop. Maps to an ML pipeline: recall (discovery), precision (verification), ranking (triage), closing the loop (patching) |

Element edges: `el-agentic-vuln-pipeline` `IdentifiedInArtifact → ia-aie-yan-secure-source`; `el-agentic-vuln-pipeline` `UsesElement → el-generator-validator-separation` **[registry]**; `el-agentic-vuln-pipeline` `ExemplifiesPattern → pat-verification-gap` **[registry]**.

Reused: `el-generator-validator-separation` **[registry]** (Yan's independent adversarial verification agent that never sees the discovery agent's reasoning traces is a textbook instance); `el-claude-mythos-preview` **[registry]** (the model behind the Mozilla step-change and the cyber time-horizon step jump).

## Signals (4 new)

All: domain `security`, `SpottedInArtifact → ia-aie-yan-secure-source`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | FormsPattern | other edges |
|---|---|---|---|
| `sig-cyber-time-horizon-step-jump` | UK AI Security Institute's cyber version of the METR time-horizon benchmark (reverse engineering, web exploitation tasks) shows the newest frontier models as a step jump above the prior regression line — a discontinuous capability improvement, not trend-following | `FormsPattern → pat-new-cyber-threats` **[registry]** | `OnElement → el-claude-mythos-preview` **[registry]** |
| `sig-mozilla-bugfix-20x` | Mozilla Firefox monthly security bug fixes went from a ~20/month 2025 average to ~60–70 in Feb–Mar and ~400 in April (~20x last year's average), about two-thirds attributed to Claude Mythos preview; Mozilla explicitly credits agentic harnesses for making previously false-positive-ridden LLM scanning practical | `FormsPattern → pat-new-cyber-threats`, `FormsPattern → pat-harness-over-model` **[registry]** | `RelevantCompany → co-mozilla`; `OnElement → el-claude-mythos-preview` |
| `sig-anthropic-oss-scan-bottleneck-shift` | Anthropic scanned 1,000+ open-source repos: 23,000 candidate vulnerabilities, 6,200 rated high/critical, 1,600 reported to maintainers, ~100 patched upstream; their stated observation: finding vulnerabilities is now straightforward — the bottleneck has shifted to verification, triage, and patching | `FormsPattern → pat-verification-gap` **[registry]** | `RelevantCompany → co-anthropic` **[registry]** |
| `sig-prompts-shrink-per-model-generation` | Practitioner observation: each model step-change requires cutting prompt size ~50%; prescriptive vulnerability-category prompts are replaced by one-liners like "look for where untrusted data hits the trust boundary"; a pentesting team that gave the model live tools (query API, read logs/source) hit near-100% true-positive rates | — (see review note 2) | — |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-security-scanning-is-ml-pipeline` | LLM security work is an ML pipeline wearing a security hat: discovery optimizes recall, verification optimizes precision (kept independent and adversarial so the discovery agent doesn't self-censor), triage is ranking under scarce engineer attention, patching closes the loop. Closing the loop converts the harness from operational expense to capital expense — each scan makes the next one better | `HighlightsPattern → pat-verification-gap` **[registry]** | `ReliesOnElement → el-agentic-vuln-pipeline`, `ReliesOnElement → el-generator-validator-separation` **[registry]** |
| `ins-org-bottleneck-outlasts-technical` | Once scanning industrializes (solvable with compute and money), the real bottlenecks are organizational: vulnerability routing at 100s/month, severity calibration between product and security engineers, and patch-review bandwidth — "non-technical problems are an order of magnitude harder than technical problems"; threat models stuck in people's heads are the scarcest input | `HighlightsPattern → pat-verification-gap` | — |

## KnowHow (3 new)

All `SourcedFromArtifact → ia-aie-yan-secure-source`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-threat-model-as-context` | Write the threat model down — it is the context | A well-documented threat model lifts true-positive rates to ~90% (aim above 75%); "the model has great context of the code but poor context of the system" — bootstrap it from docs/code/past CVE patches, then have the model interview the system expert for what is not in the code (compensating controls, VPN-only exposure); reuse the same document for severity triage | `ReferencesElement → el-agentic-vuln-pipeline` |
| `how-adversarial-verification` | Verify with an independent, adversarial agent | The verifier sees only the flagged vulnerability, never the discovery agent's reasoning traces; it assumes the finding is false and tries to prove it either way; in a sandboxed fresh container it builds and detonates a proof-of-concept exploit to confirm true positives; sandbox = no egress, no cloud credentials, reproducible baseline containers | `ReferencesElement → el-generator-validator-separation` **[registry]** |
| `how-close-the-patch-loop` | Validate patches on a ladder, then encode what you learned | Patch validation ladder: original PoC stops working → test suite stays green → a fresh discovery agent re-attacks the patched code; feed that back to the patching agent (quality improves greatly); human confirms before merge; record compensating controls in the scan config so the finding never resurfaces — start with open-source dependencies, interactively ("hands on the wheel"), before aiming for automation | `ReferencesElement → el-agentic-vuln-pipeline` |

## Dropped

- Log4Shell / Heartbleed recaps — historical framing, not new signals.
- The order-service SQL-injection walkthrough — pedagogical example, folded into knowhow rows.
- Claude Security product + open-source harness repos plug — resource pointer, no node.

## Review notes

1. "Mythos preview" ("mess preview", "me preview" in captions) read as Claude Mythos preview and mapped to `el-claude-mythos-preview` **[registry]**; "271" in "attributed about two-thirds of this to mess preview about 271" is an unresolved caption garble (possibly a version number) — left out.
2. `sig-prompts-shrink-per-model-generation` has no FormsPattern edge: it leans toward "the model needs less scaffolding each generation," which mildly cuts against `pat-harness-over-model` while the rest of the talk supports it. Attach `ContradictsPattern → pat-harness-over-model` if you want that tension explicit; I left it neutral.
3. `sig-mozilla-bugfix-20x` carries two FormsPattern edges (defender-side capability + harness-made-it-practical). Trim to `pat-new-cyber-threats` if you want one edge per signal.
4. The 90% true-positive threat-model stat is attributed to "several teams" and "one CISO" — practitioner testimony, not a published benchmark.
