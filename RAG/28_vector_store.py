from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# Embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Sample documents
documents = [
    "To restart the TV, hold the power button for five seconds.",
    "Open Settings and select Network to configure WiFi.",
    "You can adjust brightness from Picture Settings.",
    "Bluetooth devices can be paired from the Bluetooth menu."
]

# Create vector store
vector_store = Chroma.from_texts(
    documents,
    embedding=embeddings,
    collection_name="tv_manual"
)

# Search
results = vector_store.similarity_search(
    "How do I reboot my television?",
    k=2
)

for i, document in enumerate(results, start=1):
    print(f"\nResult {i}:")
    print(document.page_content)