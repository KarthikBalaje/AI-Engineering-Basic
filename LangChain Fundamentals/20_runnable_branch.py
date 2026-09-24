import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch

load_dotenv()

llm = ChatOpenAI(
    base_url=os.getenv("BASE_URL"),
    model=os.getenv("MODEL"),
    api_key=os.getenv("API_KEY"),
    temperature=float(os.getenv("TEMPERATURE"))
)

parser = StrOutputParser()

explain_prompt = ChatPromptTemplate.from_template(
    "Explain this concept in simple terms:\n\n{question}"
)

interview_prompt = ChatPromptTemplate.from_template(
    "Answer this interview-related question:\n\n{question}"
)

explain_chain = explain_prompt | llm | parser

interview_chain = interview_prompt | llm | parser

branch = RunnableBranch(
    (
        lambda x: "interview" in x["question"].lower(),
        interview_chain
    ),
    explain_chain
)

# result = branch.invoke({
#     "question": "What is Inference in LLM?"
# })

result = branch.invoke({
    "question": "Give me an interview question about RAG."
})

print(result)