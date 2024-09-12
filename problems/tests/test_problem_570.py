import unittest

import pandas as pd
from pandas.testing import assert_frame_equal

from problems.problem_570 import find_managers


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.scores = {
            "id": [101, 102, 103, 104, 105, 106],
            "name": ["John", "Dan", "James", "Amy", "Anne", "Ron"],
            "department": ["A", "A", "A", "A", "A", "B"],
            "managerId": [None, 101, 101, 101, 101, 101],
        }
        self.expected = {
            "name": ["John"],
        }

    def test_find_managers(self):
        actual = find_managers(pd.DataFrame(self.scores))
        expected = pd.DataFrame(self.expected)
        print(actual)
        assert_frame_equal(
            actual.reset_index(drop=True), expected.reset_index(drop=True)
        )
