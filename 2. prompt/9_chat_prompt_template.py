import os
from dotenv import load_dotenv
from huggingface_hub import login
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st
import re
load_dotenv(override=True)
login(os.getenv("HUGGINGFACEHUB_API_TOKEN"))

# Define the chat template
# This template will be used to create a prompt for the chat model
chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert.'),
])
prompt = chat_template.invoke({
    'domain': 'Python programming',
})

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b",
    task="text-generation",
    provider="auto",
)
chat_model = ChatHuggingFace(llm=llm)
while True:
    user_input = input("You: ")
    if user_input == "exit":
        break
    result = chat_model.invoke(prompt)
    print(f"AI: {result.content}")

print(prompt)