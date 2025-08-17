import os
from dotenv import load_dotenv
from huggingface_hub import login
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

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

schema = [
    ResponseSchema(name='fact_1', description='Fact 1 about the topic'),
    ResponseSchema(name='fact_2', description='Fact 1 about the topic'),
    ResponseSchema(name='fact_3', description='Fact 1 about the topic'),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='Give 3 fact about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

prompt = template.invoke({'topic':'black hole'})
result = chat_model.invoke(prompt)
final_result = parser.parse(result.content)

print(final_result)