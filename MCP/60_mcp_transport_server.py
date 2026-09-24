from mcp.server.mcpserver import MCPServer

server = MCPServer("Transport Demo")


@server.tool()
def hello(name: str) -> str:
    """Say hello."""

    return f"Hello {name}!"


if __name__ == "__main__":
    server.run(transport="stdio")