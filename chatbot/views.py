from django.shortcuts import render, redirect, get_object_or_404
from telegram.ext import Updater, MessageHandler, Filters
from django.http import StreamingHttpResponse
from decouple import config
import requests
from pprint import pprint as pp
from django.views.decorators.http import require_POST
import random
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
import json

base = "https://api.telegram.org"
token = config('TOKEN')
chat_id = config('CHATID')
ngrok = config('NGROK')

# https://api.telegram.org/bot토큰값/deletewebhook
# @app.route('/')
def write(request):
    return render(request, 'chatbot/write.html')    

# @app.route('/send')
def send(request):
    method = 'getUpdates'

    url = f'{base}/bot{token}/{method}'
    res = requests.get(url).json() #http url의 값을 가지고 올 때 사용
    pp(res)
    #2. 받아온 응답(json)을 dictionary로 바꿔서 첫번째 메시지의 chat_id를 가져온다.

    #3. write.html에서 보내온 msg를 받아 telegram api를 통해 메시지 전송
    method = 'sendMessage'
    text = request.GET.get('msg')
    url = f'{base}/bot{token}/{method}?chat_id={chat_id}&text={text}'
    print(url)
    requests.get(url)
    return redirect('chatbot:write')

# @ensure_csrf_cookie
def webhook(request, telegram_token):
    #1. webhook을 통해 telegram에 보낸 요청 안에 있는 메시지를 가져와서 
    url = f'{base}/bot{telegram_token}/setWebhook?url={ngrok}/{telegram_token}'
    
    #2. 그대로 전송
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
    return render(request, 'chatbot/write.html')
