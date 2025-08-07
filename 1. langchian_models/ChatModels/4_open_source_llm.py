from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
import os
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="conversational",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    provider="featherless-ai"
)

chat = ChatHuggingFace(llm=llm)
resp = chat.invoke([("user", "What is the capital of Bangladesh?")])
print(resp.content)


# import os
# from huggingface_hub import InferenceClient
# from dotenv import load_dotenv
# load_dotenv()
# # Initialize the InferenceClient with your Hugging Face API token
# # Ensure you have the HUGGINGFACEHUB_API_TOKEN set in your environment variables
# client = InferenceClient(
#     provider="featherless-ai",
#     api_key=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
# )

# completion = client.chat.completions.create(
#     model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     messages=[
#         {
#             "role": "user",
#             "content": "What is the capital of France?"
#         }
#     ],
# )

# print(completion.choices[0].message)