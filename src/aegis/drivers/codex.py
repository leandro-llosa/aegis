"""Codex driver — ACP via the `codex-acp` adapter.

The Codex CLI has no native ACP mode; ``@agentclientprotocol/codex-acp``
(``npm install -g @agentclientprotocol/codex-acp``) is the maintained
adapter — the older ``@zed-industries/codex-acp`` package is deprecated.
The adapter accepts Codex config overrides as ``-c key=value`` with the
value parsed as TOML, so model selection rides ``-c model="<id>"``. Auth
is Codex's own (``codex login``), untouched.
"""

from __future__ import annotations

from aegis.config import Agent
from aegis.drivers.acp import AcpDriver


class CodexDriver(AcpDriver):
    BASE_CMD = ["codex-acp"]

    def build_argv(
        self, agent: Agent, cwd: str, mcp_url: str, handle: str
    ) -> list[str]:
        argv = list(self.BASE_CMD)
        if getattr(agent, "model", ""):
            argv += ["-c", f'model="{agent.model}"']
        return argv
