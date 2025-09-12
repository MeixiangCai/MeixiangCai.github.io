#项目目标是通过量化交易，相对客观理性地买入一支股票
#先获取股票数据
import tushare as ts
ts.set_token("301cd605135b9cda475038a277cb7036ad4512cec508dcc605300c71")
api=ts.pro_api() #调取接口
df=api.daily(ts_code="601398.SH",start_date="20180701",end_date="20180718") #获取该股票的每日行情
import pandas as pd
df.to_csv("/Users/xiaoxiao/Downloads/stock.csv")
#绘制K线图，了解历史涨跌情况
import matplotlib.pyplot as plt
from matplotlib.dates import date2num
from mplfinance import original_flavor as mpf
df=pd.read_csv("/Users/xiaoxiao/Downloads/stock.csv",usecols=["trade_date","open","close","high","low"],dtype={"trade_date":object})
df["trade_date"]=pd.to_datetime(df["trade_date"])
df["time"]=date2num(df["trade_date"])
plt.rcParams["font.sans-serif"]=["Arial Unicode MS"]
fig=plt.figure()
ax=plt.subplot(1,1,1) #设置子图
ax.xaxis_date() #设置x轴为时间格式
arr=df[["time","open","close","high","low"]].values
mpf.candlestick_ochl(ax,arr,colorup="red",colordown="green")
plt.title("K线图")
plt.show()
