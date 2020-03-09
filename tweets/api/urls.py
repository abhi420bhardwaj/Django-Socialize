from django.conf.urls import url

from django.views.generic.base import RedirectView

from .views import (
    LikeToggleAPIView,
    TweetCreateAPIView,
    TweetListAPIView,
    TweetDetailAPIView,
 )

urlpatterns = [
    url(r'^$', TweetListAPIView.as_view(), name='list'), # /api/tweet/
    url(r'^create/$', TweetCreateAPIView.as_view(), name='create'), # /tweet/create/
    url(r'^(?P<pk>\d+)/$', TweetDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/like/$', LikeToggleAPIView.as_view(), name='like-toggle'),
    ]


