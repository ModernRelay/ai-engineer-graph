"""Reading a serialized agent session (see bench.agent.serialize)."""


def text_of(content) -> str:
    """A tool result's content as plain text (it is a string or a list of text blocks)."""
    if content is None:
        return ""
    if isinstance(content, str):
        return content
    return "\n".join(b.get("text", "") if isinstance(b, dict) else str(b) for b in content)


def tool_uses(trace: list[dict]) -> list[dict]:
    return [
        block
        for m in trace
        if m["kind"] == "AssistantMessage" and isinstance(m.get("content"), list)
        for block in m["content"]
        if {"id", "name", "input"} <= block.keys()
    ]


def tool_results(trace: list[dict]) -> dict[str, dict]:
    return {
        block["tool_use_id"]: block
        for m in trace
        if m["kind"] == "UserMessage" and isinstance(m.get("content"), list)
        for block in m["content"]
        if "tool_use_id" in block
    }


def init_data(trace: list[dict]) -> dict:
    return next(
        (m["data"] for m in trace if m["kind"] == "SystemMessage" and m.get("subtype") == "init"),
        {},
    )


def result_message(trace: list[dict]) -> dict | None:
    return next((m for m in trace if m["kind"] == "ResultMessage"), None)
