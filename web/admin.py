from django.contrib import admin
from . import models

admin.site.register(models.Article)
admin.site.register(models.Section)
admin.site.register(models.Image)
admin.site.register(models.DataAttachment)
