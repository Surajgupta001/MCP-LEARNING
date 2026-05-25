import os
from mcp.client.stdio import stdio_client
from mcp import ClientSession, StdioServerParameters
import asyncio

# Path to the MCP server script
MCP_SERVER_SCRIPT = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "1_first_mcpServer_stdio.py"
)
print(f"Starting MCP server from script: {MCP_SERVER_SCRIPT}")

# Create Server Parameters
server_params = StdioServerParameters(
    command="python", args=[str(MCP_SERVER_SCRIPT)], env={}
)


# Create a client session
async def main():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # Fetch the tool available from the server
            tools = await session.list_tools()
            print("Available tools from the MCP server:", tools)

            # Use the fetch tool
            result = await session.call_tool(
                "process", arguments={"path": "/path/to/data"}
            )
            print("Result from process tool:", result)


if __name__ == "__main__":
    asyncio.run(main())
