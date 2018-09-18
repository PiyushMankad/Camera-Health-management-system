import cv2
import datetime
import os, fnmatch
import datetime

def getFile(path,imgtype):
    listOfFiles = os.listdir(path)  
    pattern = "*."+imgtype
    filename=[]
    for entry in listOfFiles:  
        if fnmatch.fnmatch(entry, pattern):
                filename.append(entry)
    return filename

### Input Format : year-month-date ###
### Eg: VideoWriter('2018-06-25') ###

def VideoWriter(tstamp):
    
    fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
    out = cv2.VideoWriter(tstamp+'.mp4',fourcc, 24.0, (640,480))
    try:
        file=getFile(tstamp+'/','png')
        print(file)
        for i in range(len(file)):
            print(i,file[i])
            frame=cv2.imread(tstamp+'/'+file[i])
            out.write(frame)
    except:
        print("Error Writing to Video")
        pass            
    out.release()
    print("DONE")
    cv2.destroyAllWindows()


'''timestamp=str(datetime.datetime.now()).split('.')
tstamp=timestamp[0].split()
VideoWriter(tstamp[0])'''

