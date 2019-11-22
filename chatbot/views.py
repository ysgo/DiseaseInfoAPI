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

# https://api.telegram.org/bot토큰값/deletewebhook
# @app.route('/')
def write(request):
    return render(request, 'write.html')

# @app.route('/send')
def send(request):
    return '전송완료'

# @app.route(f'/{token}', methods=['POST'])
def follow(request):
    #1. webhook을 통해 telegram에 보낸 요청 안에 있는 메시지를 가져와서 
    #2. 그대로 전송
        # if res.get('message'):
        #     text = res.get('message').get('text')
        #     if text == '로또':
        #         text = str(sorted(random.sample(range(1,46),6)))
        #     elif text[0:4] == '/번역 ':
        #         naver_client_id = config('NAVER_CLIENT_ID')
        #         naver_client_secret = config('NAVER_CLIENT_SECRET')

        #         url = 'https://openapi.naver.com/v1/papago/n2mt'
        #         text = text[4:]
        #         headers = {
        #             'X-Naver-Client-Id' : naver_client_id,
        #             'X-Naver-Client-Secret' : naver_client_secret
        #         }
        #         data = {
        #             'source' : 'ko',
        #             'target' : 'en',
        #             'text' : text
        #         }
        #         response = requests.post(url, data=data, headers=headers).json()
        #         text = response.get('message').get('result').get('translatedText')
            
            
        #     chat_id = res.get('message').get('chat').get('id')
        #     method = 'sendMessage'
        #     requests.get(url)
        # return render(request, 'result.html')
    # return JsonResponse({
    #     'message' : '안녕 장고야',
    #     'items' : ['챗봇', '제발', '완성'],
    # },  json_dumps_params = {'ensure_ascii': True})
    return '', 200