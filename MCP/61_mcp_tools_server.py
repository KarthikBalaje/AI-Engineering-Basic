from mcp.server.mcpserver import MCPServer


server = MCPServer("Math Server")


@server.tool()
def add_numbers(a: int, b: int) -> int:
    """Add two numbers."""

    return a + b


@server.tool()
def multiply_numbers(a: int, b: int) -> int:
    """Multiply two numbers."""

    return a * b


if __name__ == "__main__":
    server.run(transport="stdio")