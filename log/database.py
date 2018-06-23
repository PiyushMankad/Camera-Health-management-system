import pymysql.cursors
import datetime
# Connect to the database
client = pymysql.connect(host='192.168.1.4',
                             user='user',
                             password='',
                             db='omni',
                             port=3306)
def select():
    try:
        cursor = client.cursor()
        date = datetime.datetime.now()
        query = "SELECT * FROM cameradb WHERE TimeStamp LIKE '2018-06-12%';"
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
            print "ID-{} code-{}    type-{}    time-{}    camID-{}   cam_status-{}     action-{}".format(id, code, type, time, cameraID,camera_status, action)
        client.commit()
        print(date)


    finally:
        client.close()

select()
