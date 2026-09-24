import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

llm = ChatOpenAI(
    base_url=os.getenv("BASE_URL"),
    model=os.getenv("MODEL"),
    api_key=os.getenv("API_KEY"),
    temperature=float(os.getenv("TEMPERATURE"))
)

parser = StrOutputParser()

explain_prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple terms."
)

interview_prompt = ChatPromptTemplate.from_template(
    "Give me one interview question about {topic}."
)

explain_chain = explain_prompt | llm | parser

interview_chain = interview_prompt | llm | parser

parallel_chain = RunnableParallel(
    explanation=explain_chain,
    interview_question=interview_chain
)

result = parallel_chain.invoke({
    "topic": "RAG"
})

print("Explanation:")
print(result["explanation"])

print("\nInterview Question:")
print(result["interview_question"])