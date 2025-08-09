# LangChain Models: LLM, ChatModel, and Embedding Model

## 1. LLM (Large Language Model)
**Definition:**  
An interface for models that take **plain text** as input and return **plain text** as output.  
Used for single-shot tasks without conversation structure.

**Example:**
```python
from langchain.llms import OpenAI
llm = OpenAI(model_name="text-davinci-003")
response = llm("Write a haiku about the ocean.")
```
**Example flow:**
```vbnet
Input: "Summarize the following text: ..."
↓
LLM processes text
↓
Output: "This text is about..."
```
**Characteristics:**
* No concept of conversation history.
* Best for single-shot tasks like summarization, classification, or content generation.
* Examples in LangChain: ```OpenAI(model_name="text-davinci-003")```, ```HuggingFaceHub(...).```

**Use case examples:**
* Generating marketing copy
* Translating text
* Summarizing documents

## 2. ChatModel
**Definition:**

An interface for message-based models designed for multi-turn conversations.
Takes structured messages with roles (```system```, ```user```, ```assistant```) and returns messages.

**Example:**
```python
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

chat = ChatOpenAI(model_name="gpt-3.5-turbo")
response = chat([HumanMessage(content="Tell me a joke.")])
```
**Purpose:**
* Designed for multi-turn conversations and message-based interactions.
* Takes structured message objects (e.g., ```SystemMessage```, ```HumanMessage```, ```AIMessage```) rather than just raw strings.

**Example flow:**
```python
messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Tell me a joke."),
]
↓
ChatModel processes messages
↓
Output: AIMessage(content="Why did the chicken cross the road? ...")

```
**Characteristics:**
* Maintains role separation (```system```, ```user```, ```assistant```).
* Can handle conversation history more naturally.
* Examples in LangChain: ```ChatOpenAI(model_name="gpt-3.5-turbo")```,``` ChatAnthropic(...).```

**Use case examples:**
* Chatbots
* Interactive tutoring systems
* Customer support automation

## 3. Embedding Model
**Definition:**

An interface for models that convert text into numerical vectors (embeddings) representing semantic meaning.
Used for similarity search, retrieval, and clustering.
**Purpose:**
* Converts text into numerical vectors (```embeddings```) that capture semantic meaning.
* These vectors are used for similarity search, semantic retrieval, or clustering.

**Example:**
```python
from langchain.embeddings import OpenAIEmbeddings
embeddings = OpenAIEmbeddings()
vector = embeddings.embed_query("Artificial intelligence in healthcare")
```
**Example Flow**:
```vbnet
Input: "Artificial intelligence is transforming industries."
↓
Embedding model processes text
↓
Output: [0.021, -0.134, 0.872, ...]  # high-dimensional vector

```
**Characteristics:**
* Does not generate human-readable text.
* Works with vector databases like FAISS, Pinecone, Weaviate.
* Examples in LangChain: ```OpenAIEmbeddings()```, ```HuggingFaceEmbeddings()```.

**Use case examples:**
* Semantic document search
* Recommendation engines
* RAG (Retrieval-Augmented Generation) pipelines

## Key Difference
| Feature               | LLM             | ChatModel        | Embedding Model            |
| --------------------- | --------------- | ---------------- | -------------------------- |
| Input Format          | String          | List of messages | String                     |
| Output Format         | String          | Message object   | Vector (list of floats)    |
| Conversation Handling | No              | Yes              | No                         |
| Primary Use           | Text generation | Conversations    | Semantic similarity search |

## Visual Over view
```mathematica
            ┌─────────────────┐
            │   Text Input    │
            └─────────────────┘
                     │
        ┌────────────┼────────────┐
        │            │            │
   ┌────▼─────┐ ┌────▼─────┐ ┌────▼─────┐
   │   LLM    │ │ ChatModel│ │ Embedding│
   └────▲─────┘ └────▲─────┘ └────▲─────┘
        │            │            │
Text Out│     Message│Out   Vector│Out
        │            │            │
```
## How They Work Together in RAG (Retrieval-Augmented Generation)
```mathematica
         ┌──────────────────────┐
         │ User Query           │
         └──────────────────────┘
                    │
                    ▼
        ┌───────────────────────────┐
        │ Embedding Model           │
        │ (e.g., OpenAIEmbeddings)  │
        └───────────────────────────┘
                    │
                    ▼
        ┌───────────────────────────┐
        │ Vector Store              │
        │ (FAISS / Pinecone / etc.) │
        └───────────────────────────┘
                    │ Retrieved Docs
                    ▼
        ┌───────────────────────────┐
        │ LLM / ChatModel           │
        │ (Generates final answer)  │
        └───────────────────────────┘
                    │
                    ▼
         ┌──────────────────────┐
         │ Final Response       │
         └──────────────────────┘
```