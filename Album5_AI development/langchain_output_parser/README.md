# LangChain Output Parser Example

## Objective
Use LangChain to parse AI responses into structured lists with a specified format.

## Process
    1.	Initialize a ChatOpenAI client with API key and model configuration.
	2.	Create a CommaSeparatedListOutputParser to define the output structure.
	3.	Generate format instructions from the parser and include them in a PromptTemplate.
	4.	Invoke the model with a subject (e.g., “诗人”) and receive AI output.
	5.	Parse the raw response into a clean Python list for further use.