import os
from dotenv import load_dotenv
load_dotenv(override=True)
from huggingface_hub import login
login(os.getenv("HUGGINGFACEHUB_API_TOKEN"))
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage


llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b",
    task="text-generation",
    provider="auto",
)
chat_model = ChatHuggingFace(llm=llm)

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="What is the capital of Bangladesh."),]

result = chat_model.invoke(messages)

messages.append(AIMessage(content=result.content))
print(messages)