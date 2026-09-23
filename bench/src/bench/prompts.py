"""System prompts: the shared answer contract plus one tool brief per arm.

The Omnigraph brief carries a catalog of every stored read query, generated
from queries/*.gq and the alias pack so it stays in step with the graph.
"""

import json
import re
from pathlib import Path

import yaml

BENCH_DIR = Path(__file__).resolve().parents[2]
PROMPTS_DIR = BENCH_DIR / "prompts"
QUERIES_DIR = BENCH_DIR.parent / "queries"
ALIAS_PACK = BENCH_DIR.parent / "omnigraph-config.example.yaml"

QUERY = re.compile(r"^query (\w+)\(([^)]*)\)", re.M)
PARAM = re.compile(r"\$(\w+):\s*([\w\[\]?]+)")
DESCRIPTION = re.compile(r'@description\("((?:[^"\\]|\\.)*)"\)')
RETURN = re.compile(r"return\s*\{(.*?)\}", re.S)


def _description(text: str, start: int, signature: str) -> str:
    """The @description annotation, else the // comment lines right above the query."""
    if m := DESCRIPTION.search(signature):
        return m.group(1)
    comment = []
    for line in reversed(text[:start].split("\n")[:-1]):
        line = line.strip()
        if not line.startswith("//"):
            break
        comment.append(line.lstrip("/").strip())
    return " ".join(c for c in reversed(comment) if "──" not in c)


def _returns(block: str) -> list[str]:
    m = RETURN.search(block)
    if not m:
        return []
    fields, depth, current = [], 0, ""
    for ch in m.group(1) + ",":
        depth += {"(": 1, ")": -1}.get(ch, 0)
        if ch == "," and depth == 0:
            if field := current.strip():
                fields.append(field.rsplit(" as ", 1)[1] if " as " in field else field)
            current = ""
        else:
            current += ch
    return [f.strip().rsplit(".", 1)[-1].lstrip("$") for f in fields]


def _alias_usage(name: str, args: list[str]) -> str:
    return " ".join(["omnigraph alias", name, *(f"<{a}>" for a in args)])


def query_catalog(queries_dir: Path, alias_pack: Path) -> str:
    aliases: dict[str, tuple[str, list[str]]] = {}
    for name, spec in (yaml.safe_load(alias_pack.read_text()).get("aliases") or {}).items():
        aliases.setdefault(spec["query"], (name, spec.get("args") or []))

    lines = []
    for gq in sorted(queries_dir.glob("*.gq")):
        if gq.name == "mutations.gq":
            continue
        text = gq.read_text(encoding="utf-8")
        matches = list(QUERY.finditer(text))
        for i, m in enumerate(matches):
            block = text[m.start() : matches[i + 1].start() if i + 1 < len(matches) else None]
            name, params = m.group(1), PARAM.findall(m.group(2))
            if name in aliases:
                head = f"- `{_alias_usage(*aliases[name])}` (stored query `{name}`)"
            else:
                usage = f"omnigraph query {name}"
                if params:
                    usage += f" --params '{json.dumps({p: f'<{t}>' for p, t in params})}'"
                head = f"- `{usage}`"
            description = _description(text, m.start(), block.split("{", 1)[0])
            if description and description[-1] not in ".!?":
                description += "."
            returns = _returns(block)
            tail = [description] if description else []
            if returns:
                tail.append(f"Returns: {', '.join(returns)}.")
            lines.append(f"{head}: {' '.join(tail)}")
    return "\n".join(lines)


def system_prompt(arm: str, workdir: Path) -> str:
    contract = (PROMPTS_DIR / "answer_contract.md").read_text(encoding="utf-8")
    brief = (PROMPTS_DIR / f"{arm}_arm.md").read_text(encoding="utf-8")
    brief = brief.replace("{workdir}", str(workdir))
    if arm == "omnigraph":
        brief = brief.replace("{catalog}", query_catalog(QUERIES_DIR, ALIAS_PACK))
    return contract + "\n" + brief
