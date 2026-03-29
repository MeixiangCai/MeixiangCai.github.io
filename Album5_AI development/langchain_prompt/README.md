# LangChain Poem Expander

## Objective
Use LangChain and AI to expand the poem “浮世三千” in a lyrical style.

## Process
	1.	Initialize a ChatOpenAI client with API key and model configuration.
	2.	Send system and user messages to generate AI-expanded poetry.
	3.	Create a PromptTemplate for batch expansion with customizable style and poem input.
	4.	Use ChatPromptTemplate to structure messages with roles for more nuanced outputs.
	5.	Print and review the generated poem expansions.