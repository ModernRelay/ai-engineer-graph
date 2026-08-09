# SPIKE extraction — "The Prompt Is Still a Punch Card" (Ted Johnson, JoinIn AI) — FOR REVIEW

Source transcript: `transcripts/johnson-joinin-prompt-punch-card.txt` (auto-captions — quotes are paraphrases, not verbatim; includes staged live demos).
Video: https://youtu.be/hVJOnuhFmTA — AI Engineer World's Fair, published 2026-07-02.
`stagingTimestamp` for the artifact, all signals, and knowhow: 2026-07-02 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-johnson-prompt-punch-card` | The Prompt Is Still a Punch Card (Ted Johnson, JoinIn AI — AI Engineer World's Fair) | youtube | https://youtu.be/hVJOnuhFmTA |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-ted-johnson`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-ted-johnson` | Ted Johnson (co-founder, JoinIn AI; 25 years in enterprise software, collaboration systems, and AI-enabled interfaces) | `AffiliatedWithCompany → co-joinin-ai` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-joinin-ai` | JoinIn AI | developer | startup founded on the observation "why do we still have to learn AI?" — building conversational AI that participates in (multiparty) conversation instead of waiting behind a batch prompt |

## Elements (4 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-channel-expression-protocol` | Channel / expression / protocol | concept | harness | Three-part anatomy of an interface: **channel** = the physical transport (keyboard, microphone, screen, punch card, prompt box); **expression** = the range/richness of meaning the channel is permitted to carry; **protocol** = the rules and shape of the exchange. Diagnosis of AI today: channels unchanged for decades (the QWERTY patent is ~1860s), expression exploded with natural language, but the protocol — prompting — is still batch: encode a complete request, submit, wait, read, repair, resubmit; inherited punch card → loom lineage |
| `el-personaplex` | PersonaPlex (NVIDIA) | technology | inference | NVIDIA research model for real-time full-duplex conversation: listens while speaking, stops and yields when interrupted, picks the dropped thread back up, and places backchannels ("mhm", "right") where a human's would land — real turn-taking rather than one-slot exchange |
| `el-gpt-realtime-2` | GPT-realtime 2 | product | inference | OpenAI speech-to-speech model (released late May, per the talk) rolled into ChatGPT voice mode; adds active-listening backchannels — read as the frontier's first step from strict your-turn/my-turn batch toward participation |
| `el-multiparty-turn-taking` | Multiparty conversational turn-taking | technology | harness | Conversation-protocol layer JoinIn demos for group settings: labels each utterance (question / proposal / answer), tracks who holds the floor and who is being addressed ("Hey Ted" was not meant for the AI), maintains utility-driven goals, and takes a turn only when no one else is speaking or holding the floor — including unprompted scope clarifications ("expense approvals, or a general approval workflow?"), deferred actions ("AI, hold that"), and answering direct asks (capture requirements, check room availability) |

Element edges: `el-personaplex` `DevelopedByCompany → co-nvidia` **[registry]**; `el-gpt-realtime-2` `DevelopedByCompany → co-openai` **[registry]**; `el-multiparty-turn-taking` `DevelopedByCompany → co-joinin-ai`; all four `IdentifiedInArtifact → ia-aie-johnson-prompt-punch-card`.

## Signals (3 new)

All: `SpottedInArtifact → ia-aie-johnson-prompt-punch-card`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | domain | FormsPattern | OnElement | RelevantCompany |
|---|---|---|---|---|---|
| `sig-voice-mode-one-slot` | Field anecdote (weeks before the talk): a frontier speech-to-speech voice mode answered a normal question fine, then — overhearing speech addressed to a human ("Hey Ted, come on in") — replied "Sure, I'm here. What's on your mind?" Not a dumb model: the protocol has exactly one slot (your message → its reply), with no concept of addressee or floor | harness | `FormsPattern → pat-model-not-bottleneck` | — | — |
| `sig-gpt-realtime-2-backchannels` | OpenAI released GPT-realtime 2 in late May and began using it for ChatGPT voice mode; it now backchannels ("mhm", "right") — the speaker reads the field as converging on the conclusion his company was built on: the interface has to stop being batch and start participating | inference | `FormsPattern → pat-model-not-bottleneck` | `OnElement → el-gpt-realtime-2` | `co-openai` **[registry]** |
| `sig-personaplex-full-duplex` | NVIDIA's PersonaPlex research model demonstrates real turn-taking: interrupted mid-answer it stops, yields, then resumes the earlier thread; its backchannels land where a person's would — listening and speaking at once in real time | inference | `FormsPattern → pat-model-not-bottleneck` | `OnElement → el-personaplex` | `co-nvidia` **[registry]** |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-prompting-is-batch` | Prompting is the punch-card protocol surviving into the AI era: package a complete turn, submit, wait, read, repair, resubmit — "batch with interactive sprinkles". Shrinking the wait from overnight to seconds fooled us into calling it interactive; "prompt engineering" is a flattering name for deck-assembly rules (think step-by-step, paste more/less context, markdown incantations). Model capacity curves up while the protocol stays flat — the human still chooses context, timing, notices ambiguity, repairs output — and when it fails, users wrongly blame themselves. The mismatch is the interface, not the user | `HighlightsPattern → pat-model-not-bottleneck` | `ReliesOnElement → el-channel-expression-protocol` |
| `ins-ai-is-interface-technology` | AI is becoming an interface technology, not just an intelligence technology: a system that can reason, listen, infer, and adapt can absorb the burdens humans carried only because machines were too limited — choosing timing, modality, context, and repair. The design question flips to "what burden are we still putting on humans only because the machine used to be too limited to carry it?" The answer space is the affordances humans already use with each other — a question, a pause, a sketch, a checklist, a quiet aside, saying nothing — with channel and moment chosen by the AI. Take that burden off people and adoption follows | `HighlightsPattern → pat-model-not-bottleneck` | `ReliesOnElement → el-multiparty-turn-taking` |

## KnowHow (1 new)

`SourcedFromArtifact → ia-aie-johnson-prompt-punch-card`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-interface-burden-audit` | Audit inherited interface burden | For each thing your interface makes the human do — encode intent completely upfront, pick the timing, choose the channel, carry the context, repair the output — ask whether it exists only because machines used to be too limited. Replace batch turns with participation: clarify mid-thought, ask follow-ups, notice what's missing and say so, know who is speaking and whether the words were meant for the system. Don't default to chat, voice, or walls of markdown; use human affordances and let the AI choose channel and moment | `ReferencesElement → el-channel-expression-protocol` |

## Dropped

- Keyboard history (Dvorak/Colemak, spacebar-splitting enthusiasts, ~1860 QWERTY patent, Hansen Writing Ball) — rhetorical setup, folded into the element brief.
- Sherry Turkle citation ("conversation is the most human and humanizing thing we do") — rhetorical support, prose only.
- Weaving-loom origin of batch — folded into `ins-prompting-is-batch` / element brief.
- The staged JoinIn meeting demo transcript (expense-approvals requirements session) — product demo, not field evidence; behaviors captured in `el-multiparty-turn-taking`, no signal built on it.

## Review notes

1. Company name: captions render "Join an AI" / "Join in AI"; official title says JoinIn AI — normalized.
2. `el-personaplex`: captions render "Personal Plex" / "Persona Plex"; normalized to PersonaPlex (NVIDIA research). Verify official name/spelling before seeding.
3. `el-gpt-realtime-2`: captions say "GPT real-time 2 in late May" — year unstated (context implies 2026); product-name normalization to OpenAI's convention is mine. Verify name and release date.
4. **Candidate resonance (no edges):** batch3's uncoined "AI adoption/UX gap" candidate (nanz file) gets a second independent data point here — Johnson's thesis is precisely adoption gated on interface, "when you take that burden off people… adoption follows". If that candidate is ever coined, both insights here would rehome from `pat-model-not-bottleneck`.
5. All pattern edges land on `pat-model-not-bottleneck` — this talk is close to that pattern's canonical statement ("it's not a dumb model… the protocol is the part that did not advance"): read this file as strong corroboration for it.
6. The frontier vendor in `sig-voice-mode-one-slot` is unnamed in the talk ("a Frontier company's voice mode") — no RelevantCompany edge on purpose.
