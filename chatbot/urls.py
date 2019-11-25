from django.urls import path
from . import views
from decouple import config
base = "https://api.telegram.org"
token = config('TOKEN')

app_name = 'chatbot'

urlpatterns = [
    path('', views.write, name='write'),
    path('send/', views.send, name='send'),
]

