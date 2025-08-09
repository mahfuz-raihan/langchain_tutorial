import os
from dotenv import load_dotenv
from huggingface_hub import login
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt
import re

load_dotenv(override=True)
login(os.getenv("HUGGINGFACEHUB_API_TOKEN"))


llm = HuggingFaceEndpoint(
    repo_id = "openai/gpt-oss-20b",
    task="text-generation",
    provider="auto",
)
chat_model = ChatHuggingFace(llm=llm)

chat_history = []
while True:
    user_intput = input("You: ")
    chat_history.append(user_intput)
    if user_intput == "exit":
        break
    result = chat_model.invoke(chat_history)
    chat_history.append(result.content)
    print(f"AI: {result.content}")

print(chat_history)