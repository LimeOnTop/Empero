from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='user',
                               widget=forms.TextInput(attrs={'class': 'uk-input', 'placeholder': 'Введите свой логин'}))
    email = forms.EmailField(label='mail',
                             widget=forms.EmailInput(attrs={'class': 'uk-input', 'placeholder': 'Введите свою почту'}))
    password1 = forms.CharField(label='lock', widget=forms.PasswordInput(
        attrs={'class': 'uk-input', 'placeholder': 'Введите свой пароль'}))
    password2 = forms.CharField(label='lock', widget=forms.PasswordInput(
        attrs={'class': 'uk-input', 'placeholder': 'Повторите свой пароль'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='user', widget=forms.TextInput(
        attrs={'class': 'uk-input', 'placeholder': 'Введите свой логин или почту'}))
    password = forms.CharField(label='lock', widget=forms.PasswordInput(
        attrs={'class': 'uk-input', 'placeholder': 'Введите свой пароль'}))
