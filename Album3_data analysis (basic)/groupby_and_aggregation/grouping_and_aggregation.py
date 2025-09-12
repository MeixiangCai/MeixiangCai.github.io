import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"]="Arial Unicode MS"
data=pd.read_csv("/Users/xiaoxiao/Downloads/yequ-6/商场营业额数据.csv")
data["date"]=pd.to_datetime(data["date"])
#按日期进行分组，然后求和再聚合
groupByDate=data.groupby(data["date"]).sum() #聚合时非数值数据会自动排除在外
print(groupByDate)
#绘制折线图来表示日期和总营业额的关系
plt.plot(groupByDate.index,groupByDate["turnover"])
plt.show()
#以月为单位更能反映趋势，进行重采样
print(groupByDate.index) #结果行索引已经是日期了
resampleData=groupByDate.resample("M").sum()
resampleData.index=resampleData.index.strftime("%Y年%m月")
plt.plot(resampleData.index,resampleData["turnover"])
plt.xticks(rotation=45)
plt.show()

#先按照业态分组，再分组聚合
data = data.set_index("date")
groupByCategory=data.groupby(data["category"]).resample("M").sum() #这里分组必须写在重采样前
#用子图直观展示结果
'''plt.subplot(2,2,1)
plt.subplot(2,2,2)
plt.subplot(2,2,3)
plt.subplot(2,2,4)'''
#选出第一层索引
enter = groupByCategory.loc["娱乐"] #得到的DataFrame结果中原本的第二层索引“日期”现在为第一层索引
service = groupByCategory.loc["服务"]
retail = groupByCategory.loc["零售"]
catering = groupByCategory.loc["餐饮"]
enter.index = enter.index.strftime("%Y/%m")
service.index = service.index.strftime("%Y/%m")
retail.index = retail.index.strftime("%Y/%m")
catering.index = catering.index.strftime("%Y/%m")
plt.subplot(2,2,1)
plt.bar(enter.index,enter["turnover"])
plt.xticks(rotation=90)
plt.title("娱乐")
plt.subplot(2,2,2)
plt.bar(service.index,service["turnover"])
plt.xticks(rotation=90)
plt.title("服务")
plt.subplot(2,2,3)
plt.bar(retail.index,retail["turnover"])
plt.xticks(rotation=90)
plt.title("零售")
plt.subplot(2,2,4)
plt.bar(catering.index,catering["turnover"])
plt.xticks(rotation=90)
plt.title("餐饮")

plt.tight_layout()
plt.show()

#绘制百分比堆积图
#重塑多层索引
groupByCategory=data.groupby(data["category"]).resample("M").sum()
print(groupByCategory.index)
groupByCategory=groupByCategory["turnover"].unstack("category") #把相应行索引变为最低级列索引，但是与数据的对应关系不变
print(groupByCategory)
sumTurnover=groupByCategory.sum(axis=1)
#apply()应用函数
def getPercentage(item):
    return item/sumTurnover
percentage=groupByCategory.apply(getPercentage)
#print(percentage) #返回一个DataFrame
percentage.index=percentage.index.strftime("%Y-%m")
#print(percentage)
percentage.plot.bar(stacked=True) #自动确定x轴、y轴内容
plt.show()