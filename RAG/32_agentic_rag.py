import os

from typing import TypedDict

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from langgraph.graph import StateGraph, START, END


load_dotenv()


# --------------------------------------------------
# LLM
# --------------------------------------------------

llm = ChatOpenAI(
    base_url=os.getenv("BASE_URL"),
    model=os.getenv("MODEL"),
    api_key=os.getenv("API_KEY"),
    temperature=0
)


# --------------------------------------------------
# Embeddings
# --------------------------------------------------

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# --------------------------------------------------
# Vector Store
# --------------------------------------------------

documents = [
    "To restart the TV, hold the power button for five seconds.",
    "Open Settings and select Network to configure WiFi.",
    "You can adjust brightness from Picture Settings.",
    "Bluetooth devices can be paired from the Bluetooth menu."
]

vector_store = Chroma.from_texts(
    documents,
    embedding=embeddings,
    collection_name="agentic_rag_demo"
)

retriever = vector_store.as_retriever(
    search_kwargs={"k": 2}
)


# --------------------------------------------------
# State
# --------------------------------------------------

class State(TypedDict):
    question: str
    need_retrieval: bool
    context: str
    answer: str


# --------------------------------------------------
# Decide
# --------------------------------------------------

def decide(state: State):

    question = state["question"]

    response = llm.invoke(
        f"""
Decide whether this question requires
retrieving information from the knowledge base.

Question:
{question}

Return ONLY:
YES
or
NO
"""
    )

    decision = response.content.strip().upper()

    return {
        "need_retrieval": decision == "YES"
    }


# --------------------------------------------------
# Retrieve
# --------------------------------------------------

def retrieve(state: State):

    documents = retriever.invoke(
        state["question"]
    )

    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    return {
        "context": context
    }


# --------------------------------------------------
# Answer
# --------------------------------------------------

def answer(state: State):

    if state["need_retrieval"]:

        response = llm.invoke(
            f"""
Answer using ONLY the context below.

Context:
{state["context"]}

Question:
{state["question"]}
"""
        )

    else:

        response = llm.invoke(
            state["question"]
        )

    return {
        "answer": response.content
    }


# --------------------------------------------------
# Routing
# --------------------------------------------------

def route(state: State):

    if state["need_retrieval"]:
        return "retrieve"

    return "answer"


# --------------------------------------------------
# Build Graph
# --------------------------------------------------

graph = StateGraph(State)

graph.add_node("decide", decide)
graph.add_node("retrieve", retrieve)
graph.add_node("answer", answer)

graph.add_edge(START, "decide")

graph.add_conditional_edges(
    "decide",
    route,
    {
        "retrieve": "retrieve",
        "answer": "answer"
    }
)

graph.add_edge("retrieve", "answer")

graph.add_edge("answer", END)


# --------------------------------------------------
# Compile
# --------------------------------------------------

app = graph.compile()


# --------------------------------------------------
# Run
# --------------------------------------------------

result = app.invoke({
    "question": "How do I restart the TV?",
    "need_retrieval": True,
    "context": "",
    "answer": ""
})


print("\nAnswer:")
print(result["answer"])