# 弹幕URL：https://comment.bilibili.com/{cid}.xml
import requests
from bs4 import BeautifulSoup
from pyecharts.charts import Line
url="https://comment.bilibili.com/28619574467.xml"
headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"}
response=requests.get(url,headers=headers)
response.encoding = response.apparent_encoding
xml=response.text

soup=BeautifulSoup(xml,"lxml")
content_all=soup.find_all(name="d")

timeList=[]
for comment in content_all:
    data=comment.attrs["p"]
    dataList=data.split(",")
    time=dataList[0]
    timeList.append(float(time))

subtitlesDict={}
for x in range(0,16):
    start=30*x+1
    end=30*(x+1)
    segment_range=f"{start}-{end}"
    subtitlesDict[segment_range]=0
for subtitle in subtitlesDict.keys():
    start_key=subtitle.split("-")[0]   
    end_key=subtitle.split("-")[1] 
    for item in timeList:
        if int(start_key)<=item<=int(end_key):
            subtitlesDict[subtitle]=subtitlesDict[subtitle]+1

line=Line()
line.add_xaxis(list(subtitlesDict.keys()))
line.add_yaxis("弹幕数",list(subtitlesDict.values()))
line.render("line.html")
print("success")




