from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login as auth_login
from .forms import SignUpForm
from django.contrib.auth import get_user_model
User = get_user_model()

def index(request):
    count = User.objects.count()
    return HttpResponse("Hello, world. You're at the users index. There are currently {} users".format(count))

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})
