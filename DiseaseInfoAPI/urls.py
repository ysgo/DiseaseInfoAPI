from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # 두 번째 API 테스트
    path('api/', include('api.urls')),
    path('main/', include('main.urls')),
]
