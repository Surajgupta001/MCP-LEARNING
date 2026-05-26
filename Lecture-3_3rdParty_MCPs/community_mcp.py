import asyncio

from langchain_mcp_adapters.client import MultiServerMCPClient


async def main():
    # Create MCP Client
    mcp_client = MultiServerMCPClient(
        {
            "data_fetch_mcp_stdio": {
                "transport": "stdio",
                "command": "uvx",
                "args": ["duckduckgo-mcp-server"],
            }
        }
    )

    # Get Tools
    tools = await mcp_client.get_tools()

    print("\nAvailable Tools:\n")

    for tool in tools:
        print(f"Tool: {tool.name}")
        print(f"Description: {tool.description}")

        # safer
        print(f"Args Schema: {tool.args_schema}")

        print("-" * 40)

    # Call Tool
    fetch_tool = tools[0]
    result = await fetch_tool.ainvoke({"query": "What is the capital of France?"})
    print("\nTool Result:\n")
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
