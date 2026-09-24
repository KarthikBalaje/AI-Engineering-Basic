import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool

load_dotenv()


llm = ChatOpenAI(
    base_url=os.getenv("BASE_URL"),
    model=os.getenv("MODEL"),
    api_key=os.getenv("API_KEY"),
    temperature=0
)


@tool
def add_numbers(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


@tool
def multiply_numbers(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b


@tool
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


tools = [
    add_numbers,
    multiply_numbers,
    get_customer_status
]

llm_with_tools = llm.bind_tools(tools)


# Tool registry
tool_map = {
    "add_numbers": add_numbers,
    "multiply_numbers": multiply_numbers,
    "get_customer_status": get_customer_status
}


questions = [
    "What is 10 multiplied by 5?",
    "What is the status of customer 102?",
    "What is 20 plus 30?"
]


for question in questions:

    response = llm_with_tools.invoke(question)

    tool_call = response.tool_calls[0]

    tool_name = tool_call["name"]
    tool_args = tool_call["args"]

    selected_tool = tool_map[tool_name]

    result = selected_tool.invoke(tool_args)

    print("\nQuestion:", question)
    print("Selected tool:", tool_name)
    print("Arguments:", tool_args)
    print("Tool result:", result)