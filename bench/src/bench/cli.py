"""Command-line entry point: `uv run bench <command>`."""

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

from bench.corpus import CHUNK_TALK_OVERRIDES, build_corpus
from bench.omnigraph import install_shim

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
    return 0
