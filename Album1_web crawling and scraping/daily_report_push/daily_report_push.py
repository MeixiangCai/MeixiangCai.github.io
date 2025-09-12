# 从马蜂窝上查看每日旅游攻略
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
# 只看美食店铺
title_list=[]
score_list=[]
review_list=[]
for page in range(1,11): #查看前10页的内容
    time.sleep(1) #查看完一页就停顿1秒
    url=f"https://www.mafengwo.cn/cy/10065/0-0-0-0-0-{page}.html"
    headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
             "cookie":"PHPSESSID=d1bqqg8aado25vp6aqsu29d8s2; mfw_uuid=67caa651-3ccd-648c-ca63-3e785f20c6be; oad_n=a%3A3%3A%7Bs%3A3%3A%22oid%22%3Bi%3A1029%3Bs%3A2%3A%22dm%22%3Bs%3A15%3A%22www.mafengwo.cn%22%3Bs%3A2%3A%22ft%22%3Bs%3A19%3A%222025-03-07+15%3A54%3A57%22%3B%7D; __mfwc=direct; uva=s%3A113%3A%22a%3A3%3A%7Bs%3A2%3A%22lt%22%3Bi%3A1741334103%3Bs%3A10%3A%22last_refer%22%3Bs%3A45%3A%22https%3A%2F%2Fwww.mafengwo.cn%2Fcy%2F10065%2Fgonglve.html%22%3Bs%3A5%3A%22rhost%22%3BN%3B%7D%22%3B; __mfwurd=a%3A3%3A%7Bs%3A6%3A%22f_time%22%3Bi%3A1741334103%3Bs%3A9%3A%22f_rdomain%22%3Bs%3A15%3A%22www.mafengwo.cn%22%3Bs%3A6%3A%22f_host%22%3Bs%3A3%3A%22www%22%3B%7D; __mfwuuid=67caa651-3ccd-648c-ca63-3e785f20c6be; __omc_chl=; __omc_r=; x-waf-captcha-referer=; __mfwb=fc829dc8100e.1.direct; __mfwa=1741334103269.20909.2.1741334103269.1741659216728; __mfwlv=1741659216; __mfwvn=2; __mfwlt=1741659216; bottom_ad_status=0; w_tsfp=ltvuV0MF2utBvS0Q7avvkUKsFDwhcDo4h0wpEaR0f5thQLErU5mB0IB/t8n0MXDZ6sxnvd7DsZoyJTLYCJI3dwMWFsXHcokZ2AiZl9AtjdgdBUQxEJ/dXFZJdbMk7DkSLXhCNxS00jA8eIUd379yilkMsyN1zap3TO14fstJ019E6KDQmI5uDW3HlFWQRzaLbjcMcuqPr6g18L5a5Tjd5g35LAp2Vu4R0UbD0CFKDSkm6ULtd+FZMxv8ds/6SqA="}
    res=requests.get(url,headers=headers)
    html=res.text
    soup=BeautifulSoup(html,"lxml")
    content_all=soup.find_all(class_="item clearfix")
    for content in content_all:
        content_grade=content.find(class_="grade")
        score=content_grade.em.string
        score_list.append(score)
        review=content_grade.p.em.string
        review_list.append(review)
        title=content.find(class_="title").h3.a.string
        title_list.append(title)
# 将数据写入Excel中
total={"名称":title_list,"评分":score_list,"点评数量":review_list} #确定行和列
info=pd.DataFrame(total)
writer=pd.ExcelWriter("/Users/xiaoxiao/Desktop/美食排行.xlsx") #打开Excel文档
info.to_excel(excel_writer=writer,sheet_name="北京美食")
writer._save()
# 获取附件表格后，开始自动发邮件
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
with open("/Users/xiaoxiao/Desktop/美食排行.xlsx","rb") as food_file: # 打开附件
    food_content=food_file.read() #读取文件内容
# 设置附件
att1=MIMEText(food_content,"base64","gb2312") #确定附件内容
att1["Content-Type"]="application/octet-stream" #规定文件类型
att1.add_header("Content-Disposition","attachment", filename="美食排行.xlsx") #在接收方的展示方法

message=MIMEMultipart()
message.attach(att1)


mailHost="smtp.qq.com"
mailUser="1140400521@qq.com"
mailPass="xagibcdamcoifiac"
mail_receiver="13508363537cai@gmail.com"

smtpObj=smtplib.SMTP_SSL(mailHost,465) #与外部服务器建立连接
smtpObj.login(mailUser,mailPass)


mail_content=MIMEText("你好呀！","plain","utf-8")
message["From"]=Header(f"mandy<{mailUser}>") #注意昵称不能包含中文
message["To"]=Header(f"Mandy Cai<{mail_receiver}>")
message["Subject"]=Header("北京美食攻略")

message.attach(mail_content)
smtpObj.sendmail(mailUser,mail_receiver,message.as_string())
print("邮件发送成功")




