from rest_test.config.settings import *

# در اینجا ماژول ها افزوده می شوند.
INSTALLED_APPS += [
    'rest_framework',
    'oauth2_provider',
    'social_django',
    'rest_framework_social_oauth2',
]

# در اینجا اپ ها افزوده می شوند.
INSTALLED_APPS += [
    'authentication.apps.AuthenticationConfig',
]

TEMPLATES += [
    {
        'OPTIONS': {
            'context_processors': [
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    }
]
