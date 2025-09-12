#基于用户协同推荐，为用户智能推荐电影，也就是推荐他最可能感兴趣的电影
import pandas as pd
ratings=pd.read_csv("/Users/xiaoxiao/Downloads/movie/ratings.csv",sep="::",header=None,names=["用户id","电影id","评分","评分时间"],usecols=["用户id","电影id","评分"]) 
#上面读取时还设置了分隔符号，列索引名称以及引用了指定列，由于操作过多，接下来先保存一下
ratings.to_csv("/Users/xiaoxiao/Downloads/movie/ratings.csv",index=False)
movies=pd.read_csv("/Users/xiaoxiao/Downloads/movie/movies.csv",usecols=["电影id","电影名"]) #也是只读取了指定列
movies.to_csv("/Users/xiaoxiao/Downloads/movie/movies.csv",index=False)
#两个表合并起来
movieRatings=pd.merge(ratings,movies) #因为只有一个共同列索引，所以不用特别设置
#数据处理已完成，接下来开始搭建模型
print(movieRatings)

#基于用户的协同过滤算法，本质上是在找相似的用户
#构造物品-用户数据透视表可以直接构造行索引为电影名，列索引为用户，值为电影评分的列表
userRatings=movieRatings.pivot_table(index="电影名",columns="用户id",values="评分")
print(userRatings)
#接下来通过计算皮尔逊相关系数来分析用户间的喜好相似程度
userMatrix=userRatings.corr(method="pearson",min_periods=10)
userCorr=userMatrix[1].drop(index=1) #获取列索引为数值1的用户与其他用户的喜好相似程度
mostCorrUser=userCorr.idxmax() #获取最大值对应的行索引，得到最相似用户
#回到数据透视表，获取相似用户评分过的所有电影
targetMovie=userRatings[mostCorrUser]
print(targetMovie)
targetMovie=targetMovie[targetMovie.values==5]
print(targetMovie)
#获取目标用户自己评分过的所有电影
user1Ratings=userRatings[1].dropna() #删除空值
print(user1Ratings)
#将targetMovie中目标用户评分过的电影删掉
targetName=targetMovie.index
user1Name=user1Ratings.index
movieList=targetName[~targetName.isin(user1Name)] #targetMovie中目标用户没看过的
print(movieList.values)















