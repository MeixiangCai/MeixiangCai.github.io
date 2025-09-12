#项目目标是提取出商品评价中的关键词，并自动判断正负性
#提前下载好的csv文件的路径为 /Users/xiaoxiao/Downloads/yequ/TVComments.csv
import csv
import jieba
file=open ("/Users/xiaoxiao/Downloads/yequ/TVComments.csv","r")
reader=csv.reader(file)
data=[] #为了标准化处理，将reader中一行一行的列表都整合到一个大列表中，方便后面通过遍历来操作
for info in reader:
    data.append(info)
word=[]   #构造词袋模型需要字符串列表
for row in data:
    text=row[0]
    ret=jieba.lcut(text) #分词后返回的是一个列表
    ret=" ".join(ret) #将字符串以空格连接，join()将可迭代对象（如列表、元组、集合等）中的字符串元素，使用指定的分隔符连接起来，形成一个新的字符串
    word.append(ret) #至此，获得字符串的列表
from sklearn.feature_extraction.text import CountVectorizer #开始构造词袋模型
# vect=CountVectorizer(max_features=15) #统计整个列表中，出现频率最高的15个词
# keywords=vect.get_feature_names_out() #查看出现频率最高的15个词
vect=CountVectorizer() #需要统计所有出现的词，不只是最高频词
X=vect.fit_transform(word) #利用该函数构造出词袋模型 （0，0）1  第一个0表示索引的列，第二个0表示出现的高频词编号，1表示出现次数
X=X.toarray() #将X转换为二维数组
y=[] #用于存储标签
for allInfo in data:
    label=allInfo[1]
    y.append(label)
# 文本特征和标签准备完毕，开始训练数据
from sklearn.model_selection import train_test_split
result=train_test_split(X,y,train_size=0.8,random_state=1)
# 训练完 提取其中的数据
train_feature=result[0]
test_feature=result[1]
train_label=result[2]
test_label=result[3]
# 开始搭建分类器
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
mlp=MLPClassifier()
mlp.fit(train_feature, train_label) #训练分类器
test_pred=mlp.predict(test_feature) #对测试集数据进行预测 分类器已经可以拿来预测了
score=accuracy_score(test_pred,test_label) #得出准确率
# print(score)

#自定义一条评论，开始测试
comment="太差了，新电视买回家不到十多天，底座支架因质量问题断裂，电视直接从桌子上摔坏！"
comment=jieba.lcut(comment)
comment=[" ".join(comment)] #需要获得字符串列表，所以外面加上了中括号
try_feature=vect.transform(comment) #构造词袋模型
try_feature=try_feature.toarray() #将结果变成Numpy数组
try_pred=mlp.predict(try_feature) #调用分类器
print(try_pred)
