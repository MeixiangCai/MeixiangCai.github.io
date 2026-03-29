# AI Conversation Memory Assistant

## Objective
Enable an AI model to remember conversation context for multi-turn dialogues.

## Process
    1.	Initialize a ChatOpenAI client with API key, model, and endpoint.
	2.	Set up ConversationBufferMemory to store and return chat history.
	3.	Define a ChatPromptTemplate with system instructions, memory placeholder, and human input.
	4.	Create a ConversationChain combining the model, prompt, and memory.
	5.	Use invoke() to ask questions and receive context-aware responses across multiple turns.