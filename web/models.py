from django.db import models


class Article(models.Model):
    slug = models.CharField(max_length=200)
    content = models.TextField()
    title = models.CharField(max_length=200)
