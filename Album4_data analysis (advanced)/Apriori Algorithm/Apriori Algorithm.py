#项目目标是公众号排版时，头条和次条文章如何编排，能增加次条文章的阅读量
import pandas as pd
df=pd.read_csv("/Users/xiaoxiao/Downloads/user_data/用户浏览数据.csv")
articles=[]
for i in df["文章类型"]:
    article=i.split(",")
    articles.append(article)
from apyori import apriori
rules=apriori(articles,min_support=0.1,min_confidence=0.6) #articles必须是一个双重列表结构
#接下来提取信息并四舍五入和前后件连接
extract_result=[]
for rule in rules:
    #print(rule) 可输出查看结果结构
    support=round(rule.support,3) #提取该属性
    for i in rule.ordered_statistics:
        head_set=list(i.items_base)
        tail_set=list(i.items_add)
        if head_set==[]:
            continue
        #将前后件转化为字符串，再串起来
        related_category=str(head_set)+"→"+str(tail_set)
        confidence=round(i.confidence,3)
        lift=round(i.lift,3)
        #print(related_category,support,confidence,lift)
        extract_result.append([related_category,support,confidence,lift])
#将全部数据转换成DataFrame形式，并设置列名
rule_data=pd.DataFrame(extract_result,columns=["关联规则","支持度","置信度","提升度"])
print(rule_data)
#提取出促进/抑制作用的数据
promoted_rules=rule_data[rule_data["提升度"]>1]
restricted_rules=rule_data[rule_data["提升度"]<1]
print(promoted_rules,restricted_rules)
#绘制簇形柱状图，对数据进行可视化
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"]="Arial Unicode MS"
promoted_rules.plot.bar("关联规则",["支持度","置信度"],rot=0) #rot表示刻度值显示的角度
plt.title("促进关系的强关联规则")
plt.show() #至此可得出结论
#顺便观察抑制作用的关联规则
restricted_rules.plot.bar("关联规则",["支持度","置信度"],rot=0)
plt.title("抑制关系的强关联规则")
plt.show()





