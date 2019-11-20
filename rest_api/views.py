from django.shortcuts import render

def index(request):
    return render(request, 'rest_api/index.html')