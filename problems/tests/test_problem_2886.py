import unittest

import pandas as pd
from pandas.testing import assert_frame_equal

from problems.problem_2886 import changeDatatype


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.students = {
            "id": [1, 2],
            "name": ["Ava", "Kate"],
            "age": [6, 15],
            "grade": [73.0, 87.0],
        }
        self.expected = {
            "id": [1, 2],
            "name": ["Ava", "Kate"],
            "age": [6, 15],
            "grade": [73, 87],
        }

    def test_changeDatatype(self):
        actual = changeDatatype(pd.DataFrame(self.students))
        expected = pd.DataFrame(self.expected)
        assert_frame_equal(
            actual.reset_index(drop=True), expected.reset_index(drop=True)
        )
