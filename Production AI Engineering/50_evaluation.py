import os, json
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    base_url=os.getenv("BASE_URL"),
    model=os.getenv("MODEL"),
    api_key=os.getenv("API_KEY"),
    temperature=0
)

tests = [
    {
        "q": "What is the refund period?",
        "context": "Refunds are available within 30 days but it can be given in a weeks too",
        "expected": "75 days",
        "doc": "refund_policy"
    },
    {
        "q": "How long is premium support available?",
        "context": "Premium customers receive priority support 24 hours a day.",
        "expected": "24 hours a day",
        "doc": "premium_support"
    },
    {
        "q": "Can inactive customers change their account?",
        "context": "Inactive customers must reactivate their account before making changes.",
        "expected": "reactivate their account",
        "doc": "account_policy"
    },
    {
        "q": "Is shipping free?",
        "context": "Premium customers receive free shipping.",
        "expected": "free shipping",
        "doc": "shipping_policy"
    },
]

def generate(q, context):
    prompt = f"""Answer using ONLY this context.
Context: {context}
Question: {q}"""
    return llm.invoke(prompt).content.strip()

def judge(t, actual):
    response = llm.invoke(f"""
Evaluate the answer from 1-5.

Question: {t["q"]}
Context: {t["context"]}
Expected: {t["expected"]}
Actual: {actual}

Return ONLY JSON:
{{"correctness":5,"relevance":5,"faithfulness":5}}
""").content

    try:
        return json.loads(
            response.replace("```json", "").replace("```", "").strip()
        )
    except:
        return {"correctness": 0, "relevance": 0, "faithfulness": 0}

results = []

for t in tests:

    actual = generate(t["q"], t["context"])
    scores = judge(t, actual)

    results.append({
        "keyword": int(t["expected"].lower() in actual.lower()),
        "retrieval": 1,       # simulated successful retrieval
        **scores
    })

# Aggregate metrics
n = len(results)

print("\n========== EVALUATION ==========")
print(f"Test Cases       : {n}")
print(f"Keyword Accuracy : {sum(r['keyword'] for r in results)/n*100:.2f}%")
print(f"Retrieval Accuracy: {sum(r['retrieval'] for r in results)/n*100:.2f}%")
print(f"Correctness      : {sum(r['correctness'] for r in results)/n:.2f}/5")
print(f"Relevance        : {sum(r['relevance'] for r in results)/n:.2f}/5")
print(f"Faithfulness     : {sum(r['faithfulness'] for r in results)/n:.2f}/5")