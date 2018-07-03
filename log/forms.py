from django.contrib.auth.forms import AuthenticationForm 
from django import forms
from captcha.fields import CaptchaField
from datetime import datetime
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))
    captcha = CaptchaField(label="Captcha")
class userform(forms.Form):
	data=forms.DateField(widget = forms.TextInput(attrs = {'type' : 'date','class' : 'datepicker'}))

class customise(forms.Form):
	start=forms.DateField(label="Start Date",widget = forms.TextInput(attrs = {'type' : 'date','class' : 'piyush'}))
	end=forms.DateField(label="End Date",widget = forms.TextInput(attrs = {'type' : 'date','class' : 'piyush'}))

