from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace, HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
import huggingface_hub

video_id = "J5_-l7WIO_w&t"

try:
    transcripts_list = YouTubeTranscriptApi().fetch(video_id, languages=['en'])
    # print(transcripts_list[:2])

    transcripts = " ".join(snipper.text for snipper in transcripts_list)
    print(transcripts)
except Exception as e:
    print(f"No captions available for this video | Error -> \n{e}")