#项目目标是利用双均线策略搭建量化交易模型，比均线策略的时效性更好
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import date2num
from mplfinance import original_flavor as mpf
plt.rcParams["font.sans-serif"] = ["Arial Unicode MS"]
df=pd.read_csv("/Users/xiaoxiao/Downloads/strategy/stock_data.csv",usecols=["date", "open", "close", "high", "low"],dtype={"date": object})
df["date"]=pd.to_datetime(df["date"])
df["time"]=date2num(df["date"])
#绘制K线图
fig=plt.figure()
ax=plt.subplot(1,1,1)
ax.xaxis_date()
arr=df[["time", "open", "close", "high", "low"]].values
mpf.candlestick_ochl(ax,arr,colorup="red",colordown="green")
#plt.show()
#绘制双均线图
df["ma5"]=df["close"].rolling(5).mean()
df["ma30"]=df["close"].rolling(30).mean()
plt.plot(df["date"],df["ma5"],color="green",label="5日均线")
plt.plot(df["date"],df["ma30"],color="red",label="30日均线")
ax.set_ylabel("收盘价（元）")
ax.legend()
plt.title("双均线效果图")
plt.show()
#通过交易回测验证策略的有效性
#寻找金叉（短期上穿长期）和死叉（短期下穿长期）
golden_cross=[]
death_cross=[]
for i in range(1,len(df)): #遍历所有日期
    if df["ma5"][i]>df["ma30"][i] and df["ma5"][i-1]<df["ma30"][i-1]:
        golden_cross.append(df["date"][i])
    if df["ma5"][i]<df["ma30"][i] and df["ma5"][i-1]>df["ma30"][i-1]:
        death_cross.append(df["date"][i])
#设置金叉和死叉的Series并且排序
S1=pd.Series(1,index=golden_cross) #值全部设为1
S2=pd.Series(0,index=death_cross) #值全部设为0
sr=pd.concat([S1,S2]).sort_index() #默认纵向拼接，后按照日期升序排序
#使用10万本金模拟炒股，计算收益率
first_money=100000
money=first_money #交易余额
hold=0 #持有多少股
#获取金叉、死叉日期的开盘价
for i in range(0,len(sr)):
    p=df[df["date"]==sr.index[i]]["open"].values[0] #开盘价
    if sr.iloc[i]==1:
        buy=(money//(100*p)) #计算能买多少手
        hold+=buy*100 #持有多少股
        money-=buy*100*p
    else:
        money+=hold*p
        hold=0
#所有买入卖出交易全部结束后
p=df["open"].values[-1] #列表里最后一个开盘价
now_money=hold*p+money
print(now_money-first_money)


