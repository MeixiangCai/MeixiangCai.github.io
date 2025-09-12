#对某网站视频会员购买记录进行数据清洗
import pandas as pd
df=pd.read_csv("/Users/xiaoxiao/Downloads/clean/视频会员订单数据源.csv")
#把price单位从分转为元
df["price"]=df["price"]/100
#把创建和支付之间转为时间格式
df["create_time"]=pd.to_datetime(df["create_time"])
df["pay_time"]=pd.to_datetime(df["pay_time"])
df.info() #发现platform和payment_provider有缺失值
print(df["payment_provider"].isnull()) #筛选出缺失值所在的行
print(df[df["payment_provider"].isnull()==True]) #输出更直观的结果
#接下来删除缺失值的行或者是补全
'''dfPayNull=df[df["payment_provider"].isnull()] #筛选出缺失值的行
df.drop(index=dfPayNull.index,inplace=True)
dfPlatNull=df[df["platform"].isnull()]
df.drop(index=dfPlatNull.index,inplace=True)
df.info()'''

#接下来对缺失值进行填充
df["payment_provider"].fillna("wxpay",inplace=True)
df["platform"].fillna("unknown",inplace=True)

#判断异常值
print(df[df["user_id"]>0]) #判断数值大小
print(~df["price"].isin([25.00,68.00,248.00])) #判断是否存在
dfWrongPrice=df[~df["price"].isin([25.00,68.00,248.00])]
print(dfWrongPrice)
df.drop(index=dfWrongPrice.index,inplace=True)
dfWrongPlat=df[~df["platform"].isin(["ios","android"])]
print(dfWrongPlat)
dfWrongPay = df[~df['payment_provider'].isin(["wxpay","alipay","applepay"])]
print(dfWrongPay)
dfWrongTime = df[df['pay_time'] < df['create_time']]
df.drop(index=dfWrongTime.index,inplace=True)

#判断重复值
dfOrderDu=df[df["order_id"].duplicated()]
print(dfOrderDu)
df.drop(index=dfOrderDu.index,inplace=True)
df.info() #一定要按顺序进行数据清洗，至此每一列都是78036行数据




