"""Model access through OpenRouter, and cost from token usage.

The Claude Code CLI inside the Agent SDK reaches OpenRouter's Anthropic-compatible
endpoint through ANTHROPIC_BASE_URL + ANTHROPIC_AUTH_TOKEN (with ANTHROPIC_API_KEY
blanked so it can't take precedence). Cost is computed from token usage against
a recorded snapshot of OpenRouter's prices rather than the SDK's own estimate.
"""

from pathlib import Path

# "[1m]" tells the Claude Code CLI to use the model's full 1M-token context (it assumes 200k
# for OpenRouter model ids otherwise); the CLI strips the suffix before calling the API.
AGENT_MODEL = "anthropic/claude-sonnet-5[1m]"
JUDGE_MODEL = "anthropic/claude-opus-5.5"
BASE_URL = "https://openrouter.ai/api"

# USD per million tokens, from https://openrouter.ai/api/v1/models on 2026-09-23.
# Flat across the whole 1M context (no long-context tier), 5-minute cache writes.
PRICES = {
    "anthropic/claude-sonnet-5": {
        "input": 2.00,
        "output": 10.00,
        "cache_read": 0.20,
        "cache_write": 2.50,
    },
    "anthropic/claude-opus-5.5": {
        "input": 4.00,
        "output": 20.00,
        "cache_read": 0.20,
        "cache_write": 5.00,
    },
}
USAGE_FIELDS = {
    "input_tokens": "input",
    "output_tokens": "output",
    "cache_read_input_tokens": "cache_read",
    "cache_creation_input_tokens": "cache_write",
}


def openrouter_env(env_file: Path) -> dict[str, str]:
    key = ""
    for line in env_file.read_text(encoding="utf-8").splitlines():
        name, sep, value = line.partition("=")
        if sep and name.strip() == "OPENROUTER_KEY":
            key = value.strip().strip("'\"")
    if not key:
        raise ValueError(f"no OPENROUTER_KEY in {env_file}")
    return {"ANTHROPIC_BASE_URL": BASE_URL, "ANTHROPIC_AUTH_TOKEN": key, "ANTHROPIC_API_KEY": ""}


def _prices(model: str) -> dict[str, float]:
    return PRICES[model.removesuffix("[1m]")]


def cost_usd(model: str, usage: dict) -> float:
    prices = _prices(model)
    return sum(usage.get(field, 0) * prices[kind] for field, kind in USAGE_FIELDS.items()) / 1e6


# The CLI's per-model tally (ResultMessage.model_usage). It covers every API call in
# the session; ResultMessage.usage leaves some out, so cost is computed from this.
MODEL_USAGE_FIELDS = {
    "inputTokens": "input",
    "outputTokens": "output",
    "cacheReadInputTokens": "cache_read",
    "cacheCreationInputTokens": "cache_write",
}


def session_cost(model_usage: dict) -> float:
    return (
        sum(
            tally.get(field, 0) * _prices(model)[kind]
            for model, tally in model_usage.items()
            for field, kind in MODEL_USAGE_FIELDS.items()
        )
        / 1e6
    )
