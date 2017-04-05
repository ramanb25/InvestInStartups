#raman
from .models import StartupProfile
from django.contrib.auth.models import User
from django import forms

class StartupUserForm(forms.ModelForm):
    #username is already defined passsword is viewable
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        

class StartupProfileForm(forms.ModelForm):
    startupName = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    stockName = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    #accno = forms.CharField(widget=forms.Select(attrs={'class' : 'form-control'}))
    class Meta:
        model = StartupProfile
        fields = ('aadhar','bank' ,'accno','ifsc','startupName','shareCount','sharePrice','stockName')
