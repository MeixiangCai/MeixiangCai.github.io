#项目目标是创建NLP客户端，利用百度AIP直接判断文本情感的正负面
from aip import AipNlp
APP_ID = "6554639"
API_KEY = "UQ0S8DKg0NQf38X9citAxd57"
SECRET_KEY = "dJqw5xEakUAyqcTRHRv91bMqvyCqwJgS"
client=AipNlp(APP_ID,API_KEY,SECRET_KEY)
text="他这个人真是太下头了"
result=client.sentimentClassify(text)
# print(result)
ret=result["items"][0] #得到一个字典
sentiment=ret["sentiment"]
confidence=ret["confidence"]
confidence=round(confidence,4)
print(f"评价内容：{text}")
if sentiment==0:
    print(f"该条评论有{confidence*100}%的可能性为负面评价。")
elif sentiment==1:
    print(f"该条评论有{confidence*100}%的可能性为中性评价。")
else:
    print(f"该条评论有{confidence*100}%的可能性为正面评价。")
    
