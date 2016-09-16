import os

HERE = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(HERE)

SECRET_KEY = 'fake-key'

INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "tests",
]

# is this necessary
MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3'
    }
}

TESTING = True

MEDIA_ROOT = os.path.join(HERE, "uploaded_files")

MEDIA_URL = ""

