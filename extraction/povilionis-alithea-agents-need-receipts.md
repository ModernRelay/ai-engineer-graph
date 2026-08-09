# SPIKE extraction — "Agents Need Receipts, Not More Tool Calls" (Armanas Povilionis, Alithea Bio) — FOR REVIEW

Source transcript: `transcripts/povilionis-alithea-agents-need-receipts.txt` (auto-captions — quotes are paraphrases; "Alifeia" = Alithea Bio).
Published 2026-07-20 on the AI Engineer channel (World's Fair). `stagingTimestamp` for all nodes: 2026-07-20.
Entities marked **[registry]** already exist; `pat-model-not-bottleneck` is **[batch2]**, defined in `dmello-nvidia-llm-stack-2008-database.md`.

---

## InformationArtifact

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-povilionis-receipts` | Agents Need Receipts, Not More Tool Calls (Armanas Povilionis, Alithea Bio — AI Engineer World's Fair) | youtube | https://youtu.be/Q9ycQHbDdJs |

Edges: `PublishedBySource → source-aie-yt`; `ContributedByExpert → exp-armanas-povilionis`.

## Experts (1 new)

| slug | name | AffiliatedWithCompany |
|---|---|---|
| `exp-armanas-povilionis` | Armanas Povilionis (Alithea Bio; a decade in life-sciences collaboration projects) | `co-alithea-bio` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-alithea-bio` | Alithea Bio | developer | Life-sciences agent infrastructure; builds the Froglet protocol (froglet.dev) |

## Elements (1 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-froglet` | Froglet | framework | harness | Protocol for agents to discover, transact with, and receive verifiable receipts from external data/service providers across organizational boundaries. Homogeneous nodes playing requester/provider/marketplace roles; keypair identity per node; every step signed into a tamper-evident chain (descriptor → offer → quote → deal → invoice → receipt); marketplace only for discovery/indexing, then peer-direct execution; two-part payments (base payment + success fee). Integrates with existing payment rails, agent harnesses, execution environments, and transports — same interface, not same stack. Website: https://froglet.dev |

Element edges: `el-froglet` DevelopedByCompany → `co-alithea-bio`; IdentifiedInArtifact → `ia-aie-povilionis-receipts`; EnablesPattern → `pat-verification-gap`.

## Patterns (0 new)

Links to **[registry]** `pat-verification-gap` (verifiable receipts = trust
re-architected outside the model, applied to agent *transactions*) and
**[batch2]** `pat-model-not-bottleneck` ("more tools alone will not enable
automation" — the blocker is the supply chain around the agent, not the
agent's local capability). `pat-saaspocalypse` considered for the
agents-with-budgets thesis — see review notes.

## Signals (2 new)

All: `SpottedInArtifact → ia-aie-povilionis-receipts`, `SourcedFromSource → source-aie-yt`.

| slug | name / brief | domain | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-froglet-launch` | Alithea Bio ships Froglet (2026-07): a cryptographic receipt-chain protocol for cross-org agent transactions — signed step chain, keypair identity, marketplace discovery, base-payment/success-fee scheme; runs locally with one command, docs live at froglet.dev | harness | `pat-verification-gap`, `pat-model-not-bottleneck` | RelevantCompany → `co-alithea-bio`; OnElement → `el-froglet` |
| `sig-science-collab-cost-barrier` | Practitioner observation from a decade of life-sciences collaboration: close scientific collaboration turns into bespoke enterprise projects taking years and millions before the first reusable workflow exists, because data and specialized analytics live in organizational silos — the automation blocker is cross-org alignment, not local tooling | data-eng | `pat-model-not-bottleneck` | RelevantCompany → `co-alithea-bio` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-agents-get-budgets` | As agentic automation matures, organizations will not just give agents more tools — they will allocate them budgets. Per-task token budgets are the primitive form; the next step is agents managing their own budget for anything they need: discovering services, requesting data, negotiating execution, and paying for work across organizational boundaries. The agent stops being "a cook with a better knife" and starts acting like an executive chef | `pat-model-not-bottleneck`, `pat-saaspocalypse` | `el-froglet` |
| `ins-receipts-not-tools` | More tools only improve local work (better knives, more ovens); autonomous collaboration is a supply-chain problem, and it requires a chain of verifiable receipts proving every step so any result can be trusted downstream. Trust infrastructure — identity, signing, settlement — is the gate to agentic scientific research, not model capability | `pat-verification-gap` | `el-froglet` |

## KnowHow (1 new)

`SourcedFromArtifact → ia-aie-povilionis-receipts`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-receipt-chain-design` | Design agent-to-agent transactions as tamper-evident receipt chains | Give every node a keypair for identity + signing; sign every interaction step into one chain (descriptor → offer → quote → deal → invoice → receipt) so tampering with any link breaks it; use a marketplace node only for service description/indexing, then let requester and provider communicate peer-direct (no middleman) in one interaction: request, sign, execute, receipt; split payments into a base payment (protects providers from request flooding) and a success fee (protects requesters from malicious providers); require a shared interface, not a shared software stack | `el-froglet` |

## Dropped

- Kitchen/Michelin-star metaphor detail — rhetorical device, folded into insight briefs.
- "Try Froglet with one prompt / walkthrough button" — marketing CTA.
- "Few thousand tokens and minutes" resource-sharing claim — aspirational product claim, not an observed fact; folded into `el-froglet` context only implicitly.

## Review notes

1. **Below the 3-signal bar on purpose**: this is a ~5-minute product pitch; only two items clear the graph-worthy bar. The launch itself is the main dated fact.
2. `ins-agents-get-budgets` → `pat-saaspocalypse` is a judgment call: agents as purchasing economic actors (budgets, procurement, machine-to-machine payment) reads as that thesis's next chapter. Cut the edge if you read SaaSpocalypse more narrowly; the pattern-worthy alternative would be a new `pat-agent-economy`, which I deliberately did NOT coin (one-new-pattern budget spent on `pat-model-not-bottleneck`).
3. `el-froglet` kind: chose `framework` (it's a protocol/spec with a reference node implementation); `product` also defensible.
