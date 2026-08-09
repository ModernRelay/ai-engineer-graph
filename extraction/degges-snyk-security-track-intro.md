# SPIKE extraction — "Security Track Intro" (Randall Degges, Snyk) — FOR REVIEW

Source transcript: `transcripts/degges-snyk-security-track-intro.txt` (auto-captions — "Sneak" = Snyk mistranscription confirmed in this one).
Published 2026-07-20 on the AI Engineer channel (World's Fair). `stagingTimestamp`: 2026-07-20.

**This talk is thin by design** — a ~3-minute track intro. One genuinely graph-worthy observation (the model-access geopolitics show of hands); everything else is agenda/logistics. A near-empty file is the correct outcome.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-degges-track-intro` | Security Track Intro (Randall Degges, AI Engineer World's Fair security track) | youtube | https://youtu.be/2xJoimgoqBg |

Edges: `PublishedBySource → source-aie-yt`; `ContributedByExpert → exp-randall-degges`.

## Experts (1 new)

| slug | name | AffiliatedWithCompany |
|---|---|---|
| `exp-randall-degges` | Randall Degges (Snyk; lifelong developer + security professional; security-track emcee) | `co-snyk` **[registry]** |

## Companies (1 new; 2 registry reuse)

| slug | name | type | note |
|---|---|---|---|
| `co-openai` | OpenAI | bigtech | referenced only for the GPT-5.6 access restriction |
| **[registry]** `co-snyk` | — | — | speaker affiliation |
| **[registry]** `co-anthropic` | — | — | Fable access reference |

## Elements

None. (Track lineup name-drops — Nvidia, Anthropic, Keycard, Snyk — are logistics, not elements.)

## Signals (1 new)

| slug | name / brief | domain | FormsPattern | RelevantCompany |
|---|---|---|---|---|
| `sig-model-access-geopolitics` | Show of hands at the World's Fair security keynote: broad audience annoyance at pulled access to Fable and at the brand-new OpenAI GPT-5.6 being unusable — frontier-model availability has become a geopolitical/security constraint on practitioners, framed by the emcee as part of "using AI fearlessly, secure by default" | security | pat-sovereign-ai **[registry]** | co-anthropic **[registry]**, co-openai |

Edges: SpottedInArtifact → `ia-aie-degges-track-intro`, SourcedFromSource → `source-aie-yt`.

## Insights

None — the intro's three "obstacles" framing (generated code has vulns; autonomous agents in prod; geopolitics) is a table of contents for the track, and the first two are covered with real evidence by the full talks (batch1 + this batch).

## KnowHow

None.

## Dropped

- "AI-generated code has security issues, same as human code" — consensus statement, no data; carried with evidence elsewhere (`sig-snyk-backlog-108pct` [batch1]).
- "How do you deploy autonomous agents and sleep at night" — rhetorical setup for the track; the Johner and Stanley talks carry the substance.
- Room numbers, schedule, presenter roll-call.

## Review notes

1. The one signal rests on an informal show of hands + the pulled-access claims as stated by the speaker — it's the only World's-Fair-dated evidence we have for `pat-sovereign-ai` from this batch; cut it and the file is empty of signals.
2. `co-openai` was (surprisingly) not in the registry; coined here for one RelevantCompany edge. If reconciliation prefers not to mint a company for a passing mention, drop the edge and the node.
3. The transcript does not say *why* Fable access was pulled or for whom — brief kept deliberately vague; do not over-specify at JSONL conversion.
