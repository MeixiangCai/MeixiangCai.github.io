#项目目标是利用Langchain的输出解析器，输出特定格式和结构的内容，也就是指定AI输出的格式
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate #本项目使用新版langchain
from langchain_core.output_parsers import CommaSeparatedListOutputParser
#创建模型客户端
client=ChatOpenAI(
    api_key="security_code",
    model="deepseek-chat",
    base_url="https://api.deepseek.com"
)
#创建列表解析器并且获取给模型的格式指令
output_parser=CommaSeparatedListOutputParser()
format_instructions=output_parser.get_format_instructions()
print(format_instructions)
#创建提示词模版并且将格式指令加入提示词
prompt=PromptTemplate.from_template(
    template="请列举5个{subject}。\n{format_instructions}",
    partial_variables={"format_instructions":format_instructions} #给部分变量赋值
)
final_prompt=prompt.invoke({"subject":"诗人"})
response=client.invoke(final_prompt)
print(response.content)
#将原始回复解析为列表
parsed_response=output_parser.parse(response.content)
print(parsed_response)
