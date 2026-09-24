import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from langgraph.graph import StateGraph, START, END

from langgraph.checkpoint.memory import MemorySaver

from typing import TypedDict


load_dotenv()


llm = ChatOpenAI(
    base_url=os.getenv("BASE_URL"),
    model=os.getenv("MODEL"),
    api_key=os.getenv("API_KEY"),
    temperature=float(os.getenv("TEMPERATURE"))
)


class State(TypedDict):
    message: str
    response: str


def chatbot(state: State):

    response = llm.invoke(
        state["message"]
    )

    return {
        "response": response.content
    }


graph = StateGraph(State)

graph.add_node("chatbot", chatbot)

graph.add_edge(START, "chatbot")
graph.add_edge("chatbot", END)


# ---------------------------------------------
# CHECKPOINTER
# ---------------------------------------------

memory = MemorySaver()

app = graph.compile(
    checkpointer=memory
)


# ---------------------------------------------
# THREAD ID
# ---------------------------------------------

config = {
    "configurable": {
        "thread_id": "user-1"
    }
}


result = app.invoke(
    {
        "message": "What is Agentic AI?",
        "response": ""
    },
    config
)

print(result["response"])