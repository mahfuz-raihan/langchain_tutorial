# import langchain

# print("LangChain version:", langchain.__version__)


# import importlib.util

# print(importlib.util.find_spec("uv") is not None)

import os
from dotenv import load_dotenv
load_dotenv()
print(os.getenv("HUGGINGFACEHUB_API_TOKEN"))
