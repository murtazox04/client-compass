from decouple import config

from .base import INSTALLED_APPS, MIDDLEWARE

DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = []

INSTALLED_APPS.append("corsheaders")
MIDDLEWARE.append("corsheaders.middleware.CorsMiddleware")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST"),
        "PORT": config("DB_PORT"),
    }
}


CORS_ALLOW_METHODS = ["*"]
CORS_ALLOW_HEADERS = ["*"]
CORS_ORIGIN_WHITELIST = ["https://*", "http://*"]
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
