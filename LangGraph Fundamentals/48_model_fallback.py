import os

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI

from langgraph.graph import StateGraph, START, END

from typing import TypedDict


load_dotenv()


primary_llm = ChatOpenAI(
    base_url=os.getenv("BASE_URL"),
    model="openai/gpt-5-mini",
    api_key=os.getenv("API_KEY"),
    temperature=0
)


backup_llm = ChatOpenAI(
    base_url=os.getenv("BASE_URL"),
    model="openai/gpt-5",
    api_key=os.getenv("API_KEY"),
    temperature=0
)


class State(TypedDict):
    question: str
    answer: str


def answer(state: State):

    try:

        response = primary_llm.invoke123(
            state["question"]
        )

    except Exception:

        print("Primary model failed. Using backup model.")

        response = backup_llm.invoke(
            state["question"]
        )

    return {
        "answer": response.content
    }


graph = StateGraph(State)

graph.add_node("answer", answer)

graph.add_edge(START, "answer")
graph.add_edge("answer", END)

app = graph.compile()


result = app.invoke({
    "question": "Explain Agentic AI.",
    "answer": ""
})


print(result["answer"])