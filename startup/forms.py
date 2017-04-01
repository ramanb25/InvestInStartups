#raman
from .models import StartupProfile
from django.contrib.auth.models import User
from django import forms

class StartupUserForm(forms.ModelForm):
    #username is already defined passsword is viewable
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class StartupProfileForm(forms.ModelForm):
    class Meta:
        model = StartupProfile
        fields = ('aadhar', 'accno','startupName','shareCount','sharePrice','stockName')
