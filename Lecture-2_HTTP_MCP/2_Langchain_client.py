import os
import asyncio
from typing import Any

from langchain_mcp_adapters.client import MultiServerMCPClient

# Path to the MCP server script
MCP_SERVER_SCRIPT = os.path.join(
    (os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "Lecture-1_CreateMCP",
    "1_first_mcpServer_stdio.py",
)

# Path to the virtual environment
VENV_PYTHON = os.path.join(
    (os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), ".venv"
)


async def main():
    connections: dict[str, Any] = {
        # Stdio MCP Server Configuration
        "data_fetch_mcp_stdio": {
            "transport": "stdio",
            "command": os.path.join(VENV_PYTHON, "Scripts", "python.exe"),
            "args": [MCP_SERVER_SCRIPT],
        },
        # Streamable HTTP MCP Server Configuration
        "data_fetch_mcp_http": {
            "transport": "streamable-http",
            "url": "http://localhost:8050/mcp",
        },
    }

    mcp_client = MultiServerMCPClient(connections)

    print("Connecting to MCP server...")

    # List the tools
    tools = await mcp_client.get_tools()

    print("Available tools from the MCP server:")
    print(tools)


if __name__ == "__main__":
    asyncio.run(main())
