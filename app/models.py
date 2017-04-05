from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


#jogu
class accounts(models.Model):
	accno=models.CharField(max_length=20)
	balance=models.DecimalField(max_digits=20,decimal_places=2)
	bankName=models.CharField(max_length=20)
	ifsc=models.CharField(max_length=20)

	def __str__(self):
		return self.accno


class uid(models.Model):
	aadhar=models.CharField(max_length=12)

	def __str__(self):
		return self.aadhar

# class holdings(models.Model):
#   shareHolder=models.ForeignKey('investor.InvestorProfile',on_delete=models.CASCADE)
#   startupName=models.ForeignKey('startup.StartupProfile',on_delete=models.CASCADE)
#   shareCount=models.IntegerField(validators=[MinValueValidator(1)])

#   def __str__(self):
#       return self.shareHolder.user.username


# class InvestorProfile(models.Model):
# 	# This line is required. Links UserProfile to a User model instance.
# 	user = models.OneToOneField(User)

# 	# new attributes
# 	aadhar = models.ForeignKey('uid', on_delete=models.CASCADE)
# 	accno = models.ForeignKey('accounts', on_delete=models.CASCADE)

# 	# Override the __unicode__() method to return out something meaningful!
# 	def __unicode__(self):
# 		return self.user.username
# 	def __str__(self):
# 		return self.user.username

# class StartupProfile(models.Model):
# 	# This line is required. Links UserProfile to a User model instance.
# 	user = models.OneToOneField(User)

# 	# new attributes
# 	aadhar = models.ForeignKey('uid', on_delete=models.CASCADE)
# 	accno = models.ForeignKey('accounts', on_delete=models.CASCADE)

# 	# Override the __unicode__() method to return out something meaningful!
# 	def __unicode__(self):
# 		return self.user.username

# 	def __str__(self):
# 		return self.user.username



# class stocks(models.Model):
# 	startup=models.ForeignKey('StartupProfile',on_delete=models.CASCADE)
# 	shareCount=models.IntegerField(validators=[MinValueValidator(1)])
# 	sharePrice=models.DecimalField(max_digits=20,decimal_places=2)

# 	def __str__(self):
# 		return self.startup.user.username







#TODO  class userManager():
# 	def isstartup(User):





#raman


# class UserProfile(models.Model):
#     # This line is required. Links UserProfile to a User model instance.
#     user = models.OneToOneField(User)
#
#     #new attributes
#     aadhar=models.ForeignKey('uid',on_delete=models.CASCADE)
#     accno=models.ForeignKey('accounts',on_delete=models.CASCADE)
#
#     # Override the __unicode__() method to return out something meaningful!
#     def __unicode__(self):
#         return self.user.username




