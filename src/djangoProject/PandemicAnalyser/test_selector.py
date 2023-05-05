from django.test import TestCase
from PandemicAnalyser.db.selector import *
from PandemicAnalyser.models import Tweet, TweetPolarity
from unittest.mock import patch

class SelectorTestCase(TestCase):
    def setUp(self):
        # Set up some test data
        self.tweet1 = Tweet.objects.create(created_at='Sat Apr 15 08:08:08 +0000 2021', id=1, id_str='1', full_text='Test tweet 1', source='Test')
        self.tweet2 = Tweet.objects.create(created_at='Fri Apr 23 18:54:14 +0000 2021', id=2, id_str='2', full_text='Test tweet 2', source='Test2')

        self.tweetp1 = TweetPolarity.objects.create(id=1, id_str='1', full_text="This is a positive tweet", created_at="Sat Apr 15 08:08:08 +0000 2021", polarity = 0.2272)
        self.tweetp2 = TweetPolarity.objects.create(id=2, id_str='2', full_text="This is a neutral tweet", created_at="Fri Apr 23 19:56:11 +0000 2021", polarity = 0.0)
        self.tweetp3 = TweetPolarity.objects.create(id=3, id_str='3', full_text="This is a negative tweet", created_at="Sat Mar 25 03:44:66 +0000 2022", polarity = -0.3)

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

    @patch("PandemicAnalyser.db.selector.get_daily_polarity")
    def test_get_all_polarity_returns_dict(self, mock_get_daily_polarity):
        mock_get_daily_polarity.return_value = 0.5  # Mock the return value of get_daily_polarity()
        result = get_all_polarity()
        self.assertIsInstance(result, dict)

    @patch("PandemicAnalyser.db.selector.get_daily_polarity")
    def test_get_all_polarity_returns_correct_monthly_average(self, mock_get_daily_polarity):
        mock_get_daily_polarity.return_value = 0.125 # Mock the return value of get_daily_polarity()
        result = get_all_polarity()
        self.assertEqual(len(result), 34)  # Ensure the result has entries for all 33 months

        mock_mar_2020 = 0.1251
        mock_apr_2020 = 0.1253
        mock_may_2020 = 0.1254
        mock_jun_2020 = 0.1253
        mock_jul_2020 = 0.1251
        mock_aug_2020 = 0.1252
        mock_sep_2020 = 0.1254
        mock_oct_2020 = 0.1253
        mock_nov_2020 = 0.1254
        mock_dec_2020 = 0.1251
        mock_jan_2021 = 0.1250
        mock_feb_2021 = 0.1253
        mock_mar_2021 = 0.1254
        mock_apr_2021 = 0.1252
        mock_may_2021 = 0.1252
        mock_jun_2021 = 0.1253
        mock_jul_2021 = 0.1254
        mock_aug_2021 = 0.1250
        mock_sep_2021 = 0.1251
        mock_oct_2021 = 0.1252
        mock_nov_2021 = 0.1253
        mock_dec_2021 = 0.1254
        mock_jan_2022 = 0.1250
        mock_feb_2022 = 0.1251
        mock_mar_2022 = 0.1252
        mock_apr_2022 = 0.1253
        mock_may_2022 = 0.1254
        mock_jun_2022 = 0.1250
        mock_jul_2022 = 0.1252
        mock_aug_2022 = 0.1253
        mock_sep_2022 = 0.1251
        mock_oct_2022 = 0.1253
        mock_nov_2022 = 0.1252
        mock_dec_2022 = 0.1254


        # Check specific months
        self.assertAlmostEqual(result["Mar 2020"], mock_mar_2020, places=3)
        self.assertAlmostEqual(result["Apr 2020"], mock_apr_2020, places=3)
        self.assertAlmostEqual(result["May 2020"], mock_may_2020, places=3)
        self.assertAlmostEqual(result["Jun 2020"], mock_jun_2020, places=3)
        self.assertAlmostEqual(result["Jul 2020"], mock_jul_2020, places=3)
        self.assertAlmostEqual(result["Aug 2020"], mock_aug_2020, places=3)
        self.assertAlmostEqual(result["Sep 2020"], mock_sep_2020, places=3)
        self.assertAlmostEqual(result["Oct 2020"], mock_oct_2020, places=3)
        self.assertAlmostEqual(result["Nov 2020"], mock_nov_2020, places=3)
        self.assertAlmostEqual(result["Dec 2020"], mock_dec_2020, places=3)
        # 2021
        self.assertAlmostEqual(result["Jan 2021"], mock_jan_2021, places=3)
        self.assertAlmostEqual(result["Feb 2021"], mock_feb_2021, places=3)
        self.assertAlmostEqual(result["Mar 2021"], mock_mar_2021, places=3)
        self.assertAlmostEqual(result["Apr 2021"], mock_apr_2021, places=3)
        self.assertAlmostEqual(result["May 2021"], mock_may_2021, places=3)
        self.assertAlmostEqual(result["Jun 2021"], mock_jun_2021, places=3)
        self.assertAlmostEqual(result["Jul 2021"], mock_jul_2021, places=3)
        self.assertAlmostEqual(result["Aug 2021"], mock_aug_2021, places=3)
        self.assertAlmostEqual(result["Sep 2021"], mock_sep_2021, places=3)
        self.assertAlmostEqual(result["Oct 2021"], mock_oct_2021, places=3)
        self.assertAlmostEqual(result["Nov 2021"], mock_nov_2021, places=3)
        self.assertAlmostEqual(result["Dec 2021"], mock_dec_2021, places=3)
        # 2022
        self.assertAlmostEqual(result["Jan 2022"], mock_jan_2022, places=3)
        self.assertAlmostEqual(result["Feb 2022"], mock_feb_2022, places=3)
        self.assertAlmostEqual(result["Mar 2022"], mock_mar_2022, places=3)
        self.assertAlmostEqual(result["Apr 2022"], mock_apr_2022, places=3)
        self.assertAlmostEqual(result["May 2022"], mock_may_2022, places=3)
        self.assertAlmostEqual(result["Jun 2022"], mock_jun_2022, places=3)
        self.assertAlmostEqual(result["Jul 2022"], mock_jul_2022, places=3)
        self.assertAlmostEqual(result["Aug 2022"], mock_aug_2022, places=3)
        self.assertAlmostEqual(result["Sep 2022"], mock_sep_2022, places=3)
        self.assertAlmostEqual(result["Oct 2022"], mock_oct_2022, places=3)
        self.assertAlmostEqual(result["Nov 2022"], mock_nov_2022, places=3)
        self.assertAlmostEqual(result["Dec 2022"], mock_dec_2022, places=3)


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


    def test_get_polarity_by_keydate(self):
        # Call the function being tested
        keydates = {"Sat Apr 15": 0, "Fri Apr 23": 0, "Sat Mar 25": 0}
        result = get_polarity_by_keydate(keydates)

        # expected results are just the polarity as these are the only values for these dates - added in setUp
        expected_results = {
            "Sat Apr 15": 0.2272,
            "Fri Apr 23": 0.0,
            "Sat Mar 25": -0.3
        }

        # Compare the actual result with the expected result for each key date
        for keydate, expected_result in expected_results.items():
            self.assertAlmostEqual(result[keydate], expected_result, places=2)


    def test_get_polarity_by_week(self):
        # test for these 2 dates we added previosuly
        dates = ["Sat Apr 15", "Fri Apr 23"]

        # Call the function being tested
        result = get_polarity_by_week(dates)
        # tweetp1 should have polarity = 0.2272, tweetp2 has polarity 0.02 - the avg of these two is 0.1136
        # (0.0 + 0.22727) / 2

        # Calculate the expected average polarity manually
        expected_result = (0.0 + 0.22727) / 2
        print("Result: " + str(result))

        # Compare the actual result with the expected result
        self.assertAlmostEqual(result, expected_result, places=2)