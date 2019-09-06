from django.db import models
from datetime import date


# Create your models here.
class Voter(models.Model):
    vunm = models.CharField(max_length=100)
    vpass = models.CharField(max_length=100)
    voter_name = models.CharField(max_length=100)
    voter_dob = models.DateField(blank=True, default=date.today)
    gender=models.CharField(max_length=10)
    area = models.CharField(max_length=100)
    flag= models.IntegerField()
    flag1=models.IntegerField()
    verified = models.BooleanField(default=False)


class Candidate(models.Model):
    cunm = models.CharField(max_length=100)
    cpass = models.CharField(max_length=100)
    candidate_name = models.CharField(max_length=100)
    candidate_dob = models.DateField(blank=True, default=date.today)
    gender=models.CharField(max_length=10)
    area = models.CharField(max_length=100)
    party_name= models.CharField(max_length=100)
    Description = models.CharField(max_length=1000 , blank=True)
    logo = models.ImageField(upload_to="img0" ,blank=True)
    face = models.ImageField(upload_to="img1" ,blank=True)
    verified = models.BooleanField(default=False)

    #flag= models.IntegerField()
