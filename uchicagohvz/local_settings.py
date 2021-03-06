"""
Django settings for uchicagohvz project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(__file__)

RECAPTCHA_USE_SSL = True

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
try:
	from secrets import SECRET_KEY
except:
	SECRET_KEY = 'SECRET KEY PLACEHOLDER'
try:
	from secrets import RECAPTCHA_PUBLIC_KEY
except:
	RECAPTCHA_PUBLIC_KEY = 'PUBLIC KEY PLACEHOLDER'
try:
	from secrets import RECAPTCHA_PRIVATE_KEY
except:
	RECAPTCHA_PRIVATE_KEY = 'PRIVATE KEY PLACEHOLDER'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'suit',
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'mptt', 'localflavor', 'djcelery_email', 'compressor', 'rest_framework', 'south', 'haystack', 'captcha', 'geoposition',
	'uchicagohvz.users', 'uchicagohvz.game',
)

MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'uchicagohvz.game.middleware.Feb262015Middleware',
)

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
TEMPLATE_CONTEXT_PROCESSORS += 'django.core.context_processors.request',

ROOT_URLCONF = 'uchicagohvz.urls'

WSGI_APPLICATION = 'uchicagohvz.wsgi.application'


# Django-Suit Admin Portal
SUIT_CONFIG = {
    #header
    'ADMIN_NAME': 'Hivemind',
    'HEADER_DATE_FORMAT': 'l, j. F Y',
    'HEADER_TIME_FORMAT': 'H:i',

    #forms
    'SHOW_REQUIRED_ASTERISK': True,
    'CONFIRM_UNSAVED_CHANGES': True,

    #menu
    'SEARCH_URL': '', #disable admin search
    'MENU_ICONS': {
        'sites': 'icon-leaf',
        'auth': 'icon-lock',
        'game': 'icon-star',
        'users': 'icon-user',
    },
    'MENU_OPEN_FIRST_CHILD': True,
    'MENU_EXPAND': ('auth.group'),
    'MENU': (
        'sites',
        {'app': 'auth', 'icon': 'icon-lock', 'models': ('user', 'group')},
        {'app': 'users', 'icon': 'icon-user', 'models': ('Profiles', )},
        {'app': 'game', 'icon': 'icon-envelope', 'models': ('Awards', 'Games', 'High value dorms', 'High value targets', 'Kills', 'New_ squads', 'Players', 'Squads')},
        {'label': 'Back to Site', 'icon': 'icon-leaf', 'url': '/'},
    ),

    #misc
    'LIST_PER_PAGE': 30
}

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	}
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'Africa/Johannesburg'

USE_I18N = False

USE_L10N = False

USE_TZ = True

# Templates
TEMPLATE_DIRS = (
	os.path.join(BASE_DIR, "templates"),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
	os.path.join(BASE_DIR, "static"),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

# Django Compressor
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder'
)

COMPRESS_PRECOMPILERS = (
    ('text/coffeescript', 'coffee -bcs'),
    ('text/less', 'lessc {infile} {outfile}'),
)
COMPRESS_ROOT = os.path.join(BASE_DIR, 'static_root')

# Datetime settings
DATETIME_FORMAT = 'N j, Y g:i A'
SHORT_DATETIME_FORMAT = 'd/m/Y g:i A'

# User-uploaded media
MEDIA_ROOT = os.path.join(BASE_DIR, "static_root", "media")
MEDIA_URL = "/static/media/"

# Authentication
AUTHENTICATION_BACKENDS = (
	'django.contrib.auth.backends.ModelBackend',
)
LOGIN_URL = "/users/login/?required=true"
LOGIN_REDIRECT_URL = "/"

# Caching and sessions
CACHES = {
	'default': {
		'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
		'LOCATION': 'memcached:11211',
	}
}
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
SESSION_COOKIE_HTTPONLY = False # required for reading sessionid cookie in chat JS

# HTTPS settings
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')

# Message framework settings
from django.contrib.messages import constants as message_constants
MESSAGE_TAGS = {
    message_constants.DEBUG: 'info',
    message_constants.INFO: 'info',
    message_constants.SUCCESS: 'success',
    message_constants.WARNING: 'warning',
    message_constants.ERROR: 'danger'
} # Bootstrap 3 alert integration

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    },
}

GEOPOSITION_MAP_OPTIONS = {
    'minZoom' : 5,
    'zoom' : 17,
    'maxZoom' : 18,
    'center' : { 'lat': -33.314236, 'lng': 26.518826},
}

GEOPOSITION_MARKER_OPTIONS = {
    'cursor': 'move',
    'position': { 'lat': -33.314236, 'lng': 26.5188267},
}

DEFAULT_INDEX_TABLESPACE = ''

# Celery configuration
BROKER_URL = 'redis://redis:6379/3'

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'RU HvZ <greg+hvz@gryphus.io>'
SERVER_EMAIL = 'greg+hvz@gryphus.io'
SYMPA_FROM_EMAIL = 'no-reply@hvz.gryphus.io'
SYMPA_TO_EMAIL = ''

# HvZ game configuration
HUMAN_KILL_POINTS = 1 # how many points killing a human is worth
HVT_KILL_POINTS = 3 # default points a high-value target is worth (replaces regular human kill points)
HVT_AWARD_POINTS = 0 # default award points a human gets for being an HVT and surviving
HVD_KILL_POINTS = 3 # default points a target from a high-value dorm is worth (can stack on top of HVT points)
LEADERBOARD_CACHE_DURATION = 3600 # how many seconds to cache certain DB-intensive leaderboard queries
NEXMO_NUMBER = '218-296-7238'
GAME_SW_BOUND = (-33.320192, 26.508758)
GAME_NE_BOUND = (-33.308830, 26.524041)

# Dealer settings
TEMPLATE_CONTEXT_PROCESSORS += 'dealer.contrib.django.staff.context_processor',
DEALER_PATH = os.path.dirname(BASE_DIR)

# Chat settings
CHAT_SERVER_URL = 'http://hvz.gryphus.io:36452/chat'
CHAT_ADMIN_URL = 'http://hvz.gryphus.io:36452/admin/'

ACTIVATION_MAIL_SUBJECT = 'Rhodes HvZ Account Activation Link'

ACTIVATION_MAIL_MSG = '''Hello Human,

Congratulations on taking the first step toward playing in
this year's game of Humans vs. Zombies.

You are receiving this email because you have registered an
account at the Rhodes University HvZ website.

To activate your account please click this link:

https://hvz.gryphus.io/users/activate/?key=%s

After you have activated your account, you must
complete your registration by doing the following:

1. Log in and register for the game you wish to participate in.
   This is separate from your account registration.

2. ATTEND A SECURITY BRIEFING! Attending at least one of these
   is mandatory as you will receive your ID card and sign a waiver
   there.

3. Wait for your game registration to be activated. This will only
   happen if we have your signed waiver on file.

If you opted-in for the High Value Target program then you are
elligible to be selected as an Original Zombie. In addition, you
must supply your cellphone number in your account profile on the
website. If you are (randomly) selected, we will use the
information on the site to call you to give you further instructions.
In order to avoid spoiling the game for other players, please do not
accept our phone call if you are around other players.

If you have received this email in error or have any problems with
your registration then please let us know by replying to this
email.

Regards
The Admin Team
'''
