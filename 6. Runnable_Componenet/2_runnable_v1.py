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
    
llm = DemoLLM()

reply = llm.predict("What is the capital of Bangladesh?")
print(reply)