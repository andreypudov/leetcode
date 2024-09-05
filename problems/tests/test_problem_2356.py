import unittest

import pandas as pd

from problems.problem_2356 import count_unique_subjects


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.teacher = {
            "teacher_id": [1, 1, 1, 2, 2, 2, 2],
            "subject_id": [2, 2, 3, 1, 2, 3, 4],
            "dept_id": [3, 4, 3, 1, 1, 1, 1],
        }
        self.expected = {
            "teacher_id": [1, 2],
            "cnt": [2, 4],
        }

    def test_count_unique_subjects(self):
        actual = count_unique_subjects(pd.DataFrame(self.teacher))
        expected = pd.DataFrame(self.expected)
        print(actual)
        self.assertEqual(actual.to_dict("records"), expected.to_dict("records"))
