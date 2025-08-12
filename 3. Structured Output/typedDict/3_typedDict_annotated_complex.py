""" When we need to generate exact output format, we can use TypedDict to define the sturctured output.
This is useful when we want to ensure the output matches a specific schema."""
import os
from dotenv import load_dotenv
from huggingface_hub import login
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from typing import TypedDict, Annotated, Optional

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
    key_themes: Annotated[list[str],"write all the key themes discussed in the review list"]
    summary: Annotated[str, "Summary of the review"]
    sentiment: Annotated[str,"Sentiment of the review"]
    pos: Annotated[Optional[list[str]], "List of positive aspects mentioned in the review"]
    neg: Annotated[Optional[list[str]], "List of negative aspects mentioned in the review"]

structured_model = chat_model.with_structured_output(ResponseSchema)
review_text = """
Jeep Wrangler Review — The Adventure Brick on Wheels
Pros:
Off-road legend - This thing will climb rocks, splash through mud, and tackle trails that make other SUVs cry.
Customizable - Doors off, roof off, windshield down... it's basically Lego for grown-ups.
Iconic style - People know it's a Wrangler from a mile away. It hasn't really changed in decades—and that's the point.
Strong resale value - Wranglers hold their value surprisingly well, especially well-kept ones.
Adventure-ready accessories - Roof racks, light bars, snorkels—you can kit it out like a survival movie prop.
Cons:
Bumpy on-road ride - Feels like the pavement is personally offended by your presence.
Fuel economy - Let's just say the gas station cashier might know your coffee order.
Wind noise - Above 60 mph, conversations turn into a yelling match.
Pricey options - A few clicks on the build sheet and you're suddenly in luxury SUV territory.
Cargo space - With the back seats up, it's not winning any Tetris championships.
Bottom line: If your life is 70% road, 30% off-road, it's a compromise. 
If it's the other way around, the Wrangler feels like home. It's not for people who want a quiet, cushy ride—it's for people who see mud puddles as an invitation.
"""

response = structured_model.invoke("Please summarize the following review and provide the sentiment (positive, negative, or neutral): \n" + review_text)
print(response)