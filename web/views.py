from django.views.generic import TemplateView, DetailView
from . import models
from django.template import Context, Template


class IndexView(TemplateView):
    template_name = "index.html"


class ArticleView(DetailView):
    template_name = "article.html"
    model = models.Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        t = Template(self.object.content)
        c = Context({})
        context["article_content"] = t.render(c)
        return context

    def get_object(self):
        obj = models.Article.objects.filter(slug=self.kwargs["slug"]).first()
        return obj

