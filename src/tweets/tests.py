from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Tweet
# Create your tests here.

User = get_user_model()

class TweetModelTestCase(TestCase):
    def setUp(self):
        randomGuy=User.objects.create(
            username="Haha",
        )
    def test_tweet_item(self):
        obj =Tweet.object.create(
            user=User.objects.first(),
            content="Some random string!"
        )
        self.assertTrue(obj.content == "Some random string!")