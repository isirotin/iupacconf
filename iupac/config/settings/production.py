from .base import *


DEBUG = False
# DB_PASS = get_env_variable("DB_PASS")

# ALLOWED_HOSTS = ['name.muctr.ru']

# DATABASES = {
#     "default": {
#     "ENGINE": "django.db.backends.mysql",
#     "NAME": "name",
#     "USER": "user",
#     "PASSWORD": DB_PASS,
#     "HOST": "host-domain",
#     "PORT": "",
#     }
# }


STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "staticfiles", "static")

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "staticfiles", "media")