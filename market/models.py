from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from investor.models import InvestorProfile
from startup.models import StartupProfile

#jogu

class holdings(models.Model):
    investorName=models.ForeignKey('investor.InvestorProfile',on_delete=models.CASCADE)
    stockName=models.ForeignKey('startup.StartupProfile',on_delete=models.CASCADE)
    shareCount=models.IntegerField()

    def __str__(self):
        return self.investorName.user.username

class onSaleInvestor(models.Model):
    owner=models.ForeignKey('investor.InvestorProfile',on_delete=models.CASCADE)
    shareCount=models.ForeignKey('holdings',on_delete=models.CASCADE)
    sharePrice=models.IntegerField()

    def __str__(self):
        return self.owner.user.username

class onSaleStartup(models.Model):
    owner=models.ForeignKey('startup.StartupProfile',on_delete=models.CASCADE)
    shareCount=models.IntegerField()
    sharePrice=models.IntegerField()

    def __str__(self):
        return self.owner.startupName

#raman


# class UserProfile(models.Model):
#     # This line is required. Links UserProfile to a User model instance.
#     user = models.OneToOneField(User)

#     #new attributes
#     aadhar=models.ForeignKey('uid',on_delete=models.CASCADE)
#     accno=models.ForeignKey('accounts',on_delete=models.CASCADE)

#     # Override the __unicode__() method to return out something meaningful!
#     def __unicode__(self):
#         return self.user.username




