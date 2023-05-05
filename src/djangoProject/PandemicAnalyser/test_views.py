from django.test import TestCase, Client
from unittest.mock import patch
from PandemicAnalyser.models import TweetPolarity


class ViewsIntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        TweetPolarity.objects.create(id=1, created_at='Tue Apr 07 2020', polarity=0.5)
        TweetPolarity.objects.create(id=2, created_at='Fri Jun 26 2020', polarity=-0.2)
        TweetPolarity.objects.create(id=3, created_at='Thu Jul 16 2020', polarity=0.8)

        TweetPolarity.objects.create(id=4, created_at='Sun Aug 02 2020', polarity=0.5)
        TweetPolarity.objects.create(id=5, created_at='Tue Sep 22 2020', polarity=-0.2)
        TweetPolarity.objects.create(id=6, created_at='Fri Oct 02 2020', polarity=0.8)

        TweetPolarity.objects.create(id=7, created_at='Mon Nov 09 2020', polarity=0.5)
        TweetPolarity.objects.create(id=8, created_at='Mon Nov 23 2020', polarity=-0.2)
        TweetPolarity.objects.create(id=9, created_at='Mon Feb 22 2021', polarity=0.8)

        TweetPolarity.objects.create(id=10, created_at='Mon Aug 23 2021', polarity=0.5)
        TweetPolarity.objects.create(id=11, created_at='Fri Nov 19 2021', polarity=-0.2)
        TweetPolarity.objects.create(id=12, created_at='Fri Nov 26 2021', polarity=0.8)

        TweetPolarity.objects.create(id=13, created_at='Mon Jan 31 2022', polarity=0.5)
        TweetPolarity.objects.create(id=14, created_at='Tue Mar 29 2022"', polarity=-0.2)

    @patch("PandemicAnalyser.Plots.searcher.get_yearly_html_files")
    @patch("PandemicAnalyser.Graphs.heatmap.get_monthly_heatmap")
    def test_homepage_view(self, mock_get_yearly_html_files, mock_get_monthly_heatmap):
        mock_get_yearly_html_files.return_value = ["test"]
        mock_get_monthly_heatmap.return_value = {"2020_05": "test","2020_04": "test","2020_03": "test"}

        response = self.client.get('/')

        # Check that page loads correctly
        self.assertEqual(response.status_code, 200)


        self.assertTemplateUsed(response, 'index.html')

        # Check that all values in the response context
        self.assertIn('barchart', response.context)
        self.assertIn('lineplot', response.context)
        self.assertIn('Mar2020', response.context)
        self.assertIn('Apr2020', response.context)
        self.assertIn('May2020', response.context)
        self.assertIn('Jun2020', response.context)
        self.assertIn('Jul2020', response.context)
        self.assertIn('Aug2020', response.context)
        self.assertIn('Sep2020', response.context)
        self.assertIn('Oct2020', response.context)
        self.assertIn('Nov2020', response.context)
        self.assertIn('Dec2020', response.context)
        self.assertIn('Jan2021', response.context)
        self.assertIn('Feb2021', response.context)
        self.assertIn('Mar2021', response.context)
        self.assertIn('Apr2021', response.context)
        self.assertIn('May2021', response.context)
        self.assertIn('Jun2021', response.context)
        self.assertIn('Jul2021', response.context)
        self.assertIn('Aug2021', response.context)
        self.assertIn('Sep2021', response.context)
        self.assertIn('Oct2021', response.context)
        self.assertIn('Nov2021', response.context)
        self.assertIn('Dec2021', response.context)
        self.assertIn('Jan2022', response.context)
        self.assertIn('Feb2022', response.context)
        self.assertIn('Mar2022', response.context)
        self.assertIn('Apr2022', response.context)
        self.assertIn('May2022', response.context)
        self.assertIn('Jun2022', response.context)
        self.assertIn('Jul2022', response.context)
        self.assertIn('Aug2022', response.context)
        self.assertIn('Sep2022', response.context)
        self.assertIn('Oct2022', response.context)
        self.assertIn('Nov2022', response.context)
        self.assertIn('Dec2022', response.context)



    @patch("PandemicAnalyser.Plots.searcher.get_monthly_html_files")
    def test_daily_view(self, mock_get_monthly_html_files):
        mock_get_monthly_html_files.return_value = ["<p> Test<p>"]

        response = self.client.get('/daily/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'daily.html')

        # Check that all values in the response context
        self.assertIn('Mar2020', response.context)
        self.assertIn('Apr2020', response.context)
        self.assertIn('May2020', response.context)
        self.assertIn('Jun2020', response.context)
        self.assertIn('Jul2020', response.context)
        self.assertIn('Aug2020', response.context)
        self.assertIn('Sep2020', response.context)
        self.assertIn('Oct2020', response.context)
        self.assertIn('Nov2020', response.context)
        self.assertIn('Dec2020', response.context)
        self.assertIn('Jan2021', response.context)
        self.assertIn('Feb2021', response.context)
        self.assertIn('Mar2021', response.context)
        self.assertIn('Apr2021', response.context)
        self.assertIn('May2021', response.context)
        self.assertIn('Jun2021', response.context)
        self.assertIn('Jul2021', response.context)
        self.assertIn('Aug2021', response.context)
        self.assertIn('Sep2021', response.context)
        self.assertIn('Oct2021', response.context)
        self.assertIn('Nov2021', response.context)
        self.assertIn('Dec2021', response.context)
        self.assertIn('Jan2022', response.context)
        self.assertIn('Feb2022', response.context)
        self.assertIn('Mar2022', response.context)
        self.assertIn('Apr2022', response.context)
        self.assertIn('May2022', response.context)
        self.assertIn('Jun2022', response.context)
        self.assertIn('Jul2022', response.context)
        self.assertIn('Aug2022', response.context)
        self.assertIn('Sep2022', response.context)
        self.assertIn('Oct2022', response.context)
        self.assertIn('Nov2022', response.context)



    def test_keydates_view(self):
        response = self.client.get('/keydates/')

        self.assertEqual(response.status_code, 200)  # Assuming the render function returns a valid HTTP response
        self.assertTemplateUsed(response, 'key_dates.html')

        # Check that all values in the response context
        self.assertIn('bchart', response.context)
        self.assertIn('Apr072020', response.context)
        self.assertIn('Jun262020', response.context)
        self.assertIn('Aug022020', response.context)
        self.assertIn('Sep222020', response.context)
        self.assertIn('Oct022020', response.context)
        self.assertIn('Nov092020', response.context)
        self.assertIn('Nov232020', response.context)
        self.assertIn('Feb222021', response.context)
        self.assertIn('Aug232021', response.context)
        self.assertIn('Nov192021', response.context)
        self.assertIn('Nov262021', response.context)
        self.assertIn('Jan312022', response.context)
        self.assertIn('Mar292022', response.context)

    @patch("PandemicAnalyser.Graphs.barchart.barchart_models")
    @patch("PandemicAnalyser.Predictor.logisticreg.get_lr_cm")
    def test_models_view(self, mock_barchart_models, mock_get_lr_cm):
        mock_barchart_models.return_value = "<p> Test<p>"
        mock_get_lr_cm.return_value = "<p> Test 2<p>"

        response = self.client.get('/models/')

        # Check that page loads correctly
        self.assertEqual(response.status_code, 200)

        # Check that models.html is used
        self.assertTemplateUsed(response, 'models.html')

        # Check that the barchart and confusion matrix are in the response context
        self.assertIn('barchart', response.context)
        self.assertIn('confusionmatrix', response.context)


    def test_about_view(self):
        response = self.client.get('/about/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
