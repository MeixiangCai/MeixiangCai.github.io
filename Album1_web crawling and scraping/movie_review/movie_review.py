import requests 
from bs4 import BeautifulSoup
import jieba
from pyecharts.charts import WordCloud

url="https://movie.douban.com/subject/34780991/?from=showing"
headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"}
response=requests.get(url,headers=headers)
html=response.text
soup=BeautifulSoup(html,"lxml")
content_all=soup.find_all(class_="short")
wordList=[]
for content in content_all:
    contentString=content.text
    words=jieba.lcut(contentString)
    wordList=wordList+words
wordDict={}
for word in wordList:
    if len(word)>1:
        if word not in wordDict:
            wordDict[word]= 1
        else:
            wordDict[word]=wordDict[word]+1
wd = WordCloud()
wd.add(series_name="",data_pair=list(wordDict.items()),width=800,height=500,word_size_range=[30,70])
wd.render("review.html")
print("success")
