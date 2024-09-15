import unittest

import pandas as pd
from pandas.testing import assert_frame_equal

from problems.problem_2887 import fillMissingValues


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.products = {
            "name": ["Wristwatch", "WirelessEarbuds", "GolfClubs", "Printer"],
            "quantity": [None, None, 779, 849],
            "price": [135, 821, 9319, 3051],
        }
        self.expected = {
            "name": ["Wristwatch", "WirelessEarbuds", "GolfClubs", "Printer"],
            "quantity": [0, 0, 779, 849],
            "price": [135, 821, 9319, 3051],
        }

    def test_fillMissingValues(self):
        actual = fillMissingValues(pd.DataFrame(self.products))
        expected = pd.DataFrame(self.expected)
        assert_frame_equal(
            actual.reset_index(drop=True),
            expected.reset_index(drop=True),
            check_dtype=False,
        )
