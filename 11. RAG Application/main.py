import os
from dotenv import load_dotenv
load_dotenv()
import utils
from huggingface_hub import login
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace, HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
login(os.getenv("HUGGINGFACEHUB_API_TOKEN"))

hf_home = os.getenv("env")
os.environ["HF_HOME"] = os.getenv("env")

ask = input("Ask a question: ")
youtube_url = input("Youtube URL: ")
video_id = utils.get_youtube_video_id(youtube_url)


try:
    transcripts_list = YouTubeTranscriptApi().fetch(video_id, languages=['en'])
    transcripts = " ".join(snipper.text for snipper in transcripts_list)
    # print(transcripts)
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.create_documents([transcripts])
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"},
        cache_folder=hf_home,
        encode_kwargs={"normalize_embeddings": False},
    )
    vector_store = FAISS.from_documents(chunks, embeddings)
    retrivers = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})
except Exception as e:
    print(f"No captions available for this video | Error -> \n{e}")

try:
    llm = HuggingFaceEndpoint(
        repo_id="openai/gpt-oss-20b",
        task="text-generation",
        max_new_tokens=512,
        do_sample=False,
        repetition_penalty=1.03,
        provider="auto",
        temperature=0.2,
    )
    chat_model = ChatHuggingFace(llm=llm)
    prompt = PromptTemplate(
        template="""
        You are a helpful assistant.
        Answer ONLY from the provided transcript context.
        If the contest is insufficient, just say you don't know.
        If any one ask about summary or about the video, then answer with proper point.
        {context}
        Question: {question}
        Answer:
        """,
        input_variables=["context", "question"],
    )
except Exception as e:
    print(f"Error happen: {e}")

try:
    parser = StrOutputParser()
    def format_docs(retrived_documents):
        context = "\n\n".join(doc.page_content for doc in retrived_documents)
        return context
    
    parallel_chain = RunnableParallel({
        "context": retrivers | RunnableLambda(format_docs),
        "question": RunnablePassthrough()
    })
    # print(parallel_chain.invoke(ask))
    main_chain = parallel_chain | prompt | chat_model | parser
    result = main_chain.invoke(ask)
    print(result)
except Exception as e:
    print(f"Error happen: {e}")