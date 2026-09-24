import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain.agents import create_agent

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


agent = create_agent(
    model=llm,
    tools=[
        add_numbers,
        multiply_numbers
    ]
)


result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Calculate (10 + 20) * 5."
            }
        ]
    }
)


print("\n===== AGENT LOOP =====\n")


for message in result["messages"]:

    print("Message type:", type(message).__name__)

    if message.content:
        print("Content:", message.content)

    if hasattr(message, "tool_calls") and message.tool_calls:
        print("Tool calls:")

        for tool_call in message.tool_calls:
            print(
                "  Tool:",
                tool_call["name"]
            )

            print(
                "  Arguments:",
                tool_call["args"]
            )

    print("-" * 50)