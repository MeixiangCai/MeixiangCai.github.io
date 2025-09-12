import pandas as pd
import matplotlib.pyplot as plt
df2019=pd.read_csv("/Users/xiaoxiao/Downloads/Lily旗舰店的后台数据/2019年下半年订单表.csv")
df2020=pd.read_csv("/Users/xiaoxiao/Downloads/Lily旗舰店的后台数据/2020年上半年订单表.csv")
#合并两个相同结构的数据集
dfYear=pd.concat([df2019,df2020])
#用分组聚合的方式先将商品销量按月度呈现
dfYear["下单时间"]=pd.to_datetime(dfYear["下单时间"])
dfnewYear=dfYear.set_index("下单时间")
dfSales=dfnewYear["数量"].groupby(dfnewYear["商品ID"]).resample("M").sum()
dfnewSales=dfSales.reset_index()
print(dfnewSales)
#统一所有数据的格式
dfnewSales["下单时间"]=dfnewSales["下单时间"].dt.strftime("%Y-%m")
#接下来合并，记得指出关联列
dfEV= pd.read_csv("/Users/xiaoxiao/Downloads/Lily旗舰店的后台数据/Exposure.csv")
dfTotal = pd.merge(dfEV, dfnewSales, left_on=["ID","Month"],right_on = ["商品ID", "下单时间"])
dfTotal["购买转化率"]=dfTotal["数量"]/dfTotal["Exposure"]
print(dfTotal)
plt.rcParams["font.sans-serif"] = "Arial Unicode MS"
#绘制6个商品的双Y轴叠加图
plt.subplot(2,3,1)
df1=dfTotal[dfTotal["ID"]==700010]
plt.bar(df1["Month"],df1["Exposure"],color="red",label="PV")
plt.xticks(rotation=90)
plt.ylim(0,500000) #统一设置纵坐标范围 才能更直观比较
plt.legend(loc="upper left")
plt.twinx()
plt.plot(df1["Month"],df1["购买转化率"].round(2),marker="o",label="转化率")
plt.ylim(0,0.3)
plt.legend()
plt.title(700010)

#画出第二至六个商品
plt.subplot(2,3,2)
df2=dfTotal[dfTotal["ID"]==700011]
plt.bar(df2["Month"],df2["Exposure"],color="r",label = "PV")
plt.xticks(rotation=90)
plt.ylim(0,500000)
plt.legend(loc="upper left")
plt.twinx()
plt.plot(df2["Month"],df2["购买转化率"].round(2),marker="o",label = "转化率")
plt.ylim(0,0.3)
plt.legend()
plt.title(700011)
plt.subplot(2,3,3)
df3=dfTotal[dfTotal["ID"]==700012]
plt.bar(df3["Month"],df3["Exposure"],color="r",label = "PV")
plt.xticks(rotation=90)
plt.ylim(0,500000)
plt.legend(loc="upper left")
plt.twinx()
plt.plot(df3["Month"],df3["购买转化率"].round(2),marker="o",label = "转化率")
plt.ylim(0,0.3)
plt.legend()
plt.title(700012)
plt.subplot(2,3,4)
df4=dfTotal[dfTotal["ID"]==700013]
plt.bar(df4["Month"],df4["Exposure"],color="r",label = "PV")
plt.xticks(rotation=90)
plt.ylim(0,500000)
plt.legend(loc="upper left")
plt.twinx()
plt.plot(df4["Month"],df4["购买转化率"].round(2),marker="o",label = "转化率")
plt.ylim(0,0.3)
plt.legend()
plt.title(700013)
plt.subplot(2,3,5)
df5=dfTotal[dfTotal["ID"]==700014]
plt.bar(df5["Month"],df5["Exposure"],color="r",label = "PV")
plt.xticks(rotation=90)
plt.ylim(0,500000)
plt.legend(loc="upper left")
plt.twinx()
plt.plot(df5["Month"],df5["购买转化率"].round(2),marker="o",label = "转化率")
plt.ylim(0,0.3)
plt.legend()
plt.title(700014)
plt.subplot(2,3,6)
df6=dfTotal[dfTotal["ID"]==700015]
plt.bar(df6["Month"],df6["Exposure"],color="r",label = "PV")
plt.xticks(rotation=90)
plt.ylim(0,500000)
plt.legend(loc="upper left")
plt.twinx()
plt.plot(df6["Month"],df6["购买转化率"].round(2),marker="o",label = "转化率")
plt.ylim(0,0.3)
plt.legend()
plt.title(700015)

plt.tight_layout()
plt.show()



