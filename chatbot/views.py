from django.shortcuts import render, redirect, get_object_or_404
from telegram.ext import Updater, MessageHandler, Filters
from django.http import StreamingHttpResponse, HttpResponse
from decouple import config
import requests
from pprint import pprint as pp
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import random
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
import json

base = "https://api.telegram.org"
token = config('TOKEN')
chat_id = config('CHATID')
ngrok = config('NGROK')

@csrf_exempt
def webhook(request, telegram_token):
    url = f'{base}/bot{telegram_token}/setWebhook?url=https://diseaseinfoapi.herokuapp.com/{telegram_token}'
    requests.get(url).json()
    body = request.body
    body = body.decode('utf-8')
    res = json.loads(body)
    print(res)
    if res.get('message'):
        text = res.get('message').get('text')
        if text == '로또':
            text = str(sorted(random.sample(range(1,46),6)))
        
        chat_id = res.get('message').get('chat').get('id')
        method = 'sendMessage'
        url = f'{base}/bot{token}/{method}?chat_id={chat_id}&text={text}'
        requests.get(url)
    return HttpResponse(f'/{telegram_token}')
