from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from . import views

urlpatterns = [
    path('', views.CalcView.as_view(), name='calc'),
    path('test-list', views.TestList.as_view(), name='test_list'),
]
