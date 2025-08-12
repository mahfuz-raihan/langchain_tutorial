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