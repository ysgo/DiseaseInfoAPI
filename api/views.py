from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post
from rest_framework import permissions

# 프레임워크에서 API 조작을 돕기 위해 제공하는 페이지 사용
class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)