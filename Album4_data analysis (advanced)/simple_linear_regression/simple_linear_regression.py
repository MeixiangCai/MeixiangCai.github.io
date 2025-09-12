#项目目标是探究广告曝光量与新增用户之间的关系，建立一元线性回归模型，对未知数据进行预测
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = "Arial Unicode MS"
df=pd.read_csv("/Users/xiaoxiao/Downloads/ad/exposure_to_new.csv")
r=df["exposure"].corr(df["new_user"]) #计算这两列的相关性
#建立线性回归模型
from sklearn.linear_model import LinearRegression
#初始化模型
lr=LinearRegression()
#开始训练模型，也就是寻找参数
x=df[["exposure"]] #必须以二维结构读取自变量
y=df[["new_user"]]
lr.fit(x,y)
#训练后，查看模型的系数和截距
b=lr.coef_[0][0] #因为系数b是二维结构
a=lr.intercept_[0] #因为截距a是一维结构
print(f"该线性回归模型为：Y={a}+{b}*X")
#开始检验该回归模型
#先用肉眼观察散点图和折线图的重叠程度
plt.scatter(df["exposure"],df["new_user"],label="原始数据")
plt.plot(df["exposure"],b*df["exposure"]+a,color="orange",label="线性回归模型")
plt.xlabel("曝光量")
plt.ylabel("新增用户量")
plt.legend()
plt.show()
#肉眼观察，效果不错，但也可以对模型进行打分，得到判定系数
r2=lr.score(x,y)
print(r2)
#利用模型预测未知数据
y_predict=lr.predict([[200000],[250000],[300000]]) #传入的自变量必须是二维结构
print(y_predict)

