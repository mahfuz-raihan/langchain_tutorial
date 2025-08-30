import os
from dotenv import load_dotenv
from huggingface_hub import login
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

load_dotenv(override=True)
login(os.getenv("HUGGINGFACEHUB_API_TOKEN"))
print("Login successfully complete.........")

# We will take 2 model parallely
# model 1
llm1 = HuggingFaceEndpoint(
    repo_id= "openai/gpt-oss-20b", #"deepseek-ai/DeepSeek-R1-0528", # "openai/gpt-oss-120b",
    task="text-generation",
    max_new_tokens=512,
    do_sample=False,
    repetition_penalty=1.03,
    provider="auto",
)

# model 2
llm2 = HuggingFaceEndpoint(
    repo_id= "deepseek-ai/DeepSeek-R1-0528", #"deepseek-ai/DeepSeek-R1-0528", # "openai/gpt-oss-120b",
    task="text-generation",
    max_new_tokens=512,
    do_sample=False,
    repetition_penalty=1.03,
    provider="auto",
)

model_1 = ChatHuggingFace(llm=llm1)
model_2 = ChatHuggingFace(llm=llm2)
print("Chatmodel Select from HuggingFace model 1: ", model_1.name)
print("Chatmodel Select from HuggingFace model 1: ", model_2.name)


prompt1 = PromptTemplate(
    template="Generate short and simple notes from the following text \n{text}",
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template="Generate 5 short questions answers from the following text \n{text}",
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template="Merge the proveded notes and quiz into a single document \n notes -> {notes} and {quiz}",
    input_variables=['notes','quiz']
)

# define parser
parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model_1 | parser,
    'quiz': prompt2 | model_2 | parser
})

merge_chain = prompt3 | model_1 | parser

chain = parallel_chain | merge_chain

text = """
Ordinarily, “automatic mixed precision training” means training with torch.autocast and torch.amp.GradScaler together.

Instances of torch.autocast enable autocasting for chosen regions. Autocasting automatically chooses the precision for operations to improve performance while maintaining accuracy.

Instances of torch.amp.GradScaler help perform the steps of gradient scaling conveniently. Gradient scaling improves convergence for networks with float16 (by default on CUDA and XPU) gradients by minimizing gradient underflow, as explained here.

torch.autocast and torch.amp.GradScaler are modular. In the samples below, each is used as its individual documentation suggests.

(Samples here are illustrative. See the Automatic Mixed Precision recipe for a runnable walkthrough.)
"""
result = chain.invoke({'text': text})

print(result)
chain.get_graph().print_ascii()