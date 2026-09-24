from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

documents = [
    "To restart the TV, hold the power button for five seconds.",
    "Open Settings and select Network to configure WiFi.",
    "You can adjust brightness from Picture Settings.",
    "Bluetooth devices can be paired from the Bluetooth menu."
]

vector_store = Chroma.from_texts(
    documents,
    embedding=embeddings,
    collection_name="tv_manual"
)

# Convert vector store into a retriever
retriever = vector_store.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 2,
        "fetch_k": 10
    }
)

# Invoke retriever
results = retriever.invoke(
    "How can I reboot my TV?"
)

for document in results:
    print(document.page_content)