import os
from dotenv import load_dotenv
from huggingface_hub import login
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
import streamlit as st

load_dotenv(override=True)
login(os.getenv("HUGGINGFACEHUB_API_TOKEN"))


def llm_invoke(prompt):
    llm = HuggingFaceEndpoint(
        repo_id= "openai/gpt-oss-20b", # "deepseek-ai/DeepSeek-R1-0528"
        task="text-generation",
        max_new_tokens=100,
        do_sample=False,
        repetition_penalty=1.03,
        provider="auto",
    )
    chat_model = ChatHuggingFace(llm=llm)
    response = chat_model.invoke(prompt)
    return response.content

def main():
    st.header('Research Assistant')
    user_input = st.text_area("Ask a question or tell something:")
    if st.button('Submit'):
        result = llm_invoke(user_input)
        st.write(result.split("<|assistant|>")[-1].strip())

if __name__ == "__main__":
    main()



