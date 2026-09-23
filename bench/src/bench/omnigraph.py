"""The Omnigraph arm's reader-only CLI: a bench-only OMNIGRAPH_HOME behind a shim.

`bench shim` writes .omnigraph-home/: the repo's alias pack as config.yaml, the
act-reader credential (stored by `omnigraph login`), and the path of the real
CLI. bin/omnigraph, first on the arm's PATH, runs that CLI with OMNIGRAPH_HOME
pointed there and every other graph credential unset.
"""

import os
import re
import shutil
import subprocess
from collections.abc import Mapping
from pathlib import Path

SERVER = "intel-local"

# Credentials an agent with a shell could use to reach the graph or its store
# without going through the reader token.
GRAPH_SECRET = re.compile(
    r"^(AWS_\w+|TOKEN_ACT_\w+|GEMINI_API_KEY|OMNIGRAPH_BEARER_TOKEN|OMNIGRAPH_CONTROL_API"
    r"|OMNIGRAPH_SERVER_BEARER_TOKENS_JSON)$"
)


def graph_secrets_in(environ: Mapping[str, str]) -> list[str]:
    return sorted(name for name in environ if GRAPH_SECRET.match(name))


def install_shim(home: Path, alias_pack: Path, omnigraph_bin: Path, token: str) -> None:
    home.mkdir(parents=True, exist_ok=True)
    home.chmod(0o700)
    shutil.copyfile(alias_pack, home / "config.yaml")
    (home / "omnigraph-bin").write_text(f"{omnigraph_bin}\n")
    subprocess.run(
        [str(omnigraph_bin), "login", SERVER],
        input=token,
        text=True,
        check=True,
        capture_output=True,
        env={**os.environ, "OMNIGRAPH_HOME": str(home)},
    )
