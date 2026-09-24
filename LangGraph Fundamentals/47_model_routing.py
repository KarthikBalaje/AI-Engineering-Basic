import os

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI

from langgraph.graph import StateGraph, START, END

from typing import TypedDict


load_dotenv()


# ---------------------------------------------
# TWO MODELS
# ---------------------------------------------

fast_llm = ChatOpenAI(
    base_url=os.getenv("BASE_URL"),
    model="openai/gpt-5.4-mini",
    api_key=os.getenv("API_KEY"),
    temperature=0
)


powerful_llm = ChatOpenAI(
    base_url=os.getenv("BASE_URL"),
    model="openai/gpt-5.4",
    api_key=os.getenv("API_KEY"),
    temperature=0
)


class State(TypedDict):
    question: str
    model: str
    answer: str


def route(state: State):

    response = fast_llm.invoke(
        f"""
        Classify this question:

        SIMPLE
        COMPLEX

        Question:
        {state['question']}

        Return only SIMPLE or COMPLEX.
        """
    )

    return {
        "model": response.content.strip().upper()
    }


def choose_model(state: State):
    print(state["model"])
    if state["model"] == "COMPLEX":
        response = powerful_llm.invoke(
            state["question"]
        )
    else:
        response = fast_llm.invoke(
            state["question"]
        )

    return {
        "answer": response.content
    }


graph = StateGraph(State)

graph.add_node("route", route)
graph.add_node("choose_model", choose_model)

graph.add_edge(START, "route")
graph.add_edge("route", "choose_model")
graph.add_edge("choose_model", END)

app = graph.compile()


result = app.invoke({
    "question": "How Hallucination can be avoided in RAG ? Explain this complex question in detail",
    "model": "",
    "answer": ""
})


print(result["answer"])