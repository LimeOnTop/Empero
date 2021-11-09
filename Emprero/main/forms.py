from django import forms
from .models import *

class UserData(forms.Form):
    Login = forms.CharField(max_length=255)
    password = forms.PasswordInput()