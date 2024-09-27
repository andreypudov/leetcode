import unittest

import pandas as pd
from pandas.testing import assert_frame_equal

from problems.problem_2877 import createDataframe


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.student_data = [
            [1, 15],
            [2, 11],
            [3, 11],
            [4, 20],
        ]
        self.expected = {
            "student_id": [1, 2, 3, 4],
            "age": [15, 11, 11, 20],
        }

    def test_createDataframe(self):
        actual = createDataframe(self.student_data)
        expected = pd.DataFrame(self.expected)
        assert_frame_equal(
            actual.reset_index(drop=True), expected.reset_index(drop=True)
        )
