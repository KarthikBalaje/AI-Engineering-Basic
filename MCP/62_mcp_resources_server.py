from mcp.server.mcpserver import MCPServer


server = MCPServer("Documentation Server")


@server.resource("policy://customer-support")
def customer_policy() -> str:
    """Customer support policy."""

    return """
    Active customers receive priority support.
    Inactive customers must reactivate their account
    before receiving premium support.
    """


if __name__ == "__main__":
    server.run(transport="stdio")