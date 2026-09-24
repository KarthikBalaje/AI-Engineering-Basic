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


# Give the tool to the model
llm_with_tools = llm.bind_tools([
    add_numbers
])


# Ask the question
response = llm_with_tools.invoke(
    "What is 25 + 17?"
)


print("Tool calls:")
print(response.tool_calls)


# ----------------------------------------
# Execute the tool
# ----------------------------------------

tool_call = response.tool_calls[0]

tool_result = add_numbers.invoke(
    tool_call["args"]
)

print("\nTool result:")
print(tool_result)