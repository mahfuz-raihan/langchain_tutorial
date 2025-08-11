from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
print("Loaded environment variables...")

load_dotenv()

llm = ChatOpenAI(model= "gpt-3.5-turbo-instruct")

print("Initialized ChatOpenAI model...")
while True:
    
    user_input = input("Enter your question (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("Exiting the program.")
        break

    print("Invoking LLM with user input...")
    resutl = llm.invoke(user_input)
    print("LLM response:", resutl)
# resutl = llm.invoke("What is the capital of Bangladesh?")

print("LLM response:", resutl)
