#项目目标是对一段音频进行变声，将运用到语音识别和语音合成技术
#创建语音识别和语音合成客户端（合二为一）
from aip import AipSpeech
APP_ID = "118959844"
API_KEY = "zrj9MhC1oI2ifeLo01A4YbCE"
SECRET_KEY = "UAmp5krjpnPFoeWQsepD4LCAjTUmX2LG" 
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
client.setConnectionTimeoutInMillis(30000) 
client.setSocketTimeoutInMillis(60000)

#定义语音转文字函数
def audio2text(wav):
    rejson=client.asr(wav,"wav",16000,{"dev_pid":1537})
    print(rejson) #实时追踪可能运行失败的原因
    if rejson["err_no"]==0:
        msg=rejson["result"][0]
    else:
        msg="语音识别错误！"
    return msg

#对音频文件进行参数设置
from pydub import AudioSegment
AudioSegment.converter = "/opt/homebrew/bin/ffmpeg"
sound=AudioSegment.from_wav("/Users/xiaoxiao/Downloads/yequ-2/音频.wav")#读取音频文件
sound=sound.set_frame_rate(16000)
sound=sound.set_channels(1)
path="/Users/xiaoxiao/Downloads/参数设置后音频.wav"
sound.export(path,format="wav")
with open(path,"rb") as fp:
    wav=fp.read()

#获取文字
text=audio2text(wav)
print(text)
#定义语音合成函数
def text2audio(wordText):
    result=client.synthesis(text,"zh","1",{"vol":12,"spd":6,"pit":7,"per":4})
    if type(result)==dict:
        output="语音合成错误"
    else:
        output=result
    return output

#调用语音合成函数
audio=text2audio(text)
print(audio)
with open("/Users/xiaoxiao/Downloads/音频变音版.wav","wb") as fp:
    fp.write(audio)
print("变音文件生成完毕！")