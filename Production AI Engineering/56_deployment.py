import os, logging
from fastapi import FastAPI
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
logging.basicConfig(level=logging.INFO)

app = FastAPI()

llm = ChatOpenAI(
    base_url=os.getenv("BASE_URL"),
    model=os.getenv("MODEL"),
    api_key=os.getenv("API_KEY"),
    temperature=0
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/ask")
def ask(question: str):
    logging.info("request received")
    r = llm.invoke(question)
    return {"answer": r.content}