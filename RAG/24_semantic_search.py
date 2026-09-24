from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

documents = [
    "To restart the TV, hold the power button.",
    "Open Settings and select Network.",
    "Connect the TV to your WiFi network.",
    "Adjust the television brightness from Picture Settings."
]

vector_store = Chroma.from_texts(
    documents,
    embedding=embeddings
)

results = vector_store.similarity_search(
    "How can I reboot my television?",
    k=2
)

for result in results:
    print(result.page_content)