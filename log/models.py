from django.db import models
from django.contrib.sessions.models import Session
# Create your models here.
class cameradb(models.Model):
    EntryID = models.CharField(max_length=30)
    InfoCode = models.CharField(max_length=30)
    InfoType = models.CharField(max_length=50)
    TimeStamp = models.DateTimeField()
    CameraID = models.CharField(max_length=20)
    CameraStatus = models.CharField(max_length=50)
    Action = models.CharField(max_length=20)

    def __str__(self):
    	return self.EntryID