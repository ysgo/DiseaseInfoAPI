from django.shortcuts import render, redirect, get_object_or_404
from rest_api.models import Disease

def index(request):
    return render(request, 'main/index.html')
    
def register(request):
    return render(request, 'main/register.html')

def login(request):
    return render(request, 'main/login.html')
    
def forgot(request):
    return render(request, 'main/forgot-password.html')

def tables(request):
    diseases = Disease.objects.all()
    print(diseases)
    return render(request, 'main/tables.html', {'diseases':diseases})
