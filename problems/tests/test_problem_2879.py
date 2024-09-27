import unittest

import pandas as pd
from pandas.testing import assert_frame_equal

from problems.problem_2879 import selectFirstRows


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.employees = {
            "employee_id": [3, 90, 9, 60, 49, 43],
            "name": [
                "Bob",
                "Alice",
                "Tatiana",
                "Annabelle",
                "Jonathan",
                "Khaled",
            ],
            "department": [
                "Operations",
                "Sales",
                "Engineering",
                "InformationTechnology",
                "HumanResources",
                "Administration",
            ],
            "salary": [48675, 11096, 33805, 37678, 23793, 40454],
        }
        self.expected = {
            "employee_id": [3, 90, 9],
            "name": [
                "Bob",
                "Alice",
                "Tatiana",
            ],
            "department": [
                "Operations",
                "Sales",
                "Engineering",
            ],
            "salary": [48675, 11096, 33805],
        }

    def test_selectFirstRows(self):
        actual = selectFirstRows(pd.DataFrame(self.employees))
        expected = pd.DataFrame(self.expected)
        assert_frame_equal(
            actual.reset_index(drop=True), expected.reset_index(drop=True)
        )
