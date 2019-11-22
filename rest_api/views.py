from django.shortcuts import render
from .models import Disease
from django.core import serializers
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
def data(request):
    data = Disease.objects.all()
    data_list = serializers.serialize('json', data)
    return HttpResponse(data_list, content_type='text/json-comment-filtered')


def verify(request):
    data = request.POST.get('token')
    print(f'Test : {data}')
    token = serializers.serialize('json', data)
    return HttpResponse(token, content_type='text/json-comment-filtered')
