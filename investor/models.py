from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from app.models import accounts,uid


class InvestorProfile(models.Model):
	# This line is required. Links UserProfile to a User model instance.
	user = models.OneToOneField(User)

	# new attributes
	aadhar = models.OneToOneField('app.uid', on_delete=models.CASCADE)
	
	accountInfo = models.OneToOneField('app.accounts', on_delete=models.CASCADE)

	# Override the __unicode__() method to return out something meaningful!
	def __unicode__(self):
		return self.user.username
	def __str__(self):
		return self.user.username




