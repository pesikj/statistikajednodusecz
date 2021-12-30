from django.db.models import Q
from django.views.generic import TemplateView, DetailView, ListView
from . import models
from django.template import Context, Template


class IndexView(TemplateView):
    template_name = "index.html"


class ArticleView(DetailView):
    template_name = "article.html"
    model = models.Article


class SectionView(DetailView):
    template_name = "section.html"
    model = models.Section

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["other_sections"] = models.Section.objects.filter(~Q(id=self.object.id)).order_by("title")
        return context


class AllArticlesView(ListView):
    template_name = "all_articles.html"
    model = models.Section

