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

MODEL = "claude-sonnet-5"
EFFORT = "high"
MAX_TURNS = 100  # pilot caps; revisit after C1.3
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


def _escapes(pattern: str) -> bool:
    return pattern.startswith(("/", "~")) or ".." in Path(pattern).parts


def markdown_gate(root: Path) -> Gate:
    def gate(tool: str, tool_input: dict) -> str | None:
        if tool == "Read":
            path = tool_input.get("file_path", "")
            if not _inside(root, path):
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


def omnigraph_gate(scratch: Path) -> Gate:
    def gate(tool: str, tool_input: dict) -> str | None:
        if tool == "Read":
            path = tool_input.get("file_path", "")
            if not _inside(scratch, path):
                return f"Read is limited to spilled tool output in {scratch}"
            return None
        if tool != "Bash":
            return f"{tool} is not available here. {OMNIGRAPH_USAGE}"
        if tool_input.get("run_in_background"):
            return "Background commands are not available here"
        return _check_omnigraph_command(tool_input.get("command", ""))

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
        model=MODEL,
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


def markdown_options(talks_dir: Path, system_prompt: str) -> ClaudeAgentOptions:
    return _options(
        ["Read", "Grep", "Glob"], talks_dir, system_prompt, markdown_gate(talks_dir), {}
    )


def omnigraph_options(scratch_dir: Path, system_prompt: str, shim_bin: Path) -> ClaudeAgentOptions:
    path = os.pathsep.join([str(shim_bin), os.environ.get("PATH", "")])
    return _options(
        ["Bash", "Read"], scratch_dir, system_prompt, omnigraph_gate(scratch_dir), {"PATH": path}
    )
