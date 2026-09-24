import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from langgraph.graph import StateGraph, START, END

from typing import TypedDict


load_dotenv()


llm = ChatOpenAI(
    base_url=os.getenv("BASE_URL"),
    model=os.getenv("MODEL"),
    api_key=os.getenv("API_KEY"),
    temperature=float(os.getenv("TEMPERATURE"))
)


class State(TypedDict):
    topic: str
    explanation: str
    summary: str


def explain(state: State):

    response = llm.invoke(
        f"Explain {state['topic']}."
    )

    return {
        "explanation": response.content
    }


def summarize(state: State):

    response = llm.invoke(
        f"Summarize:\n{state['explanation']}"
    )

    return {
        "summary": response.content
    }


graph = StateGraph(State)

graph.add_node("explain", explain)
graph.add_node("summarize", summarize)

# START → explain
graph.add_edge(START, "explain")

# explain → summarize
graph.add_edge("explain", "summarize")

# summarize → END
graph.add_edge("summarize", END)

app = graph.compile()


result = app.invoke({
    "topic": "Agentic AI",
    "explanation": "",
    "summary": ""
})


print(result["summary"])