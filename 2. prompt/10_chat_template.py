from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


# chat temeplate
chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful customer support expert."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{query}"),
])
chat_history = []
# load chat history
with open("2. prompt\\chat_history.txt") as file:
    chat_history.extend(file.readlines())

print(chat_history)

# create prompt
prompt = chat_template.invoke({
    "chat_history": chat_history,
    "query": "where is my refund for order #12345?"
})
print(prompt)