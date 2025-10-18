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


