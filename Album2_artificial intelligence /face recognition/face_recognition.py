from aip import AipFace
from PIL import Image
from PIL import ImageDraw

app_ID="6566745"
api_key="iftF3atJavrNo8gBdlMs3VZN"
secret_key="H6gl9JaN8T9gzgCpXpiuXAhVIWxgD73K"
client=AipFace(app_ID,api_key,secret_key)

#将图片转换为字符串
import base64
img_path="/Users/xiaoxiao/Downloads/口罩.png"
with open(img_path,"rb") as file:
    res=file.read()
    img=base64.b64encode(res)
    img=str(img,"utf-8") #得到字符串格式的图片
img_type="BASE64"
#利用options配置更多样化的功能
options={"max_face_num":10,"face_field":"quality,age"}
ret_data=client.detect(img,img_type,options) #利用接口进行检测

#将该图片创建为画布
with Image.open(img_path) as img:
    img_cp=img.copy() #创建一个备份
draw_img=ImageDraw.Draw(img_cp)
#在图片上添加文字的准备
from PIL import ImageFont

#接下来分析检测结果
if ret_data["error_msg"]=="SUCCESS": #注意大写
    print("识别到的人脸数量为：")
    print(ret_data["result"]["face_num"])
    print("检测到的面孔信息：")
    print(ret_data["result"]["face_list"])
    for face_msg in ret_data["result"]["face_list"]: #列表中每一个字典就是一个人的信息
        location=face_msg["location"]
        x1=location["left"]
        y1=location["top"]
        x2=x1+location["width"]
        y2=y1+location["height"]
        font_path="/System/Library/Fonts/Supplemental/Academy Engraved LET Fonts.ttf"
        font_size=location["height"]//5
        font=ImageFont.truetype(font_path,font_size)
        quality=face_msg["quality"]["occlusion"]
        if quality["nose"]>0.5 and quality["mouth"]>0.5: #如果被遮挡了
            color="green"
            text="with musk"
        else:
            color="red"
            text="no musk"

        draw_img.rectangle([x1,y1,x2,y2],outline=color,width=2) #框出面部区域
        draw_img.rectangle([x1,y2,x2,y2+font_size*2],fill=color) #绘制文字背景
        draw_img.text([x1,y2],text,"white",font)
        
    img_cp.save("/Users/xiaoxiao/Desktop/Draw.png") #注意保存的不是画布 是原始图片
else:
    print("检测失败")   
