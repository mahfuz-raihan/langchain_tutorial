import os
from dotenv import load_dotenv
from huggingface_hub import login
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt
import re

load_dotenv(override=True)
login(os.getenv("HUGGINGFACEHUB_API_TOKEN"))


llm = HuggingFaceEndpoint(
    repo_id= "openai/gpt-oss-20b", # "deepseek-ai/DeepSeek-R1-0528"
    task="text-generation",
    max_new_tokens=100,
    temperature=0,
    do_sample=False,
    repetition_penalty=1.03,
    provider="auto",
)

chat_model = ChatHuggingFace(llm=llm)

prompt_template = load_prompt('prompt_template.json')

def main():
    # Streamlit app setup
    st.set_page_config(page_title="Research Assistant", page_icon="📕")
    st.header('Research Assistant 📖')
    paper_input = st.selectbox(
        "Select Research Paper Name", 
            [
                "Attention Is All You Need", 
                "BERT: Pre-training of Deep Bidirectional Transformers", 
                "GPT-3: Language Models are Few-Shot Learners", 
                "Diffusion Models Beat GANs on Image Synthesis"
            ]
        )

    style_input = st.selectbox("Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]) 

    length_input = st.selectbox("Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"])
    
    if st.button('Summarize'):
        chain = prompt_template | chat_model
        result = chain.invoke({
            'paper_name':paper_input,
            'style':style_input,
            'length':length_input,
        })
        st.write(result.content)  # Renders Markdown + MathJax
        

if __name__ == "__main__":
    main()



