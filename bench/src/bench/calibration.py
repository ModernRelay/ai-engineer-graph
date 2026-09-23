"""D1.5: ten planted claims with known labels, to check the scorer rather than the arms.

The quotes were taken straight from five transcripts, not from any agent's answer. Real quotes
with a fair claim should come out grounded; everything else hallucinated: a contradicting claim
(judge: unsupported), an invented quote (not_found) or a real quote cited to the wrong talk
(wrong_talk).
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Plant:
    kind: str  # real | wrong_claim | invented | wrong_talk
    expected: str  # the grounding bucket a correct scorer gives it
    talk: str
    claim: str
    quote: str
    item: str = ""


GROUNDED, HALLUCINATED = "grounded", "hallucinated"
LIST_ENTRY = "Offline evaluation"

PLANTED = [
    Plant(
        "real",
        GROUNDED,
        "ia-aie-klein-agents-www",
        "Browserbase's Paul Klein says the most reliable browser agents in production combine "
        "writing code with driving the browser.",
        "The most reliable browser agents that we see in production right now are often writing "
        "code alongside using the browser to actually automate a task.",
    ),
    Plant(
        "real",
        GROUNDED,
        "ia-aie-dahl-security-firewall-agents",
        "Deno treats its agents as untrusted software and doesn't rely on the agent to guard its "
        "own actions.",
        "we take the stance that the sec the agents themselves have to be untrusted software. "
        "You can't rely on the agent itself to guard what it's doing.",
    ),
    Plant(
        "real",
        GROUNDED,
        "ia-aie-ung-evals-that-matter",
        "Lyft runs a rigorous offline evaluation before it launches an AI agent to production.",
        "before we launch this AI agents to productions we want to go through a rigorous offline "
        "evaluation process to make sure that this agent uh actually has sufficient performance",
        item=LIST_ENTRY,
    ),
    Plant(
        "real",
        GROUNDED,
        "govindarajan-openai-harness-failed",  # cited by chunk label, as the graph arm does
        "The talk argues that the model supplies capability while the harness supplies control.",
        "The model gives you capability, but the harness gives you control. A powerful engine "
        "with no brakes is not autonomy.",
    ),
    Plant(
        "real",
        GROUNDED,
        "ia-aie-krieger-anthropic-how-anthropic-builds",
        "Krieger's scaling advice is to measure everything you might need before an outage, so "
        "you can tell whether a number is normal.",
        "pre-measure everything that you think you might even remotely need because the worst "
        "thing is an outage where you're like, well, is this like number normal or is it high?",
    ),
    Plant(
        "wrong_claim",
        HALLUCINATED,
        "ia-aie-klein-agents-www",
        "Klein argues that weak models are still the main bottleneck holding back web agents.",
        "You know, until recently the the bottom neck was the models. The models one year ago "
        "really weren't good at long context horizon tasks. But that's clearly been you know, "
        "solved in a major way.",
    ),
    Plant(
        "wrong_claim",
        HALLUCINATED,
        "ia-aie-ung-evals-that-matter",
        "Lyft recommends simply prompting an LLM to generate about 50 test queries for the "
        "offline eval dataset.",
        "what ideally what you don't want to be doing is just to simply prompt an LM model to "
        "generate 50 different test query for your offline data sets.",
    ),
    Plant(
        "invented",
        HALLUCINATED,
        "ia-aie-dahl-security-firewall-agents",
        "Deno replaced its network rules with a model that decides which connections an agent "
        "may open.",
        "we replaced every network rule with a single model that decides at runtime which "
        "connections an agent is allowed to open",
    ),
    Plant(
        "invented",
        HALLUCINATED,
        "ia-aie-govindarajan-harness-failed",
        "Swapping in a new harness cut agent failures by 42% for every customer.",
        "when we swapped in the new harness our agent failures dropped by exactly forty two "
        "percent across every single customer",
    ),
    Plant(
        "wrong_talk",
        HALLUCINATED,
        "ia-aie-dahl-security-firewall-agents",  # the quote is from Klein's talk
        "Ryan Dahl notes that as much has been invested in RL environments for computer use in "
        "six months as for coding in a year.",
        "In the last year a lot of investment was made in RL environments for coding. And in "
        "the last 6 months months just as much investment has been made in RL environments for "
        "computer use.",
    ),
]


def planted_run() -> dict:
    """The plants as one run record, so they go through the same scoring path as the arms."""
    claims = [{"item": p.item, "claim": p.claim, "talk": p.talk, "quote": p.quote} for p in PLANTED]
    return {
        "qid": "CAL",
        "arm": "calibration",
        "run": 1,
        "answer_text": "",
        "answer_json": {"items": [{"label": LIST_ENTRY, "rank": 1}], "claims": claims},
    }
