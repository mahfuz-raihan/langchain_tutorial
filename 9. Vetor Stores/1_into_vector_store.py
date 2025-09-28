import os
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceInferenceAPIEmbeddings
from langchain.docstore.document import Document

# --- Configuration ---
# It's best practice to set your token as an environment variable.
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "hf_YOUR_TOKEN_HERE"

# --- Our Sample Data ---
texts = [
    "The cat sat on the mat.",
    "The dog chased the ball.",
    "Apples are a type of fruit.",
    "Cars are a form of transportation.",
    "Paris is the capital of France."
]

# --- Create LangChain Document Objects ---
documents = [Document(page_content=t) for t in texts]

# --- The Core Components (Using HF Inference API) ---
# 1. The Embedding Model: We point to a model on the Hugging Face Hub
#    and provide our API token to use it.
model_name = "sentence-transformers/all-MiniLM-L6-v2"
embeddings = HuggingFaceInferenceAPIEmbeddings(
    api_key=os.environ["HUGGINGFACEHUB_API_TOKEN"],
    model_name=model_name
)

# 2. The Vector Store: FAISS works exactly the same way.
#    Instead of running a local model, LangChain will now call the HF API
#    to get vectors for each document.
print("Creating the vector store using the Hugging Face API...")
vector_store = FAISS.from_documents(documents, embeddings)
print("Vector store created successfully! ✨")


# --- Let's Ask a Question! ---
query = "What is a feline's favorite spot?"

# --- Perform the Search ---
# the query is also sent to the HF API to be converted into a vector.
print(f"\nSearching for documents similar to: '{query}'")
results = vector_store.similarity_search(query, k=1)

# --- Display the Result ---
print("\n--- Top Result ---")
if results:
    print(f"Document: '{results[0].page_content}'")
else:
    print("No relevant documents found.")