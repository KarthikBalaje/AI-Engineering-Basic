import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from langgraph.graph import StateGraph, START, END

from typing import TypedDict


load_dotenv()


# ==================================================
# LLM
# ==================================================

llm = ChatOpenAI(
    base_url=os.getenv("BASE_URL"),
    model=os.getenv("MODEL"),
    api_key=os.getenv("API_KEY"),
    temperature=float(os.getenv("TEMPERATURE"))
)


# ==================================================
# STATE
# ==================================================

class State(TypedDict):
    topic: str
    explanation: str
    summary: str


# ==================================================
# NODE 1
# ==================================================

def explain_topic(state: State):

    response = llm.invoke(
        f"Explain {state['topic']} in simple terms."
    )

    return {
        "explanation": response.content
    }


# ==================================================
# NODE 2
# ==================================================

def summarize_topic(state: State):

    response = llm.invoke(
        f"Summarize this explanation in one sentence:\n\n"
        f"{state['explanation']}"
    )

    return {
        "summary": response.content
    }


# ==================================================
# GRAPH
# ==================================================

graph = StateGraph(State)

graph.add_node("explain", explain_topic)
graph.add_node("summarize", summarize_topic)

graph.add_edge(START, "explain")
graph.add_edge("explain", "summarize")
graph.add_edge("summarize", END)

app = graph.compile()


# ==================================================
# RUN
# ==================================================

result = app.invoke({
    "topic": "Agentic AI",
    "explanation": "",
    "summary": ""
})


print("Topic:", result["topic"])
print("\nExplanation:", result["explanation"])
print("\nSummary:", result["summary"])