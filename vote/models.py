from django.db import models
from datetime import date
from Registration.models import Candidate

# Create your models here.

class Election(models.Model):
    Edate = models.DateField(blank=True, default=date.today)
    StartTime = models.DateTimeField('date StartTime')
    EndTime = models.DateTimeField('date EndTime')

class Votes(models.Model):
    elec_id = models.ForeignKey(Election,on_delete=models.CASCADE)
    vid = models.ForeignKey(Candidate,on_delete=models.CASCADE)
    ElectionDate = models.DateField(blank=True, default=date.today)
    vote = models.IntegerField(default=0)
