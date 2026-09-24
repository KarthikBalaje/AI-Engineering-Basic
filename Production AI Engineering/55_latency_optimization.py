# 55_latency.py
import os, asyncio, time
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    base_url=os.getenv("BASE_URL"),
    model=os.getenv("MODEL"),
    api_key=os.getenv("API_KEY"),
    temperature=0
)

# Parallel independent calls
async def ask(q):
    return await llm.ainvoke(q)

async def main():
    start = time.time()

    results = await asyncio.gather(
        ask("Give 3 RAG keywords."),
        ask("Give 3 Agent keywords.")
    )

    print([r.content for r in results])
    print("Parallel latency:", round(time.time()-start, 2))

asyncio.run(main())

# Streaming → first tokens arrive before completion
for chunk in llm.stream("Explain RAG briefly."):
    print(chunk.content, end="", flush=True)