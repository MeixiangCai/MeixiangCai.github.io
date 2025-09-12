from aip import AipOcr
App_ID="6573665"
Api_key="i3SOPXHJXSkbsao15aJyxwoQ"
Secret_key="FTMwi88ixCn23gjAvQ9bbfRrk8IIPNsQ"
client=AipOcr(App_ID,Api_key,Secret_key)
options={"detect_direction":"true"}

filePath="/Users/xiaoxiao/Desktop/截屏2025-03-10 上午11.40.47.png"
with open(filePath,"rb") as f:
    image=f.read() #因为不需要转换为字符串

result=client.basicAccurate(image,options)
ending=result["words_result"]
for word in ending:
    text=word["words"]
    with open("/Users/xiaoxiao/Desktop/test.txt","a") as fp:
        fp.write(text+"\n")
print("写入完成")