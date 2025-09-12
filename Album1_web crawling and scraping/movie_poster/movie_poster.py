import requests
from bs4 import BeautifulSoup
for i in range(0,1):
    page=25*i
    url="https://movie.douban.com/top250?start="+str(page)+"&filter="
    headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"}
    response=requests.get(url,headers=headers)
    html=response.text
    soup=BeautifulSoup(html,"lxml")
    content_all=soup.find_all(class_="pic")
    for content in content_all:
        imgContent=content.find(name="img")
        imgName=imgContent.attrs["alt"]
        imgUrl=imgContent.attrs["src"]
        imgUrlHd=imgUrl.replace("s_radio_poster","m")
        imgResponse=requests.get(imgUrlHd)
        img=imgResponse.content
        with open(f"/Users/xiaoxiao/Desktop/MyImages/{imgName}.jpg","wb") as f:
            f.write(img)