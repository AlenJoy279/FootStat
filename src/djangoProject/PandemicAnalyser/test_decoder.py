from django.test import TestCase
from PandemicAnalyser.db.decoder import jsonl_to_json
from unittest.mock import patch

class DecoderTestCase(TestCase):
    def setUp(self):
        # Set up some test data
        self.test_path = "./PandemicAnalyser/tests/jsontest\\test_tweet.jsonl"
        self.test_dir = "./PandemicAnalyser/tests/jsontest"


    def test_jsonl_to_json(self):
        # Check that files are correctly added to the database and analyzed for polarity
        data = jsonl_to_json(self.test_path)
        self.assertIsInstance(data, list) # function should return the parsed json as a list
