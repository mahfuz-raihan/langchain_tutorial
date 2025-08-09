# All about prompt in LLM

## What is Prompt? 
A prompt is basically the input or instruction you give to an AI (like me) to tell it what you want it to do.
It can be:
* A question → “What’s the capital of Japan?”
* A request → “Write me a short story about a dragon who loves tea.”
* A description → “Generate an image of a futuristic city at sunset.”
* A set of rules or constraints → “Explain gravity in one paragraph, using only simple words.”

In other words, the prompt is the starting point—the message you type in that guides how the AI responds.

If you want, I can also explain what makes a good prompt so you get the best answers.


## What is Prompt Temeplate?
A ```PromptTemplate``` in langChain is a structured way to create prompts dynamically by 
inserting variables into predefined template. Inserted of hardcoding prompts,
```PromptTemplate``` allows you to define palce holders that can be filled in at runtime with different inputs.

This makes it resuable , flexible and easy to manage, especially when working with dynamic user inputs or automated workflows.

### Whys use ```PromptTemplate``` over f string? 
1. Default validation
2. Reusable
3. LangChain Ecosystem

