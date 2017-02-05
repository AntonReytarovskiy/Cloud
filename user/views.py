import os

from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from user.forms import LoginForm, RegisterForm


def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('default'))

    if request.method == 'POST':
        form = LoginForm(request.POST)
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if form.is_valid() and user:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('default'))
        else:
            return render(request, 'login.html', {'form': form})

    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('default'))

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = User()
            user.username = data['username']
            user.set_password(data['password'])
            user.save()
            form.createDir()
            auth.login(request, user)
            return HttpResponseRedirect(reverse('default'))
        else:
            return render(request, 'register.html', {'form': form})

    form = RegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required(login_url='/user/login')
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('default'))