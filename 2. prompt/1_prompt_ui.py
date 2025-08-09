import os
from dotenv import load_dotenv
from huggingface_hub import login
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
import streamlit as st
from langchain_core.prompts import PromptTemplate
import re

load_dotenv(override=True)
login(os.getenv("HUGGINGFACEHUB_API_TOKEN"))


def llm_invoke(prompt):
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
    response = chat_model.invoke(prompt)
    return response.content

# make a template for the prompt

prompt_template = PromptTemplate(
    input_variables=["paper_name", "style", "length", "user_input"],
    template="""
    Please summarize the research paper "{paper_name}" in a {style} style with a {length} length.
    Explain style: {style}
    Length: {length}
    1. Mathematical Details:
        - Include relevant mathematical equations if present in the paper.
        - Explain the mathematical concepts using simple, intuative code snippets where applicable.
    2. Analogies and Examples:
        - Use analogies and examples to explain complex concepts.
    If certain concepts are not present in the paper, respond with: "Insufficient information available" instead of guessing or making up details.
    Ensure the summary in is clear, accurate and alighned with the provided style and length.
""",
)

# fill the palceholders in the template
def format_prompt(paper_name, style, length):
    return prompt_template.format(
        paper_name=paper_name,
        style=style,
        length=length,
    )

def main():
    # Streamlit app setup
    st.set_page_config(page_title="Research Assistant", page_icon=":book:")
    st.header('Research Assistant')
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
        result = llm_invoke(format_prompt(paper_input, style_input, length_input))
        st.write(result)  # Renders Markdown + MathJax
        

if __name__ == "__main__":
    main()



