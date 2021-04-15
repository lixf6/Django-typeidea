from .base import *  # NOQA

# SECURITY WARNING: don't run with debug turned on in production!
# 测试数据库设置
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
