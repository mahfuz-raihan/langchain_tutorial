import os
from dotenv import load_dotenv
from huggingface_hub import login
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv(override=True)
login(os.getenv("HUGGINGFACEHUB_API_TOKEN"))
print("Login successfully complete.........")


llm = HuggingFaceEndpoint(
    repo_id= "openai/gpt-oss-20b", #"deepseek-ai/DeepSeek-R1-0528", # "openai/gpt-oss-120b",
    task="text-generation",
    max_new_tokens=512,
    do_sample=False,
    repetition_penalty=1.03,
    provider="auto",
)
chat_model = ChatHuggingFace(llm=llm)
print("Chatmodel Select from HuggingFace >>>>>>>>>>")

# 1st prompt -> detailed report
template1 = PromptTemplate(
    template="write a detailed report on {topic}",
    input_variables=['topic']
)
# 2nd prompt -> summary 
template2 = PromptTemplate(
    template='Write a 5 line summary on the following text. \n {text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain = template1 | chat_model | parser | template2 | chat_model | parser

result = chain.invoke({'topic':'cricket'})

print(result)
chain.get_graph().print_ascii()