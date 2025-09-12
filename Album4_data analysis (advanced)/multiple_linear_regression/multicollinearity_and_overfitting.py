#项目目标是解决多重线性回归中，实际情况中会遇到的多重共线性和过拟合问题
import pandas as pd 
df = pd.read_csv("/Users/xiaoxiao/Downloads/mul/multiple_to_new.csv")
#判断不同自变量之间的线性关系
x=df[["exposure","hot","search"]]
y=df[["new_user"]]
print(x.corr()) #发现hot和search高度相关
#使用方差膨胀系数法（VIF检验）来更严谨地确定不同自变量会不会相互影响
from statsmodels.stats.outliers_influence import variance_inflation_factor
vif=[variance_inflation_factor(x.values,x.columns.get_loc(i)) for i in x.columns]
#vif中传入的第一个参数必须是数据，第二个是要算第几列
print(vif) #hot,search有严重的多重线性问题
#先来处理过拟合问题（与内部数据过于拟合，但与外部数据拟合度不够）
#划分训练集和测试集
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=1)
lr_model=LinearRegression()
lr_model.fit(x_train,y_train)
r2=lr_model.score(x_test,y_test) #测试集派上用场
print(r2) #检验模型的精准度
b=lr_model.coef_[0][0].round(4)
c=lr_model.coef_[0][1].round(4)
d=lr_model.coef_[0][2].round(4)
a=lr_model.intercept_[0].round(2)
print(f"线性回归模型为：Y={a}+{b}X1+{c}X2+{d}X3")
#接着处理多重共线性问题，运用的方法是手动移除自变量
#尝试移除hot或search，分别看看效果
"""x=x.drop(columns="hot")
vif = [variance_inflation_factor(x.values, x.columns.get_loc(i)) for i in x.columns]
print(vif)"""
"""x=x.drop(columns="search")
vif = [variance_inflation_factor(x.values, x.columns.get_loc(i)) for i in x.columns]
print(vif)"""
#继续探究各自的最终效果
for i in ["hot","search"]:
    xi=x.drop(columns=i)
    from sklearn.model_selection import train_test_split
    x_train,x_test,y_train,y_test=train_test_split(xi,y,test_size=0.2,random_state=1)
    from sklearn.linear_model import LinearRegression
    lr_model=LinearRegression()
    lr_model.fit(x_train,y_train)
    print(lr_model.score(x_test,y_test))#最后发现不管移除哪一个，判定系数都不会发生大的变化，接下来看移除后截距的变化
    b = lr_model.coef_[0][0].round(4)
    c = lr_model.coef_[0][1].round(4)
    a = lr_model.intercept_[0].round(2)
    print(f"自变量为{xi.columns.values}时：")
    print(f"对应的线性回归模型为：Y={a}+{b}X1+{c}X2")
#原始数据，截距异常，删掉hot,截距正常，删掉search，截距异常，说明search对模型影响较大，贸然删掉会使模型失真















