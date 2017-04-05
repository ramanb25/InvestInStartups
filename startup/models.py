from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from app.models import accounts,uid


class StartupProfile(models.Model):
	# This line is required. Links UserProfile to a User model instance.
	user = models.OneToOneField(User)

	# new attributes
	aadhar = models.OneToOneField('app.uid', on_delete=models.CASCADE)
	bank=models.CharField(max_length=20)
	accno = models.OneToOneField('app.accounts', on_delete=models.CASCADE)
	ifsc=models.CharField(max_length=11)
	#TODO make it primary key
	startupName=models.CharField(max_length=100)
	stockName=models.CharField(max_length=100)
	shareCount=models.IntegerField(validators=[MinValueValidator(1)])
	sharePrice=models.DecimalField(max_digits=20,decimal_places=2)

	# Override the __unicode__() method to return out something meaningful!
	# def __unicode__(self):
	# 	return self.user.username

	def __str__(self):
		return self.startupName
