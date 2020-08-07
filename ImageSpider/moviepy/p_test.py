# -*- coding: utf-8 -*-
from moviepy.editor import *
#import moviepy.editor as mpy
import math

#读取语音
voice = AudioFileClip("./mp3/s_10.mp3")
duration=voice.duration
max_dur = math.ceil(duration)
max_dur +=2
print(duration)
print(max_dur)

#读取字幕
# lines = np.loadtxt('./text/id_4.txt')
with open('./text/id_4.txt') as f:
    lines = f.readlines()
print(lines)
line_dur=duration/len(lines)
print(line_dur)

subtitle_clips=[]
for i,line in enumerate(lines):
    line = line.strip('\n')
    subtitle_clip=TextClip(line,color='white',font="simsun.ttc",fontsize=50,bg_color='black',align='center')
    subtitle_clip=CompositeVideoClip([subtitle_clip]).set_duration(line_dur).set_start(i*line_dur).set_end((i+1)*line_dur)
    subtitle_clips.append(subtitle_clip)
    print(i)

max_len = len(lines)
print(max_len)
subtitle_clip=TextClip("yummuu", color="white", font="simsun.ttc", fontsize=50, bg_color='black', align='center')
subtitle_clip=CompositeVideoClip([subtitle_clip]).set_duration(2).set_start(max_len*line_dur).set_end(max_len*line_dur+2)
subtitle_clips.append(subtitle_clip)

subtitles = concatenate(subtitle_clips)

vfc1 = VideoFileClip("./video/t_s_89.mp4").subclip(0,max_dur)
#合成
#语音-设置时长
final_audio = CompositeAudioClip([voice.volumex(2)])
#视频-添加上文字
final_video = CompositeVideoClip([
    vfc1,
    subtitles.set_position(('center',0.8), relative=True)
]).set_duration(max_dur)


result = final_video.set_audio(final_audio)

#vfc1 = VideoFileClip("./video/s_10.mp4")
# vfc2 = VideoFileClip("./video/s_17.mp4")
# result = CompositeVideoClip([video])
#两个视频剪辑合成一个
# result = concatenate_videoclips([vfc1,vfc2])
#输出视频
result.write_videofile("new_89.mp4", fps=24)
