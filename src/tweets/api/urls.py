from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.generic.base import RedirectView
from .views import TweetListAPIView

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', TweetListAPIView.as_view(), name='list'),
]

