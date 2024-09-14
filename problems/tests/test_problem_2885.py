import unittest

import pandas as pd
from pandas.testing import assert_frame_equal

from problems.problem_2885 import renameColumns


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.students = {
            "id": [1, 2, 3, 4, 5],
            "first": ["Mason", "Ava", "Taylor", "Georgia", "Thomas"],
            "last": ["King", "Wright", "Hall", "Thompson", "Moore"],
            "age": [6, 7, 16, 18, 10],
        }
        self.expected = {
            "student_id": [1, 2, 3, 4, 5],
            "first_name": ["Mason", "Ava", "Taylor", "Georgia", "Thomas"],
            "last_name": ["King", "Wright", "Hall", "Thompson", "Moore"],
            "age_in_years": [6, 7, 16, 18, 10],
        }

    def test_renameColumns(self):
        actual = renameColumns(pd.DataFrame(self.students))
        expected = pd.DataFrame(self.expected)
        assert_frame_equal(
            actual.reset_index(drop=True), expected.reset_index(drop=True)
        )
