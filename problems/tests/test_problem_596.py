import unittest

import pandas as pd

from problems.problem_596 import find_classes


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.courses = {
            "student": ["A", "B", "C", "D", "E", "F", "G", "H", "I"],
            "class": [
                "Math",
                "English",
                "Math",
                "Biology",
                "Math",
                "Computer",
                "Math",
                "Math",
                "Math",
            ],
        }
        self.expected = {
            "class": ["Math"],
        }

    def test_find_classes(self):
        actual = find_classes(pd.DataFrame(self.courses))
        expected = pd.DataFrame(self.expected)
        self.assertEqual(actual.to_dict("records"), expected.to_dict("records"))
