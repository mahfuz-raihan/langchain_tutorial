# Runnable in LangChain
This directory contains examples and components related to the `Runnable` interface in LangChain. The `Runnable` interface is a core abstraction that allows for the execution of various components, such as language models, chains, and tools, in a consistent manner.

## Type of Runnables
Task Specific Runnables:
- **LLM**: Represents a language model that can generate text based on a given prompt.
- **Chat Model**: Represents a conversational model that can generate responses in a chat format.
- **Embeddings**: Represents a model that can generate vector representations of text for tasks like similarity search.
- **Text Splitter**: A component that splits text into smaller chunks for processing.

**Runnable Primitives**:\
**Defination**: The base interface for all runnable components. 
1. **Runnable**: The base interface for all runnable components.
2. **RunnableMap**: A component that applies a runnable to each item in a list.
3. **RunnableLambda**: A component that allows for the execution of a custom function as a runnable.
4. **RunnablePassthrough**: A component that simply passes the input through without any modification