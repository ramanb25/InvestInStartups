from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


#jogu
class accounts(models.Model):
	bankName=models.CharField(max_length=20)
	ifsc=models.CharField(max_length=20)
	accno=models.CharField(max_length=20)
	balance=models.DecimalField(max_digits=20,decimal_places=2)

	def __str__(self):
		return self.accno


class uid(models.Model):
	aadhar=models.CharField(max_length=12)

	def __str__(self):
		return self.aadhar


