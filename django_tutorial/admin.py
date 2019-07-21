from django.contrib import admin
from django_tutorial import models
admin.site.register(models.Question)
admin.site.register(models.Choice)