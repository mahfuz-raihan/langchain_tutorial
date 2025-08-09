from langchain_core.prompts import PromptTemplate
import os


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

prompt_template.save("prompt_template.json")