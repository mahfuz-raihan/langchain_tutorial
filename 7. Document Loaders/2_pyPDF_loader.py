import os
from dotenv import load_dotenv
from huggingface_hub import login
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel
from langchain_community.document_loaders import PyMuPDFLoader

load_dotenv(override=True)
login(os.getenv("HUGGINGFACEHUB_API_TOKEN"))
print("Login successfully complete.........")


loader = PyMuPDFLoader(file_path='7. Document Loaders\Mahfuz_Raihan_CV.pdf')

docs = loader.load()

# model 1
# llm1 = HuggingFaceEndpoint(
#     repo_id= "openai/gpt-oss-20b", #"deepseek-ai/DeepSeek-R1-0528", # "openai/gpt-oss-120b",
#     task="text-generation",
#     max_new_tokens=512,
#     do_sample=False,
#     repetition_penalty=1.03,
#     provider="auto",
# )

# model = ChatHuggingFace(llm=llm1)

print(docs[0].page_content)