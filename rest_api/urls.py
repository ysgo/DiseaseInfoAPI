from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

app_name = 'rest_api'

urlpatterns = [
    path('token/', obtain_jwt_token, name='generate'),
    # path('token/verify/', views.verify, name='verify'),
    path('token/verify/', verify_jwt_token, name='verify'),
    path('token/refresh/', refresh_jwt_token, name='refresh'),
    path('data/', views.data, name='data'),
]