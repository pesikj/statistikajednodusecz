from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path("ads.txt", RedirectView.as_view(url=staticfiles_storage.url("ads.txt")),),
    path('article/<slug:slug>', views.ArticleView.as_view(), name='article'),
    path('section/<slug:slug>', views.SectionView.as_view(), name='section'),
    path('all-articles/', views.AllArticlesView.as_view(), name='all_articles'),
    # Temporary link because of links from old version
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + [re_path(r'^(.*)$', views.IndexView.as_view(), name='default'), ]

