from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from .views import (TweetDetailView,
                    TweetListView,
                    TweetCreateView,
                    TweetUpdateView,
                    TweetDeleteView)

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', TweetListView.as_view(), name='list'),
    url(r'^create/$', TweetCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/edit/$', TweetUpdateView.as_view(), name='edit'),
    url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete')
]

