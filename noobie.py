import cv2
from imutils.video import FPS
from imutils.video import VideoStream
#from mysql	 import *
import time, glob, os
import numpy as np
from datetime import datetime, timedelta


## SEND EMAIL ALERTS
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def fancy_email_alert(name,ip,channel,reason,attach="None"):

	#sender="piyush@omnipresent.com"
	#receiver="bhawna@omnipresent.com"
	sender="sujayrpi@gmail.com"
	receiver=["piyush@omnipresenttech.com"]

	for index in range(len(receiver)):
		msg=MIMEMultipart()
		msg['From']=sender
		msg['to']=receiver[index]
		msg['Subject']="[	ATTENTION USER	]"
		body=" Your camera '{}' of IP '{} channel {}' has encountered {}.\n Please check below attachment".format(name,ip,channel,reason)
		

		html="""
		<html>
		  <body>
		    <p style="color:blue;">Hi,<br>
		       """+body+"""<br>
		       <a href="http://www.realpython.com">Real Python</a> 
		       has many great tutorials.
		    </p>
		  </body>
		</html>
		"""
		msg.attach(MIMEText(html,'html'))

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



def email_alert(name,ip,channel,reason,attach="None"):

	#sender="piyush@omnipresent.com"
	#receiver="bhawna@omnipresent.com"
	sender="sujayrpi@gmail.com"
	receiver="piyush@omnipresenttech.com"

	msg=MIMEMultipart()
	msg['From']=sender
	msg['to']=receiver
	msg['Subject']="[	ATTENTION USER	]"
	body=" Your camera '{}' of IP '{} channel {}' has encountered {}.\n Please check below attachment".format(name,ip,channel,reason)
	
	msg.attach(MIMEText(body,'plain'))

	if not attach=="None":
		for i in range(len(attach)):

			'''
			'''
			attachment=open(attach[i],"rb")
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
		s.sendmail(sender, receiver, text)
		# terminating the session
		s.quit()
	except:
		print("Email not sent, No Internet Connection")



def intelligent_summary(original,heatmap):
	img1=cv2.imread(original)
	img2=cv2.imread(heatmap)
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
	move_percent=hist[255]/(row*col)
	print(hist[255],move_percent)




if __name__ == '__main__':
	#attach=[r"C:\Users\Ayush\Pictures\street.jpg",r"C:\Users\Ayush\Pictures\quad.jpg",r"C:\Users\Ayush\Pictures\surface.png"]

	#fancy_email_alert("name","ip","channel","reason")
	intelligent_summary(r"E:\CameraHealthManagementSystem\static\2019-06-13\cabin\heatmap\original3.jpg",r"E:\CameraHealthManagementSystem\static\2019-06-13\cabin\heatmap\heatmap3.jpg")

	img=r"C:\Users\Ayush\Pictures\street.jpg"
	location=r"E:\CHMS\2019-05-14\overhead\tampered"
	'''
	for img in sorted(glob.glob(location+"/*.png")):
            #print(img)
            statinfo=os.stat(img)
            if statinfo.st_size<5:
                continue
            frame=cv2.imread(img)
            print(statinfo.st_size)
            cv2.putText(frame,'Tampered Frame',(20,40), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(0,0,255),2)
            cv2.imshow("frame",frame)
            cv2.waitKey(0)
            break
	'''

	d=str(datetime.now()).split(".")[0].split(" ")[1].split(":")
	print(d[0]+"_"+d[1])
