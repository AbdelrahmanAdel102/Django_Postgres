from django.db import models

class Myuser(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=16)

class Intake(models.Model):
    id=models.AutoField(primary_key=True)
    intakeName = models.CharField(max_length=30)
    startdate = models.DateField()
    enddate = models.DateField()

class Track(models.Model):
    name=models.CharField(max_length=50)

class Students(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    intakeid = models.ForeignKey('Intake', on_delete=models.CASCADE)
    trackid = models.ForeignKey('Track', on_delete=models.CASCADE)