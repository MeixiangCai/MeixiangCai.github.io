#项目目标是利用K-Means算法，在对用户进行分类时，科学地将其分为K组，具有一定客观性
import pandas as pd
df=pd.read_csv("/Users/xiaoxiao/Downloads/user_info-2/new_user_info.csv")
#获取特征变量
x=df[["time_gap","order_count","total_amount"]]
print(x)
#对数据进行归一化，避免绝对值过大的数值对系统影响过大
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
x_scale=scaler.fit_transform(x)
print(x_scale)
x_scale=pd.DataFrame(x_scale,columns=x.columns,index=x.index) #转换为DataFrame更容易观察
print(x_scale)
#利用肘部法则寻找最佳的K值
"""#了解搭建K-Means模型
from sklearn.cluster import KMeans
model=KMeans(n_clusters=3,random_state=1)
model.fit(x_scale)
print(f"质心：{model.cluster_centers_}")
print(f"标签：{model.labels_}")
print(f"SSE：{model.inertia_}")"""

'''#开始利用肘部法则寻找最佳的K值
from sklearn.cluster import KMeans
sseList=[]
for K in range(1,10): #尝试9个K
    model=KMeans(n_clusters=K,random_state=1)
    model.fit(x_scale)
    sseList.append(model.inertia_) #获取每个K的簇内误差平方和，并加入到列表中
print(sseList)
#绘图直观地看出结果
import matplotlib.pyplot as plt
plt.plot(range(1,10),sseList,marker="o")
plt.show() #“肘部”为K=3'''

#因此将K值设为3，搭建模型
from sklearn.cluster import KMeans
model=KMeans(n_clusters=3,random_state=1)
model.fit(x_scale)
labels=model.labels_ #可以看出每个样本属于哪一类
print(labels)
#绘制3D散点图，展示三个指标的分布
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
plt.rcParams["font.sans-serif"] = "Arial Unicode MS"
fig=plt.figure(figsize=(12,8))
ax=fig.add_subplot(projection="3d") #创建3D坐标轴对象
color=["dodgerblue","seagreen","lightcoral"]
for i in range(0,3):
    d=x[labels==i] #回到归一化前的原始数据中，获取当前簇的全部样本点数据，这里的语法是布尔索引可以引用外部条件
    ax.scatter(d["time_gap"],d["order_count"],d["total_amount"],color=color[i],label=f"用户群体{i}")
ax.set_xlabel("R")
ax.set_ylabel("F")
ax.set_zlabel("M")
plt.legend()
plt.show() #清楚地观察到三个用户群体的特点








