#项目目标是将中文翻译成稀缺的小语种
from openai import OpenAI
client=OpenAI(
    api_key="security_code",
    base_url="https://api.deepseek.com"
)
msg=[
    {"role": "system","content": "你是一名Tagalog语翻译大师，将用户的中文翻译成Tagalog"},
    {"role": "user", "content": "谢谢！"}
]
response=client.chat.completions.create(
    model="deepseek-chat",
    messages=msg
    #max_token=
    #stop=[""]
    #temperature=
    #top_p=
    #frequency_penalty=
    #presence_penalty=
)
print(response.choices[0].message.content)

'''缓存命中：
pref_msg={"role":"system","content":""}
msg1=[pref_msg,{"role":"user","content":""}]
msg2=[pref_msg,]
msg2.append({"role": "user", "content": "什么是Python中的列表？"})
少量样本命中：
“请使用json格式输出“
response_format={"type":"json_object"}
import json
data=json.loads(data)
print(data)'''
