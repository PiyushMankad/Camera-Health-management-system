
import numpy as np
import cv2
import copy
import argparse
from os import path
import os, time
import datetime
from imutils.video import FPS
from imutils.video import VideoStream
import imutils
import numpy as np

from multiprocessing import Pool
import pymysql as sql
from datetime import datetime

def motionMap(args):
	t1=time.time()
	rtsp,name=args
	location=os.path.join(os.getcwd(),"static",str(datetime.now()).split(" ")[0],name)
	try:
		os.mkdir(os.path.join(location,"heatmap"))
	except:
		pass

	location=os.path.join(location,"heatmap")
	image=os.path.join(location,"heatmap.jpg")
	original=os.path.join(location,"original.jpg")
	print(location)

	cap = VideoStream(src=rtsp).start()
	fgbg = cv2.createBackgroundSubtractorMOG2()


	if (os.path.exists(image)) == True:
		first_frame = cv2.imread(image)
		flag = 1
	else:
		cv2.imwrite(original,imutils.resize(cap.read()[1],width=720))
		original=str(os.path.join(str(datetime.now()).split(" ")[0],name,"heatmap","original.jpg"))
		print(original)
		#dailyEntry(name,datetime.now(),Original=original)
		flag = 0

	num_frames = 500

	for i in range(0, num_frames):
		'''
		There are some important reasons this if statement exists:
			-in the first run there is no previous frame, so this accounts for that
			-the first frame is saved to be used for the overlay after the accumulation has occurred
			-the height and width of the video are used to create an empty image for accumulation (accum_image)
		'''
		frame = imutils.resize(cap.read()[1],width=720)
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		if (i == 0):
			#first = copy.deepcopy(frame)
			if flag == 0:
				first_frame = copy.deepcopy(frame)
				#print("first",first_frame.shape)
			height, width = gray.shape[:2]
			accum_image = np.zeros((height, width), np.uint8)

		else:
			fgmask = fgbg.apply(gray)  # remove the background
			ret, th1 = cv2.threshold(fgmask, 2, 2, cv2.THRESH_BINARY)
			# add to the accumulated image
			accum_image = cv2.add(accum_image, th1)
			
		### comment this for website ###
		'''
		cv2.imshow('frame', frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
		'''
	
	color_image = cv2.applyColorMap(accum_image, cv2.COLORMAP_JET)#HOT#PINK
	result_overlay = cv2.addWeighted(first_frame, 0.8, color_image, 0.2, 0)
	convertedImage = np.hstack((result_overlay,first_frame))
	
	# save the final overlay image
	cv2.imwrite(image, convertedImage)
	heatmap=str(os.path.join(str(datetime.now()).split(" ")[0],name,"heatmap","heatmap.jpg"))
	#dailyEntry(name,datetime.now(),Heatmap=heatmap)
	print(heatmap)
	print("Time taken to Generate Heat Map ",time.time()-t1,name)
	#cv2.imwrite('motionMap_org.jpg', result2)
	cap.stop()
	cv2.destroyAllWindows()



### -> instructions for noobie
def motionMap2(args):
	t1=time.time()
	rtsp,name=args
	location=os.path.join(os.getcwd(),"static",str(datetime.datetime.now()).split(" ")[0],name)
	print(location)
	try:
		os.mkdir(os.path.join(location,"heatmap"))
	except:
		pass

	location=os.path.join(location,"heatmap")
	image=os.path.join(location,"heatmap.jpg")
	original=os.path.join(location,"original.jpg")

	cap = VideoStream(src=rtsp).start()
	fgbg = cv2.createBackgroundSubtractorMOG2()


	if (path.exists(image)) == True:
		first_frame = cv2.imread(image)
		flag = 1
	else:
		cv2.imwrite(original,imutils.resize(cap.read()[1],width=720))
		flag = 0

	num_frames = 200

	for i in range(0, num_frames):
		'''
		There are some important reasons this if statement exists:
			-in the first run there is no previous frame, so this accounts for that
			-the first frame is saved to be used for the overlay after the accumulation has occurred
			-the height and width of the video are used to create an empty image for accumulation (accum_image)
		'''
		if (i == 0):
			frame = imutils.resize(cap.read()[1],width=720)
			#first = copy.deepcopy(frame)
			if flag == 0:
				first_frame = copy.deepcopy(frame)
				#print("first",first_frame.shape)
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			height, width = gray.shape[:2]
			accum_image = np.zeros((height, width), np.uint8)

		else:
			frame = imutils.resize(cap.read()[1],width=720)  # read a frame
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # convert to grayscale
			fgmask = fgbg.apply(gray)  # remove the background
			ret, th1 = cv2.threshold(fgmask, 170, 250, cv2.THRESH_BINARY)
			# add to the accumulated image
			accum_image = cv2.add(accum_image, th1)
	
		### comment this for website ###
		'''
		cv2.imshow('frame', frame)
		'''
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	
	color_image = cv2.applyColorMap(accum_image, cv2.COLORMAP_JET)#HOT#PINK
	result_overlay = cv2.addWeighted(first_frame, 0.8, color_image, 0.2, 0)
	convertedImage = np.hstack((result_overlay,first_frame))
	
	# save the final overlay image
	cv2.imwrite(image, result_overlay)
	print("Time taken to Generate Heat Map",time.time()-t1)
	#cv2.imwrite('motionMap_org.jpg', result2)
	cap.stop()
	cv2.destroyAllWindows()

	
def get_from_file():
	dvrIP = []
	channel = []
	mode = []
	username = []
	password = []
	name=[]
	rtsp=[]

	with open('heatmap.txt') as file: 
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
	print(rtsp)
	pool.map(motionMap,zip(rtsp,name))
	

'''
def motionMap(rtsp,name):
	t1=time.time()
	rtsp,name=rtsp,name
	location=os.path.join(os.getcwd(),"static",str(datetime.now()).split(" ")[0],name)
	try:
		os.mkdir(os.path.join(location,"heatmap"))
	except:
		pass

	location=os.path.join(location,"heatmap")
	image=os.path.join(location,"heatmap.jpg")
	original=os.path.join(location,"original.jpg")
	print(location)

	cap = VideoStream(src=rtsp).start()
	fgbg = cv2.createBackgroundSubtractorMOG2()


	if (os.path.exists(image)) == True:
		first_frame = cv2.imread(image)
		flag = 1
	else:
		cv2.imwrite(original,imutils.resize(cap.read()[1],width=720))
		original=str(os.path.join(str(datetime.now()).split(" ")[0],name,"heatmap","original.jpg"))
		print(original)
		dailyEntry(name,datetime.now(),Original=original)
		flag = 0

	num_frames = 500

	for i in range(0, num_frames):
		'''
		There are some important reasons this if statement exists:
			-in the first run there is no previous frame, so this accounts for that
			-the first frame is saved to be used for the overlay after the accumulation has occurred
			-the height and width of the video are used to create an empty image for accumulation (accum_image)
		'''
		frame = imutils.resize(cap.read()[1],width=720)
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		if (i == 0):
			#first = copy.deepcopy(frame)
			if flag == 0:
				first_frame = copy.deepcopy(frame)
				#print("first",first_frame.shape)
			height, width = gray.shape[:2]
			accum_image = np.zeros((height, width), np.uint8)

		else:
			fgmask = fgbg.apply(gray)  # remove the background
			ret, th1 = cv2.threshold(fgmask, 2, 2, cv2.THRESH_BINARY)
			# add to the accumulated image
			accum_image = cv2.add(accum_image, th1)
			
		### comment this for website ###
		'''
		cv2.imshow('frame', frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
		'''
	
	color_image = cv2.applyColorMap(accum_image, cv2.COLORMAP_JET)#HOT#PINK
	result_overlay = cv2.addWeighted(first_frame, 0.8, color_image, 0.2, 0)
	convertedImage = np.hstack((result_overlay,first_frame))
	
	# save the final overlay image
	cv2.imwrite(image, result_overlay)
	heatmap=str(os.path.join(str(datetime.now()).split(" ")[0],name,"heatmap","heatmap.jpg"))
	dailyEntry(name,datetime.now(),Heatmap=heatmap)
	print(heatmap)
	print("Time taken to Generate Heat Map ",time.time()-t1,name)
	#cv2.imwrite('motionMap_org.jpg', result2)
	cap.stop()
	cv2.destroyAllWindows()








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
		data=curr.fetchall()
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

	for i in range(len(data)):
		## heatmap
		if data[i][6]==1:
			name.append(data[i][1])
			dvrIP.append(data[i][2])
			username.append(data[i][3])
			password.append(data[i][4])
			channel.append(data[i][5])
			rtsp.append("rtsp://{}:{}@{}/Streaming/Channels/{}".format(data[i][3],data[i][4],data[i][2],data[i][5]))

	#cap = cv2.VideoCapture(r'rtsp://admin:admin%40123@192.168.0.200/Streaming/Channels/201')
	print("Running on {} Cameras".format(len(data)))
	pool = Pool(len(data))
	#pool.map(motionMap ,zip(dvrIP, channel, username, password, mode, name))
	pool.map(motionMap,zip(rtsp,name))
'''


if __name__=='__main__':
		



	pass
	#get_from_database()
	get_from_file()
	
	#motionMap(inputVid)