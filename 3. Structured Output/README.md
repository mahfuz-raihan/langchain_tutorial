# Structured Output

In LangChain, Structured Output is a feature that lets you force an LLM’s response to follow a specific schema or format (like JSON, Pydantic models, or other structured objects) instead of producing free-form text.

## Why it exists
Normally, LLMs generate plain text, which:
* Can be inconsistent in formatting
* May require extra parsing
* Makes automation harder

Structured Output solves this by:
1. Defining a schema — the exact fields, types, and nesting allowed.
2. Validating output — ensuring the model’s response actually matches the schema.
3. Returning a structured object — ready to use directly in code without extra parsing logic.


## Funciton that we will use - 
Using ```with_structured_output()``` function, we can build the model output more structured and more context topic. We can say, this is called ```data_formater```

There is 3 type of ```data_format``` we can use in  ```LangChain```:
1. TypedDict
2. PyDantic
3. json_schema

### **1. TypedDict**
```TypedDict``` is a way to define a dictionary in python where you specify what keys and values should exist. It helps ensure that your distionary follows a specific structure. 

**Why use TypedDict?**
* It tells python what keys are required and what type of values they should have.
* It does not validate data at runtime (it just helps with type hints for better coding.)


### **2. Pydantic**
```pydantic``` is a data validation and data parsing library for python, it ensures that the data you work with is correct, structured and type-safe.

Importantly, it allows you to define models that can be used to validate and parse data, ensuring that the data adheres to a specific structure.
> *But pydentic with_structured_output() function is used to define a schema for the output of a model, ensuring that the response adheres to a specific structure. It can only be used with models that support structured output, like OpenAI's GPT-4o.*

### **3. JSON Schema**
```json_schema``` is a way to define the structure of JSON data, specifying what properties it should have, their types, and any constraints. 
It helps ensure that JSON data is valid and follows a specific format.

### **Example of Structured Output using HuggingFace Model**
```python
from langchain import HuggingFacePipeline
from langchain.output_parsers import JsonOutputParser
from langchain.schema import BaseOutputParser, BaseModel, Field
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.output_parsers import with_structured_output
from typing import TypedDict
from typing_extensions import Annotated
from transformers import pipeline
# Load the HuggingFace model
pipe = pipeline("text2text-generation", model="google/flan-t5-base")
# Define the output schema using TypedDict
class MyOutput(TypedDict):
    name: str
    age: int
    hobbies: list[str]
# Create the HuggingFace pipeline
hf_pipeline = HuggingFacePipeline(pipeline=pipe)
# Define the prompt template
prompt_template = PromptTemplate(
    input_variables=["input"],
    template="Extract the name, age, and hobbies from the following text: {input}"
)
# Create the output parser
output_parser: BaseOutputParser = with_structured_output(JsonOutputParser(pydantic_object=MyOutput))
# Create the LLM chain with structured output
llm_chain = LLMChain(
    llm=hf_pipeline,
    prompt=prompt_template,
    output_parser=output_parser
)
# Run the chain with an example input
input_text = "My name is Alice, I am 30 years old, and I love hiking and reading."
result = llm_chain.run(input_text)
# Print the structured output
print(result)
```
