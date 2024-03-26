from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'app',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1.host.docker.internal',
        'PORT': '53306',
        'ATOMIC_REQUESTS': True,
    }
}
