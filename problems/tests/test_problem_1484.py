import unittest

import pandas as pd
from pandas.testing import assert_frame_equal

from problems.problem_1484 import categorize_products


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.activities = {
            "sell_date": [
                pd.Timestamp("2020-05-30"),
                pd.Timestamp("2020-06-01"),
                pd.Timestamp("2020-06-02"),
                pd.Timestamp("2020-05-30"),
                pd.Timestamp("2020-06-01"),
                pd.Timestamp("2020-06-02"),
                pd.Timestamp("2020-05-30"),
            ],
            "product": [
                "Headphone",
                "Pencil",
                "Mask",
                "Basketball",
                "Bible",
                "Mask",
                "T-Shirt",
            ],
        }
        self.expected = {
            "sell_date": [
                pd.Timestamp("2020-05-30"),
                pd.Timestamp("2020-06-01"),
                pd.Timestamp("2020-06-02"),
            ],
            "num_sold": [3, 2, 1],
            "products": [
                "Basketball,Headphone,T-Shirt",
                "Bible,Pencil",
                "Mask",
            ],
        }

    def test_categorize_products(self):
        actual = categorize_products(pd.DataFrame(self.activities))
        expected = pd.DataFrame(self.expected)
        assert_frame_equal(actual, expected)
