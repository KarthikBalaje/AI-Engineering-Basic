import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

llm = ChatOpenAI(
    base_url=os.getenv("BASE_URL"),
    model=os.getenv("MODEL"),
    api_key=os.getenv("API_KEY"),
    temperature=float(os.getenv("TEMPERATURE"))
)

messages = [
    SystemMessage(content="You are a helpful AI teacher."),
    HumanMessage(content="Explain Generative AI in simple terms.")
]

response = llm.invoke(messages)

print(response.content)