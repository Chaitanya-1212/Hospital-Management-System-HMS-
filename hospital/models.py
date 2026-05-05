from django.db import models
from django.conf import settings
#settings.AUTH_USER_MODEL

# Create your models here.

class DoctorModel(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=50,null=True,blank=True)
    specialization=models.CharField(max_length=50,null=True,blank=True)
    fees=models.IntegerField(null=True,blank=True)
    days=models.IntegerField(null=True,blank=True)
    contact=models.CharField(max_length=15,null=True,blank=True)
    
    status=models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.name

class PatientModel(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=50,null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    contact=models.CharField(max_length=15,null=True,blank=True)

    def __str__(self):
        return self.name

class AppointmentModel(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
    doctor=models.ForeignKey(DoctorModel,on_delete=models.CASCADE,null=True,blank=True)
    patient=models.ForeignKey(PatientModel,on_delete=models.CASCADE,null=True,blank=True)
    date=models.DateField(null=True,blank=True)
    time=models.TimeField(null=True,blank=True)
    
    
    email=models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return f"{self.patient.name} - {self.doctor.name}"

class ProfileModel(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=50,null=True,blank=True)
    contact=models.CharField(max_length=15,null=True,blank=True)
    address=models.TextField(max_length=50,null=True,blank=True)
    email=models.CharField(max_length=50,null=True,blank=True)
    
    profile_pic=models.FileField(upload_to="prof_pic",null=True,blank=True)

    def __str__(self):
        return self.name

class Appointment_done_Model(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
    doctor=models.ForeignKey(DoctorModel,on_delete=models.CASCADE,null=True,blank=True)
    patient=models.ForeignKey(PatientModel,on_delete=models.CASCADE,null=True,blank=True)
    date=models.DateField(null=True,blank=True)
    time=models.TimeField(null=True,blank=True)
    email=models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return f"{self.patient.name} - {self.doctor.name}"