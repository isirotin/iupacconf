from .base import *


DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

INSTALLED_APPS += (
    'content',
    'feed',
    'event',
    'news',
    'navigation',
    'taggit',
    'ckeditor',
    'ckeditor_uploader',
    'watson',
)
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_BROWSE_SHOW_DIRS = 'True'
