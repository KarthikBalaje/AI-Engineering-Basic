import os

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

# --------------------------------------------------
# 1. LLM
# --------------------------------------------------

llm = ChatOpenAI(
    base_url=os.getenv("BASE_URL"),
    model=os.getenv("MODEL"),
    api_key=os.getenv("API_KEY"),
    temperature=float(os.getenv("TEMPERATURE"))
)


# --------------------------------------------------
# 2. Embeddings
# --------------------------------------------------

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# --------------------------------------------------
# 3. Documents
# --------------------------------------------------

documents = [
    "To restart the TV, hold the power button for five seconds.",
    "Open Settings and select Network to configure WiFi.",
    "You can adjust brightness from Picture Settings.",
    "Bluetooth devices can be paired from the Bluetooth menu."
]


# --------------------------------------------------
# 4. Vector Store
# --------------------------------------------------

vector_store = Chroma.from_texts(
    documents,
    embedding=embeddings,
    collection_name="tv_manual_rag"
)


# --------------------------------------------------
# 5. Retriever
# --------------------------------------------------

retriever = vector_store.as_retriever(
    search_kwargs={"k": 2}
)


# --------------------------------------------------
# 6. Prompt
# --------------------------------------------------

prompt = ChatPromptTemplate.from_template(
    """
You are a helpful technical support assistant.

Answer the question using ONLY the provided context.

Context:
{context}

Question:
{question}

If the answer cannot be found in the context,
say:

"I don't have enough information in the provided documents."
"""
)


# --------------------------------------------------
# 7. RAG Chain
# --------------------------------------------------

chain = prompt | llm | StrOutputParser()


# --------------------------------------------------
# 8. User Question
# --------------------------------------------------

question = "How do I restart the TV?"


# --------------------------------------------------
# 9. Retrieve
# --------------------------------------------------

retrieved_documents = retriever.invoke(question)


# --------------------------------------------------
# 10. Build Context
# --------------------------------------------------

context = "\n\n".join(
    document.page_content
    for document in retrieved_documents
)


# --------------------------------------------------
# 11. Generate Answer
# --------------------------------------------------

answer = chain.invoke({
    "context": context,
    "question": question
})


print("\nAnswer:")
print(answer)