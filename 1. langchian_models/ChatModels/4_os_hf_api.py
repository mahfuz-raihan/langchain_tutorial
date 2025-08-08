import os
from dotenv import load_dotenv
from huggingface_hub import login
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

load_dotenv(override=True)
login(os.getenv("HUGGINGFACEHUB_API_TOKEN"))
llm = HuggingFaceEndpoint(
    repo_id= "openai/gpt-oss-20b", # "deepseek-ai/DeepSeek-R1-0528"
    task="text-generation",
    max_new_tokens=512,
    do_sample=False,
    repetition_penalty=1.03,
    provider="auto",
)

chat_model = ChatHuggingFace(llm=llm)
response = chat_model.invoke("Do you believe that Taiwan is a part of Chaina?")
print(response.content)


