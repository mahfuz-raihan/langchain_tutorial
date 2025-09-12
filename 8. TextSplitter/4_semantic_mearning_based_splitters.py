import os
from huggingface_hub import login
from langchain_experimental.text_splitter import SemanticChunker
# We replace the OpenAIEmbeddings with HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
load_dotenv(override=True)
login(os.getenv("HUGGINGFACEHUB_API_TOKEN"))
print("Login successfully complete.........")


# --- 1. Set up the Hugging Face Embeddings ---
# We'll use a popular, lightweight model
model_name = "sentence-transformers/all-MiniLM-L6-v2"
model_kwargs = {'device': 'cpu'} # Use 'cuda' for GPU
embeddings = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs
)

# --- 2. Initialize the Semantic Chunker ---
# The text splitter now uses the local Hugging Face model
text_splitter = SemanticChunker(
    embeddings, breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=3
)

# --- 3. Run the chunker on your text ---
sample = """
Farmers were working hard in the fields, preparing the soil and planting seeds for the next season. The sun was bright, and the air smelled of earth and fresh grass. The Indian Premier League (IPL) is the biggest cricket league in the world. People all over the world watch the matches and cheer for their favourite teams.


Terrorism is a big danger to peace and safety. It causes harm to people and creates fear in cities and villages. When such attacks happen, they leave behind pain and sadness. To fight terrorism, we need strong laws, alert security forces, and support from people who care about peace and safety.
"""

docs = text_splitter.create_documents([sample])

# --- 4. Print the results ---
print(len(docs))
# The output will be a list of LangChain 'Document' objects
print(docs[0].page_content)