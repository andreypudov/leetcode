import unittest

import pandas as pd
from pandas.testing import assert_frame_equal

from problems.problem_176 import second_highest_salary


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.employee = {
            "id": [1, 2, 3],
            "salary": [100, 200, 300],
        }
        self.expected = {
            "SecondHighestSalary": [200],
        }

    def test_second_highest_salary(self):
        actual = second_highest_salary(pd.DataFrame(self.employee))
        expected = pd.DataFrame(self.expected)
        assert_frame_equal(
            actual.reset_index(drop=True), expected.reset_index(drop=True)
        )
