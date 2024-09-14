import unittest

import pandas as pd
from pandas.testing import assert_frame_equal

from problems.problem_2881 import createBonusColumn


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.employees = {
            "name": [
                "Piper",
                "Grace",
                "Georgia",
                "Willow",
                "Finn",
                "Thomas",
            ],
            "salary": [4548, 28150, 1103, 6593, 74576, 24433],
        }
        self.expected = {
            "name": [
                "Piper",
                "Grace",
                "Georgia",
                "Willow",
                "Finn",
                "Thomas",
            ],
            "salary": [4548, 28150, 1103, 6593, 74576, 24433],
            "bonus": [9096, 56300, 2206, 13186, 149152, 48866],
        }

    def test_createBonusColumn(self):
        actual = createBonusColumn(pd.DataFrame(self.employees))
        expected = pd.DataFrame(self.expected)
        assert_frame_equal(
            actual.reset_index(drop=True), expected.reset_index(drop=True)
        )
