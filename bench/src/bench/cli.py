"""Command-line entry point: `uv run bench <command>`."""

import argparse
import os
import shutil
import subprocess
import sys
import urllib.request
from pathlib import Path

from bench.corpus import CHUNK_TALK_OVERRIDES, build_corpus
from bench.omnigraph import graph_secrets_in, install_shim

BENCH_DIR = Path(__file__).resolve().parents[2]
REPO_DIR = BENCH_DIR.parent
SHIM_BIN = BENCH_DIR / "bin"


def _real_omnigraph() -> Path | None:
    """The omnigraph CLI on PATH, skipping the shim itself."""
    dirs = os.environ.get("PATH", "").split(os.pathsep)
    path = os.pathsep.join(d for d in dirs if d and Path(d).resolve() != SHIM_BIN.resolve())
    found = shutil.which("omnigraph", path=path)
    return Path(found).resolve() if found else None


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="bench")
    commands = parser.add_subparsers(dest="command", required=True)

    corpus = commands.add_parser("corpus", help="build corpus/talks/*.md from the seed's chunks")
    corpus.add_argument("--seed", type=Path, default=REPO_DIR / "seed")
    corpus.add_argument("--out", type=Path, default=BENCH_DIR / "corpus" / "talks")

    shim = commands.add_parser(
        "shim", help="install the reader-only omnigraph config (act-reader token on stdin)"
    )
    shim.add_argument("--home", type=Path, default=BENCH_DIR / ".omnigraph-home")
    shim.add_argument("--alias-pack", type=Path, default=REPO_DIR / "omnigraph-config.example.yaml")
    shim.add_argument("--omnigraph", type=Path, help="the real CLI (default: first on PATH)")

    check = commands.add_parser(
        "check-questions", help="answerability of each question from the markdown corpus alone"
    )
    check.add_argument("--questions", type=Path, default=BENCH_DIR / "questions.yaml")
    check.add_argument("--corpus", type=Path, default=BENCH_DIR / "corpus" / "talks")

    probe = commands.add_parser("probe", help="live isolation probe per arm (spends API money)")
    probe.add_argument("--arm", choices=["markdown", "omnigraph", "both"], default="both")

    args = parser.parse_args(argv)
    if args.command == "corpus":
        written = build_corpus(args.seed, args.out, CHUNK_TALK_OVERRIDES)
        print(f"wrote {written} talks to {args.out}")
    elif args.command == "shim":
        token = sys.stdin.read().strip()
        if not token:
            parser.exit(2, "bench shim: pipe the act-reader token on stdin\n")
        omnigraph_bin = args.omnigraph or _real_omnigraph()
        if omnigraph_bin is None:
            parser.exit(2, "bench shim: no omnigraph CLI on PATH\n")
        try:
            install_shim(args.home, args.alias_pack, omnigraph_bin, token)
        except subprocess.CalledProcessError as e:
            parser.exit(1, f"bench shim: omnigraph login failed: {e.stderr.strip()}\n")
        print(f"reader-only omnigraph config installed in {args.home}")
    elif args.command == "check-questions":
        from bench.questions import check_questions, load_questions

        results = check_questions(load_questions(args.questions), args.corpus)
        for r in results:
            hits = ", ".join(f"{term!r}: {n}" for term, n in r["hits"].items()) or r["detail"]
            print(f"{'PASS' if r['ok'] else 'FAIL'}  {r['id']}  {r['shape']:<12} {hits}")
        return 0 if all(r["ok"] for r in results) else 1
    elif args.command == "probe":
        return _probe(parser, ["markdown", "omnigraph"] if args.arm == "both" else [args.arm])
    return 0


def _probe(parser: argparse.ArgumentParser, arms: list[str]) -> int:
    if secrets := graph_secrets_in(os.environ):
        parser.exit(2, f"bench probe: unset graph credentials first: {', '.join(secrets)}\n")
    from bench.probe import run_probe
    from bench.provider import openrouter_env

    provider_env = openrouter_env(BENCH_DIR / ".env")
    if "markdown" in arms and not any((BENCH_DIR / "corpus" / "talks").glob("*.md")):
        parser.exit(2, "bench probe: no corpus; run `uv run bench corpus`\n")
    if "omnigraph" in arms:
        if not (BENCH_DIR / ".omnigraph-home" / "omnigraph-bin").exists():
            parser.exit(2, "bench probe: reader shim not installed; see `bench shim`\n")
        try:
            urllib.request.urlopen("http://127.0.0.1:8081/healthz", timeout=3)
        except OSError:
            parser.exit(2, "bench probe: graph server is down; run scripts/local-graph.sh serve\n")

    failed = 0
    for arm in arms:
        summary = run_probe(arm, BENCH_DIR, REPO_DIR, provider_env, BENCH_DIR / "runs" / "_probe")
        print(
            f"\n{arm}: {summary['num_turns']} turns, {summary['wall_s']}s, ${summary['cost_usd']}"
        )
        for c in summary["checks"]:
            print(f"  {'PASS' if c['ok'] else 'FAIL'}  {c['check']:<20} {c['detail']}")
        print(f"  trace: {summary['out']}")
        failed += sum(not c["ok"] for c in summary["checks"])
    return 1 if failed else 0
