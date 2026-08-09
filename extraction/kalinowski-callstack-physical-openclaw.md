# SPIKE extraction — "OpenClaw in Your Hand: Building a Physical AI Terminal" (Lech Kalinowski, Callstack) — FOR REVIEW

Source transcript: `transcripts/kalinowski-callstack-physical-openclaw.txt` (auto-captions — quotes are paraphrases, not verbatim; captions are heavily garbled in this talk, see Review notes).
Video: https://youtu.be/akk6KRlcwW4 — AI Engineer World's Fair, published 2026-06-28.
`stagingTimestamp` for the artifact, signals, and knowhow: 2026-06-28 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-kalinowski-physical-terminal` | OpenClaw in Your Hand: Building a Physical AI Terminal (Lech Kalinowski, Callstack — AI Engineer World's Fair) | youtube | https://youtu.be/akk6KRlcwW4 |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-lech-kalinowski`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-lech-kalinowski` | Lech Kalinowski (PhD in physics; builds AI-native hardware in Callstack's technological incubator) | `AffiliatedWithCompany → co-callstack` |

## Companies (1 new)

| slug | name | type | brief |
|---|---|---|---|
| `co-callstack` | Callstack | developer | Software consultancy (React Native specialists); its technological incubator funded/supported the physical AI terminal project (captions garble the name as "Kostak") |

## Elements (1 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-physical-ai-terminal` | Physical AI terminal (ESP32 dual-display OpenClaw remote) | product | robotics | Handheld battery-powered (single LiPo cell) AI-native terminal built on an ESP32 dual-core MCU with a dual-display design — small one-color OLED as the fast "live surface" for typing, bistable e-paper for rendered output — plus keyboard and rotary encoder; a thin client that drives OpenClaw and local LLMs on a DGX Spark over Wi-Fi; firmware uses pre-allocated static buffers and 1-bit images (no markdown engine, no malloc); four modes incl. internal shell, assist control, and an LLM-generated text-RPG console; built solo in ~3 months / 130 commits; provisional patent filed on the quiet text-first AI device niche |

Element edges: `el-physical-ai-terminal` `UsesElement → el-openclaw` **[registry]**, `UsesElement → el-dgx-spark` **[registry]**; `IdentifiedInArtifact → ia-aie-kalinowski-physical-terminal`.

## Signals (4 new)

All: `SpottedInArtifact → ia-aie-kalinowski-physical-terminal`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-callstack-physical-ai-terminal` | robotics | A solo practitioner (PhD physicist in Callstack's incubator) built a working physical AI terminal — ESP32, dual display, keyboard, one LiPo cell — that remote-controls his OpenClaw instance on a DGX Spark, in ~3 months / 130 commits; he frames "AI-native operating systems" for microcontroller-class devices as an open market niche. Agents are escaping the desktop into dedicated fully-local hardware | `FormsPattern → pat-sovereign-ai` **[registry]** | `OnElement → el-physical-ai-terminal`, `OnElement → el-openclaw` **[registry]**, `OnElement → el-dgx-spark` **[registry]**; `RelevantCompany → co-callstack` |
| `sig-model-off-the-metal` | inference | "Keep the model off the metal" (paraphrase): no current LLMs run on tiny MCUs, so a physical AI device must be a thin client — all inference stays on a local hub (here: an open-source ~120B GPT-family model served via TensorRT behind an OpenAI-style proxy on the DGX Spark; proxy needed because many open models don't match the OpenAI API style) | — | `OnElement → el-dgx-spark` **[registry]** |
| `sig-quiet-ai-hardware-niche` | robotics | The AI-hardware race clusters around audio interfaces and video capture; the speaker identifies (and filed a provisional patent on) the opposite niche — quiet, text-first, distraction-free AI devices for reading/writing/chatting with an LLM without colorful displays, popups, or commercials | — | `OnElement → el-physical-ai-terminal` |
| `sig-epaper-llm-rpg-console` | harness | The device's surprise killer app: a text-based RPG console where the LLM generates the four worlds, characters, maps, NPCs and their memory at runtime — "a Game Boy for LLMs" (paraphrase); noted irony that a quiet e-paper text game consumes the most powerful GPU hardware available (the DGX Spark) | — | `OnElement → el-runtime-llm-gameplay` **[registry]**, `OnElement → el-dgx-spark` **[registry]** |

## Insights (1 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-thin-client-ai-hardware` | Until models shrink onto microcontrollers, "AI-native hardware" means a radically thin, bulletproof client plus a local inference hub: graceful degradation at every layer (OLED dies → e-paper works; keyboard dies → encoder works; Wi-Fi dies → local shell works), with the differentiating IP in the interface and power management, not in on-device intelligence | `HighlightsPattern → pat-sovereign-ai` **[registry]** | `ReliesOnElement → el-physical-ai-terminal`, `ReliesOnElement → el-dgx-spark` **[registry]** |

## KnowHow (1 new)

`SourcedFromArtifact → ia-aie-kalinowski-physical-terminal`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-mcu-llm-terminal` | Field notes for building an MCU-class LLM terminal | Split the display job: fast small OLED as the live typing surface, bistable e-paper for committed renders — match each display to its job (plenty on the market). Render one-bit images into pre-allocated static buffers; no markdown engine or malloc on the MCU. Overbuild the power-management unit — regulator instability killed two displays mid-build and replacement parts took weeks. Use hardware I2C with proper physical pull-ups (software I2C without them fails); avoid GPIO13 (silent failure — move ports). Pay for quality parts: a cheap encoder produced rotational noise until pull-ups and capacitors were added. Keep the model off the metal: serve it on a local box (TensorRT) behind an OpenAI-style proxy to normalize API differences across open models. For content, "try narrative — context matters, not numbers" (paraphrase): lean on the LLM for worlds/personalities, not stat crunching | `ReferencesElement → el-physical-ai-terminal`, `ReferencesElement → el-openclaw` **[registry]** |

## Dropped

- ESP32, OLED, e-paper, TensorRT, LiPo cell as Element nodes — commodity components; load-bearing detail lives in `el-physical-ai-terminal`'s brief and the knowhow.
- The ~120B open GPT-family model as an Element — single garbled mention ("open-source GPT 120 billion parameters model", presumably gpt-oss-120b); prose only.
- The basement-discovery framing story and the four RPG world names (Older Guns, Neon Abyss, The Hollows, Void Witch — spellings uncertain) — color.
- "16 classes / four modes" numerology — captions too garbled to trust beyond: 2 displays, 4 worlds, ~3 months, 130 commits.

## Review notes

1. **Garbles resolved against official title/registry**: "Kostak" = Callstack; "DJX park" / "DGX Park" = NVIDIA DGX Spark (`el-dgx-spark` **[registry]**); "open claw" = OpenClaw (`el-openclaw` **[seed/registry]**); "130 comments" = 130 commits; "keep the model of the metal" = "off the metal"; "cardboard" = keyboard. Unresolved: exact identity of the 120B model (likely gpt-oss-120b), the RPG world names.
2. `el-runtime-llm-gameplay` **[registry]** reused on name match (batch-6 Meta game talk element) for the RPG signal — verify brief compatibility at reconciliation; downgrade to prose if that element is Meta-specific.
3. The device is unnamed in-talk; `el-physical-ai-terminal` coined from the official title. Kind `product` despite prototype status (provisional patent + stated commercial intent); domain `robotics` chosen as the physical-AI bucket — flip to `harness` if robotics is reserved for actuated systems.
4. Only `sig-callstack-physical-ai-terminal` forms a pattern (`pat-sovereign-ai`: fully local stack — own hardware, own model, no cloud). `sig-model-off-the-metal` is a capability-limit observation and deliberately pattern-less; it mildly **counters** the idea that edge AI is here (models don't fit MCUs) — no ContradictsPattern edge since no registry pattern states that.
5. `sig-quiet-ai-hardware-niche` runs mildly counter to the voice-first-input thesis in this batch's Pike talk (`ia-aie-pike-voice-visuals`) — interesting tension, prose-noted only (no pattern at stake).
6. Provisional-patent and market-niche claims are the speaker's own; not externally verified.
