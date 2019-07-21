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
    'django_tutorial.apps.DjangoTutorialConfig',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'oauth2_provider.ext.rest_framework.OAuth2Authentication',  # django-oauth-toolkit < 1.0.0
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',  # django-oauth-toolkit >= 1.0.0
        'rest_framework_social_oauth2.authentication.SocialAuthentication',
    ),
}
AUTHENTICATION_BACKENDS = (
    'rest_framework_social_oauth2.backends.DjangoOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)
