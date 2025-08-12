""" When we need to generate exact output format, we can use TypedDict to define the sturctured output.
This is useful when we want to ensure the output matches a specific schema."""
import os
from dotenv import load_dotenv
from huggingface_hub import login
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from typing import TypedDict, Annotated

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
    summary: Annotated[str, "Summary of the review"]
    sentiment: Annotated[str,"Sentiment of the review"]

structured_model = chat_model.with_structured_output(ResponseSchema)
review_text = """My middle child was absolutely captivated by a commercial for these Colgate Cleansing® Mini Brushes, and he insisted we get them. I have to say, he's been loving them, and from my perspective, they actually do a fantastic job of cleaning. The bristles are effective, and the integrated toothpaste and pick make them incredibly convenient for on-the-go use, whether it's for work, school, or travel. They truly deliver on the promise of a quick, thorough clean when a traditional brush isn't an option.
My primary reservation, and it's a significant one for me, is the inclusion of fluoride toothpaste. I've been actively trying to move towards products with a "cleaner" paste, and unfortunately, these don't align with that preference. While the product performs exceptionally well in terms of cleaning and convenience, this ingredient choice might lead me to explore other brands in the future that offer a fluoride-free option for similar disposable brushes."""

response = structured_model.invoke("Please summarize the following review and provide the sentiment (positive, negative, or neutral): \n" + review_text)
print(response)