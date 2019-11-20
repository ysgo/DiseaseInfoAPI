from django.shortcuts import render, redirect, get_object_or_404
import requests

base = "https://api.telegram.org"
token = config('TOKEN')

def index(request):
    print('index')

def send(request):
    method = 'getUpdates'
    url = f'{base}/bot{token}/{method}'
    res = requests.get(url).json() # http url의 값을 가지고 올 때 사용
    print(res)

    #2. 받아온 응답(json)을 dictionary로 바꿔서 첫번째 메시지의 chat_id를 가져온다.
    chat_id = res['result'][0]['message']['chat']['id']
