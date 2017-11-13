from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^api/v1/recommendations', views.RecommendationsView.as_view(), name='recommendations'),
    url(r'^api/v1/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
