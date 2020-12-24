import django_heroku
import os
import tensorflow.keras as tk




BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = 'h7d-t4vmdsjg6ntkf5n21gt6i*=81b665h#)xmz6zpg&i*doam'


DEBUG = True

ALLOWED_HOSTS = []




INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'oct',
    'rest_framework',
    'project_description',
    'xray',
    'subscribe'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'radiology_and_oct_backend.urls'

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

WSGI_APPLICATION = 'radiology_and_oct_backend.wsgi.application'


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



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
]


STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'

OCT_MODEL_URL = os.path.join(BASE_DIR,'data/Final-4-conv,32-nodes,1-dense,1582188407')
# print("---------------------------------------------------",OCT_MODEL_URL)
OCT_MODEL = tk.models.load_model(OCT_MODEL_URL)


OCT_CATEGORIES = [
    "Choroidal neovascularization(CNV)", 
    "Diabetic macular edema (DME)", 
    "Drusen", 
    "Normal"
]
OCT_IMG_SIZE = 80

XRAY_MODEL_URL = os.path.join(BASE_DIR,'data/my_model')
print("---------------------------------",XRAY_MODEL_URL)
XRAY_MODEL = tk.models.load_model(XRAY_MODEL_URL)

XRAY_CATEGORIES = [
    "Pleumonia",
    "Normal"
]
XRAY_IMG_SIZE = 500

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'manishdubey7777777@gmail.com'
EMAIL_HOST_PASSWORD = 'asshole7777'
EMAIL_RECEIVER = 'antim.timsina7777@gmail.com'

django_heroku.settings(locals())