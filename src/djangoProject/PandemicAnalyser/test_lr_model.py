import os

import numpy
from django.test import TestCase
import PandemicAnalyser.Predictor.logisticreg as lr


class LRModelTestCase(TestCase):

    def test_lr_dependencies_exists(self):
        project_dir = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(project_dir, 'Predictor', 'LRmodel.sav')
        train_path = os.path.join(project_dir, 'Predictor', 'train.json')
        test_path = os.path.join(project_dir, 'Predictor', 'test.json')
        self.assertTrue(os.path.exists(model_path))
        self.assertTrue(os.path.exists(train_path))
        self.assertTrue(os.path.exists(test_path))

    def test_dataframes(self):
        test_matrices = lr.create_dfs_matrices("PandemicAnalyser/tests/lrtrain.json",
                                               "PandemicAnalyser/tests/lrtest.json")
        self.assertTrue(len(test_matrices) == 5)

    def test_labelling(self):
        test_matrices = lr.create_dfs_matrices("PandemicAnalyser/tests/lrtrain.json",
                                               "PandemicAnalyser/tests/lrtest.json")

        sentiment_values = test_matrices[0].label.unique()
        self.assertTrue(len(sentiment_values == 2))
        self.assertTrue(sentiment_values[0] == 1 and sentiment_values[1] == 0)

    def test_training_matrices(self):
        test_matrices = lr.create_dfs_matrices("PandemicAnalyser/tests/lrtrain.json",
                                               "PandemicAnalyser/tests/lrtest.json")[-1]

        self.assertTrue(len(test_matrices) == 4)


