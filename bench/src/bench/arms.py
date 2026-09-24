"""The two benchmark arms: the same agent with different data interfaces.

Both arms run the same model with the same effort, caps and answer contract.
They differ only in tools, working directory and system prompt. Neither loads
filesystem settings (CLAUDE.md, hooks, plugins), MCP servers, skills or
subagents.

Each arm's gate runs as a PreToolUse hook on every tool call and returns an
explicit allow or deny. `can_use_tool` only fires for calls that still need
permission, so it is a deny-everything backstop rather than the gate.
"""

import os
import re
import shlex
from collections.abc import Callable
from pathlib import Path

from claude_agent_sdk import ClaudeAgentOptions, HookMatcher, PermissionResultDeny

from bench.provider import AGENT_MODEL

EFFORT = "high"
MAX_TURNS = 300  # a runaway guard only; budget and wall clock are the working caps
MAX_BUDGET_USD = 10.0

# A gate returns None to allow a tool call, or the reason it is denied.
Gate = Callable[[str, dict], str | None]

SHELL_CONTROL = re.compile(r"[;&|`$<>\n\r]")
OMNIGRAPH_VERBS = {"alias", "query"}
OMNIGRAPH_VALUE_FLAGS = {"--params", "--format", "--profile"}
OMNIGRAPH_BARE_FLAGS = {"--help", "-h"}
OMNIGRAPH_USAGE = (
    "Only `omnigraph alias <name> [args]` and `omnigraph query <name>` are allowed, "
    "with --params, --format or --profile"
)


def _inside(root: Path, path: str) -> bool:
    if path.startswith("~"):
        return False
    return Path(root, path).resolve().is_relative_to(root.resolve())


def _saved_output(spill_root: Path | None, path: str) -> bool:
    """A file the CLI saved an oversized tool result to: <claude-home>/.../tool-results/<file>."""
    if spill_root is None or not Path(path).is_absolute():
        return False
    resolved, root = Path(path).resolve(), spill_root.resolve()
    return resolved.is_relative_to(root) and "tool-results" in resolved.relative_to(root).parts[:-1]


def _escapes(pattern: str) -> bool:
    return pattern.startswith(("/", "~")) or ".." in Path(pattern).parts


def markdown_gate(root: Path, spill_root: Path | None = None) -> Gate:
    def gate(tool: str, tool_input: dict) -> str | None:
        if tool == "Read":
            path = tool_input.get("file_path", "")
            if not _inside(root, path) and not _saved_output(spill_root, path):
                return f"Read is limited to the talk files; {path} is outside them"
            return None
        if tool in ("Grep", "Glob"):
            path = tool_input.get("path") or "."
            if not _inside(root, path):
                return f"{tool} is limited to the talks directory; {path} is outside it"
            pattern = tool_input.get("glob" if tool == "Grep" else "pattern") or ""
            if _escapes(pattern):
                return f"{tool} patterns must stay inside the talks directory: {pattern}"
            return None
        return f"{tool} is not available here; use Read, Grep or Glob on the talk files"

    return gate


def _check_omnigraph_command(command: str) -> str | None:
    if SHELL_CONTROL.search(command):
        return f"No shell operators, substitutions or redirects. {OMNIGRAPH_USAGE}"
    try:
        tokens = shlex.split(command)
    except ValueError:
        return f"Could not parse the command (unbalanced quotes?). {OMNIGRAPH_USAGE}"
    if len(tokens) < 2 or tokens[0] != "omnigraph" or tokens[1] not in OMNIGRAPH_VERBS:
        return OMNIGRAPH_USAGE

    args = iter(tokens[2:])
    for token in args:
        if not token.startswith("-"):
            continue
        flag, has_value, _ = token.partition("=")
        if flag in OMNIGRAPH_BARE_FLAGS and not has_value:
            continue
        if flag in OMNIGRAPH_VALUE_FLAGS:
            if not has_value:
                next(args, None)  # the flag's value
            continue
        return f"{flag} is not allowed. {OMNIGRAPH_USAGE}"
    return None


def omnigraph_gate(scratch: Path, spill_root: Path | None = None) -> Gate:
    def gate(tool: str, tool_input: dict) -> str | None:
        if tool == "Read":
            path = tool_input.get("file_path", "")
            if not _inside(scratch, path) and not _saved_output(spill_root, path):
                return f"Read is limited to tool output the CLI saved for you; {path} is not one"
            return None
        if tool != "Bash":
            return f"{tool} is not available here. {OMNIGRAPH_USAGE}"
        if tool_input.get("run_in_background"):
            return "Background commands are not available here"
        return _check_omnigraph_command(tool_input.get("command", ""))

    return gate


def single_alias_gate(scratch: Path, alias: str, spill_root: Path | None = None) -> Gate:
    """The Omnigraph arm held to one stored query: `omnigraph alias <alias>` (with --format),
    plus Read of the output the CLI saved. Every other command is denied."""
    usage = f"Only `omnigraph alias {alias}` is allowed, optionally with --format"

    def gate(tool: str, tool_input: dict) -> str | None:
        if tool == "Read":
            path = tool_input.get("file_path", "")
            if not _inside(scratch, path) and not _saved_output(spill_root, path):
                return f"Read is limited to tool output the CLI saved for you; {path} is not one"
            return None
        if tool != "Bash":
            return f"{tool} is not available here. {usage}"
        if tool_input.get("run_in_background"):
            return "Background commands are not available here"
        command = tool_input.get("command", "")
        if SHELL_CONTROL.search(command):
            return f"No shell operators, substitutions or redirects. {usage}"
        try:
            tokens = shlex.split(command)
        except ValueError:
            return f"Could not parse the command (unbalanced quotes?). {usage}"
        if tokens[:3] != ["omnigraph", "alias", alias]:
            return usage
        rest = tokens[3:]
        if (
            len(rest) == 2
            and rest[0] == "--format"
            or len(rest) == 1
            and rest[0].startswith("--format=")
        ):
            return None
        return None if not rest else usage

    return gate


def gate_hook(gate: Gate) -> HookMatcher:
    async def pre_tool_use(hook_input, tool_use_id, context):
        reason = gate(hook_input["tool_name"], hook_input["tool_input"])
        output = {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny" if reason else "allow",
        }
        if reason:
            output["permissionDecisionReason"] = reason
        return {"hookSpecificOutput": output}

    return HookMatcher(matcher=None, hooks=[pre_tool_use])


async def _deny_unapproved(tool_name, tool_input, context):
    return PermissionResultDeny(message=f"{tool_name} was not approved by this arm's gate")


def _options(
    tools: list[str], workdir: Path, system_prompt: str, gate: Gate, env: dict[str, str]
) -> ClaudeAgentOptions:
    return ClaudeAgentOptions(
        model=AGENT_MODEL,
        effort=EFFORT,
        max_turns=MAX_TURNS,
        max_budget_usd=MAX_BUDGET_USD,
        setting_sources=[],
        strict_mcp_config=True,
        tools=tools,
        cwd=workdir,
        system_prompt=system_prompt,
        hooks={"PreToolUse": [gate_hook(gate)]},
        can_use_tool=_deny_unapproved,
        env=env,
    )


def _env(provider_env: dict[str, str], claude_home: Path) -> dict[str, str]:
    # A per-run Claude home keeps the CLI off the operator's ~/.claude entirely.
    return {**provider_env, "CLAUDE_CONFIG_DIR": str(claude_home)}


def markdown_options(
    talks_dir: Path, system_prompt: str, provider_env: dict[str, str], claude_home: Path
) -> ClaudeAgentOptions:
    gate = markdown_gate(talks_dir, spill_root=claude_home)
    env = _env(provider_env, claude_home)
    return _options(["Read", "Grep", "Glob"], talks_dir, system_prompt, gate, env)


def omnigraph_options(
    scratch_dir: Path,
    system_prompt: str,
    shim_bin: Path,
    provider_env: dict[str, str],
    claude_home: Path,
    gate: Gate | None = None,
) -> ClaudeAgentOptions:
    gate = gate or omnigraph_gate(scratch_dir, spill_root=claude_home)
    env = _env(provider_env, claude_home)
    env["PATH"] = os.pathsep.join([str(shim_bin), os.environ.get("PATH", "")])
    return _options(["Bash", "Read"], scratch_dir, system_prompt, gate, env)
