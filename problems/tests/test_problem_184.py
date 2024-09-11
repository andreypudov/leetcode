import unittest

import pandas as pd
from pandas.testing import assert_frame_equal

from problems.problem_184 import department_highest_salary


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.employee = {
            "id": [1, 2, 3, 4, 5],
            "name": ["Joe", "Jim", "Henry", "Sam", "Max"],
            "salary": [70000, 90000, 80000, 60000, 90000],
            "departmentId": [1, 1, 2, 2, 1],
        }
        self.department = {
            "id": [1, 2],
            "name": ["IT", "Sales"],
        }
        self.expected = {
            "Department": ["IT", "IT", "Sales"],
            "Employee": [
                "Jim",
                "Max",
                "Henry",
            ],
            "Salary": [90000, 90000, 80000],
        }

    def test_department_highest_salary(self):
        actual = department_highest_salary(
            pd.DataFrame(self.employee), pd.DataFrame(self.department)
        )
        expected = pd.DataFrame(self.expected)
        print(actual)
        assert_frame_equal(
            actual.reset_index(drop=True), expected.reset_index(drop=True)
        )
