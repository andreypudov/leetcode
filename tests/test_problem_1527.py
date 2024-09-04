import unittest

import pandas as pd

from problems.problem_1527 import find_patients


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.patients = {
            "patient_id": [1, 2, 3, 4, 5],
            "patient_name": [
                "Daniel",
                "Alice",
                "Bob",
                "George",
                "Alain",
            ],
            "conditions": [
                "YFEV COUGH",
                "",
                "DIAB100 MYOP",
                "ACNE DIAB100",
                "DIAB201",
            ],
        }
        self.expected = {
            "patient_id": [3, 4],
            "patient_name": [
                "Bob",
                "George",
            ],
            "conditions": [
                "DIAB100 MYOP",
                "ACNE DIAB100",
            ],
        }

    def test_find_patients(self):
        actual = find_patients(pd.DataFrame(self.patients))
        expected = pd.DataFrame(self.expected)
        self.assertEqual(actual.to_dict("records"), expected.to_dict("records"))
