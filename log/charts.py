
import pymysql.cursors

def doughnut(data='2018-06'):	#prints the doughnut graph
	try:
		client = pymysql.connect(host='192.168.1.27',
					 user='omni',
					 password='omni1234',
					 db='omni',
					 port=3306)
		cursor = client.cursor()
		data = str(data)+"%"
		query = "SELECT COUNT(InfoCode) FROM tablecameraactivity WHERE TimeStamp LIKE '{}' AND InfoCode = '0c0001';".format(data)
		cursor.execute(query)
		results1=cursor.fetchall()

		query = "SELECT COUNT(InfoCode) FROM tablecameraactivity WHERE TimeStamp LIKE '{}' AND InfoCode = '0c0010';".format(data)
		cursor.execute(query)
		results2=cursor.fetchall()

		query = "SELECT COUNT(InfoCode) FROM tablecameraactivity WHERE TimeStamp LIKE '{}' AND InfoCode = '0c0011';".format(data)
		cursor.execute(query)
		results3=cursor.fetchall()

		query = "SELECT COUNT(InfoCode) FROM tablecameraactivity WHERE TimeStamp LIKE '{}' AND InfoCode = '0c0100';".format(data)
		cursor.execute(query)
		results4=cursor.fetchall()

		query = "SELECT COUNT(InfoCode) FROM tablecameraactivity WHERE TimeStamp LIKE '{}' AND InfoCode = '0c0101';".format(data)
		cursor.execute(query)
		results5=cursor.fetchall()

		query = "SELECT COUNT(InfoCode) FROM tablecameraactivity WHERE TimeStamp LIKE '{}' AND InfoCode = '0w0001';".format(data)
		cursor.execute(query)
		results6=cursor.fetchall()

		query = "SELECT COUNT(InfoCode) FROM tablecameraactivity WHERE TimeStamp LIKE '{}' AND InfoCode = '0w0010';".format(data)
		cursor.execute(query)
		results7=cursor.fetchall()

		query = "SELECT COUNT(InfoCode) FROM tablecameraactivity WHERE TimeStamp LIKE '{}' AND InfoCode = '0w0100';".format(data)
		cursor.execute(query)
		results8=cursor.fetchall()

		query = "SELECT COUNT(InfoCode) FROM tablecameraactivity WHERE TimeStamp LIKE '{}' AND InfoCode = '0x0001';".format(data)
		cursor.execute(query)
		results9=cursor.fetchall()

		query = "SELECT COUNT(InfoCode) FROM tablecameraactivity WHERE TimeStamp LIKE '{}' AND InfoCode = '0x0010';".format(data)
		cursor.execute(query)
		results10=cursor.fetchall()

		query = "SELECT COUNT(InfoCode) FROM tablecameraactivity WHERE TimeStamp LIKE '{}' AND InfoCode = '0x0011';".format(data)
		cursor.execute(query)
		results11=cursor.fetchall()

		query = "SELECT COUNT(InfoCode) FROM tablecameraactivity WHERE TimeStamp LIKE '{}' AND InfoCode = '0x0100';".format(data)
		cursor.execute(query)
		results12=cursor.fetchall()
		client.commit()

	except:
		print("				NHI CHALEGA		")
	finally:
		results=[results12,results11,results10,results9,results8,results7,results6,results5,results4,results3,results2,results1]
		#print(results)
		return results
		client.close()


''' the following function takes in a range of date ie start date and end date for showing the stats in between'''

def doughnut_range(start,end):	#prints the doughnut graph
	try:
		client = pymysql.connect(host='192.168.1.27',
					 user='omni',
					 password='omni1234',
					 db='omni',
					 port=3306)
		cursor = client.cursor()
		start = str(start)+"%"
		end = str(end)+"%"
		query = "SELECT COUNT(InfoCode) FROM tablecameraactivity WHERE TimeStamp>='{}' AND TimeStamp<='{}' AND InfoCode = '0c0001';".format(start,end)
		cursor.execute(query)
		results1=cursor.fetchall()

		query = "SELECT COUNT(InfoCode) FROM tablecameraactivity WHERE TimeStamp>='{}' AND TimeStamp<='{}' AND InfoCode = '0c0010';".format(start,end)
		cursor.execute(query)
		results2=cursor.fetchall()

		query = "SELECT COUNT(InfoCode) FROM tablecameraactivity WHERE TimeStamp>='{}' AND TimeStamp<='{}' AND InfoCode = '0c0011';".format(start,end)
		cursor.execute(query)
		results3=cursor.fetchall()

		query = "SELECT COUNT(InfoCode) FROM tablecameraactivity WHERE TimeStamp>='{}' AND TimeStamp<='{}' AND InfoCode = '0c0100';".format(start,end)
		cursor.execute(query)
		results4=cursor.fetchall()

		query = "SELECT COUNT(InfoCode) FROM tablecameraactivity WHERE TimeStamp>='{}' AND TimeStamp<='{}' AND InfoCode = '0c0101';".format(start,end)
		cursor.execute(query)
		results5=cursor.fetchall()

		query = "SELECT COUNT(InfoCode) FROM tablecameraactivity WHERE TimeStamp>='{}' AND TimeStamp<='{}' AND InfoCode = '0w0001';".format(start,end)
		cursor.execute(query)
		results6=cursor.fetchall()

		query = "SELECT COUNT(InfoCode) FROM tablecameraactivity WHERE TimeStamp>='{}' AND TimeStamp<='{}' AND InfoCode = '0w0010';".format(start,end)
		cursor.execute(query)
		results7=cursor.fetchall()

		query = "SELECT COUNT(InfoCode) FROM tablecameraactivity WHERE TimeStamp>='{}' AND TimeStamp<='{}' AND InfoCode = '0w0100';".format(start,end)
		cursor.execute(query)
		results8=cursor.fetchall()

		query = "SELECT COUNT(InfoCode) FROM tablecameraactivity WHERE TimeStamp>='{}' AND TimeStamp<='{}' AND InfoCode = '0x0001';".format(start,end)
		cursor.execute(query)
		results9=cursor.fetchall()

		query = "SELECT COUNT(InfoCode) FROM tablecameraactivity WHERE TimeStamp>='{}' AND TimeStamp<='{}' AND InfoCode = '0x0010';".format(start,end)
		cursor.execute(query)
		results10=cursor.fetchall()

		query = "SELECT COUNT(InfoCode) FROM tablecameraactivity WHERE TimeStamp>='{}' AND TimeStamp<='{}' AND InfoCode = '0x0011';".format(start,end)
		cursor.execute(query)
		results11=cursor.fetchall()

		query = "SELECT COUNT(InfoCode) FROM tablecameraactivity WHERE TimeStamp>='{}' AND TimeStamp<='{}' AND InfoCode = '0x0100';".format(start,end)
		cursor.execute(query)
		results12=cursor.fetchall()
		client.commit()

	except:
		print("				NHI CHALEGA		")
	finally:
		results=[results12,results11,results10,results9,results8,results7,results6,results5,results4,results3,results2,results1]
		#print(results)
		return results
		client.close()

