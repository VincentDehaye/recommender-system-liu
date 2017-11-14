from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^api/v1/recommendations', views.RecommendationsView.as_view(), name='recommendations'),
    url(r'^api/v1/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/v1/trending', views.TrendingView.as_view(), name='trending'),
    url(r'^api/v1/youtubetrending', views.youtubetrending, name='youtubetrending'),
    url(r'^api/v1/twittertrending', views.twittertrending, name='twittertrending')
]
