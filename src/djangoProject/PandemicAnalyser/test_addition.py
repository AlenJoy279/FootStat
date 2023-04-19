from django.test import TestCase
from PandemicAnalyser.db.addition import add_to_db, add_tweet_polarity, get_files
from PandemicAnalyser.models import Tweet, TweetPolarity
from unittest.mock import patch

class AdditionTestCase(TestCase):
    def setUp(self):
        # Set up some test data
        self.test_path = "./PandemicAnalyser/tests/jsontest\\test_tweet.jsonl" # test file made
        self.test_dir = "./PandemicAnalyser/tests/jsontest"

    # functions to be mocked
    @patch('PandemicAnalyser.db.addition.add_to_db')
    @patch('PandemicAnalyser.db.addition.add_tweet_polarity')
    def test_get_files(self, mock_add_tweet_polarity, mock_add_to_db):
        # Test that files are added to db and polarity was calculated
        get_files(self.test_dir)
        mock_add_to_db.assert_called_once_with(self.test_path) # mock function - called once with correct parameter
        mock_add_tweet_polarity.assert_called_once_with(self.test_path) # mock function - called once with correct parameter


    def test_add_to_db(self):
        # Test that a tweet is added to the db
        add_to_db(self.test_path)
        tweet_count = Tweet.objects.filter(id=123).count()
        self.assertEqual(tweet_count, 1)

        # Test that the same tweet doesn't get added it twice
        add_to_db(self.test_path)
        tweet_count = Tweet.objects.filter(id=123).count()
        self.assertEqual(tweet_count, 1)


    def test_add_tweet_polarity(self):
            add_tweet_polarity(self.test_path)
            tweet_count = TweetPolarity.objects.filter(id=123).count()
            self.assertEqual(tweet_count, 1)

            # Test that a tweet is added to the db
            add_tweet_polarity(self.test_path)
            tweet_count = TweetPolarity.objects.filter(id=123).count()
            self.assertEqual(tweet_count, 1)

            # Test the polarity is correct
            added_tweets = TweetPolarity.objects.filter(id=123)
            for tweet in added_tweets:
                self.assertEqual(tweet.polarity, '0.0')  # expected polarity for test tweet

