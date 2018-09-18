
#log/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from forms import userform
from forms import customise
from django.http import HttpResponseRedirect
from django.urls import reverse
import pymysql.cursors
from django.contrib.sessions.models import Session
from datetime import datetime, timedelta, date, time
from log import charts
from log import VideoWriter
import calendar
import requests
from django.views.generic import TemplateView
import os
import moviepy.editor as mpe
# Create your views here.
# this login required decorator is to not allow to any  
# view without authenticating

client = pymysql.connect(host='192.168.1.27',
					 user='omni',
					 password='omni1234',
					 db='omni',
					 port=3306)
@login_required(login_url="login/")
def home(request):
	#request.session.set_expiry(30)		#set the session time which is in seconds
	request.session['data']=datetime.strftime(datetime.now(),'%Y-%m-%d')
	today=datetime.strftime(datetime.now(),'%Y-%m-%d')
	inactiv=inactive(today)
	war=warnings(today)
	sus = suspicious(today)
	cri=critical(today)
	chart_today=charts.doughnut(today)
	today = datetime.strptime(today,'%Y-%m-%d')
	end = today - timedelta(days=7)
	chart_week=charts.doughnut_range(end,today)
	arg = str(today)
	da = arg.split('-')
	month = da[0]+"-"+da[1]
	chart_month=charts.doughnut(month)
	return render(request,"home.html",{'inactive':inactiv,'warnings':war,'suspicious':sus,'critical':cri,'day':chart_today,'week':chart_week,'month':chart_month})

@login_required(login_url="/login/")	
def chart(request):
	day=request.session['data']							
	results=charts.doughnut(day)
	return render(request,"chart.html",{'info':results,'day':day})

@login_required(login_url="/login/")	
def weekly(request):			#shows the selected database  of the past week
	print(request.session['data'])
	form=userform(request.POST)
	if form.is_valid():
		data = form.cleaned_data['data']
		data=str(data)
		start=datetime.strptime(data, '%Y-%m-%d')
		weekend = start - timedelta(days=7)
		weekstart=start + timedelta(days=1)
		print(weekend)
		print(weekstart)
		request.session['data']=data       #setting new session date
		db=ranges(weekend,weekstart)
		inactiv=inactive_range(weekend,weekstart)
		war=warnings_range(weekend,weekstart)
		sus = suspicious_range(weekend,weekstart)
		cri=critical_range(weekend,weekstart)
		return render(request,"weekly.html",{'form': form,'db':db,'start':start,'end':weekend,'inactive':inactiv,'warnings':war,'suspicious':sus,'critical':cri})
	else:
		data=request.session['data']
		start=datetime.strptime(data, '%Y-%m-%d')
		weekend = start - timedelta(days=7)
		weekstart=start + timedelta(days=1)
		db=ranges(weekend,weekstart)
		inactiv=inactive_range(weekend,weekstart)
		war=warnings_range(weekend,weekstart)
		sus = suspicious_range(weekend,weekstart)
		cri=critical_range(weekend,weekstart)
		return render(request,"weekly.html",{'form': form,'db':db,'start':start,'end':weekend,'inactive':inactiv,'warnings':war,'suspicious':sus,'critical':cri})

@login_required(login_url="/login/")	
def custom(request):			#shows the selected database in custom range 
	print(request.session['data'])
	form=customise(request.POST)
	if form.is_valid():
		start = form.cleaned_data['start']
		end = form.cleaned_data['end']
		start=str(start)
		end=str(end)
		datetime.strptime(start, '%Y-%m-%d')
		datetime.strptime(end, '%Y-%m-%d')
		db=ranges(start,end)
		inactiv=inactive_range(start,end)
		war=warnings_range(start,end)
		sus = suspicious_range(start,end)
		cri=critical_range(start,end)
		return render(request,"custom.html",{'form': form,'start':start,'end':end,'db':db,'inactive':inactiv,'warnings':war,'suspicious':sus,'critical':cri})
	else:
		return render(request,"custom.html",{'form': form})

@login_required(login_url="/login/")	
def monthly(request):		#shows the selected database in the month
	print(request.session['data'])
	form=userform(request.POST)
	print(request.session['data'])
	if form.is_valid():
		data = form.cleaned_data['data']
		data=str(data)
		request.session['data']=data       #setting new session date
		da=data.split("-")
		data=da[0]+"-"+da[1]
		db=select(data)
		inactiv=inactive(data)
		war=warnings(data)
		sus = suspicious(data)
		cri=critical(data)
		return render(request,"monthly.html",{'form': form,'data':da[1],'db':db,'inactive':inactiv,'warnings':war,'suspicious':sus,'critical':cri})
	else:
		data=request.session['data']
		da=data.split("-")
		data=da[0]+"-"+da[1]+"%"
		db=select(data)
		inactiv=inactive(data)
		war=warnings(data)
		sus = suspicious(data)
		cri=critical(data)
		return render(request,"monthly.html",{'form': form,'data':da[1],'db':db,'inactive':inactiv,'warnings':war,'suspicious':sus,'critical':cri})
		

@login_required(login_url="/login/")
def report(request):			#shows the selected database of the date
	print(request.session['data'])
	form=userform(request.POST)
	if form.is_valid():
		data = form.cleaned_data['data']
		data=str(data)
		datetime.strptime(data, '%Y-%m-%d')
		request.session['data']=data         #setting new session date
		db=select(data)
		inactiv=inactive(data)
		war=warnings(data)
		sus = suspicious(data)
		cri=critical(data)
		return render(request,"report.html",{'form': form,'data':data,'db':db,'inactive':inactiv,'warnings':war,'suspicious':sus,'critical':cri})
	else:
		data=request.session['data']
		db=select(data)
		inactiv=inactive(data)
		war=warnings(data)
		sus = suspicious(data)
		cri=critical(data)
		return render(request,"report.html",{'form': form,'data':data,'db':db,'inactive':inactiv,'warnings':war,'suspicious':sus,'critical':cri})

def select(data):	#shows the database on a particular date/month
	try:
		global client
		cursor = client.cursor()
		data = str(data)+"%"
		query = "SELECT * FROM tablecameraactivity WHERE TimeStamp LIKE '{}';".format(data)
		cursor.execute(query)
		results=cursor.fetchall()
		
		for row in results:
			id=row[0]
			code=row[1]
			type=row[2]
			time=row[3]
			cameraID=row[4]
			camera_status=row[5]
			action= row[6]
				   
		client.commit()
	finally:
		return results
		client.close()

def ranges(start,end):	#shows the database in the selected range used in week and custom range
	try:
		global client 
		cursor = client.cursor()
		start = str(start)
		end = str(end)
		query = "SELECT * FROM tablecameraactivity WHERE TimeStamp>='{}' AND TimeStamp<='{}';".format(start,end)
		cursor.execute(query)
		results=cursor.fetchall()
		for row in results:
			id=row[0]
			code=row[1]
			type=row[2]
			time=row[3]
			cameraID=row[4]
			camera_status=row[5]
			action= row[6]
				   
		client.commit()
	finally:
		return results
		client.close()

''' the following functions are for selecting inactive cameras, warnings,  suspicious , criticals which are given on selection of a particular date 
	for eg you require ONE value in the query for showing the data of the selected date and selected month'''  


def inactive(data):	#no of inactive cameras
	try:
		global client
		cursor = client.cursor()
		data = str(data)+"%"
		query = "SELECT COUNT(CameraStatus) FROM tablecameraactivity WHERE TimeStamp LIKE '{}' AND CameraStatus LIKE 'INACTIVE%';".format(data)
		cursor.execute(query)
		results=cursor.fetchall()
		client.commit()

	except:
		print(' 		Cant access database- run Xampp')
	finally:
		return results
		client.close()

def warnings(data):	#no of warnings
	try:
		global client
		cursor = client.cursor()
		data = str(data)+"%"
		query = "SELECT COUNT(InfoType) FROM tablecameraactivity WHERE TimeStamp LIKE '{}' AND InfoType LIKE 'Warning%';".format(data)
		cursor.execute(query)
		results=cursor.fetchall()
		client.commit()
	finally:
		return results
		client.close()

def suspicious(data):	#no of suspicious activity
	try:
		global client 
		cursor = client.cursor()
		data = str(data)+"%"
		query = "SELECT COUNT(InfoType) FROM tablecameraactivity WHERE TimeStamp LIKE '{}' AND InfoType LIKE '% Suspicious%';".format(data)
		cursor.execute(query)
		results=cursor.fetchall()
		client.commit()
	finally:
		return results
		client.close()

def critical(data):	#critical cameras
	try:
		global client
		cursor = client.cursor()
		data = str(data)+"%"
		query = "SELECT COUNT(InfoType) FROM tablecameraactivity WHERE TimeStamp LIKE '{}' AND InfoType LIKE 'Critical%';".format(data)
		cursor.execute(query)
		results=cursor.fetchall()
		client.commit()
	finally:
		return results
		client.close()


''' the following functions are for selecting inactive cameras, warnings,  suspicious , criticals which are given in a range 
	for eg you require TWO values in the query for showing the data of the last week and custom dates'''  


def inactive_range(start,end):	#no of inactive cameras
	try:
		global client
		cursor = client.cursor()
		start = str(start)+"%"
		end = str(end)+"%"
		query = "SELECT COUNT(CameraStatus) FROM tablecameraactivity WHERE TimeStamp>='{}' AND TimeStamp<'{}' AND CameraStatus LIKE 'INACTIVE%';".format(start,end)
		cursor.execute(query)
		results=cursor.fetchall()
		client.commit()
	finally:
		return results
		client.close()

def warnings_range(start,end):	#no of warnings
	try:
		global client
		cursor = client.cursor()
		start = str(start)+"%"
		end = str(end)+"%"
		query = "SELECT COUNT(InfoType) FROM tablecameraactivity WHERE TimeStamp >='{}'  AND TimeStamp<'{}' AND InfoType LIKE 'Warning%';".format(start,end)
		cursor.execute(query)
		results=cursor.fetchall()
		client.commit()
	finally:
		return results
		client.close()

def suspicious_range(start,end):	#no of suspicious activity
	try:
		global client
		cursor = client.cursor()
		start = str(start)+"%"
		end = str(end)+"%"
		query = "SELECT COUNT(InfoType) FROM tablecameraactivity WHERE TimeStamp >='{}'  AND TimeStamp<'{}' AND InfoType LIKE '% Suspicious%';".format(start,end)
		cursor.execute(query)
		results=cursor.fetchall()
		client.commit()
	finally:
		return results
		client.close()

def critical_range(start,end):	#critical cameras
	try:
		global client
		cursor = client.cursor()
		start = str(start)+"%"
		end = str(end)+"%"
		query = "SELECT COUNT(InfoType) FROM tablecameraactivity WHERE TimeStamp >='{}'  AND TimeStamp<'{}' AND InfoType LIKE 'Critical%';".format(start,end)
		cursor.execute(query)
		results=cursor.fetchall()
		client.commit()
	finally:
		return results
		client.close()

'''the followin functions are used to show the calendar using an inbuilt HTMLcalendar function''' 

@login_required(login_url="login/")
def calend(request,day='2018-06-25'):
	today=date.today()
	year=today.year
	month1=today.month
		
	cal = calendar.HTMLCalendar()
	month_days = cal.itermonthdays(year, month1)
	lst = []
	
	lst1=[]
	for day in month_days:
		lst1.append(day)
		for n, i in enumerate(lst1):
			if i == 0:
				lst1[n]=''
	x=len(lst1)/7
	d=0
	for j in range(0,x):
		lst2=[]
		for i in range(d,d+7):
			lst2.append(lst1[i])
		lst.append(lst2)
		d+=7
		lsd, folder, length=carousel('2018-06-25')
	return render(request,"calendar.html",{'lst':lst,'year':year,'range':range(0,7),'month1':month1,'list':lsd,'folder':folder,'length':length,'day':day})

	
def decrement_month(month1, year):
	month1=int(month1)
	year=int(year)
	prev_month = month1-1
	if prev_month < 1:
		prev_month = 12
		prev_year=year-1
	else:
		prev_year = year
	return prev_month, prev_year
     
def increment_month(month1, year):
	month1=int(month1)
	year=int(year)
	next_month = month1 + 1
	if next_month >12:
    		next_month = 1
       		next_year=year+1
	else:
			next_year = year
	return next_month, next_year

	
@login_required(login_url="login/")	
def prev(request):
	month = request.GET.get('m')
	year = request.GET.get('y')	
	month,year=decrement_month(month,year)
	cal = calendar.HTMLCalendar()
	month_days = cal.itermonthdays(year, month)
	lst = []
	
	lst1=[]
	for day in month_days:
		lst1.append(day)
		for n, i in enumerate(lst1):
			if i == 0:
				lst1[n]=''
	x=len(lst1)/7
	d=0
	for j in range(0,x):
		lst2=[]
		for i in range(d,d+7):
			lst2.append(lst1[i])
		lst.append(lst2)
		d+=7
	return render(request,"calendar.html",{'lst':lst,'year':year,'range':range(0,7),'month1':month,})


@login_required(login_url="login/")	
def next(request):
	month = request.GET.get('m')
	year = request.GET.get('y')	
	month,year=increment_month(month,year)
	cal = calendar.HTMLCalendar()
	month_days = cal.itermonthdays(year, month)
	lst = []
	
	lst1=[]
	for day in month_days:
		lst1.append(day)
		for n, i in enumerate(lst1):
			if i == 0:
				lst1[n]=''
	x=len(lst1)/7
	d=0
	for j in range(0,x):
		lst2=[]
		for i in range(d,d+7):
			lst2.append(lst1[i])
		lst.append(lst2)
		d+=7
	return render(request,"calendar.html",{'lst':lst,'year':year,'range':range(0,7),'month1':month,})


		
''' the following functions will show the video for the selected date through the calendar'''

def video(request):
	day=request.GET.get('day')
	d=datetime.strptime(day,'%d/%m/%Y')
	day=datetime.strftime(d,'%Y-%m-%d')
	#print(day)
	request.session['data']=day

	#VideoWriter.VideoWriter(day)
	clip=mpe.VideoFileClip(r"C:\Users\omni\Documents\Camera Health management system\static\2018-06-25.mp4")
	audio=mpe.AudioFileClip(r"C:\Users\omni\Documents\Camera Health management system\static\LetHerGo.mp3")
	audio.duration=clip.duration
	final=clip.set_audio(audio)
	final.write_videofile(r"C:\Users\omni\Documents\Camera Health management system\static\test.mp4",fps=24)
	myday=calend(request)		#give [day] as an arguement inhere
	return myday


'''this function is used to display the various images in the folder'''
path="C:/Users/omni/Documents/Camera Health management system/static/"

def carousel(tdate):
    folder=path+str(tdate)
    lst=os.listdir(folder)
    length = len(lst)
    folder='/'+tdate+'/'
    return lst, folder, length
