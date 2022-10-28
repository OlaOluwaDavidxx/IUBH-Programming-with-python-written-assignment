from unittest import TestCase
import pandas as pd
from middleware.evaluate_score import squared_error
from controllers.load_data_controller import load_data
from utils.utils import find_ideal


class TestFunctions(TestCase):
    """Test for some functions."""

    def test_squared_error(self):
        """Test for squared error"""
        self.assertEqual(squared_error(2, 4), 4)

    def test_load_data(self):
        """Test for load data function"""
        test = pd.read_csv("../dataset/test.csv")
        result = test.equals(load_data("../dataset/test.csv"))
        self.assertEqual(result, True)

    def test_find_ideal(self):
        """Test to find ideal function."""
        train = pd.read_csv("../dataset/train.csv")
        ideal = pd.read_csv("../dataset/ideal.csv")

        train.columns = [f"{column}_train" if column != "x" else "x" for column in train.columns]

        self.assertEqual(find_ideal(ideal, train, "y1_train"), "y10")
        self.assertEqual(find_ideal(ideal, train, "y2_train"), "y22")
        self.assertEqual(find_ideal(ideal, train, "y3_train"), "y21")
        self.assertEqual(find_ideal(ideal, train, "y4_train"), "y2")
