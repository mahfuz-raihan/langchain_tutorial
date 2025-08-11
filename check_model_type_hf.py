import os
from dotenv import load_dotenv
from huggingface_hub import model_info

# Load environment variables
load_dotenv()
# Get model info directly
info = model_info("openai/gpt-oss-20b", token=os.getenv("HUGGINGFACEHUB_API_TOKEN"))
# print(info)
# Check the pipeline type
print("Pipeline tag:", info.pipeline_tag)

