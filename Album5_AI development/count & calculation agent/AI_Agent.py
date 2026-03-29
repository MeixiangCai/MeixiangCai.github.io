#项目目标是搭建AI智能体，完成一些特定任务（统计字符数和数值计算）
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
model=ChatOpenAI(
    api_key="sk-ae518d28b0b144179862cccbe5594daa",
    model="deepseek-chat",
    base_url="https://api.deepseek.com"
)
memory=ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)
#llm不擅长数数，但Python擅长，所以为模型准备一个趁手的工具
from langchain.tools import tool
@tool("word_counter",description="统计输入文本的字符数") #注册工具并给出描述
#给出工具本身/函数定义
def word_counter(text: str) -> int:
    return len(text)
#创建工具列表
tools=[word_counter]

#为Agent添加内置工具
from langchain_experimental.tools import PythonREPLTool
python_repl=PythonREPLTool() #内置工具无需用装饰器注册
tools.append(python_repl)

#编写提示词
from langchain import hub
react_prompt=hub.pull("hwchase17/react-chat") #从hub中下载适用的提示词模板
#创建Agent
from langchain.agents import create_react_agent, AgentExecutor
agent=create_react_agent(
    llm=model,
    tools=tools,
    prompt=react_prompt
)
#创建Agent运行器
agent_executor=AgentExecutor(
    agent=agent,
    tools=tools,
    memory=memory,
    verbose=False
)
#正式启动Agent
question="‘君不见黄河之水天上来，奔流到海不复回’这句话的字数是多少？"
ret=agent_executor.invoke({"input":question})
answer=ret["output"]
print(answer)

question2="用python求1..10的阶乘之和。只输出一个整数。"
ret2=agent_executor.invoke({"input":question2})
print(ret2["output"])

#如果只用内置工具，可以用内置启动器创建客户端
#from langchain_experimental.agents import create_python_agent
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain_experimental.tools import PythonREPLTool
react_prompt=hub.pull("hwchase17/react")
python_tool=PythonREPLTool()
agent2=create_react_agent(
    llm=model,
    tools=[python_tool],
    prompt=react_prompt
)
agent_executor2=AgentExecutor(
    agent=agent2,
    tools=[python_tool],
    verbose=False
) #已经内置提示词了
ret3=agent_executor2.invoke({"input":"计算1到100的立方和"})
print(ret3["output"])





