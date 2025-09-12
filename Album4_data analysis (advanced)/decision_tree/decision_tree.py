#项目目标是利用决策树模型，预测员工是否会离职
#以下是一个简单的决策树模型示范
"""import pandas as pd
df=pd.read_csv("/Users/xiaoxiao/Downloads/sample/员工离职数据样本.csv")
from sklearn.tree import DecisionTreeClassifier
#读取自变量和因变量的数据
x=df[["工资(k)","满意度"]]
y=df[["离职"]]
#初始化并训练模型
model=DecisionTreeClassifier(max_depth=2,random_state=1)
model.fit(x,y)
#进行分类预测
y_pre=model.predict([[8,6]])
print(y_pre)"""

import pandas as pd
df=pd.read_csv("/Users/xiaoxiao/Downloads/e_information/员工信息表.csv")
df["工资"]=df["工资"].replace({"低":0,"中":1,"高":2})
x=df.drop(columns="离职") #df本身是二维结构，删除一列还是二维结构
y=df[["离职"]]
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=123) #防止过拟合
#模型初始化和训练
from sklearn.tree import DecisionTreeClassifier
model=DecisionTreeClassifier(max_depth=3,random_state=123)
model.fit(x_train,y_train)
#预测是否离职
y_pred=model.predict(x_test)
print(y_pred[0:10])
y_test_10=y_test.values[0:10]
print(y_test_10[:,0]) #输出第一列内容
#接下来查看分类准确率
from sklearn.metrics import accuracy_score
score=accuracy_score(y_pred,y_test,normalize=True)
print(score)
#预测是否离职的概率
y_pred_proba=model.predict_proba(x_test)
print(y_pred_proba[0:10]) #读取前10行
print(y_pred_proba[:,1]) #读取第2列，即离职概率
#接下来对模型进行更细致的评估和优化
#关注命中率和误判率
from sklearn.metrics import roc_curve
fpr,tpr,thres=roc_curve(y_test,y_pred_proba[:,1])
print(fpr,tpr,thres) #预测离职概率大于等于阈值，才能被判定为离职
#绘制ROC曲线
import matplotlib.pyplot as plt
plt.plot(fpr,tpr) #不要搞混横纵坐标
plt.title("ROC")
plt.xlabel("FPR")
plt.ylabel("TPR")
plt.show() #ROC曲线越陡峭，模型越好
#使用AUC值衡量模型的优劣
from sklearn.metrics import roc_auc_score
auc_score=roc_auc_score(y_test,y_pred_proba[:,1])
print(auc_score)
#进行参数调优(在训练集中使用K折交叉验证，来评估模型)
from sklearn.model_selection import cross_val_score
auc_score=cross_val_score(model,x_train,y_train,scoring="roc_auc",cv=5)
print(auc_score)
print(auc_score.mean())
#利用GridSearch进行参数调优（穷举法）
from sklearn.model_selection import GridSearchCV
parameters={"max_depth":[1,3,5,7,9]}
grid_search=GridSearchCV(model,parameters,scoring="roc_auc",cv=5)
grid_search.fit(x_train,y_train)
best_params=grid_search.best_params_
print(best_params)
#接着可以将最优值代入到最初的模型中，观察效果是否提升，也可遍历所有待选参数搭建模型，观察最优值是不是效果最好的








