import os
from dotenv import load_dotenv
load_dotenv()
from huggingface_hub import login
login(os.getenv("HUGGINGFACEHUB_API_TOKEN"))
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import streamlit as st 



def llm_invoke(prompt):
    os.environ["HF_HOME"] = "C:/Users/BS01519/OneDrive - Brain Station 23/Desktop/rag_app/huggingface_cache"
    llm = HuggingFacePipeline.from_model_id(
        model_id= "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        task="text-generation",
        pipeline_kwargs={"temperature": 0.1, "max_new_tokens": 3000, "repetition_penalty": 1.03},
        )

    model = ChatHuggingFace(llm=llm)
    
    return model.invoke(prompt).content

def main():
    st.header('Research Assistant')
    user_input = st.text_area("Ask a question or tell something:")
    if st.button('Submit'):
        result = llm_invoke(user_input)
        st.write(result.split("<|assistant|>")[-1].strip())

if __name__ == "__main__":
    main()



