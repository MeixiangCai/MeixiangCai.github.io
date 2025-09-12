from aip import AipSpeech
App_ID="118816395"
Api_key="bCdVy6xhvizJWAEi6tYBTkQo"
Secret_key="1JR0G5TccMvuJFe8LSRS4fdxcosN7ja1"
client=AipSpeech(App_ID,Api_key,Secret_key)
#定义一个语音转文字的函数
def audio2text(wav):
    rejson=client.asr(wav,"wav",16000,{"dev_pid":1537})
    if rejson["err_no"]==0:
        msg=rejson["result"][0]  
    else:
        msg="语音识别错误！"  
    return msg

#从视频文件中提取音频
import moviepy
from moviepy.editor import VideoFileClip
video=VideoFileClip("/Users/xiaoxiao/Downloads/sd1741794502_2.MP4") #加载视频文件
audio=video.audio
audio.write_audiofile("/Users/xiaoxiao/Downloads/sd1741794502_2.wav") #将音频写入音频文件中

#对音频文件进行参数设置
from pydub import AudioSegment
sound=AudioSegment.from_wav("/Users/xiaoxiao/Downloads/sd1741794502_2.wav")#读取音频文件
sound=sound.set_frame_rate(16000)
sound=sound.set_channels(1)
# sound.export(targetPath,format="wav") 可进行保存导出操作
# 接下来切除静音段
from pydub.silence import split_on_silence
min_silence_len=500 #静音的时间长度
silence_thresh=-50 #静音的强度
count=0
pieces=split_on_silence(sound,min_silence_len,silence_thresh)#得到包含多个音频文件的列表
for i in pieces:
    path="/Users/xiaoxiao/Downloads/音频片段"+str(count)+".wav"
    i.export(path,format="wav")
    count+=1

#定义打开并读取音频文件
def read_file(filePath):
    with open(filePath,"rb") as fp:
        wavsample=fp.read()
        return wavsample
#开始批量进行语音转文字    
for i in range(count):
    wavsample=read_file("/Users/xiaoxiao/Downloads/音频片段"+str(i)+".wav")
    text=audio2text(wavsample)
    print(text) 

#下面将文字变成字幕文件，为视频配上字幕
from pydub.silence import detect_nonsilent
timestamp_list=detect_nonsilent(sound, min_silence_len, silence_thresh) #获取时间数据，二维列表

#定义获得标准字幕时间格式的函数
def getTime(t):
    spart,mspart=divmod(t,1000) #取整取模
    mpart,spart=divmod(spart,60)
    hpart,mpart=divmod(mpart,60)
    mspart=str(mspart).zfill(3) #保留三位数，不够的前面加0
    spart=str(spart).zfill(2)
    mpart=str(mpart).zfill(2)
    hpart=str(hpart).zfill(2)
    stype=hpart+":"+mpart+":"+spart+","+mspart
    return stype

#定义生成字幕文件的函数
def getsrt(sn,start_time,end_time,text):
    srt_text=str(sn)+"\n"+start_time+" --> "+end_time+"\n"+text+"\n"+"\n" 
    return srt_text

#定义字幕文件写入函数
def writesrt(srtpath,srt):
    with open(srtpath,"a") as fp:
        fp.write(srt)

#开始遍历二维列表，批量生成srt字幕     
count = 0
for i in timestamp_list:
    wavsample=read_file("/Users/xiaoxiao/Downloads/音频片段"+str(count)+".wav")
    text=audio2text(wavsample)
    symbol=["，","。","！","？"]
    for j in symbol:
        text=text.replace(j," ") #将标点符号替换为空格
    start_time=getTime(i[0])
    end_time=getTime(i[1])
    srt_text=getsrt(count,start_time,end_time,text) #生成字幕文件
    path="/Users/xiaoxiao/Downloads/sd1741794502_2.srt" #开始写入字幕文件
    writesrt(path,srt_text)
    count+=1
print(f"字幕文件已生成")
