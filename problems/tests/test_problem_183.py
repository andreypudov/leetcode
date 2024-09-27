import unittest

import pandas as pd
from pandas.testing import assert_frame_equal

from problems.problem_183 import find_customers


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.customers = {
            "id": [1, 2, 3, 4],
            "name": ["Joe", "Henry", "Sam", "Max"],
        }
        self.orders = {
            "id": [1, 2],
            "customerId": [3, 1],
        }
        self.expected = {
            "Customers": ["Henry", "Max"],
        }

    def test_find_customers(self):
        actual = find_customers(
            pd.DataFrame(self.customers), pd.DataFrame(self.orders)
        )
        expected = pd.DataFrame(self.expected)
        assert_frame_equal(
            actual.reset_index(drop=True), expected.reset_index(drop=True)
        )
