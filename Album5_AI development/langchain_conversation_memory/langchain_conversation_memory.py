#项目目标是让模型记住上下文内容，拥有记忆功能
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory #本项目使用旧版langchain
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import ConversationChain
client=ChatOpenAI(
    api_key="sk-441cc75434834381ad21c9b7c3e43689",
    model="deepseek-chat",
    base_url="https://api.deepseek.com"
)
memory=ConversationBufferMemory(memory_key="chat_history",return_messages=True) #设置键名并且确保返回的是消息列表而不是字符串
memory.load_memory_variables({})
#在提示词中为记忆内容预留占位符，且提示词中角色顺序和回忆上下文内容不能反
prompt=ChatPromptTemplate(
    [
        ("system","你是一位学习助手，简要回答用户问题。不要输出任何额外内容。"),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human","{input}")
    ]
)
#创建对话链，将几个流程串联在一起
chain=ConversationChain(
    llm=client,
    prompt=prompt,
    memory=memory
)
#用invoke()方法调用对话链
response1=chain.invoke({"input":"李白是哪个朝代的诗人？"})
print("第一个问题的回复：")
print(response1["response"])
response2=chain.invoke({"input":"说一个他代表作的名字"})
print("\n第二个问题的回复：")
print(response2["response"])

