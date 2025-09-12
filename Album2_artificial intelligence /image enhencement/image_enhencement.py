#通过网络请求API的方式对一张图片进行去雾处理
#获取第一个参数request_url
import requests

host='https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=cMy8m8Xb6lQ7CArG7sjTh91J&client_secret=jmWJkvW4dmBvMboUuLIsVOVQNizyWnQj'

response=requests.get(host)
if response:
    result=response.json()
access_token=result["access_token"]
print(access_token) #access_token相当于大厦钥匙

request_url="https://aip.baidubce.com/rest/2.0/image-process/v1/dehaze"
request_url=request_url+"?access_token=" + access_token #request_url相当于房间钥匙
print(request_url)

#获取第二个参数data
import base64
f=open("Users/xiaoxiao/Documents/haze.png","rb")
img=base64.b64encode(f.read()) #把图片转换为base64编码
params={"image":img}

#获取第三个参数headers
headers={"content_type":"application/x-www-form-urlencoded"}

#发送请求
response=requests.post(request_url,data=params,headers=headers)

#获取返回结果
if response:
    result=response.json()

#获取base64编码图片
img_str=result["image"]

#base编码转图片
img_data=base64.b64decode(img_str)

with open("/Users/xiaoxiao/Documents/dehaze.png","wb") as f:
    f.write(img_data)