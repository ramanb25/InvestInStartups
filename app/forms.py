# # #raman
# from .models import accounts
# # from django.contrib.auth.models import User
# from django import forms


# class AccountForm(forms.ModelForm):
# 	class Meta:
# 		model = accounts
# 		field = '__all__'
#
# class UserForm(forms.ModelForm):
#     #username is already defined passsword is viewable
#     password = forms.CharField(widget=forms.PasswordInput())
#
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')
#
# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ('aadhar', 'accno')
