# Structured Output

In LangChain, Structured Output is a feature that lets you force an LLM’s response to follow a specific schema or format (like JSON, Pydantic models, or other structured objects) instead of producing free-form text.

### Why it exists
Normally, LLMs generate plain text, which:
* Can be inconsistent in formatting
* May require extra parsing
* Makes automation harder

Structured Output solves this by:
1. Defining a schema — the exact fields, types, and nesting allowed.
2. Validating output — ensuring the model’s response actually matches the schema.
3. Returning a structured object — ready to use directly in code without extra parsing logic.

