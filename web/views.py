from django.views.generic import TemplateView, DetailView
from . import models
from django.template import Context, Template


class IndexView(TemplateView):
    template_name = "index.html"


class ArticleView(DetailView):
    template_name = "article.html"
    model = models.Article

    def get_object(self):
        obj = models.Article.objects.first()
        return obj

