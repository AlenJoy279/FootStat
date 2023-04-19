from django.test import TestCase
from PandemicAnalyser.db.selector import *
from PandemicAnalyser.models import Tweet, TweetPolarity
from unittest.mock import patch

class SelectorTestCase(TestCase):
    def setUp(self):
        # Set up some test data
        self.tweet1 = Tweet.objects.create(created_at='Sat Apr 15 08:08:08 +0000 2021', id=1, id_str='1', full_text='Test tweet 1', source='Test')
        self.tweet2 = Tweet.objects.create(created_at='Fri Apr 23 18:54:14 +0000 2021', id=2, id_str='2', full_text='Test tweet 2', source='Test2')

        self.tweetp1 = TweetPolarity.objects.create(id=1, id_str='1', full_text="This is a positive tweet", created_at="Sat Apr 15 08:08:08 +0000 2021")
        self.tweetp2 = TweetPolarity.objects.create(id=2, id_str='2', full_text="This is a neutral tweet", created_at="Fri Apr 23 19:56:11 +0000 2021")
        self.tweetp3 = TweetPolarity.objects.create(id=3, id_str='3', full_text="This is a negative tweet", created_at="Sat Mar 25 03:44:66 +0000 2022")

    # select_by_date unit tests
    def test_select_by_date(self):
        # Test selecting tweets by month and year
        selected_tweets = select_by_date('Apr', '2021')
        self.assertEqual(len(selected_tweets), 2)
        self.assertIn(self.tweet1, selected_tweets)
        self.assertIn(self.tweet2, selected_tweets)


    # get_count_by_date unit tests
    def test_get_count_by_date(self):
        monthly_count = get_count_by_date()
        for key,value in monthly_count.items():
            if (key != "Apr 2021"):
                self.assertEqual(monthly_count[key], 0)

        self.assertEqual(monthly_count["Apr 2021"], 2) # the two tweets from april 2021 from setUp

    # get_polarity_by_month unit tests
    def test_get_polarity_by_month(self):
        result = get_polarity_by_month()

        # check that the correct number of months are in the result
        self.assertEqual(len(result), 34)

        # check that the polarity for March and April 2022 are correct
        self.assertAlmostEqual(result["Apr 2021"], 0.0)
        self.assertAlmostEqual(result["Mar 2022"], 0.0)

        # check polarity for everything else is 0.0
        for month in result:
            if month not in ["Mar 2022", "Apr 2021"]:
                self.assertEqual(result[month], 0.0)


    def test_get_daily_polarity_long_month(self):
            month = "Jan"
            year = "2023"
            daily_polarity = get_daily_polarity(month, year)
            self.assertEqual(len(daily_polarity), 31)
            self.assertEqual(daily_polarity["01"], 0)
            self.assertEqual(daily_polarity["31"], 0)

    def test_get_daily_polarity_mid_month(self):
            month = "Apr"
            year = "2021"
            daily_polarity = get_daily_polarity(month, year)
            self.assertEqual(len(daily_polarity), 30)
            self.assertEqual(daily_polarity["01"], 0)
            self.assertAlmostEqual(daily_polarity["30"], 0)

    def test_get_daily_polarity_short_month(self):
            month = "Feb"
            year = "2021"
            daily_polarity = get_daily_polarity(month, year)
            self.assertEqual(len(daily_polarity), 28)
            self.assertEqual(daily_polarity["01"], 0)
            self.assertEqual(daily_polarity["28"], 0)

    def test_get_daily_polarity_leap_year(self):
            month = "Feb"
            year = "2020"
            daily_polarity = get_daily_polarity(month, year)
            self.assertEqual(len(daily_polarity), 29)
            self.assertEqual(daily_polarity["01"],  0)
            self.assertEqual(daily_polarity["29"], 0)


    # get_all_daily_polarity unit tests
    @patch('PandemicAnalyser.db.selector.get_daily_polarity')
    def test_get_all_daily_polarity(self, mock_get_daily_polarity):
        get_all_daily_polarity()
        self.assertEqual(mock_get_daily_polarity.call_count, 34) # mocked function called 34 times - one for every month in DB
