"""
This script loads an API key from .env, hooks LangChain to HuggingFace's 
TinyLlama chat model, sends it a user prompt (“capital of Bangladesh”), 
and prints the chatbot's reply. Basically, 
it's a quick demo of using HuggingFaceEndpoint with LangChain for lightweight conversational AI.
"""

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
import os
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="conversational",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    provider="featherless-ai"
)

chat = ChatHuggingFace(llm=llm)
resp = chat.invoke([("user", "What is the capital of Bangladesh?")])
print(resp.content)
