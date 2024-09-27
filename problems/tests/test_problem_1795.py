import unittest

import pandas as pd
from pandas.testing import assert_frame_equal

from problems.problem_1795 import rearrange_products_table


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.products = {
            "product_id": [0, 1],
            "store1": [95, 70],
            "store2": [100, None],
            "store3": [105, 80],
        }
        self.expected = {
            "product_id": [0, 0, 0, 1, 1],
            "store": ["store1", "store2", "store3", "store1", "store3"],
            "price": [95.0, 100.0, 105.0, 70.0, 80.0],
        }

    def test_rearrange_products_table(self):
        actual = rearrange_products_table(pd.DataFrame(self.products))
        expected = pd.DataFrame(self.expected)
        assert_frame_equal(
            actual.reset_index(drop=True), expected.reset_index(drop=True)
        )
