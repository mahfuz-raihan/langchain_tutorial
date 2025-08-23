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

### Example of a Graph Chain: Sequential Chain
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

### Example of a Graph Chain: Parallel Chain
```mathematica
            +---------------------------+
            | Parallel<notes,quiz>Input |
            +---------------------------+
                ***               ***
            ***                     ***
        **                              **
+----------------+                    +----------------+
| PromptTemplate |                    | PromptTemplate |
+----------------+                    +----------------+
          *                                   *
          *                                   *
          *                                   *
+-----------------+                  +-----------------+
| ChatHuggingFace |                  | ChatHuggingFace |
+-----------------+                  +-----------------+
          *                                   *
          *                                   *
          *                                   *
+-----------------+                  +-----------------+
| StrOutputParser |                  | StrOutputParser |
+-----------------+                  +-----------------+
                  ***               ***
                     ***         ***
                        **     **
             +----------------------------+
             | Parallel<notes,quiz>Output |
             +----------------------------+
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
```
### Example of a Graph Chain: Conditional Chain
```mathematica
            +-----------------------------+
            | Conditional<sentiment>Input |
            +-----------------------------+
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
                        *                *
+-----------------------+        +-----------------------+
| StrOutputParserOutput |        | StrOutputParserOutput |
+-----------------------+        +-----------------------+
                        *                *
                        *                *
                        *                *
                +----------------+  +----------------+
                | PromptTemplate |  | PromptTemplate |
                +----------------+  +----------------+
                        *                *
                        *                *
                        *                *
                +-----------------+  +-----------------+
                | ChatHuggingFace |  | ChatHuggingFace |
                +-----------------+  +-----------------+
                        *                *
                        *                *
                        *                *
                +-----------------+  +-----------------+
                | StrOutputParser |  | StrOutputParser |
                +-----------------+  +-----------------+
                            *              *
                            *              *
                            *              *
                    +------------------------------+
                    | Conditional<sentiment>Output |
                    +------------------------------+
```

### Chains in LangChain
In LangChain, chains can be created using the `Chain` class or by using predefined chains. Here’s an example of how to create a simple chain using LangChain:

|**Chian Name**|**Description**|
|--------------|---------------|
|LLMChain |A basic chain that connects a prompt to a model and then to an output parser.|
|SequentialChain |A chain that executes a series of operations in a specific order, passing outputs from one step to the next.|
|SimpleSequentialChain |A simplified version of SequentialChain for straightforward workflows.|
|RouterChain |A chain that routes inputs to different sub-chains based on certain conditions.|
|ConversationalRetrievalChain |A chain designed for managing conversational interactions, maintaining context across multiple turns.|
|RetrievalQAChain |A chain that combines retrieval and question answering, allowing for more informed responses.|
|MultiPromptChain |A chain that can handle multiple prompts, useful for scenarios requiring diverse inputs.|
|HydeChain (Hypothetical Document Embedding) |A chain that generates hypothetical documents to enhance retrieval and response quality.|
|AgentExecutorChian |A chain that executes a series of actions based on agent decisions, often used in more complex applications.|
|SQLDatabaseChain |A chain that interacts with SQL databases, allowing for querying and data manipulation.|
