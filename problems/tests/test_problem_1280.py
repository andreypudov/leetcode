import unittest

import pandas as pd
from pandas.testing import assert_frame_equal

from problems.problem_1280 import students_and_examinations


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.students = {
            "student_id": [1, 2, 13, 6],
            "student_name": ["Alice", "Bob", "John", "Alex"],
        }
        self.subjects = {
            "subject_name": ["Math", "Physics", "Programming"],
        }
        self.examinations = {
            "student_id": [1, 1, 1, 2, 1, 1, 13, 13, 13, 2, 1],
            "subject_name": [
                "Math",
                "Physics",
                "Programming",
                "Programming",
                "Physics",
                "Math",
                "Math",
                "Programming",
                "Physics",
                "Math",
                "Math",
            ],
        }
        self.expected = {
            "student_id": [1, 1, 1, 2, 2, 2, 6, 6, 6, 13, 13, 13],
            "student_name": [
                "Alice",
                "Alice",
                "Alice",
                "Bob",
                "Bob",
                "Bob",
                "Alex",
                "Alex",
                "Alex",
                "John",
                "John",
                "John",
            ],
            "subject_name": [
                "Math",
                "Physics",
                "Programming",
                "Math",
                "Physics",
                "Programming",
                "Math",
                "Physics",
                "Programming",
                "Math",
                "Physics",
                "Programming",
            ],
            "attended_exams": [
                3.0,
                2.0,
                1.0,
                1.0,
                0.0,
                1.0,
                0.0,
                0.0,
                0.0,
                1.0,
                1.0,
                1.0,
            ],
        }

    def test_students_and_examinations(self):
        actual = students_and_examinations(
            pd.DataFrame(self.students),
            pd.DataFrame(self.subjects),
            pd.DataFrame(self.examinations),
        )
        expected = pd.DataFrame(self.expected)
        assert_frame_equal(
            actual.reset_index(drop=True), expected.reset_index(drop=True)
        )
