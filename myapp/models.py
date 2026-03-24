from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Department(models.Model):
    department_name=models.CharField(max_length=100)

class Designation(models.Model):
    designation=models.CharField(max_length=100)

class staff(models.Model):
    name=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    pincode=models.BigIntegerField()
    photo=models.FileField()
    LOGIN=models.ForeignKey(User,on_delete=models.CASCADE)
    DEPARTMENT=models.ForeignKey(Department,on_delete=models.CASCADE)

class Soldier_table(models.Model):
    LOGIN=models.ForeignKey(User,on_delete=models.CASCADE)
    STAFF=models.ForeignKey(staff,on_delete=models.CASCADE)
    DESIGNATION=models.ForeignKey(Designation,on_delete=models.CASCADE)
    soldier_name=models.CharField(max_length=100)
    soldier_image=models.FileField()
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    pincode = models.BigIntegerField()
    dob=models.DateField()
    private_key=models.TextField()
    public_key=models.TextField()

class complaints(models.Model):
    LOGIN = models.ForeignKey(User, on_delete=models.CASCADE)
    Complaint_des=models.CharField(max_length=100)
    Reply=models.CharField(max_length=100)
    date=models.DateField()

class Notification(models.Model):
    Title=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)
    date=models.DateField()

class data(models.Model):
    From_soldier = models.ForeignKey(Soldier_table, on_delete=models.CASCADE, related_name='From_user')
    To_soldier = models.ForeignKey(Soldier_table, on_delete=models.CASCADE, related_name='To_user')
    data=models.CharField(max_length=1000)
    steg_data_path=models.CharField(max_length=1000)
    date=models.DateField()
    latitude=models.FloatField()
    longitude=models.FloatField()







