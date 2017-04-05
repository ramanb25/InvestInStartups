from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from investor.models import InvestorProfile
from startup.models import StartupProfile


#raman
class onsale(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    startup=models.ForeignKey('startup.StartupProfile')
    stockpercentage=models.FloatField()
    stockprice=models.FloatField()
    # onhold=models.BooleanField(default=0)
    # timeonhold=models.DateTimeField()
    #TODO Dont allow multiple sale or put id here

class ownership(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    startup=models.ForeignKey('startup.StartupProfile')
    sharepercentage=models.FloatField()

class transactions(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name='owner')
    buyer=models.ForeignKey(User,on_delete=models.CASCADE,related_name='buyer')
    stockpercentage=models.FloatField()
    stockprice=models.FloatField()
    startup=models.ForeignKey('startup.StartupProfile')
    timestamp=models.DateTimeField()





