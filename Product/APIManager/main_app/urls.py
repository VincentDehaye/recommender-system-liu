from django.conf.urls import url
from django.contrib.staticfiles.views import serve
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    url(r'^api/v1/recommendations', views.recommendations, name='recommendations'),
    url(r'^v1/recommendations', views.recommendations, name='recommendations')
]
