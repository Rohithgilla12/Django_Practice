from django.contrib import admin

# Register your models here.

from .models import Tweet
from .forms import TweetModelForm

# admin.site.register(Tweet)


class TweetModelForm(admin.ModelAdmin):
    # form = TweetModelForm
    class Meta:
        model = Tweet
        form = TweetModelForm


admin.site.register(Tweet, TweetModelForm)