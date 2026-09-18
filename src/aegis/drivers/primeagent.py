"""Prime Agent driver — native ACP via `prime-agent --mode acp`.

Prime Agent ships an ACP mode of its own (initialize / newSession / prompt
streaming over the agent-client-protocol SDK), so the generic ``AcpDriver``
does the protocol work and this shim only builds argv. Model selection
rides the CLI's ``--model <id>`` flag; auth is prime-agent's own provider
config, untouched.
"""

from __future__ import annotations

from aegis.config import Agent
from aegis.drivers.acp import AcpDriver


class PrimeAgentDriver(AcpDriver):
    BASE_CMD = ["prime-agent", "--mode", "acp"]

    def build_argv(
        self, agent: Agent, cwd: str, mcp_url: str, handle: str
    ) -> list[str]:
        argv = list(self.BASE_CMD)
        if getattr(agent, "model", ""):
            argv += ["--model", agent.model]
        return argv
