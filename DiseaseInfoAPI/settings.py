import os
from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = config('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'sampleAPI',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DiseaseInfoAPI.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'DiseaseInfoAPI.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# 웹 페이지에서 사용할 정적 파일의 최상우 URL 경로(실제 파일이 위치한 디렉토리는 아님)
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    # 정적 파일이 위치한 경로
    # 쉼표(,)를 빠뜨리게 되면 에러가 납니다. django_blog/assets/ 로 가서 정적 파일이 있는지 찾는다.
    # os.path.join(BASE_DIR, 'DJANGO_BLOG', 'assets', )
]

# STATIC_URL과 비슷, 업로드된 파일의 주소(URL)을 만들어 줌(실제 이미지 파일이 업로드 된 디렉토리를 의미하는 것은 아님)
MEDIA_URL = '/media/'

# STATICFILES_DIRS 동일한 기능, 정적 파일의 업로드가 끝나면 파일이 어디에 저장될 지를 설정하는 경로
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
