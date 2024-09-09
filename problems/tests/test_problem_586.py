import unittest

import pandas as pd
from pandas.testing import assert_frame_equal

from problems.problem_586 import largest_orders


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.orders = {
            "order_number": [3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
            "customer_number": [5, 1, 5, 4, 6, 2, 4, 16, 3, 5, 3, 16],
        }
        self.expected = {
            "customer_number": [5],
        }

    def test_largest_orders(self):
        actual = largest_orders(pd.DataFrame(self.orders))
        expected = pd.DataFrame(self.expected)
        assert_frame_equal(actual, expected)
