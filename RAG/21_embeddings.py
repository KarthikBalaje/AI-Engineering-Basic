from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

text = "RAG retrieves information from documents."

vector = embeddings.embed_query(text)

print(vector)
print(type(vector))
print("Dimensions:", len(vector))