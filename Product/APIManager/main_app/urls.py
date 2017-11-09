from django.conf.urls import url
from django.contrib.staticfiles.views import serve
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    url(r'^v1/recommendations', views.recommendations, name='recommendations'),
    url(r'^api/v1/recommendations', views.recommendations, name='recommendations'),
    url(r'^v1/trending', views.trending, name='trending'),
    url(r'^api/v1/trending', views.trending, name='trending'),
    url(r'^v1/trending2', views.trending2, name='trending2'),
    url(r'^api/v1/trending2', views.trending2, name='trending2')
]
