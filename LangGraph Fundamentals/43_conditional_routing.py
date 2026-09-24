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
    question: str
    category: str
    answer: str


# ---------------------------------------------
# CLASSIFIER
# ---------------------------------------------

def classify(state: State):

    response = llm.invoke(
        f"""
        Classify this question as either:

        technical
        general

        Question:
        {state['question']}

        Return only one word.
        """
    )

    return {
        "category": response.content.strip().lower()
    }


# ---------------------------------------------
# ROUTER
# ---------------------------------------------

def route_question(state: State):

    if "technical" in state["category"]:
        return "technical"

    return "general"


# ---------------------------------------------
# TECHNICAL NODE
# ---------------------------------------------

def technical_answer(state: State):

    response = llm.invoke(
        f"Give a technical answer to:\n{state['question']}"
    )

    return {
        "answer": response.content
    }


# ---------------------------------------------
# GENERAL NODE
# ---------------------------------------------

def general_answer(state: State):

    response = llm.invoke(
        f"Explain this for a beginner:\n{state['question']}"
    )

    return {
        "answer": response.content
    }


# ---------------------------------------------
# GRAPH
# ---------------------------------------------

graph = StateGraph(State)

graph.add_node("classify", classify)
graph.add_node("technical", technical_answer)
graph.add_node("general", general_answer)

graph.add_edge(START, "classify")

graph.add_conditional_edges(
    "classify",
    route_question,
    {
        "technical": "technical",
        "general": "general"
    }
)

graph.add_edge("technical", END)
graph.add_edge("general", END)

app = graph.compile()


result = app.invoke({
    "question": "How does vector search work?",
    "category": "",
    "answer": ""
})


print(result["answer"])