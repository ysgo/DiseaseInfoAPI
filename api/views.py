from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post
from rest_framework import permissions
from django.http import JsonResponse

# 프레임워크에서 API 조작을 돕기 위해 제공하는 페이지 사용
class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        # serializer.data를 출력할 경우 직렬화한 JSON/Dictionary 타입의 데이터를 모두 보여줌
        print(serializer.data)

