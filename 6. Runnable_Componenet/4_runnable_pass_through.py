import os
from dotenv import load_dotenv
from huggingface_hub import login
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableSequence, RunnablePassthrough

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
print("Chatmodel Select from HuggingFace model 1: ", model_1.get_name())
print("Chatmodel Select from HuggingFace model 1: ", model_2.get_name())

prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)
prompt2 = PromptTemplate(
    template='Explain the following joke - {text}',
    input_variables=['text']
)
parser = StrOutputParser()


joke_generator_chain = RunnableSequence(prompt1, model_1, parser)

parallel_chain = RunnableParallel(
    {
        'joke': RunnablePassthrough(),
        'explanation':RunnableSequence(prompt2, model_2, parser)
    }
)

final_chain = RunnableSequence(joke_generator_chain, parallel_chain)

final_result = final_chain.invoke({'topic':'football'})

print(final_result['joke'])
print(final_result['explanation'])