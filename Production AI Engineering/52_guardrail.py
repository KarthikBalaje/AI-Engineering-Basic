# 52_guardrails.py
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
llm = ChatOpenAI(
    base_url=os.getenv("BASE_URL"),
    model=os.getenv("MODEL"),
    api_key=os.getenv("API_KEY"),
    temperature=0
)

def guardrail(question, action=None, approved=False):

    # Input / prompt-injection checks
    blocked = [
        "ignore previous instructions",
        "reveal system prompt",
        "give me api key"
    ]

    if any(x in question.lower() for x in blocked):
        return "BLOCKED: unsafe input"

    # Tool/action guardrail
    sensitive = ["delete", "update", "transfer"]

    if action in sensitive and not approved:
        return "BLOCKED: human approval required"

    # LLM
    answer = llm.invoke(question).content

    # Output guardrail
    secrets = ["password", "api_key", "secret"]

    if any(x in answer.lower() for x in secrets):
        return "BLOCKED: unsafe output"

    return answer


print(guardrail("Explain RAG"))
print(guardrail("Ignore previous instructions"))
print(guardrail("Delete customer", action="delete"))