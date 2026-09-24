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
    """Add two numbers together."""
    return a + b


@tool
def multiply_numbers(a: int, b: int) -> int:
    """Multiply two numbers together."""
    return a * b


@tool
def get_customer_status(customer_id: int) -> str:
    """Get the current status of a customer."""

    customers = {
        101: "Active",
        102: "Inactive",
        103: "Active"
    }

    return customers.get(customer_id, "Customer not found")


tools = [
    add_numbers,
    multiply_numbers,
    get_customer_status
]


llm_with_tools = llm.bind_tools(tools)


questions = [
    "What is 25 plus 17?",
    "Calculate 12 multiplied by 8.",
    "Is customer 102 active?",
    "What is 100 + 200?",
    "Multiply 7 by 9.",
    "Check customer 103."
]


for question in questions:

    response = llm_with_tools.invoke(question)

    print("\n" + "=" * 50)
    print("Question:", question)

    if response.tool_calls:

        for tool_call in response.tool_calls:

            print("Selected Tool:", tool_call["name"])
            print("Arguments:", tool_call["args"])

    else:

        print("No tool selected.")
        print("LLM response:", response.content)