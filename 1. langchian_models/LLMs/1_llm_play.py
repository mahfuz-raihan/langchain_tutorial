from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
print("Loaded environment variables...")

load_dotenv()

llm = ChatOpenAI(model= "gpt-3.5-turbo-instruct")

print("Initialized ChatOpenAI model...")
resutl = llm.invoke("What is the capital of Bangladesh?")

print("LLM response:", resutl)
