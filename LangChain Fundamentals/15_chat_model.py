import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    base_url = os.getenv("BASE_URL"),
    model = os.getenv("MODEL"),
    api_key = os.getenv("API_KEY"),
    temperature =os.getenv("TEMPERATURE")
)

response = llm.invoke("What is Generative AI?")

print(response.content)