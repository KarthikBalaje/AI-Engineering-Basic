from mcp.server.mcpserver import MCPServer
import sys
from datetime import datetime


server = MCPServer("Secure Customer Server")


# ============================================================
# MOCK DATABASE
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
# AUDIT LOG
# ============================================================

def audit_log(action, customer_id, result):

    timestamp = datetime.now().isoformat()

    print(
        f"[AUDIT] {timestamp} | "
        f"action={action} | "
        f"customer={customer_id} | "
        f"result={result}",
        file=sys.stderr
    )


# ============================================================
# TOOL 1 — SAFE READ
# ============================================================

@server.tool()
def get_customer(customer_id: int) -> dict:
    """
    Get customer information.

    This is a read-only operation.
    """

    customer = customers.get(customer_id)

    if not customer:

        audit_log(
            "get_customer",
            customer_id,
            "NOT_FOUND"
        )

        return {
            "error": "Customer not found"
        }

    audit_log(
        "get_customer",
        customer_id,
        "SUCCESS"
    )

    return {
        "customer_id": customer_id,
        **customer
    }


# ============================================================
# TOOL 2 — SENSITIVE OPERATION
# ============================================================

@server.tool()
def update_customer_status(
    customer_id: int,
    status: str,
    approved: bool = False
) -> dict:
    """
    Update customer status.

    Requires explicit approval.
    """

    # --------------------------------------------------------
    # Authorization
    # --------------------------------------------------------

    if not approved:

        audit_log(
            "update_customer_status",
            customer_id,
            "BLOCKED_NO_APPROVAL"
        )

        return {
            "success": False,
            "message": "Approval required."
        }

    # --------------------------------------------------------
    # Validate customer
    # --------------------------------------------------------

    if customer_id not in customers:

        audit_log(
            "update_customer_status",
            customer_id,
            "NOT_FOUND"
        )

        return {
            "success": False,
            "message": "Customer not found."
        }

    # --------------------------------------------------------
    # Validate status
    # --------------------------------------------------------

    allowed_statuses = {
        "Active",
        "Inactive"
    }

    if status not in allowed_statuses:

        audit_log(
            "update_customer_status",
            customer_id,
            "INVALID_STATUS"
        )

        return {
            "success": False,
            "message": "Invalid status."
        }

    # --------------------------------------------------------
    # Execute
    # --------------------------------------------------------

    customers[customer_id]["status"] = status

    audit_log(
        "update_customer_status",
        customer_id,
        "SUCCESS"
    )

    return {
        "success": True,
        "customer_id": customer_id,
        "new_status": status
    }


# ============================================================
# RESOURCE
# ============================================================

@server.resource("policy://customer-support")
def customer_support_policy() -> str:
    """
    Customer support policy.
    """

    return """
Customer Support Policy

1. Customer information can be read automatically.

2. Customer status changes require explicit approval.

3. Invalid customer IDs must be rejected.

4. Invalid status values must be rejected.

5. Sensitive operations must be logged.
"""


# ============================================================
# SERVER
# ============================================================

if __name__ == "__main__":

    server.run(
        transport="stdio"
    )