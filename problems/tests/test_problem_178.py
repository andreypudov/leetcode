import unittest

import pandas as pd
from pandas.testing import assert_frame_equal

from problems.problem_178 import order_scores


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.scores = {
            "id": [1, 2, 3, 4, 5, 6],
            "score": [3.50, 3.65, 4.00, 3.85, 4.00, 3.65],
        }
        self.expected = {
            "score": [4.00, 4.00, 3.85, 3.65, 3.65, 3.50],
            "rank": [1.0, 1.0, 2.0, 3.0, 3.0, 4.0],
        }

    def test_order_scores(self):
        actual = order_scores(pd.DataFrame(self.scores))
        expected = pd.DataFrame(self.expected)
        assert_frame_equal(
            actual.reset_index(drop=True), expected.reset_index(drop=True)
        )
