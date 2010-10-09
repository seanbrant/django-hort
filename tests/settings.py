import sys
from os.path import dirname, abspath, join


TEST_DIR = dirname(abspath(__file__))

DEBUG = True

ROOT_URLCONF = 'urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}

MEDIA_ROOT = join(TEST_DIR, 'media')
ASSET_ROOT = join(TEST_DIR, '_assets')

INSTALLED_APPS = (
    'core',
    'hort',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
