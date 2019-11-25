from django.shortcuts import render, redirect, get_object_or_404
from telegram.ext import Updater, MessageHandler, Filters
from django.http import StreamingHttpResponse
from decouple import config
import requests
from pprint import pprint as pp
import random
from django.http import HttpResponse, JsonResponse

base = "https://api.telegram.org"
token = config('TOKEN')
chatid = config('CHATID')
#chatid = '899056890'

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
    url = f'{base}/bot{token}/{method}?chat_id={chatid}&text={text}'
    print(url)
    requests.get(url)
    return redirect('chatbot:write')
