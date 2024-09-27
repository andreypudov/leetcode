import unittest

import pandas as pd
from pandas.testing import assert_frame_equal

from problems.problem_2882 import dropDuplicateEmails


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.customers = {
            "customer_id": [1, 2, 3, 4, 5, 6],
            "name": ["Ella", "David", "Zachary", "Alice", "Finn", "Violet"],
            "email": [
                "emily@example.com",
                "michael@example.com",
                "sarah@example.com",
                "john@example.com",
                "john@example.com",
                "alice@example.com",
            ],
        }
        self.expected = {
            "customer_id": [1, 2, 3, 4, 6],
            "name": ["Ella", "David", "Zachary", "Alice", "Violet"],
            "email": [
                "emily@example.com",
                "michael@example.com",
                "sarah@example.com",
                "john@example.com",
                "alice@example.com",
            ],
        }

    def test_dropDuplicateEmails(self):
        actual = dropDuplicateEmails(pd.DataFrame(self.customers))
        expected = pd.DataFrame(self.expected)
        assert_frame_equal(
            actual.reset_index(drop=True), expected.reset_index(drop=True)
        )
