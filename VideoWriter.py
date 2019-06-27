import cv2
import datetime
import os
import datetime, glob, cv2
import moviepy.editor as mpe
 

def audio_video(videopath,audiopath,name,fps):
    #VideoWriter.VideoWriter(day)
    clip=mpe.VideoFileClip(videopath)
    audio=mpe.AudioFileClip(audiopath)
    audio.duration=clip.duration
    final=clip.set_audio(audio)
    if fps==20:
        location=os.path.split(videopath)[0]
        dest=os.path.join(os.getcwd(),"static",str(datetime.datetime.now()).split(" ")[0],name,"Summary.mp4")
    else:
        location=os.path.split(videopath)[0]
        dest=os.path.join(os.getcwd(),"static",str(datetime.datetime.now()).split(" ")[0],name,"Intelligent_Summary.mp4")
    
    try:
        final.write_videofile(dest,fps=fps)
    except Exception:
        print("location",location)
        dest=os.path.join(location,"Summary.mp4")
        final.write_videofile(dest,fps=fps)
        print("\nVideo Writer \n",Exception,os.getcwd())

    try:
        if os.path.exists(videopath):
            print(videopath,"deleted")
            os.remove(videopath)
        else:
            print(videopath,"couldn't be deleted")
    except Exception as e:
        pass
    
    if fps == 20:
        return os.path.join(str(datetime.datetime.now()).split(" ")[0],name,"Summary.mp4")
    else:
        return os.path.join(str(datetime.datetime.now()).split(" ")[0],name,"Intelligent_Summary.mp4")

## writes summary file
def video_summary(location,name,fps=20):
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter(os.path.join(location,"summary.avi"),0,fps,(480,270))# 480,270
    try:
        for img in sorted(glob.glob(location+"/*.jpg")):
            #print(img)
            statinfo=os.stat(img)
            if statinfo.st_size<5:
                continue

            frame=cv2.imread(img)
            out.write(frame)
    except Exception as e:
        print("Error writing file\n",e)
        #raise e

    videopath=os.path.join(location,"summary.avi")
    print("videopath",videopath)
    out.release()
    cv2.destroyAllWindows()
    return audio_video(videopath,os.path.join(os.getcwd(),"static","LetHerGo.mp3"),name,fps)


#video_summary(r"E:\CameraHealthManagementSystem\static\2019-05-22\overhead\tampered","overhead",fps=1)
#audio_video(r"E:\Camera Health management system\2019-05-10\Developer\summary.avi",r"C:\Users\Ayush\Music\01LetHerGo.mp3")
