import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatOpenAI(
    base_url=os.getenv("BASE_URL"),
    model=os.getenv("MODEL"),
    api_key=os.getenv("API_KEY"),
    temperature=float(os.getenv("TEMPERATURE"))
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI teacher."),
    ("human", "Explain {topic} in simple terms.")
])

chain = prompt | llm

response = chain.invoke({
    "topic": "Embeddings"
})

print(response.content)