from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document

# Step 1: Our scource docuemnts
documents = [
    Document(page_content="LLMAindex helps developers to build LLM application easily."),
    Document(page_content="Chroma is a vector database optimized for LLM-based search."),
    Document(page_content="Embedding convert text into high-dimentional vectors."),
    Document(page_content="OpenAI/HuggingFace provide powerful embedding models")
]

# Step 2: initialize embedding model 
embedding_model = OpenAIEmbeddings()

# Step 3: Create Chroma DB for vector store in memory
vectorstore = Chroma.from_documents(
    documents=documents,
    embedding=embedding_model,
    collection_name="first_collection"
)

retrivers = vectorstore.as_retriever(search_kwargs={"k": 2})

query = "What is the Chroma used for?"
results = retrivers.invoke(query)


for i, doc in enumerate(results):
    print(f" --- Result {i+1} ---")
    print(f"{doc.page_content}")