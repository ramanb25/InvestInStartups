#raman
from .models import StartupProfile
from django.contrib.auth.models import User
from django import forms
from app.models import accounts

class StartupUserForm(forms.ModelForm):
    #username is already defined passsword is viewable
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-inline'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-inline'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-inline'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        

class StartupProfileForm(forms.ModelForm):
    startupName = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-inline'}))
    stockName = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-inline'}))
    #accno = forms.CharField(widget=forms.Select(attrs={'class' : 'form-inline'}))
    class Meta:
        model = StartupProfile
        fields = ('aadhar','startupName','shareCount','sharePrice','stockName')

class StartupAccountForm(forms.ModelForm):
    bankName = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-inline'}))
    ifsc = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-inline'}))
    #accno = forms.CharField(widget=forms.Select(attrs={'class' : 'form-inline'}))
    class Meta:
        model = accounts
        fields = ['bankName','accno','ifsc','balance']
