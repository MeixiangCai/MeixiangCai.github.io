#项目目标是搭建多元回归线性模型，探究多个因素（自变量）对新增用户数（因变量）的影响并对未来数据作出预测
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("/Users/xiaoxiao/Downloads/mul/multiple_to_new.csv")
#绘制多变量散点图，确定相关系数
import seaborn as sns
sns.pairplot(df) #画出数据两两之间的特征图像
plt.show() #结果中只需关注因变量分别与几个自变量之间的关系即可
df=df.drop("date",axis=1) #因为日期列是字符串
corr=df.corr() #得出相关系数
#绘制相关系数热力图
sns.heatmap(corr,cmap="RdBu",square=True,annot=True)
plt.show() #相关性越高越蓝，越低越红，更直观地看出关联性，因此确定将"exposure", "hot", "search"作为自变量
#建立回归模型
#Y = a + bX1 + cX2 + dX3，需要确定三个系数和一个截距
x=df[["exposure","hot","search"]]
y=df[["new_user"]]
#模型的初始化和训练
from sklearn.linear_model import LinearRegression
lr_model=LinearRegression()
lr_model.fit(x,y)
b=lr_model.coef_[0][0].round(4)
c=lr_model.coef_[0][1].round(4)
d=lr_model.coef_[0][2].round(4)
a=lr_model.intercept_[0].round(2)
print(f"该线性回归模型为：Y={a}+{b}X1+{c}X2+{d}X3")
#检验回归模型
r2=lr_model.score(x,y)
print(r2) #结果显示精度很高
#使用模型进行预测
y_predict=lr_model.predict([[300000,10000,30000]])
print(y_predict)





