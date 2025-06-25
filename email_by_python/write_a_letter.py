import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
qqMail = smtplib.SMTP_SSL("smtp.qq.com",465)
mailName = "1140400521@qq.com"
mailPass = "llqirnyaxjcghehh"
qqMail.login(mailName,mailPass)
sender = "1140400521@qq.com"
receiver = "yequbiancheng@baicizhan.com"
message = MIMEMultipart()
message["Subject"] = Header("写给夜曲的一封信")
message["From"] = Header(f"mandy<{sender}>")
message["To"] = Header(f"yequbiancheng<{receiver}>")
textContent = "夜曲编程非常适合新手入门，我非常喜欢～感谢课程开发"
mailContent = MIMEText(textContent,"plain","utf-8")
filePath = "/Users/xiaoxiao/Desktop/成绩.png"
with open(filePath,"rb") as imageFile:
    fileContent = imageFile.read()
attachment = MIMEImage(fileContent)
attachment.add_header("Content-Disposition","attachment",filename="成绩.png")
qqMail.sendmail(sender,receiver,message.as_string())