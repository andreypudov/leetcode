import unittest

import pandas as pd

from problems.problem_1757 import find_products


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.products = {
            "product_id": [0, 1, 2, 3, 4],
            "low_fats": ["Y", "Y", "N", "Y", "N"],
            "recyclable": ["N", "Y", "Y", "Y", "N"],
        }
        self.expected = {
            "product_id": [1, 3],
        }

    def test_find_products(self):
        actual = find_products(pd.DataFrame(self.products))
        expected = pd.DataFrame(self.expected)
        self.assertEqual(actual.to_dict("records"), expected.to_dict("records"))
