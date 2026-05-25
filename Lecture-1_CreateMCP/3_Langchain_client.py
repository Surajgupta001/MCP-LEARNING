import os
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient


# Path to the MCP Server Script
MCP_SERVER_SCRIPT = os.path.join(
    (os.path.dirname(os.path.abspath(__file__))), "1_first_mcpServer_stdio.py"
)

# Path to the Virtual Environment
VENV_PYTHON = os.path.join(
    (os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), ".venv"
)


async def main():
    # Create an instance of the MultiServerMCPClient
    mcp_client = MultiServerMCPClient(
        {
            "data_fetch_mcp_stdio": {
                "transport": "stdio",
                "command": os.path.join(VENV_PYTHON, "Scripts", "python.exe"),
                "args": [MCP_SERVER_SCRIPT],
            }
        }
    )

    print("Connecting to MCP server...")

    # List the tools
    tools = await mcp_client.get_tools()
    print("Available tools from the MCP server:", tools)


if __name__ == "__main__":
    asyncio.run(main())
