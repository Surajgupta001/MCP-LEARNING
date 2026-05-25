from fastmcp import FastMCP

# Create an instance of FastMCP
mcp = FastMCP()


# Start the MCP server function
@mcp.tool()
def fetch_http():
    """Use this tool to fetch data from the source."""
    # Simulate fetching data (you can replace this with actual data fetching logic)
    """This is a placeholder for the fetch function. You can implement your data fetching logic here."""
    return {"message": "Hello from the MCP server!"}


@mcp.tool()
def process_http(path: str):
    """Use this tool to process the fetched data."""
    # Simulate processing data (you can replace this with actual data processing logic)
    """This is a placeholder for the process function. You can implement your data processing logic here."""
    return {"message": f"Data processed successfully from {path}!"}


if __name__ == "__main__":
    # Start the MCP server HTTP transport
    mcp.run(transport="streamable-http", host="localhost", port=8050)
