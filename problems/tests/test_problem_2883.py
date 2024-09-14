import unittest

import pandas as pd
from pandas.testing import assert_frame_equal

from problems.problem_2883 import dropMissingData


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.students = {
            "student_id": [32, 217, 779, 849],
            "name": ["Piper", None, "Georgia", "Willow"],
            "age": [5, 19, 20, 14],
        }
        self.expected = {
            "student_id": [32, 779, 849],
            "name": ["Piper", "Georgia", "Willow"],
            "age": [5, 20, 14],
        }

    def test_dropMissingData(self):
        actual = dropMissingData(pd.DataFrame(self.students))
        expected = pd.DataFrame(self.expected)
        assert_frame_equal(
            actual.reset_index(drop=True), expected.reset_index(drop=True)
        )
