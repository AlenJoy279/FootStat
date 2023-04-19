import os
from unittest.mock import patch

from django.test import TestCase, RequestFactory
from PandemicAnalyser.db.addition import add_to_db
from PandemicAnalyser.models import Tweet, TweetPolarity
import unittest

from PandemicAnalyser.views import models


class TweetTestCase(TestCase):
    def setUp(self): # Sat Dec 31 23:47:30 +0000 2022
        Tweet.objects.create(id=1, created_at="Sat Dec 31 23:47:30 +0000 2022", id_str="1", full_text="Test")
        Tweet.objects.create(id=2, created_at="Sun Jan 01 23:47:30 +0000 2023", id_str="2", full_text="Test2")

    def test_get_Tweet_id(self):
        tweet1 = Tweet.objects.get(id="1")
        tweet2 = Tweet.objects.get(id="2")
        self.assertEqual(tweet1.full_text, 'Test')
        self.assertEqual(tweet2.full_text, 'Test2')


class TweetPolarityTestCase(TestCase):
    def setUp(self): # Sat Dec 31 23:47:30 +0000 2022
        TweetPolarity.objects.create(id=1, created_at="Sat Dec 31 23:47:30 +0000 2022", id_str="1", full_text="Test", polarity=0.65)
        TweetPolarity.objects.create(id=2, created_at="Sun Jan 01 23:47:30 +0000 2023", id_str="2", full_text="Test2", polarity=-0.5)

    def test_get_TweetPolarity_id(self):
        tweet1 = TweetPolarity.objects.get(id="1")
        tweet2 = TweetPolarity.objects.get(id="2")
        self.assertEqual(tweet1.polarity, "0.65")
        self.assertEqual(tweet2.polarity, "-0.5")
