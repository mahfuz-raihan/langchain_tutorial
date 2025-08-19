# Chains in LangChain

## what are chains?
Chains in LangChain are sequences of operations that can be executed in a specific order. They allow you to combine multiple components, such as prompts, models, and tools, to create complex workflows.
Chains can be used to build applications that require multiple steps, such as question answering, summarization, or data processing.

## Why Use Chains?
Chains provide a structured way to manage the flow of data and operations in your application. They help to:
- Organize complex workflows into manageable steps.
- Reuse components across different parts of your application.
- Enhance readability and maintainability of your code.
- Facilitate debugging by isolating operations.
## How to Create a Chain
Creating a chain in LangChain involves defining a sequence of operations and linking them together. Here’s a simple example of how to create a chain:

## Types of Chains
- **Simple Chains**: A straightforward sequence of operations.
- **Sequential Chains**: Chains that execute operations in a specific order, passing outputs from one step to the next.
- **Parallel Chains**: Chains that execute multiple operations simultaneously.
- **Conditional Chains**: Chains that execute different operations based on certain conditions.
- **Custom Chains**: User-defined chains that can include any combination of operations.

## View of graph chain 

```mathematica
     +-------------+       
     | PromptInput |
     +-------------+
            *
            *
            *
    +----------------+
    | PromptTemplate |
    +----------------+
            *
            *
            *
   +-----------------+
   | ChatHuggingFace |
   +-----------------+
            *
            *
            *
   +-----------------+
   | StrOutputParser |
   +-----------------+
            *
            *
            *
+-----------------------+
| StrOutputParserOutput |
+-----------------------+
            *
            *
            *
    +----------------+
    | PromptTemplate |
    +----------------+
            *
            *
            *
            *
            *
            *
   +-----------------+
            *
            *
            *
            *
            *
            *
   +-----------------+
            *
            *
            *
            *
            *
            *
            *
            *
            *
            *
            *
            *
            *
            *
            *
            *
            *
            *
   +-----------------+
   | ChatHuggingFace |
   +-----------------+
            *
            *
            *
   +-----------------+
   | StrOutputParser |
   +-----------------+
            *
            *
            *
+-----------------------+
| StrOutputParserOutput |
+-----------------------+
```