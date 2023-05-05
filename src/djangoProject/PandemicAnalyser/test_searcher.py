import unittest
from unittest.mock import patch
from django.test import TestCase
import os

from PandemicAnalyser.Plots.searcher import *


class SearcherTestCase(TestCase):


    #mock the open and listdir functions' return values
    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data='This is a test')
    @patch('os.listdir', return_value=[])
    def test_get_monthly_html_files_nonexisting(self, mock_listdir, mock_open): # check that non-existing files are not called
        directory = '/path/to/directory'
        expected_result = []

        result = get_monthly_html_files(directory)

        self.assertEqual(result, expected_result)
        mock_listdir.assert_called()
        mock_open.assert_not_called()


    #mock the open and listdir functions' return values
    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data='This is a test')
    @patch('os.listdir', return_value=['AllChart1.html', 'AllPlot1.html'])
    def test_get_yearly_html_files(self, mock_listdir, mock_open):
        directory = '/path/to/directory'
        expected_result = ['This is a test', 'This is a test']

        result = get_yearly_html_files(directory)

        self.assertEqual(result, expected_result)
        mock_listdir.assert_called()
        mock_open.assert_any_call(os.path.join(directory, 'AllChart1.html'), 'r')
        mock_open.assert_any_call(os.path.join(directory, 'AllPlot1.html'), 'r')

    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data='This is a test')
    @patch('os.listdir', return_value=[])
    def test_get_yearly_html_files_nonexisting(self, mock_listdir, mock_open):
        directory = '/path/to/directory'
        expected_result = []

        result = get_yearly_html_files(directory)

        self.assertEqual(result, expected_result)
        mock_listdir.assert_called()
        mock_open.assert_not_called()



    #mock the open and listdir functions' return values
    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data='This is a test')
    @patch('os.listdir', return_value=['2020_03.html', '2020_04.html'])
    def test_get_html_heatmap(self, mock_listdir, mock_open):
        directory = '/path/to/directory'
        expected_result = ['This is a test', 'This is a test']

        result = get_html_heatmap(directory)

        self.assertEqual(result, expected_result)
        mock_listdir.assert_called()
        mock_open.assert_any_call(os.path.join(directory, '2020_03.html'), 'r')
        mock_open.assert_any_call(os.path.join(directory, '2020_04.html'), 'r')

    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data='This is a test')
    @patch('os.listdir', return_value=[])
    def test_get_html_heatmap_nonexisting(self, mock_listdir, mock_open):
        directory = '/path/to/directory'
        expected_result = []

        result = get_html_heatmap(directory)

        self.assertEqual(result, expected_result)
        mock_listdir.assert_called()
        mock_open.assert_not_called()



    # when open function is called and file is read using the mocked open function, '<html>mocked data</html>' is returned as the contents of the file
    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data ='This is a test') # mock open file function open()
    @patch('os.listdir', return_value=['confusion_matrix_bayes.html', 'confusion_matrix_dtree.html']) # mock os.listdir function
    def test_get_html_confusion_matrix(self, mock_listdir, mock_open):
        directory = '/path/to/directory'
        expected_result = ['This is a test', 'This is a test']

        result = get_html_confusion_matrix(directory)

        self.assertEqual(result, expected_result)
        mock_listdir.assert_called()
        mock_open.assert_called_with(os.path.join(directory, 'confusion_matrix_dtree.html'), 'r')

    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data='This is a test')
    @patch('os.listdir', return_value=[])
    def test_get_html_confusion_matrix_nonexisting(self, mock_listdir, mock_open):
        directory = '/path/to/directory'
        expected_result = []

        result = get_html_confusion_matrix(directory)

        self.assertEqual(result, expected_result)
        mock_listdir.assert_called()
        mock_open.assert_not_called()


if __name__ == '__main__':
    unittest.main()
