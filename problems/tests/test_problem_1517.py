import unittest

import pandas as pd

from problems.problem_1517 import valid_emails


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.users = {
            "user_id": [1, 2, 3, 4, 5, 6, 7],
            "name": [
                "Winston",
                "Jonathan",
                "Annabelle",
                "Sally",
                "Marwan",
                "David",
                "Shapiro",
            ],
            "mail": [
                "winston@leetcode.com",
                "jonathanisgreat",
                "bella-@leetcode.com",
                "sally.come@leetcode.com",
                "quarz#2020@leetcode.com",
                "david69@gmail.com",
                ".shapo@leetcode.com",
            ],
        }
        self.expected = {
            "user_id": [1, 3, 4],
            "name": ["Winston", "Annabelle", "Sally"],
            "mail": [
                "winston@leetcode.com",
                "bella-@leetcode.com",
                "sally.come@leetcode.com",
            ],
        }

    def test_valid_emails(self):
        actual = valid_emails(pd.DataFrame(self.users))
        expected = pd.DataFrame(self.expected)
        self.assertEqual(actual.to_dict("records"), expected.to_dict("records"))
