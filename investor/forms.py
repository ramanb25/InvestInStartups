from .models import InvestorProfile
from django.contrib.auth.models import User
from django import forms
from app.models import accounts

class InvestorUserForm(forms.ModelForm):
    #username is already defined passsword is viewable
    password = forms.CharField(widget=forms.PasswordInput())
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-inline'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-inline'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class InvestorProfileForm(forms.ModelForm):
    class Meta:
        model = InvestorProfile
        fields = ['aadhar']

class InvestorAccountForm(forms.ModelForm):
    bankName = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-inline'}))
    ifsc = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-inline'}))
    #accno = forms.CharField(widget=forms.Select(attrs={'class' : 'form-control'}))
    class Meta:
        model = accounts
        fields = ['bankName','accno','ifsc','balance']