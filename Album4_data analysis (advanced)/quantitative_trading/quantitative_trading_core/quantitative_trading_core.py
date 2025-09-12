#项目目标是制定量化交易的策略并且验证策略
import pandas as pd
df=pd.read_csv("/Users/xiaoxiao/Downloads/strategy/stock_data.csv",usecols=["date","close"]) #只获取日期和收盘价
df["date"]=pd.to_datetime(df["date"])
df.set_index(["date"],inplace=True)
ma10=df.rolling(window=10,min_periods=1).mean() #获取10日移动平均线
print(ma10)
#数据可视化，观察平均线与日期的关系
import matplotlib.pyplot as plt
plt.plot(df.index,df["close"],color="blue",label="df") #原始数据走向
plt.plot(ma10.index,ma10["close"],color="orange",label="ma10") #移动10日均线走向
plt.xticks(rotation=45)
plt.legend()
plt.xlabel("date")
plt.ylabel("close")
plt.rcParams["font.sans-serif"] = ["Arial Unicode MS"]
plt.title("证券收盘价和移动十日均线走势图")
plt.show()

#将收盘价与十日均线作比较
ma10_model=df["close"]>ma10["close"] #结果是一个布尔序列
print(ma10_model)
#制定交易策略函数，判断买卖点
def get_buy_date(w):
    return w[0]==False and w[1]==True #昨日低今天高，走势是上涨，需买入；自己定义的w是包含连续两日结果的序列
def get_sale_date(v):
    return v[0]==True and v[1]==False
#设定买入点
se_buy=ma10_model.rolling(window=2).apply(get_buy_date).fillna(0) #再次运用移动窗口，这次设为2,且将第一天的数据填充为0
#设定卖出点
se_sale=ma10_model.rolling(window=2).apply(get_sale_date).fillna(0)
#将买卖点可视化
#将数值转为布尔型数据
se_buy_bool=se_buy.astype(bool)
se_sale_bool=se_sale.astype(bool)
buy_price=df[se_buy_bool] #布尔索引可以引用外部数据
sale_price=df[se_sale_bool]
print(buy_price)
#绘制折线图和散点图
plt.plot(df.index,df["close"],color="blue",label="df") #原始数据走向
plt.plot(ma10.index,ma10["close"],color="orange",label="ma10") #移动十日走势
plt.scatter(buy_price.index,buy_price["close"],color="red",label="buy_price")
plt.scatter(sale_price.index,sale_price["close"],color="green",label="sale_price")
plt.xticks(rotation=45)
plt.legend()
plt.xlabel("date")
plt.ylabel("close")
plt.title("折线图和散点图叠加图")
plt.show()
#收益率测算
profit=sale_price.values-buy_price.values #一次交易的收益
profit_sum=profit.sum()
rate=profit_sum/buy_price.iloc[0].values
print(rate)


