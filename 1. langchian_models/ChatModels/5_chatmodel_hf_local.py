import os
from dotenv import load_dotenv
load_dotenv()
from huggingface_hub import login
login(os.getenv("HUGGINGFACEHUB_API_TOKEN"))
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

os.environ["HF_HOME"] = "C:/Users/BS01519/OneDrive - Brain Station 23/Desktop/rag_app/huggingface_cache"

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={"temperature": 0.1, "max_new_tokens": 100, "repetition_penalty": 1.03},
    )

model = ChatHuggingFace(llm=llm)
response = model.invoke("WHat is loss function in deep learning?")
print(response.content)