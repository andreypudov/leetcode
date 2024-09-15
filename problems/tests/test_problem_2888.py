import unittest

import pandas as pd
from pandas.testing import assert_frame_equal

from problems.problem_2888 import concatenateTables


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.df1 = {
            "student_id": [1, 2, 3, 4],
            "name": ["Mason", "Ava", "Taylor", "Georgia"],
            "age": [8, 6, 15, 17],
        }
        self.df2 = {
            "student_id": [5, 6],
            "name": ["Leo", "Alex"],
            "age": [7, 7],
        }
        self.expected = {
            "student_id": [1, 2, 3, 4, 5, 6],
            "name": ["Mason", "Ava", "Taylor", "Georgia", "Leo", "Alex"],
            "age": [8, 6, 15, 17, 7, 7],
        }

    def test_concatenateTables(self):
        actual = concatenateTables(
            pd.DataFrame(self.df1), pd.DataFrame(self.df2)
        )
        expected = pd.DataFrame(self.expected)
        assert_frame_equal(
            actual.reset_index(drop=True),
            expected.reset_index(drop=True),
        )
