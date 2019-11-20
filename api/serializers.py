from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# model 인스턴스를 JSON형태 혹은 Dictionary형태로 직렬화함
class PostSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True)
    user = serializers.CharField(
        max_length=100,
        style={
            'placeholder':'User',
            'autofocus':True
        }
    )
    test = serializers.CharField(
        style={
            # 'base_template':'textarea.html'
            # 'template':'api/custom-input.html'
            'base_template':'textarea.html', 'row':10
        }
    )
    
    # return 되는 데이터 셋 설정
    class Meta:
        model = Post
        fields = (
            'id',
            'user',
            'title',
            'subtitle',
            'content',
            'created_at',
            'test',
        )
        read_only_fields = ('created_at',)