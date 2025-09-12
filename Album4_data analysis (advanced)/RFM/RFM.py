#项目目标是对某电商店铺的用户进行分层，从而精准推出不同的策略
import pandas as pd
df=pd.read_csv("/Users/xiaoxiao/Downloads/user_info/user_info.csv")
#首先获取RFM数据
df["last_order_date"]=pd.to_datetime(df["last_order_date"])
#构建一个截止时间
from datetime import datetime
endTime=datetime(2019,4,1)
df["time_gap"]=endTime-df["last_order_date"]
df["time_gap"]=df["time_gap"].dt.days #提取整数型天数作为R
#接下来对数据进行描述性分析，从而使各个维度的5个区间分布的人数差不多
R=df["time_gap"].groupby(df["time_gap"]).count()
R_percent=R/51394
#更直观地展示比例分布
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = "Arial Unicode MS"
plt.bar(R_percent.index,R_percent.values)
plt.show()
#同样对F进行描述性分析
F=df["order_count"].groupby(df["order_count"]).count()
F_percent=F/51394
plt.bar(F_percent.index,F_percent.values)
plt.show()
#对M进行描述性分析但是用直方图呈现
plt.hist(df["total_amount"],bins=100)
plt.show()
#接下来进行数据分箱/分段/分组，将三个维度的数据等分到5个区间
#对R进行数值边界分箱

#df["R"]=pd.cut(df["time_gap"],[0,50,100,200,300,365])
#R_value=df["R"].value_counts() #统计各个区间的数量
#print(R_value) 结果显示分布还是非常不均匀，所以应该使用频率边界分箱

df["R"]=pd.qcut(df["time_gap"],q=5,labels=[5,4,3,2,1]) #q指的是分箱频率，需要均匀分成多少组，且可以直接转换成标签
R_value=df["R"].value_counts()
#对F M进行分组
df["F"]=pd.qcut(df["order_count"],q=5,labels=[1,2,3,4,5])
df["M"]=pd.qcut(df["total_amount"],q=5,labels=[1,2,3,4,5])
#对用户标记分层结果
def rfmTrans(x):
    if x>3:
        return 1
    else:
        return 0
df["R"]=df["R"].apply(rfmTrans)
df["F"]=df["F"].apply(rfmTrans)
df["M"]=df["M"].apply(rfmTrans)
#开始贴标签
df["mark"]=df["R"].astype(str)+df["F"].astype(str)+df["M"].astype(str)
def rfmType(x):
    if x=="111":
        return "高价值用户"
    elif x=="101":
        return "重点发展用户"
    elif x=="011":
        return "重点唤回用户"
    elif x=="001":
        return "重点潜力用户"
    elif x=="110":
        return "一般潜力用户"
    elif x=="100":
        return "一般发展用户"
    elif x=="010":
        return "一般维系用户"
    else:
        return "低价值用户"
df["customer_type"]=df["mark"].apply(rfmType)
print(df["customer_type"])
#可视化结果
df_type=df["customer_type"].groupby(df["customer_type"]).count()
print(df_type)
df_perc=df_type/51394
print(df_perc)
plt.bar(df_type.index,df_type.values,color="skyblue")
plt.xlabel("用户分层类别")
plt.ylabel("各层级用户总数")
plt.twinx()
plt.plot(df_perc.index,df_perc.values,marker="o",color="lightcoral")
plt.xlabel("用户分层类别")
plt.ylabel("各层级用户总数占比")
plt.show()




