#项目目标是利用布林带策略搭建量化交易模型，避免了（双）均线策略的滞后性
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
#绘制布林带策略
'''df["mid"]=df["close"].rolling(window=20).mean() #中心线为收盘价的20日均线
#绘制中心线
plt.plot(df["date"],df["mid"],color="yellow",label="中心线")
df["std"]=df["close"].rolling(window=20).std() #20日的标准差
df["up"]=df["mid"]+2*df["std"] #阻力线
#绘制上阻力线
plt.plot(df["date"],df["up"],color="green",label="上阻力线")
df["down"]=df["mid"]-2*df["std"] #支撑线
#绘制下支撑线
plt.plot(df["date"],df["down"],color="red",label="下支撑线")
ax.set_ylabel("收盘价（元）")
ax.legend()
plt.title("布林带通道效果图")
plt.show()
#进行布林带策略的交易回测
sr1=df["open"]>df["up"] #开盘价突破上阻力线时要卖出
sr2=df["open"]<df["down"] #开盘价低于下支撑线时要买入
sale_signal=df["date"][sr1] #布尔索引，存储日期
buy_signal=df["date"][sr2]
#模拟本金为100000，计算收益率
first_money=100000
money=first_money
hold=0
s1=pd.Series(1,index=buy_signal)
s2=pd.Series(0,index=sale_signal)
sr=pd.concat([s1,s2]).sort_index() #纵向合并并且排序
for i in range(0,len(sr)):
    p=df[df["date"]==sr.index[i]]["open"].values[0]
    if sr.iloc[i]==1:
        buy=(money//100*p) #一共能买多少手
        hold+=buy*100
        money-=buy*100*p
    else:
        money+=hold*p
        hold=0
p=df["open"].values[-1] #最后一天的开盘价
now_money=hold*p+money
profit=now_money-first_money
print(profit) #发现亏损，后续调整策略'''
#将标准差从2倍调整为3倍，让交易不那么频繁
#绘制布林带策略
df["mid"]=df["close"].rolling(window=20).mean() #中心线为收盘价的20日均线
#绘制中心线
plt.plot(df["date"],df["mid"],color="yellow",label="中心线")
df["std"]=df["close"].rolling(window=20).std() #20日的标准差
df["up"]=df["mid"]+3*df["std"] #阻力线
#绘制上阻力线
plt.plot(df["date"],df["up"],color="green",label="上阻力线")
df["down"]=df["mid"]-3*df["std"] #支撑线
#绘制下支撑线
plt.plot(df["date"],df["down"],color="red",label="下支撑线")
ax.set_ylabel("收盘价（元）")
ax.legend()
plt.title("布林带通道效果图")
plt.show()
#进行布林带策略的交易回测
sr1=df["open"]>df["up"] #开盘价突破上阻力线时要卖出
sr2=df["open"]<df["down"] #开盘价低于下支撑线时要买入
sale_signal=df["date"][sr1] #布尔索引，存储日期
buy_signal=df["date"][sr2]
#模拟本金为100000，计算收益率
first_money=100000
money=first_money
hold=0
s1=pd.Series(1,index=buy_signal)
s2=pd.Series(0,index=sale_signal)
sr=pd.concat([s1,s2]).sort_index() #纵向合并并且排序
for i in range(0,len(sr)):
    p=df[df["date"]==sr.index[i]]["open"].values[0]
    if sr.iloc[i]==1:
        buy=(money//100*p) #一共能买多少手
        hold+=buy*100
        money-=buy*100*p
    else:
        money+=hold*p
        hold=0
p=df["open"].values[-1] #最后一天的开盘价
now_money=hold*p+money
profit=now_money-first_money
print(profit)


