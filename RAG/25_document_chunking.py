from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("CFI-21XX_PS5_Instruction_Manual_Web$en-in.pdf")

documents = loader.load()

print("Pages:", len(documents))

print(documents[0].page_content)
print(documents[0].metadata)

from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.split_documents(documents)

print("Pages:", len(documents))
print("Chunks:", len(chunks))