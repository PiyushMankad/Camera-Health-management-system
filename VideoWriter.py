import cv2
import datetime
import os
import datetime, glob, cv2
import moviepy.editor as mpe
 

def audio_video(videopath,audiopath,name):
    #VideoWriter.VideoWriter(day)
    clip=mpe.VideoFileClip(videopath)
    audio=mpe.AudioFileClip(audiopath)
    audio.duration=clip.duration
    final=clip.set_audio(audio)
    dest=os.path.join(os.getcwd(),"static",str(datetime.datetime.now()).split(" ")[0],name,"Summary.mp4")
    '''
    final.write_videofile(dest,fps=20)
    print(os.path.split(dest))
    '''
    try:
        final.write_videofile(dest,fps=30)
    except Exception:
        #final.write_videofile(r"F:\amaretto\2019-05-13\Amretto2\Summary.mp4",fps=30)
        print("\nVideo Writer \n",Exception)

        
    if os.path.exists(videopath):
        print(videopath,"deleted")
        os.remove(videopath)
    else:
        print(videopath,"couldn't be deleted")
    #print(os.path.split(dest))
    return os.path.join(str(datetime.datetime.now()).split(" ")[0],name,"Summary.mp4")

## writes summary file
def video_summary(location,name):
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter(os.path.join(location,"summary.avi"),0,20,(480,270))# 480,270
    try:
        for img in sorted(glob.glob(location+"/*.jpg")):
            #print(img)
            frame=cv2.imread(img)
            out.write(frame)
    except Exception as e:
        print("Error writing file")
        raise e

    videopath=os.path.join(location,"summary.avi")
    print("videopath",videopath)
    out.release()
    cv2.destroyAllWindows()
    return audio_video(videopath,os.path.join(os.getcwd(),"static","LetHerGo.mp3"),name)


#video_summary(r"F:\amaretto\2019-05-13\Amretto2","Amretto2")
#audio_video(r"E:\Camera Health management system\2019-05-10\Developer\summary.avi",r"C:\Users\Ayush\Music\01LetHerGo.mp3")
