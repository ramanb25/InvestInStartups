from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class accounts(models.Model):
	accno=models.CharField(max_length=20)
	balance=models.DecimalField(max_digits=20,decimal_places=2)

	def __str__(self):
		return self.accno


class uid(models.Model):
	aadhar=models.CharField(max_length=12)

	def __str__(self):
		return self.aadhar


class Inv(models.Model):
	name=models.CharField(max_length=50)
	aadhar=models.ForeignKey('uid',on_delete=models.CASCADE)
	accno=models.ForeignKey('accounts',on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Sp(models.Model):
	name=models.CharField(max_length=100)
	aadhar=models.ForeignKey('uid',on_delete=models.CASCADE)
	accno=models.ForeignKey('accounts',on_delete=models.CASCADE)
	
	def __str__(self):
		return self.name

class holdings(models.Model):
	invName=models.ForeignKey('Inv',on_delete=models.CASCADE)
	soName=models.ForeignKey('Sp',on_delete=models.CASCADE)
	shareCount=models.IntegerField(validators=[MinValueValidator(1)])

	def __str__(self):
		return self.invName.name

class stocks(models.Model):
	soName=models.ForeignKey('Sp',on_delete=models.CASCADE)
	shareCount=models.IntegerField(validators=[MinValueValidator(1)])
	sharePrice=models.DecimalField(max_digits=20,decimal_places=2)

	def __str__(self):
		return self.soName.name



	