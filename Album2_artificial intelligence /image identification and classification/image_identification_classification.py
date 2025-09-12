from aip import AipImageClassify
"""
filePath="/Users/xiaoxiao/Documents/test.png" #先试验单张图片
with open(filePath,"rb") as f:
    image=f.read()
"""   

APP_ID="117946060"
API_KEY="aCandfpvvmBVcHGPDjj0wQnw"
SECRET_KEY="dlxrswLxp6g8piwMr2u3wtuEziFYWS4A"
client=AipImageClassify(APP_ID,API_KEY,SECRET_KEY)
"""
#试验下单张图片的步骤
ending=client.advancedGeneral(image)
value=ending["result"][0] #得到内层字典
classification=value["root"] #选择字典中root对应的值，就是分类结果
targetPath="/Users/img/"+value #目标文件夹路径
import os
if not os.path.exists(targetPath): #先判断目标文件夹是否已经存在
    os.mkdir(targetPath) #不存在的话，创建该文件夹
#将图像移动到目标文件夹中
import shutil
newPath=shutil.move(filePath,targetPath)    
"""
#批量处理:由图片路径获得分类，然后将分类结果作为文件夹名，将图片移动到该文件夹下
import os
imgroot="/Users/xiaoxiao/Documents/项目" #储存所有图片的文件夹
imglist=os.listdir(imgroot) #获取所有图片 返回一个列表
for imgname in imglist:
    if imgname[0]=="." or "." not in imgname:
        continue #排除掉系统文件或文件夹
    filePath=imgroot+"/"+imgname #获得单张图片的路径
    with open(filePath,"rb") as f:
        image=f.read()
    ending=client.advancedGeneral(image) #进行分类
    if "result" in ending: #不符合要求的图片不会返回result
        value=ending["result"][0].get("root","未分类") #root可能没有值 这样不会报错
        label=value.split("-")[0]
        targetPath=imgroot+"/"+label #生成文件夹名 之后从文件夹名就可以得知其中图片的分类
        if not os.path.exists(targetPath):
            os.mkdir(targetPath)
        import shutil
        newPath=shutil.move(filePath,targetPath) #移动图片到目标文件夹