import os
from dotenv import load_dotenv
load_dotenv()
from huggingface_hub import login
login(os.getenv("HUGGINGFACEHUB_API_TOKEN"))
from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


query = input("Enter your question: ")
# print("Question was >>", query)
text = ["What is loss function in deep learning?", 
         "Explain the concept of overfitting in machine learning.",
         "What is the purpose of dropout in neural networks?",
         "How does the backpropagation algorithm work in training neural networks?",
         "What is the difference between supervised and unsupervised learning?"
         ]
# print the documents one by one in next line
# for i in range(len(text)):
#     print(f"Q {i+1}:", text[i])


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"},
    cache_folder="C:/Users/BS01519/OneDrive - Brain Station 23/Desktop/rag_app/huggingface_cache",
    encode_kwargs={"normalize_embeddings": False},
)



doc_embedding = embeddings.embed_documents(text)
query_embedding = embeddings.embed_query(query)

cosine_sim = cosine_similarity([query_embedding], doc_embedding)[0]

index, score = sorted(list(enumerate(cosine_sim)), key=lambda x: x[1])[-1]

print("Then answer is >>", text[index])