import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from langgraph.graph import StateGraph, START, END

from langgraph.checkpoint.memory import MemorySaver

from langgraph.types import interrupt, Command

from typing import TypedDict


load_dotenv()


llm = ChatOpenAI(
    base_url=os.getenv("BASE_URL"),
    model=os.getenv("MODEL"),
    api_key=os.getenv("API_KEY"),
    temperature=float(os.getenv("TEMPERATURE"))
)


class State(TypedDict):
    request: str
    approval: str
    result: str


def prepare_action(state: State):

    response = llm.invoke(
        f"Prepare an action for this request:\n{state['request']}"
    )

    return {
        "result": response.content
    }


def human_approval(state: State):

    approval = interrupt(
        {
            "message": "Please approve this action.",
            "action": state["result"]
        }
    )

    return {
        "approval": str(approval)
    }


def execute_action(state: State):

    if state["approval"].lower() == "yes":
        return {
            "result": "Action approved and executed."
        }

    return {
        "result": "Action rejected."
    }


graph = StateGraph(State)

graph.add_node("prepare", prepare_action)
graph.add_node("approval", human_approval)
graph.add_node("execute", execute_action)

graph.add_edge(START, "prepare")
graph.add_edge("prepare", "approval")
graph.add_edge("approval", "execute")
graph.add_edge("execute", END)

memory = MemorySaver()

app = graph.compile(
    checkpointer=memory
)


config = {
    "configurable": {
        "thread_id": "approval-1"
    }
}


# First execution pauses at human approval
result = app.invoke(
    {
        "request": "Send an email to the customer.",
        "approval": "",
        "result": ""
    },
    config
)

print(result)

human_input = input(
    "\nEnter your decision (yes/no): "
).strip().lower()



# Resume after human decision
result = app.invoke(
    Command(resume=human_input),
    config
)

print(result)