from langchain_core.tools import tool


@tool
def add_numbers(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


@tool
def get_customer_status(customer_id: int) -> str:
    """Return the status of a customer."""
    customers = {
        101: "Active",
        102: "Inactive",
        103: "Active"
    }

    return customers.get(customer_id, "Customer not found")


print(add_numbers.invoke({
    "a": 10,
    "b": 20
}))

print(get_customer_status.invoke({
    "customer_id": 101
}))