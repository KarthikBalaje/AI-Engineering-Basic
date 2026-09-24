from mcp.server.mcpserver import MCPServer


server = MCPServer("Customer Support Server")


@server.tool()
def get_customer_status(customer_id: int) -> str:
    """Get the status of a customer."""

    customers = {
        101: "Active",
        102: "Inactive",
        103: "Active"
    }

    return customers.get(
        customer_id,
        "Customer not found"
    )


if __name__ == "__main__":
    server.run(transport="stdio")