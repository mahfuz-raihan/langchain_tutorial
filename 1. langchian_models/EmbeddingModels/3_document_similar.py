import os
from dotenv import load_dotenv
load_dotenv()
from huggingface_hub import login
login(os.getenv("HUGGINGFACEHUB_API_TOKEN"))
from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


query = input("User: ")
# print("Question was >>", query)
text = ["Nazmussakib is a good person working in NRBC bank in Motijheel, Dhaka.", 
         "Mahfuz working in a Software company in Dhaka named Brain Station 23.",
         "Nishan is a good friend of Tusher and Mahfuz.\n Now he working in a FMCG company named Pran-RFL,\nalso a bokacoda lover boy olo",
         "Tipu working as a IoT engineer now and he has a nice workshop named IoT Bhai.\n and CEO of One Dish party.",
         "Oh, the SEO man Tusher working on a project in Vivasoft Bangladesh.\nAnd also an SEO expert.\n"
         "Tusher Mahmood is a good friend of Mahfuz. But not a departmental friend.",
         "Tamal the CEO of Chapin Group of Industries and IELTS KIT. He's known as faportbaz in his friend circle",
         "Sadik the friend of 'Bikas', ei biskash tui ja, ami dekhsi...."
         ]



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




print("Agent:", text[index])