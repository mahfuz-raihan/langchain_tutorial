import os
from dotenv import load_dotenv
from huggingface_hub import login
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
import re

load_dotenv(override=True)
login(os.getenv("HUGGINGFACEHUB_API_TOKEN"))


llm = HuggingFaceEndpoint(
    repo_id = "openai/gpt-oss-20b",
    task="text-generation",
    provider="auto",
)
chat_model = ChatHuggingFace(llm=llm)

chat_history = [
    SystemMessage(content="You are a helpfull assistant."),
]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input == "exit":
        break
    result = chat_model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print(f"AI: {result.content}")

print(chat_history)