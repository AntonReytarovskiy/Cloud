import os
from django.conf import settings
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(min_length=4, max_length=30)
    password = forms.CharField(max_length=30, min_length=5, widget=forms.PasswordInput())

class RegisterForm(forms.Form):
    username = forms.CharField(min_length=4, max_length=30)
    password = forms.CharField(max_length=30, min_length=5, widget=forms.PasswordInput())
    confirm_password = forms.CharField(min_length=5, max_length=30, widget=forms.PasswordInput())

    def clean(self):
        if self.cleaned_data.get('password') != self.cleaned_data.get('confirm_password'):
            raise ValidationError(message='Password not confirm', code='invalid')
        if User.objects.get(username=self.cleaned_data.get('username')):
            raise ValidationError(message='User exists', code='invalid')

    def createDir(self):
        path = 'app/media/' + self.cleaned_data.get('username')
        if not os.path.exists(path):
            os.mkdir(path)
