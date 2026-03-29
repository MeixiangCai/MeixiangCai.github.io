# RAG-based Document QA Agent

## Objective
Build an AI agent that retrieves information from external documents and generates answers using LLM.

## Process
	1.	Load documents (CSV, PDF, or text) and optionally split them into chunks.
	2.	Embed documents into vectors using HuggingFace embeddings.
	3.	Build a FAISS vector database and create a retriever.
	4.	Initialize a chat model with memory for multi-turn conversation.
	5.	Combine retrieval and generation via a Conversational Retrieval Chain to answer user questions.
	
- The document to be embedded has been provided.
- The local model file has also been provided (it has to be installed in the same folder as .py).