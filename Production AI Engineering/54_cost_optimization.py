# 54_cost.py
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

models = {
    "cheap": os.getenv("CHEAP_MODEL", os.getenv("MODEL")),
    "powerful": os.getenv("MODEL")
}

cache = {}

def ask(question, complex=False):

    # Cache → avoid repeated LLM calls
    if question in cache:
        return cache[question]

    # Model routing
    model = models["powerful"] if complex else models["cheap"]

    llm = ChatOpenAI(
        base_url=os.getenv("BASE_URL"),
        model=model,
        api_key=os.getenv("API_KEY"),
        temperature=0,
        max_tokens=150
    )

    # Context/prompt reduction
    prompt = f"Answer briefly:\n{question}"

    response = llm.invoke(prompt)

    cache[question] = response.content

    print("Usage:", response.usage_metadata)

    return response.content


print(ask("What is RAG?"))
print(ask("What is RAG?"))       # cached
print(ask("Design a RAG architecture.", complex=True))