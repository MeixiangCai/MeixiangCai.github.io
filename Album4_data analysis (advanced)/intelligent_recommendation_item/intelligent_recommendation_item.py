#项目目标是基于物品协同过滤，为目标用户推荐他最有可能感兴趣的电影
import pandas as pd
ratings=pd.read_csv("/Users/xiaoxiao/Downloads/movie-4/ratings.csv")
movies=pd.read_csv("/Users/xiaoxiao/Downloads/movie-4/movies.csv")
result=pd.merge(ratings,movies) #拼接数据表
#print(result)
#构建用户-物品数据透视表，注意pearson计算的是列与列之间的相关性，所以列索引为电影
user_movie=result.pivot_table(index="用户id",columns="电影名",values="评分")
#计算每两部电影之间的pearson
corrMatrix=user_movie.corr(method="pearson") #结果是基于全部用户的喜好
#print(corrMatrix)
#目标用户为1
user1Ratings=user_movie.loc[1].dropna() #结果为1行多列
print(user1Ratings)
name=user1Ratings.index
score=user1Ratings.values
#获取用户1评分过的电影与他未评分电影之间的相关系数
simsMovie=corrMatrix[name].drop(index=name) #先选中矩阵中的列索引，再去掉评分过的行索引
prod=score*simsMovie #score为用户对某电影的评分*simsMovie与其他电影的相关性，得出用户对其他电影感兴趣程度
movieList=prod.sum(axis=1) #水平相加，是用户对某未评分电影的总感兴趣程度
#对结果进行排序
movieList=movieList.sort_values(ascending=False)
movieList=movieList.index[0:5] #取前5行
movieList=movieList.values
print(movieList)





