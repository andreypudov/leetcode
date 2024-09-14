import unittest

import pandas as pd
from pandas.testing import assert_frame_equal

from problems.problem_2880 import selectData


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.students = {
            "student_id": [101, 53, 128, 3],
            "name": [
                "Ulysses",
                "William",
                "Henry",
                "Henry",
            ],
            "age": [13, 10, 6, 11],
        }
        self.expected = {
            "name": [
                "Ulysses",
            ],
            "age": [13],
        }

    def test_selectData(self):
        actual = selectData(pd.DataFrame(self.students))
        expected = pd.DataFrame(self.expected)
        assert_frame_equal(
            actual.reset_index(drop=True), expected.reset_index(drop=True)
        )
