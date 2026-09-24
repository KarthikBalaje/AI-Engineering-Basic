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
    temperature=float(os.getenv("TEMPERATURE"))
)

explain_prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple terms."
)

summarize_prompt = ChatPromptTemplate.from_template(
    "Summarize the following explanation in one sentence:\n\n{text}"
)

parser = StrOutputParser()

explain_chain = explain_prompt | llm | parser

summarize_chain = summarize_prompt | llm | parser

explanation = explain_chain.invoke({
    "topic": "RAG"
})

summary = summarize_chain.invoke({
    "text": explanation
})

print("Explanation:")
print(explanation)

print("\nSummary:")
print(summary)