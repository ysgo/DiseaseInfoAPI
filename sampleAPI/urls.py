from django.urls import path
from . import views

app_name = 'sampleAPI'

urlpatterns = [
    path('', views.index, name='index'),
]
