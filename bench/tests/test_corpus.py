import json
from pathlib import Path

import pytest

from bench.cli import main
from bench.corpus import build_corpus


def artifact(slug, name, link, published, artifact_type="youtube"):
    return {
        "type": "InformationArtifact",
        "id": slug,
        "data": {
            "artifactType": artifact_type,
            "createdAt": published,
            "link": link,
            "name": name,
            "slug": slug,
            "stagingTimestamp": published,
            "updatedAt": published,
        },
    }


def chunk(prefix, index, text, talk):
    slug = f"{prefix}#{index}"
    return [
        {
            "type": "Chunk",
            "id": slug,
            "data": {
                "chunk_index": index,
                "createdAt": "2026-09-13T00:00:00Z",
                "slug": slug,
                "text": f"[{prefix}] {text}",
            },
        },
        {"edge": "PartOfArtifact", "from": slug, "to": talk, "data": {}},
    ]


def write_jsonl(path: Path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(r) + "\n" for r in rows))


@pytest.fixture
def seed(tmp_path):
    seed = tmp_path / "seed"
    write_jsonl(
        seed / "04-artifacts.jsonl",
        [
            artifact(
                "ia-aie-alpha-talk",
                "Alpha Talk (Ann Lee, Acme — AI Engineer World's Fair)",
                "https://youtu.be/AAA",
                "2026-08-22T00:00:00Z",
            ),
            artifact(
                "ia-aie-beta-talk",
                "Beta Talk (Bo Chen, Beta — AI Engineer World's Fair)",
                "https://youtu.be/BBB",
                "2026-07-01T00:00:00Z",
            ),
            artifact(
                "ia-aie-some-article",
                "Some Article",
                "https://example.com/a",
                "2026-04-01T00:00:00Z",
                artifact_type="article",
            ),
        ],
    )
    # chunks deliberately out of order and spread across parts
    write_jsonl(
        seed / "chunks" / "part-01.jsonl",
        chunk("alpha-talk", 10, "ten", "ia-aie-alpha-talk")
        + chunk("alpha-talk", 2, "two", "ia-aie-alpha-talk")
        + chunk("beta-talk", 0, "beta zero", "ia-aie-beta-talk"),
    )
    write_jsonl(
        seed / "chunks" / "part-02.jsonl",
        chunk("alpha-talk", 0, "[Music] zero", "ia-aie-alpha-talk"),
    )
    return seed


def test_writes_one_file_per_talk_that_has_chunks(seed, tmp_path):
    out = tmp_path / "talks"

    written = build_corpus(seed, out, overrides={})

    assert written == 2
    assert sorted(p.name for p in out.iterdir()) == [
        "ia-aie-alpha-talk.md",
        "ia-aie-beta-talk.md",
    ]


def test_talk_file_is_header_then_transcript_in_chunk_order(seed, tmp_path):
    out = tmp_path / "talks"

    build_corpus(seed, out, overrides={})

    assert (out / "ia-aie-alpha-talk.md").read_text() == (
        "# Alpha Talk (Ann Lee, Acme — AI Engineer World's Fair)\n"
        "- talk: ia-aie-alpha-talk\n"
        "- video: https://youtu.be/AAA\n"
        "- published: 2026-08-22\n"
        "\n"
        "[Music] zero\n"
        "\n"
        "two\n"
        "\n"
        "ten\n"
    )


def test_override_moves_mislinked_chunks_to_their_own_talk(seed, tmp_path):
    # the graph attaches gamma's chunks to beta's talk; the override puts them back
    write_jsonl(
        seed / "chunks" / "part-03.jsonl",
        chunk("gamma-talk", 1, "gamma one", "ia-aie-beta-talk")
        + chunk("gamma-talk", 0, "gamma zero", "ia-aie-beta-talk"),
    )
    with (seed / "04-artifacts.jsonl").open("a") as f:
        f.write(
            json.dumps(
                artifact(
                    "ia-aie-gamma-talk",
                    "Gamma Talk (Cy Diaz, Beta — AI Engineer World's Fair)",
                    "https://youtu.be/CCC",
                    "2026-08-09T00:00:00Z",
                )
            )
            + "\n"
        )
    out = tmp_path / "talks"

    build_corpus(seed, out, overrides={"gamma-talk": "ia-aie-gamma-talk"})

    assert (out / "ia-aie-beta-talk.md").read_text().endswith("\n\nbeta zero\n")
    assert (out / "ia-aie-gamma-talk.md").read_text() == (
        "# Gamma Talk (Cy Diaz, Beta — AI Engineer World's Fair)\n"
        "- talk: ia-aie-gamma-talk\n"
        "- video: https://youtu.be/CCC\n"
        "- published: 2026-08-09\n"
        "\n"
        "gamma zero\n"
        "\n"
        "gamma one\n"
    )


def test_two_transcripts_on_one_talk_without_override_is_an_error(seed, tmp_path):
    write_jsonl(
        seed / "chunks" / "part-03.jsonl",
        chunk("gamma-talk", 0, "gamma zero", "ia-aie-beta-talk"),
    )

    with pytest.raises(ValueError, match=r"ia-aie-beta-talk.*beta-talk.*gamma-talk"):
        build_corpus(seed, tmp_path / "talks", overrides={})


def test_rebuild_removes_files_for_talks_no_longer_in_the_seed(seed, tmp_path):
    out = tmp_path / "talks"
    out.mkdir()
    (out / "ia-aie-gone.md").write_text("stale")

    build_corpus(seed, out, overrides={})

    assert not (out / "ia-aie-gone.md").exists()


def test_corpus_command_builds_into_the_given_directory(seed, tmp_path):
    out = tmp_path / "talks"

    code = main(["corpus", "--seed", str(seed), "--out", str(out)])

    assert code == 0
    assert (out / "ia-aie-alpha-talk.md").exists()
