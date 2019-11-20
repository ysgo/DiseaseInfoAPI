from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # 두 번째 API 테스트
    path('chatbot', include('chatbot.urls')),
    path('api/', include('api.urls')),
    path('rest_api/', include('rest_api.urls')),
]
