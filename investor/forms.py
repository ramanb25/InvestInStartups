#raman
from .models import InvestorProfile
from django.contrib.auth.models import User
from django import forms

class InvestorUserForm(forms.ModelForm):
    #username is already defined passsword is viewable
    password = forms.CharField(widget=forms.PasswordInput())
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class InvestorProfileForm(forms.ModelForm):
    class Meta:
        model = InvestorProfile
        fields = '__all__'#('aadhar', 'accno')
