import unittest

import pandas as pd

from problems.problem_196 import delete_duplicate_emails


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.person = {
            "id": [1, 2, 3],
            "email": ["john@example.com", "bob@example.com", "john@example.com"],
        }
        self.expected = {
            "id": [1, 2],
            "email": ["john@example.com", "bob@example.com"],
        }

    def test_delete_duplicate_emails(self):
        actual = pd.DataFrame(self.person)
        delete_duplicate_emails(actual)
        expected = pd.DataFrame(self.expected)
        self.assertEqual(actual.to_dict("records"), expected.to_dict("records"))
