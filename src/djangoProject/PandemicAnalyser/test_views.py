from django.test import TestCase, Client

class MyIntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_my_integration_scenario(self):

        # Simulate an HTTP GET request to a specific URL
        response = self.client.get('/PandemicAnalyser/models/')

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
