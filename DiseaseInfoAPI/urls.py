from django.contrib import admin
from django.urls import path, include
# JWT 인증을 위해 필요한 요소들을 로드
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    # 우리가 만든 앱의 URL을 연결
    path('api/blog/', include('sampleAPI.urls')),
    # JWT 토큰 발행할 때 사용
    path('api/token/', obtain_jwt_token),
    # JWT 토큰이 유효한지 검증할 때 사용
    path('api/token/verify/', verify_jwt_token),
    # JWT 토큰을 갱신할 때 사용
    path('api/token/refresh/', refresh_jwt_token),

    # 두 번째 API 테스트
    path('api/', include('api.urls')),
]
