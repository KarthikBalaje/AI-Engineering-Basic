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
    word_count: int
    final_answer: str


# ---------------------------------------------
# LLM NODE
# ---------------------------------------------

def explain(state: State):

    response = llm.invoke(
        f"Explain {state['topic']} in simple terms."
    )

    return {
        "explanation": response.content
    }


# ---------------------------------------------
# PYTHON NODE
# ---------------------------------------------

def count_words(state: State):

    count = len(state["explanation"].split())

    return {
        "word_count": count
    }


# ---------------------------------------------
# LLM NODE
# ---------------------------------------------

def final_response(state: State):

    response = llm.invoke(
        f"""
        Create a final answer about {state['topic']}.

        Explanation:
        {state['explanation']}

        Word count: {state['word_count']}
        """
    )

    return {
        "final_answer": response.content
    }


# ---------------------------------------------
# GRAPH
# ---------------------------------------------

graph = StateGraph(State)

graph.add_node("explain", explain)
graph.add_node("count_words", count_words)
graph.add_node("final_response", final_response)

graph.add_edge(START, "explain")
graph.add_edge("explain", "count_words")
graph.add_edge("count_words", "final_response")
graph.add_edge("final_response", END)

app = graph.compile()


result = app.invoke({
    "topic": "Agentic AI",
    "explanation": "",
    "word_count": 0,
    "final_answer": ""
})


print(result)