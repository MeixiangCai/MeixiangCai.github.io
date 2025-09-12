# 统计实习僧网站上“爬虫工程师“对应的城市和薪资和数量，用柱状图呈现不同城市的薪资平均值和职位数量，注意for循环得到某数据后退出该循环
import requests
from bs4 import BeautifulSoup
import time #信息敏感，设置停顿时间，应对反爬虫
from pyecharts.charts import Bar
#每个详情页都有一样的操作，所以我们定义一个函数，变量就是URL
def getPositionInfo(detail_url):
    res=requests.get(detail_url,headers=headers)
    html=res.text
    soup=BeautifulSoup(html,"lxml")
    job=soup.find(class_="new_job_name").text.strip()
    position=soup.find(class_="job_position").string.strip()
    company=soup.find(class_="com-name").string.strip()
    salary=soup.find(class_="job_money cutom_font").string
    with open("职位数据.txt","a") as f: #新建一个文件
        f.write(job+","+position+","+company+","+salary+"\n")
    with open("/Users/xiaoxiao/Desktop/yequbiancheng/职位数据.txt","r") as f: #打开文件 进行读取
        dataList=f.readlines()
    cityDict={} #因为一个城市会对应好几个平均薪资
    city_num_dict={} #为了统计不同城市的职位数量
    for data in dataList: #遍历每一行的数据，这一步非常关键
        if "薪资面议" in data:
            continue
        city=data.split(",")[1] #获取横坐标
        salary=data.split(",")[3] #获取纵坐标
        daily=salary.split("/")[0] #提取“/天”前面的内容
        start=daily.split("-")[0]
        end=daily.split("-")[1]
        average=(int(start)+int(end))/2
        if city not in cityDict:
            cityDict[city]=[]
        cityDict[city].append(average) #至此，键为城市，值为对应的薪资列表
    for key,value in cityDict.items(): #同时遍历键和值 注意不要放在刚才的循环下面
        average_value=sum(value)//len(value)
        cityDict[key]=average_value #对键重新赋值 不同城市对应的平均薪资出来了
        city_num_dict[key]=len(value) #不同城市对应的职位数量也出来了
    bar=Bar() #开始创建柱状图
    bar.add_xaxis(list(cityDict.keys()))
    bar.add_yaxis("各城市平均薪资",list(cityDict.values()))
    bar.render("各城市平均薪资.html")
    bar2=Bar()
    bar2.add_xaxis(list(city_num_dict.keys()))
    bar2.add_yaxis("各城市平均职位数量",list(city_num_dict.values()))
    bar2.render("各城市平均职位数量.html")

for i in range(1,3): #批量获取前两页的职位
    url=f"https://www.shixiseng.com/interns?page={i}&type=intern&keyword=%E7%88%AC%E8%99%AB%E5%B7%A5%E7%A8%8B%E5%B8%88&area=&months=&days=&degree=&official=&enterprise=&salary=-0&publishTime=&sortType=&city=%E5%85%A8%E5%9B%BD&internExtend="
    headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"}
    response=requests.get(url,headers=headers)
    html=response.text
    soup=BeautifulSoup(html,"lxml")
    titles=soup.find_all(class_="title ellipsis font")
    for item in titles:
        detail_url=item.attrs["href"] #获取职位详情页
        getPositionInfo(detail_url) #开始对详情页进行操作，获取所需信息

    time.sleep(2) #每获取一个详情页信息就停顿2秒
    
    


