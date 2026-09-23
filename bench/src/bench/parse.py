"""The answer contract: the last fenced json block in an agent's reply."""

import json
import re

JSON_BLOCK = re.compile(r"```json\s*\n(.*?)\n\s*```", re.DOTALL)


def answer_block(text: str) -> dict | None:
    blocks = JSON_BLOCK.findall(text or "")
    if not blocks:
        return None
    try:
        answer = json.loads(blocks[-1])
    except json.JSONDecodeError:
        return None
    return answer if isinstance(answer, dict) else None
