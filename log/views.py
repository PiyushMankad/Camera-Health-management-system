
#log/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from forms import userform
from forms import customise
from django.http import HttpResponseRedirect
from django.urls import reverse
import pymysql.cursors
from django.contrib.sessions.models import Session
from datetime import datetime, timedelta
# Create your views here.
# this login required decorator is to not allow to any  
# view without authenticating

@login_required(login_url="login/")
def home(request):
	#request.session.set_expiry(30)		#set the session time which is in seconds
	request.session['data']=datetime.strftime(datetime.now(),'%Y-%m-%d')
	today=datetime.strftime(datetime.now(),'%Y-%m-%d')
	inactiv=inactive(today)
	war=warnings(today)
	sus = suspicious(today)
	cri=critical(today)
	request.session['']
	return render(request,"home.html",{'inactive':inactiv,'warnings':war,'suspicious':sus,'critical':cri})

@login_required(login_url="/login/")	
def chart(request):
	return render(request,"chart.html")

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
		db=range(weekend,weekstart)
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
		db=range(weekend,weekstart)
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
		db=range(start,end)
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
		datetime.strptime(data, '%Y-%m-%d')
		request.session['data']=data       #setting new session date
		da=data.split("-")
		data=da[0]+"-"+da[1]+"%"
		db=select(data)
		inactiv=inactive(data)
		war=warnings(data)
		sus = suspicious(data)
		cri=critical(data)
		return render(request,"monthly.html",{'form': form,'data':data,'db':db,'inactive':inactiv,'warnings':war,'suspicious':sus,'critical':cri})
	else:
		data=request.session['data']
		da=data.split("-")
		data=da[0]+"-"+da[1]+"%"
		db=select(data)
		inactiv=inactive(data)
		war=warnings(data)
		sus = suspicious(data)
		cri=critical(data)
		return render(request,"monthly.html",{'form': form,'data':data,'db':db,'inactive':inactiv,'warnings':war,'suspicious':sus,'critical':cri})
		

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
		client = pymysql.connect(host='localhost',
							 user='user',
							 password='user',
							 db='omni',
							 port=3306)
		cursor = client.cursor()
		data = str(data)+"%"
		query = "SELECT * FROM cameradb WHERE TimeStamp LIKE '{}';".format(data)
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

def range(start,end):	#shows the database in the selected range used in week and custom range
	try:
		client = pymysql.connect(host='localhost',
							 user='user',
							 password='user',
							 db='omni',
							 port=3306)
		cursor = client.cursor()
		start = str(start)
		end = str(end)
		query = "SELECT * FROM cameradb WHERE TimeStamp>='{}' AND TimeStamp<='{}';".format(start,end)
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

'''def re_week(data):	#weekly's query function
	try:
		client = pymysql.connect(host='localhost',
							 user='user',
							 password='user',
							 db='omni',
							 port=3306)
		cursor = client.cursor()
		d = data - timedelta(days=7)
		data = str(data)+"%"
		query = "SELECT * FROM cameradb WHERE TimeStamp>='{}' AND TimeStamp<'{}';".format(d,data)
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
	except:
		print("						NHI CHALEGA				")
	finally:
		return results
		client.close()

'''

''' the following functions are for selecting inactive cameras, warnings,  suspicious , criticals which are given on selection of a particular date 
	for eg you require ONE value in the query for showing the data of the selected date and selected month'''  


def inactive(data):	#no of inactive cameras
	try:
		client = pymysql.connect(host='localhost',
							 user='user',
							 password='user',
							 db='omni',
							 port=3306)
		cursor = client.cursor()
		data = str(data)+"%"
		query = "SELECT COUNT(CameraStatus) FROM cameradb WHERE TimeStamp LIKE '{}' AND CameraStatus LIKE 'INACTIVE%';".format(data)
		cursor.execute(query)
		results=cursor.fetchall()
		client.commit()
	finally:
		return results
		client.close()

def warnings(data):	#no of warnings
	try:
		client = pymysql.connect(host='localhost',
							 user='user',
							 password='user',
							 db='omni',
							 port=3306)
		cursor = client.cursor()
		data = str(data)+"%"
		query = "SELECT COUNT(InfoType) FROM cameradb WHERE TimeStamp LIKE '{}' AND InfoType LIKE 'Warning%';".format(data)
		cursor.execute(query)
		results=cursor.fetchall()
		client.commit()
	finally:
		return results
		client.close()
def suspicious(data):	#no of suspicious activity
	try:
		client = pymysql.connect(host='localhost',
							 user='user',
							 password='user',
							 db='omni',
							 port=3306)
		cursor = client.cursor()
		data = str(data)+"%"
		query = "SELECT COUNT(InfoType) FROM cameradb WHERE TimeStamp LIKE '{}' AND InfoType LIKE '% Suspicious%';".format(data)
		cursor.execute(query)
		results=cursor.fetchall()
		client.commit()
	finally:
		return results
		client.close()
def critical(data):	#critical cameras
	try:
		client = pymysql.connect(host='localhost',
							 user='user',
							 password='user',
							 db='omni',
							 port=3306)
		cursor = client.cursor()
		data = str(data)+"%"
		query = "SELECT COUNT(InfoType) FROM cameradb WHERE TimeStamp LIKE '{}' AND InfoType LIKE 'Critical%';".format(data)
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
		client = pymysql.connect(host='localhost',
							 user='user',
							 password='user',
							 db='omni',
							 port=3306)
		cursor = client.cursor()
		start = str(start)+"%"
		end = str(end)+"%"
		query = "SELECT COUNT(CameraStatus) FROM cameradb WHERE TimeStamp>='{}' AND TimeStamp<'{}' AND CameraStatus LIKE 'INACTIVE%';".format(start,end)
		cursor.execute(query)
		results=cursor.fetchall()
		client.commit()
	finally:
		return results
		client.close()

def warnings_range(start,end):	#no of warnings
	try:
		client = pymysql.connect(host='localhost',
							 user='user',
							 password='user',
							 db='omni',
							 port=3306)
		cursor = client.cursor()
		start = str(start)+"%"
		end = str(end)+"%"
		query = "SELECT COUNT(InfoType) FROM cameradb WHERE TimeStamp >='{}'  AND TimeStamp<'{}' AND InfoType LIKE 'Warning%';".format(start,end)
		cursor.execute(query)
		results=cursor.fetchall()
		client.commit()
	finally:
		return results
		client.close()
def suspicious_range(start,end):	#no of suspicious activity
	try:
		client = pymysql.connect(host='localhost',
							 user='user',
							 password='user',
							 db='omni',
							 port=3306)
		cursor = client.cursor()
		start = str(start)+"%"
		end = str(end)+"%"
		query = "SELECT COUNT(InfoType) FROM cameradb WHERE TimeStamp >='{}'  AND TimeStamp<'{}' AND InfoType LIKE '% Suspicious%';".format(start,end)
		cursor.execute(query)
		results=cursor.fetchall()
		client.commit()
	finally:
		return results
		client.close()
def critical_range(start,end):	#critical cameras
	try:
		client = pymysql.connect(host='localhost',
							 user='user',
							 password='user',
							 db='omni',
							 port=3306)
		cursor = client.cursor()
		start = str(start)+"%"
		end = str(end)+"%"
		query = "SELECT COUNT(InfoType) FROM cameradb WHERE TimeStamp >='{}'  AND TimeStamp<'{}' AND InfoType LIKE 'Critical%';".format(start,end)
		cursor.execute(query)
		results=cursor.fetchall()
		client.commit()
	finally:
		return results
		client.close()
