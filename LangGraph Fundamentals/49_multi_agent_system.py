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
    temperature=0
)


class State(TypedDict):
    task: str
    research: str
    coding: str
    final_answer: str


# ---------------------------------------------
# RESEARCH AGENT
# ---------------------------------------------

def research_agent(state: State):

    response = llm.invoke(
        f"""
        You are a research specialist.

        Research and explain the important concepts
        needed to solve this task:

        {state['task']}
        """
    )

    return {
        "research": response.content
    }


# ---------------------------------------------
# CODING AGENT
# ---------------------------------------------

def coding_agent(state: State):

    response = llm.invoke(
        f"""
        You are a Python coding specialist.

        Based on this research:

        {state['research']}

        Create a Python implementation for:

        {state['task']}
        """
    )

    return {
        "coding": response.content
    }


# ---------------------------------------------
# SUPERVISOR / FINAL AGENT
# ---------------------------------------------

def supervisor(state: State):

    response = llm.invoke(
        f"""
        You are the senior AI engineer.

        Task:
        {state['task']}

        Research:
        {state['research']}

        Proposed implementation:
        {state['coding']}

        Produce the final answer.
        """
    )

    return {
        "final_answer": response.content
    }


# ---------------------------------------------
# GRAPH
# ---------------------------------------------

graph = StateGraph(State)

graph.add_node("research_agent", research_agent)
graph.add_node("coding_agent", coding_agent)
graph.add_node("supervisor", supervisor)

graph.add_edge(START, "research_agent")
graph.add_edge("research_agent", "coding_agent")
graph.add_edge("coding_agent", "supervisor")
graph.add_edge("supervisor", END)

app = graph.compile()


result = app.invoke({
    "task": "Build a RAG application in Python.",
    "research": "",
    "coding": "",
    "final_answer": ""
})


print(result["final_answer"])