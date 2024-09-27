import unittest

import pandas as pd
from pandas.testing import assert_frame_equal

from problems.problem_1873 import calculate_special_bonus


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.employees = {
            "employee_id": [2, 3, 7, 8, 9],
            "name": ["Meir", "Michael", "Addilyn", "Juan", "Kannon"],
            "salary": [3000, 3800, 7400, 6100, 7700],
        }
        self.expected = {
            "employee_id": [2, 3, 7, 8, 9],
            "bonus": [0, 0, 7400, 0, 7700],
        }

    def test_calculate_special_bonus(self):
        actual = calculate_special_bonus(pd.DataFrame(self.employees))
        expected = pd.DataFrame(self.expected)
        assert_frame_equal(actual, expected)
