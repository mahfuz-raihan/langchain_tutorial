import os
from dotenv import load_dotenv
load_dotenv()
from huggingface_hub import login
login(os.getenv("HUGGINGFACEHUB_API_TOKEN"))
from langchain_huggingface import HuggingFaceEmbeddings

os.environ["HF_HOME"] = "C:/Users/BS01519/OneDrive - Brain Station 23/Desktop/rag_app/huggingface_cache"
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"},
    cache_folder="C:/Users/BS01519/OneDrive - Brain Station 23/Desktop/rag_app/huggingface_cache",
    encode_kwargs={"normalize_embeddings": False},
)
text = ["What is loss function in deep learning?", 
         "Explain the concept of overfitting in machine learning.",
         "What is the purpose of dropout in neural networks?"
         "How does the backpropagation algorithm work in training neural networks?"
         "What is the difference between supervised and unsupervised learning?"
         ]
embedding = embeddings.embed_documents(text)
print(str(embedding))
print("Length of the vector:", len(embedding))  # Should print the dimension of the embedding vector