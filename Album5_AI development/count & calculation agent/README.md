# AI Agent for Character Count and Python Computation

## Objective
Build an AI agent capable of counting characters and performing Python-based calculations.

## Process
	1.	Initialize the AI model and conversation memory.
	2.	Create tools: a character counter and Python REPL for computations.
	3.	Build a ReAct-style agent with the tools and prompt template.
	4.	Run the agent via AgentExecutor to answer text and calculation queries.
	5.	Optionally, run a Python-only agent for standalone computations.

## Requirements
The agent should be able to solve:

	1. ‘君不见黄河之水天上来，奔流到海不复回’这句话的字数是多少?  
	2. 用python求1..10的阶乘之和。只输出一个整数。  
	3. 计算1到100的立方和
