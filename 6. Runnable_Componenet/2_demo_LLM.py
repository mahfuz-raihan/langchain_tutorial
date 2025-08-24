import random

class DemoLLM():
    def __init__(self):
        print("LLM Created.")
    
    def predict(self, prompt:str):
        response_list = [
            'Dhaka is the capital of Bangladesh',
            'BPL is a cricket leagure',
            'Brain Station 23 is just open the AI team.'
        ]

        return {'response': random.choice(response_list)}
    
# llm = DemoLLM()

class DemoPromptTemplate():
    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables
    
    def format(self, input_dict):
        return self.template.format(**input_dict)
    
template = DemoPromptTemplate(
    template='Write a {length} story about {topic}',
    input_variables=['length','topic']
)

class LLMChain:
    def __init__(self, llm, prompt):
        self.prompt = prompt
        self.llm = llm
    
    def run(self, input_dict):
        final_prompt = self.prompt.format(input_dict)
        result = self.llm.predict(final_prompt)

        return result['response']

llm = DemoLLM()
chain = LLMChain(llm,template)
print(chain.run({'topic':'Bangladesh','length':'short'}))
# prompt = template.format({'topic':'Bangladesh','length':'short'})
# reply = llm.predict(prompt=prompt)
# print(reply)