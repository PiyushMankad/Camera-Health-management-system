
import argparse
import datetime
import cv2
import numpy as np
from centroidtracker import CentroidTracker
from multiprocessing import Pool

from imutils.video import FPS
from imutils.video import VideoStream
import imutils

objectIdIn = []
objectIdOut = []
countIn = 0
countOut = 0

def inCounter(objectID):
	global objectIdIn,countIn
	
	if objectID not in objectIdIn:
		
		objectIdIn.append(objectID)
		#print("objectId",objectIdIn)
		#print("obj")
		countIn+=1
	else:
		pass
	
	return countIn

def outCounter(objectID):
	global objectIdOut,countOut
	
	if objectID not in objectIdOut:
		objectIdOut.append(objectID)
		#print("obj",objectID)
		countOut+=1	
	else:
		pass
	
	return countOut


def peopleCounter(source):
	#camera = cv2.VideoCapture(r"D:\chrome_downloads\test2.mp4")
	#camera = cv2.VideoCapture(r"C:\Users\Asus\Desktop\Reliance-PeopleCounter\people-counting-opencv\videos\example_01.mp4")
	#camera = cv2.VideoCapture(0)
	#camera = cv2.VideoCapture(r"D:\FACE_DETECT_RECOG\test0.mp4")
	#camera = cv2.VideoCapture('rtsp://admin:admin123@192.168.0.100')
	#camera = cv2.VideoCapture('rtsp://admin:admin%40123@192.168.0.200/Streaming/Channels/101')
	#camera = cv2.VideoCapture('rtsp://admin:admin%40123@192.168.0.200/Streaming/Channels/401')
	
	ct = CentroidTracker()
	camera = VideoStream(src=source).start()
	ret,old = camera.read()
	old=imutils.resize(old,width=480)
	
	r = cv2.selectROI(old)
	#frame2 = frame1[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
	print("\n ROI",r)
	
	firstFrame = None
	obj = []
	
	totalDown = 0
	totalUp = 0
	i = 0
	mask = np.zeros_like(old)
	# loop over the frames of the video
	while True:
		# grab the current frame and initialize the occupied/unoccupied
		# text
		(grabbed, frame_org) = camera.read()
		frame_org=imutils.resize(old,width=480)
		#count+=1
		if grabbed == True:
			y1 = int(r[1])
			y2 = int(r[1]+r[3])
			x1 = int(r[0])
			x2 = int(r[0]+r[2])
			#frame = frame1[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
			frame = frame_org[y1:y2,x1:x2]
			#row,col,_=frame.shape
			text = "Unoccupied"
	
			# if the frame could not be grabbed, then we have reached the end
			# of the video
			if not grabbed:
				break
	
			W,H,_=frame.shape
			rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			gray = cv2.GaussianBlur(gray, (21, 21), 0)
			
			# if the first frame is None, initialize it
			if firstFrame is None:
				firstFrame = gray
				continue
	
			# compute the absolute difference between the current frame and
			# first frame
			frameDelta = cv2.absdiff(firstFrame, gray)
			thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
			# dilate the thresholded image to fill in holes, then find contours
			# on thresholded image
			thresh = cv2.dilate(thresh, None, iterations=2)
			#cv2.imshow("thresh",thresh)
			(cnts,_) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
			#print("length",len(cnts))
			# loop over the contours
			#print("rect",(r[0], r[1]),(int(r[0]+r[2]),int(r[1] + r[3])))
			#(x, y, w, h) = cv2.boundingRect(r)
			cv2.rectangle(frame_org, (r[0], r[1]),(int(r[0]+r[2]),int(r[1] + r[3])), (1, 255, 0), 2)
			
			cv2.line(frame_org, (x1,int((y1+y2)/2)-20), (x2,int((y1+y2)/2)-20), (250, 0, 0), 2)
			cv2.line(frame_org, (x1,int((y1+y2)/2)), (x2,int((y1+y2)/2)), (0, 255, 255), 2)
			cv2.line(frame_org, (x1,int((y1+y2)/2)+20), (x2,int((y1+y2)/2)+20), (0, 0, 255), 2)
			#cv2.line(frame_org, (x1,int((H)/2)), (x2,int((H)/2)), (250, 0, 255), 2)
			#cv2.circle(frame1,(int(r[0]+r[2]),int(r[1] + r[3])),3,(0,0,255),-1)
			#cv2.line(frame, (x1,int((y1+y2)/2)+30), (x2,int((y1+y2)/2)+30), (255, 0, 0), 2)
			rects = []
			
			for c in cnts:
				#print(c)
				# if the contour is too small, ignore it
				if cv2.contourArea(c) < 5000:
					continue
				# compute the bounding box for the contour, draw it on the frame,
				# and update the text
				(x, y, w, h) = cv2.boundingRect(c)
				startX = x
				startY = y
				endX = x+w
				endY = y+h
				
				#rects.append(box)
				cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
				#print("rect",(x, y), (x + w, y + h))
				cv2.circle(frame,(x, y),3,(0,0,255),-1)
				cv2.circle(frame,(x + w, y + h),3,(0,0,255),-1)
			
				rectagleCenterPont = ((x + x + w) // 2, (y + y + h) // 2)
				#centroid_x = ((x + x + w) // 2)
				#centroid_y = ((y + y + h) // 2)
				
				cv2.circle(frame, rectagleCenterPont, 1, (0, 0, 255), 5)
				cv2.circle(mask, rectagleCenterPont, 1, (0, 0, 255), 5)
				#cv2.circle(frame, (int((x2-x1)/2),(y2-y1)), 1, (255, 0, 0), 10)
				#count+=1
					# add the bounding box coordinates to the rectangles list
				rects.append((startX, startY, endX, endY))
	
			#if len(rects)>0:
			#print("rect",rects[0])
			objects = ct.update(rects)
			#cv2.line(frame, (0, H // 2), (W, H // 2), (0, 255, 255), 2)
			#dict = {}
			# loop over the tracked objects
			
			#i = 0
			
			for (objectID, centroid) in objects.items():
					
				i = objectID
				obj.append(([i],centroid[1]))
				text = "ID {} ".format(objectID)
				# print("dir",direction)
				cv2.putText(frame, text, (centroid[0] - 10, centroid[1] - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
				#cv2.circle(frame, (centroid[0], centroid[1]), 4, (0, 255, 0), -1)
					#direction=[]
				
				
				#i+=1
				
			
				if len(obj)!=0:
						
					for i in range(len(obj)):
						if obj[i][0] == [objectID]:
							
							#print("difference",(obj[i][1]-obj[-1][1]))
							if (obj[i][1]-obj[-1][1])<-30 and int((y1+y2)/2)<=obj[-1][1]<=int((y1+y2)/2)+30:
								
								totalDown = inCounter(objectID)
								#length_old = length
							elif (obj[i][1]-obj[-1][1])>30 and int((y1+y2)/2)-20<obj[-1][1]<=int((y1+y2)/2):
								
								totalUp = outCounter(objectID)
								
								
					
			
			### comment this ###
			text2 = "IN {}".format(totalDown)
			text3 = "OUT {}".format(totalUp)
			cv2.putText(frame, text2,(20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
			cv2.putText(frame, text3,(20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
			cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
						(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

			
			cv2.imshow("Security Feed", frame_org)
			#cv2.imshow("Security Feed mask", mask)
			if cv2.waitKey(11) & 0xFF == ord('q'):
				break
		else:
			break
	# cleanup the camera and close any open windows
	camera.stop()
	cv2.destroyAllWindows()

	
def get_from_file():
	dvrIP = []
	channel = []
	mode = []
	username = []
	password = []
	name=[]
	rtsp=[]

	with open('peopleCounter.txt') as file: 
		data = file.readlines()
		#data = data.split('\n')

	for i in range(len(data)):
		#d=(data[i].split(":")[-1])
		data[i] = data[i].split(' : ')
		dvrIP.append(data[i][0])
		channel.append(data[i][1])
		username.append(data[i][2])
		password.append(data[i][3])
		mode.append(data[i][4])
		name.append(data[i][5].split("\n")[0])
		rtsp.append("rtsp://{}:{}@{}/Streaming/Channels/{}".format(data[i][2],data[i][3],data[i][0],data[i][1]))

		## inserting into database
		
	print("Running on {} Cameras".format(len(data)))
	pool = Pool(len(data))
	print(data)
	pool.map(peopleCounter, rtsp)
	
'''
def get_from_database():
	host1='localhost'
	user1='omni_chms'
	port1=3306
	password1='omni@1234'

	conn=sql.connect(host=host1, user=user1,port=port1,password=password1)
	with conn.cursor() as curr:
		curr.execute("USE omni;")
		conn.commit()

		curr.execute("SELECT * FROM Cameras;")
		results=curr.fetchall()
		conn.commit()

	conn.close()
	#return results

	dvrIP = []
	channel = []
	mode = []
	username = []
	password = []
	name=[]
	rtsp=[]

	for i in range(len(results)):
		## heatmap
		if data[i][7]==1:
			name.append(data[i][1])
			dvrIP.append(data[i][2])
			username.append(data[i][3])
			password.append(data[i][4])
			channel.append(data[i][5])
			rtsp.appnd("rtsp://{}:{}@{}/Streaming/Channels/{}".format(data[i][3],data[i][4],data[i][2],data[i][5]))

	#cap = cv2.VideoCapture(r'rtsp://admin:admin%40123@192.168.0.200/Streaming/Channels/201')

	print("Running on {} Cameras".format(len(results)))
	pool = Pool(len(results))
	pool.map(peopleCounter, rtsp)
'''


if __name__=='__main__':
	get_from_file()
	
	'''
	ap = argparse.ArgumentParser()
	ap.add_argument("-i", "--Input", type=str ,help="Input video source")
	args = vars(ap.parse_args())
	inputVid = args["Input"]
	'''
	#peopleCounter(inputVid)