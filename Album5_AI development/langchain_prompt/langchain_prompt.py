#项目目标是利用Langchain框架，对诗句“浮世三千”进行扩写
#导入所需的库（新版langchain)
from langchain_openai import ChatOpenAI #能与AI模型进行通信
from langchain_core.messages import SystemMessage, HumanMessage # 构建聊天消息 # type: ignore
#创建客户端实例
client=ChatOpenAI(
    api_key="security_code",
    model="deepseek-chat",
    base_url="https://api.deepseek.com",
    temperature=0.1,
    max_tokens=1000
)
msg=[
    #设置系统消息
    SystemMessage(content="你是一位诗人，擅长写抒情诗。"),
    #设置用户消息
    HumanMessage(content="请帮我扩写这首诗：浮世三千")
]
#发送请求并获取回复
response=client.invoke(msg)
print(response.content)

#接下来利用PromptTemplate编写提示词模版，进行批量处理
from langchain_core.prompts import PromptTemplate # type: ignore
template="请用{style}风格，以“{poem}”为首扩写诗歌，不超过50个字。"
#将字符串模版转换为模版对象，不然模型不知道那是模版
prompt=PromptTemplate.from_template(template)
final_prompt=prompt.invoke({"style":"抒情诗","poem":"浮世三千"})
print(final_prompt)

#接下来利用ChatPromptTemplate尝试创建带角色的消息对象/提示词模版
from langchain_core.prompts import ChatPromptTemplate
system_template="你是一位诗人，擅长写{style}。"
human_template="请帮我扩写这首诗：{poem}，不超过50个字。"
chat_prompt=ChatPromptTemplate(
    [
        ("system",system_template),
        ("human",human_template)
    ]
)
final_chat_prompt=chat_prompt.invoke({"style":"抒情诗","poem":"浮世三千"})
print(final_chat_prompt)


