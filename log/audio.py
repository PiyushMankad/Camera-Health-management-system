import moviepy.editor as mpe
import os

def insert():
	clip=mpe.VideoFileClip(r"C:\Users\omni\Documents\Camera Health management system\static\2018-06-25.mp4")
	audio=mpe.AudioFileClip(r"C:\Users\omni\Documents\Camera Health management system\static\LetHerGo.mp3")
	audio.duration=clip.duration
	final=clip.set_audio(audio)
	final.write_videofile("test.mp4",fps=24)

