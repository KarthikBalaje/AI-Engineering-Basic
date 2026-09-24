import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


llm = ChatOpenAI(
    base_url=os.getenv("BASE_URL"),
    model=os.getenv("MODEL"),
    api_key=os.getenv("API_KEY"),
    temperature=0
)


prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in one sentence."
)


chain = (
    prompt
    | llm
    | StrOutputParser()
)


result = chain.invoke(
    {
        "topic": "RAG"
    }
)


print("Chain result:")
print(result)