from mcp.server.mcpserver import MCPServer


server = MCPServer("Customer Support Server")


# ============================================================
# DATA
# ============================================================

customers = {
    101: {
        "name": "Alice",
        "status": "Active",
        "plan": "Premium"
    },
    102: {
        "name": "Bob",
        "status": "Inactive",
        "plan": "Basic"
    },
    103: {
        "name": "Charlie",
        "status": "Active",
        "plan": "Premium"
    }
}


# ============================================================
# TOOL
# ============================================================

@server.tool()
def get_customer_status(customer_id: int) -> str:
    """Get the current status of a customer."""

    customer = customers.get(customer_id)

    if not customer:
        return "Customer not found"

    return customer["status"]


@server.tool()
def update_customer_status(
    customer_id: int,
    status: str
) -> str:
    """Update the status of a customer."""

    if customer_id not in customers:
        return "Customer not found"

    customers[customer_id]["status"] = status

    return "Customer status updated"


# ============================================================
# RESOURCE
# ============================================================

@server.resource("customer://{customer_id}")
def customer_profile(customer_id: int) -> str:
    """Return customer profile information."""

    customer = customers.get(customer_id)

    if not customer:
        return "Customer not found"

    return f"""
Customer ID: {customer_id}
Name: {customer["name"]}
Status: {customer["status"]}
Plan: {customer["plan"]}
"""


# ============================================================
# RESOURCE
# ============================================================

@server.resource("policy://customer-support")
def customer_support_policy() -> str:
    """Return customer support policy."""

    return """
Customer Support Policy

1. Premium customers receive priority support.
2. Inactive customers must reactivate their account.
3. Refund requests require order verification.
4. Account changes require customer verification.
"""


# ============================================================
# PROMPT
# ============================================================

@server.prompt()
def customer_analysis_prompt(
    customer_id: int
) -> str:
    """Create a prompt for analyzing a customer."""

    return f"""
Analyze customer {customer_id}.

Consider:

1. Customer status
2. Customer plan
3. Customer support policy
4. Whether any action is required

Provide a concise analysis.
"""


# ============================================================
# SERVER
# ============================================================

if __name__ == "__main__":
    server.run(transport="stdio")