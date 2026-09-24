from mcp.server.mcpserver import MCPServer


server = MCPServer("Support Prompt Server")


@server.prompt()
def customer_support_prompt(
    customer_name: str,
    issue: str
) -> str:
    """Create a customer support prompt."""

    return f"""
Customer: {customer_name}

Issue:
{issue}

Provide a professional support response.
"""


if __name__ == "__main__":
    server.run(transport="stdio")