from django.db import models
from markdown2 import Markdown

class Article(models.Model):
    slug = models.CharField(max_length=200)
    content = models.TextField()
    title = models.CharField(max_length=200)

    @property
    def content_html(self):
        markdowner = Markdown()
        content = markdowner.convert(self.content)
        content = content.replace("<p>", '<p class="fs-5 mb-4">')
        return content
