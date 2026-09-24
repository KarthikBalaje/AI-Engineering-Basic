import os

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI

from langchain_core.prompts import ChatPromptTemplate

from langchain_core.output_parsers import (
    StrOutputParser,
    JsonOutputParser,
    CommaSeparatedListOutputParser,
    PydanticOutputParser
)

from pydantic import BaseModel, Field


load_dotenv()


# --------------------------------------------------
# LLM
# --------------------------------------------------

llm = ChatOpenAI(
    base_url=os.getenv("BASE_URL"),
    model=os.getenv("MODEL"),
    api_key=os.getenv("API_KEY"),
    temperature=float(os.getenv("TEMPERATURE"))
)


topic = "Agentic AI"


# ==================================================
# 1. StrOutputParser
# ==================================================

prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in one sentence."
)

chain = prompt | llm | StrOutputParser()

response = chain.invoke({
    "topic": topic
})

print("\n1. StrOutputParser")
print(response)
print(type(response))


# ==================================================
# 2. JsonOutputParser
# ==================================================

prompt = ChatPromptTemplate.from_template(
    """
    Analyze {topic}.

    Return ONLY valid JSON:
    {{
        "topic": "...",
        "difficulty": "...",
        "score": 1
    }}
    """
)

chain = prompt | llm | JsonOutputParser()

response = chain.invoke({
    "topic": topic
})

print("\n2. JsonOutputParser")
print(response)
print(type(response))


# ==================================================
# 3. CommaSeparatedListOutputParser
# ==================================================

prompt = ChatPromptTemplate.from_template(
    """
    Give me 5 important concepts related to {topic}.
    Return them as a comma-separated list.
    """
)

chain = prompt | llm | CommaSeparatedListOutputParser()

response = chain.invoke({
    "topic": topic
})

print("\n3. CommaSeparatedListOutputParser")
print(response)
print(type(response))


# ==================================================
# 4. PydanticOutputParser
# ==================================================

class TopicAnalysis(BaseModel):

    topic: str = Field(
        description="The topic being analyzed"
    )

    difficulty: str = Field(
        description="Difficulty level of the topic"
    )

    score: int = Field(
        description="Score from 1 to 10"
    )


parser = PydanticOutputParser(
    pydantic_object=TopicAnalysis
)

prompt = ChatPromptTemplate.from_template(
    """
    Analyze {topic}.

    {format_instructions}
    """
)

chain = prompt | llm | parser

response = chain.invoke({
    "topic": topic,
    "format_instructions": parser.get_format_instructions()
})

print("\n4. PydanticOutputParser")
print(response)
print(type(response))

print("\nIndividual fields:")
print("Topic:", response.topic)
print("Difficulty:", response.difficulty)
print("Score:", response.score)