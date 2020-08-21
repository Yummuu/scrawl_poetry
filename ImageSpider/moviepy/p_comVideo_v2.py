# -*- coding: utf-8 -*-
from moviepy.editor import *
import math
import re
import time

def outPoetryVideo(mp3_name, text_name, version_name):
    global start
    # #读取语音
    voice = AudioFileClip("./mp3/"+str(mp3_name)+".mp3")
    duration=voice.duration
    max_dur = math.ceil(duration)
    #读取字幕
    with open('./text/'+str(text_name)+'.txt', 'r', encoding='UTF-8-sig') as f:
        lines = f.readlines()
    line_dur=duration/len(lines)
    #报幕信息
    first_line = lines[0]
    first_line = first_line.strip('\n').strip('[1秒]').strip('[0.5秒]')
    title = first_line+'\n'+str(version_name)
    title_clips = TextClip(title,color='white', font="simsun.ttc", fontsize=80,stroke_color='black',stroke_width=1).set_start(0).set_end(line_dur).set_position(('center','center'), relative=True)

    #字幕创建-轨道同步
    subtitle_clips=[]
    for i,line in enumerate(lines):
        line = line.strip('\n').strip('[1秒]').strip('[0.5秒]')
        subtitle_clip=TextClip(line,color='white',font="simsun.ttc",fontsize=65,align='center',stroke_color='black',stroke_width=1)
        subtitle_clip=CompositeVideoClip([subtitle_clip]).set_duration(line_dur).set_start(i*line_dur).set_end((i+1)*line_dur)
        subtitle_clips.append(subtitle_clip)
    subtitles = concatenate(subtitle_clips)
    global videoC
    vfc1 = videoC.subclip(start,(start+max_dur))

    #设置字幕
    final_video = CompositeVideoClip([
        vfc1,
        subtitles.set_position(('center',0.8), relative=True),
        title_clips,
    ]).set_duration(max_dur)
    #设置音频
    final_audio = CompositeAudioClip([voice.volumex(2)])
    result = final_video.set_audio(final_audio)
    #输出视频
    result.write_videofile("./result/"+str(text_name)+"_"+str(version_name)+".mp4", fps=24)
    start += max_dur

    #关闭句柄
    vfc1.reader.close()
    vfc1.audio.reader.close_proc()
    pass

#交互输入
id_name = input("please input id_name:")
video_name = input("please input video_name:")

ids_arr = re.split(',', id_name)
ids_len = len(ids_arr)
start = 0
videoC = VideoFileClip("./video/"+str(video_name)+".flv")
if ids_len>1:
    for id_n in ids_arr:
        outPoetryVideo(id_n+'_pth',id_n,'【普通话版】')
        outPoetryVideo(id_n+'_cp',id_n,'【四川话版】')
        outPoetryVideo(id_n+'_yy',id_n,'【粤语版】')
        pass
else:
    print("仅支持多个id一个视频组合")
    pass

info='''
----input info---
    id_name:{_id_name}
    video_name:{_videoName}
'''.format(_id_name=id_name, _videoName=video_name)
print(info)