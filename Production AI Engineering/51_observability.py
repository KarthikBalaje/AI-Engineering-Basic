import os, time
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    base_url=os.getenv("BASE_URL"),
    model=os.getenv("MODEL"),
    api_key=os.getenv("API_KEY"),
    temperature=0
)

start = time.time()

try:
    response = llm.invoke("Explain RAG in one sentence.")

    print("Answer:", response.content)
    print("Latency:", round(time.time() - start, 2), "sec")
    print("Usage:", response.usage_metadata)

except Exception as e:
    print("ERROR:", e)