import os
from dotenv import load_dotenv
from huggingface_hub import login
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain.prompts import PromptTemplate


load_dotenv(override=True)
login(os.getenv("HUGGINGFACEHUB_API_TOKEN"))
print("Login successfully complete.........")


# model
LLM = HuggingFaceEndpoint(
    repo_id= "openai/gpt-oss-20b", #"deepseek-ai/DeepSeek-R1-0528", # "openai/gpt-oss-120b",
    task="text-generation",
    max_new_tokens=512,
    do_sample=False,
    repetition_penalty=1.03,
    provider="auto",
)

model = ChatHuggingFace(llm=LLM)

# define a prompt
prompt = PromptTemplate(
    input_variables=['topic'],
    template='Suggest a catchy blog title about {topic}'
)

topic = input("Enter a topic:")

# format prompt manually using PromptTemplate
formated_prompt = prompt.format(topic=topic)

blog_title = model.invoke(formated_prompt)

# print the output
print(f"Geneted Blog Title: {blog_title.content}")