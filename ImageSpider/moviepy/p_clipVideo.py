# -*- coding: utf-8 -*-
import moviepy.editor as mp

# clip = mp.AudioFileClip('./video/wz.flv')
# clip.write_audiofile('wx.mp3')
file_name = input("please input file name:")
clip_dur = input("please input clip duration:")
keep_audio = input("keep audio or not:")
info='''
----input info---
    Name:{__name}
    Clip_dur:{__clip_dur}
    Keep_audio:{__yes}
'''.format(__name=file_name, __clip_dur=clip_dur,__yes=keep_audio)
print(info)

clip = mp.VideoFileClip('./video/'+str(file_name)+'.flv')
#删除声音
if keep_audio=='no':
	clip = clip.without_audio()

duration = clip.duration
i = 0
while i < duration:
	print(i)
	start = i
	i += int(clip_dur)
	if(i > duration):
		continue
	v_name = './video_clip/'+str(file_name)+'_s_'+str(start)+'.mp4'
	vfc = clip.subclip(start,i)
	vfc.write_videofile(v_name)
	print(v_name)
	pass

# vfc.write_videofile('test2.mp4')