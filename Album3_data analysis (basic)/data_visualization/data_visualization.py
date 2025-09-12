import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"]="Arial Unicode MS" #设置中文字体
#创建画布
plt.figure(figsize=(4,3),facecolor="blue")
#展示图像
plt.show()
#绘制折线图
import pandas as pd
data=pd.read_csv("/Users/xiaoxiao/Downloads/yequ-4/书店每月销量数据.csv")
plt.rcParams["font.sans-serif"]="Arial Unicode MS"
plt.plot(data["month"],data["sum"],color="orange",marker="o",label="每月总销量")
plt.xlabel("月份")
plt.ylabel("销量")
plt.title("2019年8月至2020年7月书店每月销量走势")
plt.legend()
plt.show()
#绘制柱状图
data=pd.read_csv("/Users/xiaoxiao/Downloads/yequ-4/书店每月销量数据.csv")
plt.rcParams["font.sans-serif"]="Arial Unicode MS"
plt.bar(data["month"],data["sum"],width=0.6,color="orange",label="每月总销量")
plt.xlabel("月份")
plt.ylabel("销量")
plt.title("2019年8月至2020年7月书店每月销量走势")
plt.legend()
plt.show()
#绘制散点图
data=pd.read_csv("/Users/xiaoxiao/Downloads/yequ-5/书店图书销量和广告费用.csv")
plt.scatter(data["ads_fee"],data["sales"],color="green")
plt.show()
#绘制双y轴叠加图
data=pd.read_csv("/Users/xiaoxiao/Downloads/yequ-5/每月曝光量和转化率.csv")
plt.bar(data["month"],data["exposure"],color="skyblue",label="PV")
plt.xlabel("月份")
plt.ylabel("曝光量")
plt.legend(loc="upper left") #防止两个图例重合在一起
plt.twinx() #表示在原有X轴上再添加一条Y轴
plt.plot(data["month"],data["CVR"],marker="o",label="CVR")
plt.ylabel("转化率")
plt.legend()
plt.show()
#绘制簇形柱状图
data=pd.read_csv("/Users/xiaoxiao/Downloads/yequ-5/书店每月销量数据.csv")
data.plot.bar("month",["first_floor","second_floor","third_floor"])#分别传入需要作为x轴和y轴的列索引即可
plt.xlabel("月份")
plt.ylabel("销量")
plt.title("2019年8月至2020年7月书店每月各楼层销量走势")
plt.show()
# 可以单独绘制一列的：data["first_floor"].plot.bar()
plt.show()
#绘制百分比堆积柱状图
data=pd.read_csv("/Users/xiaoxiao/Downloads/yequ-5/书店每月销量数据百分比.csv")
data.plot.bar("month",["一楼","二楼","三楼"],stacked=True)
plt.xlabel("月份")
plt.ylabel("占比")
plt.title("2019年8月至2020年7月书店每月销量占比")
plt.show()
#绘制并列子图 新建一个图形
plt.figure(figsize=(10,8))
data=pd.read_csv("/Users/xiaoxiao/Downloads/yequ-5/书店每月销量数据.csv")
plt.subplot(2,1,1) #传入的分别是行数 列数 选择序号
plt.plot(data["month"],data["sum"])
plt.xticks(rotation=90) #旋转横坐标刻度
plt.subplot(2,1,2)
data.plot.bar("month",["first_floor","second_floor","third_floor"],ax=plt.gca())#用到pandas模块中的函数
plt.tight_layout() #调整子图布局
plt.show()