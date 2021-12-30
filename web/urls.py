from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('article/<slug:slug>', views.ArticleView.as_view(), name='article'),
    path('section/<slug:slug>', views.SectionView.as_view(), name='section'),
    path('all-articles/', views.AllArticlesView.as_view(), name='all_articles'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
