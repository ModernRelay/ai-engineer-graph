"""Run one agent session and keep every message as a JSON-ready trace."""

import dataclasses
import time

from claude_agent_sdk import ClaudeAgentOptions, query


def serialize(message) -> dict:
    return {"kind": type(message).__name__, **dataclasses.asdict(message)}


async def run_agent(prompt: str, options: ClaudeAgentOptions) -> tuple[list[dict], float]:
    """The session's messages, serialized, and its wall-clock seconds."""
    trace, start = [], time.monotonic()
    async for message in query(prompt=prompt, options=options):
        trace.append(serialize(message))
    return trace, time.monotonic() - start
