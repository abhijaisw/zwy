from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.
def index(request):
	return render(request, 'main/index.html', {})


def about(request):
	return render(request, 'main/about.html', {})

def about_me(request):
	return render(request, 'main/about-me.html',{})


def login(request):
	return render(request, 'accounts/login.html', {})

def register(request):
	return render(request, 'accounts/register.html', {})

def log_out(request):
    logout(request)
    return redirect("/")