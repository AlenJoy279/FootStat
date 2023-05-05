from django.db import models
from django.contrib.auth.models import AbstractUser

class Summarised_Tweet(models.Model):
    id = models.IntegerField(primary_key=True)
    created_at = models.CharField(max_length=200,null=True)
    id_str = models.CharField(max_length=750, null=True)
    full_text = models.CharField(max_length=280,null=True)
    geo = models.CharField(max_length=500, null=True)


class Tweet(models.Model):
    created_at = models.CharField(max_length=200,null=True)
    id = models.IntegerField(primary_key=True)
    id_str = models.CharField(max_length=750, null=True)
    full_text = models.CharField(max_length=10000,null=True)
    display_text_range = models.CharField(max_length=500,null=True)
    entities = models.CharField(max_length=500,null=True)
    source = models.CharField(max_length=500,null=True)
    in_reply_to_status_id = models.CharField(max_length=500,null=True)
    in_reply_to_status_id_str = models.CharField(max_length=500,null=True)
    in_reply_to_user_id = models.CharField(max_length=500,null=True)
    in_reply_to_user_id_str = models.CharField(max_length=500,null=True)
    in_reply_to_screen_name = models.CharField(max_length=500,null=True)
    user = models.CharField(max_length=500,null=True)
    geo = models.CharField(max_length=500,null=True)
    coordinates = models.CharField(max_length=500,null=True)
    place = models.CharField(max_length=500,null=True)
    contributors = models.CharField(max_length=500,null=True)
    is_quote_status = models.CharField(max_length=500,null=True)
    retweet_count = models.CharField(max_length=500,null=True)
    favorite_count = models.CharField(max_length=500,null=True)
    favorited = models.CharField(max_length=500,null=True)
    retweeted = models.CharField(max_length=500,null=True)
    lang = models.CharField(max_length=500,null=True)



class TweetPolarity(models.Model):
    id = models.IntegerField(primary_key=True)
    created_at = models.CharField(max_length=200,null=True)
    id_str = models.CharField(max_length=750, null=True)
    full_text = models.CharField(max_length=280,null=True)
    geo = models.CharField(max_length=500, null=True)
    entities = models.CharField(max_length=500,null=True)
    source = models.CharField(max_length=500,null=True)
    retweet_count = models.CharField(max_length=500,null=True)
    favorite_count = models.CharField(max_length=500,null=True)
    favorited = models.CharField(max_length=500,null=True)
    retweeted = models.CharField(max_length=500,null=True)
    polarity = models.CharField(max_length=8, null=True)
    user = models.CharField(max_length=500, null=True)