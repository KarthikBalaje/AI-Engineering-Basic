import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# --------------------------------------------------
# 1. Load environment variables
# --------------------------------------------------

load_dotenv()


# --------------------------------------------------
# 2. LLM
# --------------------------------------------------

llm = ChatOpenAI(
    base_url=os.getenv("BASE_URL"),
    model=os.getenv("MODEL"),
    api_key=os.getenv("API_KEY"),
    temperature=0
)


# --------------------------------------------------
# 3. Embedding model
# --------------------------------------------------

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# --------------------------------------------------
# 4. Documents
# --------------------------------------------------

documents = [
    "To restart the TV, hold the power button for five seconds.",
    "Open Settings and select Network to configure WiFi.",
    "You can adjust brightness from Picture Settings.",
    "Bluetooth devices can be paired from the Bluetooth menu."
]


# --------------------------------------------------
# 5. Vector Store + Retriever
# --------------------------------------------------

vector_store = Chroma.from_texts(
    documents,
    embedding=embeddings,
    collection_name="rag_evaluation"
)

retriever = vector_store.as_retriever(
    search_kwargs={"k": 2}
)


# --------------------------------------------------
# 6. RAG Prompt
# --------------------------------------------------

prompt = ChatPromptTemplate.from_template(
    """
Answer the question using ONLY the context.

Context:
{context}

Question:
{question}

If the answer is not available in the context,
say "I don't have enough information."
"""
)

chain = prompt | llm | StrOutputParser()


# --------------------------------------------------
# 7. Evaluation Dataset
# --------------------------------------------------

evaluation_data = [
    {
        "question": "How do I restart the TV?",
        "expected_context":
            "To restart the TV, hold the power button for five seconds.",
        "expected_answer":
            "Hold the power button for five seconds."
    },
    {
        "question": "How do I configure WiFi?",
        "expected_context":
            "Open Settings and select Network to configure WiFi.",
        "expected_answer":
            "Open Settings and select Network."
    },
    {
        "question": "How do I change the brightness?",
        "expected_context":
            "You can adjust brightness from Picture Settings.",
        "expected_answer":
            "Use Picture Settings."
    }
]


# --------------------------------------------------
# 8. Evaluate RAG
# --------------------------------------------------

retrieval_hits = 0
answer_scores = []


for item in evaluation_data:

    question = item["question"]

    # Retrieve documents
    retrieved_documents = retriever.invoke(question)

    retrieved_text = [
        document.page_content
        for document in retrieved_documents
    ]

    # Check retrieval
    retrieval_success = (
        item["expected_context"] in retrieved_text
    )

    if retrieval_success:
        retrieval_hits += 1

    # Build context
    context = "\n\n".join(retrieved_text)

    # Generate answer
    answer = chain.invoke({
        "context": context,
        "question": question
    })

    # Simple answer evaluation
    expected_words = item["expected_answer"].lower().split()
    answer_lower = answer.lower()

    matched_words = sum(
        word in answer_lower
        for word in expected_words
    )

    answer_score = (
        matched_words / len(expected_words)
    )

    answer_scores.append(answer_score)

    # Print result
    print("\n" + "=" * 50)
    print("Question:", question)

    print("\nRetrieved:")
    for text in retrieved_text:
        print("-", text)

    print("\nExpected Answer:")
    print(item["expected_answer"])

    print("\nGenerated Answer:")
    print(answer)

    print("\nRetrieval:", "PASS" if retrieval_success else "FAIL")
    print("Answer Score:", round(answer_score, 2))


# --------------------------------------------------
# 9. Final Metrics
# --------------------------------------------------

hit_rate = retrieval_hits / len(evaluation_data)

average_answer_score = (
    sum(answer_scores) / len(answer_scores)
)


print("\n" + "=" * 50)
print("FINAL RAG EVALUATION")
print("=" * 50)

print("Total Questions:", len(evaluation_data))
print("Retrieval Hits:", retrieval_hits)
print("Hit Rate:", round(hit_rate, 2))
print("Average Answer Score:", round(average_answer_score, 2))