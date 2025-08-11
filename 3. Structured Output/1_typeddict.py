import os
from dotenv import load_dotenv
from huggingface_hub import login
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from typing import TypedDict

load_dotenv(override=True)
login(os.getenv("HUGGINGFACEHUB_API_TOKEN"))
llm = HuggingFaceEndpoint(
    repo_id= "deepseek-ai/DeepSeek-R1-0528", # "openai/gpt-oss-120b",
    task="text-generation",
    max_new_tokens=512,
    do_sample=False,
    repetition_penalty=1.03,
    provider="auto",
)
chat_model = ChatHuggingFace(llm=llm)

class ResponseSchema(TypedDict):
    summary: str
    sentiment: str

structured_model = chat_model.with_structured_output(ResponseSchema)
review_text = """
Perfect for having in the car for those days you are running late and forget to brush your teeth or just need to brush your teeth randomly in the middle of a busy day running errands! 
Makes me feel refreshed while out and about, love that they come in a hard case for easy storage in the car or a bag. Love how clean my teeth feel after using these! 
Obviously doesn't replace brushing but great when you are away from home and need to do something."""

response = structured_model.invoke("Please summarize the following review and provide the sentiment (positive, negative, or neutral): \n" + review_text)
print(response)
