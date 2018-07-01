from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login as auth_login
from .forms import SignUpForm, LoginForm

def index(request):
    return render(request, 'users/index.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return render(request, 'users/login.html', {user: user})
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return render(request, 'users/index.html', {user: user})
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})
