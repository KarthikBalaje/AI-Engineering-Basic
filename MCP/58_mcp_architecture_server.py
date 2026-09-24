from mcp.server.mcpserver import MCPServer


server = MCPServer("Customer Server")


@server.tool()
def get_customer(customer_id: int) -> dict:
    """Get customer information."""

    customers = {
        101: {
            "name": "Alice",
            "status": "Active"
        },
        102: {
            "name": "Bob",
            "status": "Inactive"
        }
    }

    return customers.get(
        customer_id,
        {
            "error": "Customer not found"
        }
    )


if __name__ == "__main__":
    server.run(transport="stdio")