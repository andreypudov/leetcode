import unittest

import pandas as pd

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
            "price": [95, 100, 105, 70, 80],
        }

    def test_rearrange_products_table(self):
        actual = rearrange_products_table(pd.DataFrame(self.products))
        expected = pd.DataFrame(self.expected)
        print(actual)
        self.assertEqual(actual.to_dict("records"), expected.to_dict("records"))
