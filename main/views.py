from django.shortcuts import render, redirect, get_object_or_404

def index(request):
    return render(request, 'main/index.html')
    
def register(request):
    return render(request, 'main/register.html')

def login(request):
    return render(request, 'main/login.html')
    
def forgot(request):
    return render(request, 'main/forgot-password.html')

def tables(request):
    return render(request, 'main/tables.html')
