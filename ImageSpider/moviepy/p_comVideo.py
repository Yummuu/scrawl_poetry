# -*- coding: utf-8 -*-
import moviepy.editor as mp
import math

#交互输入
id_name = input("please input id_name:")
video_name = input("please input video_name:")


def outPoetryVideo(mp3_name, text_name, version_name, video_name):
	#读取语音
    voice = mp.AudioFileClip("./mp3/"+str(mp3_name)+".mp3")
    duration=voice.duration
    max_dur = math.ceil(duration)
    #读取字幕
    with open('./text/'+str(text_name)+'.txt', 'r', encoding='UTF-8') as f:
        lines = f.readlines()
    line_dur=duration/len(lines)

    #报幕信息
    first_line = lines[0]
    first_line = first_line.strip('\n').strip('[1秒]').strip('[0.5秒]')
    title = first_line+'\n'+str(version_name)
    title_clips = mp.TextClip(title,color='white', font="simsun.ttc", fontsize=80, bg_color='black').set_start(0).set_end(line_dur).set_position(('center','center'), relative=True)

    #字幕创建-轨道同步
    subtitle_clips=[]
    for i,line in enumerate(lines):
        line = line.strip('\n').strip('[1秒]').strip('[0.5秒]')
        subtitle_clip=mp.TextClip(line,color='white',font="simsun.ttc",fontsize=60,bg_color='black',align='center')
        subtitle_clip=mp.CompositeVideoClip([subtitle_clip]).set_duration(line_dur).set_start(i*line_dur).set_end((i+1)*line_dur)
        subtitle_clips.append(subtitle_clip)
    subtitles = mp.concatenate(subtitle_clips)

    #读取视频文件
    if video_name!='none':
        #手动添加的视频
        vfc1 = mp.VideoFileClip("./video_clip/"+str(video_name)+".mp4").subclip(0,max_dur)
    else:
        #随机视频-取长视频
        rand_video = "xk.flv"
        vfc1 = mp.VideoFileClip("./video/"+rand_video).subclip(40,(max_dur+40))
    #设置字幕
    final_video = mp.CompositeVideoClip([
        vfc1,
        subtitles.set_position(('center',0.8), relative=True),
        title_clips,
    ]).set_duration(max_dur)
    #设置音频
    final_audio = mp.CompositeAudioClip([voice.volumex(2)])
    result = final_video.set_audio(final_audio)
    #输出视频
    result.write_videofile("./result/"+str(text_name)+"_"+str(version_name)+".mp4", fps=24)
    pass

outPoetryVideo(id_name+'_pth',id_name,'【普通话版】',video_name)
outPoetryVideo(id_name+'_cp',id_name,'【四川话版】',video_name)
outPoetryVideo(id_name+'_yy',id_name,'【粤语版】',video_name)

info='''
----input info---
    id_name:{_id_name}
    video_name:{_videoName}
'''.format(_id_name=id_name, _videoName=video_name)
print(info)