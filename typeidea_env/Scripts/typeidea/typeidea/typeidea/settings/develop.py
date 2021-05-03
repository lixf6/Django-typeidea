from .base import *  # NOQA

# SECURITY WARNING: don't run with debug turned on in production!
# 测试数据库设置
DEBUG = True
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'typeidea_db',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        # 'CONN_MAX_AGE': 5 * 60,
        # 'OPTIONS': {'charset': 'utf8mb4'}
    }
}

INSTALLED_APPS += [
    # 'debug_toolbar',
    'silk',
]

MIDDLEWARE += [
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    'silk.middleware.SilkyMiddleware',
]

INTERNAL_IPS = ['127.0.0.1']
