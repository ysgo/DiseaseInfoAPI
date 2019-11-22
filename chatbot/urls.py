from django.urls import path
from . import views
from decouple import config
base = "https://api.telegram.org"
token = config('TOKEN')

app_name = 'chatbot'

urlpatterns = [
    path(f'{base}/bot{token}/getUpdates', views.send, name='send'),
    path(f'{base}/bot{token}/setWebhook?url=https://7df8ca78.ngrok.io/{token}', views.follow, name='follow'),
]

