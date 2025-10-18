import os
from dotenv import load_dotenv

from huggingface_hub import login

from langchain_huggingface import HuggingFaceEmbeddings, HuggingFaceEndpoint, ChatHuggingFace
from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound, TranscriptsDisabled
from langchain_core.output_parsers import StrOutputParser
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda



# Load the environments variables 
load_dotenv()
HF_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
hf_home = os.getenv("env")
os.environ["HF_HOME"] = os.getenv("env")
if not HF_TOKEN:
    raise ValueError("HF Token not found in .env file")
login(HF_TOKEN)

# process the video transcript
def process_video_transcript(video_id: str):
    """
    Fetches transcript, splits it, create embeddings, and returns a retrivaer.
    Return None if no english transcript is available.
    """

    try:
        # Define available english transcripts
        ytt = YouTubeTranscriptApi()
        transcript_list =ytt.fetch(video_id=video_id, languages=['en'])
        transcripts = " ".join(snipper.text for snipper in transcript_list)
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = splitter.create_documents([transcripts])
        
        # define embeddings
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={"device": "cpu"},
            cache_folder=hf_home,
            encode_kwargs={"normalize_embeddings": False},
        )
        # text to vectore embeddings
        vector_store = FAISS.from_documents(chunks, embeddings) 

        retrivers = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})

        return retrivers
    except (NoTranscriptFound, TranscriptsDisabled) as e:
        print(f"No captions available for this video | Error -> \n{e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def create_rag_chain(retrivers: FAISS):
    """
    Create the complete RAG chain.
    """

    # define the LLM from HugginegFace
    llm = HuggingFaceEndpoint(
        repo_id="mistralai/Mistral-7B-Instruct-v0.2",
        task="text-generation",
        max_new_tokens=512,
        do_sample=False,
        repetition_penalty=1.03,
        temperature=0.1,
    )
    chat_model = ChatHuggingFace(llm=llm)

    # Define the prompt template
    prompt_template = """
    You are a helpful assistant who answers questions based ONLY on the provided video transcript context.
    Your answer should be concise and directly address the user's question.
    If the context is insufficient to answer the question, you MUST say 'I do not have enough information from the video to answer that.'

    CONTEXT:
    {context}

    QUESTION:
    {question}

    ANSWER:
    """
    prompt = PromptTemplate(
        template=prompt_template,
        input_variables=["context", "question"],
    )

    # Define how to format the retrieved documents into a single context string
    def format_docs(retrieved_documents):
        context = "\n\n".join(doc.page_content for doc in retrieved_documents)
        return context

    # Define the chain that runs in parallel to fetch context and pass the question
    parallel_chain = RunnableParallel({
        "context": retrivers | RunnableLambda(format_docs),
        "question": RunnablePassthrough()
    })

    # The final chain that pieces everything together
    parser = StrOutputParser()
    main_chain = parallel_chain | prompt | chat_model | parser
    return main_chain