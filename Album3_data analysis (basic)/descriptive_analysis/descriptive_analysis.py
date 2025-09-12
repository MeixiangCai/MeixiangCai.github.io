import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("/Users/xiaoxiao/Downloads/housing/成都市房源信息.csv")
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
#计算均值
price_mean=df["单价价格(元/平方)"].mean()
area_mean=df["建筑面积(平方)"].mean()
#计算中位数
price_median=df["单价价格(元/平方)"].median()
area_median=df["建筑面积(平方)"].median()
#绘制直方图(可展示分布情况)
plt.hist(df["单价价格(元/平方)"],bins=100)
plt.show()
plt.hist(df["建筑面积(平方)"],bins=100)
plt.show()
#接下来进行离散趋势的描述
area_var=df["建筑面积(平方)"].var()
area_std=df["建筑面积(平方)"].std()

#描述函数
print(df["单价价格(元/平方)"].describe())
print(df.describe())
#将区域数据转为分类数据
df["所在区域"]=df["所在区域"].astype("category")
print(df["所在区域"].describe())
print(df["所在区域"].value_counts())