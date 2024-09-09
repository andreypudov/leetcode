import unittest

import pandas as pd
from pandas.testing import assert_frame_equal

from problems.problem_1378 import replace_employee_id


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.employees = {
            "id": [1, 7, 11, 90, 3],
            "name": ["Alice", "Bob", "Meir", "Winston", "Jonathan"],
        }
        self.employee_uni = {
            "id": [3, 11, 90],
            "unique_id": [1, 2, 3],
        }
        self.expected = {
            "unique_id": [float("nan"), float("nan"), 2, 3, 1],
            "name": ["Alice", "Bob", "Meir", "Winston", "Jonathan"],
        }

    def test_replace_employee_id(self):
        actual = replace_employee_id(
            pd.DataFrame(self.employees), pd.DataFrame(self.employee_uni)
        )
        expected = pd.DataFrame(self.expected)
        assert_frame_equal(actual, expected)
