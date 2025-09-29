from langchain_community.retrievers import WikipediaRetriever
print("Necessary Librariy imported successfully.....")


# initialize the retriverser 
retrivers = WikipediaRetriever(top_k_results=2, lang='en')

# define the query

query = "the geopolitical history of Bangladesh and Pakistan from the perspective of a chinese."

docs = retrivers.invoke(query)

for i, doc in enumerate(docs):
    print(f"\n --- Result {i+1} ---")
    print(f"Content:\n{doc.page_content}...")

