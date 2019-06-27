from imutils.video import FPS
from imutils.video import VideoStream
import cv2
import copy

import time
import datetime, os, glob, shutil
import numpy as np
import imutils
from datetime import datetime, timedelta

from multiprocessing import Pool
import pymysql as sql
from mysql import*
from VideoWriter import video_summary

	
## SEND EMAIL ALERTS
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def email_alert(name,ip,channel,reason,attach="None"):

	#sender="piyush@omnipresent.com"
	#receiver="bhawna@omnipresent.com"
	sender="sujayrpi@gmail.com"
	receiver=["piyush@omnipresenttech.com","rishabh@omnipresenttech.com"]

	for index in range(len(receiver)):
		msg=MIMEMultipart()
		msg['From']=sender
		msg['to']=receiver[index]
		msg['Subject']="[	ATTENTION USER	]"
		body=" Your camera '{}' of IP '{} channel {}' has encountered {}.\n Please check below attachment".format(name,ip,channel,reason)
		
		msg.attach(MIMEText(body,'plain'))


		## attaches multiple images
		if not attach=="None":
			for i in range(len(attach)):

				## if not enough frames are found for attachment then a string is passed in the search frame Arguement
				try:
					attachment=open(attach[i],"rb")
				except:
					print("No such Attachment %s"%attach[i])

				# instance of MIMEBase and named as p
				p = MIMEBase('application', 'octet-stream')
				# To change the payload into encoded form
				p.set_payload((attachment).read())
				# encode into base64
				encoders.encode_base64(p)
				p.add_header('Content-Disposition', "attachment; filename= %s" % attach[i])
				# attach the instance 'p' to instance 'msg'
				msg.attach(p)
		

		try:
			# creates SMTP session
			s = smtplib.SMTP('smtp.gmail.com', 587)
			# start TLS for security
			s.starttls()
			# Authentication
			s.login(sender, "sujay2908")
			print("Logging into server account") 

			# Converts the Multipart msg into a string
			text = msg.as_string()
			s.sendmail(sender, receiver[index], text)
			# terminating the session
			s.quit()
		except Exception as e:
			##raise e
			print("Email not sent, No Internet Connection")



## removinng frames so that space is available
def remove_frames(location):
	print("Removing Frames from",location)
	img_list=[]
	for img in sorted(glob.glob(location+"/*.jpg")):
		try:
			os.remove(img)
		except:
			print("cannot remove",img)
			pass

## searchs for the last frame after tampering or feed loss
def search_frame(times,location,name,pasttimes="00_00_00"):
	stimes=times.split(" ")[1].replace(":","_")
	print("search_arguement",location,stimes,pasttimes)
	copy=[]
	copycount=0
	searchframe=[]

	for img in sorted(glob.glob(location+"/*.jpg")):
		#print("image traversed",os.path.split(img)[1].split(".")[0],stimes,pasttimes)
		if os.path.split(img)[1].split(".")[0] <= stimes and os.path.split(img)[1].split(".")[0] > pasttimes:
			copycount=copycount+1
			if copycount>4:
				break
			copy.append(img)
			#print("\nImages Copied",img)

	if copy==[]:
		return ["Error:","Copy","is","Empty"]
	else:
		for i in range(len(copy)):
			searchframe.append(os.path.join(times.split(" ")[0],name,"tampered","search."+os.path.split(copy[i])[1]))
			#print("Search Frame %s \tCopyframe %s"%(searchframe,copy[i]))
			shutil.copy(copy[i],os.path.join(location,"tampered","search."+os.path.split(copy[i])[1]))
			#tamperframe=os.path.join(location,"tampered","search."+os.path.split(copy)[1])
		return searchframe
		

## checks if the folder / location exists or not
def check_location(location,name):
	if not os.path.exists(location):
		try:
			os.mkdir(os.path.join("static",str(datetime.now()).split(" ")[0]))
			os.mkdir(location)
			os.mkdir(os.path.join(location,"tampered"))
			os.mkdir(os.path.join(location,"heatmap"))
		except:
			os.mkdir(location)
			os.mkdir(os.path.join(location,"tampered"))
			os.mkdir(os.path.join(location,"heatmap"))

## this function is used to check for tampering events
def feed(args):
	dvr_ip, channel, username, password, mode, name, vidtime = args
	if channel == '':
		## save frame is called in os.system for saving frames every 4 seconds wrt time
		saveFrame="ffmpeg -loglevel panic -i rtsp://"+username+':'+password+'@'+dvr_ip+":554 -vf"" fps=1 -t 1 "
		## source is used in video stream
		source="rtsp://"+username+':'+password+'@'+dvr_ip
		## location where the saveframes would be stored
		location=os.path.join(os.getcwd(),"static",str(datetime.now()).split(" ")[0],name)

	else:
		saveFrame="ffmpeg -loglevel panic -i rtsp://" + username + ':' + password + '@' + dvr_ip + ":554/Streaming/Channels/"+ channel + " -vf fps=1 -t 1 "
		source="rtsp://" + username + ':' + password + '@' + dvr_ip + ":554/Streaming/Channels/"+ channel
		location=os.path.join(os.getcwd(),"static",str(datetime.now()).split(" ")[0],name)

		## amaretto details
		##source="rtsp://" + username + ':' + password + '@' + dvr_ip + "/cam/realmonitor?channel="+ channel+"&subtype=0"



	#print("\n ID ",os.getpid(),mode)
	with open(os.path.join(os.getcwd(),"processkill.txt"),"a+") as file:
		file.write(str(os.getpid())+"\n")

	#print(source)
	#print("location",location)
	check_location(location,name)

	heatTime=time.time()

	try:
		Hmaps = len(os.listdir(os.path.join(location,"heatmap")))/2+1
	except:
		print("Exception Hmaps")
		Hmaps=1

	Hcounter=0

	while True:
		
		vid=VideoStream(src=source).start()
		bgsub = cv2.createBackgroundSubtractorMOG2()
		startTime=time.time()
		summaryCount=0
		feedloss=False

		while True:

			try:
				ret,frame=vid.read()
				frame=imutils.resize(frame,width=480)

				if ret:
					updateCameraHealth(name,dvr_ip,status="Working")
				else:
					'''
				    times=str(datetime.now()).split(".")[0]
				    #tamperframe=search_frame(times,location,name)
				    updateCameraHealth(name,dvr_ip,status="Not Working")
				    insert2tampered(name,dvr_ip,times,TamperedFrame="None",searchframe=["None"],Event="Feed Loss")
				    #email_alert(name,dvr_ip,channel,tamperframe,"Feed Loss")
				    '''
					print("Invalid Information for ",name)
					time.sleep(30)
					break
				rows,cols,channels=frame.shape
				tamperThreshold=(rows*cols*0.6)

			except Exception as e:
				if feedloss:
					print("feedloss for",name)
					break
					#continue
				else:
					feedloss=True
					times=str(datetime.now()).split(".")[0]
					pasttimes=str(datetime.now()-timedelta(seconds=16)).split(".")[0].split(" ")[1].replace(":","_")
					#tamperframe=search_frame(times,location)
					SearchFrame=search_frame(times,location,name,pasttimes)
					updateCameraHealth(name,dvr_ip,status="Invalid Information")
					insert2tampered(name,dvr_ip,times,TamperedFrame="None",searchframe=SearchFrame,Event="Feed Loss")
					print("Frame can't be processed for",name)
					#email_alert(name,dvr_ip,channel,"Feed Loss",attach=SearchFrame)
					time.sleep(60)
					## Use "continue" for contigous feedloss event to be true
					continue
					#break
				#raise e


			feedloss=False
			## applying background subtraction
			sub=bgsub.apply(frame)


			## saving frame of particular camera after 4 seconds
			if time.time()-startTime>4:
				times=str(datetime.now()).split(".")[0].split(" ")[1].replace(":","_")
				#os.system(saveFrame+os.path.join(location,times+".jpg"))
				cv2.imwrite(os.path.join(location,times+".jpg"),frame)
				startTime=time.time()

			## Summary Generation 
			if str(datetime.now()).split(".")[0].split(" ")[1]>=vidtime and summaryCount==0:
				path=video_summary(location,name)
				## add vidpath to database
				dailyEntry(name,str(datetime.now()),Video=path)

				## Intelligent_Summary Generation
				if os.path.exists(os.path.join(location,"tampered")):
					path=video_summary(os.path.join(location,"tampered"),name,fps=1)
					## add vidpath to database
					dailyEntry(name,str(datetime.now()),Intelligent_Summary=path)
				else:
					pass


				time.sleep(10)
				summaryCount=1
				print("summary generarted for",name)
				remove_frames(location)
				continue



			## run MOTION MAP every 15 min 	/ mode 2 ## heatmap
			if time.time()-heatTime>90 and mode == "2":

				num_frames=250
				Hcounter= Hcounter+1

				location_H=os.path.join(os.getcwd(),"static",str(datetime.now()).split(" ")[0],name)
				'''
				try:
					os.mkdir(os.path.join(location_H,"heatmap")) ##opti
				except:
					pass
				'''
				location_H=os.path.join(location_H,"heatmap")
				image=os.path.join(location_H,"heatmap%s.jpg"%str(Hmaps))
				original=os.path.join(location_H,"original%s.jpg"%str(Hmaps))
				#print(location_H)
				#print("Hcounter", name,Hcounter)
				
				if (os.path.exists(image)):
					first_frame = cv2.imread(image)
					flag = 1
				else:
					#cv2.imwrite(original,imutils.resize(vid.read()[1],width=720))
					#cv2.imwrite(original,frame) ## opti writing image multiple times
					flag = 0



				#frame = imutils.resize(vid.read()[1],width=720)
				#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
				
				if Hcounter == 1:
					if flag == 0:
						first_frame = copy.deepcopy(frame)
						#print("first",first_frame.shape)
					height, width = frame.shape[:2]
					accum_image = np.zeros((height, width), np.uint8)

				else:
					#fgmask = bgsub.apply(gray)  # remove the background
					ret, th1 = cv2.threshold(sub, 2, 2, cv2.THRESH_BINARY)
					# add to the accumulated image
					accum_image = cv2.add(accum_image, th1)
				

				if Hcounter==num_frames:

					color_image = cv2.applyColorMap(accum_image, cv2.COLORMAP_JET)#HOT#PINK
					result_overlay = cv2.addWeighted(first_frame, 0.7, color_image, 0.3, 0)
					#convertedImage = np.hstack((result_overlay,first_frame))
					
					# save the final overlay image
					cv2.imwrite(original,frame)
					cv2.imwrite(image, result_overlay) ## opti

					heatmapEntry=(os.path.join(str(datetime.now()).split(" ")[0],name,"heatmap","heatmap%s.jpg"%str(Hmaps)))
					originalEntry=(os.path.join(str(datetime.now()).split(" ")[0],name,"heatmap","original%s.jpg"%str(Hmaps)))
					move_percent=heatmap_percent(frame,result_overlay)

					#print(name,datetime.now(),originalEntry,heatmapEntry,move_percent)
					#print(type(name),type(datetime.now()),type(originalEntry),type(heatmapEntry),type(move_percent))
					heatmapsEntry(name,str(datetime.now()),originalEntry,heatmapEntry,move_percent)
					print("Time taken to Generate Heat Map ",time.time()-heatTime,name)
					
					heatTime=time.time()
					Hcounter=0
					Hmaps=Hmaps+1
				#continue

			## taking threshold to make img binary
			_,thresh=cv2.threshold(sub,150,255,cv2.THRESH_BINARY)
			## calculating white pixels ie motion pixels
			hist=np.bincount(thresh.ravel(),minlength=256)
			#print("{} motion pixels of {}".format(hist[255],rows*cols))


			## tamper condition along with saving the frames 
			if hist[255]>tamperThreshold:
				tamperpath=os.path.join(location,"tampered")
				'''
				try:
					os.mkdir(tamperpath)
				except:
					pass
				'''
				print("Tampered",source)
				times=str(datetime.now()).split(".")[0]
				pasttimes=str(datetime.now()-timedelta(seconds=16)).split(".")[0].split(" ")[1].replace(":","_")

				tsave=times.split(" ")[1].replace(":","_")
				cv2.putText(frame,'Tampered Frame',(20,40), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(0,0,255),2)
				cv2.imwrite(os.path.join(tamperpath,"tamper."+tsave+".jpg"),frame)#imutils.resize(frame,width=640))
				tamperframe=os.path.join(times.split(" ")[0],name,"tampered","tamper."+tsave+".jpg")

				SearchFrame=search_frame(times,location,name,pasttimes)
				insert2tampered(name,dvr_ip,times,TamperedFrame=tamperframe,searchframe=SearchFrame,Event="Tampered")
				updateCameraHealth(name,dvr_ip,status="Not Working")
				print("Tamper Complete")
				## adding tamperframe to search frame
				SearchFrame.append(tamperframe)
				#email_alert(name,dvr_ip,channel,"Tampering",attach=SearchFrame)
				#break
			cv2.imshow("sub",frame)
			if cv2.waitKey(1) & 0xff==ord('q'):
				break
			'''
			'''

		print("\n\tSTOPPED... \nTime Taken",time.time()-startTime)
		vid.stop()
		#vid.release()
		cv2.destroyAllWindows()



def get_from_file():
	dvrIP = []
	channel = []
	mode = []
	username = []
	password = []
	name=[]
	vidtime=[]
	with open(os.path.join(os.getcwd(),"CameraDetails3.txt"),"r") as file: 
		data = file.readlines()
		#data = data.split('\n')

	for i in range(len(data)):
		#d=(data[i].split(":")[-1])
		data[i] = data[i].split(' ; ')
		dvrIP.append(data[i][0])
		channel.append(data[i][1])
		username.append(data[i][2])
		password.append(data[i][3])
		mode.append(data[i][4])
		name.append(data[i][5].split("\n")[0])
		vidtime.append(data[i][6])
		## inserting into database
		insertCameraHealth(data[i][5],data[i][0])


		#print("asss",data[i][6])
		## checks daily or an entry
		if checkout():
			dailyEntry(data[i][5].split("\n")[0],datetime.now(),data[i][0])

	print("Running on {} Cameras".format(len(data)))
	pool = Pool(len(data))
	pool.map(feed, zip(dvrIP, channel, username, password, mode, name, vidtime))


def checkout():
	'''
	date=os.getenv("DateCheck")
	today=datetime.strftime(datetime.today(),'%Y-%m-%d')
	if date==today:
		return False
	else:
		os.system("setx DateCheck {}".format(str(today)))
		return True
	'''

	with open("DateCheck.txt","r+") as file:
		date=file.read()

	today=datetime.strftime(datetime.today(),'%Y-%m-%d')
	#print("Checking out...",today)
	#print(type(date),date)
	#print(type(today),today)

	if date==today:
		return False
	else:
		with open("DateCheck.txt","w+") as file:
			file.write(today)
		return True


def heatmap_percent(original,heatmap):
	img1=(original)
	img2=(heatmap)
	row,col,channel=img1.shape
	sub=cv2.absdiff(img1,img2)
	sub=cv2.cvtColor(sub,cv2.COLOR_BGR2GRAY)
	thresh=cv2.threshold(sub,50,255,cv2.THRESH_BINARY)[1]
	'''
	cv2.imshow("sub",sub)
	cv2.imshow("heatmap",img2)
	cv2.imshow("thresh",thresh)
	cv2.waitKey(0)
	'''
	hist=np.bincount(thresh.ravel(),minlength=256)
	move_percent=hist[255]/(row*col)*100
	return move_percent


if __name__ == '__main__':

	'''
	print((time.ctime(time.time())))
	print(os.getcwd())
	times=str(datetime.now()).split(".")[0].split(" ")[1].replace(":","_")
	print(times)
	killfile=os.path.join(os.getcwd(),"processkill.txt")
	if os.path.exists(killfile):
		#print(killfile,"is DELETED")
		os.remove(killfile)
	
	tg=datetime.strptime(str(datetime.now()).split(".")[0].split(" ")[1],"%H:%M:%S")-timedelta(seconds=10)
	print("timedelta",tg)	
	pasttimes=str(datetime.now()-timedelta(seconds=5)).split(".")[0].split(" ")[1].replace(":","_")
	print(pasttimes)
	'''	

	#get_from_database()
	get_from_file()


	#search_frame(str(datetime.now()).split(".")[0],r"E:\CHMS\2019-05-04\overhead")
	#search_frame("diss 17:52:23",r"E:\CameraHealthManagementSystem\static\2019-05-22\overhead","overhead")
	#video_summary(r"E:\Camera Health management system\static\2018-06-25")
	#video_summary(r"E:\CHMS\2019-05-09\Storage")
	#email_alert("name","192.168.0.200","01","Tampering")
	#checkout()
	#remove_frames(r"E:\CameraHealthManagementSystem\static\2019-05-22\overhead")

	'''
	192.168.0.103 ;  ; admin ; admin123 ; 2 ; entry ; 17:23:00
	192.168.0.102 ;  ; admin ; admin123 ; 2 ; overhead ; 17:27:009  
	192.168.0.101 ;  ; admin ; admin123 ; 2 ; cabin ; 17:20:00
	192.168.0.104 ;  ; admin ; admin123 ; 1 ; outside ; 17:25:00

	'''