from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

query = "How do I restart my TV?"

documents = [
    "How can I reboot my television?",
    "How do I connect my TV to WiFi?",
    "What is the best recipe for chicken biryani?"
]

query_vector = embeddings.embed_query(query)

document_vectors = embeddings.embed_documents(documents)

scores = cosine_similarity(
    [query_vector],
    document_vectors
)[0]

for document, score in zip(documents, scores):
    print(f"{score:.4f} -> {document}")