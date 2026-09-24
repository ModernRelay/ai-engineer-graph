import json
import re
from pathlib import Path

import pytest

from bench.prompts import query_catalog, system_prompt

REPO = Path(__file__).resolve().parents[2]
PROMPTS = Path(__file__).resolve().parents[1] / "prompts"


# ── catalog format, on a small fixture ──────────────────────────────────────


@pytest.fixture
def queries(tmp_path):
    root = tmp_path / "queries"
    root.mkdir()
    (root / "a.gq").write_text(
        "// ── Section header ──\n"
        "\n"
        "// Semantic neighbors: embed the question\n"
        "// at query time.\n"
        "query related_chunks($q: String) {\n"
        "    match { $c: Chunk }\n"
        "    return { $c.text, $c.chunk_index }\n"
        "    order { nearest($c.embedding, $q) }\n"
        "    limit 10\n"
        "}\n"
        "\n"
        "query company_experts($slug: String, $since: DateTime)\n"
        '@description("Experts affiliated with a company")\n'
        "{\n"
        "    match { $c: Company { slug: $slug } }\n"
        "    return {\n"
        "        $x.slug,\n"
        "        $x.name as expert,\n"
        "        count($s) as signals\n"
        "    }\n"
        "}\n"
        "\n"
        "// A note about the file, not about the next query.\n"
        "\n"
        "query top_things()\n"
        "{\n"
        "    match { $t: Thing }\n"
        "    return { $t.slug }\n"
        "}\n"
    )
    (root / "mutations.gq").write_text(
        "query add_signal($slug: String) {\n    insert Signal { slug: $slug }\n}\n"
    )
    return root


@pytest.fixture
def alias_pack(tmp_path):
    path = tmp_path / "aliases.yaml"
    path.write_text(
        "servers:\n  s: { url: http://127.0.0.1:8081 }\n"
        "aliases:\n"
        "  related: { server: s, graph: g, query: related_chunks, args: [q] }\n"
    )
    return path


def test_catalog_lists_read_queries_with_usage_description_and_returns(queries, alias_pack):
    assert query_catalog(queries, alias_pack) == (
        "- `omnigraph alias related <q>` (stored query `related_chunks`): "
        "Semantic neighbors: embed the question at query time. Returns: text, chunk_index.\n"
        "- `omnigraph query company_experts --params "
        """'{"slug": "<String>", "since": "<DateTime>"}'`: """
        "Experts affiliated with a company. Returns: slug, expert, signals.\n"
        "- `omnigraph query top_things`: Returns: slug."
    )


# ── the real catalog and prompts ────────────────────────────────────────────


def real_query_names(pattern: str) -> set[str]:
    names = set()
    for gq in (REPO / "queries").glob("*.gq"):
        if re.fullmatch(pattern, gq.name):
            names |= set(re.findall(r"^query (\w+)\(", gq.read_text(), re.M))
    return names


@pytest.fixture(scope="module")
def catalog():
    return query_catalog(REPO / "queries", REPO / "omnigraph-config.example.yaml")


def test_catalog_covers_every_stored_read_query_and_no_mutation(catalog):
    reads = real_query_names(r"(?!mutations\.gq).*")
    mutations = real_query_names(r"mutations\.gq")

    assert len(reads) == 91
    assert [
        q for q in sorted(reads) if f"`{q}`" not in catalog and f"query {q}" not in catalog
    ] == []
    assert [m for m in sorted(mutations) if m in catalog] == []


def test_catalog_offers_every_alias_in_the_pack(catalog):
    aliases = re.findall(
        r"^  ([\w-]+):\s*\{", (REPO / "omnigraph-config.example.yaml").read_text(), re.M
    )

    assert len(aliases) == 67
    assert [a for a in aliases if f"`omnigraph alias {a}" not in catalog] == []


def test_transcript_search_entries_say_what_comes_back(catalog):
    assert "`omnigraph alias hybrid-search <q>` (stored query `hybrid_chunks`)" in catalog
    assert re.search(r"hybrid-search <q>`.*Returns: text, chunk_index\.", catalog)
    assert re.search(r"sem-context <q>`.*Returns: text, talk, talk_title, speaker\.", catalog)


@pytest.fixture(scope="module")
def prompts(tmp_path_factory):
    workdir = tmp_path_factory.mktemp("run")
    return workdir, system_prompt("markdown", workdir), system_prompt("omnigraph", workdir)


def test_both_arms_open_with_the_same_answer_contract(prompts):
    _, md, og = prompts
    contract = (PROMPTS / "answer_contract.md").read_text()

    assert md.startswith(contract)
    assert og.startswith(contract)


def test_prompts_name_the_working_directory_and_leave_no_placeholders(prompts):
    workdir, md, og = prompts

    assert str(workdir) in md and str(workdir) in og
    assert not re.search(r"\{(workdir|catalog)\}", md + og)


def test_each_arm_is_told_only_about_its_own_tools(prompts):
    _, md, og = prompts

    assert "omnigraph" not in md.lower() and "graph" not in md.lower()
    assert not re.search(r"\b(Grep|Glob)\b", og)


def test_prompts_leak_no_graph_data(prompts):
    _, md, og = prompts
    ids = {
        json.loads(line)["id"]
        for f in (REPO / "seed").glob("0[1-9]-*.jsonl")
        for line in f.open(encoding="utf-8")
    }

    assert len(ids) == 5034
    assert sorted(i for i in ids if i in md or i in og) == []


def test_every_stored_read_query_is_described(catalog):
    undescribed = re.findall(r"^- `([^`]+)`(?: \(stored query `\w+`\))?: Returns:", catalog, re.M)

    assert undescribed == []


def test_the_brief_says_where_verbatim_transcript_text_comes_from(prompts):
    _, _, og = prompts

    assert "signal-evidence" in og.split("### Stored queries")[0]


def test_single_alias_brief_names_the_alias_and_carries_no_catalog(tmp_path):
    prompt = system_prompt("omnigraph_single", tmp_path, alias="contested-claims")

    assert "omnigraph alias contested-claims" in prompt
    assert "{alias}" not in prompt and "{workdir}" not in prompt
    assert "Stored queries" not in prompt
    assert "pat-" not in prompt
