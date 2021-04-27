from django import forms
from newapp.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_no = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    class Meta:
        model = User
        fields = ['username', 'email','phone_no','password1', 'password2','first_name','last_name']

class UserSSIDForm(UserCreationForm):
    ssid = forms.CharField(max_length=15)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = ssidPassword
        fields = ['ssid','password']