import unittest

import pandas as pd
from pandas.testing import assert_frame_equal

from problems.problem_1907 import count_salary_categories


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.scores = {
            "account_id": [3, 2, 8, 6],
            "income": [108939, 12747, 87709, 91796],
        }
        self.expected = {
            "category": ["Low Salary", "Average Salary", "High Salary"],
            "accounts_count": [1, 0, 3],
        }

    def test_count_salary_categories(self):
        actual = count_salary_categories(pd.DataFrame(self.scores))
        expected = pd.DataFrame(self.expected)
        assert_frame_equal(
            actual.reset_index(drop=True), expected.reset_index(drop=True)
        )
