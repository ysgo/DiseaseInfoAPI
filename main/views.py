from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCustomCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model

def index(request):
    return render(request, 'main/index.html')

def register(request):
    return render(request, 'main/register.html')

def login(request):
    return render(request, 'main/login.html')
    
def forgot(request):
    return render(request, 'main/forgot-password.html')
