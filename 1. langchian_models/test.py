# import langchain

# print("LangChain version:", langchain.__version__)


import importlib.util

print(importlib.util.find_spec("uv") is not None)
