from django.db import models
from datetime import date
from Registration.models import Candidate

# Create your models here.
class question(models.Model):
    Que = models.CharField(max_length=500)
    mnth = models.DateField(blank=True, default=date.today)

class Reward(models.Model):
    q_id = models.ForeignKey(question,on_delete=models.CASCADE)
    v_Id= models.ForeignKey(Candidate,on_delete=models.CASCADE)
    month = models.DateField(blank=True, default=date.today)
    reward = models.IntegerField(default=0)
